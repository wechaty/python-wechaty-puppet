"""file-box test"""
import pytest
from wechaty_puppet.file_box.utils import extract_file_name_from_url


def test_url_parse_with_file_name():
    url = 'https://img2020.cnblogs.com/blog/2042116/202006/2042116-202006281' \
          '63052872-2123530534.png'
    extracted_file_name, _ = extract_file_name_from_url(url)
    assert extracted_file_name == '2042116-20200628163052872-2123530534.png'


def test_url_parse_with_suffix():
    url = 'https://img2020.cnblogs.com/blog/2042116/202006/2042116-202006281' \
          '63052872-2123530534.png?name=23'
    extracted_file_name, _ = extract_file_name_from_url(url)
    assert extracted_file_name, _ == '2042116-20200628163052872-2123530534.png'


def test_url_parse_with_html_page():
    url = 'https://www.csdn.net/'
    extracted_file_name, _ = extract_file_name_from_url(url)
    assert extracted_file_name == 'www.csdn.net.html'


def test_url_parse_with_():
    url = 'https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWdrci5jbi1iai51ZmlsZW9z' \
          'LmNvbS9lMGZlYzAxNC0yNjkxLTRkZmUtOTc5NS1iNGU2NzdmYTE2ZTcucG5n?x-oss' \
          '-process=image/format,pngv'
    extracted_file_name, _ = extract_file_name_from_url(url)
    assert extracted_file_name == 'aHR0cHM6Ly9pbWdrci5jbi1iai51ZmlsZW9zLmNv' \
                                  'bS9lMGZlYzAxNC0yNjkxLTRkZmUtOTc5NS1iNGU2' \
                                  'NzdmYTE2ZTcucG5n.jpeg'

