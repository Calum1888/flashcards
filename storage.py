import json
from pathlib import Path
from models import Deck

def load_deck(name: str, decks_dir=Path("decks")):
    path = f'{decks_dir}/{name}.json'

    with open(path) as f:
        data = json.load(f)

    card_data = Deck.from_dicts(name, data)

    return card_data