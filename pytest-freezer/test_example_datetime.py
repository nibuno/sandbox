from datetime import datetime

def test_get_current_time(freezer):
    # arrange
    freezer.move_to("2023-01-01 12:00:00")

    expected = "2023-01-01 12:00:00"

    # act
    actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # assert
    assert actual == expected

def test_fail_get_current_time(freezer):
    # arrange
    freezer.move_to("2023-01-01 12:00:00")

    expected = datetime(year=2024, month=1, day=1, hour=12, minute=0)

    # act
    actual = datetime.now()

    # assert
    # AssertionError: assert FakeDatetime(2023, 1, 1, 12, 0) == FakeDatetime(2024, 1, 1, 12, 0) となる
    assert actual == expected
