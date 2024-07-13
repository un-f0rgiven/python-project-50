import pytest

@pytest.fixture
def first_coll_json():
    return 'file1.json'

@pytest.fixture
def second_coll_json():
    return 'file2.json'

@pytest.fixture
def first_coll_yml():
    return 'file1.yaml'

@pytest.fixture
def second_coll_yml():
    return 'file2.yaml'
