import pytest
import requests as rq
from srvcs.chks import status, ping

#STATUS CHECKS
#check good response
def test_check_good_response(mocker):
    print("Good Response Test...")
    mock = mocker.patch("srvcs.chks.rq.get")
    mock.return_value.status_code = 200
    testurl = "https://test1.com"
    status_result = status(testurl)
    assert status_result == 200
    mock.assert_called_once_with(testurl)

#check error response
def test_check_bad_response(mocker):
    print("Bad Response Test...")
    mock = mocker.patch("srvcs.chks.rq.get")
    mock.return_value.status_code = 404
    testurl = "https://test2.com"
    status_result = status(testurl)
    assert status_result == 404
    mock.assert_called_once_with(testurl)

#check bad url input
def test_check_bad_input(mocker):
    print("Bad Input Test...")
    mock = mocker.patch("srvcs.chks.rq.get")
    mock.side_effect = rq.exceptions.RequestException
    testurl = "#^#%&%&#$&$$$@^"
    status_result = status(testurl)
    assert status_result == 0
    mock.assert_called_once_with(testurl)


#check empty input
def test_check_empty_input(mocker):
    print("Empty Input Test...")
    mock = mocker.patch("srvcs.chks.rq.get")
    mock.side_effect = rq.exceptions.RequestException
    testurl = ""
    status_result = status(testurl)
    assert status_result == 0
    mock.assert_called_once_with(testurl)

#PING CHECKS
#successful ping
def test_successful_ping(mocker):
    print("Bad Input Test...")
    mock = mocker.patch("srvcs.chks.rq.get")
    mock.return_value.elapsed.total_seconds.return_value = 0.1
    testurl = "https://test1.com"
    ping_result = ping(testurl)
    assert ping_result == 0.1
    mock.assert_called_once_with(testurl)

#failed ping
def test_failed_ping(mocker):
    print("Bad Input Test...")
    mock = mocker.patch("srvcs.chks.rq.get")
    mock.side_effect = rq.exceptions.RequestException
    #mock.return_value.elapsed.total_seconds.return_value = 0.1
    testurl = "https://test1.com"
    ping_result = ping(testurl)
    assert ping_result == -1
    mock.assert_called_once_with(testurl)

#bad url input
def test_ping_bad_input(mocker):
    print("Bad Input Test...")
    mock = mocker.patch("srvcs.chks.rq.get")
    mock.side_effect = rq.exceptions.RequestException
    testurl = "#^#%&%&#$&$$$@^"
    ping_result = ping(testurl)
    assert ping_result == -1
    mock.assert_called_once_with(testurl)

#empty input
def test_ping_empty_input(mocker):
    print("Bad Input Test...")
    mock = mocker.patch("srvcs.chks.rq.get")
    mock.side_effect = rq.exceptions.RequestException
    testurl = ""
    ping_result = ping(testurl)
    assert ping_result == -1
    mock.assert_called_once_with(testurl)

#force timeout

