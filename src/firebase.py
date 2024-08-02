import firebase_admin
import jsonpickle
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("../askall private key.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client(app)
doc_ref = db.collection("members")


def add_member(name: str, number: str):
    doc_ref.document(number).set({'name': name})


def member_exist(number: str):
    return doc_ref.document(number).get().exists


def get_member(number: str):
    return doc_ref.document(number)


def set_member_history(number: str, history: str):
    doc_ref.document(number).set({'history': history}, merge=True)


def get_member_history(number: str) -> list:
    try:
        return jsonpickle.decode(doc_ref.document(number).get(['history']).get('history'))
    except (KeyError, TypeError):
        return []
