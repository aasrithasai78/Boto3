##author : Aasritha Sai V

#Importing necessary python ojects
import boto3
from datetime import datetime, timedelta, timezone
#calling  boto3 resource to access aws IAM
iam_resource = boto3.resource('iam')
print(iam_resource)

ist_timezone_offset = timedelta(hours=5, minutes=30)
print("offset time : ", ist_timezone_offset)

now_utc = datetime.now(timezone.utc)
print(now_utc)

now_ist = datetime.now(timezone.utc) + ist_timezone_offset
print("IST now : ", now_ist)

#Iterating thrugh ll the users using .all90 methos of  iAM  Resource
for user in iam_resource.users.all():
    print(user.user_name)
    last_sign_in = user.password_last_used

    if last_sign_in:
        last_sign_in_ist = last_sign_in.replace(tzinfo=timezone.utc) + ist_timezone_offset
        print("Last signed in at: ",last_sign_in_ist)
        # Calculate the time difference in hours
        delta = (now_ist - last_sign_in_ist).total_seconds() // 3600
        if delta >= 24:
            print(f"Username: {user.user_name} haven't loggedin for a day, Last Signed In: {delta} hours ago ")
    else:
        print(f"Username: {user.user_name}, Last Signed In: Never signed in")

