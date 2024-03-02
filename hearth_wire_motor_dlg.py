from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog

from ui.HearthWireMotor import Ui_HearthWireMotor
from utils.data_utils import *


class HearthWireMotorDlg(QDialog, Ui_HearthWireMotor):
    """
    1炉丝电机参数配置对话框
    """
    config_hex_signal = Signal(str, int)

    def __init__(self):
        super(HearthWireMotorDlg, self).__init__()
        # 是否是新ID
        self.is_new_action = None
        # 最终的16进制配置信息
        self.config_hex = None

        self.setupUi(self)
        # 读取参数配置
        config = get_config(1)
        # --------------------- 电机参数片选 ------------------
        self.motor_conf_1 = config["motor_conf_select"]["zhuan_ji_1"]
        self.motor_conf_2 = config["motor_conf_select"]["yang_ti_ji_2"]
        self.motor_conf_3 = config["motor_conf_select"]["lu_shang_ji_3"]
        self.motor_conf_4 = config["motor_conf_select"]["lu_zhong_ji_4"]
        self.motor_conf_5 = config["motor_conf_select"]["lu_xia_ji_5"]
        # 获取参数16进制编码
        self.motor_conf_hex = self.get_motor_conf_hex()
        # 电机参数片选复选框状态改变
        self.confCheckBox_1.stateChanged.connect(self.conf_1_state_changed)
        self.confCheckBox_2.stateChanged.connect(self.conf_2_state_changed)
        self.confCheckBox_3.stateChanged.connect(self.conf_3_state_changed)
        self.confCheckBox_4.stateChanged.connect(self.conf_4_state_changed)
        self.confCheckBox_5.stateChanged.connect(self.conf_5_state_changed)

        # ------------ 转机1参数动作设置 -------------------
        # 1.细分和方向
        self.zhuan_ji_1_forward_rotation = config["zhuan_ji_1_settings"]["subdivision_direction"]["forward_rotation"]
        self.zhuan_ji_1_backward_rotation = config["zhuan_ji_1_settings"]["subdivision_direction"]["backward_rotation"]
        self.zhuan_ji_1_two_four = config["zhuan_ji_1_settings"]["subdivision_direction"]["two_four"]
        self.zhuan_ji_1_two = config["zhuan_ji_1_settings"]["subdivision_direction"]["two"]
        self.zhuan_ji_1_four = config["zhuan_ji_1_settings"]["subdivision_direction"]["four"]
        self.zhuan_ji_1_eight = config["zhuan_ji_1_settings"]["subdivision_direction"]["eight"]
        self.zhuan_ji_1_tail = config["zhuan_ji_1_settings"]["subdivision_direction"]["tail"]
        # 下拉索引
        self.zhuan_ji_1_subdivision_index = 0
        self.zhuan_ji_1_direction_index = 0
        self.subdivisionComboBox_1.currentIndexChanged.connect(self.subdivision_1_index_changed)
        self.directionComboBox_1.currentIndexChanged.connect(self.direction_1_index_changed)
        # 得到16进制编码
        self.zhuan_ji_1_subdivision_direction_hex = self.get_zhuan_ji_1_subdivision_direction_hex()

        # 2.速度设置
        self.zhuan_ji_1_velocity_P = config["zhuan_ji_1_settings"]["velocity"]["P"]
        self.zhuan_ji_1_velocity_i = config["zhuan_ji_1_settings"]["velocity"]["i"]
        self.zhuan_ji_1_velocity_z1 = config["zhuan_ji_1_settings"]["velocity"]["z1"]
        self.zhuan_ji_1_velocity_z2 = config["zhuan_ji_1_settings"]["velocity"]["z2"]
        self.zhuan_ji_1_velocity_address_head = config["zhuan_ji_1_settings"]["velocity"]["address_head"]
        self.zhuan_ji_1_velocity_address_tail = config["zhuan_ji_1_settings"]["velocity"]["address_tail"]
        # 运动类别下拉索引
        self.type_1_index = 0
        # 单位下拉索引
        self.unit_1_index = 0
        # 输入框的值改变
        self.velocityLineEdit_1.textChanged.connect(self.velocity_1_text_changed)
        # 下拉框索引改变
        self.typeComboBox_1.currentIndexChanged.connect(self.type_1_index_changed)
        self.unitComboBox_1.currentIndexChanged.connect(self.unit_1_index_changed)
        # 得到速度对应的十六进制缩写和十六进制值
        self.zhuan_ji_1_velocity_omit_hex, self.zhuan_ji_1_velocity_hex = self.get_zhuan_ji_1_velocity_hex()

        # ------------ 样提机2参数动作设置 -------------------
        # 1.细分和方向
        self.yang_ti_ji_2_forward_rotation = config["yang_ti_ji_2_settings"]["subdivision_direction"][
            "forward_rotation"]
        self.yang_ti_ji_2_backward_rotation = config["yang_ti_ji_2_settings"]["subdivision_direction"][
            "backward_rotation"]
        self.yang_ti_ji_2_two_four = config["yang_ti_ji_2_settings"]["subdivision_direction"]["two_four"]
        self.yang_ti_ji_2_two = config["yang_ti_ji_2_settings"]["subdivision_direction"]["two"]
        self.yang_ti_ji_2_four = config["yang_ti_ji_2_settings"]["subdivision_direction"]["four"]
        self.yang_ti_ji_2_eight = config["yang_ti_ji_2_settings"]["subdivision_direction"]["eight"]
        self.yang_ti_ji_2_tail = config["yang_ti_ji_2_settings"]["subdivision_direction"]["tail"]
        # 下拉索引
        self.yang_ti_ji_2_subdivision_index = 0
        self.yang_ti_ji_2_direction_index = 0
        self.subdivisionComboBox_2.currentIndexChanged.connect(self.subdivision_2_index_changed)
        self.directionComboBox_2.currentIndexChanged.connect(self.direction_2_index_changed)
        # 得到16进制编码
        self.yang_ti_ji_2_subdivision_direction_hex = self.get_yang_ti_ji_2_subdivision_direction_hex()

        # 2.速度设置
        self.yang_ti_ji_2_velocity_P = config["yang_ti_ji_2_settings"]["velocity"]["P"]
        self.yang_ti_ji_2_velocity_i = config["yang_ti_ji_2_settings"]["velocity"]["i"]
        self.yang_ti_ji_2_velocity_z1 = config["yang_ti_ji_2_settings"]["velocity"]["z1"]
        self.yang_ti_ji_2_velocity_z2 = config["yang_ti_ji_2_settings"]["velocity"]["z2"]
        self.yang_ti_ji_2_velocity_address_head = config["yang_ti_ji_2_settings"]["velocity"]["address_head"]
        self.yang_ti_ji_2_velocity_address_tail = config["yang_ti_ji_2_settings"]["velocity"]["address_tail"]

        # 运动类别下拉索引
        self.type_2_index = 0
        # 单位下拉索引
        self.unit_2_index = 0
        # 输入框的值改变
        self.velocityLineEdit_2.textChanged.connect(self.velocity_2_text_changed)
        # 下拉框索引改变
        self.typeComboBox_2.currentIndexChanged.connect(self.type_2_index_changed)
        self.unitComboBox_2.currentIndexChanged.connect(self.unit_2_index_changed)
        # 得到速度对应的十六进制缩写和十六进制值
        self.yang_ti_ji_2_velocity_omit_hex, self.yang_ti_ji_2_velocity_hex = self.get_yang_ti_ji_2_velocity_hex()

        # ------------ 炉上机3参数设置 -------------------
        # 1.细分和方向
        self.lu_shang_ji_3_forward_rotation = config["lu_shang_ji_3_settings"]["subdivision_direction"][
            "forward_rotation"]
        self.lu_shang_ji_3_backward_rotation = config["lu_shang_ji_3_settings"]["subdivision_direction"][
            "backward_rotation"]
        self.lu_shang_ji_3_two_four = config["lu_shang_ji_3_settings"]["subdivision_direction"]["two_four"]
        self.lu_shang_ji_3_two = config["lu_shang_ji_3_settings"]["subdivision_direction"]["two"]
        self.lu_shang_ji_3_four = config["lu_shang_ji_3_settings"]["subdivision_direction"]["four"]
        self.lu_shang_ji_3_eight = config["lu_shang_ji_3_settings"]["subdivision_direction"]["eight"]
        self.lu_shang_ji_3_tail = config["lu_shang_ji_3_settings"]["subdivision_direction"]["tail"]

        # 下拉索引
        self.lu_shang_ji_3_subdivision_index = 0
        self.lu_shang_ji_3_direction_index = 0
        self.subdivisionComboBox_3.currentIndexChanged.connect(self.subdivision_3_index_changed)
        self.directionComboBox_3.currentIndexChanged.connect(self.direction_3_index_changed)
        # 得到16进制编码
        self.lu_shang_ji_3_subdivision_direction_hex = self.get_lu_shang_ji_3_subdivision_direction_hex()

        # 2.速度设置
        self.lu_shang_ji_3_velocity_P = config["lu_shang_ji_3_settings"]["velocity"]["P"]
        self.lu_shang_ji_3_velocity_i = config["lu_shang_ji_3_settings"]["velocity"]["i"]
        self.lu_shang_ji_3_velocity_z1 = config["lu_shang_ji_3_settings"]["velocity"]["z1"]
        self.lu_shang_ji_3_velocity_z2 = config["lu_shang_ji_3_settings"]["velocity"]["z2"]
        self.lu_shang_ji_3_velocity_address_head = config["lu_shang_ji_3_settings"]["velocity"]["address_head"]
        self.lu_shang_ji_3_velocity_address_tail = config["lu_shang_ji_3_settings"]["velocity"]["address_tail"]

        # 运动类别下拉索引
        self.type_3_index = 0
        # 单位下拉索引
        self.unit_3_index = 2
        # 输入框的值改变
        self.velocityLineEdit_3.textChanged.connect(self.velocity_3_text_changed)
        # 下拉框索引改变
        self.typeComboBox_3.currentIndexChanged.connect(self.type_3_index_changed)
        self.unitComboBox_3.currentIndexChanged.connect(self.unit_3_index_changed)
        # 得到速度对应的十六进制缩写和十六进制值
        self.lu_shang_ji_3_velocity_omit_hex, self.lu_shang_ji_3_velocity_hex = self.get_lu_shang_ji_3_velocity_hex()

        # ------------ 炉中机4参数设置 -------------------
        # 1.细分和方向
        self.lu_zhong_ji_4_forward_rotation = config["lu_zhong_ji_4_settings"]["subdivision_direction"][
            "forward_rotation"]
        self.lu_zhong_ji_4_backward_rotation = config["lu_zhong_ji_4_settings"]["subdivision_direction"][
            "backward_rotation"]
        self.lu_zhong_ji_4_two_four = config["lu_zhong_ji_4_settings"]["subdivision_direction"]["two_four"]
        self.lu_zhong_ji_4_two = config["lu_zhong_ji_4_settings"]["subdivision_direction"]["two"]
        self.lu_zhong_ji_4_four = config["lu_zhong_ji_4_settings"]["subdivision_direction"]["four"]
        self.lu_zhong_ji_4_eight = config["lu_zhong_ji_4_settings"]["subdivision_direction"]["eight"]
        self.lu_zhong_ji_4_tail = config["lu_zhong_ji_4_settings"]["subdivision_direction"]["tail"]

        # 下拉索引
        self.lu_zhong_ji_4_subdivision_index = 0
        self.lu_zhong_ji_4_direction_index = 0
        self.subdivisionComboBox_4.currentIndexChanged.connect(self.subdivision_4_index_changed)
        self.directionComboBox_4.currentIndexChanged.connect(self.direction_4_index_changed)
        # 得到16进制编码
        self.lu_zhong_ji_4_subdivision_direction_hex = self.get_lu_zhong_ji_4_subdivision_direction_hex()

        # 2.速度设置
        self.lu_zhong_ji_4_velocity_P = config["lu_zhong_ji_4_settings"]["velocity"]["P"]
        self.lu_zhong_ji_4_velocity_i = config["lu_zhong_ji_4_settings"]["velocity"]["i"]
        self.lu_zhong_ji_4_velocity_z1 = config["lu_zhong_ji_4_settings"]["velocity"]["z1"]
        self.lu_zhong_ji_4_velocity_z2 = config["lu_zhong_ji_4_settings"]["velocity"]["z2"]
        self.lu_zhong_ji_4_velocity_address_head = config["lu_zhong_ji_4_settings"]["velocity"]["address_head"]
        self.lu_zhong_ji_4_velocity_address_tail = config["lu_zhong_ji_4_settings"]["velocity"]["address_tail"]

        # 运动类别下拉索引
        self.type_4_index = 0
        # 单位下拉索引
        self.unit_4_index = 2
        # 输入框的值改变
        self.velocityLineEdit_4.textChanged.connect(self.velocity_4_text_changed)
        # 下拉框索引改变
        self.typeComboBox_4.currentIndexChanged.connect(self.type_4_index_changed)
        self.unitComboBox_4.currentIndexChanged.connect(self.unit_4_index_changed)
        # 得到速度对应的十六进制缩写和十六进制值
        self.lu_zhong_ji_4_velocity_omit_hex, self.lu_zhong_ji_4_velocity_hex = self.get_lu_zhong_ji_4_velocity_hex()

        # ------------ 炉下机5参数设置 -------------------
        # 1.细分和方向
        self.lu_xia_ji_5_forward_rotation = config["lu_xia_ji_5_settings"]["subdivision_direction"]["forward_rotation"]
        self.lu_xia_ji_5_backward_rotation = config["lu_xia_ji_5_settings"]["subdivision_direction"][
            "backward_rotation"]
        self.lu_xia_ji_5_two_four = config["lu_xia_ji_5_settings"]["subdivision_direction"]["two_four"]
        self.lu_xia_ji_5_two = config["lu_xia_ji_5_settings"]["subdivision_direction"]["two"]
        self.lu_xia_ji_5_four = config["lu_xia_ji_5_settings"]["subdivision_direction"]["four"]
        self.lu_xia_ji_5_eight = config["lu_xia_ji_5_settings"]["subdivision_direction"]["eight"]
        self.lu_xia_ji_5_tail = config["lu_xia_ji_5_settings"]["subdivision_direction"]["tail"]

        # 下拉索引
        self.lu_xia_ji_5_subdivision_index = 0
        self.lu_xia_ji_5_direction_index = 0
        self.subdivisionComboBox_5.currentIndexChanged.connect(self.subdivision_5_index_changed)
        self.directionComboBox_5.currentIndexChanged.connect(self.direction_5_index_changed)
        # 得到16进制编码
        self.lu_xia_ji_5_subdivision_direction_hex = self.get_lu_xia_ji_5_subdivision_direction_hex()

        # 2.速度设置
        self.lu_xia_ji_5_velocity_P = config["lu_xia_ji_5_settings"]["velocity"]["P"]
        self.lu_xia_ji_5_velocity_i = config["lu_xia_ji_5_settings"]["velocity"]["i"]
        self.lu_xia_ji_5_velocity_z1 = config["lu_xia_ji_5_settings"]["velocity"]["z1"]
        self.lu_xia_ji_5_velocity_z2 = config["lu_xia_ji_5_settings"]["velocity"]["z2"]
        self.lu_xia_ji_5_velocity_address_head = config["lu_xia_ji_5_settings"]["velocity"]["address_head"]
        self.lu_xia_ji_5_velocity_address_tail = config["lu_xia_ji_5_settings"]["velocity"]["address_tail"]

        # 运动类别下拉索引
        self.type_5_index = 0
        # 单位下拉索引
        self.unit_5_index = 2
        # 输入框的值改变
        self.velocityLineEdit_5.textChanged.connect(self.velocity_5_text_changed)
        # 下拉框索引改变
        self.typeComboBox_5.currentIndexChanged.connect(self.type_5_index_changed)
        self.unitComboBox_5.currentIndexChanged.connect(self.unit_5_index_changed)
        # 得到速度对应的十六进制缩写和十六进制值
        self.lu_xia_ji_5_velocity_omit_hex, self.lu_xia_ji_5_velocity_hex = self.get_lu_xia_ji_5_velocity_hex()

        # --------------------- 电机失步检测使能设置 ------------------
        self.motor_enable_1 = config["motor_enable_settings"]["zhuan_ji_1"]
        self.motor_enable_2 = config["motor_enable_settings"]["yang_ti_ji_2"]
        self.motor_enable_3 = config["motor_enable_settings"]["lu_shang_ji_3"]
        self.motor_enable_4 = config["motor_enable_settings"]["lu_zhong_ji_4"]
        self.motor_enable_5 = config["motor_enable_settings"]["lu_xia_ji_5"]
        self.motor_enable_tail = config["motor_enable_settings"]["tail"]
        # 获取参数16进制编码
        self.motor_enable_omit_hex = self.get_motor_enable_hex()
        self.motor_enable_hex = self.motor_enable_omit_hex[2:] + self.motor_enable_omit_hex[
                                                                 0:2] + self.motor_enable_tail
        # 电机参数片选复选框状态改变
        self.enableCheckBox_1.stateChanged.connect(self.enable_1_state_changed)
        self.enableCheckBox_2.stateChanged.connect(self.enable_2_state_changed)
        self.enableCheckBox_3.stateChanged.connect(self.enable_3_state_changed)
        self.enableCheckBox_4.stateChanged.connect(self.enable_4_state_changed)
        self.enableCheckBox_5.stateChanged.connect(self.enable_5_state_changed)

        # 更新界面参数
        self.update_hex_val()

        # 存放最后生成的动作id
        self.action_id = ""
        # 生成动作ID按钮
        self.generateIDPushButton.clicked.connect(self.generate_action_ID)

        # 确定按钮
        self.commitPushButton.clicked.connect(self.commit_config)

    def get_motor_conf_hex(self):
        val = self.motor_conf_5 + self.motor_conf_4 + self.motor_conf_3 + self.motor_conf_2 + self.motor_conf_1
        return format(int("1100" + val + "00", 2), '04X')  # 二进制字符串转16进制

    def update_hex_val(self):
        """
        将16进制缩写和16进制的值在界面上更新
        :return:
        """
        # 电机参数片选
        self.hexLineEdit_1.setText(self.motor_conf_hex[2:] + self.motor_conf_hex[0:2])
        # 转机1细分和方向
        self.hexLineEdit_2.setText(self.zhuan_ji_1_subdivision_direction_hex)
        # 转机1速度
        self.hexLineEdit_3.setText(self.zhuan_ji_1_velocity_hex)
        self.hexOmitLineEdit_3.setText(self.zhuan_ji_1_velocity_omit_hex)
        # 样提机2细分和方向
        self.hexLineEdit_4.setText(self.yang_ti_ji_2_subdivision_direction_hex)
        # 样提机2速度
        self.hexLineEdit_5.setText(self.yang_ti_ji_2_velocity_hex)
        self.hexOmitLineEdit_5.setText(self.yang_ti_ji_2_velocity_omit_hex)
        # 炉上机3细分和方向
        self.hexLineEdit_6.setText(self.lu_shang_ji_3_subdivision_direction_hex)
        # 炉上机3速度
        self.hexLineEdit_7.setText(self.lu_shang_ji_3_velocity_hex)
        self.hexOmitLineEdit_7.setText(self.lu_shang_ji_3_velocity_omit_hex)
        # 炉中机4细分和方向
        self.hexLineEdit_8.setText(self.lu_zhong_ji_4_subdivision_direction_hex)
        # 炉中机4速度
        self.hexLineEdit_9.setText(self.lu_zhong_ji_4_velocity_hex)
        self.hexOmitLineEdit_9.setText(self.lu_zhong_ji_4_velocity_omit_hex)
        # 炉下机5细分和方向
        self.hexLineEdit_10.setText(self.lu_xia_ji_5_subdivision_direction_hex)
        # 炉下机5速度
        self.hexLineEdit_11.setText(self.lu_xia_ji_5_velocity_hex)
        self.hexOmitLineEdit_11.setText(self.lu_xia_ji_5_velocity_omit_hex)
        # 电机失步使能
        self.hexLineEdit_12.setText(self.motor_enable_hex)
        self.hexOmitLineEdit_12.setText(self.motor_enable_omit_hex)

    # ------------- 电机参数复选框状态改变 --------------------
    def conf_1_state_changed(self, state):
        if state == 2:
            self.motor_conf_1 = "11"
        else:
            self.motor_conf_1 = "00"
        # 获取配置参数的16进制编码
        self.motor_conf_hex = self.get_motor_conf_hex()
        # 更新界面所展示的值
        self.update_hex_val()

    def conf_2_state_changed(self, state):
        if state == 2:
            self.motor_conf_2 = "11"
        else:
            self.motor_conf_2 = "00"
        # 获取配置参数的16进制编码
        self.motor_conf_hex = self.get_motor_conf_hex()
        # 更新界面所展示的值
        self.update_hex_val()

    def conf_3_state_changed(self, state):
        if state == 2:
            self.motor_conf_3 = "11"
        else:
            self.motor_conf_3 = "00"
        # 获取配置参数的16进制编码
        self.motor_conf_hex = self.get_motor_conf_hex()
        # 更新界面所展示的值
        self.update_hex_val()

    def conf_4_state_changed(self, state):
        if state == 2:
            self.motor_conf_4 = "11"
        else:
            self.motor_conf_4 = "00"
        # 获取配置参数的16进制编码
        self.motor_conf_hex = self.get_motor_conf_hex()
        # 更新界面所展示的值
        self.update_hex_val()

    def conf_5_state_changed(self, state):
        if state == 2:
            self.motor_conf_5 = "11"
        else:
            self.motor_conf_5 = "00"
        # 获取配置参数的16进制编码
        self.motor_conf_hex = self.get_motor_conf_hex()
        # 更新界面所展示的值
        self.update_hex_val()

    # ------------------- 转机1 ---------------------------
    def get_zhuan_ji_1_subdivision_direction_hex(self):
        subdivision = self.zhuan_ji_1_two_four
        rotation = self.zhuan_ji_1_forward_rotation
        if self.zhuan_ji_1_direction_index == 1:
            rotation = self.zhuan_ji_1_backward_rotation
        if self.zhuan_ji_1_subdivision_index == 1:
            subdivision = self.zhuan_ji_1_two
        elif self.zhuan_ji_1_subdivision_index == 2:
            subdivision = self.zhuan_ji_1_four
        elif self.zhuan_ji_1_subdivision_index == 3:
            subdivision = self.zhuan_ji_1_eight
        return subdivision + rotation + self.zhuan_ji_1_tail

    # 转机1下拉框索引改变
    def subdivision_1_index_changed(self):
        self.zhuan_ji_1_subdivision_index = self.subdivisionComboBox_1.currentIndex()
        self.zhuan_ji_1_subdivision_direction_hex = self.get_zhuan_ji_1_subdivision_direction_hex()
        self.update_hex_val()

    def direction_1_index_changed(self):
        self.zhuan_ji_1_direction_index = self.directionComboBox_1.currentIndex()
        self.zhuan_ji_1_subdivision_direction_hex = self.get_zhuan_ji_1_subdivision_direction_hex()
        self.update_hex_val()

    def get_zhuan_ji_1_velocity_hex(self):
        """
        根据公式计算速度对应的16进制值
        :return: 十六进制缩写，十六进制值
        """
        # 默认单位mm/s，只有直线运动才改变单位值
        V1 = float(self.velocityLineEdit_1.text())
        if self.unit_1_index == 1 and self.type_1_index == 0:
            # mm/min
            V1 = V1 / 60
        elif self.unit_1_index == 2 and self.type_1_index == 0:
            # mm/H
            V1 = V1 / 3600

        if self.type_1_index == 0:
            # 直线运动
            F = ((V1 / (self.zhuan_ji_1_velocity_P / self.zhuan_ji_1_velocity_i)) / (
                        self.zhuan_ji_1_velocity_z1 / self.zhuan_ji_1_velocity_z2)) * 200
        else:
            # 圆周运动
            F = (V1 / (self.zhuan_ji_1_velocity_z1 / self.zhuan_ji_1_velocity_z2)) / (
                        1 / self.zhuan_ji_1_velocity_i) / 1.8

        # 保留小数点后8位，不然对不上
        data = round((((1024 * 1000) / F) / 2) - 1, 8)
        hex_val = format(int(data), '08X')
        hex_val_address = hex_val[2:4] + hex_val[0:2] + self.zhuan_ji_1_velocity_address_head + hex_val[6:8] + hex_val[
                                                                                                               4:6] + self.zhuan_ji_1_velocity_address_tail
        return hex_val, hex_val_address

    def velocity_1_text_changed(self):
        """
        转机1速度输入框的值改变
        """
        self.zhuan_ji_1_velocity_omit_hex, self.zhuan_ji_1_velocity_hex = self.get_zhuan_ji_1_velocity_hex()
        self.update_hex_val()

    def type_1_index_changed(self):
        """
        转机1运动类别下拉框索引改变
        """
        self.type_1_index = self.typeComboBox_1.currentIndex()
        self.zhuan_ji_1_velocity_omit_hex, self.zhuan_ji_1_velocity_hex = self.get_zhuan_ji_1_velocity_hex()
        self.update_hex_val()

    def unit_1_index_changed(self):
        """
        转机1单位下拉框索引改变
        """
        self.unit_1_index = self.unitComboBox_1.currentIndex()
        self.zhuan_ji_1_velocity_omit_hex, self.zhuan_ji_1_velocity_hex = self.get_zhuan_ji_1_velocity_hex()
        self.update_hex_val()

    # ------------------- 样提机2 ---------------------------
    def get_yang_ti_ji_2_subdivision_direction_hex(self):
        subdivision = self.yang_ti_ji_2_two_four
        rotation = self.yang_ti_ji_2_forward_rotation
        if self.yang_ti_ji_2_direction_index == 1:
            rotation = self.yang_ti_ji_2_backward_rotation
        if self.yang_ti_ji_2_subdivision_index == 1:
            subdivision = self.yang_ti_ji_2_two
        elif self.yang_ti_ji_2_subdivision_index == 2:
            subdivision = self.yang_ti_ji_2_four
        elif self.yang_ti_ji_2_subdivision_index == 3:
            subdivision = self.yang_ti_ji_2_eight
        return subdivision + rotation + self.yang_ti_ji_2_tail

    # 转机1下拉框索引改变
    def subdivision_2_index_changed(self):
        self.yang_ti_ji_2_subdivision_index = self.subdivisionComboBox_2.currentIndex()
        self.yang_ti_ji_2_subdivision_direction_hex = self.get_yang_ti_ji_2_subdivision_direction_hex()
        self.update_hex_val()

    def direction_2_index_changed(self):
        self.yang_ti_ji_2_direction_index = self.directionComboBox_2.currentIndex()
        self.yang_ti_ji_2_subdivision_direction_hex = self.get_yang_ti_ji_2_subdivision_direction_hex()
        self.update_hex_val()

    def get_yang_ti_ji_2_velocity_hex(self):
        """
        根据公式计算速度对应的16进制值
        :return: 十六进制缩写，十六进制值
        """
        # 默认单位mm/s，只有直线运动才改变单位值
        V1 = float(self.velocityLineEdit_2.text())
        if self.unit_2_index == 1 and self.type_2_index == 0:
            # mm/min
            V1 = V1 / 60
        elif self.unit_2_index == 2 and self.type_2_index == 0:
            # mm/H
            V1 = V1 / 3600

        if self.type_2_index == 0:
            # 直线运动
            F = ((V1 / (self.yang_ti_ji_2_velocity_P / self.yang_ti_ji_2_velocity_i)) / (
                        self.yang_ti_ji_2_velocity_z1 / self.yang_ti_ji_2_velocity_z2)) * 200
        else:
            # 圆周运动
            F = (V1 / (self.yang_ti_ji_2_velocity_z1 / self.yang_ti_ji_2_velocity_z2)) / (
                        1 / self.yang_ti_ji_2_velocity_i) / 1.8

        # 保留小数点后8位，不然对不上
        data = round((((1024 * 1000) / F) / 2) - 1, 8)
        hex_val = format(int(data), '08X')
        hex_val_address = hex_val[2:4] + hex_val[0:2] + self.yang_ti_ji_2_velocity_address_head + hex_val[6:8] + hex_val[4:6] + self.yang_ti_ji_2_velocity_address_tail
        return hex_val, hex_val_address

    def velocity_2_text_changed(self):
        """
        转机1速度输入框的值改变
        """
        self.yang_ti_ji_2_velocity_omit_hex, self.yang_ti_ji_2_velocity_hex = self.get_yang_ti_ji_2_velocity_hex()
        self.update_hex_val()

    def type_2_index_changed(self):
        """
        转机1运动类别下拉框索引改变
        """
        self.type_2_index = self.typeComboBox_2.currentIndex()
        self.yang_ti_ji_2_velocity_omit_hex, self.yang_ti_ji_2_velocity_hex = self.get_yang_ti_ji_2_velocity_hex()
        self.update_hex_val()

    def unit_2_index_changed(self):
        """
        转机1单位下拉框索引改变
        """
        self.unit_2_index = self.unitComboBox_2.currentIndex()
        self.yang_ti_ji_2_velocity_omit_hex, self.yang_ti_ji_2_velocity_hex = self.get_yang_ti_ji_2_velocity_hex()
        self.update_hex_val()

    # ------------------- 炉上机3 ---------------------------
    def get_lu_shang_ji_3_subdivision_direction_hex(self):
        subdivision = self.lu_shang_ji_3_two_four
        rotation = self.lu_shang_ji_3_forward_rotation
        if self.lu_shang_ji_3_direction_index == 1:
            rotation = self.lu_shang_ji_3_backward_rotation
        if self.lu_shang_ji_3_subdivision_index == 1:
            subdivision = self.lu_shang_ji_3_two
        elif self.lu_shang_ji_3_subdivision_index == 2:
            subdivision = self.lu_shang_ji_3_four
        elif self.lu_shang_ji_3_subdivision_index == 3:
            subdivision = self.lu_shang_ji_3_eight
        return subdivision + rotation + self.lu_shang_ji_3_tail

    # 炉上机3下拉框索引改变
    def subdivision_3_index_changed(self):
        self.lu_shang_ji_3_subdivision_index = self.subdivisionComboBox_3.currentIndex()
        self.lu_shang_ji_3_subdivision_direction_hex = self.get_lu_shang_ji_3_subdivision_direction_hex()
        self.update_hex_val()

    def direction_3_index_changed(self):
        self.lu_shang_ji_3_direction_index = self.directionComboBox_3.currentIndex()
        self.lu_shang_ji_3_subdivision_direction_hex = self.get_lu_shang_ji_3_subdivision_direction_hex()
        self.update_hex_val()

    def get_lu_shang_ji_3_velocity_hex(self):
        """
        根据公式计算速度对应的16进制值
        :return: 十六进制缩写，十六进制值
        """
        # 默认单位mm/s，只有直线运动才改变单位值
        V1 = float(self.velocityLineEdit_3.text())
        if self.unit_3_index == 1 and self.type_3_index == 0:
            # mm/min
            V1 = V1 / 60
        elif self.unit_3_index == 2 and self.type_3_index == 0:
            # mm/H
            V1 = V1 / 3600

        if self.type_3_index == 0:
            # 直线运动
            F = ((V1 / (self.lu_shang_ji_3_velocity_P / self.lu_shang_ji_3_velocity_i)) / (
                        self.lu_shang_ji_3_velocity_z1 / self.lu_shang_ji_3_velocity_z2)) * 1600
        else:
            # 圆周运动
            F = (V1 / (self.lu_shang_ji_3_velocity_z1 / self.lu_shang_ji_3_velocity_z2)) / (
                        1 / self.lu_shang_ji_3_velocity_i) / 1.8

        # 保留小数点后8位，不然对不上
        data = round((((1024 * 1000) / F) / 2) - 1, 8)
        hex_val = format(int(data), '08X')
        hex_val_address = hex_val[2:4] + hex_val[0:2] + self.lu_shang_ji_3_velocity_address_head + hex_val[6:8] + hex_val[4:6] + self.lu_shang_ji_3_velocity_address_tail
        return hex_val, hex_val_address

    def velocity_3_text_changed(self):
        """
        炉上机3速度输入框的值改变
        """
        self.lu_shang_ji_3_velocity_omit_hex, self.lu_shang_ji_3_velocity_hex = self.get_lu_shang_ji_3_velocity_hex()
        self.update_hex_val()

    def type_3_index_changed(self):
        """
        炉上机3运动类别下拉框索引改变
        """
        self.type_3_index = self.typeComboBox_3.currentIndex()
        self.lu_shang_ji_3_velocity_omit_hex, self.lu_shang_ji_3_velocity_hex = self.get_lu_shang_ji_3_velocity_hex()
        self.update_hex_val()

    def unit_3_index_changed(self):
        """
        炉上机3单位下拉框索引改变
        """
        self.unit_3_index = self.unitComboBox_3.currentIndex()
        self.lu_shang_ji_3_velocity_omit_hex, self.lu_shang_ji_3_velocity_hex = self.get_lu_shang_ji_3_velocity_hex()
        self.update_hex_val()

    # ------------------- 炉中机4 ---------------------------
    def get_lu_zhong_ji_4_subdivision_direction_hex(self):
        subdivision = self.lu_zhong_ji_4_two_four
        rotation = self.lu_zhong_ji_4_forward_rotation
        if self.lu_zhong_ji_4_direction_index == 1:
            rotation = self.lu_zhong_ji_4_backward_rotation
        if self.lu_zhong_ji_4_subdivision_index == 1:
            subdivision = self.lu_zhong_ji_4_two
        elif self.lu_zhong_ji_4_subdivision_index == 2:
            subdivision = self.lu_zhong_ji_4_four
        elif self.lu_zhong_ji_4_subdivision_index == 3:
            subdivision = self.lu_zhong_ji_4_eight
        return subdivision + rotation + self.lu_zhong_ji_4_tail

    # 炉上机3下拉框索引改变
    def subdivision_4_index_changed(self):
        self.lu_zhong_ji_4_subdivision_index = self.subdivisionComboBox_4.currentIndex()
        self.lu_zhong_ji_4_subdivision_direction_hex = self.get_lu_zhong_ji_4_subdivision_direction_hex()
        self.update_hex_val()

    def direction_4_index_changed(self):
        self.lu_zhong_ji_4_direction_index = self.directionComboBox_4.currentIndex()
        self.lu_zhong_ji_4_subdivision_direction_hex = self.get_lu_zhong_ji_4_subdivision_direction_hex()
        self.update_hex_val()

    def get_lu_zhong_ji_4_velocity_hex(self):
        """
        根据公式计算速度对应的16进制值
        :return: 十六进制缩写，十六进制值
        """
        # 默认单位mm/s，只有直线运动才改变单位值
        V1 = float(self.velocityLineEdit_4.text())
        if self.unit_4_index == 1 and self.type_4_index == 0:
            # mm/min
            V1 = V1 / 60
        elif self.unit_4_index == 2 and self.type_4_index == 0:
            # mm/H
            V1 = V1 / 3600

        if self.type_4_index == 0:
            # 直线运动
            F = ((V1 / (self.lu_zhong_ji_4_velocity_P / self.lu_zhong_ji_4_velocity_i)) / (
                    self.lu_zhong_ji_4_velocity_z1 / self.lu_zhong_ji_4_velocity_z2)) * 1600
        else:
            # 圆周运动
            F = (V1 / (self.lu_zhong_ji_4_velocity_z1 / self.lu_zhong_ji_4_velocity_z2)) / (
                    1 / self.lu_zhong_ji_4_velocity_i) / 1.8

        # 保留小数点后8位，不然对不上
        data = round((((1024 * 1000) / F) / 2) - 1, 8)
        hex_val = format(int(data), '08X')
        hex_val_address = hex_val[2:4] + hex_val[0:2] + self.lu_zhong_ji_4_velocity_address_head + hex_val[
                                                                                                   6:8] + hex_val[
                                                                                                          4:6] + self.lu_zhong_ji_4_velocity_address_tail
        return hex_val, hex_val_address

    def velocity_4_text_changed(self):
        """
        炉上机3速度输入框的值改变
        """
        self.lu_zhong_ji_4_velocity_omit_hex, self.lu_zhong_ji_4_velocity_hex = self.get_lu_zhong_ji_4_velocity_hex()
        self.update_hex_val()

    def type_4_index_changed(self):
        """
        炉上机3运动类别下拉框索引改变
        """
        self.type_4_index = self.typeComboBox_4.currentIndex()
        self.lu_zhong_ji_4_velocity_omit_hex, self.lu_zhong_ji_4_velocity_hex = self.get_lu_zhong_ji_4_velocity_hex()
        self.update_hex_val()

    def unit_4_index_changed(self):
        """
        炉上机3单位下拉框索引改变
        """
        self.unit_4_index = self.unitComboBox_4.currentIndex()
        self.lu_zhong_ji_4_velocity_omit_hex, self.lu_zhong_ji_4_velocity_hex = self.get_lu_zhong_ji_4_velocity_hex()
        self.update_hex_val()

    # ------------------- 炉下机5 ---------------------------
    def get_lu_xia_ji_5_subdivision_direction_hex(self):
        subdivision = self.lu_xia_ji_5_two_four
        rotation = self.lu_xia_ji_5_forward_rotation
        if self.lu_xia_ji_5_direction_index == 1:
            rotation = self.lu_xia_ji_5_backward_rotation
        if self.lu_xia_ji_5_subdivision_index == 1:
            subdivision = self.lu_xia_ji_5_two
        elif self.lu_xia_ji_5_subdivision_index == 2:
            subdivision = self.lu_xia_ji_5_four
        elif self.lu_xia_ji_5_subdivision_index == 3:
            subdivision = self.lu_xia_ji_5_eight
        return subdivision + rotation + self.lu_xia_ji_5_tail

    # 炉上机3下拉框索引改变
    def subdivision_5_index_changed(self):
        self.lu_xia_ji_5_subdivision_index = self.subdivisionComboBox_5.currentIndex()
        self.lu_xia_ji_5_subdivision_direction_hex = self.get_lu_xia_ji_5_subdivision_direction_hex()
        self.update_hex_val()

    def direction_5_index_changed(self):
        self.lu_xia_ji_5_direction_index = self.directionComboBox_5.currentIndex()
        self.lu_xia_ji_5_subdivision_direction_hex = self.get_lu_xia_ji_5_subdivision_direction_hex()
        self.update_hex_val()

    def get_lu_xia_ji_5_velocity_hex(self):
        """
        根据公式计算速度对应的16进制值
        :return: 十六进制缩写，十六进制值
        """
        # 默认单位mm/s，只有直线运动才改变单位值
        V1 = float(self.velocityLineEdit_5.text())
        if self.unit_5_index == 1 and self.type_5_index == 0:
            # mm/min
            V1 = V1 / 60
        elif self.unit_5_index == 2 and self.type_5_index == 0:
            # mm/H
            V1 = V1 / 3600

        if self.type_5_index == 0:
            # 直线运动
            F = ((V1 / (self.lu_xia_ji_5_velocity_P / self.lu_xia_ji_5_velocity_i)) / (
                    self.lu_xia_ji_5_velocity_z1 / self.lu_xia_ji_5_velocity_z2)) * 1600
        else:
            # 圆周运动
            F = (V1 / (self.lu_xia_ji_5_velocity_z1 / self.lu_xia_ji_5_velocity_z2)) / (
                    1 / self.lu_xia_ji_5_velocity_i) / 1.8

        # 保留小数点后8位，不然对不上
        data = round((((1024 * 1000) / F) / 2) - 1, 8)
        hex_val = format(int(data), '08X')
        hex_val_address = hex_val[2:4] + hex_val[0:2] + self.lu_xia_ji_5_velocity_address_head + hex_val[6:8] + hex_val[
                                                                                                                4:6] + self.lu_xia_ji_5_velocity_address_tail
        return hex_val, hex_val_address

    def velocity_5_text_changed(self):
        """
        炉上机3速度输入框的值改变
        """
        self.lu_xia_ji_5_velocity_omit_hex, self.lu_xia_ji_5_velocity_hex = self.get_lu_xia_ji_5_velocity_hex()
        self.update_hex_val()

    def type_5_index_changed(self):
        """
        炉上机3运动类别下拉框索引改变
        """
        self.type_5_index = self.typeComboBox_5.currentIndex()
        self.lu_xia_ji_5_velocity_omit_hex, self.lu_xia_ji_5_velocity_hex = self.get_lu_xia_ji_5_velocity_hex()
        self.update_hex_val()

    def unit_5_index_changed(self):
        """
        炉上机3单位下拉框索引改变
        """
        self.unit_5_index = self.unitComboBox_5.currentIndex()
        self.lu_xia_ji_5_velocity_omit_hex, self.lu_xia_ji_5_velocity_hex = self.get_lu_xia_ji_5_velocity_hex()
        self.update_hex_val()

    # ----------------- 电机失步测试使能 ----------------------
    def get_motor_enable_hex(self):
        val = self.motor_enable_5 + self.motor_enable_4 + self.motor_enable_3 + self.motor_enable_2 + self.motor_enable_1
        return format(int("000000" + val, 2), '04X')  # 二进制字符串转16进制

    def enable_1_state_changed(self, state):
        if state == 2:
            self.motor_enable_1 = "11"
        else:
            self.motor_enable_1 = "00"
        # 获取配置参数的16进制编码
        self.motor_enable_omit_hex = self.get_motor_enable_hex()
        self.motor_enable_hex = self.motor_enable_omit_hex[2:] + self.motor_enable_omit_hex[
                                                                 0:2] + self.motor_enable_tail
        # 更新界面所展示的值
        self.update_hex_val()

    def enable_2_state_changed(self, state):
        if state == 2:
            self.motor_enable_2 = "11"
        else:
            self.motor_enable_2 = "00"
        # 获取配置参数的16进制编码
        self.motor_enable_omit_hex = self.get_motor_enable_hex()
        self.motor_enable_hex = self.motor_enable_omit_hex[2:] + self.motor_enable_omit_hex[
                                                                 0:2] + self.motor_enable_tail
        # 更新界面所展示的值
        self.update_hex_val()

    def enable_3_state_changed(self, state):
        if state == 2:
            self.motor_enable_3 = "11"
        else:
            self.motor_enable_3 = "00"
        # 获取配置参数的16进制编码
        self.motor_enable_omit_hex = self.get_motor_enable_hex()
        self.motor_enable_hex = self.motor_enable_omit_hex[2:] + self.motor_enable_omit_hex[
                                                                 0:2] + self.motor_enable_tail
        # 更新界面所展示的值
        self.update_hex_val()

    def enable_4_state_changed(self, state):
        if state == 2:
            self.motor_enable_4 = "11"
        else:
            self.motor_enable_4 = "00"
        # 获取配置参数的16进制编码
        self.motor_enable_omit_hex = self.get_motor_enable_hex()
        self.motor_enable_hex = self.motor_enable_omit_hex[2:] + self.motor_enable_omit_hex[
                                                                 0:2] + self.motor_enable_tail
        # 更新界面所展示的值
        self.update_hex_val()

    def enable_5_state_changed(self, state):
        if state == 2:
            self.motor_enable_5 = "11"
        else:
            self.motor_enable_5 = "00"
        # 获取配置参数的16进制编码
        self.motor_enable_omit_hex = self.get_motor_enable_hex()
        self.motor_enable_hex = self.motor_enable_omit_hex[2:] + self.motor_enable_omit_hex[
                                                                 0:2] + self.motor_enable_tail
        # 更新界面所展示的值
        self.update_hex_val()

    # ------------- 生成动作ID ----------------
    def generate_action_ID(self):
        # 得到最终的动作16进制编码
        self.config_hex = self.motor_conf_hex[2:] + self.motor_conf_hex[0:2] + self.zhuan_ji_1_subdivision_direction_hex + self.zhuan_ji_1_velocity_hex + \
                          self.yang_ti_ji_2_subdivision_direction_hex + self.yang_ti_ji_2_velocity_hex + \
                          self.lu_shang_ji_3_subdivision_direction_hex + self.lu_shang_ji_3_velocity_hex + \
                          self.lu_zhong_ji_4_subdivision_direction_hex + self.lu_zhong_ji_4_velocity_hex + \
                          self.lu_xia_ji_5_subdivision_direction_hex + self.lu_xia_ji_5_velocity_hex + \
                          self.motor_enable_hex
        # print(f"生成的16进制参数配置: {self.config_hex}")
        self.action_id, self.is_new_action = get_action_id(self.config_hex, 1)
        # id显示到界面
        self.actionIDLineEdit.setText(self.action_id)

    # ------------ 提交 -----------------------
    def commit_config(self):
        # 发送信号(id的前两位和后两位要调换位置)
        self.config_hex_signal.emit(self.action_id[2:] + self.action_id[0:2] + self.config_hex, self.is_new_action)
        # 发送完关闭窗口
        self.close()
