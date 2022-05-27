"""file-box test"""
import json
from wechaty_puppet.file_box.file_box import FileBox
from wechaty_puppet.file_box.utils import extract_file_name_from_url


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