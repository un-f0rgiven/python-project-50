from gendiff.scripts.generate_diff import generate_diff
import pytest

@pytest.fixture
def first_coll():
    return 'file1.json'

@pytest.fixture
def second_coll():
    return 'file2.json'

def test_generate_diff(first_coll, second_coll):
    result = generate_diff(first_coll, second_coll)
    assert result == '{\n- follow: false\n  host: hexlet.io\n- proxy: 123.234.53.22\n- timeout: 50\n+ timeout: 20\n+ verbose: true\n}'
    print(result)


