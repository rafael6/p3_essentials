import subprocess

args = ["ping", "-c 1", "www.yahoo.com"]
process = subprocess.Popen(args, stdout=subprocess.PIPE)

data = process.communicate()
for line in data:
    print(line)