#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import yaml
import sys
import os
import time
import random

out = "new.yaml"

with open("data/english/verbs/data.yaml") as fd:
    english_yaml = yaml.load(fd)

with open("test.yaml") as fd:
    other_yaml = yaml.load(fd)

print(len(english_yaml))

for d in other_yaml:
    print(d)
    for word in english_yaml:
        if word["root"] == d["english"]:
            del d["english"]
            d["ids"] = word["ids"]
            print(word)
            break


with open(out, 'w+') as fd:
    yaml.dump(other_yaml, fd, default_flow_style=False, allow_unicode=True)


#vim-run: python3 %
