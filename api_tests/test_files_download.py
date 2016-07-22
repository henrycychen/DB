"""
This is a Dropbox API. All information can be found at the below web address:
https://www.dropbox.com/developers/documentation/http/documentation.
"""

# Objective - Download a file from a user on db
# Expected Outcome - Assert http code == 200 and downloaded filename
# == file name from search api
def test_download_valid():
    assert True == False

# Objective - Enter an invalid path to attempt to download a file
# Expected Outcome - Assert http code != 200 and file cannot be found
# on the desktop

def test_download_invalid():
    assert True == False

# Objective - Input a valid path in the path field when downloading
# Expected Outcome - Assert http code == 200 and downloaded file ==
# filename from the search api.
def test_download_path_valid():
    assert True == False

# Objective - Attempt to download a file with an invalid path
# Expected Outcome - Assert html code != 200 and returned response
# "path does not match /....".
def test_download_path_invalid():
    assert True == False

# Objective - Input a rev code when downloading a file
# Expected Outcome - Assert html code == 200 and rev code == rev field
# from search api
def test_download_rev():
    assert True == False

# Objective - Download a file from db and see if the size is the same.
# Expected Outcome - Assert desktop file size == file size from search
# api.
def test_download_size():
    assert True == False

# Objective - Test download a file by using an incorrect path.
# Expected Outcome - Assert http code != 200 and will receive a
# malformed response error message stating that the file could not be
# saved.
def test_download_error_malformed_path():
    assert True == False

# Objective - Attempt to download with an erroneous filename
# Expected Outcome - Assert html code != 200 and returned error "There
# is nothing at the given path".
def test_download_error_not_found():
    assert True == False

# Objective - Attempt to download a file that is not a file.
# Expected Outcome - Assert html code != 200 and returned error "We were
# expecting a file, but the given path refers to something that isn't a
# file.
def test_download_error_not_file():
    assert True == False

# Objective - Attempt to download a folder that is not a folder or file.
# Expected Outcome - Assert html code != 200 and returned error "We were
# expecting a folder, but the given path refers to something that isn't
# a folder.
def test_download_error_not_folder():
    assert True == False

# Objective - Attempt to download a file that has restricted content
# Expected Outcome - Assert html code != 200 and return error "The file
# cannot be transferred because the content is restricted. For example,
# sometimes there are legal restrictions due to copyright claims."
def test_download_error_restricted_content():
    assert True == False