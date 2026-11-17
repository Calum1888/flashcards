import sys
import argparse

from flashcards.storage import load_deck
from flashcards.exceptions import FlashcardError
from flashcards.quiz import run_quiz, show_summary

def build_parser():
    parser = argparse.ArgumentParser(prog="flashcards", description="Flashcard quiz app")
    subparsers = parser.add_subparsers(dest="command", required=True)
    quiz_parser = subparsers.add_parser("quiz", help="Run a quiz on a deck")
    quiz_parser.add_argument("deck", help="Name of the deck, e.g. python")
    quiz_parser.add_argument("--count", type=int, default=None, help="Number of questions you want to answer")
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
    except FlashcardError as err:
        print(f"Error: {err}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nQuiz cancelled.")
        sys.exit(130)


if __name__ == "__main__":
    main()