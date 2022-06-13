"""file-box test"""
import json
import os
from typing import Optional

import tempfile

import pytest

from wechaty_puppet.file_box.file_box import FileBox
from wechaty_puppet.file_box.utils import extract_file_name_from_url


def generate_temp_voice_file(temp_dir: tempfile.TemporaryDirectory, file_name: Optional[str] = None):
    """generate the temp voice file

    Args:
        temp_dir: the path of temp dir
        file_name: the name of the voice file. Defaults to None.

    Returns:
        the path of the temp voice file
    """
    file_name = os.path.join(temp_dir.name, file_name or 'test.silk')
    with open(file_name, 'wb') as f:
        f.write(b'test content')
    return file_name
    

def test_url_parse_with_file_name():
    url = 'https://wechaty.js.org/img/wechaty-logo.svg'
    extracted_file_name, _ = extract_file_name_from_url(url)
    assert extracted_file_name == 'wechaty-logo.svg'


def test_url_parse_with_suffix():
    url = 'https://wechaty.js.org/img/wechaty-logo.svg?name=23'
    extracted_file_name, _ = extract_file_name_from_url(url)
    assert extracted_file_name, _ == 'wechaty-logo.svg'


def test_url_parse_with_html_page():
    url = 'https://wechaty.js.org/'
    extracted_file_name, _ = extract_file_name_from_url(url)
    assert extracted_file_name == 'wechaty.js.org.html'


def test_to_json_str():
    file_box = FileBox.from_base64('', name='test.file')
    json_string = file_box.to_json_str()
    json_data = json.loads(json_string)
    assert 'mimeType' in json_data
    assert '_mimType' not in json_data
    

def test_to_json_str_check_data():
    file_box = FileBox.from_base64('', name='test.file')
    file_box.mimeType = 'text/plain'
    file_box.mediaType = 'text/media'

    json_string = file_box.to_json_str()
    json_data = json.loads(json_string)
    assert 'mimeType' in json_data
    assert json_data['mimeType'] == 'text/media'
    assert json_data['mediaType'] == 'text/media'


@pytest.mark.parametrize(
    "file_name",
    [
        None,
        'test.silk',
        'test.sil',
        'test.slk'
    ]
)
def test_silk_voice_file(file_name: str):
    temp_dir = tempfile.TemporaryDirectory()
    voice_file = generate_temp_voice_file(temp_dir=temp_dir, file_name=file_name)
    file_box = FileBox.from_file(voice_file)
    file_box.metadata = {
        'voiceLength': 2000
    }
    json_string = json.loads(file_box.to_json_str())

    assert file_box.name.endswith('.sil')
    assert json_string['metadata']['voiceLength'] == 2000
    assert json_string['mediaType'] == 'audio/silk'
