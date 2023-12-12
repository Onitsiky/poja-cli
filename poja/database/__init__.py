import poja.sed as sed
import os

function_snapstart_enabled = """AutoPublishAlias: live
    SnapStart:
      ApplyOn: PublishedVersions"""


def set_postgres(with_database, temp, exclude):
    if with_database == "postgres":
        postgres_env_vars = """DATABASE_URL: !Sub '{{resolve:ssm:/<?app-name>/${Env}/db/url}}'
        DATABASE_USERNAME: !Sub '{{resolve:ssm:/<?app-name>/${Env}/db/username}}'
        DATABASE_PASSWORD: !Sub '{{resolve:ssm:/<?app-name>/${Env}/db/password}}'"""
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
        upsert_constraint_dummy = "on conflict on constraint dummy_pk do nothing;"
        upsert_constraint_dummy_uuid = (
            "on conflict on constraint dummy_uuid_pk do nothing;"
        )
        function_snapstart = function_snapstart_enabled
    else:
        postgres_env_vars = ""
        upsert_constraint_dummy = ";"
        postgres_configure_it_properties = ""
        postgres_start_container = ""
        upsert_constraint_dummy_uuid = ";"
        function_snapstart = "<?function-snapstart>"
        os.remove("%s/.github/workflows/cd-storage-database.yml" % temp)
        os.remove("%s/cf-stacks/storage-database-stack.yml" % temp)
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
    sed.find_replace(temp, "<?function-snapstart>", function_snapstart, exclude)


def set_sqlite(with_database, package_full_name, temp, exclude):
    if with_database == "sqlite":
        efs_mount_point = "/mnt/efs"
        sqlite_env_vars = """DRIVERCLASSNAME: org.sqlite.JDBC
        SPRING_JPA_DATABASEPLATFORM: %s.repository.conf.SqliteDialect
        DATABASE_URL: jdbc:sqlite:%s/sqlite-data:db?cache=shared
        DATABASE_USERNAME: sa
        DATABASE_PASSWORD: sa""" % (
            package_full_name,
            efs_mount_point,
        )
        sqlite_configure_it_properties = (
            "new SqliteConf().configureProperties(registry);"
        )
        function_fs_configs = (
            """FileSystemConfigs:
        - Arn: !Sub '{{resolve:ssm:/<?app-name>/${Env}/efs/access-point/arn}}'
          LocalMountPath: %s"""
            % efs_mount_point
        )
        function_snapstart = ""
    else:
        sqlite_env_vars = ""
        sqlite_configure_it_properties = ""
        os.remove(temp + "/.github/workflows/cd-storage-efs.yml")
        os.remove(temp + "/cf-stacks/storage-efs-stack.yml")
        function_fs_configs = ""
        function_snapstart = function_snapstart_enabled

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
    sed.find_replace(temp, "<?function-snapstart>", function_snapstart, exclude)
