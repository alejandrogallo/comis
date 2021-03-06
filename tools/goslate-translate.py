#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import yaml
import sys
import os
import goslate
import time
import random

gs = goslate.Goslate()

language = sys.argv[1]
lang_code = sys.argv[2]

print(language, lang_code)

out = "new.yaml"

with open("data/english/verbs/data.yaml") as fd:
    english_yaml = yaml.load(fd)

other_yaml = [d for d in english_yaml]

for d in other_yaml:
    del d["root"]
    time.sleep(random.randint(1,10))
    try:
        d["infinitive"] = gs.translate(d["infinitive"], lang_code)
    except:
        print('Google is evil')
    print(d)


with open(out, 'w+') as fd:
    yaml.dump(other_yaml, fd)


#vim-run: python3 % hebrew he
