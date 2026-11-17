# Flashcards

![Tests](https://github.com/Calum1888/flashcards/actions/workflows/tests.yml/badge.svg)

A command-line flashcard quiz app written in Python. Decks are stored as JSON files, and you can quiz yourself, list your decks and add new cards from the terminal.

It comes with three decks:

| Deck | Cards | Covers |
|---|---|---|
| `python` | 44 | Syntax, strings, exceptions, functions, classes, dunder methods |
| `ml` | 40 | Supervised and unsupervised learning, overfitting, loss functions, regularisation, metrics, neural networks |
| `sql` | 44 | Filtering, grouping, joins, NULL handling, CTEs, window functions, transactions |

The app uses only the Python standard library. [pytest](https://docs.pytest.org/) is needed only to run the tests.

## Requirements

- Python 3.11 or newer

## Installation

```bash
pip install -e ".[test]"
```

## Usage

Run all commands from the project root folder.

### Take a quiz

```bash
flashcards quiz python
```

```
Type 'skip' to skip a question or 'quit' to stop.

Question: Which keyword exits a loop immediately?
Answer (or 'skip' / 'quit'): break
Correct answer. Well done!
Question: What type does *args collect extra positional arguments into?
Answer (or 'skip' / 'quit'): list
Unlucky, incorrect answer. The correct answer is tuple
...
```

Questions are asked in a random order. Answers are not case-sensitive, and surrounding spaces and trailing punctuation are ignored, so `" Tuple. "` matches `tuple`. Many cards accept more than one answer.

To answer only a set number of questions, use `--count`:

```bash
flashcards quiz sql --count 10
```

During a quiz:
- type `skip` to move on without answering. Skipped cards don't count towards your score.
- type `quit` to stop early. Your score is based on the questions you answered.

### List your decks

```bash
flashcards list
```

```
1. ml (40 cards)
2. python (44 cards)
3. sql (44 cards)
```

### Add a card

```bash
flashcards add python
```

```
Question: Which built-in function returns the largest item?
Answer(s), separated by commas: max, max()
Card added to 'python' (45 cards).
```

### Help

```bash
flashcards --help
flashcards quiz --help
```

## Deck format

Each deck is a JSON file in the `decks/` folder, named after the deck (`python.json` is the `python` deck). A deck is a list of cards, and each card has a question and a list of accepted answers:

```json
[
  {
    "question": "Is a tuple mutable or immutable?",
    "answers": ["immutable"]
  },
  {
    "question": "What type does **kwargs collect extra keyword arguments into?",
    "answers": ["dict", "dictionary"]
  }
]
```

To create a new deck, add a JSON file in this format to `decks/`. It will appear in `python -m flashcards list`.

If a deck file is missing, isn't valid JSON, or has a card without a `question` or `answers` field, the app prints a short error message instead of crashing.

## Project structure

```
flashcards/
├── flashcards/
│   ├── __init__.py
│   ├── __main__.py      # command-line interface (argparse)
│   ├── models.py        # Card and Deck classes
│   ├── storage.py       # loading, saving and listing decks
│   ├── quiz.py          # quiz loop, scoring and adding cards
│   ├── exceptions.py    # custom exceptions
│   └── decks/           # deck JSON files
├── tests/
│   ├── test_models.py
│   ├── test_storage.py
│   ├── test_quiz.py
│   └── test_cli.py
├── conftest.py          # shared test fixtures
├── requirements.txt
└── README.md
```

## Running the tests

```bash
pytest -v
```

The tests cover answer checking, deck behaviour, saving and loading (using temporary folders, so real decks are never touched), error handling, the quiz loop (with simulated keyboard input) and command-line argument parsing.

Tests run automatically on GitHub Actions for every push and pull request, on Windows and Ubuntu with Python 3.11, 3.12 and 3.13.

## Possible future work

- Quiz history and a `stats` command showing scores over time and the hardest cards
- Spaced repetition, so cards you get wrong come up more often
- `delete` and `edit` commands
- Importing decks from CSV