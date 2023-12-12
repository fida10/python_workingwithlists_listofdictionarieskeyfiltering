import unittest
from src.ans import filter_dict_list


class TestFilterDictList(unittest.TestCase):
    def test_filter_dict_list(self):
        input_list = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
        expected = [{'age': 30}, {'age': 25}]
        self.assertEqual(filter_dict_list(input_list, 'name'), expected)

    def test_empty_list(self):
        self.assertEqual(filter_dict_list([], 'name'), [])

    def test_key_not_present(self):
        input_list = [{'name': 'Alice'}, {'name': 'Bob'}]
        self.assertEqual(filter_dict_list(input_list, 'age'), input_list)


if __name__ == '__main__':
    unittest.main()
