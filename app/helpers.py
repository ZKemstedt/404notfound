from typing import List, Tuple, Optional


def user_choice(
    menu_items: List[Tuple[str, str]],
    *,
    above: Optional[str] = '\n',
    below: Optional[str] = '',
    separator: Optional[str] = '\n',
    prompt: Optional[str] = '> ',
    invalid: Optional[str] = None,
    exception: Optional[str] = None,
    error_string: Optional[str] = 'Invalid choice'
) -> str:
    """Prompts the user to choose an option from a menu and return the corresponding key.

    Args:
        menu_items (list): a list of tuples representing the menu items: (key, description)
                    where key is the expected value the user will enter as well as the value to return.
                    And description is the description of said choice

        above (str): optional, string to print above the list of menu options. Defaults to a linebreak
        below (str): optional, string to print below the list of menu options. Defaults to a linebreak
        separator (str): optional, string used to separate the menu options. Defaults to a linebreak
        prompt (str): optional, the string used when prompting the user for input. Defaults to `> `
        invalid (str): optionl, if set; return said value when the user enters an invalid choice.
        exception (str): optional, if set; return said value when the user raises `KeyboardInterrupt`.
        error_string (str): optional, string to print when the user enters an invalid choice.

    Returns:
        choice (str): one of the specified correct choices
        invalid (str): if provided as argument and user enters an invalid choice
        exception (str): if provided as argument and users raises `KeyboardInterrupt`
    """
    choices = []
    text = above
    text += '\n'
    for key, description in menu_items:
        text += f'[ {key} ]  {description}'
        text += separator
        choices.append(key)
    text += below

    print(text)
    while True:
        try:
            choice = input(prompt)
            if choice in choices:
                return choice
            elif invalid:
                return invalid
            elif error_string:
                print(error_string)

        except KeyboardInterrupt:
            if exception:
                return exception
            elif error_string:
                print(error_string)
