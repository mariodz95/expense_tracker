def test_service_health_status(client):
    actual = client.get("/health/")

    assert actual.status_code == 200
    assert actual.json() == {}
