from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QDialog, QTableWidget, QCompleter
from PySide6.QtCore import Qt
from ui.employeeManager import Ui_employee
from services.EmployeeService import EmployeeService
from controllers.EmployeeDialogController import EmployeeDialogController


class EmployeeManagerController(QWidget, Ui_employee):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.employee_service = EmployeeService()
        self.selected_employee_id = None

        # Bảng đã có 9 cột theo UI, ta giữ nguyên
        self.tableEmployee.setColumnCount(9)
        self.tableEmployee.setHorizontalHeaderLabels([
            "Mã NV", "Họ tên", "Tên đăng nhập", "Mật khẩu",
            "SĐT", "Email", "Địa chỉ", "Lương", "Vai trò"
        ])
        self.tableEmployee.horizontalHeader().setStretchLastSection(True)
        self.tableEmployee.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableEmployee.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableEmployee.setSelectionMode(QTableWidget.SingleSelection)

        self.load_data()
        self.setup_completer()
        self._setup_connections()

    def setup_completer(self):
        employees = self.employee_service.get_all_employees()
        names = [e.fullName for e in employees if e.fullName.strip()]
        completer = QCompleter(names, self.txtSearchEmployee)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setFilterMode(Qt.MatchContains)
        self.txtSearchEmployee.setCompleter(completer)

    def _setup_connections(self):
        self.btnSearchEmployee.clicked.connect(self.handle_search)
        self.txtSearchEmployee.returnPressed.connect(self.handle_search)
        self.btnAddEmployee.clicked.connect(self.handle_add)
        self.btnEditEmployee.clicked.connect(self.handle_edit)
        self.tableEmployee.itemSelectionChanged.connect(self.handle_row_selected)

    def handle_row_selected(self):
        row = self.tableEmployee.currentRow()
        if row < 0:
            self.selected_employee_id = None
            return
        id_item = self.tableEmployee.item(row, 0)
        self.selected_employee_id = id_item.text() if id_item else None

    def load_data(self, employees=None):
        if employees is None:
            employees = self.employee_service.get_all_employees()

        self.tableEmployee.setRowCount(len(employees))
        for row, emp in enumerate(employees):
            self.tableEmployee.setItem(row, 0, QTableWidgetItem(str(emp.employeeID)))
            self.tableEmployee.setItem(row, 1, QTableWidgetItem(emp.fullName))
            self.tableEmployee.setItem(row, 2, QTableWidgetItem(emp.username))
            self.tableEmployee.setItem(row, 3, QTableWidgetItem(emp.password))  # có thể ẩn nếu muốn
            self.tableEmployee.setItem(row, 4, QTableWidgetItem(emp.phone))
            self.tableEmployee.setItem(row, 5, QTableWidgetItem(emp.email))
            self.tableEmployee.setItem(row, 6, QTableWidgetItem(emp.address))
            self.tableEmployee.setItem(row, 7, QTableWidgetItem(str(emp.salary) if emp.salary is not None else ""))
            self.tableEmployee.setItem(row, 8, QTableWidgetItem(emp.role))

        self.selected_employee_id = None

    def handle_search(self):
        keyword = self.txtSearchEmployee.text().strip()
        employees = self.employee_service.search_employees(keyword)
        self.load_data(employees)

    def handle_add(self):
        dialog = EmployeeDialogController(employee=None, parent=self)
        if dialog.exec() == QDialog.Accepted:
            self.load_data()
            self.setup_completer()

    def handle_edit(self):
        if not self.selected_employee_id:
            QMessageBox.warning(self, "Chưa chọn", "Vui lòng chọn một nhân viên để sửa.")
            return
        emp = self.employee_service.get_employee_by_id(self.selected_employee_id)
        if not emp:
            QMessageBox.warning(self, "Lỗi", "Không tìm thấy nhân viên.")
            return
        dialog = EmployeeDialogController(employee=emp, parent=self)
        if dialog.exec() == QDialog.Accepted:
            self.load_data()
            self.setup_completer()

    