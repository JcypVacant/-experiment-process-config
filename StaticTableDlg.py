from datetime import datetime
import os
import re
from PySide6.QtWidgets import QDialog, QMessageBox
from ui.StaticTable import Ui_StaticTable
import fnmatch
from tkinter import Tk, filedialog
from utils.data_utils import hex_string_to_binary_file


class StaticTableDlg(QDialog, Ui_StaticTable):
    def __init__(self):
        super(StaticTableDlg, self).__init__()
        self.setupUi(self)
        # 实验总批数
        self.experimental_total_hex = ''
        # 静态表中间.bin中间参数
        self.middle_bin = ''
        # 每类动作数.bin参数
        self.actions_bin = ''
        # 静态表.bin尾部参数
        self.tail_bin = ''
        # 静态表.bin总参数
        self.total_bin = ''
        # 动态表数
        self.dynamic_count = 0
        # 初始化每类动作数
        self.actions_count = {hex(i)[-1].upper(): 0 for i in range(16)}
        # 初始化一个字典，用于存储每类动作的名字
        self.action_names = {0: "炉子开关动作表", 1: "炉丝电机1参数动作表", 2: "电机1动作表", 3: "电机2动作表", 4: "电机3动作表",
                             5: "电机4动作表", 6: "电机5动作表", 7: "电机状态查询", 8: "磁场动作表", 9: "电机磁场电流动作表",
                             'A': "炉丝加热电压动作表", 'B': "PID控温曲线设置动作表", 'C': "在线监控状态查询表", 'D': "电机关闭设置动作表", 'E': "在线监控表头设置动作表",
                             'F': "预留"}
        # 计算每类动作数
        self.pushButton_2.clicked.connect(self.get_actions_count)
        # 计算流程表数
        self.pushButton.clicked.connect(self.get_dynamic_count)
        # 生成静态表
        self.pushButton_3.clicked.connect(self.generate_static_bin)

    def convert_and_reverse(self, d_value, e_value):
        """将十进制数转换为指定长度的十六进制字符串，并反转每两个字符一组"""
        hex_str = format(d_value, f'0{e_value * 2}X')
        # 每两个字符一组进行反转
        reversed_hex = ''.join([hex_str[i:i + 2] for i in range(0, len(hex_str), 2)][::-1])
        return reversed_hex
    def get_actions_count(self):
        """
        计算每类动作数,读取电脑中文件夹中的所有文件
        选择文件夹并筛选出所有以 AT 开头且包含四位十六进制数的 .bin 文件，并按十六进制数的首位分类统计文件数
        :return:
        """
        # 打开文件夹选择对话框
        Tk().withdraw()  # 隐藏主窗口
        folder_selected = filedialog.askdirectory()

        if not folder_selected:
            return

        # 初始化计数字典
        self.actions_count = {hex(i)[-1].upper(): 0 for i in range(16)}

        # 正则表达式匹配以四位十六进制数
        pattern = re.compile(r'AT.*?([0-9A-Fa-f]{4}).*?\.bin$')

        # 筛选文件
        for root, dirs, files in os.walk(folder_selected):
            for filename in fnmatch.filter(files, 'AT*.bin'):
                match = pattern.match(filename)
                if match:
                    hex_num = match.group(1).upper()
                    first_char = hex_num[0]
                    if first_char in self.actions_count:
                        self.actions_count[first_char] += 1

        # 使用 convert_and_reverse 函数处理每个类别的文件数量
        result_list = []
        for key, value in self.actions_count.items():
            manipulated_hex = self.convert_and_reverse(value, 2)
            result_list.append(manipulated_hex)

        # 将结果连接成一个字符串
        self.actions_bin = ''.join(result_list)

        # 打印分类统计结果和处理后的字符串
        print("每类动作数分类统计：")
        for key, value in self.actions_count.items():
            print(f"{key}: {value}")

    def get_dynamic_count(self):
        """
        计算流程表数，读取电脑中文件夹中的所有文件，计算以DT开头的文件数，文件名后缀为.bin
        :return:
        """
        # 打开文件夹选择对话框
        Tk().withdraw()  # 隐藏主窗口
        folder_selected = filedialog.askdirectory()

        if not folder_selected:
            return

        # 筛选文件
        self.dynamic_count = 0
        for root, dirs, files in os.walk(folder_selected):
            for filename in fnmatch.filter(files, 'DT*.bin'):
                self.dynamic_count += 1
        print(f"文件夹中共有流程表文件：{self.dynamic_count}个")
        self.experimental_total_hex = format(self.dynamic_count, '02X')
        print(f"对应的十六进制值为：{self.experimental_total_hex}")
    def read_txt_file(self, file_name):
        """读取与脚本文件位于相同目录下的 txt 文件内容"""
        # 获取脚本文件的当前目录
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # 构建 txt 文件的完整路径
        file_path = os.path.join(script_dir, file_name)

        # 读取 txt 文件内容
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        return content
    def generate_static_bin(self):
        """
        生成静态表.bin文件
        :return:
        """
        # 读取静态表中间.bin
        self.middle_bin = self.read_txt_file('static_middle_bin.txt')
        # 读取静态表尾部.bin
        self.tail_bin = self.read_txt_file('static_tail_bin.txt')
        # 计算静态表总.bin
        self.total_bin = self.experimental_total_hex + self.middle_bin + self.actions_bin + self.tail_bin

        # 获取今天的月份和日期，并格式化为字符串
        today = datetime.today()
        month_day_str = today.strftime('%m%d')

        # 将生成的静态表写入文件
        if len(self.total_bin) == 0:
            QMessageBox.information(None, "Success", "没有静态表需要生成！")
            return
        # 文件夹不存在则创建
        base_path = os.path.abspath('./static_bin')
        if not os.path.exists(base_path):
            os.makedirs(base_path)
        # 生成静态表的.bin文件
        output_file_path = base_path + os.path.sep + 'ST_静态表' + month_day_str + '.bin'
        hex_string_to_binary_file(self.total_bin, output_file_path)
        print(f"静态表生成成功！\n文件所在目录：{base_path}")
        QMessageBox.information(None, "Success", f"静态表生成成功！\n文件所在目录：{base_path}")
        # 关闭窗口
        self.close()
