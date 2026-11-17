import sys
import argparse

from flashcards.storage import load_deck, save_deck, list_decks
from flashcards.exceptions import FlashcardError
from flashcards.quiz import run_quiz, show_summary, add_card

def build_parser():
    parser = argparse.ArgumentParser(prog="flashcards", description="Flashcard quiz app")
    subparsers = parser.add_subparsers(dest="command", required=True)

    quiz_parser = subparsers.add_parser("quiz", help="Run a quiz on a deck")
    quiz_parser.add_argument("deck", help="Name of the deck, e.g. python")
    quiz_parser.add_argument("--count", type=int, default=None, help="Number of questions you want to answer")

    add_parser = subparsers.add_parser("add", help="Add a card to a deck")
    add_parser.add_argument("deck", help="Name of the deck to add to")

    subparsers.add_parser("list", help="Show all decks")

    return parser

def main():
    parser = build_parser()
    args = parser.parse_args()

    try:
        match args.command:
            case "quiz":
                deck = load_deck(args.deck)
                print("Type 'skip' to skip a question or 'quit' to stop.\n")
                score, answered = run_quiz(deck, args.count)
                print(show_summary(score, answered))
            case "list":
                names = list_decks()
                if not names:
                    print("No decks found.")
                for number, name in enumerate(names, start=1):
                    try:
                        deck = load_deck(name)
                        print(f"{number}. {deck.name} ({len(deck)} cards)")
                    except FlashcardError as err:
                        print(f"{name} (could not load: {err})")
            case "add":
                deck = load_deck(args.deck)
                card = add_card()
                deck.add(card)
                save_deck(deck)
                print(f"Card added to {deck.name!r} ({len(deck)} cards).")
            
    except FlashcardError as err:
        print(f"Error: {err}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nQuiz cancelled.")
        sys.exit(130)


if __name__ == "__main__":
    main()