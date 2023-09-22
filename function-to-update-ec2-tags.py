# How to update EC2 tags with lambda function 

import boto3

def lambda_handler(event, context):
    instance_id = event['instance-id']
    tags = event['tags']

    ec2 = boto3.client('ec2')
    response = ec2.create_tags(Resources=[instance_id], Tags=tags)
    return response


# example 
{
    "instance-id": "i-0972b665eaf3664dc",
    "tags": [
        {
            "Key": "Name",
            "Value": "MyInstance"
        },
        {
            "Key": "Environment",
            "Value": "Production"
        }
    ]
}

# how to delete a ec2 tag with lambda function  

import boto3

def lambda_handler(event, context):
    instance_id = event['instance-id']
    tags = event['tags']

    ec2 = boto3.client('ec2')
    response = ec2.delete_tags(Resources=[instance_id], Tags=tags)
    return response


# example 
{
    "instance-id": "i-0972b665eaf3664dc",
    "tags": [
        {
            "Key": "Name",
            "Value": "MyInstance"
        },
        {
            "Key": "Environment",
            "Value": "Production"
        }
    ]
}