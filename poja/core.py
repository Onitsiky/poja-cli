import poja.mygit as mygit
import shutil
import poja.sed as sed
from poja.myrich import print_title, print_normal, print_banner
from poja.version import get_version
import yaml

GIT_URL = "https://github.com/hei-school/poja"
GIT_TAG = "v1.0.0"


def gen(app_name, region, ssm_sg_id, ssm_subnet1_id, ssm_subnet2_id, output_dir=None):
    if output_dir is None:
        output_dir = app_name

    print_banner("POJA v" + get_version())

    print_title("Checkout base repository...")
    print_normal("git_url=%s" % GIT_URL)
    print_normal("git_tag=%s" % GIT_TAG)
    temp_dir = mygit.checkout(GIT_URL, GIT_TAG, no_git=True)
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

    print_title("Save conf..")
    save_conf(temp_dir, app_name, region, ssm_sg_id, ssm_subnet1_id, ssm_subnet2_id)
    print_normal("poja.yml")

    print_title("Copy to output dir..")
    shutil.copytree(temp_dir, output_dir, dirs_exist_ok=True)

    print_title("... all done!")


def save_conf(temp_dir, app_name, region, ssm_sg_id, ssm_subnet1_id, ssm_subnet2_id):
    conf = {
        "cli_version": get_version(),
        "app_name": app_name,
        "region": region,
        "ssm_sg_id": ssm_sg_id,
        "ssm_subnet1_id": ssm_subnet1_id,
        "ssm_subnet2_id": ssm_subnet2_id,
    }
    with open(temp_dir + "/poja.yml", "w") as file:
        yaml.dump(conf, file)
