import requests
from bs4 import BeautifulSoup

def check_xss(url: str) -> bool:
    test_payload = "<script>alert('XSS')</script>"
    try:
        response = requests.post(url, data={"input": test_payload}, timeout=5)
        return test_payload in response.text
    except Exception as e:
        print(f"XSS check error: {e}")
        return False

def check_sqli(url: str) -> bool:
    test_payloads = ["' OR 1=1 --", "' AND 1=CONVERT(int,@@version)--"]
    for payload in test_payloads:
        try:
            response = requests.get(f"{url}?id={payload}", timeout=5)
            if "error in your SQL syntax" in response.text.lower():
                return True
        except Exception as e:
            print(f"SQLi check error: {e}")
    return False