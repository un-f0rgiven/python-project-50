from gendiff.scripts.generate_diff import generate_diff
import pytest

@pytest.fixture
def first_coll_json():
    return 'file1.json'

@pytest.fixture
def second_coll_json():
    return 'file2.json'

def test_generate_diff(first_coll_json, second_coll_json):
    result = generate_diff(first_coll_json, second_coll_json)
    assert result == '{\n- follow: false\n  host: hexlet.io\n- proxy: 123.234.53.22\n- timeout: 50\n+ timeout: 20\n+ verbose: true\n}'

@pytest.fixture
def first_coll_yml():
    return 'file1.yml'

@pytest.fixture
def second_coll_yml():
    return 'file2.yml'

def test_generate_diff(first_coll_yml, second_coll_yml):
    result = generate_diff(first_coll_yml, second_coll_yml)
    assert result == '{\n- follow: false\n  host: hexlet.io\n- proxy: 123.234.53.22\n- timeout: 50\n+ timeout: 20\n+ verbose: true\n}'
