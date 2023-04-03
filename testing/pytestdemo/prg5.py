import pytest
def countstring1(string1):
    count=0
    a=list(string1)
    for i in a:
        count=count+1
    return count
@pytest.mark.parametrize("string1,expected_output",[('neelima',7),('neel',4)])
def test_countstring1(string1,expected_output):
    assert countstring1(string1)==expected_output