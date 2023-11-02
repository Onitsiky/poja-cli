import poja
from filecmp import dircmp
import os.path


def test_gen_annotator():
    output_dir = "test-poja-base"
    poja.gen(
        "poja-base",
        region="eu-west-3",
        ssm_sg_id="/poja/sg/id",
        ssm_subnet1_id="/poja/subnet/public1/id",
        ssm_subnet2_id="/poja/subnet/public2/id",
        package_full_name="com.company.base",
        output_dir=output_dir,
    )
    assert is_dir_superset_of("oracle-poja-base", output_dir)


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
