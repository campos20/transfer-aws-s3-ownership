import boto3


def list_objects(bucket_name):
    s3 = boto3.client("s3")
    response = s3.list_objects_v2(Bucket=bucket_name)

    if "Contents" in response:
        for obj in response["Contents"]:
            print(obj["Key"])
    else:
        print("No objects found in the bucket.")


def main():
    bucket_name = "test"
    list_objects(bucket_name)


if __name__ == "__main__":
    main()
