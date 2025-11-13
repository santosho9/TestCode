class checkdatasum:
    import os
    import boto3

    
    def __init__(self, name):
        self.name = name
        self.ds = []

    def get(self, string_name):
        fmt = "test name instance [{}] is getting you {} , Code lib 2 testing ".format(self.name, string_name)
        return fmt

    def add(self, string_name):
        self.ds.append(string_name)
        return string_name

    def get_all(self):
        fmt = ""
        for s in self.ds:
            fmt = fmt + s
        fmt = "test name instance [{}] is getting you {} , In Code Lib".format(self.name, fmt)
        return fmt
    def show_msg():
        msg = "########################################## This is a test message with OS ######################################"
        return msg
    def check_sum_all(predict_values):
        
        predict_values  = predict_values  + 200
        return predict_values
    
