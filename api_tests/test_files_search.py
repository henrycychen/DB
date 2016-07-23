"""
This is a Dropbox API. All information can be found at the below web address:
https://www.dropbox.com/developers/documentation/http/documentation.
"""
import tempfile
import json
import pytest
import time
import os
import requests
from helper_library_DB import Dropbox
from helper_library_DB import Fake
from helper_library_DB import my_fixture

d = Dropbox()
f = Fake()

@pytest.mark.search
def test_search_valid(my_fixture):
    print "\n This is my test"

    my_data2 = {"path": "", "query": fake_name}
    r2 = d.db_search(my_data2=my_data2)
    check_assert = json.loads(r2.text)['matches'][0]['metadata']['name']
    assert check_assert == fake_name

"""
@pytest.mark.search
def test_search_invalid():
    assert True == False

@pytest.mark.search
def test_search_path_valid():
    assert True == False

@pytest.mark.search
def test_search_path_invalid():
    assert True == False

@pytest.mark.search
def test_search_query_valid():
    assert True == False

@pytest.mark.search
def test_search_query_invalid():
    assert True == False

@pytest.mark.search
def test_search_exact_name_search():
    assert True == False

@pytest.mark.search
def test_search_partial_name_search():
    assert True == False

@pytest.mark.search
def test_search_what_if_same_file_in_different_folder():
    assert True == False

@pytest.mark.search
def test_search_wrong_filename():
    assert True == False

@pytest.mark.search
def test_search_by_file_ext():
    assert True == False

@pytest.mark.search
def test_search_what_if_file_and_folder_have_same_name_what_output_returned()
    assert True == False

@pytest.mark.search
def test_search_start_valid():
    assert True == False

@pytest.mark.search
def test_search_start_invalid():
    assert True == False

@pytest.mark.search
def test_search_max_result_valid():
    assert True == False

@pytest.mark.search
def test_search_max_result_invalid():
    assert True == False

@pytest.mark.search
def test_search_mode_filename():
    assert True == False

@pytest.mark.search
def test_search_mode_filename_and_content():
    assert True == False

@pytest.mark.search
def test_search_mode_deleted_file_name():
    assert True == False
"""