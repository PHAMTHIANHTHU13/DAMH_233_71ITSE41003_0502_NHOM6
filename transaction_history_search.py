class TransactionHistorySearch:
    def __init__(self, card_number):
        self.card_number = card_number

    def search_transactions(self, start_date, end_date):
        # Giả định: Hàm này thực hiện tìm kiếm lịch sử giao dịch của thẻ Visa
        # từ ngày start_date đến end_date và trả về kết quả
        # Trong thực tế, bạn cần thay thế hàm này bằng logic tìm kiếm thực tế
        transactions = [
            {"date": "2023-01-01", "amount": 100.0},
            {"date": "2023-01-05", "amount": 50.0},
            {"date": "2023-01-10", "amount": 200.0}
        ]

        # Lọc các giao dịch trong khoảng thời gian cho trước
        filtered_transactions = [
            transaction for transaction in transactions
            if start_date <= transaction["date"] <= end_date
        ]

        return filtered_transactions

# Sử dụng:
if __name__ == "__main__":
    # Giả định số thẻ Visa cần tìm kiếm lịch sử giao dịch
    card_number = '1234 5678 9012 3456'

    # Tạo đối tượng TransactionHistorySearch và tìm kiếm lịch sử giao dịch
    transaction_search = TransactionHistorySearch(card_number)
    start_date = "2023-01-01"
    end_date = "2023-01-31"
    transactions = transaction_search.search_transactions(start_date, end_date)

    # Hiển thị kết quả
    if transactions:
        print(f"Lịch sử giao dịch của thẻ Visa {card_number} từ {start_date} đến {end_date}:")
        for transaction in transactions:
            print(f"Ngày: {transaction['date']}, Số tiền: {transaction['amount']}")
    else:
        print(f"Không tìm thấy giao dịch nào cho thẻ Visa {card_number} trong khoảng thời gian từ {start_date} đến {end_date}.")