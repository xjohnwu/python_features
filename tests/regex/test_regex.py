import re


def test_search_string_in_between():
    s = 'Too many requests; current limit of IP(54.150.96.215) is 2400 requests per minute. Please use the websocket for live updates to avoid polling the API.'
    result = re.search('current limit of IP\((.*)\)', s)
    assert result.group(1) == '54.150.96.215'


def test_search_string_two():
    s = 'Way too much request weight used; IP banned until 1651221451934. Please use the websocket for live updates to avoid bans.'
    result = re.search('IP banned until (\d+)\.', s)
    assert result.group(1) == '1651221451934'
