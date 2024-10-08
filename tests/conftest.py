import pytest
import json
import yaml
import os

FIXTURES_PATH = 'tests/fixtures/'


@pytest.fixture
def test_file1_json():
    config_file_path = os.path.join(
        os.path.dirname(__file__), FIXTURES_PATH, 'test_file1.json'
    )
    with open(config_file_path, 'r') as f:
        data = json.load(f)
    return data


@pytest.fixture
def test_file2_json():
    config_file_path = os.path.join(
        os.path.dirname(__file__), 'fixtures', 'test_file2.json'
    )
    with open(config_file_path, 'r') as f:
        data = json.load(f)
    return data


@pytest.fixture
def test_file1_yaml_():
    config_file_path = os.path.join(
        os.path.dirname(__file__), 'fixtures', 'test_file1.yaml'
    )
    with open(config_file_path, 'r') as f:
        data = yaml.safe_load(f)
    return data


@pytest.fixture
def test_file2_yaml():
    config_file_path = os.path.join(
        os.path.dirname(__file__), 'fixtures', 'test_file2.yaml'
    )
    with open(config_file_path, 'r') as f:
        data = yaml.safe_load(f)
    return data


@pytest.fixture
def test_file1_r_json():
    config_file_path = os.path.join(
        os.path.dirname(__file__), FIXTURES_PATH, 'test_file1_r.json'
    )
    with open(config_file_path, 'r') as f:
        data = json.load(f)
    return data


@pytest.fixture
def test_file2_r_json():
    config_file_path = os.path.join(
        os.path.dirname(__file__), FIXTURES_PATH, 'test_file2_r.json'
    )
    with open(config_file_path, 'r') as f:
        data = json.load(f)
    return data


@pytest.fixture
def test_file1_r_yaml():
    config_file_path = os.path.join(
        os.path.dirname(__file__), 'fixtures', 'test_file1_r.yaml'
    )
    with open(config_file_path, 'r') as f:
        data = yaml.safe_load(f)
    return data


@pytest.fixture
def test_file2_r_yaml():
    config_file_path = os.path.join(
        os.path.dirname(__file__), 'fixtures', 'test_file2_r.yaml'
    )
    with open(config_file_path, 'r') as f:
        data = yaml.safe_load(f)
    return data


@pytest.fixture
def stylish_format_result():
    with open(os.path.join(FIXTURES_PATH, 'stylish_format.txt'), 'r') as f:
        return f.read().strip()


@pytest.fixture
def plain_format_result():
    with open(os.path.join(FIXTURES_PATH, 'plain_format.txt'), 'r') as f:
        return f.read().strip()


@pytest.fixture
def json_format_result():
    with open(os.path.join(FIXTURES_PATH, 'json_format.txt'), 'r') as f:
        return f.read().strip()
