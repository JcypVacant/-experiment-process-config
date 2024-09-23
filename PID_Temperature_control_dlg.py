from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog

from ui.PIDTemperatureControl import Ui_PIDTemperatureControl
from utils.data_utils import *


class PIDTemperatureControlDlg(QDialog, Ui_PIDTemperatureControl):
    """
    11PID控温曲线设置参数配置界面
    """
    config_hex_signal = Signal(str, int)

    def __init__(self):
        super(PIDTemperatureControlDlg, self).__init__()
        # 是否是新ID
        self.is_new_action = None
        # 最终的16进制配置信息
        self.config_hex = None

        self.setupUi(self)
        # 读取参数配置
        config = get_config("B")
        # -------------- 爬升率配置使能 ---------------------
        self.climb_enable_up = config["rate_of_climb_enable"]["PID_up"]
        self.climb_enable_open = config["rate_of_climb_enable"]["PID_open"]
        self.climb_enable_close = config["rate_of_climb_enable"]["PID_close"]
        self.climb_enable_none = config["rate_of_climb_enable"]["PID_none"]
        self.climb_enable_down = config["rate_of_climb_enable"]["PID_down"]
        # 下拉索引
        self.PID1_index = 3
        # 设置下拉框默认值为climb_enable_none（PID1不选）
        self.comboBox_1.setCurrentIndex(self.PID1_index)
        self.PID2_index = 4
        self.comboBox_2.setCurrentIndex(self.PID2_index)
        self.PID3_index = 3
        self.comboBox_3.setCurrentIndex(self.PID3_index)
        self.PID4_index = 3
        self.comboBox_4.setCurrentIndex(self.PID4_index)
        # 16进制值
        self.climb_enable_omit_hex, self.climb_enable_hex = self.get_climb_enable_hex()
        # 下拉索引改变
        self.comboBox_1.currentIndexChanged.connect(self.c_1_index_changed)
        self.comboBox_2.currentIndexChanged.connect(self.c_2_index_changed)
        self.comboBox_3.currentIndexChanged.connect(self.c_3_index_changed)
        self.comboBox_4.currentIndexChanged.connect(self.c_4_index_changed)

        # ------------- PID1 -------------------------
        # 获取输入框的值改变val1
        self.PID1ValLineEdit_1.textChanged.connect(self.PID1_val_1_text_changed)
        # 获取16进制值和16进制缩写
        self.PID1_val_1_omit_hex, self.PID1_val_1_hex = self.get_PID1_val_1_hex()

        # 获取输入框的值改变val2
        self.PID1ValLineEdit_2.textChanged.connect(self.PID1_val_2_text_changed)
        # 获取16进制值和16进制缩写
        self.PID1_val_2_omit_hex, self.PID1_val_2_hex = self.get_PID1_val_2_hex()

        # 获取输入框的值改变val3
        self.PID1ValLineEdit_3.textChanged.connect(self.PID1_val_3_text_changed)
        # 获取16进制值和16进制缩写
        self.PID1_val_3_omit_hex, self.PID1_val_3_hex = self.get_PID1_val_3_hex()

        # 获取输入框的值改变val4
        self.PID1ValLineEdit_4.textChanged.connect(self.PID1_val_4_text_changed)
        # 获取16进制值和16进制缩写
        self.PID1_val_4_omit_hex, self.PID1_val_4_hex = self.get_PID1_val_4_hex()

        # ------------- PID2 -------------------------
        # 获取输入框的值改变val1
        self.PID2ValLineEdit_1.textChanged.connect(self.PID2_val_1_text_changed)
        # 获取16进制值和16进制缩写
        self.PID2_val_1_omit_hex, self.PID2_val_1_hex = self.get_PID2_val_1_hex()

        # 获取输入框的值改变val2
        self.PID2ValLineEdit_2.textChanged.connect(self.PID2_val_2_text_changed)
        # 获取16进制值和16进制缩写
        self.PID2_val_2_omit_hex, self.PID2_val_2_hex = self.get_PID2_val_2_hex()

        # 获取输入框的值改变val3
        self.PID2ValLineEdit_3.textChanged.connect(self.PID2_val_3_text_changed)
        # 获取16进制值和16进制缩写
        self.PID2_val_3_omit_hex, self.PID2_val_3_hex = self.get_PID2_val_3_hex()

        # 获取输入框的值改变val4
        self.PID2ValLineEdit_4.textChanged.connect(self.PID2_val_4_text_changed)
        # 获取16进制值和16进制缩写
        self.PID2_val_4_omit_hex, self.PID2_val_4_hex = self.get_PID2_val_4_hex()

        # ------------- PID3 -------------------------
        # 获取输入框的值改变val1
        self.PID3ValLineEdit_1.textChanged.connect(self.PID3_val_1_text_changed)
        # 获取16进制值和16进制缩写
        self.PID3_val_1_omit_hex, self.PID3_val_1_hex = self.get_PID3_val_1_hex()

        # 获取输入框的值改变val2
        self.PID3ValLineEdit_2.textChanged.connect(self.PID3_val_2_text_changed)
        # 获取16进制值和16进制缩写
        self.PID3_val_2_omit_hex, self.PID3_val_2_hex = self.get_PID3_val_2_hex()

        # 获取输入框的值改变val3
        self.PID3ValLineEdit_3.textChanged.connect(self.PID3_val_3_text_changed)
        # 获取16进制值和16进制缩写
        self.PID3_val_3_omit_hex, self.PID3_val_3_hex = self.get_PID3_val_3_hex()

        # 获取输入框的值改变val4
        self.PID3ValLineEdit_4.textChanged.connect(self.PID3_val_4_text_changed)
        # 获取16进制值和16进制缩写
        self.PID3_val_4_omit_hex, self.PID3_val_4_hex = self.get_PID3_val_4_hex()

        # ------------- PID4 -------------------------
        # 获取输入框的值改变val1
        self.PID4ValLineEdit_1.textChanged.connect(self.PID4_val_1_text_changed)
        # 获取16进制值和16进制缩写
        self.PID4_val_1_omit_hex, self.PID4_val_1_hex = self.get_PID4_val_1_hex()

        # 获取输入框的值改变val2
        self.PID4ValLineEdit_2.textChanged.connect(self.PID4_val_2_text_changed)
        # 获取16进制值和16进制缩写
        self.PID4_val_2_omit_hex, self.PID4_val_2_hex = self.get_PID4_val_2_hex()

        # 获取输入框的值改变val3
        self.PID4ValLineEdit_3.textChanged.connect(self.PID4_val_3_text_changed)
        # 获取16进制值和16进制缩写
        self.PID4_val_3_omit_hex, self.PID4_val_3_hex = self.get_PID4_val_3_hex()

        # 获取输入框的值改变val4
        self.PID4ValLineEdit_4.textChanged.connect(self.PID4_val_4_text_changed)
        # 获取16进制值和16进制缩写
        self.PID4_val_4_omit_hex, self.PID4_val_4_hex = self.get_PID4_val_4_hex()

        self.update_hex_val()
        # 存放最后生成的动作id
        self.action_id = ""
        # 生成动作ID按钮
        self.generateIDPushButton.clicked.connect(self.generate_action_ID)

        # 确定按钮
        self.commitPushButton.clicked.connect(self.commit_config)
        # 取消按钮
        self.cancelPushButton.clicked.connect(self.cancel_config)

    def update_hex_val(self):
        self.hexOmitLineEdit_1.setText(self.climb_enable_omit_hex)
        self.hexLineEdit_1.setText(self.climb_enable_hex)
        # PID1
        self.hexOmitLineEdit_2.setText(self.PID1_val_1_omit_hex)
        self.hexLineEdit_2.setText(self.PID1_val_1_hex)
        self.hexOmitLineEdit_3.setText(self.PID1_val_2_omit_hex)
        self.hexLineEdit_3.setText(self.PID1_val_2_hex)
        self.hexOmitLineEdit_4.setText(self.PID1_val_3_omit_hex)
        self.hexLineEdit_4.setText(self.PID1_val_3_hex)
        self.hexOmitLineEdit_5.setText(self.PID1_val_4_omit_hex)
        self.hexLineEdit_5.setText(self.PID1_val_4_hex)
        # PID2
        self.hexOmitLineEdit_6.setText(self.PID2_val_1_omit_hex)
        self.hexLineEdit_6.setText(self.PID2_val_1_hex)
        self.hexOmitLineEdit_7.setText(self.PID2_val_2_omit_hex)
        self.hexLineEdit_7.setText(self.PID2_val_2_hex)
        self.hexOmitLineEdit_8.setText(self.PID2_val_3_omit_hex)
        self.hexLineEdit_8.setText(self.PID2_val_3_hex)
        self.hexOmitLineEdit_9.setText(self.PID2_val_4_omit_hex)
        self.hexLineEdit_9.setText(self.PID2_val_4_hex)
        # PID3
        self.hexOmitLineEdit_10.setText(self.PID3_val_1_omit_hex)
        self.hexLineEdit_10.setText(self.PID3_val_1_hex)
        self.hexOmitLineEdit_11.setText(self.PID3_val_2_omit_hex)
        self.hexLineEdit_11.setText(self.PID3_val_2_hex)
        self.hexOmitLineEdit_12.setText(self.PID3_val_3_omit_hex)
        self.hexLineEdit_12.setText(self.PID3_val_3_hex)
        self.hexOmitLineEdit_13.setText(self.PID3_val_4_omit_hex)
        self.hexLineEdit_13.setText(self.PID3_val_4_hex)
        # PID4
        self.hexOmitLineEdit_14.setText(self.PID4_val_1_omit_hex)
        self.hexLineEdit_14.setText(self.PID4_val_1_hex)
        self.hexOmitLineEdit_15.setText(self.PID4_val_2_omit_hex)
        self.hexLineEdit_15.setText(self.PID4_val_2_hex)
        self.hexOmitLineEdit_16.setText(self.PID4_val_3_omit_hex)
        self.hexLineEdit_16.setText(self.PID4_val_3_hex)
        self.hexOmitLineEdit_17.setText(self.PID4_val_4_omit_hex)
        self.hexLineEdit_17.setText(self.PID4_val_4_hex)

    # -------------- 爬升率配置使能 ---------------------
    def get_climb_enable_hex(self):
        PID1_hex = self.climb_enable_none
        PID2_hex = self.climb_enable_down
        PID3_hex = self.climb_enable_none
        PID4_hex = self.climb_enable_none
        # ---------- PID1 ------------
        if self.PID1_index == 0:
            PID1_hex = self.climb_enable_up
        elif self.PID1_index == 1:
            PID1_hex = self.climb_enable_open
        elif self.PID1_index == 2:
            PID1_hex = self.climb_enable_close
        elif self.PID1_index == 3:
            PID1_hex = self.climb_enable_none
        elif self.PID1_index == 4:
            PID1_hex = self.climb_enable_down
        # ---------- PID2 ------------
        if self.PID2_index == 0:
            PID2_hex = self.climb_enable_up
        elif self.PID2_index == 1:
            PID2_hex = self.climb_enable_open
        elif self.PID2_index == 2:
            PID2_hex = self.climb_enable_close
        elif self.PID2_index == 3:
            PID2_hex = self.climb_enable_none
        elif self.PID2_index == 4:
            PID2_hex = self.climb_enable_down
        # ---------- PID3 ------------
        if self.PID3_index == 0:
            PID3_hex = self.climb_enable_up
        elif self.PID3_index == 1:
            PID3_hex = self.climb_enable_open
        elif self.PID3_index == 2:
            PID3_hex = self.climb_enable_close
        elif self.PID3_index == 3:
            PID3_hex = self.climb_enable_none
        elif self.PID3_index == 4:
            PID3_hex = self.climb_enable_down
        # ---------- PID4 ------------
        if self.PID4_index == 0:
            PID4_hex = self.climb_enable_up
        elif self.PID4_index == 1:
            PID4_hex = self.climb_enable_open
        elif self.PID4_index == 2:
            PID4_hex = self.climb_enable_close
        elif self.PID4_index == 3:
            PID4_hex = self.climb_enable_none
        elif self.PID4_index == 4:
            PID4_hex = self.climb_enable_down

        hex_val = PID4_hex + PID3_hex + PID2_hex + PID1_hex
        return hex_val, hex_val[2:] + hex_val[0:2]

    def c_1_index_changed(self):
        self.PID1_index = self.comboBox_1.currentIndex()
        self.climb_enable_omit_hex, self.climb_enable_hex = self.get_climb_enable_hex()
        self.update_hex_val()

    def c_2_index_changed(self):
        self.PID2_index = self.comboBox_2.currentIndex()
        self.climb_enable_omit_hex, self.climb_enable_hex = self.get_climb_enable_hex()
        self.update_hex_val()

    def c_3_index_changed(self):
        self.PID3_index = self.comboBox_3.currentIndex()
        self.climb_enable_omit_hex, self.climb_enable_hex = self.get_climb_enable_hex()
        self.update_hex_val()

    def c_4_index_changed(self):
        self.PID4_index = self.comboBox_4.currentIndex()
        self.climb_enable_omit_hex, self.climb_enable_hex = self.get_climb_enable_hex()
        self.update_hex_val()

    # -------------- PID1 ---------------------
    def get_PID1_val_1_hex(self):
        val = float(self.PID1ValLineEdit_1.text())
        hex_val = format(int(val), '04X')
        return hex_val, hex_val[2:] + hex_val[0:2]

    def PID1_val_1_text_changed(self):
        self.PID1_val_1_omit_hex, self.PID1_val_1_hex = self.get_PID1_val_1_hex()
        self.update_hex_val()

    def get_PID1_val_2_hex(self):
        val = float(self.PID1ValLineEdit_2.text())
        hex_val = format(int(val), '04X')
        return hex_val, hex_val[2:] + hex_val[0:2]

    def PID1_val_2_text_changed(self):
        self.PID1_val_2_omit_hex, self.PID1_val_2_hex = self.get_PID1_val_2_hex()
        self.update_hex_val()

    def get_PID1_val_3_hex(self):
        val = float(self.PID1ValLineEdit_3.text())
        hex_val = format(int(val), '04X')
        return hex_val, hex_val[2:] + hex_val[0:2]

    def PID1_val_3_text_changed(self):
        self.PID1_val_3_omit_hex, self.PID1_val_3_hex = self.get_PID1_val_3_hex()
        self.update_hex_val()

    def get_PID1_val_4_hex(self):
        val = float(self.PID1ValLineEdit_4.text())
        hex_val = format(int(val), '04X')
        return hex_val, hex_val[2:] + hex_val[0:2]

    def PID1_val_4_text_changed(self):
        self.PID1_val_4_omit_hex, self.PID1_val_4_hex = self.get_PID1_val_4_hex()
        self.update_hex_val()

    # -------------- PID2 ---------------------
    def get_PID2_val_1_hex(self):
        val = float(self.PID2ValLineEdit_1.text())
        hex_val = format(int(val), '04X')
        return hex_val, hex_val[2:] + hex_val[0:2]

    def PID2_val_1_text_changed(self):
        self.PID2_val_1_omit_hex, self.PID2_val_1_hex = self.get_PID2_val_1_hex()
        self.update_hex_val()

    def get_PID2_val_2_hex(self):
        val = float(self.PID2ValLineEdit_2.text())
        hex_val = format(int(val), '04X')
        return hex_val, hex_val[2:] + hex_val[0:2]

    def PID2_val_2_text_changed(self):
        self.PID2_val_2_omit_hex, self.PID2_val_2_hex = self.get_PID2_val_2_hex()
        self.update_hex_val()

    def get_PID2_val_3_hex(self):
        val = float(self.PID2ValLineEdit_3.text())
        hex_val = format(int(val), '04X')
        return hex_val, hex_val[2:] + hex_val[0:2]

    def PID2_val_3_text_changed(self):
        self.PID2_val_3_omit_hex, self.PID2_val_3_hex = self.get_PID2_val_3_hex()
        self.update_hex_val()

    def get_PID2_val_4_hex(self):
        val = float(self.PID2ValLineEdit_4.text())
        hex_val = format(int(val), '04X')
        return hex_val, hex_val[2:] + hex_val[0:2]

    def PID2_val_4_text_changed(self):
        self.PID2_val_4_omit_hex, self.PID2_val_4_hex = self.get_PID2_val_4_hex()
        self.update_hex_val()

    # -------------- PID3 ---------------------
    def get_PID3_val_1_hex(self):
        val = float(self.PID3ValLineEdit_1.text())
        hex_val = format(int(val), '04X')
        return hex_val, hex_val[2:] + hex_val[0:2]

    def PID3_val_1_text_changed(self):
        self.PID3_val_1_omit_hex, self.PID3_val_1_hex = self.get_PID3_val_1_hex()
        self.update_hex_val()

    def get_PID3_val_2_hex(self):
        val = float(self.PID3ValLineEdit_2.text())
        hex_val = format(int(val), '04X')
        return hex_val, hex_val[2:] + hex_val[0:2]

    def PID3_val_2_text_changed(self):
        self.PID3_val_2_omit_hex, self.PID3_val_2_hex = self.get_PID3_val_2_hex()
        self.update_hex_val()

    def get_PID3_val_3_hex(self):
        val = float(self.PID3ValLineEdit_3.text())
        hex_val = format(int(val), '04X')
        return hex_val, hex_val[2:] + hex_val[0:2]

    def PID3_val_3_text_changed(self):
        self.PID3_val_3_omit_hex, self.PID3_val_3_hex = self.get_PID3_val_3_hex()
        self.update_hex_val()

    def get_PID3_val_4_hex(self):
        val = float(self.PID3ValLineEdit_4.text())
        hex_val = format(int(val), '04X')
        return hex_val, hex_val[2:] + hex_val[0:2]

    def PID3_val_4_text_changed(self):
        self.PID3_val_4_omit_hex, self.PID3_val_4_hex = self.get_PID3_val_4_hex()
        self.update_hex_val()

    # -------------- PID4 ---------------------
    def get_PID4_val_1_hex(self):
        val = float(self.PID4ValLineEdit_1.text())
        hex_val = format(int(val), '04X')
        return hex_val, hex_val[2:] + hex_val[0:2]

    def PID4_val_1_text_changed(self):
        self.PID4_val_1_omit_hex, self.PID4_val_1_hex = self.get_PID4_val_1_hex()
        self.update_hex_val()

    def get_PID4_val_2_hex(self):
        val = float(self.PID4ValLineEdit_2.text())
        hex_val = format(int(val), '04X')
        return hex_val, hex_val[2:] + hex_val[0:2]

    def PID4_val_2_text_changed(self):
        self.PID4_val_2_omit_hex, self.PID4_val_2_hex = self.get_PID4_val_2_hex()
        self.update_hex_val()

    def get_PID4_val_3_hex(self):
        val = float(self.PID4ValLineEdit_3.text())
        hex_val = format(int(val), '04X')
        return hex_val, hex_val[2:] + hex_val[0:2]

    def PID4_val_3_text_changed(self):
        self.PID4_val_3_omit_hex, self.PID4_val_3_hex = self.get_PID4_val_3_hex()
        self.update_hex_val()

    def get_PID4_val_4_hex(self):
        val = float(self.PID4ValLineEdit_4.text())
        hex_val = format(int(val), '04X')
        return hex_val, hex_val[2:] + hex_val[0:2]

    def PID4_val_4_text_changed(self):
        self.PID4_val_4_omit_hex, self.PID4_val_4_hex = self.get_PID4_val_4_hex()
        self.update_hex_val()

    # ------------ 生成动作ID -----------------------
    def generate_action_ID(self):
        # 得到最终的动作16进制编码
        self.config_hex = self.climb_enable_hex + self.PID1_val_1_hex + self.PID1_val_2_hex + self.PID1_val_3_hex + \
                          self.PID1_val_4_hex + self.PID2_val_1_hex + self.PID2_val_2_hex + self.PID2_val_3_hex + \
                          self.PID2_val_4_hex + self.PID3_val_1_hex + self.PID3_val_2_hex + self.PID3_val_3_hex + \
                          self.PID3_val_4_hex + self.PID4_val_1_hex + self.PID4_val_2_hex + self.PID4_val_3_hex + \
                          self.PID4_val_4_hex
        # print(f"生成的16进制参数配置: {self.config_hex}")
        self.action_id, self.is_new_action = get_action_id(self.config_hex, "B")
        # id显示到界面
        self.actionIDLineEdit.setText(self.action_id)

    # ------------ 提交 -----------------------
    def commit_config(self):
        # 发送信号(id的前两位和后两位要调换位置)
        self.config_hex_signal.emit(self.action_id[2:] + self.action_id[0:2] + self.config_hex, self.is_new_action)
        # 发送完关闭窗口
        self.close()

    def cancel_config(self):
        # 取消配置
        self.actionIDLineEdit.clear()
        self.close()
