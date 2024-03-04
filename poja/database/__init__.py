import poja.sed as sed
import os


def set_postgres(
    with_database,
    aurora_min_capacity,
    aurora_max_capacity,
    aurora_scale_point,
    aurora_sleep,
    aurora_auto_pause,
    database_non_root_username,
    database_non_root_password,
    temp,
    exclude,
):
    if with_database == "postgres":
        postgres_env_vars = f"""SPRING_DATASOURCE_URL: !Sub '{{{{resolve:ssm:/<?app-name>/${{Env}}/db/url}}}}'
        SPRING_DATASOURCE_USERNAME: !Sub '{{{{resolve:ssm:{'/<?app-name>/${Env}/db/username' if database_non_root_username is None else database_non_root_username}}}}}'
        SPRING_DATASOURCE_PASSWORD: !Sub '{{{{resolve:ssm:{'/<?app-name>/${Env}/db/password' if database_non_root_password is None else database_non_root_password}}}}}'"""
        upsert_constraint_dummy = "on conflict on constraint dummy_pk do nothing;"
        upsert_constraint_dummy_uuid = (
            "on conflict on constraint dummy_uuid_pk do nothing;"
        )
    else:
        postgres_env_vars = ""
        upsert_constraint_dummy = ";"
        postgres_configure_it_properties = ""
        postgres_start_container = ""
        upsert_constraint_dummy_uuid = ";"
        os.remove(f"{temp}/.github/workflows/cd-storage-database.yml")
        os.remove(f"{temp}/cf-stacks/storage-database-stack.yml")

    if with_database == "postgres" or with_database == "non-poja-managed-postgres":
        postgres_start_container = """private static final PostgresConf POSTGRES_CONF = new PostgresConf();
  @BeforeAll
  static void beforeAll() {
    POSTGRES_CONF.start();
    getRuntime()
        // Do _not_ stop postgresTest in afterAll as it is shared between multiple subclasses of
        // FacadeTest.
        // Doing so might cause some subclasses to stop it while other ones are still using it!
        .addShutdownHook(new Thread(POSTGRES_CONF::stop));
  }"""
        postgres_configure_it_properties = (
            "POSTGRES_CONF.configureProperties(registry);"
        )

    if (
        aurora_min_capacity is not None
        and aurora_max_capacity is not None
        and aurora_scale_point is not None
        and aurora_sleep is not None
    ):
        if aurora_min_capacity <= aurora_max_capacity:
            aurora_capacity_conf = f"""MaxCapacity: {aurora_max_capacity}
        MinCapacity: {aurora_min_capacity}
        SecondsBeforeTimeout: {aurora_scale_point}
        AutoPause: {aurora_auto_pause}
        SecondsUntilAutoPause: !If [ IsProdEnv, {aurora_sleep}, !Ref ProdDbClusterTimeout]
            """
        else:
            raise ValueError(
                "aurora_min_capacity value must be less than or equal to aurora_max_capacity"
            )
    else:
        aurora_capacity_conf = f"SecondsUntilAutoPause: !If [ IsProdEnv, {aurora_sleep}, !Ref ProdDbClusterTimeout]"

    sed.find_replace(
        temp,
        "<?postgres-env-vars>",
        postgres_env_vars,
        exclude,
    )
    sed.find_replace(
        temp,
        "<?postgres-start-container>",
        postgres_start_container,
        exclude,
    )
    sed.find_replace(
        temp,
        "<?postgres-configure-it-properties>",
        postgres_configure_it_properties,
        exclude,
    )
    sed.find_replace(
        temp, "<?upsert-constraint-dummy>", upsert_constraint_dummy, exclude
    )
    sed.find_replace(
        temp, "<?upsert-constraint-dummy-uuid>", upsert_constraint_dummy_uuid, exclude
    )
    sed.find_replace(temp, "<?db-scaling-capacities>", aurora_capacity_conf, exclude)


def set_sqlite(with_database, temp, exclude):
    if with_database == "sqlite":
        efs_mount_point = "/mnt/efs"
        sqlite_env_vars = f"""DRIVERCLASSNAME: org.sqlite.JDBC
        SPRING_JPA_DATABASEPLATFORM: org.hibernate.community.dialect.SQLiteDialect
        SPRING_DATASOURCE_URL: jdbc:sqlite:{efs_mount_point}/sqlite-data:db?cache=shared
        SPRING_DATASOURCE_USERNAME: sa
        SPRING_DATASOURCE_PASSWORD: sa"""
        sqlite_configure_it_properties = (
            "new SqliteConf().configureProperties(registry);"
        )
        function_fs_configs = (
            """FileSystemConfigs:
        - Arn: !Sub '{{resolve:ssm:/<?app-name>/${Env}/efs/access-point/arn}}'
          LocalMountPath: %s"""
            % efs_mount_point
        )
    else:
        sqlite_env_vars = ""
        sqlite_configure_it_properties = ""
        os.remove(temp + "/.github/workflows/cd-storage-efs.yml")
        os.remove(temp + "/cf-stacks/storage-efs-stack.yml")
        function_fs_configs = ""

    sed.find_replace(
        temp,
        "<?sqlite-env-vars>",
        sqlite_env_vars,
        exclude,
    )
    sed.find_replace(
        temp,
        "<?sqlite-configure-it-properties>",
        sqlite_configure_it_properties,
        exclude,
    )
    sed.find_replace(
        temp,
        "<?function-fs-configs>",
        function_fs_configs,
        exclude,
    )
