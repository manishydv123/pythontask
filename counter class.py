class Counter:
    def __init__(self, value):
        self.value = value

    def increase_one(self):
        self.value = self.value + 1
        return self.value
    def decrease_one(self):
        self.value = self.value - 1
        return self.value
    def get_value(self):
        print(self.value)


x = Counter(1)

x.get_value()
x.increase_one()
x.increase_one()
x.get_value()
x.decrease_one()
x.decrease_one()
x.get_value()