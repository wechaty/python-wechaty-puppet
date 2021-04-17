"""unit test for logger"""
from __future__ import annotations

import os
from wechaty_puppet.logger import _get_logger_level


def test_get_log_level_info():
    os.environ['WECHATY_LOG'] = 'info'
    log_level = _get_logger_level()
    assert log_level == 'INFO'


def test_get_log_level_silly():
    os.environ['WECHATY_LOG'] = 'silly'
    log_level = _get_logger_level()
    assert log_level == 'CRITICAL'


def test_get_log_level_warn():
    os.environ['WECHATY_LOG'] = 'warn'
    log_level = _get_logger_level()
    assert log_level == 'WARNING'


def test_get_log_level_silent():
    os.environ['WECHATY_LOG'] = 'silent'
    log_level = _get_logger_level()
    assert log_level == 'NOTSET'


def test_get_log_level_error():
    os.environ['WECHATY_LOG'] = 'error'
    log_level = _get_logger_level()
    assert log_level == 'ERROR'
