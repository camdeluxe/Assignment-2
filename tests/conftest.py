import os
import pytest
import csv

from flix.adapters import memory_repository
from flix.adapters.memory_repository import MemoryRepository

TEST_DATA_PATH = os.path.join('C:', os.sep, 'Users', 'camer', 'Desktop', 'A place to save stuff', 'Compsci235', 'Assignment-2',
                              'tests', 'data')

@pytest.fixture
def in_memory_repo():
    repo = MemoryRepository()
    memory_repository.populate(TEST_DATA_PATH, repo)
    return repo