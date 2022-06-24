import argparse
import os
import sys


class LS:
    def get_path(mode: enumerate):
        path = ""
        return path

    def get_content_list(path: str):
        '''
        returns a list of files and folders in the path passed
        :return: array
        '''
        files_list = []
        return files_list

    def get_file_list(self, path: str):
        '''
        returns a list of files the path passed
        :return: array
        '''
        content_list = []
        return content_list

    def get_directory_list(self, path: str):
        '''
        returns a list of folders in the path passed
        :return: array
        '''
        directories_list = []
        return directories_list

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
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", action="store_true", help="path where to run the script from")
    parser.add_argument("-s", action="store_true", help="path where the script is stored")
    parser.add_argument("-p", action="store_true", help="set the path explicitly")
    parser.add_argument("-f", action="store_true", help="only files")
    parser.add_argument("-d", action="store_true", help="only directories")
    parser.add_argument("-v", action="store_true", help="show more details in output")
    parser.add_argument("-l", action="store_true", help="show less details in output")
    parser.add_argument("-t", action="store_true", help="output format - TXT")
    parser.add_argument("-j", action="store_true", help="output format - JSON")
    parser.add_argument("-c", action="store_true", help="output format - CSV")
    parser.add_argument("-h", action="store_true", help="output format - HTML")

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    work_dir = os.curdir
    sys.exit(0)