class FlashcardError(Exception):
    """Base class for all errors raised by the flashcard app."""

class DeckNotFoundError(FlashcardError):
    """Raised when a deck file does not exist."""

class DeckFormatError(FlashcardError):
    """Raised when a deck file is not valid JSON or is missing required fields."""