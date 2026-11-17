import pytest

from models import Card, Deck

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

def test_correct_answer_is_accepted():
    card = Card("Is a tuple mutable?", ["immutable"])
    assert card.check_answer("immutable")

def test_check_answer_ignores_case_and_punctuation():
    card = Card("Is a tuple mutable?", ["immutable"])   
    result = card.check_answer(" Immutable. ")          
    assert result is True                

def test_reject_wrong_answer():
    card = Card("Is a tuple mutable?", ["immutable"])   
    result = card.check_answer("mutable")          
    assert result is False

def test_reject_empty_answer():
    card = Card("Is a tuple mutable?", ["immutable"])
    result = card.check_answer("")
    assert result is False

def test_reject_partial_answers():
    card = Card("Is a tuple mutable?", ["immutable"])
    result = card.check_answer("immut")
    assert result is False

def test_additional_answers_accepted():
    card = Card("What type does **kwargs collect extra keyword arguments into?", ["dict", "dictionary"])
    result = card.check_answer("dictionary")
    assert result is True

def test_check_doesnt_alter_card_answers():
    card = Card("Which exception is raised by int(\"abc\")?", ["ValueError"])
    card.check_answer("value")
    assert card.answers == ["ValueError"] 

def test_from_to_dict_equality():
    card = Card("Which exception is raised by int(\"abc\")?", ["ValueError"])
    copy = Card.from_dict(card.to_dict())
    assert copy.question == card.question 
    assert copy.answers == card.answers 

def test_empty_deck_length():
    assert len(Deck("empty")) == 0

def test_empty_decks_dont_share_cards():
    card = Card("Which exception is raised by int(\"abc\")?", ["ValueError"])
    deck_1 = Deck("empty")
    deck_2 = Deck("empty")
    deck_1.add(card)
    assert len(deck_1) == 1
    assert len(deck_2) == 0

def test_from_dicts():
    cards =[{
        "question": "What does a function return if it has no return statement?",
        "answers": ["None"]
    },
    {
        "question": "Which keyword skips the rest of the current loop iteration?",
        "answers": ["continue"]
    }]

    deck = Deck.from_dicts("deck_1", cards)
    assert len(deck) == 2
    assert all(isinstance(card, Card) for card in deck)

def test_shuffle_preserves_deck_order(sample_deck):
    deck_order = [card.question for card in sample_deck]
    sample_deck.shuffled()
    assert deck_order == [card.question for card in sample_deck]

def test_shuffle_returns_same_cards(sample_deck):
    result = sample_deck.shuffled()
    assert len(result) == len(sample_deck)