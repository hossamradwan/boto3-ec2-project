import boto3
import schedule

### Get all vpc in the account ###
# ec2_client = boto3.client("ec2")
# # ec2_client = boto3.client("ec2", region_name="eu-central-1")

# all_available_vpcs = ec2_client.describe_vpcs()
# print(all_available_vpcs['Vpcs'][0])

# vpcs = all_available_vpcs['Vpcs']

# for vpc in vpcs:
#     print(f"Vpc Id: {vpc['VpcId']}")
#     cidr_block_assoc_sets = vpc['CidrBlockAssociationSet']
#     for assoc_set in cidr_block_assoc_sets:
#         print(assoc_set['CidrBlockState'])

############################################################

### Create Vpc and subnets ###
# ec2_resource = boto3.resource('ec2')
#
# new_vpc = ec2_resource.create_vpc(CidrBlock='10.0.0.0/16')
# new_vpc.create_tags(
#     Tags=[
#         {
#             'Key': 'Name',
#             'Value': 'my-vpc-python'
#         }
#     ]
# )
# new_vpc.create_subnet(
#     CidrBlock='10.0.1.0/24'
# )
# new_vpc.create_subnet(
#     CidrBlock='10.0.2.0/24'
# )

#####################################################

## schedule monitoring ec2 instances ###
ec2_client = boto3.client("ec2")
ec2_resource = boto3.resource('ec2')

# reservations = ec2_client.describe_instances()
# for reservation in reservations['Reservations']:
#     instances = reservation['Instances']
#     for instance in instances:
#         print(f"Instance {instance['InstanceId']} is {instance['State']['Name']}")


def check_instance_status():
    statuses = ec2_client.describe_instance_status(
        IncludeAllInstances=True
    )
    for status in statuses['InstanceStatuses']:
        ins_status = status['InstanceStatus']['Status']
        sys_status = status['SystemStatus']['Status']
        state = status['InstanceState']['Name']
        print(f"Instance {status['InstanceId']} is {state} with instance status {ins_status} and system status {sys_status}")
    print("###################")


schedule.every(5).seconds.do(check_instance_status)
# schedule.every().day.at("1:00")
# schedule.every().monday.at("12:00")

while True:
    schedule.run_pending()
