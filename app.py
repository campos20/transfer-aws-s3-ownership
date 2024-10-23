import os
import boto3

from src.env_vars import (
    SOURCE_AWS_ACCESS_KEY_ID,
    SOURCE_AWS_SECRET_ACCESS_KEY,
    SOURCE_S3,
    TARGET_AWS_ACCESS_KEY_ID,
    TARGET_AWS_SECRET_ACCESS_KEY,
    TARGET_S3,
)


def move_files():
    source_s3 = boto3.client(
        "s3",
        aws_access_key_id=SOURCE_AWS_ACCESS_KEY_ID,
        aws_secret_access_key=SOURCE_AWS_SECRET_ACCESS_KEY,
    )
    response = source_s3.list_objects_v2(Bucket=SOURCE_S3)

    to_move = []
    if "Contents" in response:
        for obj in response["Contents"]:
            key = obj["Key"]
            to_move.append(key)
    else:
        print("No objects found in the bucket.")
        return

    print(f"Found {len(to_move)} objects to move.")

    target_s3 = boto3.client(
        "s3",
        aws_access_key_id=TARGET_AWS_ACCESS_KEY_ID,
        aws_secret_access_key=TARGET_AWS_SECRET_ACCESS_KEY,
    )

    download_path = "temp"
    current = 0

    for key in to_move:
        current += 1

        if current % 10 == 0:
            print(f"Moved {current} of {len(to_move)}")

        local_file_path = os.path.join(download_path, key)
        parent_dir = os.path.dirname(local_file_path)
        os.makedirs(parent_dir, exist_ok=True)

        source_s3.download_file(SOURCE_S3, key, local_file_path)

        target_s3.upload_file(local_file_path, TARGET_S3, key)
        print(f"Moved {key}")

        source_s3.delete_object(Bucket=SOURCE_S3, Key=key)
        print(f"Deleted {key}")

    # This is a recursive function that will keep calling itself until all files are moved
    move_files()


def main():
    move_files()


if __name__ == "__main__":
    main()
