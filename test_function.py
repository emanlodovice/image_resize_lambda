import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('func_name')

args = parser.parse_args()

func_name = args.func_name

command = 'aws lambda invoke --invocation-type Event --function-name {func_name} --region ap-southeast-1 --payload file://inputfile.txt outputfile.txt'.format(
    func_name=func_name)
os.system(command)
