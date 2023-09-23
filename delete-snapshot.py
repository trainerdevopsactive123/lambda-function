import boto3
import datetime

def lambda_handler(event, context):
    # Connect to the EC2 client
    ec2 = boto3.client('ec2')

    # Get the tag value to filter by
    tag_value = event['tag_value']

    # Get all snapshots
    snapshots = ec2.describe_snapshots(Filters=[{'Name': 'tag:Name', 'Values': [tag_value]}]).get('Snapshots')

    # Delete the snapshots
    for snapshot in snapshots:
        ec2.delete_snapshot(SnapshotId=snapshot['SnapshotId'])

    return {
        'statusCode': 200,
        'body': 'Snapshots deleted successfully.'
    }




# In the test env give 

{
  "tag_value": "backup"
}


# look for snapshot tag Name backup