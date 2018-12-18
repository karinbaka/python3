#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: karinbaka
# @Date:   2018-11-01 11:24:31
# @Email: 47525620@qq.com
from datetime import datetime

now = datetime.now()
print(now)

print(type(now))

dt = datetime(2015,4,19,12,20)
print(dt)

stamp = dt.timestamp()
print(stamp)
a=datetime.fromtimestamp(1429417200.0)
print(a)

b=datetime.utcfromtimestamp(1429417200.0)
print(b)
