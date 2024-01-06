from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog

from ui.OnlineMonitoringHead import Ui_OnlineMonitoringHead
from utils.data_utils import *


class OnlineMonitoringHeadDlg(QDialog, Ui_OnlineMonitoringHead):
    config_hex_signal = Signal(str, int)

    def __init__(self):
        super(OnlineMonitoringHeadDlg, self).__init__()
        # 是否是新ID
        self.is_new_action = None
        # 最终的16进制配置信息
        self.config_hex = None

        self.setupUi(self)
        # -------- 配置 ------------
        self.val1_omit_hex, self.val1_hex = self.get_val_hex(1)
        self.val2_omit_hex, self.val2_hex = self.get_val_hex(2)
        self.val3_omit_hex, self.val3_hex = self.get_val_hex(3)
        self.val4_omit_hex, self.val4_hex = self.get_val_hex(4)

        self.valLineEdit_1.textChanged.connect(self.val_text_changed)
        self.valLineEdit_2.textChanged.connect(self.val_text_changed)
        self.valLineEdit_3.textChanged.connect(self.val_text_changed)
        self.valLineEdit_4.textChanged.connect(self.val_text_changed)

        self.update_hex_val()
        # 存放最后生成的动作id
        self.action_id = ""
        # 生成动作ID按钮
        self.generateIDPushButton.clicked.connect(self.generate_action_ID)
        # 确定按钮
        self.commitPushButton.clicked.connect(self.commit_config)

    def update_hex_val(self):
        self.hexOmitLineEdit_1.setText(self.val1_omit_hex)
        self.hexOmitLineEdit_2.setText(self.val2_omit_hex)
        self.hexOmitLineEdit_3.setText(self.val3_omit_hex)
        self.hexOmitLineEdit_4.setText(self.val4_omit_hex)
        self.hexLineEdit_1.setText(self.val1_hex)
        self.hexLineEdit_2.setText(self.val2_hex)
        self.hexLineEdit_3.setText(self.val3_hex)
        self.hexLineEdit_4.setText(self.val4_hex)

    def get_val_hex(self, index):
        val = self.valLineEdit_1.text()
        if index == 2:
            val = self.valLineEdit_2.text()
            return val, val[2:4] + val[0:2]
        elif index == 3:
            val = self.valLineEdit_3.text()
            return val, val
        elif index == 4:
            val = self.valLineEdit_4.text()
            return val, val
        return val, val[2:4] + val[0:2]

    def val_text_changed(self):
        self.val1_omit_hex, self.val1_hex = self.get_val_hex(1)
        self.val2_omit_hex, self.val2_hex = self.get_val_hex(2)
        self.val3_omit_hex, self.val3_hex = self.get_val_hex(3)
        self.val4_omit_hex, self.val4_hex = self.get_val_hex(4)
        self.update_hex_val()

    # ------------ 生成动作ID -----------------------
    def generate_action_ID(self):
        # 得到最终的动作16进制编码
        self.config_hex = self.val1_hex + self.val2_hex + self.val3_hex + self.val4_hex
        # print(f"生成的16进制参数配置: {self.config_hex}")
        self.action_id, self.is_new_action = get_action_id(self.config_hex, "E")
        # id显示到界面
        self.actionIDLineEdit.setText(self.action_id)

    # ------------ 提交 -----------------------
    def commit_config(self):
        # 发送信号(id的前两位和后两位要调换位置)
        self.config_hex_signal.emit(self.action_id[2:] + self.action_id[0:2] + self.config_hex, self.is_new_action)
        # 发送完关闭窗口
        self.close()