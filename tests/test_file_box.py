"""file-box test"""
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
