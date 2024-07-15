class VisaCardStorage:
    def __init__(self, card_info):
        self.card_info = card_info

    def save_to_file(self, filename):
        try:
            with open(filename, 'w') as file:
                file.write("Thông tin chi tiết thẻ Visa:\n")
                file.write(f"Số thẻ: {self.card_info['card_number']}\n")
                file.write(f"Hạn sử dụng: {self.card_info['expiry_date']}\n")
                file.write(f"Chủ thẻ: {self.card_info['card_holder_name']}\n")
                file.write(f"Loại thẻ: {self.card_info['card_type']}\n")
            print(f"Đã lưu thông tin thẻ vào file {filename} thành công.")
        except IOError:
            print(f"Lỗi: Không thể ghi vào file {filename}.")

# Sử dụng:
if __name__ == "__main__":
    # Giả định là đã có dữ liệu thẻ Visa từ chức năng quét
    scanned_card_info = {
        'card_number': '1234 5678 9012 3456',
        'expiry_date': '12/25',
        'card_holder_name': 'John Doe',
        'card_type': 'Visa'
    }

    # Tạo đối tượng VisaCardStorage và lưu thông tin thẻ vào file
    card_storage = VisaCardStorage(scanned_card_info)
    card_storage.save_to_file('visa_card_info.txt')