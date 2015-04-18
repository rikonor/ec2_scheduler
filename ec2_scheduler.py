from boto.ec2.connection import EC2Connection
import json

# Depending on the operator
# parse
# start
# stop

# parse the map
# start a machine
# stop a machine

aws_id = "123"
aws_secret = "123"

conn = EC2Connection(
    aws_access_key_id=aws_id,
    aws_secret_access_key=aws_secret
)