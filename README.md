# transfer-aws-s3-ownership

Currently, there is no way to move S3 between AWS accounts. This is a script to do so.

## Requirements

- python 3.10
- [virtualenv](https://pypi.org/project/virtualenv/)

## Get Started

```
python -m virtualenv .venv
source .venv/bin/activate
pip install poetry
poetry install
```

## TODO

- Avoid the need to inform target S3
- Use sqlite to store meta (example the name of the target bucket)
