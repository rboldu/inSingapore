import socket	#for TCP communication

TCP_IP = '192.168.1.250'
TCP_PORT = 50000

version='1'
command='11'
group='1'
constant_light='1'
block='1'
scene='1'
fade_time='1'
#group = input('Enter group number:')

#V:version/C:command_number/G:group_number/K:constant_light/B:block/S:scene/F:fade_time
#command = '>V:%s,C:%s,G:%s,K:%s,B:%s,S:%s,F:%s,@1.250.2.1#' %(version,command,group,constant_light,block,scene,fade_time)

command='>V:1,C:14,L:60,F:1,@1.250.2.6#'

command='>V:1,C:14,L:100,F:1,@1.250.2.2.10#'
#command='>V:1,C:12,B:1,S:1,F:100,@1.250.2.2.10#' #<<<<<<<-----TRY THIS
#command='>V:1,C:14,L:60,F:9000,@1.250.2.10#'
print command
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(command)
s.close()