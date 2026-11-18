from urllib.parse import urlsplit, urlparse, parse_qs, unquote, urlunsplit

url = "https://alice:demo-pass@api.example.com:8443/v2/books/python;edition=3?search=web%20development&tag=python&tag=networking&page=2#chapter-4"
parsed_url = urlparse(url)
split_url = urlsplit(url)
scheme = split_url.scheme
print(scheme)
hostname = split_url.hostname
print(hostname)
path = split_url.path
print(path)
port = split_url.port
print(port)
query = split_url.query
print(query)
fragment = split_url.fragment
print(fragment)
username = split_url.username
print(username)
password = split_url.password
print(password)

query_params = parse_qs(query)
print(query_params)

unquoted_query = unquote(query)
print(unquoted_query)

original_url = urlunsplit((scheme,hostname,path,query,fragment))
print(original_url)






