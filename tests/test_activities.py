from src.app import activities


def test_root_redirects_to_static_index(client):
    # Arrange

    # Act
    response = client.get("/", follow_redirects=False)

    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"


def test_get_activities_returns_expected_payload(client):
    # Arrange
    expected_activities = activities

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(payload, dict)
    assert set(payload.keys()) == set(expected_activities.keys())
    assert isinstance(payload["Chess Club"]["participants"], list)
    assert payload["Chess Club"]["max_participants"] == 12
