from pathlib import Path
from typing import Union

import yaml

from app.character import Wizard, Knight, Thief, Character
from app.helpers import user_choice


FILENAME = 'savedata.yml'
data_path = Path(FILENAME)


def load_yaml() -> dict:
    try:
        with data_path.open(mode='r', encoding='UTF-8') as f:
            data = yaml.load(f)
            return data
    except FileNotFoundError:
        print('File not found.')
        raise  # NOTE


def write_yaml(data) -> None:
    try:
        with data_path.open(mode='w', encoding='UTF-8') as f:
            yaml.dump(data, f)
    except FileNotFoundError:
        print('File not found. Creating..')
        with data_path.open(mode='w+', encoding='UTF-8') as f:
            yaml.dump(data, f)


def load_character(name: str) -> Union[Character, None]:
    """Loads a previously saved character object.

    Args:
        name (str): Name of the character to load

    Returns:
        Character: The loaded Character
        None: A Character with `name` couldn not be found.
    """
    try:
        data = load_yaml()
    except Exception as e:
        print(f'An error occured when trying to load data!\n {type(e)}: {e}')
        return None

    _name = data.get(name, default=None)
    _class = data.get('class', default=None)
    if _name is None:
        print(f'No character with the name {name} exist!')
    elif _class is None:
        print('The class of the character is invalid!')
    else:
        if _class == 'Knight':
            character = Knight(_name)
        elif _class == 'Wizard':
            character = Wizard(name)
        elif _class == 'Thief':
            character = Thief(name)
        return character
    return None


def save_data(character: Character) -> None:
    """Saves a `Character` object

    Args:
        character (Character): The `Character` object to save
    """
    data = load_yaml()
    if character.name in data.keys():
        choices = [
            ('y', 'Yes'),
            ('n', 'No')
        ]
        header = f'There is already a saved character with the name {character.name}. Do you want to Overwrite?'
        choice = user_choice(choices, above=header, exception='n')
        if choice == 'n':
            return
    data.update(character.export())
    write_yaml(data)


if __name__ == "__main__":
    pass
