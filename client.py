#GNU nano 4.8                                                                                                                   
import boto3
from pprint import pprint
aws_console = boto3.session.Session(profile_name="default")
iam_console = aws_console.client(service_name="iam")
user=iam_console.list_users()
pprint(user)














