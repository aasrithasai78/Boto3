import boto3

def lambda_handler(event, context):
    region = event['region']
    ec2 = boto3.resource('ec2', region_name=region)
    print('region: ',region)
    instances = []
    for instance in ec2.instances.all():
        if instance.state['Name'] == 'running':
            instances.append(instance.id)
            print('Instance id: ',instances)
    return {
        "instances": instances,
        "region": region
    }
