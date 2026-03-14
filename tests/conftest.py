from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app

_ORIGINAL_ACTIVITIES = deepcopy(activities)


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities_state():
    activities.clear()
    activities.update(deepcopy(_ORIGINAL_ACTIVITIES))
    yield
    activities.clear()
    activities.update(deepcopy(_ORIGINAL_ACTIVITIES))
