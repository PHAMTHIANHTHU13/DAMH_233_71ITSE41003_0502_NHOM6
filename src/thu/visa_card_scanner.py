class VisaCardScanner:
    def __init__(self):
        # Khởi tạo các thông số cần thiết cho việc quét thẻ Visa
        pass

    def scan_card(self):
        # Giả định là một hàm để thực hiện quét thẻ Visa
        # Thực hiện quét thẻ và trả về thông tin chi tiết
        card_info = self._perform_card_scan()
        if card_info:
            print("Thông tin chi tiết thẻ Visa:")
            print(f"Số thẻ: {card_info['card_number']}")
            print(f"Hạn sử dụng: {card_info['expiry_date']}")
            print(f"Chủ thẻ: {card_info['card_holder_name']}")
            print(f"Loại thẻ: {card_info['card_type']}")
        else:
            print("Không thể quét thẻ Visa. Vui lòng thử lại.")

    def _perform_card_scan(self):
        # Giả định: Hàm này thực hiện quét thẻ và trả về thông tin chi tiết của thẻ
        # Thực tế, bạn cần sử dụng thư viện hoặc API thích hợp để quét thẻ Visa
        # Đoạn code dưới đây là một giả định đơn giản
        scanned_card_info = {
            'card_number': '1234 5678 9012 3456',
            'expiry_date': '12/25',
            'card_holder_name': 'John Doe',
            'card_type': 'Visa'
        }
        return scanned_card_info  # Thay thế bằng kết quả thực tế từ thư viện thực hiện quét thẻ

# Sử dụng:
if __name__ == "__main__":
    scanner = VisaCardScanner()
    scanner.scan_card()