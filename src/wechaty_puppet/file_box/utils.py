"""
file-box utils functions
"""
import mimetypes
import os
from typing import Tuple
from urllib.parse import urlparse
import requests
import uuid


def data_url_to_base64(data_url: str) -> str:
    """
    transfer the DataUrl to base64 format

    data_url:  dataURL: `data:image/png;base64,${base64Text}`,

    return :
    """
    if ',' not in data_url:
        raise ValueError('DataUrl value is not valid, value: %s', data_url)

    return data_url.split(',')[-1]


def _extract_content_type(content_type: str) -> str:
    """extract content type"""
    if ';' in content_type:
        content_type = content_type.split(';')[0]

    if '/' in content_type:
        content_type = content_type.split('/')[-1]
    return content_type


def extract_file_name_from_url(url: str) -> Tuple[str, str]:
    """
    """
    # if we can guess the type from url
    res = requests.get(url)
    content_type = _extract_content_type(res.headers.get('Content-Type', ''))

    if mimetypes.guess_type(url)[0]:
        url_path = urlparse(url).path

        try:
            # refer to : https://stackoverflow.com/a/18727481/6894382
            file_name = os.path.basename(url_path)
            return file_name, content_type
        except TypeError as type_error:
            # return then random name of the file
            file_type, _ = mimetypes.guess_type(url)
            assert file_type is not None
            return '{}.{}'.format(str(uuid.uuid4()), file_type.split('/')[0]), \
                   content_type
    else:

        if res.status_code != 200:
            raise FileNotFoundError('can"t get the file from url <%s>' % url)

        if '?' in url:
            url = url[:url.index('?')]

        if url.endswith('/'):
            url = url[:-1]

        suffix = ''
        if not url.endswith(f'.{content_type}'):
            # if the url contains the file-name, so return it
            suffix = f'.{content_type}'

        file_name = f'{url[url.rindex("/")+1 :]}{suffix}'
        return file_name, content_type
