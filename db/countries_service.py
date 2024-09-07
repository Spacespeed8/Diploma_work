from db.models import Countries
from db import get_db

def add_country(countries_with_bonus,which_country,country_id):
    with next(get_db()) as db:
        new_country = Countries(country_id=country_id,
                                countries_with_bonus=countries_with_bonus,
                                which_country=which_country)
        db.add(new_country)
        db.commit()
        return True


def delete_exact_country(country_id,which_country):
    with (next(get_db()) as db):
        delete_exact_country = db.query(Countries).filter_by(country_id=country_id,
                                                             which_country=which_country
                                                             ).first()
        if delete_exact_country:
            db.delete(delete_exact_country)
            db.commit()
            return True
        return False



def get_country_id(country_id):
    with next(get_db()) as db:
        get_country_id = db.query(Countries).filter_by(country_id=country_id).first()
        if get_country_id:
            return get_country_id
        return False



def checker_country_info(country_id,which_country,countries_with_bonus):
    with next(get_db()) as db:
        checker_country_info = db.query(Countries).filter_by(country_id=country_id,
                                                             countries_with_bonus=countries_with_bonus,
                                                             which_country=which_country).all()
        if checker_country_info:
            return True
        return False