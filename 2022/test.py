#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
f=[[1,2],[4,3]]
for r in f:print(r)
R=[c[::-1] for c in zip(*f)]
for r in R:print(r)
