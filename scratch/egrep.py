#!/usr/bin/env python
import sys, re

# 実行コマンド(数字を含む行をカウントする)
# cat ../test.txt | python egrep.py "[0-9]" | python line_count.py
# 結果: 3

# sys.argvは、コマンドライン引数のリスト
# sys.argv[0]はプログラム名
# sys.argv[1]は、コマンドライン上に指定した正規表現

regex = sys.argv[1]

# スクリプトが処理する各業に対して

for line in sys.stdin:
    # 正規表現に合致したなら、stdoutに出力
    if re.search(regex, line):
        sys.stdout.write(line)
        