import datetime
from unittest.mock import patch, Mock

import pytest

from flight_status_redis import FlightStatusTracker


@pytest.fixture
def tracker():
    return FlightStatusTracker()


def test_patch(tracker):
    tracker.redis.set = Mock()
    fake_now = datetime.datetime(2015, 4, 1)
    with patch("datetime.datetime") as dt:
        dt.now.return_value = fake_now
        tracker.change_status("AC102", "on time")
    dt.now.assert_called_once_with()
    tracker.redis.set.assert_called_once_with(
        "flightno:AC102", "2015-04-01T00:00:00|ON TIME"
    )

# pytest test_pytest_patch.py -s


# pip install coverage
# coverage run test_pytest_patch.py
# coverage report
# coverage report -m
# coverage html

