def create_random_number(minimum : int, maximum : int) -> int:
    """
    Creates a random integer within the specified range, minimum and maximum, both included.

    Parameters:
        - minimum (int) : The inclusive lower bound of the random number range.
        - maximum (int) : The inclusive upper bound of the random number range.

    Returns:
        - random_number (int) : A randomly created integer within the specified range.
    """

    import random

    random_number = random.randint(minimum, maximum)

    print(f'minimum       : { minimum }')
    print(f'maximum       : { maximum }')
    print(f'random_number : { random_number }')

    return random_number


if __name__ == '__main__':
    """
    Elyra Pipelines
    """

    import os
    import json

    minimum = int(os.getenv('minimum'))
    maximum = int(os.getenv('maximum'))

    random_number = create_random_number(
        minimum = minimum,
        maximum = maximum
    )

    output = {
        'minimum'       : minimum,
        'maximum'       : maximum,
        'random_number' : random_number
    }

    with open('create_random_number.json', 'w', encoding = 'utf-8') as output_file:

        json.dump(output, output_file, ensure_ascii = False, indent = 4)