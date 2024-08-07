import os
import sys
from PySide6 import QtWidgets
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog, QTableWidgetItem, QMessageBox, QFileDialog

from StaticTableDlg import StaticTableDlg
from TotalTableDlg import TotalTableDlg
from ui.MainWindow import Ui_MainWindow
from ui.NewFlowItem import Ui_NewFlowItem

from furnace_switch_dlg import FurnaceSwitchDlg
from hearth_wire_motor_dlg import HearthWireMotorDlg
from transfer1_dlg import Transfer1Dlg
from sample2_dlg import Sample2Dlg
from stove3_dlg import Stove3Dlg
from stove4_dlg import Stove4Dlg
from stove5_dlg import Stove5Dlg
from motor_status_inquiry_dlg import MotorStatusInquiryDlg
from magnetic_field_dlg import MagneticFieldDlg
from motor_magnetic_field_current_dlg import MotorMagneticFieldCurrentDlg
from furnace_wire_heating_dlg import FurnaceWireHeatingDlg
from PID_Temperature_control_dlg import PIDTemperatureControlDlg
from online_monitoring_status_dlg import OnlineMonitoringStatusDlg
from motor_closing_dlg import MotorClosingDlg
from online_monitoring_head_dlg import OnlineMonitoringHeadDlg
from PID_config_settings_dlg import PIDConfigSettingsDlg
from utils.data_utils import hex_string_to_binary_file, clear_data, load_action_bin_to_data
from db_utils import *


class FlowItem:
    """
    实验流程项类，定义了实验流程表中一行的参数信息
    """
    def __init__(self):
        # 起始时刻
        self.startTime = 0
        # 动作起始条件
        self.startCondition = ""
        # 动作名称与描述
        self.descText = ""
        # 动作结束判据
        self.endCriterion = ""
        # 本动作多长时间后下一个动作
        self.interval = 0
        # 动作时间
        self.duration = 0
        # 备注
        self.remark = ""
        # 动作ID
        self.actionID = ""
        # 动作参数的16进制编码
        self.config_hex = ""
        # 是否是新动作
        self.is_new_action = 0


