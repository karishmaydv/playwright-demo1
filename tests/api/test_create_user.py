def test_create_user(playwright):

    request = playwright.request.new_context()

    response = request.post(
        "https://jsonplaceholder.typicode.com/posts",
        data={
            "title": "Playwright",
            "body": "API Testing",
            "userId": 1
        }
    )

    assert response.status == 201

    print(response.json())

    request.dispose()