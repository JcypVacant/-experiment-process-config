import os
from PySide6.QtWidgets import QDialog, QMessageBox
from ui.totaltable import Ui_TotalTable
from utils.data_utils import get_config
from tkinter import Tk, filedialog

class TotalTableDlg(QDialog, Ui_TotalTable):
    def __init__(self):
        super(TotalTableDlg, self).__init__()
        self.setupUi(self)
        # 静态表长度
        self.static_length = ""
        # 读取配置
        furnace_config = get_config('E')
        # ------------电机选择--------------
        self.motor1_val = furnace_config["motor_select"]["motor_1"]
        self.motor2_val = furnace_config["motor_select"]["motor_2"]
        self.motor3_val = furnace_config["motor_select"]["motor_3"]
        self.motor4_val = furnace_config["motor_select"]["motor_4"]
        self.motor5_val = furnace_config["motor_select"]["motor_5"]
        # 获取配置参数的16进制编码
        self.motor_selection_hex = self.get_motor_selection_hex()
        # 电机复选框状态改变
        self.motor_1.stateChanged.connect(self.motor1_state_changed)
        self.motor_2.stateChanged.connect(self.motor2_state_changed)
        self.motor_3.stateChanged.connect(self.motor3_state_changed)
        self.motor_4.stateChanged.connect(self.motor4_state_changed)
        self.motor_5.stateChanged.connect(self.motor5_state_changed)
        # 更新界面所展示的值
        self.update_hex_val()
        # 获取静态表.bin文件和静态表长度
        self.totalStatic_pushButton.clicked.connect(self.get_static_length)

    def update_hex_val(self):
        """
        将十六进制值在界面上更新
        :return:
        """
        # 电机选择
        self.motorHex_lineEdit.setText(self.motor_selection_hex[2:] + self.motor_selection_hex[0:2])

    def motor1_state_changed(self, state):
        if state == 2:
            self.motor1_val = "11"
        else:
            self.motor1_val = "00"
        # 获取配置参数的16进制编码
        self.motor_selection_hex = self.get_motor_selection_hex()
        # 更新界面所展示的值
        self.update_hex_val()

    def motor2_state_changed(self, state):
        if state == 2:
            self.motor2_val = "11"
        else:
            self.motor2_val = "00"
        # 获取配置参数的16进制编码
        self.motor_selection_hex = self.get_motor_selection_hex()
        # 更新界面所展示的值
        self.update_hex_val()

    def motor3_state_changed(self, state):
        if state == 2:
            self.motor3_val = "11"
        else:
            self.motor3_val = "00"
        # 获取配置参数的16进制编码
        self.motor_selection_hex = self.get_motor_selection_hex()
        # 更新界面所展示的值
        self.update_hex_val()

    def motor4_state_changed(self, state):
        if state == 2:
            self.motor4_val = "11"
        else:
            self.motor4_val = "00"
        # 获取配置参数的16进制编码
        self.motor_selection_hex = self.get_motor_selection_hex()
        # 更新界面所展示的值
        self.update_hex_val()

    def motor5_state_changed(self, state):
        if state == 2:
            self.motor5_val = "11"
        else:
            self.motor5_val = "00"
        # 获取配置参数的16进制编码
        self.motor_selection_hex = self.get_motor_selection_hex()
        # 更新界面所展示的值
        self.update_hex_val()

    def get_motor_selection_hex(self):
        """
        返回电机配置值对应的十六进制
        :return:
        """
        val = self.motor5_val + self.motor4_val + self.motor3_val + self.motor2_val + self.motor1_val
        binary_str = "1100" + val + "00"
        # 提取前8个字符和后8个字符
        part1 = binary_str[:8]
        part2 = binary_str[8:]
        # 转换为十六进制，并确保每个部分是两个字符
        hex1 = format(int(part1, 2), '02X')
        hex2 = format(int(part2, 2), '02X')
        return hex1 + hex2
    def get_static_length(self):
        """读取文件夹下的以 ST 开头且文件名包含 '静态表' 的 .bin 文件，并计算字节数和内容"""
        # 打开文件夹选择对话框
        Tk().withdraw()  # 隐藏主窗口
        folder_selected = filedialog.askdirectory()

        if not folder_selected:
            print("未选择任何文件")
            return

        # 筛选符合条件的文件
        bin_files = [f for f in os.listdir(folder_selected) if
                     f.startswith('ST') and '静态表' in f and f.endswith('.bin')]

        for bin_file in bin_files:
            file_path = os.path.join(folder_selected, bin_file)
            with open(file_path, 'rb') as file:
                file_content = file.read()
                file_length = len(file_content)
                file_length_str = str(file_length)  # 将文件字节数转换为字符串
                file_content_hex = file_content.hex().upper()  # 转换为十六进制字符串

                print(f"文件: {bin_file}")
        static_hex_string = self.calculate_hex_string()
        self.static_length = file_length_str
        self.staticTable_lineEdit.setText(self.static_length)
        self.lineEdit_7.setText(static_hex_string)
        print(f"字节数: {file_length}")
        print(f"内容字符串: {file_content_hex}")

    def calculate_hex_string(self):
        # 基础值
        base_value = 2181038080

        # 计算总和
        total_value = base_value + 0

        # 转换为十六进制（8位，不足位数前补0）
        hex_value = format(total_value, '08X')

        # 提取部分
        part1 = hex_value[6:8]  # 第 7 和第 8 位
        part2 = hex_value[4:6]  # 第 5 和第 6 位
        part3 = hex_value[2:4]  # 第 3 和第 4 位
        part4 = hex_value[0:2]  # 第 1 和第 2 位

        # 拼接结果
        result = (part1 + part2 + part3 + part4) * 3  # 重复三次
        return result
