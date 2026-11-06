import json
from pathlib import Path
from models import Deck, Card

DECKS_DIR = Path(__file__).parent / "decks"

def load_deck(name: str, decks_dir: Path = DECKS_DIR) -> Deck:
    '''
    Loads a deck of flashcards from a json file and returns the deck.
    '''
    path = decks_dir / f"{name}.json"

    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    return Deck.from_dicts(name, data)

def save_deck(deck: Deck, decks_dir: Path = DECKS_DIR) -> None:
    '''
    Saves the deck with any new flashcards that have been added to the deck.
    '''

    decks_dir.mkdir(parents=True, exist_ok=True)

    data = [card.to_dict() for card in deck]

    path = decks_dir / f"{deck.name}"

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
