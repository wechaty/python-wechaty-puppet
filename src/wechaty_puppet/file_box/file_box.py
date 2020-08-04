"""
docstring
"""
from __future__ import annotations

import json
import base64
import requests
import os
from collections import defaultdict

from typing import (
    Type,
    Optional,
    Union,
)

import qrcode   # type: ignore

from .utils import extract_file_name_from_url, data_url_to_base64

from .type import (
    FileBoxOptionsFile,
    FileBoxOptionsUrl,
    FileBoxOptionsStream,
    FileBoxOptionsBuffer,
    FileBoxOptionsQrCode,
    FileBoxOptionsBase64,
    FileBoxOptionsBase,
    Metadata, FileBoxType)


class FileBoxEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')

        return json.JSONEncoder.default(self, obj)


class FileBox:
    """
    # TODO -> need to implement pipeable
    maintain the file content, which is sended by wechat
    """

    def __init__(self, options: FileBoxOptionsBase):

        self.mimeType: Optional[str] = None

        self._metadata: Metadata = defaultdict()

        self.name = options.name
        self.boxType: int = options.type.value

        if isinstance(options, FileBoxOptionsFile):
            self.localPath = options.path

        elif isinstance(options, FileBoxOptionsBuffer):
            self.buffer = options.buffer

        elif isinstance(options, FileBoxOptionsUrl):
            self.remoteUrl = options.url
            self.headers = options.headers

        elif isinstance(options, FileBoxOptionsStream):
            # TODO -> need to get into detail for stream sending
            pass

        elif isinstance(options, FileBoxOptionsQrCode):
            self.qrCode = options.qr_code

        elif isinstance(options, FileBoxOptionsBase64):
            self.base64 = options.base64

    @property
    def metadata(self) -> dict:
        """
        get meta data for file-box
        """
        return self._metadata

    @metadata.setter
    def metadata(self, data: Metadata):
        """
        set meta data for file-box
        :param data:
        :return:
        """
        self._metadata.update(data)

    def type(self) -> FileBoxType:
        """get filebox type"""
        return FileBoxType(self.boxType)

    async def ready(self):
        """
        sync the name from remote
        """
        if self.type() == FileBoxType.Url:
            await self.sync_remote_name()

    async def sync_remote_name(self):
        """sync remote name
        refer : https://developer.mozilla.org/en-US/docs/Web/HTTP/
                Headers/Content-Disposition

                Content-Disposition: attachment; filename="cool.html"

        # wujingjing comment 2020-6-29:  according the implementation of
            file-box: https://github.com/huan/file-box/blob/e42d7207bb1cf5
                b76afb8ead6f72715f4a197b35/src/misc.ts#L66

            headers in requests package doesn't contains attribute:
                content-disposition, so we need to change the way to sync
                file-name from url type

            I find the better way to extract file name from url:
                https://stackoverflow.com/questions/18727347/how-to-extract-a-
                filename-from-a-url-append-a-word-to-it/18727481#18727481
        """
        file_box_type = self.type()
        if file_box_type != FileBoxType.Url:
            raise TypeError('type <{0}> is not remote'.format(
                file_box_type.name))

        if not hasattr(self, 'remoteUrl'):
            raise AttributeError('not have attribute url')

        url = getattr(self, 'remoteUrl')
        self.name, self.mimeType = extract_file_name_from_url(url)

    def to_json_str(self) -> str:
        """
        dump the file content to json object
        :return:
        """
        json_data = {}
        for key in self.__dict__:
            if getattr(self, key) is not None:
                json_data[key] = getattr(self,key)

        data = json.dumps(json_data, cls=FileBoxEncoder, indent=4)
        return data

    async def to_file(self, file_path: Optional[str] = None,
                      overwrite: bool = False):
        """
        save the content to the file
        :return:
        """
        if self.type() == FileBoxType.Url:
            if not self.mimeType or not self.name:
                await self.sync_remote_name()

        file_path = self.name if file_path is None else file_path

        if os.path.exists(file_path) and not overwrite:
            raise FileExistsError(f'FileBox.toFile(${file_path}): file exist. '
                                  f'use FileBox.toFile(${file_path}, true) to '
                                  f'force overwrite.')
        file_box_type = self.type()

        if file_box_type == FileBoxType.Buffer:
            with open(file_path, 'wb+') as f:
                f.write(self.buffer)

        elif file_box_type == FileBoxType.Url:
            with open(file_path, 'wb+') as text_io:
                # get the content of the file from url
                res = requests.get(self.remoteUrl)
                text_io.write(res.content)

        elif file_box_type == FileBoxType.QRCode:
            with open(file_path, 'wb+') as f:
                # create the qr_code image file
                img = qrcode.make(self.qrCode)
                img.get_image().save(f)

        elif file_box_type == FileBoxType.Base64:
            data = base64.b64decode(self.base64)
            with open(file_path, 'wb') as f:
                f.write(data)

    def to_base64(self) -> str:
        """
        transfer file-box to base64 string
        :return:
        """
        # TODO -> need to implement other data format
        return ''

    @classmethod
    def from_url(cls: Type[FileBox], url: str, name: Optional[str],
                 headers: Optional[dict] = None) -> FileBox:
        """
        create file-box from url
        """
        if name is None:
            response = requests.get(url)
            # TODO -> should get the name of the file
            name = response.content.title().decode(encoding='utf-8')
        options = FileBoxOptionsUrl(name=name, url=url, headers=headers)
        return cls(options)

    @classmethod
    def from_file(cls: Type[FileBox], path: str, name: Optional[str]
                  ) -> FileBox:
        """
        create file-box from file
        """
        if not os.path.exists(path):
            raise FileNotFoundError(f'{path} file not found')
        if name is None:
            name = os.path.basename(path)

        options = FileBoxOptionsFile(name=name, path=path)
        return cls(options)

    @classmethod
    def from_stream(cls: Type[FileBox], stream: bytes, name: str) -> FileBox:
        """
        create file-box from stream

        TODO -> need to implement stream detials
        """
        options = FileBoxOptionsStream(name=name, stream=stream)
        return cls(options)

    @classmethod
    def from_buffer(cls: Type[FileBox], buffer: bytes, name: str) -> FileBox:
        """
        create file-box from buffer

        TODO -> need to implement buffer detials
        """
        options = FileBoxOptionsBuffer(name=name, buffer=buffer)
        return cls(options)

    @classmethod
    def from_base64(cls: Type[FileBox], base64: str, name: str) -> FileBox:
        """
        create file-box from base64 str

        refer to the file-box implementation, name field is required.

        :param base64:
            example data: data:image/png;base64,${base64Text}
        :param name: name the file name of the base64 data
        :return:
        """
        options = FileBoxOptionsBase64(base64=base64, name=name)
        return FileBox(options)

    @classmethod
    def from_data_url(cls: Type[FileBox], data_url: str, name: str) -> FileBox:
        """
        example value: dataURL: `data:image/png;base64,${base64Text}`,
        """
        return cls.from_base64(
            data_url_to_base64(data_url),
            name
        )

    @classmethod
    def from_qr_code(cls: Type[FileBox], qr_code: str) -> FileBox:
        """
        create file-box from base64 str
        """
        options = FileBoxOptionsQrCode(name='qrcode.png', qr_code=qr_code)
        return cls(options)

    @classmethod
    def from_json(cls: Type[FileBox], obj: Union[str, dict]) -> FileBox:
        """
        create file-box from json data

        TODO -> need to translate :
            https://github.com/huan/file-box/blob/master/src/file-box.ts#L175

        :param obj:
        :return:
        """
        if isinstance(obj, str):
            json_obj = json.loads(obj)
        else:
            json_obj = obj

        # original box_type field name is boxType
        if 'boxType' not in json_obj:
            raise Exception('boxType field must be required')
        # assert that boxType value must match the value of FileBoxType values

        if json_obj['boxType'] == FileBoxType.Base64.value:
            file_box = FileBox.from_base64(
                base64=json_obj['base64'],
                name=json_obj['name']
            )
        elif json_obj['boxType'] == FileBoxType.Url.value:
            file_box = FileBox.from_url(
                url=json_obj['remoteUrl'],
                name=json_obj['name']
            )
        elif json_obj['boxType'] == FileBoxType.QRCode.value:
            file_box = FileBox.from_qr_code(
                qr_code=json_obj['qrCode']
            )
        else:
            raise ValueError('unknown file_box json object %s',
                             json.dumps(json_obj))

        if 'metadata' not in json_obj:
            json_obj['metadata'] = {}
        elif not isinstance(json_obj['metadata'], dict):
            raise AttributeError('metadata field is not dict type')

        file_box.metadata = json_obj['metadata']

        return file_box




