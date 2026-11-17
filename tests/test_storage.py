import json

import pytest
from flashcards.models import Deck
from flashcards.storage import save_deck, load_deck, list_decks
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

def test_list_decks_returns_sorted_names(tmp_path, sample_deck):
    save_deck(Deck("zeta", sample_deck.cards), decks_dir=tmp_path)
    save_deck(Deck("alpha", sample_deck.cards), decks_dir=tmp_path)
    assert list_decks(decks_dir=tmp_path) == ["alpha", "zeta"]


def test_list_decks_empty_folder(tmp_path):
    assert list_decks(decks_dir=tmp_path) == []


def test_list_decks_ignores_non_json_files(tmp_path, sample_deck):
    save_deck(sample_deck, decks_dir=tmp_path)
    (tmp_path / "notes.txt").write_text("not a deck", encoding="utf-8")
    assert list_decks(decks_dir=tmp_path) == [sample_deck.name]


def test_list_decks_missing_folder(tmp_path):
    assert list_decks(decks_dir=tmp_path / "does_not_exist") == []

def test_all_bundled_decks_load():
    names = list_decks()
    assert names, "no decks found"
    for name in names:
        assert len(load_deck(name)) > 0