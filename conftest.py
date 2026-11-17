import pytest

from models import Deck

@pytest.fixture
def sample_deck():
    card_dicts = [{
        "question": "Which keyword exits a loop immediately?",
        "answers": ["break"]
    },
    {
        "question": "Which string method removes whitespace from both ends of a string?",
        "answers": ["strip", "strip()", ".strip()"]
    },
    {
        "question": "Is a tuple mutable or immutable?",
        "answers": ["immutable"]
    },
    {
        "question": "How many items are in the list returned by \"a,b,c\".split(\",\")?",
        "answers": ["3", "three"]
    },
    {
        "question": "Which exception is raised by int(\"abc\")?",
        "answers": ["ValueError"]
    }]
    return Deck.from_dicts("sample", card_dicts)