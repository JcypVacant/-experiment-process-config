from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog

from ui.OnlineMonitoringStatus import Ui_OnlineMonitoringStatus
from utils.data_utils import *


class OnlineMonitoringStatusDlg(QDialog, Ui_OnlineMonitoringStatus):
    """
    12在线监控状态参数配置界面
    """
    config_hex_signal = Signal(str, int)

    def __init__(self):
        super(OnlineMonitoringStatusDlg, self).__init__()
        # 是否是新ID
        self.is_new_action = None
        # 最终的16进制配置信息
        self.config_hex = None

        self.setupUi(self)
        # 读取参数配置
        config = get_config("C")
        # ---------- 在线监控判据类型 ----------
        self.type1 = config["judge_type"]["type1"]
        self.type2 = config["judge_type"]["type2"]
        self.type3 = config["judge_type"]["type3"]
        self.type4 = config["judge_type"]["type4"]
        # ---------- 逻辑判断后续实现处理标识 --------
        self.id1 = config["process_identification"]["id1"]
        self.id2 = config["process_identification"]["id2"]
        # ---------- 判断后续处理 -----------
        self.process1 = config["post_process"]["process1"]
        self.process2 = config["post_process"]["process2"]
        self.process3 = config["post_process"]["process3"]

        # --------- 在线监控查询时间间隔 ----------
        self.val1_hex = self.get_val1_hex()
        self.valLineEdit_1.textChanged.connect(self.val_text_changed)
        # ---------- 在线监控查询次数 ---------
        self.val2_hex = self.get_val2_hex()
        self.valLineEdit_2.textChanged.connect(self.val_text_changed)
        # ---------- 在线监控判据类型 ----------
        self.comb1_index = 0
        self.comb1_hex = self.get_comb1_hex()
        self.comboBox_1.currentIndexChanged.connect(self.comb1_index_changed)
        # --------- 在线监控地址和阈值 ---------
        self.val3_omit_hex, self.val3_hex = self.get_val3to6_hex(3)
        self.val4_omit_hex, self.val4_hex = self.get_val3to6_hex(4)
        self.val5_omit_hex, self.val5_hex = self.get_val3to6_hex(5)
        self.val6_omit_hex, self.val6_hex = self.get_val3to6_hex(6)
        self.valLineEdit_3.textChanged.connect(self.val_text_changed)
        self.valLineEdit_4.textChanged.connect(self.val_text_changed)
        self.valLineEdit_5.textChanged.connect(self.val_text_changed)
        self.valLineEdit_6.textChanged.connect(self.val_text_changed)
        # --------- 当发生逻辑时需进行的异常处理类型 ---------------
        self.comb2_index = 0
        self.comb2_hex = self.get_comb2_hex()
        self.comboBox_2.currentIndexChanged.connect(self.comb2_index_changed)
        # -------- 判断后续处理 ---------------
        self.comb3_index = 0
        self.comb3_hex = self.get_comb3_hex()
        self.comboBox_3.currentIndexChanged.connect(self.comb3_index_changed)
        # -------- 备用 -----------
        self.backup_hex = "0000"

        self.update_hex_val()
        # 存放最后生成的动作id
        self.action_id = ""
        # 生成动作ID按钮
        self.generateIDPushButton.clicked.connect(self.generate_action_ID)

        # 确定按钮
        self.commitPushButton.clicked.connect(self.commit_config)

    def update_hex_val(self):
        self.hexOmitLineEdit_1.setText(self.val1_hex)
        self.hexLineEdit_1.setText(self.val1_hex)
        self.hexOmitLineEdit_2.setText(self.val2_hex)
        self.hexLineEdit_2.setText(self.val2_hex)
        self.hexOmitLineEdit_3.setText(self.comb1_hex)
        self.hexLineEdit_3.setText(self.comb1_hex)

        self.hexOmitLineEdit_4.setText(self.val3_omit_hex)
        self.hexLineEdit_4.setText(self.val3_hex)
        self.hexOmitLineEdit_5.setText(self.val4_omit_hex)
        self.hexLineEdit_5.setText(self.val4_hex)
        self.hexOmitLineEdit_6.setText(self.val5_omit_hex)
        self.hexLineEdit_6.setText(self.val5_hex)
        self.hexOmitLineEdit_7.setText(self.val6_omit_hex)
        self.hexLineEdit_7.setText(self.val6_hex)

        self.hexOmitLineEdit_8.setText(self.comb2_hex[2:])
        self.hexLineEdit_8.setText(self.comb2_hex)
        self.hexOmitLineEdit_9.setText(self.comb3_hex[0:2])
        self.hexLineEdit_9.setText(self.comb3_hex)

    def get_val1_hex(self):
        val = int(self.valLineEdit_1.text())
        return format(val, '02X')

    def get_val2_hex(self):
        val = int(self.valLineEdit_2.text()) - 1
        return format(val, '02X')

    def get_comb1_hex(self):
        if self.comb1_index == 0:
            return self.type1
        elif self.comb1_index == 1:
            return self.type2
        elif self.comb1_index == 2:
            return self.type3
        else:
            return self.type4

    def get_comb2_hex(self):
        if self.comb2_index == 0:
            return self.id1
        elif self.comb2_index == 1:
            return self.id2

    def get_comb3_hex(self):
        if self.comb3_index == 0:
            return self.process1
        elif self.comb3_index == 1:
            return self.process2
        elif self.comb3_index == 2:
            return self.process3

    def comb1_index_changed(self):
        self.comb1_index = self.comboBox_1.currentIndex()
        self.comb1_hex = self.get_comb1_hex()
        self.update_hex_val()

    def comb2_index_changed(self):
        self.comb2_index = self.comboBox_2.currentIndex()
        self.comb2_hex = self.get_comb2_hex()
        self.update_hex_val()

    def comb3_index_changed(self):
        self.comb3_index = self.comboBox_3.currentIndex()
        self.comb3_hex = self.get_comb3_hex()
        self.update_hex_val()

    def get_val3to6_hex(self, index):
        val = self.valLineEdit_3.text()
        if index == 4:
            val = self.valLineEdit_4.text()
        elif index == 5:
            val = self.valLineEdit_5.text()
        elif index == 6:
            val = self.valLineEdit_6.text()
        hex_val = format(0, f"0{8 - len(val)}X") + val
        omit_hex = hex_val[4:]
        hex_val = hex_val[6:] + hex_val[4:6] + hex_val[2:4] + hex_val[0:2]
        return omit_hex, hex_val

    def val_text_changed(self):
        self.val1_hex = self.get_val1_hex()
        self.val2_hex = self.get_val2_hex()
        self.val3_omit_hex, self.val3_hex = self.get_val3to6_hex(3)
        self.val4_omit_hex, self.val4_hex = self.get_val3to6_hex(4)
        self.val5_omit_hex, self.val5_hex = self.get_val3to6_hex(5)
        self.val6_omit_hex, self.val6_hex = self.get_val3to6_hex(6)
        self.update_hex_val()

    # ------------ 生成动作ID -----------------------
    def generate_action_ID(self):
        # 得到最终的动作16进制编码
        self.config_hex = self.val1_hex + self.val2_hex + self.comb1_hex + self.val3_hex + self.val4_hex + \
                          self.val5_hex + self.val6_hex + self.comb2_hex + self.comb3_hex + self.backup_hex
        # print(f"生成的16进制参数配置: {self.config_hex}")
        self.action_id, self.is_new_action = get_action_id(self.config_hex, "C")
        # id显示到界面
        self.actionIDLineEdit.setText(self.action_id)

    # ------------ 提交 -----------------------
    def commit_config(self):
        # 发送信号(id的前两位和后两位要调换位置)
        self.config_hex_signal.emit(self.action_id[2:] + self.action_id[0:2] + self.config_hex, self.is_new_action)
        # 发送完关闭窗口
        self.close()