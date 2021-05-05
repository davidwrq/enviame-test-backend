import time
from typing import List

from fastapi import Depends, FastAPI, HTTPException

from . import crud, database, models, schemas
from .database import db_state_default


database.db.connect()

database.db.create_tables([models.Enterprise])

database.db.close()


app = FastAPI()

sleep_time = 10


async def reset_db_state():
    database.db._state._state.set(db_state_default.copy())
    database.db._state.reset()


def get_db(db_state=Depends(reset_db_state)):
    try:
        database.db.connect()
        yield
    finally:
        if not database.db.is_closed():
            database.db.close()


# CREATE
@app.post(
    "/enterprises/", response_model=schemas.Enterprise, dependencies=[Depends(get_db)]
)
def create_user(enterprise: schemas.EnterpriseCreate):
    db_enterprise = crud.get_enterprise_by_name(name=enterprise.name)
    if db_enterprise:
        raise HTTPException(status_code=400, detail="enterprise already created")
    return crud.create_enterprise(enterprise=enterprise)


# READ ALL
@app.get(
    "/enterprises/",
    response_model=List[schemas.Enterprise],
    dependencies=[Depends(get_db)],
)
def get_enterprises(skip: int = 0, limit: int = 100):
    users = crud.get_enterprises(skip=skip, limit=limit)
    return users


# get BY ID
@app.get(
    "/enterprises/{enterprise_id}",
    response_model=schemas.Enterprise,
    dependencies=[Depends(get_db)],
)
def get_enterprise(enterprise_id: int):
    db_enterprise = crud.get_enterprise_by_id(enterprise_id)
    if db_enterprise is None:
        raise HTTPException(status_code=404, detail="Enterprise not found")
    return db_enterprise


# DELETE
@app.delete("/enterprises/{enterprise_id}")
def delete_enterprise(enterprise_id: int):
    db_enterprise = crud.delete_enterprise(enterprise_id)
    if db_enterprise is None:
        raise HTTPException(status_code=404, detail="Enterprise not found")
    return db_enterprise
