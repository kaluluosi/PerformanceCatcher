nuitka ^
--standalone ^
--follow-imports ^
--show-progress ^
--plugin-enable=pyside6 ^
--include-data-dir=src/perfcat/assets=perfcat/assets  ^
--include-data-dir=src/perfcat/adb=perfcat/adb  ^
--output-dir=dist\win ^
--windows-disable-console ^
--windows-icon-from-ico=src/perfcat/assets/logo.ico ^
--windows-company-name="xinyuanstudio" ^
--windows-file-version="1.0.0" ^
--windows-file-description="性能测试工具" ^
.\src\perfcat\PerfCat.py
