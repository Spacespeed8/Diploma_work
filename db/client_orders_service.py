from db.models import CorporativeClients
from db import get_db


def add_corporative_client(type_of_bussiness,id,company):
    with next(get_db()) as db:
        new_corporative_client = CorporativeClients(type_of_bussiness=type_of_bussiness,id=id,company=company)
        db.add(new_corporative_client)
        db.commit()
        return True

# def delete_corporative_client(id):
#     with next(get_db()) as db:
#         delete_corporative_client = db.query(CorporativeClients).filter_by(id=id).first()
#         if delete_corporative_client :
#             db.delete(delete_corporative_client)
#             db.commit()
#             return True
#         return False







def get_exact_corporative_client(id):
    with next(get_db()) as db:
        get_exact_corporative_client= db.query(CorporativeClients).filter_by(id=id).first()
        if get_exact_corporative_client:
            return get_exact_corporative_client
        return False

def checker_corporative_client(id,company):
    with next(get_db()) as db:
        checker1 = db.query(CorporativeClients).filter_by(id=id,company=company).first()
        if checker1:
            return True
        return False