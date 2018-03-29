from csv_reader import CsvReader
from DataScientistMethod import train_split_data
from model import IrisModel

data = CsvReader.create_from_csv("iris.csv")
# print(data)

test_data, to_learn = train_split_data(data, 'iris_type', 0.3)

irisModel = IrisModel(test_data, to_learn, data.get_types_of_data('iris_type'))

irisModel.learn()

count = 0
count_equal = 0

for item in test_data:
    a = irisModel.predict(item)
    sorted_ = sorted(a, key = lambda tup: tup[0])
    print('real = {}, predicted = {}'.format(item[-1], sorted_[-1][-1]))
    count += 1
    if item[-1] == sorted_[-1][-1]:
        count_equal += 1
print('accuracy = %.2f' % (float(count_equal)/float(count)))
print(count_equal)
print(count)

































































































































































