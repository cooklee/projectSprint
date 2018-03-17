from copy import copy


class DataFrame(object):

    def __init__(self, labels=[], data=[], reindex=True):
        self.data = data
        self.labels = labels

    def set_labels(self, data_frame):
        if isinstance(data_frame[0], list):
            self.labels = data_frame[0]
        else:
            self.labels = data_frame

    def set_data_from_csv(self, data_frame):
        counter = 0
        for line in data_frame:
            temp = [counter]
            temp.extend(line)
            self.data.append(temp)
            counter += 1

    def convert_data_to_type(self, give_type):
        for line in self.data:
            for index, item in enumerate(line):
                try:
                    line[index] = give_type(item)
                except:
                    pass

    def __iter__(self):
        for item in self.data:
            yield item

    def __getitem__(self, index):
        if isinstance(index, tuple):
            return self.get_columns(index[0]).get_rows(index[1])
        return self.get_columns(index)

    def get_columns(self, key):
        if isinstance(key, slice):
            return self.__get_column_by_slice(key)
        return self.__get_column_by_index(key)

    def get_rows(self, key):
        if isinstance(key, slice):
            return self.__get_row_by_slice(key)
        return self.__get_row_by_index(key)

    def __get_column_by_index(self, index):
        label = self.labels[index]
        data = [[x[index]] for x in self.data]
        return DataFrame(labels=label, data=data)

    def __get_column_by_slice(self, slice_obj):
        label = self.labels[slice_obj.start: slice_obj.stop]
        data = [x[slice_obj.start: slice_obj.stop: slice_obj.step] for x in self.data]
        return DataFrame(labels=label, data=data)

    def reindex(self):
        for index, line in enumerate(self.data):
            line[0] = index

    def __get_row_by_index(self, index):
        return DataFrame(labels=self.labels, data=[self.data[index]])

    def __get_row_by_slice(self, slice_obj):
        return DataFrame(labels=self.labels, data=self.data[slice_obj.start:slice_obj.stop:slice_obj.step])

    def get_number_of_column(self, column_name):
        if type(column_name) is int:
            return column_name
        for index, column_name_from_df in enumerate(self.labels):
            if column_name_from_df == column_name:
                return index

    def get_types_of_data(self, column):
        column_number = self.get_number_of_column(column)
        counter = 1
        types = {}
        for item in self.data:
            if item[column_number] in types:
                continue
            else:
                types[item[column_number]] = counter
                counter += 1
        return types

    def swap_values(self, column, values_to_swap):
        column = self.get_number_of_column(column)
        for key in values_to_swap:
            for item in self.data:
                if item[column] == key:
                    item[column] = values_to_swap[item[column]]

    def get_values_equal_to(self, column, value):
        column = self.get_number_of_column(column)
        data = [copy(x) for x in self.data if x[column] == value]
        return DataFrame(labels=copy(self.labels), data=data)

    def __str__(self):
        ret_str = str(self.labels)+"\n"
        for item in self.data:
            ret_str += str(item)+"\n"
        return ret_str

    def __check_if_labels_are_the_same(self, dataframe):
        for index, label in enumerate(self.labels):
            if label != dataframe.labels[index]:
                return False
        return True

    def __add__(self, other):
        if isinstance(other, DataFrame):
            if self.__check_if_labels_are_the_same(other):
                data = copy(self.data)
                labels = copy(self.labels)
                data.extend(copy(other.data))
                dataFrame = DataFrame(labels=labels, data=data)
                return dataFrame
            else:
                raise Exception("Lables are diffrent")
        else:
            raise Exception("{} is not datafram".format(other))


if __name__ == "__main__":
    from csv_reader import CsvReader


