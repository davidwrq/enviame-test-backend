from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#from ..database import Base
from app.main import app, get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


#Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)



def test_read_item():

    response = client.get("/enterprises/")
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200
    assert len(response.json()) == 2



# import pytest

# from fastapi.testclient import TestClient

# from app.main import app


# @pytest.fixture
# def client():
#     client = TestClient(app)
#     yield client

# # def test_read_item():
# #     response = client.get("/enterprises/")
# #     print(response.status_code)
# #     print(response.json())
# #     assert response.status_code == 200


# # import collections

# # try:
# #     collectionsAbc = collections.abc
# # except AttributeError:
# #     collectionsAbc = collections


# # from unittest.mock import Mock
# # import pytest

# # from src import mocks


# @pytest.mark.usefixtures("client")
# class TestEnterpriseAPIView:
#     url = "/enterprises/"

#     def test_(self, client):
#         response = client.get(self.url)

#         assert response.status_code == 200
#         assert response.json() == "a"


#     def test_test_route_sucess(self, client):
#         response = client.get(self.url)

#         assert response.status_code == 200
#         assert response.json() == "a"

