import boto3
aws_console = boto3.session.Session(profile_name = "default")
iam_console = aws_console.resource("iam")

for user in iam_console.users.all():
   print(user.user_name)

