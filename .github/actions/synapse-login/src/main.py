import os

import synapseclient

username = os.getenv("INPUT_USERNAME")
password = os.getenv("INPUT_PASSWORD")

syn = synapseclient.login(username=username,
                          password=password,
                          rememberMe=True)
