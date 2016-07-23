"""
This is a helper library that includes a couple of class objects for
testing dropbox APIs.
class Dropbox stores all request information to POST/GET/DELETE
information to and from their database.
class Fake creates fake data and files for testing purposes.

"""

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

    def db_upload(self, my_headers, my_data):
        return requests.post(Dropbox().db_upload_url, headers=my_headers, data=my_data)

    def db_search(self, my_data2):
        my_headers2 = {
        "Authorization": Dropbox().authorization,
        "Content-Type": "application/json"
        }
        return requests.post(Dropbox().db_search_url, headers=my_headers2, data=json.dumps(my_data2))

    def db_get_account(self):
        headers = {
        "Authorization": "Bearer Wvf7h-SwacMAAAAAAAAE0TqNOIfvYFuGZAOxLpnjQjKB4V3oWAH5O29aIwVOl4AX",
        "Content-Type": "application/json"
        }
        data = None
        return requests.post(Dropbox().db_account_url, headers=headers, data=json.dumps(data))



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


@pytest.fixture()
def my_fixture():
    print "\nI'm the fixture"
    #Creating a fake file name
    fake_name = Fake().create_file_name()
    #create a temporary file to memory
    tf = tempfile.NamedTemporaryFile(delete=False)
    fake_file = tf.name
    #create random file size
    tf.write('Hello World!!' * (100000*(random.randint(1,2))))

    base_dir = "{\"path\":\"/"
    filename = fake_name+"\"}"
    db_path = os.path.join(base_dir, filename)

    my_headers = {
        "Authorization": Dropbox().authorization,
        "Content-Type": "application/octet-stream",
        "Dropbox-API-Arg": db_path
    }
    my_data = open(fake_file, "rb").read()
    r1 = Dropbox().db_upload(my_headers=my_headers,my_data=my_data)
    return fake_name