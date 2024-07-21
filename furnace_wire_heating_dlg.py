from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog

from ui.FurnaceWireHeating import Ui_FurnaceWireHeating
from utils.data_utils import *


class FurnaceWireHeatingDlg(QDialog, Ui_FurnaceWireHeating):
    """
    10炉丝加热电压参数配置界面
    """
    config_hex_signal = Signal(str, int)

    def __init__(self):
        super(FurnaceWireHeatingDlg, self).__init__()
        # 是否是新ID
        self.is_new_action = None
        # 最终的16进制配置信息
        self.config_hex = None

        self.setupUi(self)
        # 读取参数配置
        config = get_config("A")
        # --------------------- 电机电流片选 ------------------------
        self.furnace_wire_heating_select_voltage1 = config["furnace_wire_heating_select"]["voltage1"]
        self.furnace_wire_heating_select_voltage2 = config["furnace_wire_heating_select"]["voltage1"]
        self.furnace_wire_heating_select_voltage3 = config["furnace_wire_heating_select"]["voltage1"]
        self.furnace_wire_heating_select_voltage4 = config["furnace_wire_heating_select"]["voltage1"]
        # 获取参数16进制编码
        self.furnace_wire_heating_select_omit_hex = self.get_furnace_wire_heating_select_hex()
        self.furnace_wire_heating_select_hex = self.furnace_wire_heating_select_omit_hex[2:] + \
                                               self.furnace_wire_heating_select_omit_hex[0:2]
        # 电机电流片选复选框状态改变
        self.checkBox_1.stateChanged.connect(self.c_1_state_changed)
        self.checkBox_2.stateChanged.connect(self.c_2_state_changed)
        self.checkBox_3.stateChanged.connect(self.c_3_state_changed)
        self.checkBox_4.stateChanged.connect(self.c_4_state_changed)

        # --------------------- 电流1设置 ------------------------
        self.voltage1_tail = config["voltage1_settings"]["tail"]
        # 获取输入框的值改变
        self.valLineEdit_1.textChanged.connect(self.val_1_text_changed)
        # 获取16进制值和16进制缩写
        self.val_1_omit_hex, self.val_1_hex = self.get_val_1_hex()

        # --------------------- 电流2设置 ------------------------
        self.voltage2_tail = config["voltage2_settings"]["tail"]
        # 获取输入框的值改变
        self.valLineEdit_2.textChanged.connect(self.val_2_text_changed)
        # 获取16进制值和16进制缩写
        self.val_2_omit_hex, self.val_2_hex = self.get_val_2_hex()

        # --------------------- 电流3设置 ------------------------
        self.voltage3_tail = config["voltage3_settings"]["tail"]
        # 获取输入框的值改变
        self.valLineEdit_3.textChanged.connect(self.val_3_text_changed)
        # 获取16进制值和16进制缩写
        self.val_3_omit_hex, self.val_3_hex = self.get_val_3_hex()

        # --------------------- 磁场电流设置 ------------------------
        self.voltage4_tail = config["voltage4_settings"]["tail"]
        # 获取输入框的值改变
        self.valLineEdit_4.textChanged.connect(self.val_4_text_changed)
        # 获取16进制值和16进制缩写
        self.val_4_omit_hex, self.val_4_hex = self.get_val_4_hex()

        self.update_hex_val()

        # 存放最后生成的动作id
        self.action_id = ""
        # 生成动作ID按钮
        self.generateIDPushButton.clicked.connect(self.generate_action_ID)

        # 确定按钮
        self.commitPushButton.clicked.connect(self.commit_config)

    def update_hex_val(self):
        self.hexOmitLineEdit_1.setText(self.furnace_wire_heating_select_omit_hex)
        self.hexLineEdit_1.setText(self.furnace_wire_heating_select_hex)
        self.hexOmitLineEdit_2.setText(self.val_1_omit_hex)
        self.hexLineEdit_2.setText(self.val_1_hex)
        self.hexOmitLineEdit_3.setText(self.val_2_omit_hex)
        self.hexLineEdit_3.setText(self.val_2_hex)
        self.hexOmitLineEdit_4.setText(self.val_3_omit_hex)
        self.hexLineEdit_4.setText(self.val_3_hex)
        self.hexOmitLineEdit_5.setText(self.val_4_omit_hex)
        self.hexLineEdit_5.setText(self.val_4_hex)

    def get_furnace_wire_heating_select_hex(self):
        val = self.furnace_wire_heating_select_voltage4 + self.furnace_wire_heating_select_voltage3 + \
              self.furnace_wire_heating_select_voltage2 + self.furnace_wire_heating_select_voltage1
        return format(int("110000" + val + "00", 2), '04X')  # 二进制字符串转16进制（四位）

    # ------------- 电机状态复选框状态改变 --------------------
    def c_1_state_changed(self, state):
        if state == 2:
            self.furnace_wire_heating_select_voltage1 = "11"
        else:
            self.furnace_wire_heating_select_voltage1 = "00"
        # 获取配置参数的16进制编码
        self.furnace_wire_heating_select_omit_hex = self.get_furnace_wire_heating_select_hex()
        self.furnace_wire_heating_select_hex = self.furnace_wire_heating_select_omit_hex[2:] + \
                                               self.furnace_wire_heating_select_omit_hex[0:2]
        # 更新界面所展示的值
        self.update_hex_val()

    def c_2_state_changed(self, state):
        if state == 2:
            self.furnace_wire_heating_select_voltage2 = "11"
        else:
            self.furnace_wire_heating_select_voltage2 = "00"
        # 获取配置参数的16进制编码
        self.furnace_wire_heating_select_omit_hex = self.get_furnace_wire_heating_select_hex()
        self.furnace_wire_heating_select_hex = self.furnace_wire_heating_select_omit_hex[2:] + \
                                               self.furnace_wire_heating_select_omit_hex[0:2]
        # 更新界面所展示的值
        self.update_hex_val()

    def c_3_state_changed(self, state):
        if state == 2:
            self.furnace_wire_heating_select_voltage3 = "11"
        else:
            self.furnace_wire_heating_select_voltage3 = "00"
        # 获取配置参数的16进制编码
        self.furnace_wire_heating_select_omit_hex = self.get_furnace_wire_heating_select_hex()
        self.furnace_wire_heating_select_hex = self.furnace_wire_heating_select_omit_hex[2:] \
                                               + self.furnace_wire_heating_select_omit_hex[0:2]
        # 更新界面所展示的值
        self.update_hex_val()

    def c_4_state_changed(self, state):
        if state == 2:
            self.furnace_wire_heating_select_voltage4 = "11"
        else:
            self.furnace_wire_heating_select_voltage4 = "00"
        # 获取配置参数的16进制编码
        self.furnace_wire_heating_select_omit_hex = self.get_furnace_wire_heating_select_hex()
        self.furnace_wire_heating_select_hex = self.furnace_wire_heating_select_omit_hex[2:] \
                                               + self.furnace_wire_heating_select_omit_hex[0:2]
        # 更新界面所展示的值
        self.update_hex_val()

    # ------------- 电流1设置 ---------------------------
    def val_1_text_changed(self):
        self.val_1_omit_hex, self.val_1_hex = self.get_val_1_hex()
        self.update_hex_val()

    def get_val_1_hex(self):
        val = float(self.valLineEdit_1.text())
        data = ((val - 2.8) / (28 - 2.8)) * 4095
        hex_val = format(int(data), '04X')
        hex_adress = hex_val[2:4] + hex_val[0:2] + self.voltage1_tail
        return hex_val, hex_adress

    # ------------- 电流2设置 ---------------------------
    def val_2_text_changed(self):
        self.val_2_omit_hex, self.val_2_hex = self.get_val_2_hex()
        self.update_hex_val()

    def get_val_2_hex(self):
        val = float(self.valLineEdit_2.text())
        data = ((val - 2.8) / (28 - 2.8)) * 4095
        hex_val = format(int(data), '04X')
        hex_adress = hex_val[2:4] + hex_val[0:2] + self.voltage2_tail
        return hex_val, hex_adress

    # ------------- 电流3设置 ---------------------------
    def val_3_text_changed(self):
        self.val_3_omit_hex, self.val_3_hex = self.get_val_3_hex()
        self.update_hex_val()

    def get_val_3_hex(self):
        val = float(self.valLineEdit_3.text())
        data = ((val - 2.8) / (28 - 2.8)) * 4095
        hex_val = format(int(data), '04X')
        hex_adress = hex_val[2:4] + hex_val[0:2] + self.voltage3_tail
        return hex_val, hex_adress

    # ------------- 磁场电流设置 ---------------------------
    def val_4_text_changed(self):
        self.val_1_omit_hex, self.val_1_hex = self.get_val_1_hex()
        self.update_hex_val()

    def get_val_4_hex(self):
        val = float(self.valLineEdit_4.text())
        data = ((val - 2.8) / (28 - 2.8)) * 4095
        hex_val = format(int(data), '04X')
        hex_adress = hex_val[2:4] + hex_val[0:2] + self.voltage4_tail
        return hex_val, hex_adress

    # ------------- 生成动作ID ----------------
    def generate_action_ID(self):
        # 得到最终的动作16进制编码
        self.config_hex = self.furnace_wire_heating_select_hex + self.val_1_hex + \
                          self.val_2_hex + self.val_3_hex + self.val_4_hex

        # print(f"生成的16进制参数配置: {self.config_hex}")
        self.action_id, self.is_new_action = get_action_id(self.config_hex, "A")
        # id显示到界面
        self.actionIDLineEdit.setText(self.action_id)

    # ------------ 提交 -----------------------
    def commit_config(self):
        # 发送信号(id的前两位和后两位要调换位置)
        self.config_hex_signal.emit(self.action_id[2:] + self.action_id[0:2] + self.config_hex, self.is_new_action)
        # 发送完关闭窗口
        self.close()
