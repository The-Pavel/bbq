import requests

def get_quotes():

    url = 'https://breaking-bad-quotes.herokuapp.com/v1/quotes'

    response = requests.get(url).json()[0]

    print(f"{response['author']} said '{response['quote']}'")
    return response
