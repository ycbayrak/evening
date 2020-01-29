import pytest

from evening import create_app, __version__


@pytest.fixture
def app():
    return create_app(config="test")


@pytest.fixture
def client(app):
    return app.test_client()


def test_version():
    assert __version__ == "0.0.1-alpha.0"


def test_index_view(client):
    r = client.get("/")
    assert r.status_code == 200
