import argparse

from flashcards.storage import load_deck
from flashcards.exceptions import FlashcardError
from flashcards.quiz import run_quiz, show_summary

def build_parser():
    parser = argparse.ArgumentParser(prog="flashcards", description="Flashcard quiz app")
    subparsers = parser.add_subparsers(dest="command", required=True)
    quiz_parser = subparsers.add_parser("quiz", help="Run a quiz on a deck")
    quiz_parser.add_argument("deck", help="Name of the deck, e.g. python")
    return parser

def main():
    parser = build_parser()
    args = parser.parse_args()

    try:
        match args.command:
            case "quiz":
                deck = load_deck(args.deck)
                score, answered = run_quiz(deck)
                print(show_summary(score, answered))
    except FlashcardError as err:
        raise
if __name__ == "__main__":
    main()