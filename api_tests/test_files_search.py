"""
This is a Dropbox API. All information can be found at the below web address:
https://www.dropbox.com/developers/documentation/http/documentation.
"""


import json
import pytest
import time
import requests
from helper_library_DB import Dropbox
from helper_library_DB import Fake
from helper_library_DB import my_fixture
from helper_library_DB import my_fixture2
from helper_library_DB import my_fixture3
from helper_library_DB import my_fixture4

d = Dropbox()
f = Fake()

@pytest.mark.search
def test_search_valid(my_fixture):
    time.sleep(30)
    my_data2 = {"path": "", "query": my_fixture}
    r2 = d.db_search(my_data2=my_data2)
    check_assert = json.loads(r2.text)['matches'][0]['metadata']['name']
    assert check_assert == my_fixture

@pytest.mark.search
def test_search_invalid():
    #Searched using query '///////' to make it invalid
    my_data2 = {"path": "", "query": '///////'}
    r2 = d.db_search(my_data2=my_data2)
    r2.status_code
    check_assert = json.loads(r2.text)['matches']
    assert check_assert == []

@pytest.mark.search
def test_search_path_valid(my_fixture):
    time.sleep(30)
    #Used the valid path where files are uploaded
    my_data2 = {"path": "/test", "query": my_fixture}
    r2 = d.db_search(my_data2=my_data2)
    check_assert = json.loads(r2.text)['matches'][0]['metadata']['path_lower']
    assert check_assert == "/test/"+my_fixture

@pytest.mark.search
def test_search_path_invalid(my_fixture):
    time.sleep(30)
    #Used an invalid path "/"
    my_data2 = {"path": "/", "query": ""}
    r2 = d.db_search(my_data2=my_data2)
    assert r2.status_code != 200

@pytest.mark.search
def test_search_exact_name_search(my_fixture):
    time.sleep(30)
    my_data2 = {"path": "", "query": my_fixture}
    r2 = d.db_search(my_data2=my_data2)
    check_assert = json.loads(r2.text)['matches'][0]['metadata']['name']
    assert check_assert == my_fixture

@pytest.mark.search
def test_search_partial_name_search(my_fixture):
    time.sleep(30)
    #my_fixture[0:4] will be used as a partial search
    my_data2 = {"path": "", "query": my_fixture[0:4]}
    r2 = d.db_search(my_data2=my_data2)
    check_assert = json.loads(r2.text)['matches'][0]['metadata']['name']
    assert check_assert == my_fixture

# File will appear in two different indexes when searched. Assert both
# file names are the same.
@pytest.mark.search
def test_search_what_if_same_file_in_different_folder(my_fixture2):
    time.sleep(30)
    my_data2 = {"path": "", "query": my_fixture2}
    r2 = d.db_search(my_data2=my_data2)
    check_assert1 = json.loads(r2.text)['matches'][0]['metadata']['name']
    check_assert2 = json.loads(r2.text)['matches'][1]['metadata']['name']
    assert check_assert1 == my_fixture2 and check_assert2 == my_fixture2

@pytest.mark.search
def test_search_wrong_filename(my_fixture):
    #Searched using query filename + additional info to make it invalid
    #result will return nothing.
    my_data2 = {"path": "", "query": my_fixture+"123"}
    r2 = d.db_search(my_data2=my_data2)
    r2.status_code
    check_assert = json.loads(r2.text)['matches']
    assert check_assert == []

@pytest.mark.search
def test_search_by_file_ext(my_fixture):
    time.sleep(30)
    #my_fixture[0:-4] will search by extension.
    my_data2 = {"path": "", "query": my_fixture[0:-4]}
    r2 = d.db_search(my_data2=my_data2)
    check_assert = json.loads(r2.text)['matches'][0]['metadata']['name']
    assert check_assert == my_fixture

#Test outcome will list two indexes. One as a folder and second as a file
@pytest.mark.search
def test_search_what_if_file_and_folder_have_same_name_what_output_returned(my_fixture3):
    time.sleep(30)
    my_data2 = {"path": "", "query": my_fixture3}
    r2 = d.db_search(my_data2=my_data2)
    check_assert1 = json.loads(r2.text)['matches'][0]['metadata']['name']
    check_assert2 = json.loads(r2.text)['matches'][1]['metadata']['name']
    check_assert3 = json.loads(r2.text)['matches'][0]['metadata']['.tag']
    check_assert4 = json.loads(r2.text)['matches'][1]['metadata']['.tag']
    assert check_assert1 == my_fixture3 and \
           check_assert2 == my_fixture3 and \
           check_assert3 == 'folder' and \
           check_assert4 == 'file'

#Test if the first page works after uploading a file
@pytest.mark.search
def test_search_start_valid(my_fixture):
    time.sleep(30)
    my_data2 = {"path": "", "query": my_fixture, "start": 0}
    r2 = d.db_search(my_data2=my_data2)
    assert r2.status_code == 200

@pytest.mark.search
def test_search_start_invalid(my_fixture):
    time.sleep(30)
    my_data2 = {"path": "", "query": my_fixture, "start": '/'}
    r2 = d.db_search(my_data2=my_data2)
    assert r2.status_code != 200

#Max returned search results is 100 items
@pytest.mark.search
def test_search_max_result_valid(my_fixture):
    time.sleep(30)
    my_data2 = {"path": "", "query": my_fixture, "max_results": 100}
    r2 = d.db_search(my_data2=my_data2)
    assert r2.status_code == 200


#Outcome should be html status code != 200. Error occurs at 1001
@pytest.mark.search
def test_search_max_result_invalid(my_fixture):
    time.sleep(30)
    my_data2 = {"path": "", "query": my_fixture, "max_results": 1001}
    r2 = d.db_search(my_data2=my_data2)
    assert r2.status_code != 200

#Will search for filenames and folders
@pytest.mark.search
def test_search_mode_filename(my_fixture3):
    time.sleep(30)
    my_data2 = {"path": "", "query": my_fixture3, "mode": {".tag":"filename"}}
    r2 = d.db_search(my_data2=my_data2)
    check_assert1 = json.loads(r2.text)['matches'][0]['metadata']['name']
    check_assert2 = json.loads(r2.text)['matches'][1]['metadata']['name']
    check_assert3 = json.loads(r2.text)['matches'][0]['metadata']['.tag']
    check_assert4 = json.loads(r2.text)['matches'][1]['metadata']['.tag']
    assert check_assert1 == my_fixture3 and \
           check_assert2 == my_fixture3 and \
           check_assert3 == 'folder' and \
           check_assert4 == 'file'

#Only available for business accounts
@pytest.mark.blocker
def test_search_mode_filename_and_content():
    assert True == False

#Upload file first(from fixture), then delete, then search
@pytest.mark.search
def test_search_mode_deleted_file_name(my_fixture4):
    time.sleep(30)
    headers = {
        "Authorization": "Bearer Wvf7h-SwacMAAAAAAAAFFcJH8AWy3DXRE7Dh8NFYijEvQX25vLH9cDNIzvDcixpl",
        "Content-Type": "application/json"
    }
    data = {
        "path": "/test/"+my_fixture4
    }
    r3 = requests.post(Dropbox().db_delete_url, headers=headers,
                       data=json.dumps(data))
    print "Deleted file"

    time.sleep(30)
    my_data2 = {"path": "", "query": my_fixture4,
                "mode": {".tag":"deleted_filename"}}
    r2 = d.db_search(my_data2=my_data2)
    check_assert = json.loads(r2.text)['matches'][0]['metadata']['name']
    assert r2.status_code == 200 and check_assert == my_fixture4

