from datetime import datetime

def test_get_current_time(freezer):
    # arrange
    freezer.move_to("2023-01-01 12:00:00")

    expected = "2023-01-01 12:00:00"

    # act
    actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # assert
    assert actual == expected
