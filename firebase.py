import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

__cred = credentials.Certificate("./delivery-slot-checker-firebase-adminsdk-hmnrl-22ecfa8c53.json")
firebase_admin.initialize_app(__cred)

db = firestore.client()

