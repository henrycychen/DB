"""
This is a Dropbox API. All information can be found at the below web address:
https://www.dropbox.com/developers/documentation/http/documentation.
"""

import tempfile
import json
import pytest
import time
import os
from helper_library_DB import Dropbox
from helper_library_DB import Fake

d = Dropbox()
f = Fake()

@pytest.mark.upload
# Objective - Test if the api can upload a file to DB.
# Expected Outcome - Assert http status code == 200 and use the search
# api to see that the file exists.
def test_upload_validation():
    #Creating a fake file name
    fake_name = f.create_file_name()
    #create a temporary file to memory
    tf = tempfile.NamedTemporaryFile(delete=False)
    fake_file = tf.name
    base_dir = "{\"path\":\"/"
    filename = fake_name+"\"}"
    db_path = os.path.join(base_dir, filename)
    my_headers = {
        "Authorization": d.authorization,
        "Content-Type": "application/octet-stream",
        "Dropbox-API-Arg": db_path
    }
    my_data = open(fake_file, "rb").read()
    r1 = d.db_upload(my_headers=my_headers,my_data=my_data)
    #Have to set a delay, otherwise the assert will check before the file has
    # been uploaded into the DB database.
    time.sleep(10)
    my_data2 = {"path": "", "query": fake_name}
    r2 = d.db_search(my_data2=my_data2)
    check_assert = json.loads(r2.text)['matches'][0]['metadata']['name']
    assert r1.status_code == 200 and check_assert == fake_name

@pytest.mark.upload
# Objective - Input an acceptable upload path to upload a file to DB.
# Expected Outcome - Assert that the file was uploaded using the search
# api.
def test_upload_path():
    #Creating a fake filename
    fake_name = f.create_file_name()
    #create a temporary file to memory
    tf = tempfile.NamedTemporaryFile(delete=False)
    fake_file = tf.name
    base_dir = "{\"path\":\"/"
    filename = "test/"+fake_name+"\"}" #adding a path for parametization
    db_path = os.path.join(base_dir, filename)
    my_headers = {
        "Authorization": d.authorization,
        "Content-Type": "application/octet-stream",
        "Dropbox-API-Arg": db_path
    }
    my_data = open(fake_file, "rb").read()
    r1 = d.db_upload(my_headers=my_headers,my_data=my_data)
    #Have to set a delay, otherwise the assert will check before the file has
    # been uploaded into the DB database.
    time.sleep(10)
    my_data2 = {"path": "", "query": fake_name}
    r2 = d.db_search(my_data2=my_data2)
    check_assert = json.loads(r2.text)['matches'][0]['metadata']['path_lower']
    assert r1.status_code == 200 and check_assert == "/test/"+fake_name

@pytest.mark.upload
# Objective - Input an unacceptable upload path on DB (use incorrect
# formats, ie. use '\' instead of '/')
# Expected Outcome - Assert that http error code != 200 and response
# is returned with "path does not match..."
def test_upload_path_invalid():
    #Creating a fake filename
    fake_name = f.create_file_name()
    #create a temporary file to memory
    tf = tempfile.NamedTemporaryFile(delete=False)
    fake_file = tf.name
    base_dir = "{\"path\":\"/"
    #adding a '/' to start the path for parametization. This should not
    # pass
    filename = "/"+fake_name+"\"}"
    db_path = os.path.join(base_dir, filename)
    my_headers = {
        "Authorization": d.authorization,
        "Content-Type": "application/octet-stream",
        "Dropbox-API-Arg": db_path
    }
    my_data = open(fake_file, "rb").read()
    r1 = d.db_upload(my_headers=my_headers,my_data=my_data)
    assert r1.status_code != 200 and \
    r1.content == 'Error in call to API function "files/upload": HTTP header ' \
                  '"Dropbox-API-Arg": could not decode input as JSON'

