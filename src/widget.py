from datetime import datetime


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


def convert_date(input_date: str) -> str:
    """
    Converts the input date string to the required format.

    Args:
        input_date (str): The input date string in the format '%Y-%m-%dT%H:%M:%S.%f'.

    Returns:
        str: The converted date string in the format '%d.%m.%Y'.
    """
    date_obj = datetime.strptime(input_date, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")
