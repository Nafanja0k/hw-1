import argparse
import csv
import json
import os
import tempfile
from unittest import TestCase, mock
from unittest.mock import mock_open, patch
import super_script


class TestLS(TestCase):
    def setUp(self):
        parser = super_script.create_parser()
        self.args = parser.parse_args(['-v'])
        self.ls = super_script.LS(self.args)

    def test_get_path(self):
        path = self.ls.get_path(mode=super_script.Path.SCRIPT_PATH)
        if not os.path.exists(os.path.dirname(path)):
           raise AssertionError("Path does not exist: %s" % str(path))

    def test_get_content_list(self):
        content = self.ls.get_content_list(self.ls.get_path(mode=super_script.Path.SCRIPT_PATH))
        self.assertTrue(content)

    def test_get_file_list(self):
        content = self.ls.get_file_list(self.ls.get_path(mode=super_script.Path.SCRIPT_PATH))
        self.assertTrue(content)

    def test_get_directory_list(self):
        content = self.ls.get_directory_list(self.ls.get_path(mode=super_script.Path.SCRIPT_PATH))
        self.assertTrue(content)


    def test_print_result(self):
        self.fail()

    def test_get_file_info(self):
        info = {}
        with tempfile.NamedTemporaryFile(mode='w', delete=True) as tmp_file:
            info = self.ls.get_file_info(tmp_file.name, self.ls.timecode)
        self.assertEqual(info["size"], 0)
        self.assertTrue(info["hash"])
        self.assertTrue(info["owner"])
        self.assertTrue(info["m_date"])
        self.assertTrue(info["c_date"])

    def test_get_directory_info(self):
        info = {}
        with tempfile.TemporaryDirectory() as tmp_dir:
            info = self.ls.get_directory_info(tmp_dir, self.ls.timecode)
        self.assertTrue(info["size"])
        self.assertTrue(info["hash"])
        self.assertTrue(info["owner"])
        self.assertTrue(info["m_date"])
        self.assertTrue(info["c_date"])

    def test_get_contents_info(self):
        info = {}
        info = self.ls.get_contents_info(self.ls.script_path)
        self.assertGreater(len(info), 0, "dict is empty")
        self.assertTrue(info[0]["size"], "item is empty")
        self.assertTrue(info[0]["hash"], "hash is empty")
        self.assertTrue(info[0]["owner"], "owner is empty")
        self.assertTrue(info[0]["m_date"], "modification timestamp is empty")
        self.assertTrue(info[0]["c_date"], "creation timestamp is empty")

    def test_get_files_info(self):
        info = {}
        info = self.ls.get_contents_info(self.ls.script_path)
        self.assertGreater(len(info), 0, "dict is empty")
        self.assertTrue(info[0]["size"], "item is empty")
        self.assertTrue(info[0]["hash"], "hash is empty")
        self.assertTrue(info[0]["owner"], "owner is empty")
        self.assertTrue(info[0]["m_date"], "modification timestamp is empty")
        self.assertTrue(info[0]["c_date"], "creation timestamp is empty")

    def test_get_directories_info(self):
        info = {}
        info = self.ls.get_contents_info(self.ls.script_path)
        self.assertGreater(len(info), 0, "dict is empty")
        self.assertTrue(info[0]["size"], "item is empty")
        self.assertTrue(info[0]["hash"], "hash is empty")
        self.assertTrue(info[0]["owner"], "owner is empty")
        self.assertTrue(info[0]["m_date"], "modification timestamp is empty")
        self.assertTrue(info[0]["c_date"], "creation timestamp is empty")

    def test_save_as_html(self):
        test_data = [
            {
                "c_date": "2022-06-26 11:40:31.702139",
                "full_path": "/Users/user/Documents/homework-1/output.json",
                "hash": "71313849ff4ce59ae543130fb079dd3a",
                "m_date": "2022-06-26 11:40:31.702139",
                "name": "output.json",
                "owner": "user",
                "path": "/Users/user/Documents/homework-1",
                "size": "2711",
                "type": "file"
            }
        ]
        contains = '<table border="1" class="dataframe">\n'
        content = []
        with tempfile.TemporaryDirectory() as tmp_dir:
            self.ls.save_as_html(path=tmp_dir, content=json.dumps(test_data))
            with open(tmp_dir + "/output.html", "r") as file:
                content = file.readlines()
        self.assertEqual(content[0], contains, "file content is different from expected one")

    def test_save_as_csv(self):
        test_data = [
            {
                "c_date": "2022-06-26 11:40:31.702139",
                "full_path": "/Users/user/Documents/homework-1/output.json",
                "hash": "71313849ff4ce59ae543130fb079dd3a",
                "m_date": "2022-06-26 11:40:31.702139",
                "name": "output.json",
                "owner": "user",
                "path": "/Users/user/Documents/homework-1",
                "size": "2711",
                "type": "file"
            }
        ]
        content = []
        with tempfile.TemporaryDirectory() as tmp_dir:
            self.ls.save_as_csv(path=tmp_dir, content=json.dumps(test_data))
            with open(tmp_dir + "/output.csv", "r") as csvfile:
                dr = csv.DictReader(csvfile)
                for row in dr:
                    content.append(row)
        a, b = json.dumps(test_data, sort_keys=True, ), json.dumps(content, sort_keys=True)
        self.assertEqual(a, b, "file content is different from expected one")

    def test_save_as_json(self):
        test_data = [
            {
                "c_date": "2022-06-26 11:40:31.702139",
                "full_path": "/Users/user/Documents/homework-1/output.json",
                "hash": "71313849ff4ce59ae543130fb079dd3a",
                "m_date": "2022-06-26 11:40:31.702139",
                "name": "output.json",
                "owner": "user",
                "path": "/Users/user/Documents/homework-1",
                "size": "2711",
                "type": "file"
            }
        ]
        content = []
        with tempfile.TemporaryDirectory() as tmp_dir:
            self.ls.save_as_json(path=tmp_dir, content=json.dumps(test_data))
            with open(tmp_dir + "/output.json", "r") as csvfile:
                content = json.load(csvfile)

        a, b = json.dumps(test_data, sort_keys=True, ), json.dumps(content, sort_keys=True)
        self.assertEqual(a, b, "file content is different from expected one")

    def test_save_as_txt(self):
        test_data = [
            {
                "c_date": "2022-06-26 11:40:31.702139",
                "full_path": "/Users/user/Documents/homework-1/output.json",
                "hash": "71313849ff4ce59ae543130fb079dd3a",
                "m_date": "2022-06-26 11:40:31.702139",
                "name": "output.json",
                "owner": "user",
                "path": "/Users/user/Documents/homework-1",
                "size": "2711",
                "type": "file"
            }
        ]
        contains = ['                    c_date                                    full_path                             hash                     m_date        name owner                             path size type\n',
                    '2022-06-26 11:40:31.702139 /Users/user/Documents/homework-1/output.json 71313849ff4ce59ae543130fb079dd3a 2022-06-26 11:40:31.702139 output.json  user /Users/user/Documents/homework-1 2711 file']
        content = []
        with tempfile.TemporaryDirectory() as tmp_dir:
            self.ls.save_as_txt(path=tmp_dir, content=json.dumps(test_data))
            with open(tmp_dir + "/output.txt", "r") as file:
                content = file.readlines()
        self.assertListEqual(content, contains, "file content is different from expected one")

    def test_get_task_status(self):
        self.fail()



    def test_get_report_content(self):
        self.fail()