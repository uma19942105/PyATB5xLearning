import pytest
import allure
import requests
import os
import ctypes

class MyClass:
    _type_ = "example_type"

from functools import lru_cache


class SHGetFolderPathW:
    pass


@lru_cache(maxsize=None)
def _pick_get_win_folder():
    CSIDL_WINDOWS = 0x0024
    SHGFP_TYPE_CURRENT = 0
    buf = ctypes.create_unicode_buffer(260)
  #  ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_WINDOWS, None, SHGFP_TYPE_CURRENT, buf)
    SHGetFolderPathW(None, CSIDL_WINDOWS, None, SHGFP_TYPE_CURRENT, buf)
    return buf.value

# Get the path to the Windows folder
get_win_folder = _pick_get_win_folder()
print(get_win_folder)


@allure.title("Tc#1- to verify that 2-2==0")
@allure.description("this is a BASIC MAth Test")
@pytest.mark.smoke
def test_basic_math():
  #  assert 2-2 ==0
    print("test1")


@allure.title("Tc#2- to verify that 3-3==0")
@allure.description("this is a BASIC MAth Test")
@pytest.mark.regression
def test_basic_math():
    print("test1")

 #   assert 2-2 ==0
