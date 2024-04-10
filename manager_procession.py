import openpyxl
import datetime

class StudentSignInSystem:
    def __init__(self):
        self.students = {}  # 学生信息字典，用于存储学生ID和姓名的对应关系
        self.sign_in_data = []  # 签到记录列表，用于存储学生的签到和签退记录

    def login(self, username, password):
        # 在这里添加登录验证逻辑，例如与数据库中的数据进行比较
        pass

    def start_sign_in(self, student_id):
        # 开始签到函数，记录学生的签到时间
        if student_id in self.students:
            self.sign_in_data.append((student_id, datetime.datetime.now()))  # 将学生ID和当前时间加入到签到记录中
        else:
            print("学生ID不存在")

    def end_sign_in(self, student_id):
        # 结束签到函数，记录学生的签退时间
        if student_id in self.students:
            sign_in_time = [record for record in self.sign_in_data if record[0] == student_id][-1][1]  # 获取该学生最近的签到时间
            sign_out_time = datetime.datetime.now()  # 获取当前时间作为签退时间
            self.sign_in_data.append((student_id, sign_out_time))  # 将学生ID和签退时间加入到签到记录中
        else:
            print("学生ID不存在")

    def add_student(self, student_id, name):
        # 添加学生信息到系统中
        self.students[student_id] = name  # 将学生ID和姓名加入到学生信息字典中

    def delete_student(self, student_id):
        # 从系统中删除学生信息
        if student_id in self.students:
            del self.students[student_id]  # 从学生信息字典中删除指定的学生ID
        else:
            print("学生ID不存在")

    def export_to_excel(self, file_name):
        # 将签到记录导出到Excel文件
        wb = openpyxl.Workbook()  # 创建一个新的Excel工作簿
        ws = wb.active
        ws.title = "签到记录"  # 将当前工作表命名为"签到记录"
        ws.append(["学生ID", "签到时间", "签退时间"])  # 添加表头

        for record in self.sign_in_data:
            ws.append(record)  # 将签到记录逐行加入到Excel工作表中

        wb.save(file_name)  # 保存Excel文件

# 示例用法
system = StudentSignInSystem()
system.add_student(1, "张三")
system.add_student(2, "李四")
system.start_sign_in(1)
system.end_sign_in(1)
system.export_to_excel("签到记录.xlsx")
