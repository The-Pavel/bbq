from bbq.quotes import get_quotes

def test_bbquote():
    assert type(get_quotes()) == dict
    assert 'author' in get_quotes().keys()
