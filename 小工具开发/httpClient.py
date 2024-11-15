"""
# 导入对应的库


"""
# 1- 应用对象
from PySide2.QtWidgets import QApplication
# 2- 界面ui文件需要导入代码里去
from PySide2.QtUiTools import QUiLoader
# 3-导入读取ui文件的库
from PySide2.QtCore import QFile
import json, requests
import threading

"""
后端处理流程：
    1- 发送请求
        1- 使用对应的requests库操作
            1- 请求方法
                4种方法
                    1- request.get/post
            2- 请求url
            3- 请求头
            4- 请求body
    2- 显示响应
    3- 清空数据
                
"""


class HttpClient:
    def __init__(self, uiName='接口工具.ui'):  # 初始化方法--只要创建实例就会自动调用
        # 获取ui文件
        self.qFile = QFile(uiName)
        # 打开这个ui文件
        self.qFile.open(QFile.ReadOnly)
        # 加载这个ui文件
        self.ui = QUiLoader().load(self.qFile)
        # 关闭qfile文件
        self.qFile.close()
        # 关联按钮--调用
        self.ui.pushButton.clicked.connect(self.request_send)

    # 1- 封装发送方法
    def request_send(self):
        # 1- 获取请求方法
        method = self.ui.comboBox.currentText()  # 下拉框当前的值
        # 2- 请求的url
        url = self.ui.lineEdit.text()
        # 3- 请求头--从控件获取的数据是str---转化---dict
        header = self.ui.plainTextEdit.toPlainText()
        if header.strip() != "":
            header = json.loads(header)
        # 4- 请求体
        payload = self.ui.plainTextEdit_2.toPlainText()
        if payload.strip() != "":
            payload = json.loads(payload)
        # 打印信息--调试
        print(method, url, header, payload, sep='\n')
        # 5- 发送请求
        req = requests.Request(method, url, headers=header, data=payload)
        prepare = req.prepare()  # 获取请求数据
        s = requests.Session()  # 创建会话
        # 发送
        # resp = s.send(prepare)
        t1 = threading.Thread(target=self.thread_send, args=(s, prepare))
        t1.start()

    # 有一个新想法：一个线程，如果这个url 不存在--那个gui会卡住
    def thread_send(self, s, prepare):
        resp = s.send(prepare)
        self.show_response(resp)

    def show_response(self, resp):
        # 1- 响应头
        # 2- 响应体
        resp.encoding = 'utf-8'
        self.ui.textBrowser.append(
            "HTTP/1.1 {} \n{} \n \n{}".format(
                resp.status_code,  # 状态码
                '\n'.join('{}:{}'.format(k, v) for k, v in resp.headers.items()),  # 响应头
                resp.text  # 响应体
            )
        )


# 需要一个应用程序对象
app = QApplication([])  # sys.argv
# 显示这个ui
HttpClient = HttpClient()
# 显示这个ui
HttpClient.ui.show()

# 运行应用对象
app.exec_()
