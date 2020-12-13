import random
from random import randint
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
    text += separator
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


def dice_sum(n: int = 1, s: int = 20) -> int:
    """Throw `n`-amount of `s`-sided dices and return the sum

    Args:
        n (int): Amount of dices to throw, defautls to 1.
        s (int): How many sides each dice has, defaults to 20.
                 Dice are represented with incremental side values,
                 so this also represents the max/min value of the dice

    Returns:
        int: The sum of the dice

    Raises:
        ValueError: If `n` is less than 0
        ValueError: If `s` is 0
    """
    if not s:
        raise ValueError('Dice cannot have 0 sides!')
    if n < 0:
        raise ValueError('Cannot throw less than 0 dices!')
    if s < 0:
        return sum(randint(s - 1, -1) for _ in range(n))
    else:
        return sum(randint(1, s) for _ in range(n))


def dice(n) -> int:
    dice_sum = 0
    for x in range(n):
        b = random.randint(1, 6)

        dice_sum += b
    return dice_sum