@pytest.mark.upload
# Objective - Make sure there is an existing file before uploading the
# same file. Select mode:add when uploading.
# Expected Outcome - Assert http code == 200 and use the search api to
# find the file name that has been overwritten with "<filename>(1).ext"
def test_upload_mode_add():
    #Creating a LOCAL fake file name
    fake_name = f.create_file_name()
    #create a temporary file to memory
    tf = tempfile.NamedTemporaryFile(delete=False)
    fake_file = tf.name
    x = 1
    while x < 3:
        #Create a file size > than a meg and increase during the 2nd iteration
        tf.write('Hello World!!' * (100000*x))
        base_dir = "{\"path\":\"/"
        filename = fake_name+"\",\"autorename\":true,\"mode\":{\".tag\":\"add\"}}"
        db_path = os.path.join(base_dir, filename)
        my_headers = {
            "Authorization": d.authorization,
            "Content-Type": "application/octet-stream",
            "Dropbox-API-Arg": db_path
        }
        my_data = open(fake_file, "rb").read()
        r1 = d.db_upload(my_headers=my_headers,my_data=my_data)
        #whileloop stopper
        x += 1
    #Need this time delay for information to post to their database.
    time.sleep(20)
    my_data2 = {"path": "", "query": fake_name}
    r2 = d.db_search(my_data2=my_data2)
    check_assert = json.loads(r2.text)['matches'][1]['metadata']['name']
    #The string indexing below follows the DB autorename business logic
    assert check_assert == (fake_name[0:-4]+' (1)'+fake_name[-4::]) and \
           r1.status_code == 200

@pytest.mark.upload
# Objective - Make sure there is an existing file before uploading the
# same file. Select mode:upload when uploading.
# Expected Outcome - Assert http code == 200 and use the search api to
# confirm the updated file size.
def test_upload_mode_overwrite():
    #Creating a LOCAL fake file name
    fake_name = f.create_file_name()
    #create a temporary file to memory
    tf = tempfile.NamedTemporaryFile(delete=False)
    fake_file = tf.name
    x = 1
    while x < 3:
        #Create a file size > than a meg and increase during the 2nd iteration
        tfile = tf.write('Hello World!!' * (100000*x))
        #Use os stat info to find the size of the file.
        statinfo = os.stat(fake_file)
        base_dir = "{\"path\":\"/"
        filename = fake_name+"\",\"autorename\":true,\"mode\":{\".tag\":\"overwrite\"}}"
        db_path = os.path.join(base_dir, filename)
        my_headers = {
            "Authorization": d.authorization,
            "Content-Type": "application/octet-stream",
            "Dropbox-API-Arg": db_path
        }
        my_data = open(fake_file, "rb").read()
        r1 = d.db_upload(my_headers=my_headers,my_data=my_data)
        #whileloop stopper
        x += 1
    #Need this time delay for information to post to their database.
    time.sleep(20)
    my_data2 = {"path": "", "query": fake_name}
    r2 = d.db_search(my_data2=my_data2)
    check_assert = json.loads(r2.text)['matches'][0]['metadata']['size']
    assert r1.status_code == 200 and check_assert == statinfo.st_size

@pytest.mark.upload
# Objective - Make sure there is an existing file before uploading the
# same file. Select mode:update when uploading.
# Expected Outcome - Assert http code == 200 and use the search api to
# find same file name with appended "conflicted copy" string.
def test_upload_mode_update():
    #Creating a LOCAL fake file name
    fake_name = f.create_file_name()
    #create a temporary file to memory
    tf = tempfile.NamedTemporaryFile(delete=False)
    fake_file = tf.name
    x = 1
    rev_name = '123456789'
    while x < 3:
        #Create a file size > than a meg and increase during the 2nd iteration
        tfile = tf.write('Hello World!!' * (100000*x))
        base_dir = "{\"path\":\"/"
        if x == 2:
            rev_name == json.loads(r1.text)['rev']
        filename = fake_name+"\",\"autorename\":true,\"mode\":" \
                             "{\".tag\":\"update\",\"update\":\""\
                   +rev_name\
                   +"\"}}"
        db_path = os.path.join(base_dir, filename)
        my_headers = {
            "Authorization": d.authorization,
            "Content-Type": "application/octet-stream",
            "Dropbox-API-Arg": db_path
        }
        my_data = open(fake_file, "rb").read()
        r1 = d.db_upload(my_headers=my_headers,my_data=my_data)
        #whileloop stopper
        x += 1
    #Need this time delay for information to post to their database.
    time.sleep(20)
    #Get user account info
    r2 = d.db_get_account()
    account_name = json.loads(r2.text)['name']['display_name']
    my_data2 = {"path": "", "query": fake_name}
    r3 = d.db_search(my_data2=my_data2)
    check_assert = json.loads(r3.text)['matches'][1]['metadata']['name']
    #The string indexing below follows the DB autorename business logic
    #ex: 17576599 (Henry Chen's conflicted copy).jpg
    assert check_assert == (fake_name[0:-4]
                            +' ('
                            +account_name
                            +"'s"
                            +' conflicted copy)'
                            +fake_name[-4::]) and \
           r1.status_code == 200

