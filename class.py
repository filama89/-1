class Father:
    def __init__(self, value):
        self.value = value
        print(self.value)


class Son(Father):
    def __init__(self, value):
        super().__init__(value)

