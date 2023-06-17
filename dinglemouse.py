class Dinglemouse(object):

    def __init__(self):
        self.name = None
        self.sex = None
        self.age = None
        self.hell = 'Hello.'

    def setAge(self, age):
        if self.age is None:
            self.hell = self.hell + ' I am {age}.'
        self.age = age
        return self

    def setSex(self, sex):
        if self.sex is None:
            self.hell = self.hell + ' I am {sex}.'
        self.sex = "male" if sex == 'M' else "female"
        return self

    def setName(self, name):
        if self.name is None:
            self.hell = self.hell + ' My name is {name}.'
        self.name = name
        return self

    def hello(self):
        return self.hell.format(age=self.age, sex=self.sex, name=self.name)
