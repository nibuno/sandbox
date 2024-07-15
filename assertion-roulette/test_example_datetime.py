from datetime import datetime

def test_is_assertion_roulette(freezer):
    """アサーションルーレットのテストケース"""

    # arrange
    freezer.move_to("2023-01-01 12:00:00")

    expected_year = 2024  # 期待値が2024で失敗する
    expected_month = 1
    expected_day = 1
    expected_hour = 11  # 期待値が11で失敗するが、expected_yearが失敗しているため、この行は実行されない
    expected_minute = 0

    # act
    actual = datetime.now()

    actual_year = actual.year
    actual_month = actual.month
    actual_day = actual.day
    actual_hour = actual.hour
    actual_minute = actual.minute

    # assert
    assert expected_year == actual_year
    assert expected_month == actual_month
    assert expected_day == actual_day
    assert expected_hour == actual_hour
    assert expected_minute == actual_minute


def test_is_not_assertion_roulette(freezer):
    """アサーションルーレットではないテストケース"""

    # arrange
    freezer.move_to("2023-01-01 12:00:00")

    expected_year = 2024
    expected_month = 1
    expected_day = 1
    expected_hour = 11
    expected_minute = 0

    expected_tuple = (expected_year, expected_month, expected_day, expected_hour, expected_minute)

    # act
    actual = datetime.now()

    actual_year = actual.year
    actual_month = actual.month
    actual_day = actual.day
    actual_hour = actual.hour
    actual_minute = actual.minute

    actual_tuple = (actual_year, actual_month, actual_day, actual_hour, actual_minute)

    # assert
    assert expected_tuple == actual_tuple
