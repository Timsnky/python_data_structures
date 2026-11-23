import requests
import logging
from requests.adapters import HTTPAdapter
from requests.exceptions import HTTPError, Timeout, ConnectionError, RequestException
from urllib3 import Retry

# Simple get request
def requests_get_request():
    url = "https://httpbin.org/anything"
    # url = "https://httpbin.org/anythi"
    # url = "https://127.0.0.1:9999"
    params = {
        "name": "James Anderson",
        "phone_numbers": [12344, 45676],
        "message": "Hello world"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        print("Status Code: ", response.status_code)
        print("Content Type: ", response.headers.get("content-type"))
        response.raise_for_status()
        result = response.json()
    except Timeout as exc:
        print("Timeout Error: ", exc)
    except ConnectionError as exc:
        print("Connection Error: ", exc)
    except HTTPError as exc:
        print("Http Error: ", exc)
    except RequestException as exc:
        print("Request Exception: ", exc)
    else:
        print("Success")
        print(result)


# requests_get_request()

# Sample post request
def requests_post_request():
    url = "https://jsonplaceholder.typicode.com/posts"
    data = {
        "userId": 1,
        "id": 1,
        "title": "Sample title",
        "body": "This is a body"
    }

    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
    except RequestException as exc:
        print("Request Exception: ", exc)
    else:
        result = response.json()
        print(result)

# requests_post_request()

# Sample retry setup
def requests_get_with_retries():
    retry_policy = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "HEAD"],
        respect_retry_after_header=True
    )

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(name)s %(levelname)s: %(message)s"
    )
    logging.getLogger("urllib3").setLevel(logging.DEBUG)

    retry_adapter = HTTPAdapter(max_retries=retry_policy)
    url = "https://httpbin.org/status/503"
    # url = "https://httpbin.org/anything"

    with requests.Session() as session:
        session.mount("https://", retry_adapter)

        try:
            response = session.get(url, timeout=(3, 10))
            response.raise_for_status()
        except requests.exceptions.RetryError as exc:
            print("Retry policy exhausted: ", exc)
        except requests.exceptions.Timeout as exc:
            print("Request timed out: ", exc)
        except requests.exceptions.RequestException as exc:
            print("Request Exception: ", exc)
        else:
            print(response.json())

requests_get_with_retries()