@pytest.mark.upload
# Objective - Test to see what makes the upload mode invalid. Ex: Leave
# the revision field blank when uploading.
# Expected Outcome - Assert html response != 200
def test_upload_mode_invalid():
    #Creating a LOCAL fake file name
    fake_name = f.create_file_name()
    #create a temporary file to memory
    tf = tempfile.NamedTemporaryFile(delete=False)
    fake_file = tf.name
    x = 1
    while x < 3:
        #Create a file size > than a meg and increase during the 2nd iteration
        tfile = tf.write('Hello World!!' * (100000*x))
        base_dir = "{\"path\":\"/"
        filename = fake_name+"\",\"autorename\":true,\"mode\":{\".tag\":\"upload\"}}"
        db_path = os.path.join(base_dir, filename)
        my_headers = {
            "Authorization": d.authorization,
            "Content-Type": "application/octet-stream",
            "Dropbox-API-Arg": db_path
        }
        my_data = open(fake_file, "rb").read()
        r1 = d.db_upload(my_headers=my_headers,my_data=my_data)
        #whileloop stopper
        x += 1
    assert r1.status_code != 200

@pytest.mark.upload
# Objective - Test to see if DB will autorename the file if autorename
# is set to false.
# Expected Outcome - Assert http code != 200 and use the search api to
# find the same file (DB will not autorename the file).
def test_upload_autorename_false():
    #Creating a LOCAL fake file name
    fake_name = f.create_file_name()
    #create a temporary file to memory
    tf = tempfile.NamedTemporaryFile(delete=False)
    fake_file = tf.name
    x = 1
    while x < 3:
        #Create a file size > than a meg and increase during the 2nd iteration
        tf.write('Hello World!!' * (100000*x))
        base_dir = "{\"path\":\"/"
        filename = fake_name+"\",\"autorename\":false,\"mode\":{\".tag\":\"add\"}}"
        db_path = os.path.join(base_dir, filename)
        my_headers = {
            "Authorization": d.authorization,
            "Content-Type": "application/octet-stream",
            "Dropbox-API-Arg": db_path
        }
        my_data = open(fake_file, "rb").read()
        r1 = d.db_upload(my_headers=my_headers,my_data=my_data)
        #whileloop stopper
        x += 1
    #Need this time delay for information to post to their database.
    time.sleep(20)
    my_data2 = {"path": "", "query": fake_name}
    r2 = d.db_search(my_data2=my_data2)
    check_assert = json.loads(r2.text)['matches'][0]['metadata']['name']
    #The string indexing below follows the DB autorename business logic
    assert check_assert == fake_name and r1.status_code != 200

