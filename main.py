import random

import time

def generate(startdate, enddate):

randomgen = random.random()

print("i will generate random date between",startdate,"and",enddate)

dateformat = '%m/%d/%Y'

st = time.mktime(time.strptime(enddate, dateformat))

et = time.mktime(time.strptime(startdate, dateformat)) # i want ny answer i n the form first i want month then date ghen year

rt = st + randomgen * (st-et)

print(st,"AND",et)

rd = time.strftime(dateformat, time.localtime(rt))

return rt

print(generate("11/25/2013","12/12/2021"))