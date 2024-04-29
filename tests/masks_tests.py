from src.masks import mask_bank_account, mask_credit_card

credit_card_number = "7000792289606361"
masked_credit_card = mask_credit_card(credit_card_number)
print(masked_credit_card)

bank_account_number = "73654108430135874305"
masked_bank_account = mask_bank_account(bank_account_number)
print(masked_bank_account)
