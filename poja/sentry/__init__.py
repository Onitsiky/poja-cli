import poja.sed as sed


def set_sentry(dsn, dir, exclude):

    sentry_deps = """
    implementation 'io.sentry:sentry-spring-boot-starter-jakarta:7.4.0'
    <?java-deps>
    """
    sentry_env_vars = f"""
        SENTRY_DSN: !Sub '{{{{resolve:ssm:{dsn}}}}}'
        SENTRY_ENVIRONMENT: !Ref Env
        <?java-env-vars>
    """
    sentry_test_env = """
        registry.add("sentry.dsn", () -> "https://public@sentry.example.com/1");
        registry.add("sentry.environment", () -> "dummy");
    """

    sed.find_replace(dir, "<?sentry-test-env>", sentry_test_env, exclude)
    sed.find_replace(dir, "<?java-deps>", sentry_deps, exclude)
    sed.find_replace(dir, "<?java-env-vars>", sentry_env_vars, exclude)
