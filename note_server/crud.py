from sqlalchemy.orm import Session
from logging.config import dictConfig
import logging
from .config import LogConfig

from . import models, schemas

dictConfig(LogConfig().dict())
logger = logging.getLogger("mycoolapp")

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_notes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Note).offset(skip).limit(limit).all()


#https://stackoverflow.com/questions/73122511/flask-sqlalchemy-dict-object-has-no-attribute-sa-instance-state
def is_pydantic(obj: object):
    """ Checks whether an object is pydantic. """
    return type(obj).__class__.__name__ == "ModelMetaclass"

# eventually I will need to better review this, and migrate it to a helper file (or something)
def parse_pydantic_schema(schema):
    """
        Iterates through pydantic schema and parses nested schemas
        to a dictionary containing SQLAlchemy models.
        Only works if nested schemas have specified the Meta.orm_model.
    """
    logger.debug ("Schema: " + str(schema))
    parsed_schema = dict(schema)
    for key, value in parsed_schema.items():
        try:
            if isinstance(value, list) and len(value):
                if is_pydantic(value[0]):
                    parsed_schema[key] = [schema.Meta.orm_model(**schema.dict()) for schema in value]
            else:
                if is_pydantic(value):
                    parsed_schema[key] = value.Meta.orm_model(**value.dict())
        except AttributeError:
            raise AttributeError("Found nested Pydantic model but Meta.orm_model was not specified.")
    return parsed_schema


def create_note(db: Session, note: schemas.Note):
    #logger.debug("Tags: " + str(tags))
    parsed_schema = parse_pydantic_schema(note)
    db_note = models.Note(**parsed_schema)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note