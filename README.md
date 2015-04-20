### EC2 Scheduler

The following program may be used to control the scheduling of starting and stopping of AWS EC2 virtual machines. It does this by parsing a JSON map of your schedule per machine and creating CRON jobs.
***This means it requires a running machine to execute those CRON jobs.***
To run the program, you'll also have to install the dependencies (specified in *requirements.txt*)

####Instructions - ***parse schedule map***
* Tag your machines with a Name tag.
* To turn on your machine every day at 07:00 and stop it at 20:00, create a JSON file with the following structure:
```json
[
  {
    "name": "rikonor",
    "region": "eu-west-1",
    "start_time": "07:00",
    "stop_time": "20:00"
  }
]
```
* Run  <code>python ec2_scheduler.py parse map_file --id aws_access_key_id --secret aws_secret_key</code>
* This will create cron jobs as needed in the crontab of the user running the script.

####Instructions - ***manually run / stop machine***
* Run  <code>python ec2_scheduler.py (start|stop) your_machine_name --id aws_access_key_id --secret aws_secret_key --region machine_region</code>

####Instructions - ***clear all jobs***
* Run  <code>python ec2_scheduler.py clear</code>
* This will remove all jobs related to ec2_scheduler from the user's crontab
