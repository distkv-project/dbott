import requests


def main():
    print("hello world.")
    URL = "https://api.github.com/repos/dst-project/giter/pulls/1/reviews"
    headers = {
        'Authorization': "Basic am92YW55LXdhbmc6d3F3ZTE1MjE7",
    }

    payload = "{\n  \"body\": \"This is a comment from giter robot in python.\",\n  \"event\": \"COMMENT\"\n}"

    response = requests.request("POST", URL, headers=headers, data=payload)
    print(response.text)


if __name__ == "__main__":
    main()
