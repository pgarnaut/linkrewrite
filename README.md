Django app for generating and maintaining a list of links that can be rewritten by the server.

Eg. 
    
    --> client POST /link/ 
            header = {redirect_url: some_redirect_url}
            content = some_content
    <-- server returns 200
            content = "/link/some_random_hex_string"
    
    
    --> client GET "/link/some_random_hex_string"
    <-- server response 3xx
            header = {redirect_url: some_redirect_url}
            content = some_content
            

Links on server ordered by access time. Old ones pruned according to configurable amount.