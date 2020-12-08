import yaml
from pathlib import Path

from app.character import Wizard, Knight, Thief, Character


FILENAME = 'data.yml'
data_path = Path(FILENAME)


def load_yaml() -> dict:
    try:
        with data_path.open(mode='r', encoding='UTF-8') as f:
            data = yaml.load(f)
            return data
    except FileNotFoundError:
        print('File not found.')


def write_yaml(data) -> None:
    try:
        with data_path.open(mode='w', encoding='UTF-8') as f:
            yaml.dump(data, f)
    except FileNotFoundError:
        print('File not found. Creating..')
        with data_path.open(mode='w+', encoding='UTF-8') as f:
            yaml.dump(data, f)


def check_name_exists(key: str) -> bool:
    file_data = load_yaml()
    if key in file_data:
        return True
    return False


def load_character(name: str) -> object:
    """[loads character, creates character object]

    Args:
        name (str): [name of character]

    Returns:
        object: [character object]
    """
    try:
        loaded_yaml = load_yaml()
        if check_name_exists(name):
            result = loaded_yaml.get(name)
            result_class = result.get('class')
            if result_class == 'Knight':
                user_character = Knight(name)
                return user_character
            elif result_class == 'Wizard':
                user_character = Wizard(name)
                return user_character
            elif result_class == 'Thief':
                user_character = Thief(name)
                return user_character
    except Exception as e:
        print('Error: ' + e)


def save_data(character: Character) -> None:
    """Saves a `Character` object

    Args:
        character (Character): The `Character` object to save
    """
    if check_name_exists(character.name):
        while True:
            try:
                choice = input(
                    'User exists. Overwrite? Yes = y, No = n\n'
                    ).lower()
            except KeyboardInterrupt:
                return
            if choice == 'n':
                return
            elif choice == 'y':
                break
    data = load_yaml()
    data.update(character.export())
    write_yaml(data)


if __name__ == "__main__":
    pass
