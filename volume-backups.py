import boto3
import schedule

ec2_client = boto3.client('ec2')


def create_volume_snapshots():
    volumes = ec2_client.describe_volumes(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': ['dev']
            }
        ]
    )
    # print(volumes['Volumes'])
    for volume in volumes['Volumes']:
        new_snapshot = ec2_client.create_snapshot(
            VolumeId=volume['VolumeId']
        )
        print(new_snapshot)


schedule.every(20).seconds.do(create_volume_snapshots)
# schedule.every().day.do(create_volume_snapshots)

while True:
    schedule.run_pending()

