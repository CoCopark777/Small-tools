"""
# 导入对应的库


"""
# 1- 应用对象
from PySide2.QtWidgets import QApplication
# 2- 界面ui文件需要代入代码里去
from PySide2.QtUiTools import QUiLoader
# 3-导入读取ui文件的库
from PySide2.QtCore import QFile
# 4- 生成数据用的库
from faker import Faker

"""
后端处理流程：
    1- 发送请求
        1- 请求方法faker库操作
            1-生成姓名
            2-生成身份证
            3-生成电话
            4-生成地址
    2- 显示响应
    3- 清空数据

"""



class IDCardClient:
    def __init__(self, uiName='客户信息生成工具.ui'): # 初始化方法--只要创建实例就会自动调用
        # 获取ui文件
        self.qFile = QFile(uiName)
        # 打开ui文件
        self.qFile.open(QFile.ReadOnly)
        #加载ui文件
        self.ui = QUiLoader().load(self.qFile)
        # 关闭ui文件
        self.qFile.close()
        #关联按钮--调用
        self.ui.pushButton.clicked.connect(self.faker_send)


    # 1- 封装生成方法
    def faker_send(self):
        # 1- 生成客户信息
        f = Faker(locale='zh_CN')
        name = f.name()
        id_card = f.ssn()
        p_number = f.phone_number()
        address = f.address()
        self.ui.textBrowser.clear()
        self.ui.textBrowser_2.clear()
        self.ui.textBrowser_3.clear()
        self.ui.textBrowser_4.clear()
        self.ui.textBrowser_5.clear()
        self.ui.textBrowser_2.append(name)
        self.ui.textBrowser_3.append(id_card)
        self.ui.textBrowser_4.append(p_number)
        self.ui.textBrowser_5.append(address)
        # 打印信息调试
        print(name, id_card,p_number,address, sep='\n')
        self.show_information(name, id_card,p_number,address)

    def show_information(self, name,id_card,p_number,address):
        # 姓名，身份证，电话，地址
        self.ui.textBrowser.append(
            "姓名:{} \n身份证:{} \n电话:{} \n地址:{}".format(
                name,id_card,p_number,address
            )
        )


# 需要一个应用程序对象
app = QApplication([])
# 实例化
IDCardClient = IDCardClient()
# 显示这个ui
IDCardClient.ui.show()

# 运行应用对象
app.exec_()