class NewFlowItemDlg(QDialog, Ui_NewFlowItem):
    """
    点击新建实验流程项弹出的对话框
    """

    # 创建信号
    flow_item_signal = Signal(object)

    def __init__(self):
        super(NewFlowItemDlg, self).__init__()
        # 判断是否是新动作
        self.is_new_action = 0
        # 存放动作参数配置的16进制编码
        self.config_hex = ""
        # 存放动作表信息
        self.action_startTime = None
        self.action_actionID = ''
        self.action_duration = None

        self.setupUi(self)
        # 记录当前动作的索引
        self.currentIndex = self.actionComboBox.currentIndex()
        # 点击创建动作按钮
        self.createActionPushButton.clicked.connect(self.show_action_config_dialog)
        # 下拉框索引改变
        self.actionComboBox.currentIndexChanged.connect(self.changeCurrentIndex)
        # 点击确定按钮
        self.confirmPushButton.clicked.connect(self.commitFlowItem)
        # 流程项对象
        self.flow_item = FlowItem()

    def commitFlowItem(self):
        """
        提交实验流程项，封装成对象发送给主窗口展示，同时把动作起始时刻、动作ID、动作时间保存到数据库
        :return:
        """
        # 封装流程项信息
        self.flow_item.startTime = self.startTimeLineEdit.text()
        self.flow_item.startCondition = self.startConditionLineEdit.text()
        self.flow_item.descText = self.descTextEdit.toPlainText()
        self.flow_item.endCriterion = self.endCriterionLineEdit.text()
        self.flow_item.interval = self.intervalLineEdit.text()
        self.flow_item.duration = self.durationLineEdit.text()
        self.flow_item.remark = self.remarkTextEdit.toPlainText()
        self.flow_item.actionID = self.actionIDLineEdit.text()
        self.flow_item.config_hex = self.config_hex
        self.flow_item.is_new_action = self.is_new_action

        # 把信息存入动态表
        self.action_startTime = int(self.flow_item.startTime)
        self.action_actionID = self.flow_item.actionID
        self.action_duration = int(self.flow_item.duration)
        # 创建数据库连接
        conn = create_connection()
        # 插入数据
        insert_experiment_flow(conn, self.action_startTime, self.action_actionID, self.action_duration)
        # 关闭数据库连接
        conn.close()
        # 发送信号
        self.flow_item_signal.emit(self.flow_item)
        # 发送完信号关闭
        self.close()

    def show_action_config_dialog(self):
        """
        打开动作参数配置对话框
        """
        if self.currentIndex == 0:
            dlg = FurnaceSwitchDlg()
            dlg.config_hex_signal.connect(self.get_config_hex_from_dlg)
            print("^^^^^^打开0炉子开关参数配置界面！")
            dlg.exec()
        elif self.currentIndex == 1:
            dlg = HearthWireMotorDlg()
            dlg.config_hex_signal.connect(self.get_config_hex_from_dlg)
            print("^^^^^^打开1炉丝电机参数配置界面！")
            dlg.exec()
        elif self.currentIndex == 2:
            dlg = Transfer1Dlg()
            dlg.config_hex_signal.connect(self.get_config_hex_from_dlg)
            print("^^^^^^打开转机1参数配置界面！")
            dlg.exec()
        elif self.currentIndex == 3:
            dlg = Sample2Dlg()
            dlg.config_hex_signal.connect(self.get_config_hex_from_dlg)
            print("^^^^^^打开样提机2参数配置界面！")
            dlg.exec()
        elif self.currentIndex == 4:
            dlg = Stove3Dlg()
            dlg.config_hex_signal.connect(self.get_config_hex_from_dlg)
            print("^^^^^^打开炉上机3参数配置界面！")
            dlg.exec()
        elif self.currentIndex == 5:
            dlg = Stove4Dlg()
            dlg.config_hex_signal.connect(self.get_config_hex_from_dlg)
            print("^^^^^^打开炉中机4参数配置界面！")
            dlg.exec()
        elif self.currentIndex == 6:
            dlg = Stove5Dlg()
            dlg.config_hex_signal.connect(self.get_config_hex_from_dlg)
            print("^^^^^^打开炉下机5参数配置界面！")
            dlg.exec()
        elif self.currentIndex == 7:
            dlg = MotorStatusInquiryDlg()
            dlg.config_hex_signal.connect(self.get_config_hex_from_dlg)
            print("^^^^^^打开电机状态查询参数配置界面！")
            dlg.exec()
        elif self.currentIndex == 8:
            dlg = MagneticFieldDlg()
            dlg.config_hex_signal.connect(self.get_config_hex_from_dlg)
            print("^^^^^^打开磁场参数配置界面！")
            dlg.exec()
        elif self.currentIndex == 9:
            dlg = MotorMagneticFieldCurrentDlg()
            dlg.config_hex_signal.connect(self.get_config_hex_from_dlg)
            print("^^^^^^打开电机磁场电流参数配置界面！")
            dlg.exec()
        elif self.currentIndex == 10:
            dlg = FurnaceWireHeatingDlg()
            dlg.config_hex_signal.connect(self.get_config_hex_from_dlg)
            print("^^^^^^打开炉丝加热电压参数配置界面！")
            dlg.exec()
        elif self.currentIndex == 11:
            dlg = PIDTemperatureControlDlg()
            dlg.config_hex_signal.connect(self.get_config_hex_from_dlg)
            print("^^^^^^打开PID控温曲线配置界面！")
            dlg.exec()
        elif self.currentIndex == 12:
            dlg = OnlineMonitoringStatusDlg()
            dlg.config_hex_signal.connect(self.get_config_hex_from_dlg)
            print("^^^^^^打开在线监控状态查询表！")
            dlg.exec()
        elif self.currentIndex == 13:
            dlg = MotorClosingDlg()
            dlg.config_hex_signal.connect(self.get_config_hex_from_dlg)
            print("^^^^^^电机关闭设置界面！")
            dlg.exec()
        elif self.currentIndex == 14:
            dlg = OnlineMonitoringHeadDlg()
            dlg.config_hex_signal.connect(self.get_config_hex_from_dlg)
            print("^^^^^^在线监控表头设置！")
            dlg.exec()
        elif self.currentIndex == 15:
            dlg = PIDConfigSettingsDlg()
            dlg.config_hex_signal.connect(self.get_config_hex_from_dlg)
            print("^^^^^^PID参数设置动作表！")
            dlg.exec()

    def changeCurrentIndex(self):
        """
        更新动作下拉框的索引
        """
        self.currentIndex = self.actionComboBox.currentIndex()

    def get_config_hex_from_dlg(self, config_hex, is_new_action):
        # 将动作ID展示到对话框上
        self.actionIDLineEdit.setText(config_hex[2:4] + config_hex[0:2])
        # 将动作参数的16进制编码保存下来
        self.config_hex = config_hex
        self.is_new_action = is_new_action


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """
    主窗口程序
    """
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # 点击新建流程项按钮
        self.newItemButton.clicked.connect(self.show_new_item_dialog)
        # 流程表项索引
        self.rowCount = 0
        # 流程表格样式设置
        self.flowTableWidget.resizeRowsToContents()
        # 存放新动作的16进制参数配置信息
        self.new_action_hex_list = []
        # 存放动态表的16进制配置信息
        self.dynamic_hex_list = []
        # 生成动作表
        self.pushButton_1.clicked.connect(self.generate_action_bin)
        # 生成动态表
        self.dynamic_id = None  # 动态表配置序号ID
        self.MAX_ACTION_NUM = 128  # 一个实验流程最大动作数
        self.pushButton_2.clicked.connect(self.generate_dynamic_bin)
        # 生成静态表
        self.pushButton_4.clicked.connect(self.show_generate_static_dialog)
        # 生成总表
        self.pushButton_5.clicked.connect(self.show_total_table_dialog)

        # 导入动作表的数据
        self.loadDataPushButton.clicked.connect(self.load_data)

    def load_data(self):
        """
        点击导入数据按钮：导入动作表数据
        :return:
        """
        # 创建文件选择对话框
        dialog = QFileDialog()

        # 设置对话框类型为选择文件
        dialog .setFileMode(QFileDialog.Directory)

        # 显示对话框并获取用户选择的目录
        selected_directory = dialog.getExistingDirectory(
            None, "选择文件目录", "", QFileDialog.ShowDirsOnly | QFileDialog.DontUseNativeDialog
        )
        # 用户选择了的有效目录
        if selected_directory:
            print("用户选择的目录:", selected_directory)
            # 清空原有的数据
            clear_data()
            print("》》》》》》》导入数据开始》》》》》》")
            # 导入新的数据
            load_action_bin_to_data(selected_directory + os.path.sep)
            print("》》》》》》》导入数据结束》》》》》》")
            QMessageBox.information(None, "Success", "导入成功！")

    def show_new_item_dialog(self):
        new_item_dlg = NewFlowItemDlg()
        # 添加实验流程项函数绑定
        new_item_dlg.flow_item_signal.connect(self.addNewFlowItem)
        new_item_dlg.exec()

    def addNewFlowItem(self, new_item):
        """
        往实验流程表中添加一行实验流程项
        :param new_item: 新建的实验流程项
        :return:
        """
        # 插入索引
        index_item = QTableWidgetItem(str(self.rowCount + 1))
        self.flowTableWidget.setItem(self.rowCount, 0, index_item)
        # 插入起始时间
        start_time_item = QTableWidgetItem(new_item.startTime)
        self.flowTableWidget.setItem(self.rowCount, 1, start_time_item)
        # 插入动作起始条件
        start_condition_item = QTableWidgetItem(new_item.startCondition)
        self.flowTableWidget.setItem(self.rowCount, 2, start_condition_item)
        # 插入动作名称与描述
        desc_text_item = QTableWidgetItem(new_item.descText)
        self.flowTableWidget.setItem(self.rowCount, 3, desc_text_item)
        # 插入动作结束判据
        end_criterion_item = QTableWidgetItem(new_item.endCriterion)
        self.flowTableWidget.setItem(self.rowCount, 4, end_criterion_item)
        # 插入多长时间后下一个动作
        interval_item = QTableWidgetItem(new_item.interval)
        self.flowTableWidget.setItem(self.rowCount, 5, interval_item)
        # 插入动作时间（s）
        duration_item = QTableWidgetItem(new_item.duration)
        self.flowTableWidget.setItem(self.rowCount, 6, duration_item)
        # 插入备注
        remark_item = QTableWidgetItem(new_item.remark)
        self.flowTableWidget.setItem(self.rowCount, 7, remark_item)
        # 插入动作ID
        action_ID_item = QTableWidgetItem(new_item.actionID)
        self.flowTableWidget.setItem(self.rowCount, 8, action_ID_item)
        # 是否是新动作
        is_new_action_item = QTableWidgetItem("是" if new_item.is_new_action == 1 else "否")
        self.flowTableWidget.setItem(self.rowCount, 9, is_new_action_item)
        # 更新行索引
        self.rowCount = self.rowCount + 1
        # 如果是新动作则保存配置信息
        if new_item.is_new_action == 1:
            self.new_action_hex_list.append(new_item.config_hex)
            print(f"所有新动作的参数配置：{self.new_action_hex_list}")

    def generate_action_bin(self):
        '''
        生成动作表的.bin文件
        :return: void
        '''
        # 去重
        self.new_action_hex_list = list(set(self.new_action_hex_list))
        if len(self.new_action_hex_list) == 0:
            QMessageBox.information(None, "Success", "没有新动作需要生成！")
            return
        # print(self.new_action_hex_list)
        # 文件夹不存在则创建
        base_path = os.path.abspath('./action_bin')
        if not os.path.exists(base_path):
            os.makedirs(base_path)
        for hex_str in self.new_action_hex_list:
            output_file_path = base_path + os.path.sep + 'AT_' + hex_str[2:4] + hex_str[0:2] + '.bin'
            hex_string_to_binary_file(hex_str, output_file_path)
        QMessageBox.information(None, "Success", f"新动作ID生成成功！\n文件所在目录：{base_path}")

    def show_generate_static_dialog(self):
        """
        点击生成静态表按钮，弹出对话框
        """
        dlg = StaticTableDlg()
        dlg.exec()
    def generate_dynamic_bin(self):
        '''
        生成动态表.bin文件
        :return: void
        '''
        if len(self.new_action_hex_list) == 0:
            QMessageBox.information(None, "Success", "没有动态表需要生成,请先生成动作表！")
            return
        # 创建数据库连接
        conn = create_connection()
        # 查询动态表配置序号dynamic_id(默认为0，自增)
        dynamic_num_record = fetch_dynamic_num_by_id(conn)
        if dynamic_num_record:
            self.dynamic_id = dynamic_num_record[1]
        self.dynamic_id += 1
        # 将 dynamic_id 格式化为四位数字
        format_id = format_four_digits(self.dynamic_id)
        # 将 dynamic_id 字符串反转
        reversed_dynamic_id = format_dynamic_id(format_id)
        # 将最大动作数转换为十六进制并反转
        max_action_hex = format_max_action(self.MAX_ACTION_NUM)
        # 存放动态表的16进制编码
        self.dynamic_hex_list.append(reversed_dynamic_id)
        self.dynamic_hex_list.append(max_action_hex)

        # 查询并处理所有记录
        experiment_flow_records = fetch_all_experiment_flow(conn)
        processed_records = process_experiment_flow_records(experiment_flow_records)
        for record in processed_records:
            record_id, formatted_start_time, formatted_action_id, formatted_action_time = record
            dynamic_hex = formatted_start_time + formatted_action_id + formatted_action_time
            self.dynamic_hex_list.append(dynamic_hex)

        # 将所有十六进制字符串拼接成一个大的十六进制字符串
        combined_hex_string = ''.join(self.dynamic_hex_list)
        # 文件夹不存在则创建
        base_path = os.path.abspath('./dynamic_bin')
        if not os.path.exists(base_path):
            os.makedirs(base_path)
        # 生成动态表的.bin文件
        output_file_path = base_path + os.path.sep + 'DT_' + format_id + '.bin'
        hex_string_to_binary_file(combined_hex_string, output_file_path)

        # ------------------------生成动态表的Excel文件-------------------------
        excel_records = []
        excel_records.append((self.dynamic_id, self.MAX_ACTION_NUM, ' '))
        for record in experiment_flow_records:
            record_id, start_time, action_id, action_time = record
            excel_records.append((start_time, action_id, action_time))

        excel_filename = f'DT_{format_id}.xlsx'
        # 保存到Excel文件
        save_to_excel(excel_records, excel_filename)

        # 更新 id 等于给定值的 dynamic_id 加1
        update_dynamic_id_by_id(conn)
        # 删除 experiment_flow 表中的所有数据
        delete_all_experiment_flow_data(conn)
        # 关闭数据库连接
        conn.close()
        # ---------------清空表格信息---------------
        # 获取表格中的行数和列数
        row_count = self.flowTableWidget.rowCount()
        column_count = self.flowTableWidget.columnCount()
        # 迭代每个单元格并将其内容设置为空
        for row in range(row_count):
            for col in range(column_count):
                self.flowTableWidget.setItem(row, col, QTableWidgetItem(""))
        QMessageBox.information(None, "Success", f"动态表生成成功！\n文件所在目录：{base_path}")

    def show_total_table_dialog(self):
        """
        点击生成总表按钮，弹出对话框
        :return:
        """
        dlg = TotalTableDlg()
        dlg.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
