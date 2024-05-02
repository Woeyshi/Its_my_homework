from src.widget import convert_date, mask_bank_account, mask_credit_card

credit_card_number = "1596837868705199"
masked_credit_card = mask_credit_card(credit_card_number)
print(masked_credit_card)

bank_account_number = "64686473678894779589"
masked_bank_account = mask_bank_account(bank_account_number)
print(masked_bank_account)

credit_card_number = "7158300734726758"
masked_credit_card = mask_credit_card(credit_card_number)
print(masked_credit_card)

bank_account_number = "35383033474447895560"
masked_bank_account = mask_bank_account(bank_account_number)
print(masked_bank_account)

credit_card_number = "6831982476737658"
masked_credit_card = mask_credit_card(credit_card_number)
print(masked_credit_card)

bank_account_number = "8990922113665229"
masked_bank_account = mask_bank_account(bank_account_number)
print(masked_bank_account)

credit_card_number = "5999414228426353"
masked_credit_card = mask_credit_card(credit_card_number)
print(masked_credit_card)

bank_account_number = "73654108430135874305"
masked_bank_account = mask_bank_account(bank_account_number)
print(masked_bank_account)

print(convert_date("2018-07-11T02:26:18.671407"))
