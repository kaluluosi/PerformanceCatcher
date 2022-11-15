from ppadb.client import Client
from ppadb.device import Device

adb = Client()


app_name = "com.xinyuan.w9"


dev: Device = adb.devices()[0]

surface_info: str = dev.shell("dumpsys SurfaceFlinger --list")

surface_infos = surface_info.split("\n")

surface_views = filter(lambda txt: txt.startswith("SurfaceView"), surface_infos)
surface_views = list(surface_views)
if surface_views:
    last_surface_view = surface_views[-1]
    print(last_surface_view)


app_surface_infos = []

# lines = len(surface_infos)
# cur_line = 0
# k = 0  # ??

# while cur_line < lines:
#     surface_info = surface_infos[cur_line]
#     if surface_info:
#         if app_name in surface_info:
#             app_surface_infos.append(surface_info)

#         if "SurfaceView" == surface_info.strip():
#             k = cur_line

#     cur_line += 1

# if len(app_surface_infos) > 0:
#     for j in range(len(app_surface_infos) - 1, -1, -1):
#         i = len(app_surface_infos)
#         if app_surface_infos[j].startswith("SurfaceView"):
#             continue
#         i = j
#         break

#     surface_info = app_surface_infos[i].strip()
# elif k != 0:
#     surface_info = "SurfaceView"


# print(surface_info)
