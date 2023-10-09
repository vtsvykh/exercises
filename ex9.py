import random

with open('input.txt', 'r') as data:
    num = data.read().split()
    jan = num[:30]
    feb = num[30:58]
    mar = num[58:89]
    apr = num[89:119]
    may = num[119:150]
    jun = num[150:180]
    jul = num[180:211]
    aug = num[211:242]
    sep = num[242:272]
    ocb = num[272:303]
    nov = num[303:333]
    dec = num[333:364]

for day in month:
