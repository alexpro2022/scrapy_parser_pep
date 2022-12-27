from pathlib import Path


BASE_DIR = Path(__file__).parent.parent / 'results'
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
DIALECT = 'unix'
ENCODING = 'utf-8'
EXT = 'csv'


'''
На ЯП не проходит тесты так как там Python 3.7
BASE_DIR: Final = Path(__file__).parent.parent / 'results'
DATETIME_FORMAT: Final = '%Y-%m-%d_%H-%M-%S'
DIALECT: Final = 'unix'
ENCODING: Final = 'utf-8'
EXT: Final = 'csv'
'''
