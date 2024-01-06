from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog

from ui.MotorClosing import Ui_MotorClosing
from utils.data_utils import *


class MotorClosingDlg(QDialog, Ui_MotorClosing):
    """
    0炉子开关参数配置界面
    """
    config_hex_signal = Signal(str, int)

    def __init__(self):
        super(MotorClosingDlg, self).__init__()
        # 最终生成参数配置的十六进制编码
        self.config_hex = ""
        # 是否是新动作
        self.is_new_action = 0
        self.setupUi(self)
        # 读取配置
        config = get_config("D")
        # ---------- 电机片选 ----------
        self.motor_1 = config["motor_conf_select"]["dian_ji_1"]
        self.motor_2 = config["motor_conf_select"]["dian_ji_2"]
        self.motor_3 = config["motor_conf_select"]["dian_ji_3"]
        self.motor_4 = config["motor_conf_select"]["dian_ji_4"]
        self.motor_5 = config["motor_conf_select"]["dian_ji_5"]
        # 获取配置参数的16进制编码
        self.motor_omit_hex, self.motor_hex = self.get_motor_hex()
        # 开关量片选复选框状态改变
        self.checkBox_1.stateChanged.connect(self.motor_1_changed)
        self.checkBox_2.stateChanged.connect(self.motor_2_changed)
        self.checkBox_3.stateChanged.connect(self.motor_3_changed)
        self.checkBox_4.stateChanged.connect(self.motor_4_changed)
        self.checkBox_5.stateChanged.connect(self.motor_5_changed)

        # ------------ 关闭设置 ------------------
        self.tail1 = config["dian_ji_1_closing"]["tail"]
        self.tail2 = config["dian_ji_2_closing"]["tail"]
        self.tail3 = config["dian_ji_3_closing"]["tail"]
        self.tail4 = config["dian_ji_4_closing"]["tail"]
        self.tail5 = config["dian_ji_5_closing"]["tail"]
        self.val1_hex = self.get_val_hex(1)
        self.val2_hex = self.get_val_hex(2)
        self.val3_hex = self.get_val_hex(3)
        self.val4_hex = self.get_val_hex(4)
        self.val5_hex = self.get_val_hex(5)
        # 输入框值改变
        self.valLineEdit_1.textChanged.connect(self.val_text_changed)
        self.valLineEdit_2.textChanged.connect(self.val_text_changed)
        self.valLineEdit_3.textChanged.connect(self.val_text_changed)
        self.valLineEdit_4.textChanged.connect(self.val_text_changed)
        self.valLineEdit_5.textChanged.connect(self.val_text_changed)

        self.update_hex_val()
        # 存放最后生成的动作id
        self.action_id = ""
        # 生成动作ID按钮
        self.generateIDPushButton.clicked.connect(self.generate_action_ID)

        # 确定按钮
        self.commitPushButton.clicked.connect(self.commit_config)

    def update_hex_val(self):
        self.hexLineEdit_1.setText(self.motor_hex)
        self.hexOmitLineEdit_1.setText(self.motor_omit_hex)
        self.hexLineEdit_2.setText(self.val1_hex)
        self.hexOmitLineEdit_2.setText(self.val1_hex[0:2])
        self.hexLineEdit_3.setText(self.val2_hex)
        self.hexOmitLineEdit_3.setText(self.val2_hex[0:2])
        self.hexLineEdit_4.setText(self.val3_hex)
        self.hexOmitLineEdit_4.setText(self.val3_hex[0:2])
        self.hexLineEdit_5.setText(self.val4_hex)
        self.hexOmitLineEdit_5.setText(self.val4_hex[0:2])
        self.hexLineEdit_6.setText(self.val5_hex)
        self.hexOmitLineEdit_6.setText(self.val5_hex[0:2])

    def get_motor_hex(self):
        val = self.motor_5 + self.motor_4 + self.motor_3 + self.motor_2 + self.motor_1
        hex_val = format(int("1100" + val + "00", 2), '04X')  # 二进制字符串转16进制
        return hex_val, hex_val[2:] + hex_val[0:2]

    def motor_1_changed(self, state):
        if state == 2:
            self.motor_1 = "11"
        else:
            self.motor_1 = "00"
        # 获取配置参数的16进制编码
        self.motor_omit_hex, self.motor_hex = self.get_motor_hex()
        # 更新界面所展示的值
        self.update_hex_val()

    def motor_2_changed(self, state):
        if state == 2:
            self.motor_2 = "11"
        else:
            self.motor_2 = "00"
        # 获取配置参数的16进制编码
        self.motor_omit_hex, self.motor_hex = self.get_motor_hex()
        # 更新界面所展示的值
        self.update_hex_val()

    def motor_3_changed(self, state):
        if state == 2:
            self.motor_3 = "11"
        else:
            self.motor_3 = "00"
        # 获取配置参数的16进制编码
        self.motor_omit_hex, self.motor_hex = self.get_motor_hex()
        # 更新界面所展示的值
        self.update_hex_val()

    def motor_4_changed(self, state):
        if state == 2:
            self.motor_4 = "11"
        else:
            self.motor_4 = "00"
        # 获取配置参数的16进制编码
        self.motor_omit_hex, self.motor_hex = self.get_motor_hex()
        # 更新界面所展示的值
        self.update_hex_val()

    def motor_5_changed(self, state):
        if state == 2:
            self.motor_5 = "11"
        else:
            self.motor_5 = "00"
        # 获取配置参数的16进制编码
        self.motor_omit_hex, self.motor_hex = self.get_motor_hex()
        # 更新界面所展示的值
        self.update_hex_val()

    def get_val_hex(self, index):
        global val, tail
        if index == 1:
            val = self.valLineEdit_1.text()
            tail = self.tail1
        elif index == 2:
            val = self.valLineEdit_2.text()
            tail = self.tail2
        elif index == 3:
            val = self.valLineEdit_3.text()
            tail = self.tail3
        elif index == 4:
            val = self.valLineEdit_4.text()
            tail = self.tail4
        elif index == 5:
            val = self.valLineEdit_5.text()
            tail = self.tail5
        return val + tail

    def val_text_changed(self):
        self.val1_hex = self.get_val_hex(1)
        self.val2_hex = self.get_val_hex(2)
        self.val3_hex = self.get_val_hex(3)
        self.val4_hex = self.get_val_hex(4)
        self.val5_hex = self.get_val_hex(5)
        self.update_hex_val()

    # ------------ 生成动作ID -----------------------
    def generate_action_ID(self):
        # 得到最终的动作16进制编码
        self.config_hex = self.motor_hex + self.val1_hex + self.val2_hex + self.val3_hex + self.val4_hex + self.val5_hex

        # print(f"生成的16进制参数配置: {self.config_hex}")
        self.action_id, self.is_new_action = get_action_id(self.config_hex, "D")
        # id显示到界面
        self.actionIDLineEdit.setText(self.action_id)

    # ------------ 提交 -----------------------
    def commit_config(self):
        # 发送信号(id的前两位和后两位要调换位置)
        self.config_hex_signal.emit(self.action_id[2:] + self.action_id[0:2] + self.config_hex, self.is_new_action)
        # 发送完关闭窗口
        self.close()