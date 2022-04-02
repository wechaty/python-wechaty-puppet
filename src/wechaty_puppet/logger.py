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
from typing import Optional


WECHATY_LOG_KEY = 'WECHATY_LOG'
WECHATY_LOG_FILE_KEY = 'WECHATY_LOG_FILE'
DEFAULT_LOG_LEVEL = 'INFO'


def _get_logger_level() -> str:
    """refer to : https://docs.python.org/3/library/logging.html#logging-levels

    fix: https://github.com/wechaty/python-wechaty/issues/192

    According to our Wechaty Specification <https://wechaty.js.org/docs/specs/wechaty>:
    The `WECHATY_LOG` should support the values of `silly`, `verbose`, `info`, `warn`, `silent`
    All Polyglot Wechaty should at least support the above names as an alias.
    Link to https://github.com/wechaty/wechaty/issues/2167
    """
    level_map = {
        'silly': 'CRITICAL',
        'verbose': 'INFO',
        'info': 'INFO',
        'warn': 'WARNING',
        'error': 'ERROR',
        'silent': 'NOTSET'
    }
    level: str = os.environ.get(WECHATY_LOG_KEY, DEFAULT_LOG_LEVEL).lower()
    if level not in level_map:
        raise ValueError(
            f'{WECHATY_LOG_KEY} should support the values of `silly`, '
            '`verbose`, `info`, `warn`, `error`, `silent`'
        )
    return level_map.get(level, DEFAULT_LOG_LEVEL)


def get_logger(name: Optional[str] = None, file: Optional[str] = None) -> logging.Logger:
    """get the logger object

    Args:
        name (str): the logger name
        file (Optional[str], optional): the log file name. Defaults to None.

    Examples:
        >>> logger = get_logger("WechatyPuppet")
        >>> logger = get_logger("WechatyPuppet", file="wechaty-puppet.log")
        >>> logger.info('log info ...')

    Returns:
        logging.Logger: the logger object
    """
    WECHATY_LOG = _get_logger_level()

    log_formatter = logging.Formatter(
        fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # create logger and set level to debug
    logger = logging.getLogger(name)
    logger.handlers = []
    logger.setLevel(WECHATY_LOG)
    logger.propagate = False

    # create file handler and set level to debug
    file = os.environ.get(WECHATY_LOG_FILE_KEY, file)
    if file:
        file_handler = logging.FileHandler(file, 'a', encoding='utf-8')
        file_handler.setLevel(WECHATY_LOG)
        file_handler.setFormatter(log_formatter)
        logger.addHandler(file_handler)

    # create console handler and set level to info
    console_handler = logging.StreamHandler()
    console_handler.setLevel(WECHATY_LOG)
    console_handler.setFormatter(log_formatter)
    logger.addHandler(console_handler)

    return logger
