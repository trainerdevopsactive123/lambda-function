import boto3

def lambda_handler(event, context):
    # Initialize the EC2 client
    ec2 = boto3.client('ec2')

    # Specify the parameters for the instance
    instance_params = {
        'ImageId': 'ami-05552d2dcf89c9b24',  # Replace with your desired AMI ID
        'InstanceType': 't2.micro',  # Replace with your desired instance type
        'KeyName': 'newserver',  # Replace with your key pair name
        'MinCount': 1,
        'MaxCount': 1,
        'SecurityGroupIds': ['sg-0098ea776ec399ba1'],  # Replace with your security group ID(s)
        'SubnetId': 'subnet-07b6082cc6a94e850',  # Replace with your subnet ID
        'TagSpecifications': [
            {
                'ResourceType': 'instance',
                'Tags': [
                    {'Key': 'Name', 'Value': 'MyEC2Instance'},  # Replace with your desired tags
                ],
            },
        ],
    }

    # Launch the EC2 instance
    response = ec2.run_instances(**instance_params)

    # Extract instance ID from the response
    instance_id = response['Instances'][0]['InstanceId']

    return {
        'statusCode': 200,
        'body': f'EC2 instance {instance_id} created successfully'
    }
