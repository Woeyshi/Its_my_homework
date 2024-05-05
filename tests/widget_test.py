from src.widget import converted_date, masked_cards


def test_masked_cards() -> None:
    assert masked_cards("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"
    assert masked_cards("Счет 73654108430135874305") == "Счет **4305"


def test_converted_date() -> None:
    assert converted_date("2018-07-11T02:26:18.671407") == "11.07.2018"
