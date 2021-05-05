from app.models import Enterprise
from app.schemas import EnterpriseCreate


def get_enterprise_by_id(enterprise_id: int):
    return Enterprise.filter(Enterprise.id == enterprise_id).first()


def get_enterprises(skip: int = 0, limit: int = 100):
    return list(Enterprise.select().offset(skip).limit(limit))


def create_enterprise(enterprise: EnterpriseCreate):
    db_enterprise = Enterprise(name=enterprise.name)
    db_enterprise.save()
    return db_enterprise


def get_enterprise_by_name(name: str):
    return Enterprise.filter(Enterprise.name == name).first()


def delete_enterprise(enterprise_id: int):
    return Enterprise.delete().where(Enterprise.id == enterprise_id).execute()
