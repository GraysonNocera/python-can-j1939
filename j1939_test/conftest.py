import pytest

from j1939_test.feeder import Feeder

@pytest.fixture()
def feeder():
    #setup
    feeder = Feeder()
    yield feeder
    #teardown
    feeder.stop()