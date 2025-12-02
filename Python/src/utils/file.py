import csv
import os
from datetime import datetime
from os import environ as env

import pandas


class UtilFile:
    def open(self, path):
        os.system("open "+path)

    def write_text_file(self, path, body):
        with open(path, "w") as f:
            f.write(body)

    def write_csv(self, path, data):
        if not os.path.exists(path):
            os.system(f"touch '{path}'")

        with open(path, "w", newline="") as f:
            f.write("sep=,\n")
            csv_writer = csv.writer(f)

            # Write separator
            header = data[0].keys()
            csv_writer.writerow(header)

            for item in data:
                csv_writer.writerow(item.values())

    def write_excel(self, path, sheet_name, df):
        df.to_excel(path, sheet_name=sheet_name, index=False)

    def read_text_file(self, path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    def read_text_file_as_list(self, path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read().split("\n")

    def read_excel(self, path, sheet_name):
        return pandas.read_excel(path, sheet_name=sheet_name)

    def check_if_path_exist(self, path):
        if not os.path.exists(path):
            os.path.dirname(path)
            os.mkdir(path)

    def filter_by_column(self, excel_df: pandas.DataFrame, column_name, query):
        return excel_df[excel_df[column_name] == query]

    def get_one_column_excel(self, excel_df: pandas.DataFrame, column_name):
        return excel_df[column_name].to_list()

    def clear_file_content(self, path):
        os.system(f"echo > {path}")

    def timestamp_filename(self, filename):
        return env[filename].format(
            timestamp=datetime.utcnow().strftime("%d%b%y%H%M%S")
        )
