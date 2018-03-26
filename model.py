import math
class ModelInfo(object):

    def __init__(self,name):
        self.name = name
        self.mean = None
        self.variance = None

    def get_lower_boundry(self, amount = 1):
        return self.mean - amount * math.sqrt(self.variance)

    def get_upper_boundry(self, amount = 1):
        return self.mean +  amount * math.sqrt(self.variance)

    def calculate_mean(self, data):
        self.mean = sum(data)/len(data)

    def calculate_variance(self, data):
        if self.mean is None:
            self.calculate_mean(data)

        sum_of_pow = 0
        for item in data:
            sum_of_pow += (self.mean-item) ** 2

        self.variance = sum_of_pow/len(data)

class IrisModel(object):



    def __init__(self, test_sample, learn_sample, types):
        self.test_sample = test_sample
        self.learn_sample = learn_sample
        self.types = types
        self.modelInfos = {}


    def learn(self):
        for type in self.types:
            data_frame = self.learn_sample[type].get_values_equal_to(4, type)
            self.modelInfos[type] = []
            for column in data_frame.labels[:-1]:
                data_to_process = data_frame.get_column_as_list(column)
                modelInfo = ModelInfo(column)
                modelInfo.calculate_mean(data_to_process)
                modelInfo.calculate_variance(data_to_process)
                self.modelInfos[type].append(modelInfo)

    def check_if_value_is_in_range(self, value, modelInfo):
        if  modelInfo.get_upper_boundry(1) > value > modelInfo.get_lower_boundry(1):
            return 1
        elif modelInfo.get_upper_boundry(2) > value > modelInfo.get_lower_boundry(2):
            return 0.5
        elif modelInfo.get_upper_boundry(3) > value > modelInfo.get_lower_boundry(3):
            return 0.25
        return 0

    def check_all_values_aginst_model_info(self, data_row, iris_type):
        ret_value = 0

        for index, modelinfo in enumerate(self.modelInfos[iris_type]):
            ret_value += self.check_if_value_is_in_range(value=data_row[index], modelInfo=modelinfo)
        return ret_value/len(self.modelInfos[iris_type])

    def predict(self, data_row):
        result = []
        for iris_type in self.modelInfos:
            result.append((self.check_all_values_aginst_model_info(data_row, iris_type),iris_type))

        return result

