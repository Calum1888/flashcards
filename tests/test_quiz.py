import pytest

from models import Card, Deck
from quiz import flashcard, run_quiz, show_summary


def fake_inputs(monkeypatch, answers):
    """Make input() return each item in `answers` in turn."""
    responses = iter(answers)
    monkeypatch.setattr("builtins.input", lambda prompt="": next(responses))


@pytest.fixture
def card():
    return Card("What type does *args collect into?", ["tuple"])


@pytest.fixture
def uniform_deck():
    """Every card has the same answer, so results don't depend on shuffle order."""
    return Deck("uniform", [Card(f"Question {i}", ["yes"]) for i in range(3)])


# ---- flashcard ----

def test_flashcard_correct(monkeypatch, card):
    fake_inputs(monkeypatch, ["tuple"])
    assert flashcard(card) == "correct"


def test_flashcard_correct_with_messy_input(monkeypatch, card):
    fake_inputs(monkeypatch, ["  Tuple. "])
    assert flashcard(card) == "correct"


def test_flashcard_incorrect(monkeypatch, card):
    fake_inputs(monkeypatch, ["list"])
    assert flashcard(card) == "incorrect"


def test_flashcard_incorrect_shows_answer(monkeypatch, capsys, card):
    fake_inputs(monkeypatch, ["list"])
    flashcard(card)
    assert "tuple" in capsys.readouterr().out


@pytest.mark.parametrize("command", ["skip", "SKIP", " skip "])
def test_flashcard_skip(monkeypatch, card, command):
    fake_inputs(monkeypatch, [command])
    assert flashcard(card) == "skip"


@pytest.mark.parametrize("command", ["quit", "QUIT", "quit."])
def test_flashcard_quit(monkeypatch, card, command):
    fake_inputs(monkeypatch, [command])
    assert flashcard(card) == "quit"


def test_flashcard_empty_input_is_incorrect(monkeypatch, card):
    fake_inputs(monkeypatch, [""])
    assert flashcard(card) == "incorrect"


# ---- run_quiz ----

def test_run_quiz_all_correct(monkeypatch, uniform_deck):
    fake_inputs(monkeypatch, ["yes", "yes", "yes"])
    assert run_quiz(uniform_deck) == (3, 3)


def test_run_quiz_all_wrong(monkeypatch, uniform_deck):
    fake_inputs(monkeypatch, ["no", "no", "no"])
    assert run_quiz(uniform_deck) == (0, 3)


def test_run_quiz_skips_not_counted(monkeypatch, uniform_deck):
    fake_inputs(monkeypatch, ["skip", "yes", "skip"])
    assert run_quiz(uniform_deck) == (1, 1)


def test_run_quiz_quit_on_first_card(monkeypatch, uniform_deck):
    fake_inputs(monkeypatch, ["quit"])
    assert run_quiz(uniform_deck) == (0, 0)


def test_run_quiz_quit_stops_asking(monkeypatch, uniform_deck):
    fake_inputs(monkeypatch, ["yes", "quit"])   # only two answers supplied
    assert run_quiz(uniform_deck) == (1, 1)     # would raise StopIteration if it asked a third time


# ---- show_summary ----

def test_show_summary_zero_answered_does_not_crash():
    message = show_summary(0, 0)
    assert "0" in message


def test_show_summary_high_score():
    assert "Amazing" in show_summary(3, 3)


def test_show_summary_low_score():
    assert "Keep practicing" in show_summary(1, 4)