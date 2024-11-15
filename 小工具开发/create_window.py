# 导入对应的库
# 1-应用对象
from PySide2.QtWidgets import QApplication
# 2-界面UI 文件需要导入代码里面去
from PySide2.QtUiTools import QUiLoader
# 3-导入读取UI文件的库
from PySide2.QtCore import QFile
from ID_card import generate_id_card

# 4-需要一个应用程序的对象
app = QApplication([])
# 5-获取UI文件
qFile = QFile('登录.ui')
# 6-打开UI文件
qFile.open(QFile.ReadOnly)
# 7-加载UI对象
ui = QUiLoader().load(qFile)
# 8-关闭qfile文件
qFile.close()

### ---登录操作---
def login():
    # 账号密码获取 --ui页面对应的对象获取
    username = ui.username_lineEdit.text()
    password = ui.password_lineEdit_2.text()
    ui.textBrowser.append(f"用户{username},登录成功")
    # 密码获取

def exit():
    ui.textBrowser.clear()

def id_number():
    id = generate_id_card()
    ui.textBrowser_2.append(f"用户的身份证号码是 {id}")


ui.pushButton.clicked.connect(id_number)

# 动作关联

ui.login_pushButton.clicked.connect(login)
ui.clear_pushButton.clicked.connect(exit)


# 9-显示这个UI界面
ui.show()
# 10-运行应用对象
app.exec_()



