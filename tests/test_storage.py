import json

import pytest

from flashcards.storage import save_deck, load_deck
from flashcards.exceptions import DeckNotFoundError, DeckFormatError


def test_save_load_consistency(sample_deck, tmp_path):
    save_deck(sample_deck, decks_dir=tmp_path)
    loaded = load_deck(sample_deck.name, decks_dir=tmp_path)

    assert [c.question for c in loaded] == [c.question for c in sample_deck]
    assert [c.answers for c in loaded] == [c.answers for c in sample_deck]


def test_create_new_folder_in_save(sample_deck, tmp_path):
    new_path = tmp_path / "new_folder"
    save_deck(sample_deck, decks_dir=new_path)

    assert (new_path / f"{sample_deck.name}.json").exists()


def test_missing_deck_error(tmp_path):
    with pytest.raises(DeckNotFoundError):
        load_deck("dog", decks_dir=tmp_path)


def test_invalid_json_error(tmp_path):
    (tmp_path / "bad.json").write_text("{not valid", encoding="utf-8")

    with pytest.raises(DeckFormatError):
        load_deck("bad", decks_dir=tmp_path)


def test_missing_field_error(tmp_path):
    card_dicts = [{"question": "Which keyword exits a loop immediately?"}]  # no "answers"
    (tmp_path / "incomplete.json").write_text(json.dumps(card_dicts), encoding="utf-8")

    with pytest.raises(DeckFormatError):
        load_deck("incomplete", decks_dir=tmp_path)