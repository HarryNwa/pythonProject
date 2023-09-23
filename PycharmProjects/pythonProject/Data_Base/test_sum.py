from Data_Base.Sum import sum_list, list1


def test_summation():
    assert sum_list(list1, 12) == [0, 2]
    assert sum_list(list1, 16) == [2, 3]
    assert sum_list(list1, 15) is None

