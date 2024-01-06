from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog

from ui.PIDConfigSettings import Ui_PIDConfigSettings
from utils.data_utils import *


class PIDConfigSettingsDlg(QDialog, Ui_PIDConfigSettings):
    """
    0炉子开关参数配置界面
    """
    config_hex_signal = Signal(str, int)

    def __init__(self):
        super(PIDConfigSettingsDlg, self).__init__()
        # 最终生成参数配置的十六进制编码
        self.config_hex = ""
        # 是否是新动作
        self.is_new_action = 0
        self.setupUi(self)

        self.val1_omit_hex, self.val1_hex = self.get_val_hex(self.valLineEdit_1.text())
        self.val2_omit_hex, self.val2_hex = self.get_val_hex(self.valLineEdit_2.text())
        self.val3_omit_hex, self.val3_hex = self.get_val_hex(self.valLineEdit_3.text())
        self.val4_omit_hex, self.val4_hex = self.get_val_hex(self.valLineEdit_4.text())
        self.val5_omit_hex, self.val5_hex = self.get_val_hex(self.valLineEdit_5.text())
        self.val6_omit_hex, self.val6_hex = self.get_val_hex(self.valLineEdit_6.text())
        self.val7_omit_hex, self.val7_hex = self.get_val_hex(self.valLineEdit_7.text())
        self.val8_omit_hex, self.val8_hex = self.get_val_hex(self.valLineEdit_8.text())
        self.val9_omit_hex, self.val9_hex = self.get_val_hex(self.valLineEdit_9.text())
        self.val10_omit_hex, self.val10_hex = self.get_val_hex(self.valLineEdit_10.text())
        self.val11_omit_hex, self.val11_hex = self.get_val_hex(self.valLineEdit_11.text())
        self.val12_omit_hex, self.val12_hex = self.get_val_hex(self.valLineEdit_12.text())

        self.valLineEdit_1.textChanged.connect(self.val_text_changed)
        self.valLineEdit_2.textChanged.connect(self.val_text_changed)
        self.valLineEdit_3.textChanged.connect(self.val_text_changed)
        self.valLineEdit_4.textChanged.connect(self.val_text_changed)
        self.valLineEdit_5.textChanged.connect(self.val_text_changed)
        self.valLineEdit_6.textChanged.connect(self.val_text_changed)
        self.valLineEdit_7.textChanged.connect(self.val_text_changed)
        self.valLineEdit_8.textChanged.connect(self.val_text_changed)
        self.valLineEdit_9.textChanged.connect(self.val_text_changed)
        self.valLineEdit_10.textChanged.connect(self.val_text_changed)
        self.valLineEdit_11.textChanged.connect(self.val_text_changed)
        self.valLineEdit_12.textChanged.connect(self.val_text_changed)

        self.update_hex_val()
        # 存放最后生成的动作id
        self.action_id = ""
        # 生成动作ID按钮
        self.generateIDPushButton.clicked.connect(self.generate_action_ID)

        # 确定按钮
        self.commitPushButton.clicked.connect(self.commit_config)

    def update_hex_val(self):
        self.hexOmitLineEdit_1.setText(self.val1_omit_hex)
        self.hexLineEdit_1.setText(self.val1_hex)
        self.hexOmitLineEdit_2.setText(self.val2_omit_hex)
        self.hexLineEdit_2.setText(self.val2_hex)
        self.hexOmitLineEdit_3.setText(self.val3_omit_hex)
        self.hexLineEdit_3.setText(self.val3_hex)
        self.hexOmitLineEdit_4.setText(self.val4_omit_hex)
        self.hexLineEdit_4.setText(self.val4_hex)
        self.hexOmitLineEdit_5.setText(self.val5_omit_hex)
        self.hexLineEdit_5.setText(self.val5_hex)
        self.hexOmitLineEdit_6.setText(self.val6_omit_hex)
        self.hexLineEdit_6.setText(self.val6_hex)
        self.hexOmitLineEdit_7.setText(self.val7_omit_hex)
        self.hexLineEdit_7.setText(self.val7_hex)
        self.hexOmitLineEdit_8.setText(self.val8_omit_hex)
        self.hexLineEdit_8.setText(self.val8_hex)
        self.hexOmitLineEdit_9.setText(self.val9_omit_hex)
        self.hexLineEdit_9.setText(self.val9_hex)
        self.hexOmitLineEdit_10.setText(self.val10_omit_hex)
        self.hexLineEdit_10.setText(self.val10_hex)
        self.hexOmitLineEdit_11.setText(self.val11_omit_hex)
        self.hexLineEdit_11.setText(self.val11_hex)
        self.hexOmitLineEdit_12.setText(self.val12_omit_hex)
        self.hexLineEdit_12.setText(self.val12_hex)

    def get_val_hex(self, val_text):
        val = float(val_text) * 1000
        val_hex = format(int(val), '04X')
        return val_hex, val_hex[2:] + val_hex[0:2]

    def val_text_changed(self):
        self.val1_omit_hex, self.val1_hex = self.get_val_hex(self.valLineEdit_1.text())
        self.val2_omit_hex, self.val2_hex = self.get_val_hex(self.valLineEdit_2.text())
        self.val3_omit_hex, self.val3_hex = self.get_val_hex(self.valLineEdit_3.text())
        self.val4_omit_hex, self.val4_hex = self.get_val_hex(self.valLineEdit_4.text())
        self.val5_omit_hex, self.val5_hex = self.get_val_hex(self.valLineEdit_5.text())
        self.val6_omit_hex, self.val6_hex = self.get_val_hex(self.valLineEdit_6.text())
        self.val7_omit_hex, self.val7_hex = self.get_val_hex(self.valLineEdit_7.text())
        self.val8_omit_hex, self.val8_hex = self.get_val_hex(self.valLineEdit_8.text())
        self.val9_omit_hex, self.val9_hex = self.get_val_hex(self.valLineEdit_9.text())
        self.val10_omit_hex, self.val10_hex = self.get_val_hex(self.valLineEdit_10.text())
        self.val11_omit_hex, self.val11_hex = self.get_val_hex(self.valLineEdit_11.text())
        self.val12_omit_hex, self.val12_hex = self.get_val_hex(self.valLineEdit_12.text())
        self.update_hex_val()

    # ------------ 生成动作ID -----------------------
    def generate_action_ID(self):
        # 得到最终的动作16进制编码
        self.config_hex = self.val1_hex + self.val2_hex + self.val3_hex + self.val4_hex + self.val5_hex + self.val6_hex + \
                          self.val7_hex + self.val8_hex + self.val9_hex + self.val10_hex + self.val11_hex + self.val12_hex

        # print(f"生成的16进制参数配置: {self.config_hex}")
        self.action_id, self.is_new_action = get_action_id(self.config_hex, "F")
        # id显示到界面
        self.actionIDLineEdit.setText(self.action_id)

    # ------------ 提交 -----------------------
    def commit_config(self):
        # 发送信号(id的前两位和后两位要调换位置)
        self.config_hex_signal.emit(self.action_id[2:] + self.action_id[0:2] + self.config_hex, self.is_new_action)
        # 发送完关闭窗口
        self.close()


# if __name__ == "__main__":
#     print(get_val_hex("0.1"))
