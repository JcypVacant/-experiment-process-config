from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog

from ui.Sample2 import Ui_Sample2
from utils.data_utils import *


class Sample2Dlg(QDialog, Ui_Sample2):
    """
    3样提机2参数配置界面
    """
    config_hex_signal = Signal(str, int)

    def __init__(self):
        super(Sample2Dlg, self).__init__()
        self.is_new_action = None
        self.config_hex = None
        self.setupUi(self)
        # 读取参数配置
        config = get_config(3)

        # ------------------- 开环参数 ----------------------
        self.open_loop_config_P = config["open_loop_config"]["P"]
        self.open_loop_config_i = config["open_loop_config"]["i"]
        self.open_loop_config_z1 = config["open_loop_config"]["z1"]
        self.open_loop_config_z2 = config["open_loop_config"]["z2"]
        # 显示在界面上
        self.pLineEdit_1.setText(str(self.open_loop_config_P))
        self.iLineEdit_1.setText(str(self.open_loop_config_i))
        self.z1LineEdit_1.setText(str(self.open_loop_config_z1))
        self.z2LineEdit_1.setText(str(self.open_loop_config_z2))
        # 运动类别索引
        self.open_loop_type_index = 0
        # ------------------- 非开环参数 ----------------------
        self.no_open_loop_config_P = config["no_open_loop_config"]["P"]
        self.no_open_loop_config_i = config["no_open_loop_config"]["i"]
        self.no_open_loop_config_z1 = config["no_open_loop_config"]["z1"]
        self.no_open_loop_config_z2 = config["no_open_loop_config"]["z2"]
        # 显示在界面上
        self.pLineEdit_2.setText(str(self.no_open_loop_config_P))
        self.iLineEdit_2.setText(str(self.no_open_loop_config_i))
        self.z1LineEdit_2.setText(str(self.no_open_loop_config_z1))
        self.z2LineEdit_2.setText(str(self.no_open_loop_config_z2))
        # 运动类别索引
        self.no_open_loop_type_index = 0
        # ------------------- 限位开关有效参数 ----------------------
        self.limit_switch_config_P = config["limit_switch_config"]["P"]
        self.limit_switch_config_i = config["limit_switch_config"]["i"]
        self.limit_switch_config_z1 = config["limit_switch_config"]["z1"]
        self.limit_switch_config_z2 = config["limit_switch_config"]["z2"]
        # 显示在界面上
        self.pLineEdit_3.setText(str(self.limit_switch_config_P))
        self.iLineEdit_3.setText(str(self.limit_switch_config_i))
        self.z1LineEdit_3.setText(str(self.limit_switch_config_z1))
        self.z2LineEdit_3.setText(str(self.limit_switch_config_z2))
        # 运动类别索引
        self.limit_switch_type_index = 0

        # --------------- 样提机2运行方式设置 ------------------
        self.run_mode_open_loop = config["zhuan_ji_1_run_mode"]["open_loop"]
        self.run_mode_limit_switch = config["zhuan_ji_1_run_mode"]["limit_switch"]
        self.run_mode_encoder = config["zhuan_ji_1_run_mode"]["encoder"]
        self.run_mode_tail = config["zhuan_ji_1_run_mode"]["tail"]

        # 下拉索引
        self.run_mode_index = 0
        # 十六进制缩写和十六进制值
        self.run_mode_hex = self.get_run_mode_hex()
        self.run_mode_omit_hex = self.run_mode_hex[2:4] + self.run_mode_hex[0:2]
        # 下拉框索引改变
        self.runModeComboBox.currentIndexChanged.connect(self.run_mode_index_changed)

        # ---------------------- 样提机2运行开环设置 -------------------
        self.run_loop_high_address = config["run_loop_settings"]["high_address"]
        self.run_loop_low_address = config["run_loop_settings"]["low_address"]
        # 获取输入框的值改变
        self.valLineEdit_1.textChanged.connect(self.val_1_text_changed)
        # 获取16进制值和16进制缩写
        self.val_1_omit_hex, self.val_1_hex = self.get_val_1_hex()
        # 下拉框索引改变
        self.typeComboBox_1.currentIndexChanged.connect(self.type_1_index_changed)

        # ---------------------- 样提机2运行编码器设置 -------------------
        self.run_encoder_high_address = config["run_encoder_settings"]["high_address"]
        self.run_encoder_low_address = config["run_encoder_settings"]["low_address"]
        # 获取输入框的值改变
        self.valLineEdit_2.textChanged.connect(self.val_2_text_changed)
        # 获取16进制值和16进制缩写
        self.val_2_omit_hex, self.val_2_hex = self.get_val_2_hex()

        # ---------------------- 样提机2脉冲输出阈值 -------------------
        self.pulse_high_address = config["pulse_output_threshold"]["high_address"]
        self.pulse_low_address = config["pulse_output_threshold"]["low_address"]
        # 输入框的值改变
        self.valLineEdit_3.textChanged.connect(self.val_3_text_changed)
        # 获取16进制值和16进制缩写
        self.val_3_omit_hex, self.val_3_hex = self.get_val_3_hex()
        # 下拉框索引改变
        self.typeComboBox_2.currentIndexChanged.connect(self.type_2_index_changed)

        # ---------------------- 样提机2续转步数 -------------------
        self.consecutive_steps_address = config["consecutive_steps"]["address"]
        # 输入框的值改变
        self.valLineEdit_4.textChanged.connect(self.val_4_text_changed)
        # 获取16进制值和16进制缩写
        self.val_4_omit_hex, self.val_4_hex = self.get_val_4_hex()
        # 下拉框索引改变
        self.typeComboBox_3.currentIndexChanged.connect(self.type_3_index_changed)

        # ---------------------- 限位开关设置值 -------------------
        self.limit_switch_address = config["limit_switch_settings"]["address"]
        # 获取参数配置
        self.ti_ji_2_shang = config["limit_switch_settings"]["ti_ji_2_shang"]
        self.ti_ji_2_xia = config["limit_switch_settings"]["ti_ji_2_xia"]
        self.zhuan_ji_1_0 = config["limit_switch_settings"]["zhuan_ji_1_0"]
        self.zhuan_ji_1_ji = config["limit_switch_settings"]["zhuan_ji_1_ji"]
        self.wu_hao = config["limit_switch_settings"]["wu_hao"]
        self.liu_hao = config["limit_switch_settings"]["liu_hao"]
        self.lu_shang_ji_3_shang = config["limit_switch_settings"]["lu_shang_ji_3_shang"]
        self.lu_shang_ji_3_xia = config["limit_switch_settings"]["lu_shang_ji_3_xia"]
        self.no_use = config["limit_switch_settings"]["no_use"]
        self.lu_xia_ji_5_shang = config["limit_switch_settings"]["lu_xia_ji_5_shang"]
        self.lu_xia_ji_5_xia = config["limit_switch_settings"]["lu_xia_ji_5_xia"]
        # 下拉索引
        self.limit_switch_index = 0
        # 十六进制缩写和十六进制值
        self.limit_switch_hex = self.get_limit_switch_hex()
        self.limit_switch_omit_hex = self.limit_switch_hex[2:4] + self.limit_switch_hex[0:2]
        # 下拉框索引改变
        self.switchValComboBox.currentIndexChanged.connect(self.limit_switch_index_changed)

        # ---------------------- 样提机2失步阈值 -------------------
        self.out_of_step_address = config["out_of_step_threshold"]["address"]
        # 输入框的值改变
        self.valLineEdit_5.textChanged.connect(self.val_5_text_changed)
        # 获取16进制值和16进制缩写
        self.val_5_omit_hex, self.val_5_hex = self.get_val_5_hex()
        # 更新显示
        self.update_hex_val()

        # 存放最后生成的动作id
        self.action_id = ""
        # 生成动作ID按钮
        self.generateIDPushButton.clicked.connect(self.generate_action_ID)

        # 确定按钮
        self.commitPushButton.clicked.connect(self.commit_config)

    def update_hex_val(self):
        #  样提机2运行方式设置
        self.hexOmitLineEdit_1.setText(self.run_mode_omit_hex)
        self.hexLineEdit_1.setText(self.run_mode_hex)
        # 样提机2运行开环设置
        self.hexLineEdit_2.setText(self.val_1_hex)
        self.hexOmitLineEdit_2.setText(self.val_1_omit_hex)
        # 样提机2运行编码器设置
        self.hexLineEdit_3.setText(self.val_2_hex)
        self.hexOmitLineEdit_3.setText(self.val_2_omit_hex)
        # 样提机2脉冲输出阈值
        self.hexLineEdit_4.setText(self.val_3_hex)
        self.hexOmitLineEdit_4.setText(self.val_3_omit_hex)
        # 样提机2续转步数
        self.hexLineEdit_5.setText(self.val_4_hex)
        self.hexOmitLineEdit_5.setText(self.val_4_omit_hex)
        # 限位开关
        self.hexLineEdit_6.setText(self.limit_switch_hex)
        self.hexOmitLineEdit_6.setText(self.limit_switch_omit_hex)
        # 失步阈值
        self.hexLineEdit_7.setText(self.val_5_hex)
        self.hexOmitLineEdit_7.setText(self.val_5_omit_hex)

    # ----------- 样提机2运行方式设置 --------------------
    def get_run_mode_hex(self):
        val = self.run_mode_open_loop
        if self.run_mode_index == 1:
            val = self.run_mode_limit_switch
        elif self.run_mode_index == 2:
            val = self.run_mode_encoder
        return val + self.run_mode_tail

    def run_mode_index_changed(self):
        self.run_mode_index = self.runModeComboBox.currentIndex()
        self.run_mode_hex = self.get_run_mode_hex()
        self.run_mode_omit_hex = self.run_mode_hex[2:4] + self.run_mode_hex[0:2]
        self.update_hex_val()

    # ------------- 运行开环设置值 -------------------------
    def val_1_text_changed(self):
        self.val_1_omit_hex, self.val_1_hex = self.get_val_1_hex()
        self.update_hex_val()

    def get_val_1_hex(self):
        val = float(self.valLineEdit_1.text())
        if self.open_loop_type_index == 0:
            # 直线运动计算方式
            data = ((val / (self.open_loop_config_z1 / self.open_loop_config_z2)) / (
                    self.open_loop_config_P / self.open_loop_config_i)) * 200
        else:
            # 圆周运动计算方式
            data = ((val / (self.open_loop_config_z1 / self.open_loop_config_z2)) / (1 / self.open_loop_config_i)) / 1.8
        hex_val = format(int(data), '08X')
        hex_adress = hex_val[2:4] + hex_val[0:2] + self.run_loop_high_address + hex_val[6:] + hex_val[
                                                                                              4:6] + self.run_loop_low_address
        return hex_val, hex_adress

    def type_1_index_changed(self):
        self.open_loop_type_index = self.typeComboBox_1.currentIndex()
        self.val_1_text_changed()

    # ------------- 运行编码器设置值 -------------------------
    def val_2_text_changed(self):
        self.val_2_omit_hex, self.val_2_hex = self.get_val_2_hex()
        self.update_hex_val()

    def get_val_2_hex(self):
        val = float(self.valLineEdit_2.text())
        data = (val * 1024) / 3
        hex_val = format(int(data), '08X')
        hex_adress = hex_val[2:4] + hex_val[0:2] + self.run_encoder_high_address + hex_val[6:] + hex_val[
                                                                                                 4:6] + self.run_encoder_low_address
        return hex_val, hex_adress

    # ------------- 脉冲输出阈值设置值 -------------------------
    def val_3_text_changed(self):
        self.val_3_omit_hex, self.val_3_hex = self.get_val_3_hex()
        self.update_hex_val()

    def get_val_3_hex(self):
        val = float(self.valLineEdit_3.text())
        if self.no_open_loop_type_index == 0:
            # 直线运动计算方式
            data = ((val / (self.no_open_loop_config_z1 / self.no_open_loop_config_z2)) / (
                    self.no_open_loop_config_P / self.no_open_loop_config_i)) * 200
        else:
            # 圆周运动计算方式
            data = ((val / (self.no_open_loop_config_z1 / self.no_open_loop_config_z2)) / (
                    1 / self.no_open_loop_config_i)) / 1.8
        hex_val = format(int(data), '08X')
        hex_adress = hex_val[2:4] + hex_val[0:2] + self.pulse_high_address + hex_val[6:] + hex_val[4:6] + self.pulse_low_address
        return hex_val, hex_adress

    def type_2_index_changed(self):
        self.no_open_loop_type_index = self.typeComboBox_2.currentIndex()
        # 脉冲输出值需要改变
        self.val_3_text_changed()
        # 失步阈值需要改变
        self.val_5_text_changed()

    # ------------- 续转步数 -------------------------
    def val_4_text_changed(self):
        self.val_4_omit_hex, self.val_4_hex = self.get_val_4_hex()
        self.update_hex_val()

    def get_val_4_hex(self):
        val = float(self.valLineEdit_4.text())
        if self.limit_switch_type_index == 0:
            # 直线运动计算方式
            data = ((val / (self.limit_switch_config_z1 / self.limit_switch_config_z2)) / (
                    self.limit_switch_config_P / self.limit_switch_config_i)) * 200
        else:
            # 圆周运动计算方式
            data = ((val / (self.limit_switch_config_z1 / self.limit_switch_config_z2)) / (
                    1 / self.limit_switch_config_i)) / 1.8
        hex_val = format(int(data), '04X')
        hex_adress = hex_val[2:4] + hex_val[0:2] + self.consecutive_steps_address
        return hex_val, hex_adress

    def type_3_index_changed(self):
        self.limit_switch_type_index = self.typeComboBox_3.currentIndex()
        self.val_4_text_changed()

    # ------------------ 限位开关设置值 ------------------
    def get_limit_switch_hex(self):
        if self.limit_switch_index == 0:
            hex_val = self.ti_ji_2_shang
        elif self.limit_switch_index == 1:
            hex_val = self.ti_ji_2_xia
        elif self.limit_switch_index == 2:
            hex_val = self.zhuan_ji_1_0
        elif self.limit_switch_index == 3:
            hex_val = self.zhuan_ji_1_ji
        elif self.limit_switch_index == 4:
            hex_val = self.wu_hao
        elif self.limit_switch_index == 5:
            hex_val = self.liu_hao
        elif self.limit_switch_index == 6:
            hex_val = self.lu_shang_ji_3_shang
        elif self.limit_switch_index == 7:
            hex_val = self.lu_shang_ji_3_xia
        elif self.limit_switch_index == 8:
            hex_val = self.lu_xia_ji_5_shang
        elif self.limit_switch_index == 9:
            hex_val = self.lu_xia_ji_5_xia
        else:
            hex_val = self.no_use
        return hex_val + self.limit_switch_address

    def limit_switch_index_changed(self):
        self.limit_switch_index = self.switchValComboBox.currentIndex()
        self.limit_switch_hex = self.get_limit_switch_hex()
        self.limit_switch_omit_hex = self.limit_switch_hex[2:4] + self.limit_switch_hex[0:2]
        self.update_hex_val()

    # ------------- 失步阈值 -------------------------
    def val_5_text_changed(self):
        self.val_5_omit_hex, self.val_5_hex = self.get_val_5_hex()
        self.update_hex_val()

    def get_val_5_hex(self):
        val = float(self.valLineEdit_5.text())
        if self.no_open_loop_type_index == 0:
            # 直线运动计算方式
            data = ((val / (self.no_open_loop_config_z1 / self.no_open_loop_config_z2)) / (
                    self.no_open_loop_config_P / self.no_open_loop_config_i)) * 200
        else:
            # 圆周运动计算方式
            data = ((val / (self.no_open_loop_config_z1 / self.no_open_loop_config_z2)) / (
                    1 / self.no_open_loop_config_i)) / 1.8
        hex_val = format(int(data), '08X')
        hex_adress = hex_val[6:] + hex_val[4:6] + self.out_of_step_address
        return hex_val, hex_adress

    # ------------ 生成动作ID -----------------------
    def generate_action_ID(self):
        # 得到最终的动作16进制编码
        self.config_hex = self.run_mode_hex + self.val_1_hex + self.val_2_hex + self.val_3_hex + \
                          self.val_4_hex + self.limit_switch_hex + self.val_5_hex
        # print(f"生成的16进制参数配置: {self.config_hex}")
        self.action_id, self.is_new_action = get_action_id(self.config_hex, 3)
        # id显示到界面
        self.actionIDLineEdit.setText(self.action_id)

    # ------------ 提交 -----------------------
    def commit_config(self):
        # 发送信号(id的前两位和后两位要调换位置)
        self.config_hex_signal.emit(self.action_id[2:] + self.action_id[0:2] + self.config_hex, self.is_new_action)
        # 发送完关闭窗口
        self.close()
