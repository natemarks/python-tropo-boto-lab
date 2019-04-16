import boto3
import random
import string
from typing import Dict, List

# prefix for objects created in test
ID_PREFIX = "fake-"

# us-east-1 is bleeding edge features
DEV_REGION = "us-east-1"


def id_generator(size=8, chars=string.ascii_lowercase + string.digits):
    random_string = ''.join(random.choice(chars) for _ in range(size))
    return ID_PREFIX + random_string


def create_bucket_with_client(bucket_id, tag_set):
    dev_session = boto3.Session(region_name=DEV_REGION, profile_name='personal')
    s3_resource = dev_session.resource('s3')
    response = s3_resource.create_bucket(Bucket=bucket_id)
    bucket_tagging = s3_resource.BucketTagging(bucket_id)
    bucket_tagging.put(Tagging={'TagSet': tag_set})
    return response


def destroy_bucket_with_client(bucket_name):
    """Destroy bucket by bucket name

    :param str bucket_name: name of bucket to delete

    """
    dev_session = boto3.Session(region_name=DEV_REGION, profile_name='personal')
    s3_resource = dev_session.resource('s3')
    for bucket in s3_resource.buckets.all():
        if bucket.name == bucket_name:
            for key in bucket.objects.all():
                key.delete()
            bucket.delete()
            break


def bucket_name_exists(bucket_name):
    """Destroy bucket by bucket name

    :param str bucket_name: name of bucket to delete

    :rtype: bool

    """
    dev_session = boto3.Session(region_name=DEV_REGION, profile_name='personal')
    s3_resource = dev_session.resource('s3')
    all_buckets = [bucket.name for bucket in s3_resource.buckets.all()]

    return bucket_name in all_buckets


def simple_get_bucket_by_tags(tag_filter, type_filter):
    """The summary line for a method docstring should fit on one line.

    Example tag filter
                TagFilters=[
                {
                    'Key': 'shape',
                    'Values': ['round']
                }
            ]

    :param List[Dict[str, str or List[str]]] tag_filter: tag filter

    Type filter options:
    https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces
    """
    dev_session = boto3.Session(region_name=DEV_REGION, profile_name='personal')
    client = dev_session.client('resourcegroupstaggingapi')

    def lookup_for_tags(token):
        response = client.get_resources(
            PaginationToken=token,
            TagFilters=tag_filter,
            ResourcesPerPage=50,
            ResourceTypeFilters=[
                type_filter,
            ]
        )
        return response

    results = []
    response = lookup_for_tags("")
    page_token = ""
    while True:
        results += response["ResourceTagMappingList"]
        page_token = response["PaginationToken"]
        if page_token == "":
            break
        response = lookup_for_tags(page_token)
    for r in results:
        print
        r["ResourceARN"]

    return response


def list_bucket_arns_by_tags(tag_filter, type_filter):

    """The summary line for a method docstring should fit on one line.

    Example tag filter
                TagFilters=[
                {
                    'Key': 'shape',
                    'Values': ['round']
                }
            ]

    :param List[Dict[str, str or List[str]]] tag_filter: tag filter
    :param str type_filter: see options for string below


    Type filter options:
    https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces

    :rtype: List[str]
    """
    res = []
    response = simple_get_bucket_by_tags(tag_filter, type_filter)
    for arn in response['ResourceTagMappingList']:
        res.append(arn['ResourceARN'])

    return res


def list_cfn_by_tags(tag_filter, type_filter="cloudformation"):

    """The summary line for a method docstring should fit on one line.

    Example tag filter
                TagFilters=[
                {
                    'Key': 'shape',
                    'Values': ['round']
                }
            ]

    :param List[Dict[str, str or List[str]]] tag_filter: tag filter
    :param str type_filter: see options for string below

    Type filter options:
    https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces

    :rtype: List[str]
    """
    res = []
    response = simple_get_bucket_by_tags(tag_filter, type_filter)
    for arn in response['ResourceTagMappingList']:
        res.append(arn['ResourceARN'])

    return res


def get_file_path(file_name, path=None):
    """Fild path of file_name in search_dir subtree

    Given a file name (file_name) walk the subtrees under search_dir and return the full path of the first found
    instance of the file name.  If no search_dir is provided, use cwd

    :param str file_name: name of a file

    :param str path: absolute path to a directory to be searched. default to cwd

    :rtype: str
    """
    import os
    for root, dirs, files in os.walk(path):
        if file_name in files:
            return os.path.join(root, file_name)
