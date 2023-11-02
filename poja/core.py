import poja.mygit as mygit
import shutil
import poja.sed as sed
from poja.myrich import print_title, print_normal, print_banner
from poja.version import get_version
import yaml
import os

GIT_URL = "https://github.com/hei-school/poja"
GIT_TAG_OR_COMMIT = "00cf6c2"

DEFAULT_PACKAGE_FULL_NAME = "school.hei.poja"


def gen(
    app_name,
    region,
    ssm_sg_id,
    ssm_subnet1_id,
    ssm_subnet2_id,
    package_full_name=DEFAULT_PACKAGE_FULL_NAME,
    output_dir=None,
):
    if output_dir is None:
        output_dir = app_name

    print_banner("POJA v" + get_version())

    print_title("Checkout base repository...")
    print_normal("git_url=%s" % GIT_URL)
    print_normal("git_tag=%s" % GIT_TAG_OR_COMMIT)
    temp_dir = mygit.checkout(GIT_URL, GIT_TAG_OR_COMMIT, no_git=True)
    print_normal("temp_dir=%s" % temp_dir)

    print_title("Handle arguments...")
    exclude = "*.jar"
    print_normal("app_name")
    sed.find_replace(temp_dir, "<?app-name>", app_name, exclude)
    print_normal("region")
    sed.find_replace(temp_dir, "<?aws-region>", region, exclude)
    print_normal("ssm_sg_id")
    sed.find_replace(temp_dir, "<?ssm-param-sg-id>", ssm_sg_id, exclude)
    print_normal("ssm_subnet1_id")
    sed.find_replace(temp_dir, "<?ssm-param-name-subnet1-id>", ssm_subnet1_id, exclude)
    print_normal("ssm_subnet2_id")
    sed.find_replace(temp_dir, "<?ssm-param-name-subnet2-id>", ssm_subnet2_id, exclude)
    print_normal("package_full_name")
    sed.find_replace(temp_dir, DEFAULT_PACKAGE_FULL_NAME, package_full_name, exclude)
    set_package_dirs(temp_dir, package_full_name, "main")
    set_package_dirs(temp_dir, package_full_name, "test")

    print_title("Save conf..")
    save_conf(
        temp_dir,
        app_name,
        region,
        ssm_sg_id,
        ssm_subnet1_id,
        ssm_subnet2_id,
        package_full_name,
    )
    print_normal("poja.yml")

    print_title("Rm project-specific files..")
    print_normal("README.*")
    os.remove(temp_dir + "/README.md")

    print_title("Copy to output dir..")
    shutil.copytree(temp_dir, output_dir, dirs_exist_ok=True)

    print_title("... all done!")


def save_conf(
    temp_dir,
    app_name,
    region,
    ssm_sg_id,
    ssm_subnet1_id,
    ssm_subnet2_id,
    package_full_name,
):
    conf = {
        "cli_version": get_version(),
        "app_name": app_name,
        "region": region,
        "ssm_sg_id": ssm_sg_id,
        "ssm_subnet1_id": ssm_subnet1_id,
        "ssm_subnet2_id": ssm_subnet2_id,
        "package_full_name": package_full_name,
    }
    with open(temp_dir + "/poja.yml", "w") as file:
        yaml.dump(conf, file)


def set_package_dirs(temp_dir, package_full_name, scope):
    package_full_name_parts = package_full_name.split(".")
    if len(package_full_name_parts) != 3:
        raise Exception(
            "package_full_name must exactly have 3 parts such as com.company.base"
        )
    default_package_full_name_parts = DEFAULT_PACKAGE_FULL_NAME.split(".")
    os.rename(
        "%s/src/%s/java/%s" % (temp_dir, scope, default_package_full_name_parts[0]),
        "%s/src/%s/java/%s" % (temp_dir, scope, package_full_name_parts[0]),
    )
    os.rename(
        "%s/src/%s/java/%s/%s"
        % (
            temp_dir,
            scope,
            package_full_name_parts[0],
            default_package_full_name_parts[1],
        ),
        "%s/src/%s/java/%s/%s"
        % (temp_dir, scope, package_full_name_parts[0], package_full_name_parts[1]),
    )
    os.rename(
        "%s/src/%s/java/%s/%s/%s"
        % (
            temp_dir,
            scope,
            package_full_name_parts[0],
            package_full_name_parts[1],
            default_package_full_name_parts[2],
        ),
        "%s/src/%s/java/%s/%s/%s"
        % (
            temp_dir,
            scope,
            package_full_name_parts[0],
            package_full_name_parts[1],
            package_full_name_parts[2],
        ),
    )
