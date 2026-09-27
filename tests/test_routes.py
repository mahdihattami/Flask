def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Selected work" in response.data


def test_about(client):
    assert client.get("/about").status_code == 200


def test_projects(client):
    assert client.get("/projects").status_code == 200


def test_project_detail(client):
    assert client.get("/projects/nebula").status_code == 200
    assert client.get("/projects/not-real").status_code == 404


def test_contact_get(client):
    assert client.get("/contact").status_code == 200


def test_contact_post(client):
    response = client.post(
        "/contact",
        data={
            "name": "Test User",
            "email": "test@example.com",
            "subject": "Hello there",
            "message": "This is a test message for the portfolio.",
        },
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"Thanks" in response.data


def test_health(client):
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_sitemap(client):
    response = client.get("/sitemap.xml")
    assert response.status_code == 200
    assert b"<urlset" in response.data
