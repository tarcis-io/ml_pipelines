def create_odds_or_evens_message(hello_world_message : str, random_number : int) -> str:
    """
    Creates a game result message based on the given random number, containing the given hello world message.

    Parameters:
        - hello_world_message (str) : The hello world message to be incorporated into the odds or evens message.
        - random_number       (int) : The random number used to determine the odds or evens result.

    Returns:
        - odds_or_evens_message (str) : The message combining the hello world message and the odds or evens game result.

    Raises:
        - ValueError : If the given hello world message is empty or None.
    """

    if not hello_world_message:

        raise ValueError

    odds_or_evens_message = f"""
    { hello_world_message }

    You're odds, I'm evens...
    Random Number : { random_number }

    { 'I won! Better luck next time.' if random_number % 2 == 0 else 'You won! I like you!' }
    """

    print(f'hello_world_message   : { hello_world_message }')
    print(f'random_number         : { random_number }')
    print(f'odds_or_evens_message : { odds_or_evens_message }')

    return odds_or_evens_message


if __name__ == '__main__':
    """
    Elyra Pipelines
    """

    import json

    create_hello_world_message_output = json.load(open('create_hello_world_message.json', 'r', encoding = 'utf-8'))
    create_random_number_output       = json.load(open('create_random_number.json',       'r', encoding = 'utf-8'))

    hello_world_message = create_hello_world_message_output['hello_world_message']
    random_number       = create_random_number_output['random_number']

    odds_or_evens_message = create_odds_or_evens_message(
        hello_world_message = hello_world_message,
        random_number       = random_number
    )

    output = {
        'hello_world_message'   : hello_world_message,
        'random_number'         : random_number,
        'odds_or_evens_message' : odds_or_evens_message
    }

    with open('create_odds_or_evens_message.json', 'w', encoding = 'utf-8') as output_file:

        json.dump(output, output_file, ensure_ascii = False, indent = 4)