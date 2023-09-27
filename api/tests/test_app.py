def test_root_must_return_200_hello_world(client):
    response = client.get('/')

    assert response.status_code == 200
    assert response.json() == {'message': 'Hello, world!'}
