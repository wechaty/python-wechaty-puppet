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

from dataclasses import Field, dataclass, fields, is_dataclass, MISSING
import importlib
import os

from typing import Any, Dict, List, Optional, Tuple

from wechaty_puppet.logger import get_logger

logger = get_logger('WechatyPuppet.Schema.Base')


def _get_verison_wechaty_related_package(module_name: str) -> Optional[str]:
    """
    get the version of wechaty related package
    """
    if not module_name.endswith('.version'):
        module_name += '.version'
    try:
        module = importlib.import_module(module_name)
        version = None
        if hasattr(module, 'VERSION'):
            version = getattr(module, 'VERSION')
        return version
    except ImportError:
        return None


def _guess_token_type() -> str:
    token = os.environ.get('WECHATY_PUPPET_SERVICE_TOKEN', None) or \
        os.environ.get('TOKEN', None) or \
        os.environ.get('token', None) or None
    unknown_token = '<unkonwn> token'
    if not token:
        return unknown_token
    
    if token.startswith('puppet_padlocal_'):
        return 'padlocal'
    if token.startswith('puppet_wxwork'):
        return 'wxwork'
    return unknown_token


@dataclass
class BaseDataClass:
    """Abstract Event Payload which handle initialization"""

    def __init__(self, **kwargs) -> None:

        all_fields = fields(self)
        invalid_fields = self.check_fields(kwargs)
        if invalid_fields:
            BaseDataClass._print_warning_about_dataclass_fields(self, kwargs)

            for invalid_field in invalid_fields:
                kwargs.pop(invalid_field)

        for field in all_fields:
            value = kwargs.get(field.name, None)
            if value is None:
                value = field.default

            # type: ignore
            if field.default_factory is not MISSING:
                # type: ignore
                value = field.default_factory()

            if value is MISSING:
                raise ValueError(
                    f'the field<{field.name}> is required in dataclass<{type(self)}>'
                )

            setattr(self, field.name, value)

    @classmethod
    def check_fields(cls, kwargs: Dict[str, Any]) -> List[str]:
        """check if the input data is valid to initialize the dataclass

        Args:
            cls (subclass of EventPayloadBase): the type of the dataclass
            kwargs (Dict[str, Any]): the input data

        Returns:
            List[str]: the invalid fields
        """
        if not is_dataclass(cls):
            raise TypeError(f'{cls} is not a subclass of EventPayloadBase')

        dataclass_fields: List[Field] = [field for field in fields(cls)]
        dataclass_field_names: set = {
            field.name for field in dataclass_fields}
        return list(set(kwargs.keys()) - dataclass_field_names)

    @staticmethod
    def _print_warning_about_dataclass_fields(obj, kwargs: Dict[str, Any]):
        """print warning info and notice that the developer
        can post issue to help python-wechaty to improve the quality of code

        Args:
            obj (_type_): the instance of the dataclass
            kwargs (Dict[str, Any]): the arguments of __init__ function 
        """
        # 1. check if the obj is a dataclass
        if not is_dataclass(obj):
            return

        # 2. get invalid fields
        invalid_fields = BaseDataClass.check_fields(kwargs)
        if not invalid_fields:
            return

        # 3. get the version of token/wechaty/wechaty-puppet/wechaty-puppet-service packages
        package_versions = {
            "wechaty": "0.0.0",
            "wechaty_puppet": "0.0.0",
            "wechaty_puppet_service": "0.0.0",
        }
        for package_module, default_version in package_versions.items():
            package_version = _get_verison_wechaty_related_package(
                package_module)
            package_versions[package_module] = package_version or default_version

        # 5. guess the token type
        token_type = _guess_token_type()

        # 4. print warning info
        logger.warning(
            f'invalid fields: <{invalid_fields}> to initialize type<{type(obj)}> '
            'which are should not be here, we suggest that you should post an issue to python-wechaty to fix this issue \n'
            'you should give these infos: \n'
            f'* the version of wechaty: \t\t\t{package_versions["wechaty"]}\n'
            f'* the version of wechaty_puppet: \t\t{package_versions["wechaty_puppet"]}\n'
            f'* the version of wechaty_puppet_service: \t{package_versions["wechaty_puppet_service"]}\n'
            f'* the token type: {token_type} \n'
        )
