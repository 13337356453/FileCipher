import os
import random

from PyQt5.QtWidgets import QFileDialog, QMessageBox

from Cipher import Cipher
from tools.Consoler import Consoler
from tools.FileReader import FileReader


class FileCipherEvent:
    def __init__(self,parent):
        self.parent=parent

    def choiceFile(self):
        filenames=QFileDialog.getOpenFileNames(self.parent,"打开文件","./","txt文件(*.txt);;所有文件(*.*)")[0]
        if filenames:
            text=""
            for name in filenames:
                text+=name+"|"
            self.parent.pathfield.setText(text)
    def makeKey(self):
        length=self.parent.key_len_edit.value()
        key=""
        for i in range(length):
            key+=chr(random.randint(33,125))
        self.parent.keyedit.setText(key)
    def copyKey(self):
        self.parent.keyedit.selectAll()
        self.parent.keyedit.copy()
    def choiceOut(self):
        path=QFileDialog.getExistingDirectory(self.parent,'打开','./')
        if path:
            self.parent.outPathEdit.setText(path)
    def start(self):
        self.consoler=Consoler(self.parent.console)
        self.consoler.clear()
        # 打开文件
        files=self.parent.pathfield.text()
        fs=[]
        if files.strip():
            files=files.split("|")
            for file in files:
                if file.strip()!="":
                    self.consoler.echoText("正在打开文件："+file)
                    reader=FileReader(file)
                    text=reader.read()
                    if text==None:
                        self.consoler.echoError("文件打开失败："+file)
                        return
                    fs.append(file)
        else:
            self.consoler.echoError('请指定文件')
            return
        # 读取密钥
        key=self.parent.keyedit.text()
        self.consoler.echoText("")
        self.consoler.echoText("正在读取密钥")
        if key=="":
            self.consoler.echoError("密钥为空，请指定密钥")
            return
        # 读取输出路径
        self.consoler.echoText("")
        self.consoler.echoText("正在读取输出路径")
        outpath=self.parent.outPathEdit.text()
        if not os.path.exists(outpath):
            os.mkdir(outpath)
        # 开始
        self.consoler.echoText("")
        if self.parent.enMode.isChecked():
            self.consoler.echoText("开始加密",color='red')
            self.encrypt(key,fs,outpath)
        else:
            self.consoler.echoText("开始解密", color='red')
            self.decrypt(key, fs,outpath)
    def encrypt(self,key,files,outpath):
        c=Cipher(key)
        for file in files:
            try:
                self.consoler.echoText("正在加密："+file)
                reader=FileReader(file)
                text=reader.read()
                encoding=reader.encoding
                result=c.encrypt(text)
                with open(f"{outpath}/en_{file.split('/')[-1]}",'w',encoding=encoding) as f:
                    f.write(result)
                self.consoler.echoText("加密成功，输出路径："+f"{outpath}/en_{file.split('/')[-1]}",color='red')
            except:
                self.consoler.echoError("加密失败："+file)
    def decrypt(self,key,files,outpath):
        c = Cipher(key)
        for file in files:
            try:
                self.consoler.echoText("正在解密：" + file)
                reader = FileReader(file)
                text = reader.read()
                encoding = reader.encoding
                result = c.decrypt(text)
                with open(f"{outpath}/de_{file.split('/')[-1]}", 'w', encoding=encoding) as f:
                    f.write(result)
                self.consoler.echoText("解密成功，输出路径：" + f"{outpath}/de_{file.split('/')[-1]}",color='red')
            except:
                self.consoler.echoError("解密失败：" + file)

