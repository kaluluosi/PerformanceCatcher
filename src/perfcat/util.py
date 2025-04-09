'''
author:        kaluluosi111 <kaluluosi@gmail.com>
date:          2025-04-10 00:02:19
Copyright © Kaluluosi All rights reserved
'''
from importlib import resources

def is_nuitka():
    return "__compiled__" in globals()

def read_text(package:str, file:str)->str:
    """
    读取包内文件内容

    Args:
        package (str): 包路径
        file (str): 文件名

    Returns:
        str: 文件内容
    """
    if is_nuitka():
        package = package.replace(".", "/")
        with open(f"{package}/{file}", "r", encoding="utf-8") as f:
            return f.read()
    else:
        return resources.read_text(package, file, encoding="utf-8")
    
def get_path(package:str, file:str) ->str:
    """
    获取包内文件路径

    Args:
        package (str): 包路路径
        file (str): 文件名

    Returns:
        str: 文件路径
    """
    # 判断是否使用nuitka编译
    if is_nuitka():
        # 将package中的"."替换为"/"
        package = package.replace(".", "/")
        # 返回package和file的拼接路径
        return f"{package}/{file}"
    else:
        # 使用resources模块获取package和file的路径
        with resources.path(package, file) as p:
            # 返回路径
            return str(p)
        
        