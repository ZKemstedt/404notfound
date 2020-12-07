import yaml
from pathlib import Path
from app.character import Wizard, Knight, Thief, Character


FILENAME = 'data.yml'
data_path = Path(FILENAME)


def export_character_info(character: Character) -> dict:
    user_class = character.__class__.__name__
    character_info = {}
    name = getattr(character, 'name')
    health = getattr(character, 'health')
    #  treasure = getattr(character, 'treasure') NOT YET
    character_info[name] = {'class': user_class, 'health': health}
    return character_info


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


def save_data(character: Character, character_info: dict) -> None:
    """[summary]

    Args:
        character (Character): [current character object]
        character_info (dict): [exported character_info]
    """
    loaded_yaml = load_yaml()
    if check_name_exists(character.name):
        answer_yes = ['y']
        answer_no = ['n']
        error = ('You can only enter y or n')
        while True:
            try:
                choice = input(
                    'User exists. Overwrite? Yes = y, No = n\n'
                    )
            except ValueError:
                print(error)

            if choice.lower() in answer_yes:
                loaded_yaml.update(character_info)
                write_yaml(loaded_yaml)
                break
            elif choice.lower() in answer_no:
                break
    else:
        loaded_yaml.update(character_info)
        write_yaml(loaded_yaml)
