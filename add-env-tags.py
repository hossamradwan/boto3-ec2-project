import boto3

ec2_client_ohio = boto3.client("ec2") # region: Ohio
reservations_ohio = ec2_client_ohio.describe_instances()['Reservations']
instance_ids_ohio = []
for res in reservations_ohio:
    instances = res['Instances']
    for ins in instances:
        instance_ids_ohio.append(ins['InstanceId'])

print(instance_ids_ohio)

ec2_resource_ohio = boto3.resource('ec2') # region: Ohio
ec2_resource_ohio.create_tags(
    Resources=instance_ids_ohio,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'prod'
        }
    ]
)


