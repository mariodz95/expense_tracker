from app.routers import router


def test_router():
    expected = {
        "/health/",
    }

    for route in router.router.routes:

        assert route.path in expected
