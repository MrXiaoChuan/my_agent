"""
    时间工具模块
    提供获取当前时间等日期相关的工具函数。
"""

from datetime import datetime
from langchain_core.tools import tool

@tool
def get_current_date() -> str:
    """获取当前的日期和时间。当需要知道今天几号、现在几点时，可以使用此工具。"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
