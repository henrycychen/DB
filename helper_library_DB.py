"""
This is a helper library that includes a couple of class objects for
testing dropbox APIs.
class Dropbox stores all request information to POST/GET/DELETE
information to and from their database.
class Fake creates fake data and files for testing purposes.
"""

import json
import requests
import random
from faker import Factory
faker = Factory.create()

class Dropbox(object):

    authorization = "Bearer Wvf7h-SwacMAAAAAAAAECLY51n13M2ltZImFjM9M242G96wJV32mWiXR8F9fwVvl"
    db_upload_url = "https://content.dropboxapi.com/2/files/upload"
    db_search_url = "https://api.dropboxapi.com/2/files/search"

    def db_upload(self, my_headers, my_data):
        return requests.post(Dropbox().db_upload_url, headers=my_headers, data=my_data)

    def db_search(self, my_data2):
        my_headers2 = {
        "Authorization": Dropbox().authorization,
        "Content-Type": "application/json"
        }
        return requests.post(Dropbox().db_search_url, headers=my_headers2, data=json.dumps(my_data2))

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
        return faker.first_name() + chosen_ext

    def create_file(self,fname=''):
        new_file = open(fname, 'a+')
        new_file.truncate(random.randint(0,1024*1024))