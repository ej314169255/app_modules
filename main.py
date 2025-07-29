from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees


from python_accounting import config

"""
This module provides the configuration for python accounting. Its properties are populated from 
`config.toml <https://github.com/ekmungai/python-accounting/blob/main/config.toml>`__ by default and 
should be adequate for most settings, but there are a few methods for overriding the database, 
hashing and dates configurations. For more extensive custom configurations, you can initialize 
the class with a custom config.tml file.

"""

if __name__ == '__main__':
    print(calculate_salary())
    print(get_employees())
    print(f"{datetime.now()}")
    print(config)