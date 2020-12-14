from pathlib import Path
from typing import Union

import yaml

from app.character import Wizard, Knight, Thief, Character
from app.helpers import user_choice


FILENAME = 'savedata.yml'
data_path = Path(FILENAME)


def load_yaml() -> dict:
    try:
        if not data_path.exists():
            data_path.touch()
        with data_path.open(mode='r', encoding='UTF-8') as f:
            data = yaml.safe_load(f)
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

    char_data = data.get(name, None)
    if char_data is None:
        print(f'No character with the name {name} exist!')
        return None

    _class = char_data.get('class', None)
    _treasure = char_data.get('treasure', None)
    if _class is None:
        print('The character doesn\'t have a class!')
    else:
        if _class == 'Knight':
            character = Knight(name, _treasure)
        elif _class == 'Wizard':
            character = Wizard(name, _treasure)
        elif _class == 'Thief':
            character = Thief(name, _treasure)
        else:
            print('The character is not a valid class!')
            return None
        return character
    return None


def save_character(character: Character) -> None:
    """Saves a `Character` object

    Args:
        character (Character): The `Character` object to save
    """
    data = load_yaml()
    try:
        if character.name in data.keys():
            choices = [
                ('1', 'Yes'),
                ('2', 'No')
            ]
            header = f'There is already a saved character with the name {character.name}. Do you want to Overwrite?'
            choice = user_choice(choices, above=header, exception='2')
            if choice == '2':
                return
        data.update(character.export())
        write_yaml(data)

    except AttributeError:
        write_yaml(character.export())



if __name__ == "__main__":
    pass
