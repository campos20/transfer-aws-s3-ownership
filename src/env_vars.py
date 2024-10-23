from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

SOURCE_S3 = os.getenv("SOURCE_S3")
SOURCE_AWS_ACCESS_KEY_ID = os.getenv("SOURCE_AWS_ACCESS_KEY_ID")
SOURCE_AWS_SECRET_ACCESS_KEY = os.getenv("SOURCE_AWS_SECRET_ACCESS_KEY")

TARGET_S3 = os.getenv("TARGET_S3")
TARGET_AWS_ACCESS_KEY_ID = os.getenv("TARGET_AWS_ACCESS_KEY_ID")
TARGET_AWS_SECRET_ACCESS_KEY = os.getenv("TARGET_AWS_SECRET_ACCESS_KEY")
