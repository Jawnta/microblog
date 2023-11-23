def test_version_route(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/version' route is requested (GET)
    THEN check that the response is correct
    """

    # Make a GET request to the /version route
    response = client.get('/version')

    # Check that the status code is 200 (OK)
    assert response.status_code == 200


