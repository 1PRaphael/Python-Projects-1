# Python-Projects-1
This repository contains two Python scripts designed to perform specific tasks related to managing resources in AWS and retrieving file information within a directory.

1. Lambda Function to Stop EC2 Instances

File: stop_ec2_instances_lambda.py

Description:

This Python script is designed to be deployed as an AWS Lambda function. Its purpose is to stop EC2 instances tagged with a specific value, in this case, "Dev_Lab".

Functionality:

    The script utilizes the Boto3 library to interact with AWS services.
    It describes EC2 instances to retrieve information about running instances.
    It identifies instances tagged with "Dev_Lab" and collects their instance IDs.
    The ec2.stop_instances() method (currently commented out) can be uncommented to initiate the stopping of identified instances.
    Finally, it prints the list of stopped instance IDs.

Usage:

Ensure proper IAM permissions are assigned to the Lambda function for interacting with EC2 instances. Uncomment the line response = ec2.stop_instances(InstanceIds=instances) to enable the instance stopping functionality.

2. Retrieve File Information

File: retrieve_file_info.py

Description:

This Python script is designed to retrieve information about files within a directory. It utilizes the os module to traverse the directory structure and gather information about each file.

Functionality:

    It initializes an empty list to store file information.
    Utilizing os.walk(), it traverses through the directory structure.
    For each file encountered, it creates a dictionary containing file path, name, and size.
    The dictionaries are then appended to the file_list.
    Finally, it prints the list of dictionaries, each containing file information.

Usage:

Ensure the script is executed within the directory you want to retrieve file information from. Modify the thisdir variable if needed to specify a different directory.

Note: Before deploying or executing these scripts, ensure you understand their functionalities and have appropriate permissions and safeguards in place, especially when interacting with AWS resources. Always test scripts in a controlled environment before applying them to production systems.
