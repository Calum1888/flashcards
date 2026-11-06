import json
from pathlib import Path
from models import Deck

def load_deck(name: str, decks_dir: Path = Path("decks")) -> Deck:
    '''
    Loads a deck of flashcards from a json file and returns the deck.
    '''
    path = decks_dir / f"{name}.json"

    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    return Deck.from_dicts(name, data)