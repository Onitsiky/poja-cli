import fire
import poja.mygit as mygit
import shutil
import poja.sed as sed

GIT_URL = "https://github.com/hei-school/poja"
GIT_TAG = "v1.0.0"


def gen(app_name, region, ssm_sg_id, ssm_subnet1_id, ssm_subnet2_id, output_dir=None):
    if output_dir is None:
        output_dir = app_name

    temp_dir = mygit.checkout(GIT_URL, GIT_TAG, no_git=True)
    exclude = "*.jar"
    sed.find_replace(temp_dir, "<?app-name>", app_name, exclude)
    sed.find_replace(temp_dir, "<?aws-region>", region, exclude)
    sed.find_replace(temp_dir, "<?ssm-param-sg-id>", ssm_sg_id, exclude)
    sed.find_replace(temp_dir, "<?ssm-param-name-subnet1-id>", ssm_subnet1_id, exclude)
    sed.find_replace(temp_dir, "<?ssm-param-name-subnet2-id>", ssm_subnet2_id, exclude)

    shutil.copytree(temp_dir, output_dir, dirs_exist_ok=True)
    return output_dir
