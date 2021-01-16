class InOutUpperString():
    def __init__(self):
        self.n = ''

    def get_string(self):
        self.n = input('Enter a string ')

    def print_string(self):
        print(self.n.upper())


p = InOutUpperString()
p.get_string()
p.print_string()
