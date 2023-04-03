import pytest
def f(n):
    list1=[]
    for i in range(1,n):
        if n%i==0:
            list1.append(i)
    return list1
@pytest.mark.parametrize("n,expected_output" ,[(6,[1,2,3]),(4,[1,2]),(12,[1,2,3,4,6])])
def test_f(n, expected_output):
    assert f(n)==expected_output