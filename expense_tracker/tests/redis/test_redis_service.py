from app.services import redis_service


def test_connection():
    actual = redis_service.connection()

    assert actual is not None
