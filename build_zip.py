import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('env')
parser.add_argument('filename')

args = parser.parse_args()

env = args.env
filename = args.filename
dir_path = os.path.dirname(os.path.realpath(__file__))

packages_path = '~/.virtualenvs/{}/lib/python2.7/site-packages'.format(env)
zip_command = 'cd {} && zip -r9 {}/{} *'.format(packages_path, dir_path,
                                                filename)
add_file_to_zip = 'zip -g {} CreateThumbnail.py'.format(filename)

os.system(zip_command)
os.system(add_file_to_zip)
