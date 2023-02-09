import subprocess

def spawnProcessSync(process):
    p = subprocess.Popen(process, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    for line in p.stdout.readlines():
        print(line)
    p.wait()