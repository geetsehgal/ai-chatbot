import firebase_admin

from firebase_admin import credentials
from firebase_admin import auth

cred = credentials.Certificate(
    "firebase-service-account.json"
)

firebase_admin.initialize_app(cred)

def verify_token(token):

    return auth.verify_id_token(token)
