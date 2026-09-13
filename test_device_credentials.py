import os


def test_device_credentials_available():

    username = os.getenv("DEVICE_CREDENTIALS_USR")
    password = os.getenv("DEVICE_CREDENTIALS_PSW")

    assert username is not None
    assert password is not None

    print("Device credentials are available securely")