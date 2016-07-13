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

    #Creating a fake directory name and file (First 5 lines)
    filename = f.create_file_name()
    f.create_file(filename)
    base_dir = "{\"path\":\"/"
    end_dir = filename+"\"}"
    db_path = os.path.join(base_dir, end_dir)

    my_headers = {
        "Authorization": d.authorization,
        "Content-Type": "application/octet-stream",
        "Dropbox-API-Arg": db_path
    }
    my_data = open(filename, "rb").read()
    r1 = d.db_upload(my_headers=my_headers,my_data=my_data)

    #Have to set a delay, otherwise the assert will check before the file has
    # been uploaded into the DB database.
    time.sleep(10)

    my_data2 = {"path": "", "query": filename}
    r2 = d.db_search(my_data2=my_data2)
    check_assert = json.loads(r2.text)['matches'][0]['metadata']['name']
    assert r1.status_code == 200 and check_assert == filename

test_upload_validation()
