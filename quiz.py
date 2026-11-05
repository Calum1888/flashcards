from models import normalize_string, Card, Deck

card_data = [
    {
        "question": "What type does *args collect extra positional arguments into?",
        "answers": ["tuple"],
    },
    {
        "question": "What type does **kwargs collect extra keyword arguments into?",
        "answers": ["dict", "dictionary"],
    },
    {
        "question": "What does a function return if it has no return statement?",
        "answers": ["None"],
    },
    {
        "question": "Which keyword skips the rest of the current loop iteration?",
        "answers": ["continue"],
    },
    {
        "question": "Which keyword exits a loop immediately?",
        "answers": ["break"],
    },
    {
        "question": "Which string method removes whitespace from both ends of a string?",
        "answers": ["strip", "strip()", ".strip()"],
    },
    {
        "question": "Is a tuple mutable or immutable?",
        "answers": ["immutable"],
    },
    {
        "question": 'How many items are in the list returned by "a,b,c".split(",")?',
        "answers": ["3", "three"],
    },
    {
        "question": 'Which exception is raised by int("abc")?',
        "answers": ["ValueError"],
    },
    {
        "question": "Which built-in function gives you both the index and the item when looping?",
        "answers": ["enumerate", "enumerate()"],
    },
]

def flashcard(card: Card) -> str:
    '''
    
    '''
    print(card)
    # takes user answer
    user = input('Answer: ')

    # normalizes user answer
    norm_user = normalize_string(user)

    checked = card.check_answer(user)

    # quits loop
    if norm_user == 'quit':
        print('Quitting session.')
        return 'quit'
    # skips to next question
    elif norm_user == 'skip':
        print('Skipping Question.')
        return 'skip'
    # correct answer
    elif checked == True:
        print('Correct answer. Well done!')
        return 'correct'
    # incorrect answer
    elif checked == False:
        print(f'Unlucky, incorrect answer. The correct answer is {card.answers[0]}')
        return 'incorrect'

def run_quiz(deck: Deck) -> tuple[int, int]:
    '''
    Runs through all the flashcards in the deck, keeping track of the number answered and the score for correct answers.

    Input:
        deck (list) A list of dictionaries of questions and answers.
    Returns:
        score (int) The score.
        answered (int) Number of questions answered.
    '''
    # initializes the score and tally of questions answered 
    score = 0
    answered = 0

    # loops through all the cards in the deck
    for card in deck.shuffled():

        # loads the card only once for each card instead of for every different outcome
        result = flashcard(card)

        # breaks loop for quit input
        if result == 'quit':
            break
        # skip to next question
        elif result == 'skip':
            pass
        # +1 score for correct answers
        elif result == 'correct':
            score += 1
            answered += 1
        # 0 score for incorrect answers
        elif result == 'incorrect':
            answered += 1

    return score, answered

def show_summary(score: int, answered: int) -> str:

    if answered == 0:
        return '0 questions answered'

    else:
        result = score / answered
        pct = round(100 * result, 2)

        if pct >= 75:
            return f'You answered {answered} questions and got {pct}%. Amazing job!'
        elif pct >= 50:
            return f'You answered {answered} questions and got {pct}%. Good job!'
        else:
            return f'You answered {answered} questions and got {pct}%. Keep practicing!'

def main() -> None:
    """Run a flashcard quiz and print the summary.
    """
    print("Flashcard quiz. Type 'skip' to skip a question or 'quit' to stop.\n")
    deck = Deck.from_dicts("python", card_data)
    score, answered = run_quiz(deck)
    print(show_summary(score, answered))


if __name__ == "__main__":
    main()