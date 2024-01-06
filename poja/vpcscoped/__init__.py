import poja.sed as sed
from poja.myrich import print_normal


def set_vpc_scoped_resources(
    with_own_vpc, ssm_sg_id, ssm_subnet1_id, ssm_subnet2_id, tmp_dir, exclude
):
    if with_own_vpc == "true":
        sed.find_replace(
            tmp_dir,
            "<?function-vpc-config>",
            """VpcConfig:
      SecurityGroupIds:
        - !Sub '{{resolve:ssm:<?ssm-param-sg-id>}}'
      SubnetIds:
        - !Sub '{{resolve:ssm:<?ssm-param-name-subnet1-id>}}'
        - !Sub '{{resolve:ssm:<?ssm-param-name-subnet2-id>}}'""",
            exclude,
        )
        sed.find_replace(
            tmp_dir,
            "<?db-subnet-group>",
            """DBSubnetGroup:
    Type: AWS::RDS::DBSubnetGroup
    Properties:
      DBSubnetGroupDescription: !Join [ '', [ Subnet group for <?app-name> , !Ref Env ] ]
      DBSubnetGroupName: !Join [ '', [ <?app-name>-, !Ref Env, -subnet-group ] ]
      SubnetIds:
        - !Sub '{{resolve:ssm:<?ssm-param-name-subnet1-id>}}'
        - !Sub '{{resolve:ssm:<?ssm-param-name-subnet2-id>}}'""",
            exclude,
        )
        sed.find_replace(
            tmp_dir,
            "<?db-subnet-group-name>",
            "DBSubnetGroupName: !Ref DBSubnetGroup",
            exclude,
        )
        sed.find_replace(
            tmp_dir,
            "<?db-sg-ids>",
            """VpcSecurityGroupIds:
        - !Sub '{{resolve:ssm:<?ssm-param-sg-id>}}'""",
            exclude,
        )

        print_normal("ssm_sg_id")
        sed.find_replace(tmp_dir, "<?ssm-param-sg-id>", ssm_sg_id, exclude)
        print_normal("ssm_subnet1_id")
        sed.find_replace(
            tmp_dir, "<?ssm-param-name-subnet1-id>", ssm_subnet1_id, exclude
        )
        print_normal("ssm_subnet2_id")
        sed.find_replace(
            tmp_dir, "<?ssm-param-name-subnet2-id>", ssm_subnet2_id, exclude
        )
    else:
        sed.find_replace(tmp_dir, "<?function-vpc-config>", "", exclude)
        sed.find_replace(tmp_dir, "<?db-sg-ids>", "", exclude)

        # TODO: Aurora Postgres v1 cannot be put inside AWS-managed network
        sed.find_replace(tmp_dir, "<?db-subnet-group>", "", exclude)
        sed.find_replace(tmp_dir, "<?db-subnet-group-name>", "", exclude)
