import json
from pathlib import Path
from flashcards.models import Deck, Card

from flashcards.exceptions import DeckNotFoundError, DeckFormatError

DECKS_DIR = Path(__file__).parent / "decks"

def load_deck(name: str, decks_dir: Path = DECKS_DIR) -> Deck:
    """Load a deck from <decks_dir>/<name>.json and return it as a Deck."""
    path = decks_dir / f"{name}.json"

    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)

    except FileNotFoundError as err:
        raise DeckNotFoundError(f"No deck called {name!r} in {decks_dir}") from err
    
    except json.JSONDecodeError as err:
        raise DeckFormatError(
            f"{path.name} is not valid JSON (line {err.lineno}, column {err.colno})"
        ) from err

    try:
        return Deck.from_dicts(name, data)
    
    except KeyError as err:
        raise DeckFormatError(f"A card in {path.name} is missing the {err} field") from err

def save_deck(deck: Deck, decks_dir: Path = DECKS_DIR) -> None:
    '''
    Saves the deck with any new flashcards that have been added to the deck.
    '''

    decks_dir.mkdir(parents=True, exist_ok=True)

    data = [card.to_dict() for card in deck]
    
    path = decks_dir / f"{deck.name}.json"

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def list_decks(decks_dir: Path = DECKS_DIR) -> list[str]:
    """
    Return the names of all decks in decks_dir, sorted alphabetically.
    """
    return sorted(path.stem for path in decks_dir.glob("*.json"))