[![poja](https://snyk.io/advisor/python/poja/badge.svg)](https://snyk.io/advisor/python/poja)

POJA CLI
========

The Python CLI for maintaining a [POJA stack](https://github.com/hei-school/poja)... or dozens of them!

## General usage

1. Invoke the [POJA CLI](https://pypi.org/project/poja/) depending on the use case you want to address, see section below. We recommend prefixing your poja application names with `poja-`.
2. Commit changes and push them to Github.
3. Define the Github secrets for deploying into your AWS prod and preprod accounts: `PROD_AWS_ACCESS_KEY_ID`, `PROD_AWS_SECRET_ACCESS_KEY`, `PREPROD_AWS_ACCESS_KEY_ID`, and `PREPROD_AWS_SECRET_ACCESS_KEY`. If you use the same account for prod and preprod, just give the same values to the prod and preprod variables.
4. Run the `CD compute` action. This creates the serverless Spring Boot. The API URL is printed in the Github console.

## Use cases

### Install poja and list all possible parameters

```
pip install poja
python -m poja --help
```

### Create a completely new project

```
python -m poja \
  --app-name=poja-base \
  --package-full-name=com.company.base \
  --region=eu-west-3 \
  --output-dir=folder-to-be-created \

  --with-own-vpc=true \
  --ssm-sg-id=/poja/sg/id \
  --ssm-subnet1-id=/poja/subnet/private1/id \
  --ssm-subnet2-id=/poja/subnet/private2/id
```

Those configurations will be automatically saved in [poja.yml](https://github.com/hei-school/poja-base/blob/prod/poja.yml) at the end of the creation.
See section "Use your own VPC" for the `--with-own-vpc` and `--ssm-xxx-id` arguments.

### Upgrade an already existing project

```
pip install poja --upgrade
python -m poja \
  --app-name=poja-base \
  ...
  --output-dir=folder-already-created
```
Note the `--upgrade` and the `--output-dir=folder-already-created` flags. The POJA configuration that was used for the previous generation is saved in `poja.yml`: it will be updated after the new upgrade.

If you want to do an upgrade without re-specifying each parameter (there are more than 20 of them!), then poja conveniently provides the `--poja-conf` parameter.
Just modify the existing `poja.yml`
(modify mandatorily the `version` parameter so that it reflects the newly upgraded version,
modify optionally any other parameter depending on your needs), then:
```
pip install poja --upgrade
cd folder-already-created
python -m poja --poja-conf=poja.yml --output-dir=.
```

### Configure your database

Use `--with-database=postgres|non-poja-managed-postgres|sqlite`.
In particular, `non-poja-managed-postgres` is handy if you want to use an already existing Postgres, that you will manually reference through custom Java env vars.

If you want POJA to fully manage Postgres: from creation, to operations -- scale-in, scale-out to zero, DDoS protection, regular backups -- to deletion. Then do as follows before running the `CD compute` action:

1. Create two entries in SSM that stores the credentials of the database that will be created. The name MUST be as follows: `/<?app-name>/<?env>/db/username` and `/<?app-name>/<?env>/db/password` where `<?app-name>` is any name you want and `<?env>` is either `prod` or `preprod`.
2. Define the Github variable `PROD_DB_CLUSTER_TIMEOUT` that sets the prod database cluster scaling down timeout. Note that its value must be between 300 seconds (5 minutes) and 86_400 seconds (1 day). Due to the once-per-day health check action, the (serverless) prod database will always be hot if you set it to one day.
3. Run the `CD storage` action. This creates the serverless Postgres. The database URL is printed in the Github console.

### Use custom/additional Java deps

Just provide the argument `--custom-java-deps=your-list-of-deps`
where `your-list-of-deps` contains the dependency lines that are to be added to `build.gradle`.
[Here](./custom-java-deps-aws-ses.txt) is an example of such a file.

Once the generation finishes, `your-list-of-deps` will be copied at the root path of the genrated directory,
under the name `poja-custom-java-deps.txt`.
That file will come handy for future generations based on past generations.

### Use custom/additional Java env vars

Similar to the Java deps section above, but with `--custom-java-env-vars` as argument name.
[Here](./custom-java-env-vars.txt) is an example of such a file.

### Set application properties

Use `application.properties` as standard.
These properties hold for both frontals and workers.
If you want to use specific values for workers,
then set them inside a file named `application-worker.properties`.

> **Warning**
> Values from `application-worker.properties` will take precedence over `application.properties`.


### Use your own VPC

```diff
- For the moment, you MUST use your own managed VPC for hosting the POJA generated resources.
- That is, you MUST use --with-own-vpc=true.
- If you want to put POJA resources inside AWS managed network,
- contact us and we will tell you what needs to be done.
```

Create first:
- Two subnets. They MUST be private, and access Internet through a NAT Gateway. Reference their id in SSM under any name you want. If you use public subnets, then some parts of POJA might not work correctly, notably the asynchronous stack and the bucket stack.
- A security group that allows incoming HTTP traffic, allows all internal traffic, and allows all outcoming traffic. Put its id in SSM under any name you want.

> **Warning**
> Remind that the NAT Gateway associated to the subnets is __not__ serverless.
> Whether your POJA is used or not, the NAT Gateway will generate a fixed lower cost of around $35 per month.
> If you host 100 POJA in the same VPC, that makes $0.35 the fixed cost per POJA.

Then invoke Poja CLI with the following additional parameters:
```
--with-own=vpc=true \
--ssm-sg-id=/poja/sg/id \
--ssm-subnet1-id=/poja/subnet/private1/id \
--ssm-subnet2-id=/poja/subnet/private2/id
```

