from unittest import TestCase
from DataScientistMethod import train_split_data, __get_number_of_samples

class Scient_Method_class(TestCase):


    def test_get_numbers_of_samples_by_int_23(self):
        self.assertEqual(__get_number_of_samples(23, 100), 23)

    def test_get_numbers_of_samples_by_int_100(self):
        self.assertEqual(__get_number_of_samples(100, 100), 100)

    def test_get_numbers_of_samples_by_int_0(self):
        self.assertEqual(__get_number_of_samples(0, 100), 0)

    def test_get_numbers_of_samples_by_float_0_0(self):
        self.assertEqual(__get_number_of_samples(0.0, 100), 0)

    def test_get_numbers_of_samples_by_float_0_1(self):
        self.assertEqual(__get_number_of_samples(0.1, 100), 10)

    def test_get_numbers_of_samples_by_float_0_15(self):
        self.assertEqual(__get_number_of_samples(0.15, 100), 15)

    def test_get_numbers_of_samples_by_float_0_5(self):
        self.assertEqual(__get_number_of_samples(0.5, 100), 50)

    def test_get_numbers_of_samples_by_float_0_5_in99(self):
        self.assertEqual(__get_number_of_samples(0.5, 99), 49)



