import pytest
import requests as rq
from srvcs.chks import status, ping

#STATUS CHECKS
#Check good response
def test_check_good_response(mocker):
    print("Check good response test...")
    mock = mocker.patch("srvcs.chks.rq.get")
    mock.return_value.status_code = 200
    testurl = "https://test1.com"
    status_result = status(testurl)
    assert status_result == 200
    mock.assert_called_once_with(testurl)

#Check bad response
def test_check_bad_response(mocker):
    print("Check bad response test...")
    mock = mocker.patch("srvcs.chks.rq.get")
    mock.return_value.status_code = 404
    testurl = "https://test1.com"
    status_result = status(testurl)
    assert status_result == 404
    mock.assert_called_once_with(testurl)

#Check exception
def test_check_network_exception(mocker):
    print("Check bad input test...")
    mock = mocker.patch("srvcs.chks.rq.get")
    mock.side_effect = rq.exceptions.RequestException
    testurl = "#^#%&%&#$&$$$@^"
    status_result = status(testurl)
    assert status_result == 0
    mock.assert_called_once_with(testurl)

#PING CHECKS
#Successful ping
def test_successful_ping(mocker):
    print("Ping succeeded test...")
    mock = mocker.patch("srvcs.chks.rq.get")
    mock.return_value.elapsed.total_seconds.return_value = 0.1
    testurl = "https://test1.com"
    ping_result = ping(testurl)
    assert ping_result == 100.0 # ping is returning latency in ms
    mock.assert_called_once_with(testurl)

#Ping exception
def test_ping_network_exception(mocker):
    print("Ping bad input test...")
    mock = mocker.patch("srvcs.chks.rq.get")
    mock.side_effect = rq.exceptions.RequestException
    testurl = "#^#%&%&#$&$$$@^"
    ping_result = ping(testurl)
    assert ping_result == -1
    mock.assert_called_once_with(testurl)

#force timeout
def test_ping_timeout(mocker):
    print("Ping timout test...")
    mock = mocker.patch("srvcs.chks.rq.get")
    mock.side_effect = rq.exceptions.Timeout
    testurl = "https://test1.com"
    ping_result = ping(testurl)
    assert ping_result == -1
    mock.asset_called_once_with(testurl)

