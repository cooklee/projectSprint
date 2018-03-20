from unittest import TestCase
from DataFrame import DataRaw
from copy import copy

class Test_dataRaw(TestCase):


    def setUp(self):
        self.data = DataRaw([x for x in range(20)])
        self.data.index = 123

    def test_copy_vlues_are_the_same(self):
        copied = copy(self.data)
        for loc_item, item_to_check in zip(self.data, copied):
            self.assertEqual(loc_item, item_to_check)

    def test_if_new_object_is_different_obj(self):
        copied = copy(self.data)
        copied[0] = 'MU'
        self.assertNotEquals(copied[0], self.data[0])

    def test_if_index_is_copied(self):
        copied = copy(self.data)
        self.assertEquals(copied.index, self.data.index)