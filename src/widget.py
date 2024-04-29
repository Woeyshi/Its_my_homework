def mask_card_or_account_number(input_string: str) -> str:
    """
    Masks the card or account number in the given input string.

    Args:
        input_string (str): The input string containing the card or account number.

    Returns:
        str: The masked card or account number.
    """
    if "Счет" in input_string:
        masked_number = input_string.replace("Счет ", "Счет **").split()[1][-4:]
    else:
        card_details = input_string.split()
        masked_number = (
            card_details[0] + " " + card_details[1] + " " + card_details[2][:2] + "** **** " + card_details[4]
        )

    return masked_number
