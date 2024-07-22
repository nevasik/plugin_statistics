import os

config_file_path = os.getenv('CONFIG', 'config.txt')


def load_config(file_path):
    cfg = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip() and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    key = key.strip()
                    value = value.strip()
                    if key == 'WHITELIST':
                        value = set(map(int, value.strip('{}').split(',')))
                    cfg[key] = value
    except FileNotFoundError:
        print(f"Конфигурационный файл '{file_path}' не найден.")
    except Exception as e:
        print(f"Ошибка при чтении конфигурационного файла: {e}")
    return cfg


config = load_config(config_file_path)

TELEGRAM_BOT_TOKEN = config.get('TOKEN')
WHITELIST = config.get('WHITELIST')
DATABASE_CONFIG = {
    'dbname': config.get('POSTGRES_DB'),
    'user': config.get('POSTGRES_USER'),
    'password': config.get('POSTGRES_PASSWORD'),
    'host': config.get('POSTGRES_HOST'),
    'port': config.get('POSTGRES_PORT')
}
