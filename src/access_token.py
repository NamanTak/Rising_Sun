from fyers_api import fyersModel
from fyers_api import accessToken
import os
import webbrowser

APP_ID = "JBGZVR59OA-100"
SECRET_KEY = "CNMXMDL77L"
REDIRECT_URI = "https://www.google.com/"
RESPONSE_TYPE = "code"
GRANT_TYPE = "authorization_code"


# Authentication of the APP from the FYERS Server
def get_access_token():
    """
    Authentication of the APP from the FYERS Server
    :return:
    """
    print("\n\nRetrieving: Access Token from FYERS Server")
    if not os.path.exists("access_token.txt"):
        session = accessToken.SessionModel(client_id=APP_ID, secret_key=SECRET_KEY, redirect_uri=REDIRECT_URI,
                                           response_type=RESPONSE_TYPE, grant_type=GRANT_TYPE)
        response = session.generate_authcode()
        print(response)
        print("open")
        webbrowser.open(response)
        auth_code = input("1. Enter Auth Code: ")
        session.set_token(auth_code)
        access_token = session.generate_token()["access_token"]
        print("2. Creating Access Token text file.")
        with open("access_token.txt", "w") as f:
            f.write(access_token)
        print("3. Access Token file created")
        print("Retrieved: Access Token from Server\n")
    else:
        print("1. Retrieving: Access Token from local file")
        with open("access_token.txt", "r") as f:
            access_token = f.read()
        print("Retrieved: Access Token from file\n")
    return access_token


# Retrieving Access Token to have an ENTRY POINT in the project
def get_fyers_entry_point():
    """
    Retrieving Access Token to have an ENTRY POINT in the project
    :return: fyers key
    """
    fyers = fyersModel.FyersModel(client_id=APP_ID, token=get_access_token(), log_path="")
    return fyers



