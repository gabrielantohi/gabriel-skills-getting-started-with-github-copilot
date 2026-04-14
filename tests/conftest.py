import copy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module


@pytest.fixture(autouse=True)
def reset_activities_state():
    snapshot = copy.deepcopy(app_module.activities)

    # Arrange test state: restore the in-memory dataset before each test.
    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(snapshot))

    yield

    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(snapshot))


@pytest.fixture
def client():
    return TestClient(app_module.app)
