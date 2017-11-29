# -*- coding: utf-8 -*-
__author__ = 'Yaicky'
import sys

for line in sys.stdin:
    c1, c2 = map(int, line.split())
    seconds = int((c2 - c1) / 100) if (c2 - c1) % 100 < 50 else int((c2 - c1) / 100) + 1
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    print(":".join(map(lambda c: str(c).rjust(2, "0"), [h, m, s])))

'''
123 4577973
'''