from importlib import resources
import os

files = resources.files("perfcat.adb")
adb_path = files.joinpath("adb.exe")
ret = os.system(f"{adb_path} start-server")
print("adb start-server return:",ret)

# print(os.path.join(os.path.dirname(__file__), "adb.exe"))