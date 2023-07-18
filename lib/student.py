#!/usr/bin/env python

from user import User


class Student(User):
    def learn(self, string):
        Student.knowledge.append(string)

    knowledge = []
