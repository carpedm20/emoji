import pytest
import emoji


@pytest.mark.parametrize("input_text,expected", [
    (":pizza:", "🍕"),
    (":rocket:", "🚀"),
    (":thumbs_up:", "👍"),
    (":red_heart:", "❤️"),
    (":grinning_face:", "😀"),
])
def test_emojize_basic(input_text: str, expected: str) -> None:
    assert emoji.emojize(input_text) == expected
