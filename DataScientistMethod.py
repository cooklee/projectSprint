
def train_split_data(dataframe, column, test_size):
    types_of_data = dataframe.get_types_of_data(column)
    for key in types_of_data:
        types_of_data[key] = dataframe.get_values_equal_To(column, key)
    a =1


