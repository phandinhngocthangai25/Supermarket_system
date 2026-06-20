from PySide6.QtWidgets import QDialog, QPushButton, QHBoxLayout, QWidget, QMessageBox
from ui.employeeDialog import Ui_Dialog
from services.EmployeeService import EmployeeService
from models.Employee import Employee


class EmployeeDialogController(QDialog, Ui_Dialog):
    def __init__(self, employee: Employee = None, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.employee_service = EmployeeService()
        self.employee = employee 
        self.setWindowTitle("Sửa nhân viên" if employee else "Thêm nhân viên")
        self.txtEmployeeID.setReadOnly(True)

        if self.employee:
            self._fill_data(self.employee)

        self._add_action_buttons()

    def _add_action_buttons(self):
        self.btnSave = QPushButton("Lưu")
        self.btnCancel = QPushButton("Hủy")
        btn_container = QWidget(self)
        btn_layout = QHBoxLayout(btn_container)
        btn_layout.addWidget(self.btnSave)
        btn_layout.addWidget(self.btnCancel)

        next_row = self.gridLayout.rowCount()
        self.gridLayout.addWidget(btn_container, next_row, 0, 1, 3)

        self.btnSave.clicked.connect(self.handle_save)
        self.btnCancel.clicked.connect(self.reject)

    def _fill_data(self, emp: Employee):
        self.txtEmployeeID.setText(str(emp.employeeID))
        self.txtFullName.setText(emp.fullName)
        self.txtPhone.setText(emp.phone)
        self.txtEmail.setText(emp.email)
        self.txtAddress.setText(emp.address)
        self.txtSalary.setText(str(emp.salary) if emp.salary is not None else "")
        self.txtUserName.setText(emp.username)
        self.txtPassword.setText(emp.password)
        self.txtRole.setText(emp.role)

    def handle_save(self):
        full_name = self.txtFullName.text().strip()
        phone = self.txtPhone.text().strip()
        email = self.txtEmail.text().strip()
        address = self.txtAddress.text().strip()
        salary_str = self.txtSalary.text().strip()
        username = self.txtUserName.text().strip()
        password = self.txtPassword.text().strip()
        role = self.txtRole.text().strip()

        if not full_name:
            QMessageBox.warning(self, "Thiếu dữ liệu", "Vui lòng nhập tên nhân viên!")
            return
        if not username or not password:
            QMessageBox.warning(self, "Thiếu dữ liệu", "Vui lòng nhập tên đăng nhập và mật khẩu!")
            return
        try:
            salary = float(salary_str) if salary_str else 0
        except ValueError:
            QMessageBox.warning(self, "Lỗi dữ liệu", "Lương phải là số hợp lệ!")
            return

        emp = Employee(
            fullName=full_name,
            phone=phone,
            email=email,
            address=address,
            salary=salary,
            username=username,
            password=password,
            role=role
        )

        if self.employee:
            emp.employeeID = self.employee.employeeID
            self.employee_service.update_employee(emp)
            QMessageBox.information(self, "Thành công", "Đã cập nhật nhân viên!")
        else:
            self.employee_service.add_employee(emp)
            QMessageBox.information(self, "Thành công", "Đã thêm nhân viên mới!")

        self.accept()