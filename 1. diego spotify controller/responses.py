from random import choice, randint


def get_responses(user_input) -> str:
    lowered = user_input.lower()

    if lowered == "":
        return 'Well, you\'re awfully silent...'
    elif 'hello' in lowered:
        return 'Hello there!'
    elif 'how are you' in lowered:
        return 'Good, thanks!'
    elif 'bye' in lowered:
        return 'See you!'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 6)}'
    else:
        return choice([
            'I do not understand...',
            'What are you talking about?',
            'Do you mind rephrasing that?'
        ])