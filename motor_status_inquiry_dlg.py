from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog

from ui.MotorStatusInquiry import Ui_MotorStatusInquiry
from utils.data_utils import *


class MotorStatusInquiryDlg(QDialog, Ui_MotorStatusInquiry):
    """
    7电机状态查询参数配置界面
    """
    config_hex_signal = Signal(str, int)

    def __init__(self):
        super(MotorStatusInquiryDlg, self).__init__()
        # 是否是新ID
        self.is_new_action = None
        # 最终的16进制配置信息
        self.config_hex = None

        self.setupUi(self)
        # 读取参数配置
        config = get_config(7)
        # --------------------- 电机片选 ------------------
        self.motor_1 = config["motor_status_select"]["motor_1"]
        self.motor_2 = config["motor_status_select"]["motor_2"]
        self.motor_3 = config["motor_status_select"]["motor_3"]
        self.motor_4 = config["motor_status_select"]["motor_4"]
        self.motor_5 = config["motor_status_select"]["motor_5"]
        # 获取参数16进制编码
        self.motor_hex = self.get_motor_hex()
        # 电机参数片选复选框状态改变
        self.checkBox_1.stateChanged.connect(self.motor_1_state_changed)
        self.checkBox_2.stateChanged.connect(self.motor_2_state_changed)
        self.checkBox_3.stateChanged.connect(self.motor_3_state_changed)
        self.checkBox_4.stateChanged.connect(self.motor_4_state_changed)
        self.checkBox_5.stateChanged.connect(self.motor_5_state_changed)

        # -------------- 电机1状态查询 --------------------
        self.motor1_time_condition = config["motor1_status"]["time_condition"]
        self.motor1_in_place_condition = config["motor1_status"]["in_place_condition"]
        self.motor1_tail = config["motor1_status"]["tail"]
        # 电机1状态查询下拉框索引
        self.motor1_index = 0
        # 十六进制编码
        self.motor1_omit_hex, self.motor1_hex = self.get_motor1_hex()
        # 下拉框状态改变
        self.comboBox_1.currentIndexChanged.connect(self.motor1_index_changed)

        # ------------ 电机2状态查询 ------------------------
        self.motor2_time_condition = config["motor2_status"]["time_condition"]
        self.motor2_in_place_condition = config["motor2_status"]["in_place_condition"]
        self.motor2_tail = config["motor2_status"]["tail"]
        # 电机2状态查询下拉框索引
        self.motor2_index = 0
        # 十六进制编码
        self.motor2_omit_hex, self.motor2_hex = self.get_motor2_hex()
        # 下拉框状态改变
        self.comboBox_2.currentIndexChanged.connect(self.motor2_index_changed)

        # ------------------ 电机3状态查询 -------------------------
        self.motor3_time_condition = config["motor3_status"]["time_condition"]
        self.motor3_in_place_condition = config["motor3_status"]["in_place_condition"]
        self.motor3_tail = config["motor3_status"]["tail"]
        # 电机3状态查询下拉框索引
        self.motor3_index = 0
        # 十六进制编码
        self.motor3_omit_hex, self.motor3_hex = self.get_motor3_hex()
        # 下拉框状态改变
        self.comboBox_3.currentIndexChanged.connect(self.motor3_index_changed)

        # ------------------------ 电机4状态查询 ----------------------
        self.motor4_time_condition = config["motor4_status"]["time_condition"]
        self.motor4_in_place_condition = config["motor4_status"]["in_place_condition"]
        self.motor4_tail = config["motor4_status"]["tail"]
        # 电机4状态查询下拉框索引
        self.motor4_index = 0
        # 十六进制编码
        self.motor4_omit_hex, self.motor4_hex = self.get_motor4_hex()
        # 下拉框状态改变
        self.comboBox_4.currentIndexChanged.connect(self.motor4_index_changed)

        # ------------------ 电机5状态查询 -----------------------
        self.motor5_time_condition = config["motor5_status"]["time_condition"]
        self.motor5_in_place_condition = config["motor5_status"]["in_place_condition"]
        self.motor5_tail = config["motor5_status"]["tail"]
        # 电机5状态查询下拉框索引
        self.motor5_index = 0
        # 十六进制编码
        self.motor5_omit_hex, self.motor5_hex = self.get_motor5_hex()
        # 下拉框状态改变
        self.comboBox_5.currentIndexChanged.connect(self.motor5_index_changed)

        self.update_hex_val()

        # 存放最后生成的动作id
        self.action_id = None
        # 生成动作ID按钮
        self.generateIDPushButton.clicked.connect(self.generate_action_ID)

        # 确定按钮
        self.commitPushButton.clicked.connect(self.commit_config)

    def update_hex_val(self):
        # 电机片选
        self.hexOmitLineEdit.setText(self.motor_hex)
        self.hexLineEdit.setText(self.motor_hex[2:] + self.motor_hex[0:2])
        # 电机1状态查询
        self.hexOmitLineEdit_1.setText(self.motor1_omit_hex)
        self.hexLineEdit_1.setText(self.motor1_hex)
        # 电机2状态查询
        self.hexOmitLineEdit_2.setText(self.motor2_omit_hex)
        self.hexLineEdit_2.setText(self.motor2_hex)
        # 电机3状态查询
        self.hexOmitLineEdit_3.setText(self.motor3_omit_hex)
        self.hexLineEdit_3.setText(self.motor3_hex)
        # 电机4状态查询
        self.hexOmitLineEdit_4.setText(self.motor4_omit_hex)
        self.hexLineEdit_4.setText(self.motor4_hex)
        # 电机5状态查询
        self.hexOmitLineEdit_5.setText(self.motor5_omit_hex)
        self.hexLineEdit_5.setText(self.motor5_hex)

    def get_motor_hex(self):
        val = self.motor_5 + self.motor_4 + self.motor_3 + self.motor_2 + self.motor_1
        return format(int("1100" + val + "00", 2), '04X')  # 二进制字符串转16进制

    # ------------- 电机状态复选框状态改变 --------------------
    def motor_1_state_changed(self, state):
        if state == 2:
            self.motor_1 = "11"
        else:
            self.motor_1 = "00"
        # 获取配置参数的16进制编码
        self.motor_hex = self.get_motor_hex()
        # 更新界面所展示的值
        self.update_hex_val()

    def motor_2_state_changed(self, state):
        if state == 2:
            self.motor_2 = "11"
        else:
            self.motor_2 = "00"
        # 获取配置参数的16进制编码
        self.motor_hex = self.get_motor_hex()
        # 更新界面所展示的值
        self.update_hex_val()

    def motor_3_state_changed(self, state):
        if state == 2:
            self.motor_3 = "11"
        else:
            self.motor_3 = "00"
        # 获取配置参数的16进制编码
        self.motor_hex = self.get_motor_hex()
        # 更新界面所展示的值
        self.update_hex_val()

    def motor_4_state_changed(self, state):
        if state == 2:
            self.motor_4 = "11"
        else:
            self.motor_4 = "00"
        # 获取配置参数的16进制编码
        self.motor_hex = self.get_motor_hex()
        # 更新界面所展示的值
        self.update_hex_val()

    def motor_5_state_changed(self, state):
        if state == 2:
            self.motor_5 = "11"
        else:
            self.motor_5 = "00"
        # 获取配置参数的16进制编码
        self.motor_hex = self.get_motor_hex()
        # 更新界面所展示的值
        self.update_hex_val()

    # ----------------- 电机1状态查询 ---------------------------------
    def get_motor1_hex(self):
        hex_val = "00FF"
        if self.motor1_index == 1:
            hex_val = "0000"
        return hex_val, hex_val[2:] + hex_val[0:2] + self.motor1_tail

    def motor1_index_changed(self):
        self.motor1_index = self.comboBox_1.currentIndex()
        self.motor1_omit_hex, self.motor1_hex = self.get_motor1_hex()
        self.update_hex_val()

    # ----------------- 电机2状态查询 ---------------------------------
    def get_motor2_hex(self):
        hex_val = "00FF"
        if self.motor2_index == 1:
            hex_val = "0000"
        return hex_val, hex_val[2:] + hex_val[0:2] + self.motor2_tail

    def motor2_index_changed(self):
        self.motor2_index = self.comboBox_2.currentIndex()
        self.motor2_omit_hex, self.motor2_hex = self.get_motor2_hex()
        self.update_hex_val()

    # ----------------- 电机3状态查询 ---------------------------------
    def get_motor3_hex(self):
        hex_val = "00FF"
        if self.motor3_index == 1:
            hex_val = "0000"
        return hex_val, hex_val[2:] + hex_val[0:2] + self.motor3_tail

    def motor3_index_changed(self):
        self.motor3_index = self.comboBox_3.currentIndex()
        self.motor3_omit_hex, self.motor3_hex = self.get_motor3_hex()
        self.update_hex_val()

    # ----------------- 电机4状态查询 ---------------------------------
    def get_motor4_hex(self):
        hex_val = "00FF"
        if self.motor4_index == 1:
            hex_val = "0000"
        return hex_val, hex_val[2:] + hex_val[0:2] + self.motor4_tail

    def motor4_index_changed(self):
        self.motor4_index = self.comboBox_4.currentIndex()
        self.motor4_omit_hex, self.motor4_hex = self.get_motor4_hex()
        self.update_hex_val()

    # ----------------- 电机5状态查询 ---------------------------------
    def get_motor5_hex(self):
        hex_val = "00FF"
        if self.motor5_index == 1:
            hex_val = "0000"
        return hex_val, hex_val[2:] + hex_val[0:2] + self.motor5_tail

    def motor5_index_changed(self):
        self.motor5_index = self.comboBox_5.currentIndex()
        self.motor5_omit_hex, self.motor5_hex = self.get_motor5_hex()
        self.update_hex_val()

    # ------------- 生成动作ID ----------------
    def generate_action_ID(self):
        # 得到最终的动作16进制编码
        self.config_hex = self.motor_hex[2:] + self.motor_hex[0:2] + self.motor1_hex + self.motor2_hex + \
                          self.motor3_hex + self.motor4_hex + self.motor5_hex

        # print(f"生成的16进制参数配置: {self.config_hex}")
        self.action_id, self.is_new_action = get_action_id(self.config_hex, 7)
        # id显示到界面
        self.actionIDLineEdit.setText(self.action_id)

    # ------------ 提交 -----------------------
    def commit_config(self):
        # 发送信号(id的前两位和后两位要调换位置)
        self.config_hex_signal.emit(self.action_id[2:] + self.action_id[0:2] + self.config_hex, self.is_new_action)
        # 发送完关闭窗口
        self.close()