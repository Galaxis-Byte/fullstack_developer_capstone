import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")

def get_request(endpoint, **kwargs):
    """
    Send a GET request to the specified endpoint with optional query parameters.

    Args:
        endpoint (str): The API endpoint.
        **kwargs: Query parameters to include in the request.

    Returns:
        dict: The JSON response from the server.
    """
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params = params + key + "=" + value + "&"
    request_url = backend_url + endpoint + "?" + params
    print("GET from {}".format(request_url))
    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")

def analyze_review_sentiments(text):
    """
    Analyze the sentiment of the given text using the sentiment analyzer service.

    Args:
        text (str): The text to analyze.

    Returns:
        dict: The JSON response from the sentiment analyzer.
    """
    request_url = sentiment_analyzer_url + "analyze/" + text
    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")

def post_review(data_dict):
    """
    Post a review to the backend service.

    Args:
        data_dict (dict): The review data to post.

    Returns:
        dict: The JSON response from the backend.
    """
    request_url = backend_url + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")
