#!/usr/bin/env python

from lib.user import User

#!/usr/bin/env python

from lib.user import User

class Student(User):
    
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []

    def learn(self, str):
        self.knowledge.append(str)