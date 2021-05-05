from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from app.main import app, get_db
from app.database import Base


SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_create_enterprise():
    data = {"name": "enviame"}
    response = client.post("/enterprises/", json=data)

    assert response.status_code == 200, response.text

    data = response.json()
    data_expected = {
    "name": "test3",
    "id": 1,
    "is_active": true
}
    assert data == data_expected
