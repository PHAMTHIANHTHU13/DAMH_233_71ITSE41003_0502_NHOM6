# Tính tổng các số chẵn từ 1 đến 100

def sum_even_numbers(limit):
    total = 0
    for num in range(2, limit + 1, 2):
        total += num
    return total

# Giới hạn là 100
limit = 100
sum_even = sum_even_numbers(limit)
print(f"Tổng các số chẵn từ 1 đến {limit} là: {sum_even}")