@pytest.mark.upload
# Objective - Test to see if DB will autorename the file if there is a
# conflict with the mode.
# Expected Outcome - Assert http code == 200 and use the search api to
# find the amended file name (DB will autorename the file).
def test_upload_authorename_true():
    #Creating a LOCAL fake file name
    fake_name = f.create_file_name()
    #create a temporary file to memory
    tf = tempfile.NamedTemporaryFile(delete=False)
    fake_file = tf.name
    x = 1
    while x < 3:
        #Create a file size > than a meg and increase during the 2nd iteration
        tf.write('Hello World!!' * (100000*x))
        base_dir = "{\"path\":\"/"
        filename = fake_name+"\",\"autorename\":true,\"mode\":{\".tag\":\"add\"}}"
        db_path = os.path.join(base_dir, filename)
        my_headers = {
            "Authorization": d.authorization,
            "Content-Type": "application/octet-stream",
            "Dropbox-API-Arg": db_path
        }
        my_data = open(fake_file, "rb").read()
        r1 = d.db_upload(my_headers=my_headers,my_data=my_data)
        #whileloop stopper
        x += 1
    #Need this time delay for information to post to their database.
    time.sleep(20)
    my_data2 = {"path": "", "query": fake_name}
    r2 = d.db_search(my_data2=my_data2)
    check_assert = json.loads(r2.text)['matches'][1]['metadata']['name']
    #The string indexing below follows the DB autorename business logic
    assert check_assert == (fake_name[0:-4]+' (1)'+fake_name[-4::]) and \
           r1.status_code == 200

@pytest.mark.upload
# Objective - See if inputting a timestamp when a user uploads the file
# will appear on the "client modified" response.
# Expected Outcome - Assert http code == 200 and use the search api and
# assert the "client modified" field of the metadata is the same as
# what was inputted
def test_upload_client_modified_future():
    #Creating a fake file name
    fake_name = f.create_file_name()
    fake_time = f.create_timestamp()
    #create a temporary file to memory
    tf = tempfile.NamedTemporaryFile(delete=False)
    fake_file = tf.name
    base_dir = "{\"path\":\"/"
    filename = fake_name+"\",\"client_modified\":\""+fake_time+"\"}"
    db_path = os.path.join(base_dir, filename)
    my_headers = {
        "Authorization": d.authorization,
        "Content-Type": "application/octet-stream",
        "Dropbox-API-Arg": db_path
    }
    my_data = open(fake_file, "rb").read()
    r1 = d.db_upload(my_headers=my_headers,my_data=my_data)
    #Have to set a delay, otherwise the assert will check before the file has
    # been uploaded into the DB database.
    time.sleep(10)
    my_data2 = {"path": "", "query": fake_name}
    r2 = d.db_search(my_data2=my_data2)
    check_assert = json.loads(r2.text)['matches'][0]['metadata']['client_modified']
    assert r1.status_code == 200 and check_assert == fake_time

@pytest.mark.blocker
# Objective - Upload the file with mute: True.
# Expected Outcome - User should not receive a notification on this
# modification.
def test_upload_mute_true():
    assert True == False

@pytest.mark.blocker
# Objective - Upload the file with mute: False.
# Expected Outcome - User should receive a notification on any
# modification to the file.
def test_upload_mute_false():
    assert True == False

@pytest.mark.upload
# Objective - Test to see if original uploaded file size is the same as
# the size response.
# Expected Outcome - Assert using the search api and confirm that the
# size field == what was uploaded.
def test_upload_response_size():
    #Creating a fake file name
    fake_name = f.create_file_name()
    #create a temporary file to memory
    tf = tempfile.NamedTemporaryFile(delete=False)
    fake_file = tf.name
    tfile = tf.write('Hello World!!' * (100000))
    #Use os stat info to find the size of the file.
    statinfo = os.stat(fake_file)
    base_dir = "{\"path\":\"/"
    filename = fake_name+"\"}"
    db_path = os.path.join(base_dir, filename)
    my_headers = {
        "Authorization": d.authorization,
        "Content-Type": "application/octet-stream",
        "Dropbox-API-Arg": db_path
    }
    my_data = open(fake_file, "rb").read()
    r1 = d.db_upload(my_headers=my_headers,my_data=my_data)
    #Have to set a delay, otherwise the assert will check before the file has
    # been uploaded into the DB database.
    time.sleep(10)
    my_data2 = {"path": "", "query": fake_name}
    r2 = d.db_search(my_data2=my_data2)
    check_assert = json.loads(r2.text)['matches'][0]['metadata']['size']
    assert r1.status_code == 200 and check_assert == statinfo.st_size

