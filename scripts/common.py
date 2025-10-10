import os
import sys


def setup_project_paths():
    """
    设置项目路径，确保能够正确导入项目中的模块
    
    返回:
        dict: 包含项目相关路径的字典
    """
    # 获取当前脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__))
    
    # 获取项目根目录
    project_root = os.path.dirname(script_dir)
    
    # 获取src目录
    src_dir = os.path.join(project_root, 'src')
    
    # 将项目根目录和src目录添加到sys.path
    if project_root not in sys.path:
        sys.path.append(project_root)
    if src_dir not in sys.path:
        sys.path.append(src_dir)
    
    # 返回路径信息，供调用者使用
    return {
        'script_dir': script_dir,
        'project_root': project_root,
        'src_dir': src_dir
    }


# 提供一个简单的函数来初始化路径
def init_project():
    """\初始化项目路径"""
    return setup_project_paths()