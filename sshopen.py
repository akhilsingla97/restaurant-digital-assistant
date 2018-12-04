import os
import paramiko
import time

def openssh(ip,usr,psw):
  print("Opening SSH connection to "+ usr + "@" +ip)
  ssh = paramiko.SSHClient()
  ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  ssh.connect(ip, username=usr, password=psw)
  return ssh
