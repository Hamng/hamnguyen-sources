# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 08:24:34 2021

@author: Ham
"""

import sys

class God:
    pass

class Person(God):
    def __init__(self, first_name, sex=None, date=None, father=None, mother=None):
        self.first_name = first_name
        self.sex=sex
        self.spouse = None
        self.children = []
        self.attribute = []
        if sex=="son":
            self.role=(sex, "husband", "father")
        else:
            self.role=(sex, "wife", "mother")
        if father:
            father.add_child(self)
            print("Announcement:",
                  ("on " + date + "," if date else ""),
                  father.first_name, "and", mother.first_name,
                  "joyfully celebrate the birth of their", sex + ",", first_name)

    def marry(self, spouse, date=None):
        self.spouse = spouse
        print("Announcement:",
              ("on " + date + "," if date else ""),
              self.first_name, "and", spouse.first_name,
              "lovingly announce their union")

    def add_child(self, child):
        self.children.append(child.first_name)

    def add_attribute(self, *args):
        self.attribute += args

    def pass_away(self, date=None):
        print("Announcement:",
              ("on " + date + "," if date else ""),
              "with profound sadness, the family of",
              self.spouse.first_name + ",",
              ", ".join(self.children[:-1]), "and", self.children[-1],
              "announces the passing of", self.first_name + '.')
        print("We will remember", "him", "forever as",
              ", ".join(self.attribute))


class Pet(God):
    def __init__(self, name, kind=None, owner=None):
        self.name=name
        self.kind=kind
        print("Announcement:", owner.first_name,
              "happily adopts a", kind, "named", name)

if __name__ == '__main__':
    ham = Person(first_name="Ham", sex="son", date="1958-07-11",
                 father=Person("Hoa"),
                 mother=Person("Hien"))

    anh = Person(first_name="Anh")
    ham.marry(anh)

    darren = Person(first_name="Darren", sex="son",
                    father=ham, mother=anh)

    neil = Person(first_name="Neil", sex="son",
                  father=ham, mother=anh)

    jazlynn = Person(first_name="Jazlynn", sex="daughter",
                     father=ham, mother=anh)

    prince = Pet(name="Prince", kind="dog", owner=jazlynn)

    ham.add_attribute(
        "a dutiful " + ham.sex + " to his parents",
        "a faithful and loyal " + ham.role[1] + " to " + ham.spouse.first_name,
        "a supportive and inspirational " + ham.role[2] + " to his children",
        "an unwilling walker of our " + prince.kind + " " + prince.name
        )

    ham.pass_away()