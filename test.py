import subprocess


path = r"E:\Program Files\adb\adb.EXE"
cmd = r"{path} start-server".format(path=path)
print(cmd)
subprocess.call([path, 'start-server'], shell=True)
