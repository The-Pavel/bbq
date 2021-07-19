import streamlit as st

from bbq.quotes import get_quotes

response = get_quotes()  # assuming the function returns an author and a quote

f"{response['quote']}, {response['author']}"
