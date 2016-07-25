"""
This is a helper library that includes a couple of class objects for
testing dropbox APIs.
class Dropbox stores all request information to POST/GET/DELETE
information to and from their database.
class Fake creates fake data and files for testing purposes.

"""
import time
import pytest
import json
import requests
import random
import tempfile
import os
from faker import Factory
faker = Factory.create()

class Dropbox(object):

    authorization = "Bearer Wvf7h-SwacMAAAAAAAAEi244ttuNU_zn7cD0suT5Xog6-Up1VhiIvKqyoZfbOGot"
    db_upload_url = "https://content.dropboxapi.com/2/files/upload"
    db_search_url = "https://api.dropboxapi.com/2/files/search"
    db_account_url = "https://api.dropboxapi.com/2/users/get_current_account"
    db_delete_url = "https://api.dropboxapi.com/2/files/delete"
    db_create_folder_url = "https://api.dropboxapi.com/2/files/create_folder"

    def db_upload(self, my_headers, my_data):
        return requests.post(Dropbox().db_upload_url, headers=my_headers,
                             data=my_data)

    def db_search(self, my_data2):
        my_headers2 = {
        "Authorization": Dropbox().authorization,
        "Content-Type": "application/json"
        }
        return requests.post(Dropbox().db_search_url, headers=my_headers2,
                             data=json.dumps(my_data2))

    def db_get_account(self):
        headers = {
        "Authorization": "Bearer Wvf7h-SwacMAAAAAAAAE0TqNOIfvYFuGZAOxLpnjQjKB4V3oWAH5O29aIwVOl4AX",
        "Content-Type": "application/json"
        }
        data = None
        return requests.post(Dropbox().db_account_url, headers=headers,
                             data=json.dumps(data))

class Fake(object):

    def create_fake_name(self):
        return faker.name()

    def create_first_name(self):
        return faker.first_name()

    def create_last_name(self):
        return faker.last_name()

    def create_file_name(self):
        ext_list = ['.txt', '.mpg', '.jpg']
        chosen_ext = ext_list[random.randint(0,2)]
        return str(random.randint(10000000,20000000)) + chosen_ext

    def create_file(self,fname=''):
        new_file = open(fname, 'w+')
        new_file.truncate(random.randint(0,1024*1024))

    def create_timestamp(self):
        year = str(random.randint(2015,2016))
        month = str(random.randint(10,12))
        day = str(random.randint(10,31))
        hour = str(random.randint(10,23))
        minute = str(random.randint(10,59))
        second = str(random.randint(10,59))
        return year\
               +'-'\
               +month\
               +'-'\
               +day\
               +'T'\
               +hour\
               +':'\
               +minute\
               +':'\
               +second\
               +'Z'

#Fixtures for setup/teardown of tests.
#my_fixture uploads a temporary file into a folder called "test"
@pytest.fixture()
def my_fixture(request):
    print "\nUploading a file"
    #Creating a fake file name
    fake_name = Fake().create_file_name()
    #create a temporary file to memory
    tf = tempfile.NamedTemporaryFile(delete=False)
    fake_file = tf.name
    #create random file size
    tf.write('Hello World!!' * (100000*(random.randint(1,2))))

    base_dir = "{\"path\":\"/"
    filename = "test/"+fake_name+"\"}"
    db_path = os.path.join(base_dir, filename)

    my_headers = {
        "Authorization": Dropbox().authorization,
        "Content-Type": "application/octet-stream",
        "Dropbox-API-Arg": db_path
    }
    my_data = open(fake_file, "rb").read()
    r1 = Dropbox().db_upload(my_headers=my_headers,my_data=my_data)

    def fin():
        print "Deleting the file"
        headers = {
            "Authorization": "Bearer Wvf7h-SwacMAAAAAAAAFFcJH8AWy3DXRE7Dh8NFYijEvQX25vLH9cDNIzvDcixpl",
            "Content-Type": "application/json"
        }
        data = {
            "path": "/test/"+fake_name
        }
        r2 = requests.post(Dropbox().db_delete_url, headers=headers,
                           data=json.dumps(data))
    request.addfinalizer(fin)
    return fake_name

