from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog

from ui.FurnaceSwitch import Ui_FurnaceSwitch
from utils.data_utils import *


class FurnaceSwitchDlg(QDialog, Ui_FurnaceSwitch):
    """
    0炉子开关参数配置界面
    """
    config_hex_signal = Signal(str, int)

    def __init__(self):
        super(FurnaceSwitchDlg, self).__init__()
        # 最终生成参数配置的十六进制编码
        self.config_hex = ""
        # 是否是新动作
        self.is_new_action = 0
        self.setupUi(self)
        # 读取配置
        furnace_config = get_config(0)
        # -------- 1.初始化开关量片选 ----------------
        self.led_switch_val = furnace_config["switch_plate_selection"]["LED"]
        self.ccd_switch_val = furnace_config["switch_plate_selection"]["CCD"]
        self.valve_switch_val = furnace_config["switch_plate_selection"]["valve"]
        self.acc_switch_val = furnace_config["switch_plate_selection"]["acceleration"]
        self.sample_box_switch_val = furnace_config["switch_plate_selection"]["sample_box"]
        # 获取配置参数的16进制编码
        self.switch_plate_selection_hex = self.get_switch_plate_selection_hex()
        # 开关量片选复选框状态改变
        self.LEDCheckBox.stateChanged.connect(self.led_state_changed)
        self.CCDCheckBox.stateChanged.connect(self.ccd_state_changed)
        self.valveCheckBox.stateChanged.connect(self.valve_state_changed)
        self.accCheckBox.stateChanged.connect(self.acc_state_changed)
        self.sampleBoxCheckBox.stateChanged.connect(self.sample_box_state_changed)

        # ---------- 2.初始化LED使能设置 --------------
        self.led1_enable = furnace_config["LED_enable_settings"]["LED1_enable"]
        self.led1_close = furnace_config["LED_enable_settings"]["LED1_close"]
        self.led2_enable = furnace_config["LED_enable_settings"]["LED2_enable"]
        self.led2_close = furnace_config["LED_enable_settings"]["LED2_close"]
        self.led_enable_tail = furnace_config["LED_enable_settings"]["tail"]
        # 下拉框索引
        self.led_enable_index = 0
        self.LEDComboBox.currentIndexChanged.connect(self.led_enable_index_changed)
        # 获取配置参数的16进制编码
        self.led_enable_hex = self.get_led_enable_settings_hex()

        # --------------------- 3.CCD 使能设置 ------------------
        self.ccd1_enable = furnace_config["CCD_enable_settings"]["CCD1_enable"]
        self.ccd1_close = furnace_config["CCD_enable_settings"]["CCD1_close"]
        self.ccd2_enable = furnace_config["CCD_enable_settings"]["CCD2_enable"]
        self.ccd2_close = furnace_config["CCD_enable_settings"]["CCD2_close"]
        self.ccd_enable_tail = furnace_config["CCD_enable_settings"]["tail"]
        # 下拉框索引
        self.ccd_enable_index = 0
        self.CCDComboBox.currentIndexChanged.connect(self.ccd_enable_index_changed)
        # 获取配置参数的16进制编码
        self.ccd_enable_hex = self.get_ccd_enable_settings_hex()

        # --------------------- 4.阀门使能设置 ------------------
        self.nitrogen_valve_open = furnace_config["valve_enable_settings"]["nitrogen_valve_open"]
        self.nitrogen_valve_close = furnace_config["valve_enable_settings"]["nitrogen_valve_close"]
        self.repressing_open = furnace_config["valve_enable_settings"]["re-pressing_open"]
        self.repressing_close = furnace_config["valve_enable_settings"]["re-pressing_close"]
        self.exhaust_switching = furnace_config["valve_enable_settings"]["exhaust_switching"]
        self.vacuum_control = furnace_config["valve_enable_settings"]["vacuum_control"]
        self.exhaust_vacuum_open = furnace_config["valve_enable_settings"]["exhaust_vacuum_open"]
        self.exhaust_vacuum_close = furnace_config["valve_enable_settings"]["exhaust_vacuum_close"]
        self.valve_enable_tail = furnace_config["valve_enable_settings"]["tail"]
        # 下拉索引
        self.valve_enable_index = 0
        self.valveComboBox.currentIndexChanged.connect(self.valve_enable_index_changed)
        # 获取配置参数的16进制编码
        self.valve_enable_hex = self.get_valve_enable_settings_hex()

        # --------------- 5.加速度设置 --------------------------
        self.acc_open = furnace_config["acceleration_settings"]["open"]
        self.acc_close = furnace_config["acceleration_settings"]["close"]
        self.acc_tail = furnace_config["acceleration_settings"]["tail"]
        # 下拉索引
        self.acc_index = 0
        self.accComboBox.currentIndexChanged.connect(self.acc_index_changed)
        # 获取配置参数的16进制编码
        self.acc_hex = self.get_acc_settings_hex()

        # --------------- 6.样品盒开关 -----------------------------
        self.sample_box_open = furnace_config["sample_box_settings"]["open"]
        self.sample_box_close = furnace_config["sample_box_settings"]["close"]
        self.sample_box_tail = furnace_config["sample_box_settings"]["tail"]
        # 下拉索引
        self.sample_box_index = 0
        self.sampleBoxComboBox.currentIndexChanged.connect(self.sample_box_index_changed)
        # 获取配置参数的16进制编码
        self.sample_box_hex = self.get_sample_box_settings_hex()

        # 更新界面上的16进制值
        self.update_hex_val()

        # 存放最后生成的动作id
        self.action_id = ""
        # 生成动作ID按钮
        self.generateIDPushButton.clicked.connect(self.generate_action_ID)

        # 确定按钮
        self.commitPushButton.clicked.connect(self.commit_config)

    def commit_config(self):
        # 发送信号(id的前两位和后两位要调换位置)
        self.config_hex_signal.emit(self.action_id[2:] + self.action_id[0:2] + self.config_hex, self.is_new_action)
        # 发送完关闭窗口
        self.close()

    def update_hex_val(self):
        """
        将16进制缩写和16进制的值在界面上更新
        :return:
        """
        # 开关量片选
        self.hexLineEdit_1.setText(self.switch_plate_selection_hex[2:] + self.switch_plate_selection_hex[0:2])
        self.hexOmitLineEdit_1.setText(self.switch_plate_selection_hex)
        # led使能设置
        self.hexLineEdit_2.setText(self.led_enable_hex)
        self.hexOmitLineEdit_2.setText(self.led_enable_hex[0:2])
        # ccd使能设置
        self.hexLineEdit_3.setText(self.ccd_enable_hex)
        self.hexOmitLineEdit_3.setText(self.ccd_enable_hex[0:2])
        # 阀门使能设置
        self.hexLineEdit_4.setText(self.valve_enable_hex)
        self.hexOmitLineEdit_4.setText(self.valve_enable_hex[0:2])
        # 加速度开关设置
        self.hexLineEdit_5.setText(self.acc_hex)
        self.hexOmitLineEdit_5.setText(self.acc_hex[2:4] + self.acc_hex[0:2])
        # 样品盒设置
        self.hexLineEdit_6.setText(self.sample_box_hex)
        self.hexOmitLineEdit_6.setText(self.sample_box_hex[0:2])

    # ---------------- switch_plate_selection --------------------------------
    def led_state_changed(self, state):
        if state == 2:
            self.led_switch_val = "11"
        else:
            self.led_switch_val = "00"
        # 获取配置参数的16进制编码
        self.switch_plate_selection_hex = self.get_switch_plate_selection_hex()
        # 更新界面所展示的值
        self.update_hex_val()

    def ccd_state_changed(self, state):
        if state == 2:
            self.ccd_switch_val = "11"
        else:
            self.ccd_switch_val = "00"
        # 获取配置参数的16进制编码
        self.switch_plate_selection_hex = self.get_switch_plate_selection_hex()
        # 更新界面所展示的值
        self.update_hex_val()

    def valve_state_changed(self, state):
        if state == 2:
            self.valve_switch_val = "11"
        else:
            self.valve_switch_val = "00"
        # 获取配置参数的16进制编码
        self.switch_plate_selection_hex = self.get_switch_plate_selection_hex()
        # 更新界面所展示的值
        self.update_hex_val()

    def acc_state_changed(self, state):
        if state == 2:
            self.acc_switch_val = "11"
        else:
            self.acc_switch_val = "00"
        # 获取配置参数的16进制编码
        self.switch_plate_selection_hex = self.get_switch_plate_selection_hex()
        # 更新界面所展示的值
        self.update_hex_val()

    def sample_box_state_changed(self, state):
        if state == 2:
            self.sample_box_switch_val = "11"
        else:
            self.sample_box_switch_val = "00"
        # 获取配置参数的16进制编码
        self.switch_plate_selection_hex = self.get_switch_plate_selection_hex()
        # 更新界面所展示的值
        self.update_hex_val()

    def get_switch_plate_selection_hex(self):
        """
        返回开关片选量的配置值对应的十六进制
        :return:
        """
        val = self.sample_box_switch_val + self.acc_switch_val + self.valve_switch_val + self.ccd_switch_val + self.led_switch_val
        return format(int("1100" + val + "00", 2), 'X')     # 二进制字符串转16进制

    # ---------------- LED_enable_settings --------------------------------
    def led_enable_index_changed(self):
        """
        更新 led使能设置 下拉框索引
        :return:
        """
        self.led_enable_index = self.LEDComboBox.currentIndex()
        self.led_enable_hex = self.get_led_enable_settings_hex()
        self.update_hex_val()

    def get_led_enable_settings_hex(self):
        value = self.led1_enable
        if self.led_enable_index == 1:
            value = self.led1_close
        elif self.led_enable_index == 2:
            value = self.led2_enable
        elif self.led_enable_index == 3:
            value = self.led2_close
        return value + self.led_enable_tail

    # ---------------- ccd_enable_settings --------------------------------
    def ccd_enable_index_changed(self):
        """
        更新 ccd使能设置 下拉框索引
        :return:
        """
        self.ccd_enable_index = self.CCDComboBox.currentIndex()
        self.ccd_enable_hex = self.get_ccd_enable_settings_hex()
        self.update_hex_val()

    def get_ccd_enable_settings_hex(self):
        value = self.ccd1_enable
        if self.ccd_enable_index == 1:
            value = self.ccd1_close
        elif self.ccd_enable_index == 2:
            value = self.ccd2_enable
        elif self.ccd_enable_index == 3:
            value = self.ccd2_close
        return value + self.ccd_enable_tail

    # ---------------- valve_enable_settings --------------------------------
    def valve_enable_index_changed(self):
        """
        更新 阀门设置 下拉框索引
        :return:
        """
        self.valve_enable_index = self.valveComboBox.currentIndex()
        self.valve_enable_hex = self.get_valve_enable_settings_hex()
        self.update_hex_val()

    def get_valve_enable_settings_hex(self):
        value = self.nitrogen_valve_open
        if self.valve_enable_index == 1:
            value = self.nitrogen_valve_close
        elif self.valve_enable_index == 2:
            value = self.repressing_open
        elif self.valve_enable_index == 3:
            value = self.repressing_close
        elif self.valve_enable_index == 4:
            value = self.exhaust_switching
        elif self.valve_enable_index == 5:
            value = self.vacuum_control
        elif self.valve_enable_index == 6:
            value = self.exhaust_vacuum_open
        elif self.valve_enable_index == 7:
            value = self.exhaust_vacuum_close

        return value + self.valve_enable_tail

    # ---------------- acceleration_settings --------------------------------
    def acc_index_changed(self):
        """
        更新 acc设置 下拉框索引
        :return:
        """
        self.acc_index = self.accComboBox.currentIndex()
        self.acc_hex = self.get_acc_settings_hex()
        self.update_hex_val()

    def get_acc_settings_hex(self):
        value = self.acc_open
        if self.acc_index == 1:
            value = self.acc_close
        return value + self.acc_tail

    # ---------------- acceleration_settings --------------------------------
    def sample_box_index_changed(self):
        """
        更新 sample_box设置 下拉框索引
        :return:
        """
        self.sample_box_index = self.sampleBoxComboBox.currentIndex()
        self.sample_box_hex = self.get_sample_box_settings_hex()
        self.update_hex_val()

    def get_sample_box_settings_hex(self):
        value = self.sample_box_open
        if self.sample_box_index == 1:
            value = self.sample_box_close
        return value + self.sample_box_tail

    # 生成动作ID
    def generate_action_ID(self):
        # 得到最终的动作16进制编码
        self.config_hex = self.switch_plate_selection_hex[2:] + self.switch_plate_selection_hex[0:2] + \
                          self.led_enable_hex + self.ccd_enable_hex + \
                          self.valve_enable_hex + self.acc_hex + self.sample_box_hex
        self.action_id, self.is_new_action = get_action_id(self.config_hex, 0)
        # id显示到界面
        self.actionIDLineEdit.setText(self.action_id)


