# transfer-aws-s3-ownership

Currently, there is no way to move S3 between AWS accounts. This is a script to do so.

This project will move the content of SOURCE_S3 (currently to TARGET_S3). In the future, there will be no need to pass the TARGET_S3. Check the TODO.

## Requirements

- python 3.10
- [virtualenv](https://pypi.org/project/virtualenv/)

## Get Started

```
python -m virtualenv .venv
source .venv/bin/activate
pip install poetry
poetry install
python app.py
```

## TODO

- Use sqlite to store meta (example the name of the target bucket)
- Avoid the need to inform target S3. Create unique a temp name, store it in sqlite, move the files to the temp one, delete the original, create the SOURCE S3 again and sync them.
