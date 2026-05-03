import subprocess

getoutput = subprocess.getoutput("df -h")
print(getoutput)
