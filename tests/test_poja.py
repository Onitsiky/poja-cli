import platform
import poja
from poja.myos import cd_then_exec
from filecmp import dircmp
import shutil
from tempfile import TemporaryDirectory
import os.path
from pathlib import Path
from pytest import raises


def oracle_rel_path(oracle_dir_name):
    return f"tests/oracles/{oracle_dir_name}"


def test_app_name_must_be_defined():
    with raises(Exception) as e:
        poja.gen()
    assert (
        str(e.value)
        == "app_name in conf file (or --app-name as argument) must be defined"
    )


def test_poja_conf_must_use_proper_version():
    with raises(Exception) as e:
        poja.gen(poja_conf=oracle_rel_path("poja-conf-bad-version.yml"))
    assert (
        str(e.value)
        == "You must use the poja version defined in your conf file. Forgot to upgrade?"
    )


def test_base():
    output_dir = "test-poja-base"
    Path(f"{output_dir}/doc").mkdir(parents=True, exist_ok=True)
    Path(f"{output_dir}/doc/api.yml").write_text("DO NOT OVERRIDE")
    poja.gen(
        app_name="poja-base",
        region="eu-west-3",
        with_own_vpc="true",
        ssm_sg_id="/poja/sg/id",
        ssm_subnet1_id="/poja/subnet/private1/id",
        ssm_subnet2_id="/poja/subnet/private2/id",
        ses_source="lou@hei.school",
        with_database="postgres",
        package_full_name="com.company.base",
        output_dir=output_dir,
        jacoco_min_coverage="0.5",
        custom_java_deps=oracle_rel_path("custom-java-deps-justice.txt"),
        with_snapstart="true",
    )
    assert is_dir_superset_of(oracle_rel_path("oracle-poja-base"), output_dir)


def test_without_own_vpc():
    output_dir = "test-poja-base-without-own-vpc"
    poja.gen(
        app_name="poja-base",
        region="eu-west-3",
        with_own_vpc="false",
        package_full_name="com.company.base",
        with_database="postgres",
        output_dir=output_dir,
        with_gen_clients="true",
        jacoco_min_coverage="0.9",
        with_snapstart="true",
    )
    assert is_dir_superset_of(
        oracle_rel_path("oracle-poja-base-without-own-vpc"), output_dir
    )


def test_without_postgres():
    output_dir = "test-poja-base-without-postgres"
    poja.gen(
        app_name="poja-base-without-postgres",
        region="eu-west-3",
        with_own_vpc="true",
        ssm_sg_id="/poja/sg/id",
        ssm_subnet1_id="/poja/subnet/private1/id",
        ssm_subnet2_id="/poja/subnet/private2/id",
        package_full_name="com.company.base",
        with_database="non-poja-managed-postgres",
        output_dir=output_dir,
        with_gen_clients="false",
        jacoco_min_coverage="0.9",
        with_snapstart="true",
    )
    assert is_dir_superset_of(
        oracle_rel_path("oracle-poja-base-without-postgres"), output_dir
    )


def test_with_custom_java_repos_and_sqlite():
    output_dir = "test-poja-sqlite"
    poja.gen(
        app_name="poja-sqlite",
        region="eu-west-3",
        with_own_vpc="true",
        ssm_sg_id="/poja/sg/id",
        ssm_subnet1_id="/poja-sqlite/subnet/public1/id",
        ssm_subnet2_id="/poja-sqlite/subnet/public2/id",
        package_full_name="com.company.base",
        with_database="sqlite",
        custom_java_repositories=oracle_rel_path("custom-java-repositories.txt"),
        output_dir=output_dir,
        jacoco_min_coverage="0.5",
    )
    assert is_dir_superset_of(oracle_rel_path("oracle-poja-sqlite"), output_dir)
    assert oracle_tests_are_passing(output_dir)


