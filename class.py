#!/usr/bin/env python3

class Robot:
    def introduce_self(self):
        print("My name is " + self.name)
        # Self is an additional argument
        # This is for what he doesn't say yet

r1 = Robot()
r1.name = "Tom"
r1.color = "red"
r1.weight = 30

r1.introduce_self()