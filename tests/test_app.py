def test_success_load(app, client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to Blood Pressure App - Version 4" in response.data
    assert b"Username" in response.data
    assert b"systolic_level" in response.data


