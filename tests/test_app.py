from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get("/")  # Act (execução)

    assert response.status_code == HTTPStatus.OK  # Assert (verificação)
    assert response.json() == {"message": "Olá, mundo!"}


def test_ola_mundo_html_deve_retornar_ola_mundo(client):
    response = client.get("/olamundo")

    assert response.status_code == HTTPStatus.OK
    assert (
        response.text
        == """
    <html>
        <head>
            <title>Olá, mundo!</title>
        </head>
        <body>
            <h1>Olá, mundo!</h1>
        </body>
    </html>
    """
    )


def test_create_user(client):
    response = client.post(
        "/users",
        json={
            "name": "XXXXX",
            "email": "alice@example.com",
            "password": "senha123",
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "name": "XXXXX",
        "email": "alice@example.com",
        "id": 1,
    }


def test_read_users(client):
    response = client.get("/users")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": [
            {
                "name": "XXXXX",
                "email": "alice@example.com",
                "id": 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        "/users/1",
        json={
            "name": "testeusername2",
            "email": "alice@example.com",
            "password": "senha123",
        },
    )

    assert response.json() == {
        "id": 1,
        "name": "testeusername2",
        "email": "alice@example.com",
    }


def test_delete_user(client):
    response = client.delete("/users/1")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "User deleted"}
