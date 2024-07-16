class VisaCardInfoDisplay:
    def __init__(self, card_info):
        self.card_info = card_info

    def display_card_info(self):
        print("Thông tin chi tiết thẻ Visa:")
        print(f"Số thẻ: {self.card_info['card_number']}")
        print(f"Hạn sử dụng: {self.card_info['expiry_date']}")
        print(f"Chủ thẻ: {self.card_info['card_holder_name']}")
        print(f"Loại thẻ: {self.card_info['card_type']}")

# Sử dụng:
if __name__ == "__main__":
    # Giả định là đã có dữ liệu thẻ Visa từ chức năng quét
    scanned_card_info = {
        'card_number': '1234 5678 9012 3456',
        'expiry_date': '12/25',
        'card_holder_name': 'John Doe',
        'card_type': 'Visa'
    }

    # Tạo đối tượng VisaCardInfoDisplay và hiển thị thông tin thẻ
    card_info_display = VisaCardInfoDisplay(scanned_card_info)
    card_info_display.display_card_info()