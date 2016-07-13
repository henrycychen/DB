"""
This is a Dropbox API. All information can be found at the below web address:
https://www.dropbox.com/developers/documentation/http/documentation.
"""
import json
import pytest
import requests
import time
import os
from helper_library_DB import Dropbox
from helper_library_DB import Fake

d = Dropbox()
f = Fake()

# Objective - Test if the api can upload a file to DB.
# Expected Outcome - Assert http status code == 200 and use the search
# api to see that the file exists.
def test_upload_validation():

    #Creating a fake directory name (First 4 lines)
    fake_name = f.create_file_name()
    base_dir = "{\"path\":\"/"
    filename = fake_name+"\"}"
    db_path = os.path.join(base_dir, filename)

    my_headers = {
        "Authorization": d.authorization,
        "Content-Type": "application/octet-stream",
        "Dropbox-API-Arg": db_path
    }
    my_data = open("C:/Users/Henry/Pictures/IMG_0399.JPG", "rb").read()
    r1 = d.db_upload(my_headers=my_headers,my_data=my_data)

    #Have to set a delay, otherwise the assert will check before the file has
    # been uploaded into the DB database.
    time.sleep(10)

    my_data2 = {"path": "", "query": fake_name}
    r2 = d.db_search(my_data2=my_data2)
    check_assert = json.loads(r2.text)['matches'][0]['metadata']['name']
    assert r1.status_code == 200 and check_assert == fake_name

"""
# Objective - Input an acceptable upload path to upload a file to DB.
# Expected Outcome - Assert that the file was uploaded using the search
# api.
def test_upload_path():
    assert True == False
# Objective - Input an unacceptable upload path on DB (use incorrect
# formats, ie. use '\' instead of '/')
# Expected Outcome - Assert that http error code != 200 and response
# is returned with "path does not match..."
def test_upload_path_invalid():
    assert True == False
# Objective - Make sure there is an existing file before uploading the
# same file. Select mode:add when uploading.
# Expected Outcome - Assert http code == 200 and use the search api to
# find the file name that has been overwritten with "<filename>(2).ext"
def test_upload_mode_add():
    assert True == False
# Objective - Make sure there is an existing file before uploading the
# same file. Select mode:upload when uploading.
# Expected Outcome - Assert http code == 200 and use the search api to
# confirm there is not a duplicate filename.
def test_upload_mode_override():
    assert True == False
# Objective - Make sure there is an existing file before uploading the
# same file. Select mode:update when uploading.
# Expected Outcome - Assert http code == 200 and use the search api to
# find same file name with appended "conflicted copy" string.
def test_upload_mode_update():
    assert True == False
# Objective - Test to see what makes the upload mode invalid. Ex: Leave
# the field blank when uploading.
# Expected Outcome - Assert using the search api and find the uploaded
# file with appended "(2).ext" after the file name.
def test_upload_mode_invalid():
    assert True == False
# Objective - Test to see if DB will autorename the file if there is a
# conflict with the mode.
# Expected Outcome - Assert http code == 200 and use the search api to
# find the same file (DB will not autorename the file).
def test_upload_autorename_false()
    assert True == False
# Objective - Test to see if DB will autorename the file if there is a
# conflict with the mode.
# Expected Outcome - Assert http code == 200 and use the search api to
# find the amended file name (DB will autorename the file).
def test_upload_authorname_true():
    assert True == False
# Objective - See if inputting a timestamp when a user uploads the file
# will appear on the "client modified" response.
# Expected Outcome - Assert http code == 200 and use the search api and
# assert the "client modified" field of the metadata is the same as
# what was inputted
def test_upload_client_modified_future():
    assert True == False
@pytest.mark.mute
# Objective - Upload the file with mute: True.
# Expected Outcome - User should not receive a notification on this
# modification.
def test_upload_mute_true():
    assert True == False
@pytest.mark.mute
# Objective - Upload the file with mute: False.
# Expected Outcome - User should receive a notification on any
# modification to the file.
def test_upload_mute_false():
    assert True == False
# Objective - Test to see if original uploaded file size is the same as
# the size response.
# Expected Outcome - Assert using the search api and confirm that the
# size field == what was uploaded.
def test_upload_response_size():
    assert True == False
# Objective - Upload a file and make sure the file path is correct.
# Expected Outcome - Assert http response == 200 and use the search
# api and check to see if "path_lower" field starts with a '/'
def test_upload_response_pathlower():
    assert True == False
# Objective - Create an error that returns a malformed response.
# Expected Outcome - Assert http code != 200 and will receive a
# malformed response error message stating that the file could not be
# saved.
def test_upload_error_malformed_path():
    assert True == False
# Objective - Create a situation that does not give the user permission
# to write to the target location.
# Expected Outcome - Assert http code != 200 and use the search api to
# assert the file does not exist.
def test_upload_error_no_write_permission():
    assert True == False
# Objective - Create a situation where the user goes over the available
# space (bytes) when uploading a file.
# Expected Outcome - Assert http code != 200 and use the search api to
# assert the file does not exist.
def test_upload_error_insufficient_space():
    assert True == False
# Objective - Upload a file or folder with an inappropriate name or name
# format.
# Expected Outcome - Assert http code != 200 and use the search api to
# assert the file does not exist.
def test_upload_error_disallowed_name():
    assert True == False
"""