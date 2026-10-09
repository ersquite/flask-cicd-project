from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert "Flask CI/CD" in response.get_data(as_text=True)

def test_hello():
    client = app.test_client()
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.get_data(as_text=True) == "Hello, World!"
