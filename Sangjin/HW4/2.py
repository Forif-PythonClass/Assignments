class string_:
    string = ""
    def __init__(self):
        self.string=""
    def get_String(self):
        self.string=input("input string:")
    def print_String(self):
        print ((self.string).upper())

_string_=string_()
_string_.get_String()
_string_.print_String()
