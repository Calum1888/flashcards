import random

def normalize_string(answer: str) -> str:
    '''
    Takes a users answer and returns as a string which is all lowercase, with punctuation removed.

    Input:
        answer (str) An answer to a question.
    Return:
        A normalized string which has space and punctuation removed
        and all in lowercase.
    Example:
        '  The dog sat ON the mat.' -> 'the dog sat on the mat' 
    '''    
    return answer.strip().lower().strip('.,!?()')

class Card():
    def __init__(self, question: str, answers: list):
        self.question = question
        self.answers = answers

    def check_answer(self, user_answer: str) -> bool:
        '''
        Takes the users answer and checks if it is correct or not.

        Input:
            user_answer (str) The users answer.
            accepted_answers (list) A list of possible/acceptable answers.
        Returns:
            user_answer in accepted_answers (bool) True/False if the answer is correct/incorrect
        Example:
            user_answer = 'tuple' in ['tuple'] = acceptable_answers -> True
        '''
        # normalize the users answer 
        user_answer = normalize_string(user_answer)

        # normalize the acceptable answers
        accepted_answers = [normalize_string(answer) for answer in self.answers]

        return user_answer in accepted_answers

    def __repr__(self):
        return f'Question: {self.question!r}, Answers: {self.answers!r}'

    def __str__(self):
        return f'Question: {self.question}'

    @classmethod
    def from_dict(cls, flashcard_dict: dict):
        '''
        Create a Card from a dict with question and answers keys.
        '''
        return cls(flashcard_dict['question'], flashcard_dict['answers'])


class Deck():
    def __init__(self, name: str, cards = None):
        self.name = name
        if cards is None:
            cards = []
        self.cards = cards

    def add(self, card):
        self.cards.append(card)
        
    def shuffled(self):
        cards_copy = self.cards.copy()
        random.shuffle(cards_copy)
        return cards_copy

    def __len__(self):
        return len(self.cards)

    def __iter__(self):
        return iter(self.cards)

    def __repr__(self):
        return f'Deck({self.name!r}, {len(self.cards)} cards)'

    @classmethod
    def from_dicts(cls, name: str, card_dicts: list):
        cards = [Card.from_dict(d) for d in card_dicts]
        return cls(name, cards)