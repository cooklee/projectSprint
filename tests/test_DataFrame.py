from unittest import TestCase
from copy import copy
from .dataframe_testdata import test_data
from DataFrame import DataFrame, DataRaw


class TestDataFrame(TestCase):

    def setUp(self):
        self.data_frame = DataFrame(labels=test_data[0], data=test_data[1:])
        self.labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'type']
        self.data = test_data[1:]
        pass

    def test_indexing(self):
        self.data_frame.reindex()
        for index, item in enumerate(self.data_frame):
            self.assertEqual(index, item.index)


    def test_createDataFrame_labels(self):
        self.assertEqual(len(self.data_frame.labels), len(test_data[0]))

    def test_createDataFrame_data(self):
        self.assertEqual(len(self.data_frame.data), len(test_data) - 1)

    def test_label_correct(self):
        for item_loc, item_to_test in zip(self.labels, self.data_frame.labels):
            self.assertEqual(item_loc, item_to_test)

    def test_data_correct(self):
        for line_loc, line_to_test in zip(test_data[1:], self.data_frame.data):
            for item_loc, item_to_test in zip(line_loc, line_to_test):
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

    def test_swap_values_one(self):
        self.data_frame.swap_values('type', {"MID": "@MID@"})
        types = self.data_frame.get_types_of_data('type')
        self.assertTrue("@MID@" in types)

    def test_swap_values_all(self):
        self.data_frame.swap_values('type', {"SML": "TINY","MID": "@MID@", "BIG":"HUGE"})
        types = self.data_frame.get_types_of_data('type')
        self.assertTrue("@MID@" in types)
        self.assertTrue("TINY" in types)
        self.assertTrue("HUGE" in types)
        self.assertTrue("SML" not in types)
        self.assertTrue("MID" not in types)
        self.assertTrue("BIG" not in types)

    def test_check_if_correct_values_are_teken(self):
        data = self.data_frame.get_values_equal_to('type', "SML")
        self.assertEqual(len(data.data), 50)
        data_sliced = data[-1,:]
        for item in data_sliced.data:
            self.assertEqual(item[0], 'SML')

    def test_pop_item_int_index_0(self):
        data_raw = self.data_frame.pop_item(0)
        expected_values = [0]*10 + ['SML']
        for exp_item, test_item in zip(expected_values, data_raw):
            self.assertEqual(exp_item, test_item)

    def test_pop_item_int_index_50(self):
        data_raw = self.data_frame.pop_item(50)
        expected_values = [0]*10 + ['MID']
        for exp_item, test_item in zip(expected_values, data_raw):
            self.assertEqual(exp_item, test_item)


    def test_pop_item_int_index_100(self):
        data_raw = self.data_frame.pop_item(100)
        expected_values = [0]*10 + ['BIG']
        for exp_item, test_item in zip(expected_values, data_raw):
            self.assertEqual(exp_item, test_item)

    def test_len_of_data_for_poping(self):
        items_in_frame = len(self.data_frame)
        for item in range(items_in_frame):
            self.assertEqual(len(self.data_frame), items_in_frame - (item))
            self.data_frame.pop_item(item)
        self.assertEqual(len(self.data_frame), 0)

    def test_copy_dataframe_if_is_correct_instance(self):
        copied_dataframe = copy(self.data_frame)
        self.assertTrue(isinstance(copied_dataframe, DataFrame))

    def test_copy_correct_values(self):
        copied_dataframe = copy(self.data_frame)
        for rawdata_base, rawdata_copied in zip(self.data_frame, copied_dataframe):
            self.assertEquals(rawdata_base.index, rawdata_copied.index)
            for item_base, item_copied in zip(rawdata_base, rawdata_copied):
                self.assertEquals(item_base, item_copied)

    def test_if_inner_objects_are_diffrent_data(self):
        copied_dataframe = copy(self.data_frame)
        copied_dataframe.data[0][0] = "Mu point"
        self.assertEquals(copied_dataframe.data[0].index, self.data_frame.data[0].index)
        self.assertNotEquals(copied_dataframe.data[0][0], self.data_frame.data[0][0])

    def test_if_inner_objects_are_diffrent_lables(self):
        copied_dataframe = copy(self.data_frame)
        copied_dataframe.labels[0] = "Mu point"
        self.assertNotEquals(copied_dataframe.labels[0], self.data_frame.labels[0])

    def test_check_pop_by_position(self):
        self.data_frame.pop_on_poss(50)
        self.assertEqual(self.data_frame.data[50].index, 51)

















