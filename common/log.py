import logging
from logging.handlers import TimedRotatingFileHandler
import sys


def _get_logger():
    base_format = logging.Formatter('[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d] - %(message)s',
                                                  datefmt='%Y-%m-%d %H:%M:%S')
    log = logging.getLogger('log')
    log.setLevel(logging.DEBUG)


    #控制台控制器
    console_handle = logging.StreamHandler(sys.stdout)
    console_handle.setFormatter(base_format)
    console_handle.setLevel(logging.INFO)
    log.addHandler(console_handle)

    #文件控制器
    #debug信息
    time_rotating_file_handler = TimedRotatingFileHandler(filename='./log/debug.log', when='D', encoding='utf-8')
    time_rotating_file_handler.setLevel(logging.DEBUG)
    time_rotating_file_handler.setFormatter(base_format)
    log.addHandler(time_rotating_file_handler)

    #error信息
    time_rotating_file_Error_handler = TimedRotatingFileHandler(filename='./log/error.log', when='D', encoding='utf-8')
    time_rotating_file_Error_handler.setLevel(logging.ERROR)
    time_rotating_file_Error_handler.setFormatter(base_format)
    log.addHandler(time_rotating_file_Error_handler)
    return log


# 日志句柄
logger = _get_logger()