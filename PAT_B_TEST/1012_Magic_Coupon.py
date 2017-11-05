# -*- coding: utf-8 -*-
__author__ = 'Yaicky'
import sys

cur, num_coupon, num_product = 0, 0, 0
coupons, products = [], []
positive_products, positive_coupons = [], []
negative_products, negative_coupons = [], []
def sum_list(l1, l2):
    len1, len2 = len(l1), len(l2)
    l = min(len1, len2)
    rlt = 0
    for i in range(l):
        rlt += l1[i]*l2[i]
    return rlt

for line in sys.stdin:
    if cur == 0:
        num_coupon = int(line)

    elif cur == 1:
        coupons = list(map(int, line.split()))
        positive_coupons = filter(lambda x: x > 0, coupons)
        negative_coupons = filter(lambda x: x < 0, coupons)
        positive_coupons = sorted(positive_coupons, reverse=True)
        negative_coupons = sorted(negative_coupons)

    elif cur == 2:
        num_product = int(line)

    else:
        products = list(map(int, line.split()))
        positive_products = filter(lambda x: x > 0, products)
        negative_products = filter(lambda x: x < 0, products)
        positive_products = sorted(positive_products, reverse=True)
        negative_products = sorted(negative_products)

    cur += 1

    if cur == 4:
        cur = 0
        rlt = 0

        rlt = sum_list(positive_products, positive_coupons)
        rlt += sum_list(negative_products, negative_coupons)

        print(rlt)



'''
4
1 2 4 -1
4
7 6 -2 -3
'''