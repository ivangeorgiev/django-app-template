from django.urls import reverse
import pytest



@pytest.fixture(name="hello_url")
def given_hello_url() -> str:
    return reverse("hello-django")

def test_hello_django(client, hello_url):
    response = client.get(hello_url)
    assert response.status_code == 200
    assert response.content == b'Hello, Django!'
