#!/usr/bin/env python
import sys
from collections import Counter

# 実行コマンド
# cat ../Data_Science_from_Scratch.txt  | python ./most_common_words.py 10


# 第一引数として、出力する単語数を指定する
try:
    num_words = int(sys.argv[1])
except:
    print("usage: most_common_words.py num_words")
    sys.exit(1) # error終了

counter = Counter(word.lower()#文字をすべて小文字に
                  for line in sys.stdin
                  for word in line.strip().split()#単語は空白で区切る
                  if word)#空文字列はスキップ

for word, count in counter.most_common(num_words):
    sys.stdout.write(str(count))
    sys.stdout.write("\t")
    sys.stdout.write(word)
    sys.stdout.write("\n")
    