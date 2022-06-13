from wechaty_puppet.file_box.utils import get_json_data

class FakeObject:
    def __init__(self) -> None:
        self._metadata = {
            'init_data': 'init_data',
        }

        self.field = 0
    
    @property
    def metadata(self):
        return self._metadata
    
    @metadata.setter
    def metadata(self, value):
        self._metadata = value


def test_get_json_data():
    fake_obj = FakeObject()

    json_data = get_json_data(fake_obj)
    assert json_data['field'] == 0
    assert json_data['metadata']['init_data'] == 'init_data'

    fake_obj.metadata = {
        'data': 'data'
    }
    json_data = get_json_data(fake_obj)
    assert json_data['metadata']['data'] == 'data'
    assert 'init_data' not in json_data['metadata']