#my_fixture2 uploads two identical temporary files into a folder called
# "test" and "test2" and then deletes it.
@pytest.fixture()
def my_fixture2(request):
    #Creating a fake file name
    fake_name = Fake().create_file_name()
    #create a temporary file to memory
    tf = tempfile.NamedTemporaryFile(delete=False)
    fake_file = tf.name
    #create random file size
    tf.write('Hello World!!' * (100000*(random.randint(1,2))))

    base_dir = "{\"path\":\"/"
    filename = "test/"+fake_name+"\"}"
    db_path = os.path.join(base_dir, filename)

    my_headers = {
        "Authorization": Dropbox().authorization,
        "Content-Type": "application/octet-stream",
        "Dropbox-API-Arg": db_path
    }
    my_data = open(fake_file, "rb").read()
    r1 = Dropbox().db_upload(my_headers=my_headers,my_data=my_data)
    print "\nUploaded 1st file"

    base_dir = "{\"path\":\"/"
    filename = "test2/"+fake_name+"\"}"
    db_path = os.path.join(base_dir, filename)

    my_headers = {
        "Authorization": Dropbox().authorization,
        "Content-Type": "application/octet-stream",
        "Dropbox-API-Arg": db_path
    }
    my_data = open(fake_file, "rb").read()
    r2 = Dropbox().db_upload(my_headers=my_headers,my_data=my_data)
    print "\nUploaded 2nd file"

    def fin():
        headers = {
            "Authorization": "Bearer Wvf7h-SwacMAAAAAAAAFFcJH8AWy3DXRE7Dh8NFYijEvQX25vLH9cDNIzvDcixpl",
            "Content-Type": "application/json"
        }
        data = {
            "path": "/test/"+fake_name
        }
        r3 = requests.post(Dropbox().db_delete_url, headers=headers,
                           data=json.dumps(data))
        print "Deleting 1st file"
        data = {
            "path": "/test2/"+fake_name
        }
        r4 = requests.post(Dropbox().db_delete_url, headers=headers,
                           data=json.dumps(data))
        print "Deleting 2nd file"
    request.addfinalizer(fin)
    return fake_name

#my_fixture3 creates a folder and file with the same name
@pytest.fixture()
def my_fixture3(request):

    #Creating a fake file name
    fake_name = Fake().create_file_name()
    #create a temporary file to memory
    tf = tempfile.NamedTemporaryFile(delete=False)
    fake_file = tf.name
    #create random file size
    tf.write('Hello World!!' * (100000*(random.randint(1,2))))

    base_dir = "{\"path\":\"/"
    filename = "test/"+fake_name+"\"}"
    db_path = os.path.join(base_dir, filename)

    my_headers = {
        "Authorization": Dropbox().authorization,
        "Content-Type": "application/octet-stream",
        "Dropbox-API-Arg": db_path
    }
    my_data = open(fake_file, "rb").read()
    r1 = Dropbox().db_upload(my_headers=my_headers,my_data=my_data)
    print "\nUploaded file"

    #Creating folder with same file name
    headers = {
        "Authorization": "Bearer Wvf7h-SwacMAAAAAAAAFJU1eu32RpPOVwNDCE3iVUr8uSfB4TrD_9rk_uUIS4B-b",
        "Content-Type": "application/json"
    }
    data = {
        "path": "/"+fake_name
    }
    r2 = requests.post(Dropbox().db_create_folder_url, headers=headers,
                       data=json.dumps(data))
    print "\nCreated folder"

    #Tear down mode, delete file and folder
    def fin():
        headers = {
            "Authorization": "Bearer Wvf7h-SwacMAAAAAAAAFFcJH8AWy3DXRE7Dh8NFYijEvQX25vLH9cDNIzvDcixpl",
            "Content-Type": "application/json"
        }
        data = {
            "path": "/test/"+fake_name
        }
        r3 = requests.post(Dropbox().db_delete_url, headers=headers,
                           data=json.dumps(data))
        print "Deleted file"

        data = {
            "path": "/"+fake_name
        }
        r3 = requests.post(Dropbox().db_delete_url, headers=headers,
                           data=json.dumps(data))
        print "Deleted folder"
    request.addfinalizer(fin)
    return fake_name

# my_fixture4 creates a temporary file in a test folder
@pytest.fixture()
def my_fixture4(request):
    print "\nUploading a file"
    #Creating a fake file name
    fake_name = Fake().create_file_name()
    #create a temporary file to memory
    tf = tempfile.NamedTemporaryFile(delete=False)
    fake_file = tf.name
    #create random file size
    tf.write('Hello World!!' * (100000*(random.randint(1,2))))

    base_dir = "{\"path\":\"/"
    filename = "test/"+fake_name+"\"}"
    db_path = os.path.join(base_dir, filename)

    my_headers = {
        "Authorization": Dropbox().authorization,
        "Content-Type": "application/octet-stream",
        "Dropbox-API-Arg": db_path
    }
    my_data = open(fake_file, "rb").read()
    r1 = Dropbox().db_upload(my_headers=my_headers,my_data=my_data)
    return fake_name