def test_gen_with_all_cmd_args_is_equivalent_to_gen_with_poja_conf():
    oracle_dir = oracle_rel_path("oracle-poja-sqlite")
    # do NOT create tmp_dir using with-as, as Python will prematurely rm it
    tmp_dir = TemporaryDirectory()
    oracle_dir_clone = shutil.copytree(oracle_dir, tmp_dir.name, dirs_exist_ok=True)

    install_cmd = "pip install -r requirements.txt -r requirements-dev.txt && python setup.py install"
    os.system("pip uninstall -y poja && %s" % install_cmd)
    gen_cmd = "python -m poja --poja-conf poja.yml --output-dir=."
    gen_cmd_return_code = cd_then_exec(oracle_dir_clone, gen_cmd, gen_cmd)

    assert gen_cmd_return_code == 0
    assert are_dir_equals(oracle_dir, oracle_dir_clone)


def test_with_custom_java_env_vars_and_swagger_ui():
    output_dir = "test-poja-base-with-java-env-vars"
    poja.gen(
        app_name="poja-base-with-java-env-vars",
        region="eu-west-3",
        with_own_vpc="true",
        ssm_sg_id="/poja/sg/id",
        ssm_subnet1_id="/poja/subnet/private1/id",
        ssm_subnet2_id="/poja/subnet/private2/id",
        package_full_name="com.company.base",
        with_swagger_ui="true",
        with_database="postgres",
        custom_java_env_vars=oracle_rel_path("custom-java-env-vars.txt"),
        output_dir=output_dir,
        with_gen_clients="true",
        jacoco_min_coverage="0.9",
        with_snapstart="true",
    )
    assert is_dir_superset_of(
        oracle_rel_path("oracle-poja-base-with-java-env-vars"), output_dir
    )


def test_with_script_to_publish_to_npm_registry():
    output_dir = "test-poja-base-with-publication-to-npm-registry"
    poja.gen(
        app_name="poja-base-with-publication-to-npm-registry",
        region="eu-west-3",
        with_own_vpc="true",
        ssm_sg_id="/poja/sg/id",
        ssm_subnet1_id="/poja/subnet/private1/id",
        ssm_subnet2_id="/poja/subnet/private2/id",
        package_full_name="com.company.base",
        custom_java_env_vars=oracle_rel_path("custom-java-env-vars.txt"),
        output_dir=output_dir,
        jacoco_min_coverage="0.9",
        with_database="postgres",
        with_publish_to_npm_registry="true",
        with_gen_clients="true",
        ts_client_default_openapi_server_url="http://localhost",
        ts_client_api_url_env_var_name="CLIENT_API_URL",
        with_snapstart="true",
    )
    assert is_dir_superset_of(
        oracle_rel_path("oracle-poja-base-with-publication-to-npm-registry"), output_dir
    )


def are_dir_equals(dir1, dir2):
    return is_dir_superset_of(dir1, dir2) and is_dir_superset_of(dir2, dir1)


def is_dir_superset_of(superset_dir, subset_dir):
    compared = dircmp(superset_dir, subset_dir)
    print(
        "superset_only=%s, subset_only=%s, both=%s, incomparables=%s"
        % (
            compared.left_only,
            compared.right_only,
            compared.diff_files,
            compared.funny_files,
        ),
    )
    if compared.right_only or compared.diff_files or compared.funny_files:
        return False
    for subdir in compared.common_dirs:
        if not is_dir_superset_of(
            os.path.join(superset_dir, subdir), os.path.join(subset_dir, subdir)
        ):
            return False
    return True


def oracle_tests_are_passing(oracle_dir):
    if "Windows" in platform.system():
        return True
    gradlew_file = f"{oracle_dir}/gradlew"
    os.system(f"chmod +x {gradlew_file}")

    aws_env = "AWS_ACCESS_KEY_ID=dummy AWS_SECRET_ACCESS_KEY=dummy AWS_REGION=dummy"
    test_return_code = os.system(f"cd {oracle_dir} && {aws_env} ./gradlew test")

    return test_return_code == 0
