from boto.s3 import connection
from boto.s3.key import Key
from boto.s3.bucket import Bucket
from . import settings

BUCKET_CACHE = {}


def get_connection(region):
    return connection.S3Connection(region)


def get_bucket(bucket):
    if not bucket in BUCKET_CACHE:
        connection = get_connection(settings.METROLOGY_REGION)
        BUCKET_CACHE[bucket] = connection.get_bucket(bucket)
    return BUCKET_CACHE[bucket]


def pull(bucket, path, dest_file):
    bucket = get_bucket(bucket)
    key = bucket.get_key(path)
    key.get_contents_to_filename(dest_file)


def pull_content(bucket, path):
    bucket = get_bucket(bucket)
    key = bucket.get_key(path)
    return key.get_contents_as_string()


def push(bucket, path, src_file, content_type=None):
    bucket = get_bucket(bucket)
    key = Key(bucket, path)
    headers = {}
    if content_type:
        headers["content_type"] = content_type
    key.set_contents_from_filename(src_file, headers=headers)


def push_content(bucket, path, content, content_type=None):
    bucket = get_bucket(bucket)
    key = Key(bucket, path)
    headers = {}
    if content_type:
        headers["content_type"] = content_type
    key.set_contents_from_string(content, headers=headers)


def list(bucket, path=None):
    bucket = get_bucket(bucket)
    return bucket.list(path)
