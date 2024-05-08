import pytest

from src.masks import mask_bank_account, mask_credit_card


@pytest.fixture
def number() -> str:
    return "9871236540"


def test_mask_bank_account(number: str) -> None:
    assert mask_bank_account(number) == "**6540"


@pytest.mark.parametrize(
    "number_card, mask_number_card",
    [("4444555566667777", "4444 55** **** 7777"), ("0000111122223333", "0000 11** **** 3333")],
)
def test_masked_card(number_card: str, mask_number_card: str) -> None:
    assert mask_credit_card(number_card) == mask_number_card
