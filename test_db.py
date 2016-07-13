import pytest
import dropbox
import requests
import json

"""
#Get metadata from a specific file (metadata = information on the file
#why is this a post request?
def test_get_metadata():
    url = "https://api.dropboxapi.com/2/files/alpha/get_metadata"
    headers = {
        "Authorization": "Bearer <input token code>",
        "Content-Type": "application/json"
    }
    data = {
        "path": "/Rome.jpg"
    }
    r = requests.post(url, headers=headers, data=json.dumps(data))
    print r.text

#Upload files to dropbox
#"Dropbox-API-Arg": "{\"path\":\"/<enter the path, starts at root and name the
# file ext>\"}" Note: Can change the file type even if it doesn't match what is
# being uploaded.
#data = open("C:/Users/Henry/Pictures/20160204_194806.jpg", "rb").read() Note:
# need to use '/' slashes for file directory

def test_upload():
    url = "https://content.dropboxapi.com/2/files/alpha/upload"
    headers = {
        "Authorization": "Bearer <input token code>",
        "Content-Type": "application/octet-stream",
        "Dropbox-API-Arg": "{\"path\":\"/Rome.jpg\"}"
    }
    data = open("C:/Users/Henry/Pictures/IMG_0483.JPG", "rb").read()
    r = requests.post(url, headers=headers, data=data)
    print r.text

#Copy one file from db to another path
def test_copy():
    url = "https://api.dropboxapi.com/2/files/copy"
    headers = {
        "Authorization": "Bearer <input token code>",
        "Content-Type": "application/json"
    }
    data = {
        "from_path": "/Rome.jpg",
        "to_path": "/Rome/Rome2/Rome3/Rome.jpg"
    }
    r = requests.post(url, headers=headers, data=json.dumps(data))
    print r.text

#Create a folder on dropbox - update the path to create the folder.
def test_create_folder():
    url = "https://api.dropboxapi.com/2/files/create_folder"
    headers = {
        "Authorization": "Bearer <input token code>",
        "Content-Type": "application/json"
    }
    data = {
        "path": "/test"
    }
    r = requests.post(url, headers=headers, data=json.dumps(data))
    print r.text

def test_delete_folder():
    url = "https://api.dropboxapi.com/2/files/delete"
    headers = {
        "Authorization": "Bearer <input token code>",
        "Content-Type": "application/json"
    }
    data = {
        "path": "/test"
    }
    r = requests.post(url, headers=headers, data=json.dumps(data))
    r.text

#gets the client info using drop boxes sdk
def test_dbx_sdk1():
    client = dropbox.client.DropboxClient('<input token code>')
    print 'linked account: ', client.account_info()

#gets a list of all files in the root folder
def test_dbx_sdk2():
    dbx = dropbox.Dropbox(
        '<input token code')

    dbx.users_get_current_account()

    for entry in dbx.files_list_folder('').entries:
        print(entry.name)

    dbx.files_upload("Potential headline: Game 5 a nail-biter as Warriors inch "
                     "out Cavs", '/cavs vs warriors/game 5/story.txt')

    print(dbx.files_get_metadata('/Cavs vs Warriors/Game 5/story.txt').server_modified)
"""

