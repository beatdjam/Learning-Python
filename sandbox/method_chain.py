# https://stackoverflow.com/questions/1436703/what-is-the-difference-between-str-and-repr
class ReprText:
    def __init__(self):
        self.text = ''

    def add(self, add_text):
        self.text += add_text
        return self

    def __repr__(self):
        return self.text


#
class StrSample:
    def __init__(self):
        self.text = ''

    def add(self, add_text):
        self.text += add_text
        return self

    def __str__(self):
        return self.text


def main():
    a = ReprText()
    print(a.add('test').add('_test'))  # test_test

    b = StrSample()
    print(b.add('test').add('_test'))  # test_test


if __name__ == '__main__':
    main()
