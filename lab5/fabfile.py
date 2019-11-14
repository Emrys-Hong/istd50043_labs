import boto3
import json

ec2 = boto3.client('ec2')
s3 = boto3.client('s3')

def create_bucket(name, acl='private', location='ap-southeast-1'):
  s3.create_bucket(ACL=acl, Bucket=name, CreateBucketConfiguration={'LocationConstraint': location})

def put_objects_test(name):
  data={}
  data["hello"] = "world"
  s3.put_object(Bucket=name, Key='data0', Body=json.dumps(data))

def list_objects_test(name):
  print(s3.list_objects(Bucket=name))


def list_ec2_instances():
	instances = {}
	res = ec2.describe_instances()
	for r in res['Reservations']:
		for ins in r['Instances']:
			if ins['State']['Name'] == 'running':
				instances[ins['InstanceId']] = ins['PublicIpAddress']
	print(instances)

def list_images():
	res = ec2.describe_images(Owners=['self'])
	for img in res['Images']:
		print("Name: ",img['Name'])
		print("Image: ", img['ImageId'])
		print("Description: ", img['Description'])
		print("----")

def save_instance(ins, name, desc='My new instance'):
	res = ec2.create_image(InstanceId=ins, Name=name, Description=desc)
	print("Created image: ",res['ImageId'])
	print("Waiting for it to be available...")

	# wait for it to be available
	available = 0
	while (not available):
		status = ec2.describe_images(ImageIds=[res['ImageId']])
		img = status['Images'][0]
		available = (img['State'] == 'available')
		time.sleep(1)

