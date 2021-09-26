class Function():
    def __init__(self, function, min_value,max_value):
        self.function = function
        self.min_value = self.validateNumber(min_value)
        self.max_value = self.validateNumber(max_value)

    def validateNumber(self,value):
        try:
            numeric_value = int(value)
            return numeric_value
        except:
            raise ValueError('Min and max values should be integers')
    
