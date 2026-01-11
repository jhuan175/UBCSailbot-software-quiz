from standard_calc import bound_to_180, is_angle_between


""" Tests for bound_to_180() """


def test_bound_basic1():
    assert bound_to_180(0) == 0
    assert bound_to_180(135) == 135
    assert bound_to_180(200) == -160
    assert bound_to_180(180) == -180
    assert bound_to_180(360) == 0
    assert bound_to_180(-390) == -30
    assert bound_to_180(800) == 80
    assert bound_to_180(196.4) == -163.6


""" Tests for is_angle_between() """


def test_between_basic1():
    assert is_angle_between(0, 1, 2)
    assert is_angle_between(0, 45, 90)
    assert not is_angle_between(45, 90, 270)
    assert not is_angle_between(135, 90, 270)
    assert is_angle_between(270.001, 200.97, 135.64)
    assert is_angle_between(800, -193, 1261)
