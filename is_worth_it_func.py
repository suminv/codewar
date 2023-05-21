def is_worth_it(self):
    return self.draft - (self.crew * 1.5) > 20


Titanic = Ship(15, 10)  # False
Titanic.is_worth_it()


class Ghost(object):
