#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
cp=str(sys.argv[0])
dre=re.compile(r"^Day (\d+):")
day=dre.findall(cp)[0]
fn,part=f"d{day}.txt",0
data=open(fn).read().split("\n\n")[part].splitlines()
