import sys
from smart_plug import *
from switch import *
from dali_lights import *
import time

ip='192.168.81.1'
port='3480'

dali_ip='192.168.1.250'
dali_port='50000'

switch4 = switch(ip,port,id=4)

switch4.setOn()
time.sleep(10)
switch4.setOff()

'''
k=switch4.getId()
print k

l=switch4.Increase_val(78)

m=switch4.getIntensity()
print m


#switch4.setId(4)
switch5 = smart_plug(ip,port)
switch5.setId(5)

switch4.setCategory('Light')

switch4.setOff()

switch4.setOn()

k=switch5.getId()
print k

l=switch4.getStatus()
print l

switch4.setIntensity(20)

switch4.Increase_val(50)

p=switch4.getIntensity()
print p

j=switch4.getWhoIm()
print j

for x in range(0, 3):
	switch4.Increase()
	time.sleep(0.5)

p=switch4.getIntensity()
print p

print '---------------------dali testing------------------------'

dali_group_2=dali_lights(dali_ip,dali_port)
dali_group_2.setGroup(2)

dali_group_2.setOn()

a=dali_group_2.getGroup()
print a

device = input('Enter group number:')

if(device==4):
	print 'device 4'
elif(device==5):
	print'device 5'
'''




