

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





