import signal
import sys
from sshopen import openssh
import time
import datetime
from datetime import datetime
 
ip = '172.31.65.128'
usr = 'amrit'
psw = '1541'
ssh = openssh(ip,usr,psw)

#do jobs
remotePath = "/home/amrit/logs/convlog.txt"
message = "JASPER ! HOW ARE YOU"
ts = time.time()
timestamp = datetime.fromtimestamp(ts).strftime('%d-%m-%Y %H:%M:%S')
cmd = "echo " + timestamp + ":" + message + " >> " + remotePath
print "Executing "+cmd
ssh.exec_command(cmd)









ssh.close()

#signal handler
def signal_handler(sig, frame):
        print('You pressed Ctrl+C! Closing ssh connection')
        ssh.close()
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler) 
#signal.pause()


