def test_get_list_of_users(client):
    response = client.get('/users')
    assert response.json == ['mango']
