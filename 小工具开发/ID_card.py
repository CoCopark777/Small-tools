
import random

def generate_id_card():
    area_code = str(random.randint(100000, 999999))
    birth_year = str(random.randint(1950, 2023))
    birth_month = str(random.randint(1, 12)).zfill(2)
    birth_day = str(random.randint(1, 28)).zfill(2)
    birth_date = birth_year + birth_month + birth_day
    sequence_code = str(random.randint(100, 999))
    id_card_number = area_code + birth_date + sequence_code
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    check_sum = 0
    for i in range(17):
        check_sum += int(id_card_number[i]) * weight[i]
    remainder = check_sum % 11
    check_code_mapping = "10X98765432"
    check_code = check_code_mapping[remainder]
    id_card_number += check_code
    return id_card_number

print(generate_id_card())