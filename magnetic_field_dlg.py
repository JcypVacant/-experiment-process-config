from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog

from ui.MagneticField import Ui_MagneticField
from utils.data_utils import *


class MagneticFieldDlg(QDialog, Ui_MagneticField):
    """
    8磁场参数配置界面
    """
    config_hex_signal = Signal(str, int)
    def __init__(self):
        super(MagneticFieldDlg, self).__init__()
        # 是否是新ID
        self.is_new_action = None
        # 最终的16进制配置信息
        self.config_hex = None

        self.setupUi(self)
        # 读取参数配置
        config = get_config(8)
        # -------------- 磁场细分 -----------------
        self.xi_fen_1 = config["magnetic_xi_fen"]["xi_fen_1"]
        self.xi_fen_2 = config["magnetic_xi_fen"]["xi_fen_2"]
        self.xi_fen_4 = config["magnetic_xi_fen"]["xi_fen_4"]
        self.xi_fen_16 = config["magnetic_xi_fen"]["xi_fen_16"]
        self.xi_fen_tail = config["magnetic_xi_fen"]["tail"]
        # 细分索引
        self.xi_fen_index = 0
        # 16进制值
        self.xi_fen_omit_hex, self.xi_fen_hex = self.get_xi_fen_hex()
        # 下拉框索引改变
        self.comboBox_1.currentIndexChanged.connect(self.xi_fen_index_changed)

        # --------------- 磁场运行方向 ------------------
        self.run_forward = config["magnetic_direction"]["forward"]
        self.run_backward = config["magnetic_direction"]["backward"]
        self.run_tail = config["magnetic_direction"]["tail"]
        self.run_index = 0
        # 16进制值
        self.run_omit_hex, self.run_hex = self.get_run_hex()
        # 下拉框索引改变
        self.comboBox_2.currentIndexChanged.connect(self.run_index_changed)

        # ---------------- 磁场运行速率设置 -----------------
        self.high_address = config["magnetic_velocity"]["high_address"]
        self.low_address = config["magnetic_velocity"]["low_address"]
        # 16进制值
        self.velocity_omit_hex, self.velocity_hex = self.get_velocity_hex()

        # --------------- 磁场驱动使能 -------------------
        self.magnetic1 = config["magnetic_enable"]["magnetic1"]
        self.magnetic2 = config["magnetic_enable"]["magnetic2"]
        self.magnetic3 = config["magnetic_enable"]["magnetic3"]
        self.magnetic4 = config["magnetic_enable"]["magnetic4"]
        self.magnetic_tail = config["magnetic_enable"]["tail"]
        # 获取参数16进制编码
        self.magnetic_omit_hex, self.magnetic_hex = self.get_magnetic_hex()
        # 电机参数片选复选框状态改变
        self.checkBox_1.stateChanged.connect(self.c_1_state_changed)
        self.checkBox_2.stateChanged.connect(self.c_2_state_changed)
        self.checkBox_3.stateChanged.connect(self.c_3_state_changed)
        self.checkBox_4.stateChanged.connect(self.c_4_state_changed)

        self.update_hex_val()

        # 存放最后生成的动作id
        self.action_id = None
        # 生成动作ID按钮
        self.generateIDPushButton.clicked.connect(self.generate_action_ID)

        # 确定按钮
        self.commitPushButton.clicked.connect(self.commit_config)

    def update_hex_val(self):
        # 细分
        self.hexOmitLineEdit_1.setText(self.xi_fen_omit_hex)
        self.hexLineEdit_1.setText(self.xi_fen_hex)
        # 方向
        self.hexOmitLineEdit_2.setText(self.run_omit_hex)
        self.hexLineEdit_2.setText(self.run_hex)
        # 速率
        self.hexOmitLineEdit_3.setText(self.velocity_omit_hex)
        self.hexLineEdit_3.setText(self.velocity_hex)
        # 驱动使能
        self.hexOmitLineEdit_4.setText(self.magnetic_omit_hex)
        self.hexLineEdit_4.setText(self.magnetic_hex)

    # -------------- 磁场细分 -----------------
    def get_xi_fen_hex(self):
        hex_val = self.xi_fen_1
        if self.xi_fen_index == 1:
            hex_val = self.xi_fen_2
        elif self.xi_fen_index == 2:
            hex_val = self.xi_fen_4
        elif self.xi_fen_index == 3:
            hex_val = self.xi_fen_16
        return hex_val[2:] + hex_val[0:2], hex_val + self.xi_fen_tail

    def xi_fen_index_changed(self):
        self.xi_fen_index = self.comboBox_1.currentIndex()
        self.xi_fen_omit_hex, self.xi_fen_hex = self.get_xi_fen_hex()
        self.update_hex_val()

    # --------------- 磁场运行方向 ------------------
    def get_run_hex(self):
        hex_val = self.run_forward
        if self.run_index == 1:
            hex_val = self.run_backward
        return hex_val[2:] + hex_val[0:2], hex_val + self.run_tail

    def run_index_changed(self):
        self.run_index = self.comboBox_2.currentIndex()
        self.run_omit_hex, self.run_hex = self.get_run_hex()
        self.update_hex_val()

    # ---------------- 磁场运行速率设置 -----------------
    def get_velocity_hex(self):
        hex_val = float(self.velocityLineEdit.text())
        data = ((1024 * 1000) / (hex_val * 64) / 2) - 1
        hex_val = format(int(data), '08X')
        return hex_val, hex_val[2:4] + hex_val[0:2] + self.high_address + hex_val[6:] + hex_val[4:6] + self.low_address

    # --------------- 磁场驱动使能 -------------------
    def get_magnetic_hex(self):
        hex_val = self.magnetic4 + self.magnetic3 + self.magnetic2 + self.magnetic1
        return hex_val, hex_val[2:] + hex_val[0:2] + self.magnetic_tail

    def c_1_state_changed(self, state):
        if state == 2:
            self.magnetic1 = "F"
        else:
            self.magnetic1 = "0"
        # 获取配置参数的16进制编码
        self.magnetic_omit_hex, self.magnetic_hex = self.get_magnetic_hex()
        # 更新界面所展示的值
        self.update_hex_val()

    def c_2_state_changed(self, state):
        if state == 2:
            self.magnetic2 = "F"
        else:
            self.magnetic2 = "0"
        # 获取配置参数的16进制编码
        self.magnetic_omit_hex, self.magnetic_hex = self.get_magnetic_hex()
        # 更新界面所展示的值
        self.update_hex_val()

    def c_3_state_changed(self, state):
        if state == 2:
            self.magnetic3 = "F"
        else:
            self.magnetic3 = "0"
        # 获取配置参数的16进制编码
        self.magnetic_omit_hex, self.magnetic_hex = self.get_magnetic_hex()
        # 更新界面所展示的值
        self.update_hex_val()

    def c_4_state_changed(self, state):
        if state == 2:
            self.magnetic4 = "F"
        else:
            self.magnetic4 = "0"
        # 获取配置参数的16进制编码
        self.magnetic_omit_hex, self.magnetic_hex = self.get_magnetic_hex()
        # 更新界面所展示的值
        self.update_hex_val()

    # ------------- 生成动作ID ----------------
    def generate_action_ID(self):
        # 得到最终的动作16进制编码
        self.config_hex = self.xi_fen_hex + self.run_hex + self.velocity_hex + self.magnetic_hex

        # print(f"生成的16进制参数配置: {self.config_hex}")
        self.action_id, self.is_new_action = get_action_id(self.config_hex, 8)
        # id显示到界面
        self.actionIDLineEdit.setText(self.action_id)

    # ------------ 提交 -----------------------
    def commit_config(self):
        # 发送信号(id的前两位和后两位要调换位置)
        self.config_hex_signal.emit(self.action_id[2:] + self.action_id[0:2] + self.config_hex, self.is_new_action)
        # 发送完关闭窗口
        self.close()