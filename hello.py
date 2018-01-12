#!/usr/bin/env python
# -*- coding=utf-8 -*-
from __future__ import print_function
from platform import python_version

f = open("hello.txt", "w")
for i in range(10):
    print(i, "Hello python", python_version(), sep=";")
    print(i, "Hello python", python_version(), sep=";", end="\n", file=f)
f.close()
