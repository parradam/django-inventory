import pytest
from django.conf import settings


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass


# @pytest.fixture(scope="session", autouse=True)
# def print_database_info():
#     """
#     Fixture to print the current database information before running tests.
#     """
#     print(f"Using database: {settings.DATABASES['default']}")


# @pytest.fixture(scope="session")
# def django_db_setup():
#     settings.DATABASES["test"]
