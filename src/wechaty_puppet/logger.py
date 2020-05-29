"""
Python Wechaty - https://github.com/wechaty/python-wechaty

Authors:    Huan LI (李卓桓) <https://github.com/huan>
            Jingjing WU (吴京京) <https://github.com/wj-Mcat>

2020-now @ Copyright Wechaty

Licensed under the Apache License, Version 2.0 (the 'License');
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an 'AS IS' BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from __future__ import annotations
import logging
import os


def get_logger(name: str) -> logging.Logger:
    """
    configured Loggers
    """
    WECHATY_LOG_KEY = 'WECHATY_LOG'

    if WECHATY_LOG_KEY in os.environ:
        WECHATY_LOG = os.environ[WECHATY_LOG_KEY].upper()
    else:
        WECHATY_LOG = 'INFO'

    LOGGER_LEVELS = [
        'CRITICAL',
        'ERROR',
        'WARNING',
        'INFO',
        'DEBUG',
    ]

    if WECHATY_LOG in LOGGER_LEVELS:
        level = getattr(logging, WECHATY_LOG, logging.INFO)
    else:
        level = logging.INFO

    _log = logging.getLogger(name)
    _log.setLevel(level)

    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    handler.setFormatter(formatter)

    # add ch to logger
    _log.addHandler(handler)

    return _log
