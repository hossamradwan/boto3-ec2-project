import boto3
import schedule
from operator import itemgetter

ec2_client = boto3.client('ec2')

volumes = ec2_client.describe_volumes(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': ['dev']
            }
        ]
    )

for volume in volumes['Volumes']:
    snapshots = ec2_client.describe_snapshots(
        OwnerIds=['self'],
        Filters=[
            {
                'Name': 'volume-id',
                'Values': [volume['VolumeId']]
            }
        ]
    )
    # print(snapshots['Snapshots'])

    sorted_by_date = sorted(snapshots['Snapshots'], key=itemgetter('StartTime'), reverse=True)

    # for snap in snapshots['Snapshots']:
    #     print(snap['StartTime'])
    #
    # print("#######################")
    #
    # for snap in sorted_by_date:
    #     print(snap['StartTime'])

    for snap in sorted_by_date[2:]:
        # delete snapshots
        response = ec2_client.delete_snapshot(
            SnapshotId=snap['SnapshotId']
        )
        print(response)



