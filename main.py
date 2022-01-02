import csv
import os
import sys
import json
import yaml


def read_config(config_path: str):
  with open(config_path, "r") as fp:
    return yaml.safe_load(fp)

  raise Exception(f"Issues Reading the File: {config_path}")


def get_extension(file_name: str):
    return file_name.split(".")[-1]


def convert_file(file_path: str, conversion_path: str):
  file_extension = get_extension(file_path)
  conversion_extension = get_extension(conversion_path)

  if file_extension == "csv" and conversion_extension == "json":
    csv_to_json(file_path, conversion_path)



def csv_to_json(file_path: str, conversion_path: str):

  with open(file_path, "r") as fp:
    csv_list = list(csv.DictReader(fp))

  if not os.path.exists(os.path.dirname(conversion_path)):
    os.makedirs(os.path.dirname(conversion_path))

  with open(conversion_path, "w") as fp:
    json.dump(csv_list, fp)


def main():
  config_path = sys.argv[-1]
  config = read_config(config_path)

  for file_path in config.keys():

    for conversion_path in config[file_path]:

      convert_file(file_path, conversion_path)


if __name__ == '__main__':
    main()
