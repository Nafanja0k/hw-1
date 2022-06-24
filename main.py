import argparse
import os
import sys
from enum import Enum


class LS:
    def get_path(self, mode: enumerate):
        return mode.value

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
        file_info = {"size": 0, "hash": "", "m_date": "", "c_date": ""}
        return file_info

    def get_directory_info(self, path: str, time_mode: enumerate):
        '''
        returns a dict with directory info
        :return: array
        '''
        dir_info = {"size": 0, "hash": "", "m_date": "", "c_date": ""}
        return dir_info

    def save_as_txt(self, path: str, content: str):
        return

    def save_as_csv(self, path: str, content: str):
        return

    def save_as_json(self, path: str, content: str):
        return

    def save_as_html(self, path: str, content: str):
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





if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--help', action='help', help='show help message and exit')
    parser.add_argument("-r", help="path where to run the script from")
    parser.add_argument("-s", help="path where the script is stored")
    parser.add_argument("-p", help="set the path explicitly")
    parser.add_argument("-f", action="store_true", help="only files")
    parser.add_argument("-d", action="store_true", help="only directories")
    parser.add_argument("-v", action="store_true", help="show more details in output")
    parser.add_argument("-l", action="store_true", help="show less details in output")
    parser.add_argument("-t", action="store_true", help="output format - TXT")
    parser.add_argument("-j", action="store_true", help="output format - JSON")
    parser.add_argument("-c", action="store_true", help="output format - CSV")
    parser.add_argument("-h", action="store_true", help="output format - HTML")

    args = parser.parse_args()

    ls = LS()
    # TODO: fix this logic to handle defined path
    script_path = args.s if args.s else os.path.abspath(os.path.dirname(__file__))
    run_path = args.r if args.r else os.getcwd()
    defined_path = args.p if args.p else ""
    enum = Enum('DynamicEnum', {'SCRIPT_PATH': script_path, 'RUN_PATH': run_path, "DEFINED_PATH": defined_path})

    content_run = ls.get_content_list(ls.get_path(enum.RUN_PATH))
    print("Files in RUN_PATH {}".format(enum.RUN_PATH))
    print(content_run)
    content_script = ls.get_content_list(ls.get_path(enum.SCRIPT_PATH))
    print("Files in SCRIPT_PATH {}".format(enum.RUN_PATH))
    print(content_script)
    content_defined = ls.get_content_list(ls.get_path(enum.DEFINED_PATH))
    print("Files in DEFINED_PATH {}".format(enum.RUN_PATH))
    print(content_defined)


    sys.exit(0)