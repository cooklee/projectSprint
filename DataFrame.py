class DataFrame(object):

    def __init__(self, data=None, labels=None):
        self.data = data
        self.labels = labels

    def create_from_csv(self, csv):
        data_read = self.__read_from_file(csv)
        data_frame = self.__create_data_frame_from_read_data(data_read)
        self.set_labels(data_frame)
        self.set_data(data_frame)


    @staticmethod
    def __read_from_file(file_path):
        with open(file_path, 'r') as file:
            readlines = []
            for line in file.readlines():
                readlines.append(line[0:-1])
            return readlines

    @staticmethod
    def __create_data_frame_from_read_data(read_lines):
        divided_data = [line.split(',') for line in read_lines]
        return divided_data

    def set_labels(self, data_frame):
        self.labels = data_frame[0]

    def set_data(self, data_frame):
        self.data = data_frame[1:]

    def convert_data_to_type(self, data_list, give_type):
        converted_list = []
        for item in data_list:
            converted_list.append(give_type(item))
        return converted_list

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
        data = [x[index] for x in self.data]
        return DataFrame(labels=label, data=data)

    def __get_column_by_slice(self, slice_obj):
        label = self.labels[slice_obj.start: slice_obj.stop]
        data = [x[slice_obj.start: slice_obj.stop] for x in self.data]
        return DataFrame(labels=label, data=data)

    def __get_row_by_index(self, index):
        return DataFrame(labels=self.labels, data=[self.data[index]])

    def __get_row_by_slice(self, slice_obj):
        return DataFrame(labels=self.labels, data=self.data[slice_obj.start:slice_obj.stop])

    def get_number_of_column(self, column_name):
        if type(column_name) is int:
            return column_name
        for index, column_name_from_df in enumerate(self.labels):
            if column_name_from_df == column_name:
                return index


    #
    # def get_type(self, dataframe, column_number=None, column_name=None):
    #     if column_number is None:
    #         column_number = get_number_of_column(dataframe, column_number=column_number, column_name=column_name)
    #     temp = {}
    #     count = 1
    #     for item in dataframe[1:]:
    #         if item[column_number] not in temp:
    #             temp[item[column_number]] = count
    #             count += 1
    #     return temp

    def __str__(self):
        ret_str = str(self.labels)+"\n"
        for item in self.data:
            ret_str += str(item)+"\n"
        return ret_str


if __name__ == "__main__":
    data = DataFrame()
    data.create_from_csv("E:\projekty\Szkolenia\PMI\project-01\data\\raw\iris.csv")
    df = data[0:2,1]
    print (df)
