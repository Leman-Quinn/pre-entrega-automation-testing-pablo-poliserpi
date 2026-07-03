import requests
import pytest

URL_POST = "https://jsonplaceholder.typicode.com/posts"
POST_BODY = {
    "userId":"20",
    "id":"",
    "title":"Random title",
    "body":"Random long text"
}

URL_PATCH = "https://jsonplaceholder.typicode.com/posts/22"
PATCH_PAYLOAD = {
    "title":"A different random tittle"
}

def test_post():
    response = requests.post(URL_POST , json=POST_BODY)

    assert response.status_code == 201
    
    data = response.json()

    received_id = data["id"]
    assert received_id == 101

    assert response.elapsed.total_seconds() < 1

def test_patch():
    response = requests.patch(URL_PATCH, json=PATCH_PAYLOAD)

    assert response.status_code == 200

    data = response.json()
    assert data["title"] == PATCH_PAYLOAD["title"]

    assert response.elapsed.total_seconds() < 1

def test_delete():
    response = requests.delete(URL_PATCH)

    assert response.status_code == 200

    assert response.elapsed.total_seconds() < 1