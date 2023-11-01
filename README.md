POJA CLI
========

A Python CLI to the [POJA stack](https://github.com/hei-school/poja).

# Usage

```
pip install poja
python -m poja \
  --app-name=poja-annotator \
  --region=eu-west-3 \
  --ssm-sg-id=/poja/sg/id \
  --ssm-subnet1-id=/poja/subnet/public1/id \
  --ssm-subnet2-id=/poja/subnet/public2/id \
  --output-dir=anywhere
```

