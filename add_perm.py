import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('func_name')
parser.add_argument('s3_arn')
parser.add_argument('acc_id')


args = parser.parse_args()

func_name = args.func_name
s3_arn = args.s3_arn
acc_id = args.acc_id

command = 'aws lambda add-permission --function-name {func_name} --region ap-southeast-1 --statement-id 1 --action "lambda:InvokeFunction" --principal s3.amazonaws.com --source-arn {arn} --source-account {acc_id}'.format(
    func_name=func_name, arn=s3_arn, acc_id=acc_id)

os.system(command)