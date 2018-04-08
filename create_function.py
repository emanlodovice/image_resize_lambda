import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('func_name')
parser.add_argument('filename')
parser.add_argument('role')


args = parser.parse_args()

func_name = args.func_name
role = args.role
filename = args.filename

command = 'aws lambda create-function --region ap-southeast-1 --function-name {func_name} --zip-file fileb://{filename} --role {role} --handler CreateThumbnail.handler --runtime python2.7 --timeout 10 --memory-size 1024'.format(
    **{'func_name': func_name, 'filename': filename, 'role': role})

os.system(command)
