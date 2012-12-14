#!/usr/bin/env python
# -*- coding: utf-8 -*-
print "Welcome to kinetic energy calculation script.."
m = input("Put mass of object[kg]:")
v = input("Put speed of object[m/sec]:")
import math
kinetic = (1.0/2.0)*m*math.pow(v,2)
print "Kinetic energy of object:%s Newton" %(kinetic)
