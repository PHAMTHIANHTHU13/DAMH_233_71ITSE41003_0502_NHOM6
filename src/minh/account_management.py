class AccountManagement:
    def __init__(self):
        self.accounts = {}  # Sử dụng một từ điển để lưu trữ các tài khoản

    def add_account(self, account_number, account_info):
        # Thêm tài khoản vào danh sách quản lý
        if account_number not in self.accounts:
            self.accounts[account_number] = account_info
            print(f"Tài khoản {account_number} đã được thêm thành công.")
        else:
            print(f"Tài khoản {account_number} đã tồn tại trong hệ thống.")

    def remove_account(self, account_number):
        # Xóa tài khoản khỏi danh sách quản lý
        if account_number in self.accounts:
            del self.accounts[account_number]
            print(f"Tài khoản {account_number} đã được xóa thành công.")
        else:
            print(f"Tài khoản {account_number} không tồn tại trong hệ thống.")

    def get_account_info(self, account_number):
        # Lấy thông tin chi tiết của một tài khoản
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            print(f"Tài khoản {account_number} không tồn tại trong hệ thống.")
            return None

# Sử dụng:
if __name__ == "__main__":
    # Tạo đối tượng quản lý tài khoản
    account_manager = AccountManagement()

    # Thêm các tài khoản vào hệ thống
    account_manager.add_account('1234567890', {'owner': 'John Doe', 'balance': 1000.0})
    account_manager.add_account('0987654321', {'owner': 'Jane Smith', 'balance': 500.0})

    # Lấy thông tin chi tiết của một tài khoản
    account_number = '1234567890'
    account_info = account_manager.get_account_info(account_number)
    if account_info:
        print(f"Thông tin tài khoản {account_number}: {account_info}")

    # Xóa một tài khoản khỏi hệ thống
    account_manager.remove_account('0987654321')