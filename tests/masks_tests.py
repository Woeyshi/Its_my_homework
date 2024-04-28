from src.masks import mask_account_number, mask_card_number

card_number = "7000792289606361"
masked_card_number = mask_card_number(card_number)
print(masked_card_number)

account_number = "73654108430135874305"
masked_account_number = mask_account_number(account_number)
print(masked_account_number)
