#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import yaml
import sys

language = sys.argv[1]
out = "new.yaml"

with open("data/english/verbs/data.yaml") as fd:
    english_yaml = yaml.load(fd)

with open("data/"+language+"/verbs/data.yaml") as fd:
    other_yaml = yaml.load(fd)

for word in other_yaml:
    ids = word.get("ids")
    found_ids = []
    if not ids:
        english_not_found = True
        while english_not_found:
            print("The following word is not related to any english other word")
            print(word)
            english_test = raw_input("Input an english equivalent: ")
            if english_test == '0':
                print("Skipping...")
                break
            for eng_word in english_yaml:
                if eng_word["root"] == english_test:
                    found_ids = eng_word.get("ids")
                    english_not_found = False
                    print('  Word found!!')
                    print(eng_word)
                    break
        word["ids"] = found_ids
        print('  New word:')
        print(word)
        print("")

with open(out, 'w+') as fd:
    yaml.dump(other_yaml, fd)


#vim-run: python % french
