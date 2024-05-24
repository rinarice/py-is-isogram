from app.main import is_isogram
import pytest
#  "Not only non-consecutive letters are not an isogram."
# "Not only consecutive letters are not an isogram."
# "Empty string is an isogram."
# "String with different cases of the same letter is not an isogram."


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("aba", False),
        ("a", True),
        ("happy", False),
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
