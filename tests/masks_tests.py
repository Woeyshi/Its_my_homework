import pytest

from src.masks import mask_bank_account, mask_credit_card


@pytest.fixture
def number() -> str:
    return "1234567890"


def pytest_mask_bank_account(number: str) -> None:
    assert mask_bank_account(number) == "**7890"


@pytest.mark.parametrize(
    "number_card, mask_number_card",
    [("0987654334567890", "0987 65** **** 7890"), ("0000111122223333", "0000 11** **** 3333")],
)
def pytest_masked_card(number_card: str, mask_number_card: str) -> None:
    assert mask_credit_card(number_card) == mask_number_card


credit_card_number = "7000792289606361"
masked_credit_card = mask_credit_card(credit_card_number)
print(masked_credit_card)

bank_account_number = "73654108430135874305"
masked_bank_account = mask_bank_account(bank_account_number)
print(masked_bank_account)
