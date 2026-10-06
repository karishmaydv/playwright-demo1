#

def test_api_get_request(playwright):
    request = playwright.request.new_context()
    response= request.get("https://jsonplaceholder.typicode.com/posts/1")

    # if want to add hearders in get api
    #response = request.get("https://jsonplaceholder.typicode.com/posts/1", headers={"Authorization": "Bearer <token>"})

'''
request = playwright.request.new_context(
   extra_http_headers={
       "Authorization": "Bearer your_token_here",
       "Accept": "application/json",
       "X-Custom-Header": "value123"
   }

response = request.get("https://api.example.com/protected-end...")
-
'''
    assert response.status == 200
    json_data = response.json()
    print(json_data)
    assert json_data["id"] == 1
    request.dispose()
    print("API GET request test completed successfully.")