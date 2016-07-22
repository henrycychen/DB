"""
This is a Dropbox API. All information can be found at the below web address:
https://www.dropbox.com/developers/documentation/http/documentation.
"""

# Objective - Delete a file from DB
# Expected Outcome - Assert http code == 200. Also assert if file exists
# using the search api.
def test_deleted_valid():
    assert True == False

# Objective - Input an incorrect file name
# Expected Outcome - Assert http code != 200 and file cannot be found
# using the search api.
def test_deleted_invalid():
    assert True == False

# Objective - Delete a file from DB
# Expected Outcome - Assert http code == 200 and file cannot be located
# using the search api.
def test_deleted_file_valid():
    assert True == False

# Objective - Delete a folder from DB
# Expected Outcome - Assert http code == 200 and file cannot be located
# using the search api.
def test_deleted_folder_valid():
    assert True == False

# Objective - Delete a file by inputting an appropriate path format
# Expected Outcome - Assert http code == 200 and file cannot be located
# using the search api.
def test_deleted_path_valid():
    assert True == False

# Objective - Input an inappropriate path format
# Expected Outcome - Assert http code != 200 and receive a response
# error "Path does not match /...."
def test_deleted_path_invalid():
    assert True == False

# Objective - Delete an existing file and try to re-delete again.
# Expected Outcome - Will receive an error response indicating that
# there use to be a file there.
def test_delete_deleted_file():
    assert True == False