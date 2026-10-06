from playwright.sync_api import sync_playwright

from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    #get request context

    request = p.request.new_context()

    response = request.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    print(response.status) 
    print(response.json())

    request.dispose() # to clean up the request context after use

'''

    # secodn method for playwright pytest

    def test_get_api(playwright):

    request = playwright.request.new_context()

    response = request.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    assert response.status == 200

    data = response.json()

    print(data)

    assert data["id"] == 1

    request.dispose()
     '''