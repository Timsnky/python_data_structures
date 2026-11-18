from urllib.request import urlopen, Request
from urllib.parse import urlencode, urlunsplit
import json
from pathlib import Path

def url_open():
    with urlopen("https://job-boards.greenhouse.io/canonical/jobs/2614095?gh_src=1943652a1", timeout=30) as response:
        print("Status Code: ", response.status)
        print("URL: " , response.geturl())
        print(response.headers.get("Content-Type"))

        body = response.read()
        encoding = response.headers.get_content_charset() or "utf-8"
        html = body.decode(encoding)

# test_url_open()

def url_open_get():
    params = {
        "query": "software & engineer",
        "location": ["Nairobi", "Global"],
        "type": ["Remote", "Hybrid", "Onsite"],
        "page": 1
    }

    encoded_params = urlencode(params)
    url = urlunsplit(("https", "httpbin.org", "/get", encoded_params, ""))
    with urlopen(url) as response:
        print("Status Code: ", response.status)
        print("URL: " , response.geturl())
        print(response.headers.get("Content-Type"))

        body = response.read().decode(response.headers.get_content_charset() or "utf-8")
        result = json.loads(body)
        print(result.get("args"))
        print(result.keys())
        print(result)

# url_open_get()

def url_open_with_request():
    params = {
        "query": "software & engineer",
        "location": ["Nairobi", "Global"],
        "type": ["Remote", "Hybrid", "Onsite"],
        "page": 1
    }

    request = Request(
        "https://httpbin.org/post",
        headers={
            "User-Agent": "PyCharm",
            "Content-Type": "application/json",
            "Accept": "application/json"
        },
        data=json.dumps(params).encode("utf-8"),
        method="POST"
    )

    with urlopen(request) as response:
        print("Status Code: ", response.status)
        print("URL: " , response.geturl())

        result = json.loads(response.read().decode(response.headers.get_content_charset() or "utf-8"))
        print(result)
        print(result.get("data", {}))
        print(result.get("json", {}))

# url_open_with_request()

def url_open_download_file():
    destination = Path("url_sample.txt")
    url = "https://sample-files.com/downloads/documents/txt/long-doc.txt"

    with urlopen(url) as response:
        print("Status Code: ", response.status)

        with destination.open("wb") as destination_file:
            while chunk := response.read(32 * 1024):
                destination_file.write(chunk)

    print("Downloaded file to: ", destination.resolve())

    file_content = destination.read_text(encoding="utf-8")
    print(file_content)

# url_open_download_file()

