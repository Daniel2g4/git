class Main_value:
    def __init__(self, value):
        self.value = value

class Combined_value(Main_value):
    def __init__(self, value, other_value):
        super().__init__(value)
        self.other_value = other_value

    def combining_values(self):
        combined = self.other_value + self.value
        return f'combined value : {combined}'
    
values = Combined_value(5,4)

print(values.combining_values())
        