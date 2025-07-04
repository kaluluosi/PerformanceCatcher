:: 移除build dist目录
rd /s /q build 2>nul
rd /s /q dist 2>nul

nicegui-pack.exe ^
--name PerformanceCatcher ^
--icon=icon.ico ^
--add-data src\perfcat\static:perfcat\static ^
--add-data src\perfcat\media:perfcat\media ^
--add-data src\perfcat\adb:perfcat\adb ^
--windowed .\prod.py