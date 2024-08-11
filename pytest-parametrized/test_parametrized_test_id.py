# from grade import grade
#
# import pytest
#
# @pytest.mark.parametrize('scode,expected', [
#     (50, '可'),
#     (70, '良'),
#     (90, '優'),
# ])
# def test_grade(scode, expected):
#     assert grade(scode) == expected

# (venv) tatsuya: pytest-parametrized/ % pytest -v                                                                                      (git)-[main]
# =============================================================== test session starts ===============================================================
# platform darwin -- Python 3.12.1, pytest-8.2.2, pluggy-1.5.0 -- /Users/tatsuya/sandbox/pytest-freezer/venv/bin/python3.12
# cachedir: .pytest_cache
# rootdir: /Users/tatsuya/sandbox/pytest-parametrized
# configfile: pytest.ini
# plugins: pytest_freezer-0.4.8
# collected 3 items
#
# test_parametrized_test_id.py::test_grade[50-\u53ef] PASSED                                                                                  [ 33%]
# test_parametrized_test_id.py::test_grade[70-\u826f] PASSED                                                                                  [ 66%]
# test_parametrized_test_id.py::test_grade[90-\u512a] PASSED                                                                                  [100%]
#
# ================================================================ 3 passed in 0.01s ================================================================

from grade import grade

import pytest

@pytest.mark.parametrize('score,expected', [
    pytest.param(50, "不可", id="param-50-Poor", marks=pytest.mark.basic),  # marksを付与すると is this a typo? とWarningが出る
    pytest.param(59, "不可", id="param-59-Poor"),
    pytest.param(60, "可", id="param-60-Average"),
    pytest.param(69, "可", id="param-69-Average"),
    pytest.param(70, "良", id="param-70-Good"),
    pytest.param(79, "良", id="param-79-Good"),
    pytest.param(80, "優", id="param-80-Excellent"),
    pytest.param(100, "優", id="param-100-Excellent"),
])
def test_grade(score, expected):
    assert grade(score) == expected

# (venv) tatsuya: pytest-parametrized/ % pytest -v                                                                                      (git)-[main]
# =============================================================== test session starts ===============================================================
# platform darwin -- Python 3.12.1, pytest-8.2.2, pluggy-1.5.0 -- /Users/tatsuya/sandbox/pytest-freezer/venv/bin/python3.12
# cachedir: .pytest_cache
# rootdir: /Users/tatsuya/sandbox/pytest-parametrized
# configfile: pytest.ini
# plugins: pytest_freezer-0.4.8
# collected 8 items
#
# test_parametrized_test_id.py::test_grade[param-50-Poor] PASSED                                                                              [ 12%]
# test_parametrized_test_id.py::test_grade[param-59-Poor] PASSED                                                                              [ 25%]
# test_parametrized_test_id.py::test_grade[param-60-Average] PASSED                                                                           [ 37%]
# test_parametrized_test_id.py::test_grade[param-69-Average] PASSED                                                                           [ 50%]
# test_parametrized_test_id.py::test_grade[param-70-Good] PASSED                                                                              [ 62%]
# test_parametrized_test_id.py::test_grade[param-79-Good] PASSED                                                                              [ 75%]
# test_parametrized_test_id.py::test_grade[param-80-Excellent] PASSED                                                                         [ 87%]
# test_parametrized_test_id.py::test_grade[param-100-Excellent] PASSED                                                                        [100%]
#
# ================================================================ 8 passed in 0.02s ================================================================
