from src import app


def test_app_runs():
    client = app.test_client()
    response = client.get("/")

    # We don’t know your routes yet,
    # so we just check server responds
    assert response.status_code in (200, 404)
