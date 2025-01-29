#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d17.txt",0
from intcodegen import computer
pgm=open(fn).readline().strip()
c=computer(pgm)
