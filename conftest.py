import pytest

from app import create_app

@pytest.fixture()
def client():
  app = create_app()
  app.config['TESTING'] = True
  yield app.test_client()
