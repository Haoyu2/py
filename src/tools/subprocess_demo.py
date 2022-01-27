import subprocess, os, platform
from collections import namedtuple

from rich import print
print(platform.system())

CMD = namedtuple('CMD', ['cmd', 'error'])
if platform.system() == 'Windows':  cmd = CMD('dir', 'ls')
elif platform.system() == 'Linux':  cmd = CMD('ls', 'dir')
print(cmd.cmd)
# subprocess.run(cmd.cmd)
p1 = subprocess.run(cmd.cmd, shell=True, capture_output=True)


# print(p1.stdout.decode())

p2 = subprocess.run(cmd.error, shell=True, capture_output=True,  text=True)
print(p2.stderr)
print(p2.stdout)


p3 = subprocess.Popen(cmd.cmd, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
for line in iter(p3.stdout.readline,""):
    print(line)
print(p3.stdout)
print('=============')
with subprocess.Popen('ipconfig', text=True) as process:
    process.wait(timeout=2)
    while process.poll() is None:
        # print(process.poll())
        print(process.communicate())