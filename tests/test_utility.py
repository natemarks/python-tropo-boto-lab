import pytest


@pytest.fixture(scope="module")
def s3_test_data():
    from tropo_boto_lab.utility import id_generator, destroy_bucket_with_client
    data = {
        'id': id_generator(),
        # uses a value string
        'put_tag_set': [{'Key': 'shape',
                         'Value': 'square'}],
        # uses a list of values. note the different key: 'Values' vs. 'Value'
        'get_tag_set': [{'Key': 'shape',
                         'Values': ['square']}],
        'type_filter': 's3'
    }
    yield data
    destroy_bucket_with_client(data['id'])


def test_neg_bucket_name_exists():
    from tropo_boto_lab.utility import bucket_name_exists
    assert bucket_name_exists('some-non-existent-bucket') is False


def test_create_s3(s3_test_data):
    from tropo_boto_lab.utility import create_bucket_with_client, bucket_name_exists, list_bucket_arns_by_tags
    # create a bucket
    create_bucket_with_client(s3_test_data['id'], s3_test_data['put_tag_set'])
    # make sure the new bucket exists
    assert bucket_name_exists(s3_test_data['id']) is True
    # find the created bucket by tags
    matching_id_list = list_bucket_arns_by_tags(s3_test_data['get_tag_set'], s3_test_data['type_filter'])
    assert matching_id_list[0].endswith(":::" + s3_test_data['id'])


def test_pos_get_resource_by_tags(s3_test_data):
    from tropo_boto_lab.utility import simple_get_bucket_by_tags
    response = simple_get_bucket_by_tags(s3_test_data['get_tag_set'], s3_test_data['type_filter'])
    assert len(response['ResourceTagMappingList']) == 1
    assert response['ResourceTagMappingList'][0]['ResourceARN'] == 'arn:aws:s3:::' + s3_test_data['id']


def test_neg_get_resource_by_tags():
    from tropo_boto_lab.utility import simple_get_bucket_by_tags
    tag_filter = [{'Key': 'shape',
                   'Values': ['shapeless']}]
    type_filter = 's3'
    response = simple_get_bucket_by_tags(tag_filter, type_filter)
    assert len(response['ResourceTagMappingList']) == 0


def test_pos_list_bucket_ids_by_tags(s3_test_data):
    from tropo_boto_lab.utility import list_bucket_arns_by_tags
    res = list_bucket_arns_by_tags(s3_test_data['get_tag_set'], s3_test_data['type_filter'])
    assert len(res) == 1