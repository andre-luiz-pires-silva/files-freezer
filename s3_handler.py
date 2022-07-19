import boto3

if __name__ == '__main__':
    client = boto3.client("s3")
    response = client.list_buckets()
    print(response)
