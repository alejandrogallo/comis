#! /usr/bin/env bash

language=spanish
url=https://www.linguasorb.com/${language}/verbs/most-common-verbs/

curl -s ${url}/{1..4}       |
grep -E verbs.conjugation   |
grep class                  |
sed "s_/*'>Conjug.*__"              |
sed "s_^.*verbs/conjugation/__"             |
sort                        |
uniq                        |
sed "/^$/d"                 |
{
  while read root; do
    if [[ ${language} == english ]]; then
      infinitive="to ${root}"
    else
      infinitive=$root
    fi
    cat <<EOF
- infinitive: ${infinitive}
  root: ${root}
EOF
  done
} |
tee ${language}.yaml




# vim-run: bash %
