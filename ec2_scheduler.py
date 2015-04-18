"""EC2 Scheduler.

Usage:
  ec2_scheduler.py parse <map_file> --id <id> --secret <secret>
  ec2_scheduler.py (start|stop) <instance_name> --id <id> --secret <secret> --region <region>
  ec2_scheduler.py clear
  ec2_scheduler.py (-h | --help)
  ec2_scheduler.py --version

Options:
  -h --help     Show this screen.
  --version     Show version..
  --id          AWS Access Key ID
  --secret      AWS Secret Access Key
  --region      AWS Region name

"""
from docopt import docopt
import boto.ec2
from datetime import datetime


def get_ec2_connection(aws_id, aws_secret, region_name):
    """
    :param aws_id: AWS Access Key ID
    :param aws_secret: AWS Secret Access Key
    :param region_name: AWS Region name
    :return: EC2Connection object

    Given AWS credentials, return an EC2Connection
    """
    region = boto.ec2.get_region(region_name)

    return boto.ec2.EC2Connection(
        aws_access_key_id=aws_id,
        aws_secret_access_key=aws_secret,
        region=region
    )

def get_ec2_instance(conn, name):
    """
    :type conn: boto.ec2.EC2Connection
    :param name: Instance name
    :return: Instance with specified name

    Given an EC2Connection and instance name, return the actual instance
    """
    reservations = conn.get_all_instances()
    for reservation in reservations:
        for instance in reservation.instances:
            if name == instance.tags.get('Name'):
                return instance

def parse(file_name, aws_id, aws_secret):
    pass
    # Don't create a line in cron if it already exists!

def command(operation, instance_name, aws_id, aws_secret, region):
    """
    :param operation: "start" / "stop"
    :param instance_name: Instance name
    :param aws_id: AWS Access Key ID
    :param aws_secret: AWS Secret Access Key
    :param region: AWS Region name

    Start or Stop a machine.
    """
    conn = get_ec2_connection(aws_id, aws_secret, region)
    instance = get_ec2_instance(conn, instance_name)
    dt = datetime.now().strftime("%D-%T")

    # If it's in accordance with the requested operation, perform it
    if operation == 'start' and instance.state == 'running':
        print "{0} - Instance {1} [{2}] already running.".format(dt, instance.id, instance_name)

    elif operation == 'stop' and instance.state == 'stopped':
        print "{0} - Instance {1} [{2}] already stopped.".format(dt, instance.id, instance_name)

    elif operation == 'start' and instance.state != 'running':
        instance.start()
        print "{0} - Instance {1} [{2}] started.".format(dt, instance.id, instance_name)

    elif operation == 'stop' and instance.state != 'stopped':
        instance.stop()
        print "{0} - Instance {1} [{2}] stopped.".format(dt, instance.id, instance_name)

def clear():
    pass

if __name__ == '__main__':
    arguments = docopt(__doc__, version='EC2 Scheduler 0.1')

    aws_id = arguments.get('<id>')
    aws_secret = arguments.get('<secret>')
    region = arguments.get('<region>')

    if arguments['parse'] is True:
        parse(arguments['<map_file>'], aws_id, aws_secret)

    elif arguments['start'] is True:
        command("start", arguments['<instance_name>'], aws_id, aws_secret, region)

    elif arguments['stop'] is True:
        command("stop", arguments['<instance_name>'], aws_id, aws_secret, region)

    elif arguments['clear'] is True:
        clear()

