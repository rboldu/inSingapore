from dali_lights import *
import time

dali_ip='192.168.1.250'
dali_port=50000

dali_group_2=dali_lights(dali_ip,dali_port,2)
dali_group_3=dali_lights(dali_ip,dali_port,1)

#dali_group_3.setOn()
dali_group_2.Increase()
time.sleep(2)
dali_group_2.setOff()


dali_group_2.getId()
dali_group_3.getId()
#print a