import poja.sed as sed


def set_sentry(dsn, dir, exclude):
    if dsn is None:
        raise Exception("You must specify a DSN in order to use Sentry")

    sentry_deps = """
    implementation 'io.sentry:sentry-spring-boot-starter-jakarta:7.4.0'
    <?java-deps>
    """
    sentry_env_vars = f"""
        SENTRY_DSN: {dsn}
        SENTRY_ENVIRONMENT: !Ref Env
        <?java-env-vars>
    """

    sed.find_replace(dir, "<?java-deps>", sentry_deps, exclude)
    sed.find_replace(dir, "<?java-env-vars>", sentry_env_vars, exclude)
