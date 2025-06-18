from app.routers import router


def test_router():
    expected = {
        "/health/",
        "/auth/signup",
        "/auth/login",
        "/budget/create",
        "/expense/create",
    }

    for route in router.router.routes:
        assert route.path in expected
