def mask_credit_card(card_number: str) -> str:
    """
    Маскирует указанный номер кредитной карты.

    Args:
        card_number (str): Номер кредитной карты, который должен быть замаскирован.

    Returns:
        str: Замаскированный номер кредитной карты в формате XXXX XX** **** XXXX.
    """
    masked_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    return masked_number


def mask_bank_account(account_number: str) -> str:
    """
    Маскирует указанный номер банковского счета.

    Args:
        account_number (str): Номер банковского счета, который должен быть замаскирован.

    Returns:
        str: Замаскированный номер банковского счета в формате **XXXX.
    """
    masked_account = "**" + account_number[-4:]
    return masked_account
