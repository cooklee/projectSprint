from unittest import TestCase
from dataframe_testdata import test_data
from DataFrame import DataFrame


class TestDataFrame(TestCase):

    def setUp(self):
        self.data_frame = DataFrame(labels=test_data[0], data=test_data[1:])
        self.labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'type']
        self.data = test_data[1:]
        pass

    def test_createDataFrame_labels(self):
        self.assertEqual(len(self.data_frame.labels), len(test_data[0]))

    def test_createDataFrame_data(self):
        self.assertEqual(len(self.data_frame.data), len(test_data) - 1)

    def test_label_correct(self):
        for item_loc, item_to_test in zip(self.labels, self.data_frame.labels):
            self.assertEqual(item_loc, item_to_test)

    def test_data_correct(self):
        for item_loc, item_to_test in zip(test_data[1:], self.data_frame.data):
            self.assertEqual(item_loc, item_to_test)

    def test_get_types_from_data_frame_by_index_last_column(self):
        types = self.data_frame.get_types_of_data(-1)
        a = {'SML', "MID", "BIG"}
        for key in types:
            a.remove(key)
        self.assertEqual(0, len(a))

    def test_get_types_from_data_frame_by_label_name(self):
        types = self.data_frame.get_types_of_data('type')
        a = {'SML', "MID", "BIG"}
        for key in types:
            a.remove(key)
        self.assertEqual(0, len(a))

    def test_get_types_from_data_frame_by_label_a_column(self):
        types = self.data_frame.get_types_of_data('a')
        a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
        for key in types:
            a.remove(key)
        self.assertEqual(0, len(a))

    def test_indexing_check_labels_01(self):
        data = self.data_frame[1, 2]
        for item_loc, item_to_check in zip(self.labels[1], data.labels):
            self.assertEqual(item_loc, item_to_check, 'wrong labels in indexing')

    def test_indexing_check_labels_02(self):
        data = self.data_frame[0, 2]
        for item_loc, item_to_check in zip(self.labels[0], data.labels):
            self.assertEqual(item_loc, item_to_check, 'wrong labels in indexing')

    def test_indexing_check_labels_03(self):
        data = self.data_frame[-1, 2]
        for item_loc, item_to_check in zip(self.labels[-1], data.labels):
            self.assertEqual(item_loc, item_to_check, 'wrong labels in indexing')

    def test_indexing_check_labels_04(self):
        data = self.data_frame[-5, 2]
        for item_loc, item_to_check in zip(self.labels[-5], data.labels):
            self.assertEqual(item_loc, item_to_check, 'wrong labels in indexing')

    def test_indexing_check_data_01(self):
        data = self.data_frame[:, 1]
        for item_loc, item_to_check in zip(self.data[1], data.data[0]):
            self.assertEqual(item_loc, item_to_check, 'wrong data in indexing')

    def test_indexing_check_data_02(self):
        data = self.data_frame[:, -1]
        for item_loc, item_to_check in zip(self.data[-1], data.data[0]):
            self.assertEqual(item_loc, item_to_check, 'wrong data in indexing')

    def test_indexing_check_data_03(self):
        data = self.data_frame[:, 100]
        for item_loc, item_to_check in zip(self.data[100], data.data[0]):
            self.assertEqual(item_loc, item_to_check, 'wrong data in indexing')

    def test_slicing_only_col_check_labels_01(self):
        data = self.data_frame[1:]
        for item_loc, item_to_check in zip(self.labels[1:], data.labels):
            self.assertEqual(item_loc, item_to_check, 'wrong labels in slicing')

    def test_slicing_only_col_check_labels_02(self):
        data = self.data_frame[:-1]
        for item_loc, item_to_check in zip(self.labels[:-1], data.labels):
            self.assertEqual(item_loc, item_to_check, 'wrong labels in slicing')

    def test_slicing_only_col_check_labels_03(self):
        data = self.data_frame[1:-1]
        for item_loc, item_to_check in zip(self.labels[1:-1], data.labels):
            self.assertEqual(item_loc, item_to_check, 'wrong labels in slicing')

    def test_slicing_only_col_check_labels_04(self):
        data = self.data_frame[2:5]
        for item_loc, item_to_check in zip(self.labels[2:5], data.labels):
            self.assertEqual(item_loc, item_to_check, 'wrong labels in slicing')

    def test_slicing_check_labels_01(self):
        data = self.data_frame[2:5, 2]
        for item_loc, item_to_check in zip(self.labels[2:5], data.labels):
            self.assertEqual(item_loc, item_to_check, 'wrong labels in slicing')

    def test_slicing_check_labels_02(self):
        data = self.data_frame[:, 2]
        for item_loc, item_to_check in zip(self.labels, data.labels):
            self.assertEqual(item_loc, item_to_check, 'wrong labels in slicing')

    def test_slicing_check_labels_03(self):
        data = self.data_frame[3:, 2]
        for item_loc, item_to_check in zip(self.labels[3:], data.labels):
            self.assertEqual(item_loc, item_to_check, 'wrong labels in slicing')

    def test_slicing_check_data_01(self):
        data = self.data_frame[:, 1:10]
        for line_loc, line_to_check in zip(self.data[1:10], data.data):
            for item_loc, item_to_check in zip(line_loc, line_to_check):
                self.assertEqual(item_loc, item_to_check, 'wrong data in slicing')

    def test_slicing_check_data_02(self):
        data = self.data_frame[:, 12:120]
        for line_loc, line_to_check in zip(self.data[12:120], data.data):
            for item_loc, item_to_check in zip(line_loc, line_to_check):
                self.assertEqual(item_loc, item_to_check, 'wrong data in slicing')

    def test_slicing_check_data_03(self):
        data = self.data_frame[:, 19:-5]
        for line_loc, line_to_check in zip(self.data[19:-5], data.data):
            for item_loc, item_to_check in zip(line_loc, line_to_check):
                self.assertEqual(item_loc, item_to_check, 'wrong data in slicing')

    def test_slicing_check_data_04(self):
        data = self.data_frame[:4, 19:-5]
        for line_loc, line_to_check in zip(self.data[19:-5], data.data):
            for item_loc, item_to_check in zip(line_loc[:4], line_to_check):
                self.assertEqual(item_loc, item_to_check, 'wrong data in slicing')

    def test_slicing_check_data_05(self):
        data = self.data_frame[1:6, 54:120]
        for line_loc, line_to_check in zip(self.data[54:120], data.data):
            for item_loc, item_to_check in zip(line_loc[1:6], line_to_check):
                self.assertEqual(item_loc, item_to_check, 'wrong data in slicing')









