




if __name__ == "__main__":
    data = read_data_from_file("E:\projekty\Szkolenia\PMI\project-01\data\\raw\iris.csv")
    data = create_data_frame_from_read_data(data)
    print (get_type(data,column_name='iris_type'))
    for line in data:
        print (line)
