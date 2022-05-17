"""This module contains all the test cases"""
import unittest
from ser_func import SerFunc


class Test_function(unittest.TestCase):
    """TestSum is the main class that is to be implemented
    Methods:
    -----------------------
    test_register_func(self):
        Testing for the newly registered users.
    test_create_func(self):
        Testing for the creation of the folders.
    test_write_func(self):
        Testing for the writing of the file.
    test_read_func(self):
        Testing for the reading of the file.
    """
    # SerFunc()

    def test_register_func(self):
        """Testing newly registered users.
        """
        given_values = [[["register", "milli", "123"], ('127.0.0.1', 56682)],
                        [["register", "prem", "123"],
                            ('127.0.0.1', 56683)]]
        expected_outputs = ["Personal folder created",
                            "Username already exists"]
        output = []
        for i in given_values:
            output.append(SerFunc().register_user(i[0], i[1]))
        self.assertListEqual(output, expected_outputs)

    def test_create_func(self):
        """Testing creation of folders.
        """
        given_values = [[["create_folder", "milli"], ('127.0.0.1', 56683)],
                        [["create_folder", "prem"], ('127.0.0.1', 56683)]]
        expected_outputs = ['folder created', "folder name already exists"]
        output = []
        for i in given_values:
            SerFunc().user_login(
                ["login", "admin", "123"], ('127.0.0.1', 56683))
            output.append(SerFunc().make_folder(i[0], i[1]))

        self.assertListEqual(output, expected_outputs)

    def test_write_func(self):
        """Testing the writing of data to the file.
        """
        given_values = [[["write_file", "sample.txt"]],
                        [["write_file", "sample.txt", "Prem is my best friend"]]]
        expected_outputs = [' File created ', ' FIle writing complete ']
        output = []
        for i in given_values:
            output.append(SerFunc().wt_fl(i[0]))
        self.assertListEqual(output, expected_outputs)

    def test_read_func(self):
        """Testing the reading of file.
        """
        SerFunc().user_login(
            ["login", "prem", "1234"], ('127.0.0.1', 56683))
        given_values = [[["read_file", "sam.txt"], ('127.0.0.1', 56683)],
                        [["read_file", "sample.txt"], ('127.0.0.1', 56683)]]
        expected_outputs = ['File doesn´t exist', 'Hello World']
        output = []
        for i in given_values:
            output.append(SerFunc().rd_fl(i[0], i[1]))
        self.assertListEqual(output, expected_outputs)


if __name__ == '__main__':
    unittest.main()
