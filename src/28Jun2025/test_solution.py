from solution import Solution


def test_max_area():
    assert Solution().max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert Solution().max_area([1, 1]) == 1
