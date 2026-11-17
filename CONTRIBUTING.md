# Contributing

Thanks for your interest in contributing. The easiest and most useful way to help is to **add or improve flashcards**. Each deck is a JSON file, so you don't need to write any Python.

## Adding cards or a new deck

Decks live in `flashcards/decks/`. Each file is one deck, named after the deck (`sql.json` is the `sql` deck).

A deck is a list of cards. Each card has a `question` and a list of accepted `answers`:

```json
[
  {
    "question": "Which clause filters groups after aggregation?",
    "answers": ["having"]
  },
  {
    "question": "Which join returns all rows from the left table plus matching rows from the right?",
    "answers": ["left join", "left outer join"]
  }
]
```

To add a new deck, create a new `.json` file in that folder. To add to an existing deck, add cards to the end of its list.

### What makes a good card

The app checks answers by exact match, after making them lowercase and removing surrounding spaces and trailing punctuation. So cards work best when:

- **The answer is short:** one word or a short phrase. "What type does *args collect into?" with the answer `tuple` works. "Explain what *args does" doesn't, because nobody will type the same sentence.
- **There's one clear correct answer.** If a question has several correct answers, rephrase it until it has one.
- **Common variations are listed**, e.g. `["k-means", "kmeans", "k means"]`, or British and American spellings like `["normalisation", "normalization"]`.
- **The answer doesn't depend on order.** Avoid questions whose answer is a list of items, since `int, str` and `str, int` won't match.
- **It's accurate.** Please check facts, especially for ML and statistics definitions.
- **It's useful for interviews.** Aim for things that come up in data science and ML interviews.

### Deck ideas

New decks that would be especially welcome:

- Statistics and probability
- pandas
- NumPy
- Git
- Experiment design and A/B testing
- Deep learning

### Checking your deck

Before opening a pull request:

1. Check the deck loads: `flashcards list` should show it with the right card count.
2. Try a few of the cards: `flashcards quiz <deck> --count 5`.
3. Run the tests: `pytest`.

## Contributing code

1. Fork the repository and create a branch for your change.
2. Set up a development environment:

   ```bash
   python -m venv .venv
   # Windows: .venv\Scripts\activate
   # macOS / Linux: source .venv/bin/activate
   pip install -e ".[test]"
   ```

3. Make your change, and **add tests** for any new behaviour.
4. Check that all tests pass with `pytest -v`.
5. Open a pull request describing what you changed and why.

Tests run automatically on GitHub Actions for every pull request, on Windows and Ubuntu with Python 3.11 to 3.13.

### Code guidelines

- Keep logic separate from input and output, so it can be tested without user input (see `models.py` and `storage.py`).
- Raise the app's own exceptions from `exceptions.py`, rather than letting low-level errors reach the user.
- Write clear docstrings and type hints.
- The app uses only the standard library. Please discuss in an issue before adding a dependency.

## Reporting a problem

If you find a wrong answer on a card, a bug or a confusing error message, please [open an issue](../../issues). For a card problem, include the deck name and the question.