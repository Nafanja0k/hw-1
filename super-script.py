import argparse
import hashlib
import json
import pandas as pd
import csv
import os
import pwd
import sys
from datetime import datetime
from enum import Enum

import checksumdir

import dirhash as dirhash

class Timecode(Enum):
    UNIX = 1
    UTC = 2


class Path(Enum):
    SCRIPT_PATH = 0
    RUN_PATH = 1
    DEFINED_PATH = 2
    def __str__(self):
        return self.name


class LS:
    # default values
    script_path = os.path.abspath(os.path.dirname(__file__))
    run_path = os.getcwd()
    defined_path = ""
    timecode = Timecode.UNIX
    location = Path.RUN_PATH
    verbosity = False

    def __init__(self, args):
        self.args = args

        if args.location:
            self.location = args.location

        if self.args.s:
            self.script_path = self.args.s
        elif self.args.r:
            self.run_path = self.args.r
        elif self.args.p:
            self.defined_path = self.args.p

        if self.args.utc:
            self.timecode = Timecode.UTC

        if self.args.v:
            self.verbosity = True

    def get_path(self, mode: enumerate):
        if mode == Path.RUN_PATH:
            return self.run_path
        elif mode == Path.SCRIPT_PATH:
            return self.script_path
        elif mode == Path.DEFINED_PATH:
            return self.defined_path
        return None

    def get_content_list(self, path: str):
        '''
        returns a list of files and folders in the path passed
        :return: array
        '''
        content_list = []
        for (dirpath, dirnames, filenames) in os.walk(path):
            content_list.extend(filenames)
            content_list.extend(dirnames)
            break # brake here to avoid iteration through the tree
        return content_list

    def get_file_list(self, path: str):
        '''
        returns a list of files the path passed
        :return: array
        '''
        content_list = []
        for (dirpath, dirnames, filenames) in os.walk(path):
            content_list.extend(filenames)
            break # brake here to avoid iteration through the tree
        return content_list

    def get_directory_list(self, path: str):
        '''
        returns a list of folders in the path passed
        :return: array
        '''
        content_list = []
        for (dirpath, dirnames, filenames) in os.walk(path):
            content_list.extend(dirnames)
            break # brake here to avoid iteration through the tree
        return content_list

    def get_file_info(self, path: str, time_mode: enumerate):
        '''
        returns a dict with file info
        :return: array
        '''
        with open(path, 'rb') as file:
            # read contents of the file
            data = file.read()
            # pipe contents of the file through
            md5_hash = hashlib.md5(data).hexdigest()
        file_info = {
            "size": os.path.getsize(path),
            "hash": md5_hash,
            "owner": pwd.getpwuid(os.stat(path).st_uid).pw_name,
            "m_date": os.path.getmtime(path),
            "c_date": os.path.getctime(path)
        }
        return file_info

    def get_directory_info(self, path: str, time_mode: enumerate):
        '''
        returns a dict with directory info
        :return: array
        '''
        dir_info = {
            "size": os.path.getsize(path),
            "hash": checksumdir.dirhash(path, "md5"),
            "owner": pwd.getpwuid(os.stat(path).st_uid).pw_name,
            "m_date": os.path.getmtime(path),
            "c_date": os.path.getctime(path)
        }
        return dir_info

    def save_as_txt(self, path: str, content: str):
        with open(path + "/output.txt", 'w') as file:
            df = pd.DataFrame(content)
            file.write(df.to_string(header=True, index=False))
        return

    def save_as_csv(self, path: str, content: str):
        with open(path + "/output.csv", 'w') as file:
            dict_writer = csv.DictWriter(file, content[0].keys())
            dict_writer.writeheader()
            dict_writer.writerows(content)
        return

    def save_as_json(self, path: str, content: str):
        with open(path + "/output.json", 'w') as file:
            json.dump(content, file, indent=4, sort_keys=True)
        return

    def save_as_html(self, path: str, content: str):
        with open(path + "/output.html", 'w') as file:
            df = pd.DataFrame(content)
            file.write(df.to_html(header=True, index=False))
        return

    def get_task_status(self):
        module = 1
        task = 1
        status = "done"
        res_status = r"module {} task %d - %s".format(module, task, status)
        return res_status

    def get_report_content(self, report_path: str):
        content = ""
        return content

    def get_directories_info(self, path: str):
        directories_info = []
        directories_list = self.get_directory_list(path)
        for directory in directories_list:
            full_path = "/".join([path, directory])
            data = self.get_directory_info(full_path, self.timecode)
            data["type"] = "directory"
            data["name"] = directory
            data["path"] = path
            data["full_path"] = full_path
            directories_info.append(data)
        return directories_info

    def get_files_info(self, path: str):
        files_info = []
        files_list = self.get_file_list(path)
        for file in files_list:
            full_path = "/".join([path, file])
            data = self.get_file_info(full_path, self.timecode)
            data["type"] = "file"
            data["name"] = file
            data["path"] = path
            data["full_path"] = full_path
            files_info.append(data)
        return files_info

    def get_contents_info(self, path: str):
        contents_info = []
        contents_info.extend(self.get_files_info(path))
        contents_info.extend(self.get_directories_info(path))
        return contents_info

    def print_result(self, content, content_type="all", verbosity=0):
        '''
        prints result to stdout
        :return:
        '''
        if self.verbosity:
            print("Files in {} {}".format(str(self.location), ls.get_path(self.location)))
            for id, item in enumerate(content):
                if self.timecode == Timecode.UTC:
                    content[id]["m_date"] = str(datetime.utcfromtimestamp(item["m_date"]))
                    content[id]["c_date"] = str(datetime.utcfromtimestamp(item["c_date"]))
            df = pd.DataFrame(content)
            with pd.option_context('display.expand_frame_repr', False):
                print(df)
        else:
            for item in content:
                print(item["name"])
        return

