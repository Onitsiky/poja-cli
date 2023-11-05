POJA CLI
========

A Python CLI to the [POJA stack](https://github.com/hei-school/poja).

# Usage

## Create a completely new project

```
pip install poja
python -m poja \
  --app-name=poja-base \
  --package-full-name=com.company.base \
  --region=eu-west-3 \
  --ssm-sg-id=/poja/sg/id \
  --ssm-subnet1-id=/poja/subnet/private1/id \
  --ssm-subnet2-id=/poja/subnet/private2/id \
  --output-dir=folder-to-be-created
```

Those configurations will be automatically saved in `poja.yml` at the end of the creation.

## Upgrade an already existing project

```
pip install poja --upgrade
python -m poja \
  --app-name=poja-base \
  --package-full-name=com.company.base \
  --region=eu-west-3 \
  --ssm-sg-id=/poja/sg/id \
  --ssm-subnet1-id=/poja/subnet/private1/id \
  --ssm-subnet2-id=/poja/subnet/private2/id \
  --output-dir=folder-already-created
```

Note the `--upgrade` and the `--output-dir=folder-already-created` flags.

The POJA configuration that was used for the previous generation is saved in `poja.yml`: it will be updated after the new upgrade.

## Use custom/additional Java deps

Just provide the argument `--custom-java-deps=your-list-of-deps`
where `your-list-of-deps` contains the dependency lines that are to be added to `build.gradle`.
[Here](./custom-java-deps-aws-ses.txt) is an example of such a file.

Once the generation finishes, `your-list-of-deps` will be copied at the root path of the genrated directory,
under the name `poja-custom-java-deps.txt`.
That file will come handy for future generations based on past generations.

