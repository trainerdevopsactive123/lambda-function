# how to update iam role to ec2 machine
# this script will add the new role and also replace the existing role on the EC2 machine 


import boto3

def lambda_handler(event, context):
    # Extract instance ID and new IAM role ARN from the event
    instance_id = event.get('instance_id')
    new_iam_role = event.get('new_iam_role')

    if not instance_id or not new_iam_role:
        return {
            'statusCode': 400,
            'body': 'Missing instance_id or new_iam_role in the event.'
        }

    # Create an EC2 client
    ec2_client = boto3.client('ec2')

    try:
        # Associate the new IAM role with the EC2 instance
        ec2_client.associate_iam_instance_profile(
            IamInstanceProfile={'Arn': new_iam_role},
            InstanceId=instance_id
        )

        return {
            'statusCode': 200,
            'body': f'Successfully updated IAM role for instance {instance_id}.'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error updating IAM role: {str(e)}'
        }



# trigger 

{
  "instance_id": "i-0972b665eaf3664dc",
  "new_iam_role": "arn:aws:iam::806337850770:instance-profile/ec2newrole"
}