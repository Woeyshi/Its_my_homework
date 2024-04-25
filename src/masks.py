def mask_credit_card(card_number):
    masked_number = (card_number[:4] + ' ' + card_number[4:6] +
                     '** **' + ' ' + card_number[-4:])
    return masked_number


def mask_bank_account(account_number):
    masked_number = '**' + account_number[-4:]
    return masked_number
