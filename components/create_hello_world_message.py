def create_hello_world_message(name : str) -> str:
    """
    Creates a personalized greeting message for the given name.

    Parameters:
        - name (str) : The name for which the message is created.

    Returns:
        - hello_world_message (str) : A personalized greeting message for the given name.

    Raises:
        - ValueError : If the given name is empty or None.
    """

    if not name:

        raise ValueError

    hello_world_message = f'Hello World, {name}!'

    print(f'name                : { name }')
    print(f'hello_world_message : { hello_world_message }')

    return hello_world_message


if __name__ == '__main__':
    """
    Elyra Pipelines
    """

    import os
    import json

    name = os.getenv('name')

    hello_world_message = create_hello_world_message(
        name = name
    )

    output = {
        'name'                : name,
        'hello_world_message' : hello_world_message
    }

    with open('create_hello_world_message.json', 'w', encoding = 'utf-8') as output_file:

        json.dump(output, output_file, ensure_ascii = False, indent = 4)