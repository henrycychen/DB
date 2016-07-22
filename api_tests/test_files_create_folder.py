"""
This is a Dropbox API. All information can be found at the below web address:
https://www.dropbox.com/developers/documentation/http/documentation.
"""

# Objective - Create a folder in DB using the create folder api
# Expected Outcome - Assert html code == 200 and folder name can be
# located using the search api.
def test_create_folder_valid():
    assert True == False

# Objective - Do not enter in a folder name to create an invalid response
# Expected Outcome - Assert html code != 200 and return response should
# return "path not matching /...."
def test_create_folder_invalid():
    assert True == False

# Objective - Input in a valid path when creating a folder
# Expected Outcome - Assert html code == 200 and folder path can be
# found by using the search api.
def test_create_path_valid():
    assert True == False

# Objective - Input an invalid path.
# Expected Outcome - Assert html code != 200 and return response should
# return "path not matching /....
def test_create_path_invalid():
    assert True == False

# Objective - Create a folder and make sure the folder path is correct.
# Expected Outcome - Assert http response == 200 and use the search
# api and check to see if "path_lower" field starts with a '/'
def test_upload_response_pathlower():
    assert True == False

# Objective - Use the same file name for the folder when creating.
# Expected Outcome - Assert html code != 200 and receive an error
# response "There's a file in the way".
def test_create_folder_conflicterror_file():
    assert True == False

# Objective - Use an existing folder name and create the folder in
# the same path.
# Expected Outcome - Assert html code != 200 and receive an error
# response "There's a folder in the way".
def test_create_folder_conflicterror_folder():
    assert True == False

# Objective - Create a folder at an ancestor path
# Expected Outcome - Assert html code != 200 and receive an error
# "There's a file at an ancestor path, so we couldn't create the
# required parent folders.
def test_create_folder_conflicterror_file_ancestor():
    assert True == False

# Objective - Create an error that returns a malformed response.
# Expected Outcome - Assert http code != 200 and will receive a
# malformed response error message stating that the folder could not be
# saved.
def test_create_folder_error_malformed_path():
    assert True == False

# Objective - Create a situation that does not give the user permission
# to write to the target location.
# Expected Outcome - Assert http code != 200 and use the search api to
# assert the folder does not exist.
def test_create_folder_error_no_write_permission():
    assert True == False

# Objective - Create a situation where the user goes over the available
# space (bytes) when uploading a file.
# Expected Outcome - Assert http code != 200 and use the search api to
# assert the folder does not exist.
def test_create_folder_error_insufficient_space():
    assert True == False

# Objective - Create a folder with an inappropriate name or name
# format.
# Expected Outcome - Assert http code != 200 and use the search api to
# assert the folder does not exist.
def test_create_folder_error_disallowed_name():
    assert True == False