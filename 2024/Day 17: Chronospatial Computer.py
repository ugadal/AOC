#!/usr/bin/env python3
#
sep="\n\n"
fn,part="d17.txt",1
from ChronoComputer import computer
data=open(fn).read().split(sep)[part].splitlines()
rega=int(data[0].split(": ")[1])
regb=int(data[1].split(": ")[1])
regc=int(data[2].split(": ")[1])
instruct=list(map(int,data[3].split(": ")[1].split(",")))
print(instruct)
cc=computer(instruct,rega,regb,regc)
v=map(str,(cc.flow))
print(",".join(v))
