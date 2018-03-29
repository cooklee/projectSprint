from copy import copy
from DataFrame import DataFrame
import random

def __get_number_of_samples(test_size, number_of_items):
    if isinstance(test_size, float):
        if 0 <= test_size <= 1:
            return int(test_size * number_of_items)
        else:
            raise Exception("float number bigger then 1")
    return test_size


def train_split_data(dataframe, column, test_size):
    types_of_data = dataframe.get_types_of_data(column)
    data_divided_by_give_column = {}
    for key in types_of_data:
        data_divided_by_give_column[key] = dataframe.get_values_equal_to(column, key)

    number_of_sumples = {}
    for key in data_divided_by_give_column:
        number_of_sumples[key] = __get_number_of_samples(test_size, len(data_divided_by_give_column[key]))
    to_learn_dataframe = {}
    for key in data_divided_by_give_column:
        to_learn_dataframe[key] = copy(data_divided_by_give_column[key])

    test_datafram = DataFrame()
    for key in to_learn_dataframe:
        for i in range(number_of_sumples[key]):
            index_to_test = random.randrange(0, len(to_learn_dataframe[key]))
            temp = to_learn_dataframe[key].pop_on_poss(index_to_test)
            test_datafram.data.append(temp)
    test_datafram.labels = dataframe.labels

    return test_datafram, to_learn_dataframe