if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=False)
    # parser.add_argument('--help', action='help', help='show help message and exit')
    parser.add_argument("--location", type=lambda path: Path[path], choices=list(Path), help="choose location to check files from")
    parser.add_argument("--print", choices=["files", "directories", "all"], help="choose location to check files from")
    parser.add_argument("-f", action="store_true", help="only files")
    parser.add_argument("-d", action="store_true", help="only directories")

    group_save_as = parser.add_mutually_exclusive_group()
    group_save_as.add_argument("-t", action="store_true", help="output format - TXT")
    group_save_as.add_argument("-j", action="store_true", help="output format - JSON")
    group_save_as.add_argument("-c", action="store_true", help="output format - CSV")
    group_save_as.add_argument("-h", action="store_true", help="output format - HTML")

    group_path = parser.add_mutually_exclusive_group()
    parser.add_argument("-r", help="path where the script is executed from")
    parser.add_argument("-s", help="path where the script is stored")
    parser.add_argument("-p", help="set the path explicitly")

    group_time = parser.add_mutually_exclusive_group()
    group_time.add_argument("--utc", action="store_true", help="UTC time")
    group_time.add_argument("--unix", action="store_true", help="UNIX time")

    group_verbosity = parser.add_mutually_exclusive_group()
    group_verbosity.add_argument("-v", action="store_true", help="show more details in output")
    group_verbosity.add_argument("-l", action="store_true", help="show less details in output")

    args = parser.parse_args()

    ls = LS(args)
    if args.print:
        if args.print == "all":
            content = ls.get_contents_info(ls.get_path(ls.location))
        elif args.print == "files":
            content = ls.get_files_info(ls.get_path(ls.location))
        elif args.print == "directories":
            content = ls.get_directories_info(ls.get_path(ls.location))
        ls.print_result(content, verbosity=ls.verbosity)

        #save to file if argument with output type is passed
        if args.t:
            ls.save_as_txt(path=ls.script_path, content=content)
        elif args.j:
            ls.save_as_json(path=ls.script_path, content=content)
        elif args.c:
            ls.save_as_csv(path=ls.script_path, content=content)
        elif args.h:
            ls.save_as_html(path=ls.script_path, content=content)

    sys.exit(0)