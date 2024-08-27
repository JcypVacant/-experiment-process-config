import os
#
# from utils.data_utils import store_data
#
# data_list = ['2500F0C03300190033001a0083001b000F00FA00CC000201', '4110C0C30B002F00000031', '18F0640064006400640064006400640064006400640064006400']
#
# # 遍历每一个数据项并处理
# for data in data_list:
#     # 获取前四个字符并重新排列
#     original_prefix = data[:4].upper()
#     # 动作ID
#     action_id = original_prefix[2:4] + original_prefix[0:2]
#     # 参数编码
#     config_code = data[4:].upper()
#     # 打印输出
#     print("更新动作表》》》》》》》》")
#     print(f"{action_id} -> {config_code}")
#     # 保存到.txt文件
#     action_code = action_id[0:1]
#     if action_code.isdigit():
#         action_code = int(action_code)
#     store_data(action_id + " " + config_code, action_code)

