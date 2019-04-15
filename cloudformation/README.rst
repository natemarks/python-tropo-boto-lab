======
README
======

awscli command example::

    aws cloudformation create-stack \
    --template-body file://cloudformation/common_vpc.yml \
    --stack-name MANAGEMENT-VPC \
    --tags Key=environment,Value=MANAGEMENT_VPC \
    --parameters  ParameterKey=environment,ParameterValue=MANAGEMENT_VPC \
    ParameterKey=PrivateDNSZone,ParameterValue=mgmt.gnops \
    --region=us-east-1 \
    --profile=personal \
    --disable-rollback


    aws cloudformation update-stack \
    --template-body file://cloudformation/common_vpc.yml \
    --stack-name MANAGEMENT-VPC \
    --tags Key=environment,Value=MANAGEMENT_VPC \
    --parameters  ParameterKey=environment,ParameterValue=MANAGEMENT_VPC \
    ParameterKey=PrivateDNSZone,ParameterValue=mgmt.gnops \
    --region=us-east-1 \
    --profile=personal

