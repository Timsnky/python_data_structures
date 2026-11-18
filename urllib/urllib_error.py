from urllib.error import URLError, HTTPError
from urllib.request import urlopen

def url_opener_with_404():
    try:
        with urlopen("https://httpbin.org/status/404", timeout=1) as response:
            print("Status: ", response.status())
    except HTTPError as e:
        print("Http Error Code: ", e.code)
        print("Http Error Message: ", e.msg)
    except URLError as e:
        print("Url Error Reason: ", e.reason)
    except TimeoutError as e:
        print("Timeout Error Reason: ", e)

# url_opener_with_404()