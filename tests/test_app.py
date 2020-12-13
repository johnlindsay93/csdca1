def test_success_load(app, client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to Blood Pressure App - Version 2" in response.data
    assert b"Username" in response.data
    assert b"systolic_level" in response.data


def test_low_result(app, client):
    response = client.post('/', data=dict(username= "John", systolic_level="150", diastolic_lelvel="90",
                                          submit=""), follow_redirects=True)
    assert b"High" in response.data

