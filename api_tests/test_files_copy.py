"""
This is a Dropbox API. All information can be found at the below web address:
https://www.dropbox.com/developers/documentation/http/documentation.
"""

@pytest.mark.files_copy
# Objective - Copy an existing file to another path on DB.
# Expected Outcome - Assert http code == 200 and the file name can be
# located at the specified path using the search api.
def test_copy_valid():
    assert True == False

# Objective - Create an invalid response by not inputting a file to copy
# Expected Outcome - Assert http code != 200 and file does not exist
# using the search API.
def test_copy_invalid():
    assert True == False

# Objective - Copy an existing file to another path on DB.
# Expected Outcome - Assert http code == 200 and the file name can
# be located at the specified path using the search api.
def test_copy_from_path_valid_file():
    assert True == False

# Objective - Attempt to copy a file to a path, but inputting
# incorrect from path string.
# Expected Outcome - Assert http code != 200 and response returned "path
# not matching \... format"
def test_copy_from_path_invalid_file():
    assert True == False

# Objective - Copy an existing folder to another path on DB.
# Expected Outcome - Assert http code == 200 and the folder name can
# be located at the specified path using the search api and all
# contents in each folder are also included.
def test_copy_from_path_valid_folder():
    assert True == False

# Objective - Attempt to copy a folder to a path, but inputting
# incorrect from path string.
# Expected Outcome - Assert http code != 200 and response returned "path
# not matching \... format"
def test_copy_from_path_invalid_folder():
    assert True == False

# Objective - Copy an existing file to another path on DB.
# Expected Outcome - Assert http code == 200 and the file name can be
# located at the specified path using the search api.
def test_copy_to_path_valid_file():
    assert True == False

# Objective - Attempt to copy a file to a path, but inputting
# incorrect from path string.
# Expected Outcome - Assert http code != 200 and response returned "path
# not matching \... format"
def test_copy_to_path_invalid_file():
    assert True == False

# Objective - Copy an existing folder to another path on DB.
# Expected Outcome - Assert http code == 200 and the folder name can
# be located at the specified path using the search api and all
# contents in each folder are also included.
def test_copy_to_path_valid_folder():
    assert True == False

# Objective - Attempt to copy a folder to a path, but inputting
# incorrect from path string.
# Expected Outcome - Assert http code != 200 and response returned "path
# not matching \... format"
def test_copy_to_path_invalid_folder():
    assert True == False


# Objective - Test to see if original copied file size is the same as
# the new copied file
# Expected Outcome - Assert using the search api and confirm that the
# size field == what was copied.
def test_copy_size():
    assert True == False

# Objective - Test to see if the pathlower starts with a '/' after
# copying a file.
# Expected Outcome - Assert using the search api and the "path_lower"
# field starts with a "/".
def test_copy_pathlower():
    assert True == False

# Objective - Test to see if name contains any slashes '/' by copying
# a file name.
# Expected Outcome - Assert name field does not contain '/' by using
# the search api.
def test_copy_filemeta_name():
    assert True == False

# Objective - Test to see if name contains any slashes '/' by copying
# a folder name.
# Expected Outcome - Assert name field does not contain '/' by using
# the search api.
def test_copy_foldermeta_name():
    assert True == False

# Objective - Delete a file and try to copy the same file to that path.
# Expected Outcome - Will receive an error response indicating that
# there use to be a file there.
def test_copy_deleted_file():
    assert True == False

# Objective - Delete a folder and try to copy the same folder to that
# path.
# Expected Outcome - Will receive an error response indicating that
# there use to be a folder there.
def test_copy_deleted_folder():
    assert True == False

# Objective - Try to copy a shared folder.
# Expected Outcome - You will receive an error summary response "can't
# copy shared folder".
def test_cant_copy_shared_folder():
    assert True == False

# Objective - Try to copy a nested shared folder.
# Expected Outcome - You will receive an error summary response "can't
# copy nested shared folder".
def test_cant_nest_shared_folder():
    assert True == False

# Objective - Copy a folder into the same folder.
# Expected Outcome - You will receive an error summary response "can't
# move folder into self".
def test_cant_move_folder_into_itself():
    assert True == False

# Objective - Move a folder that has many files.
# Expected Outcome - You will receive an error summary response "too
# many files...".
def test_too_many_files():
    assert True == False

# Objective - Create an other error.
# Expected Outcome - You will receive an error summary response "other"
def test_error_other():
    assert True == False

# Objective - Create an error that returns a malformed response.
# Expected Outcome - Assert http code != 200 and will receive a
# malformed response error message stating that the file could not be
# saved.
def test_copy_error_malformed_path():
    assert True == False

# Objective - Create a situation that does not give the user permission
# to write to the target location.
# Expected Outcome - Assert http code != 200 and use the search api to
# assert the file does not exist.
def test_copy_error_no_write_permission():
    assert True == False

# Objective - Create a situation where the user goes over the available
# space (bytes) when copying a file.
# Expected Outcome - Assert http code != 200 and use the search api to
# assert the file does not exist.
def test_copy_error_insufficient_space():
    assert True == False

# Objective - Copy a file or folder with an inappropriate name or name
# format.
# Expected Outcome - Assert http code != 200 and use the search api to
# assert the file does not exist.
def test_copy_error_disallowed_name():
    assert True == False