@pytest.mark.upload
# Objective - Upload a file and make sure the file path is correct.
# Expected Outcome - Assert http response == 200 and use the search
# api and check to see if "path_lower" field starts with a '/'
def test_upload_response_pathlower():
    #Creating a fake file name
    fake_name = f.create_file_name()
    #create a temporary file to memory
    tf = tempfile.NamedTemporaryFile(delete=False)
    fake_file = tf.name
    tfile = tf.write('Hello World!!' * (100000))
    base_dir = "{\"path\":\"/"
    filename = fake_name+"\"}"
    db_path = os.path.join(base_dir, filename)
    my_headers = {
        "Authorization": d.authorization,
        "Content-Type": "application/octet-stream",
        "Dropbox-API-Arg": db_path
    }
    my_data = open(fake_file, "rb").read()
    r1 = d.db_upload(my_headers=my_headers,my_data=my_data)
    #Have to set a delay, otherwise the assert will check before the file has
    # been uploaded into the DB database.
    time.sleep(10)
    my_data2 = {"path": "", "query": fake_name}
    r2 = d.db_search(my_data2=my_data2)
    check_assert = json.loads(r2.text)['matches'][0]['metadata']['path_lower']
    assert r1.status_code == 200 and check_assert == '/'+fake_name

# Objective - Create a malformed path so that there is an error.
# Expected Outcome - Assert http code != 200 and will receive a
# malformed response error message stating that the file could not be
# saved.
def test_upload_error_malformed_path():
    #Creating a fake file name
    fake_name = f.create_file_name()
    #create a temporary file to memory
    tf = tempfile.NamedTemporaryFile(delete=False)
    fake_file = tf.name
    base_dir = "{\"path\":\"/"
    #creating a malformed path
    filename = fake_name+"////////////////\"}"
    db_path = os.path.join(base_dir, filename)
    my_headers = {
        "Authorization": d.authorization,
        "Content-Type": "application/octet-stream",
        "Dropbox-API-Arg": db_path
    }
    my_data = open(fake_file, "rb").read()
    r1 = d.db_upload(my_headers=my_headers,my_data=my_data)
    #Have to set a delay, otherwise the assert will check before the file has
    # been uploaded into the DB database.
    time.sleep(10)
    my_data2 = {"path": "", "query": fake_name}
    r2 = d.db_search(my_data2=my_data2)
    check_assert = json.loads(r2.text)['matches']
    assert r1.status_code != 200 and check_assert == []

@pytest.mark.upload
# Objective - Upload a file or folder with an inappropriate name or name
# format.
# Expected Outcome - Assert http code != 200 and use the search api to
# assert the file does not exist.
def test_upload_error_disallowed_name():
    #Creating an inappropriate filename for the test
    fake_name = '/*&(@!)$(@*!&@^#%$&#||'
    #create a temporary file to memory
    tf = tempfile.NamedTemporaryFile(delete=False)
    fake_file = tf.name
    base_dir = "{\"path\":\"/"
    filename = fake_name+"\"}"
    db_path = os.path.join(base_dir, filename)
    my_headers = {
        "Authorization": d.authorization,
        "Content-Type": "application/octet-stream",
        "Dropbox-API-Arg": db_path
    }
    my_data = open(fake_file, "rb").read()
    r1 = d.db_upload(my_headers=my_headers,my_data=my_data)
    #Have to set a delay, otherwise the assert will check before the file has
    # been uploaded into the DB database.
    time.sleep(10)
    my_data2 = {"path": "", "query": fake_name}
    r2 = d.db_search(my_data2=my_data2)
    check_assert = json.loads(r2.text)['matches']
    assert r1.status_code != 200 and check_assert == []

"""
@pytest.mark.upload
# Objective - Create a situation where the user goes over the available
# space (bytes) when uploading a file.
# Expected Outcome - Assert http code != 200 and use the search api to
# assert the file does not exist.
def test_upload_error_insufficient_space():
    assert True == False
# Objective - Create a situation that does not give the user permission
# to write to the target location.
# Expected Outcome - Assert http code != 200 and use the search api to
# assert the file does not exist.
def test_upload_error_no_write_permission():
    assert True == False
"""