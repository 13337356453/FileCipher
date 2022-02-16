
class FileReader:
    encoding=""
    def __init__(self,path):
        self.path=path
        self.encodings=['utf-8','utf-16','gbk','gb2312','ansi']
    def read(self):
        try:
            f=open(self.path,'rb')
            data=f.read()
            encoding=self.getEncoding(data)
            if encoding!="Not Found":
                f.close()
                return data.decode(encoding)
            f.close()
            return
        except FileNotFoundError:
            return

    def getEncoding(self,data):
        available = []
        for encoding in self.encodings:
            try:
                data.decode(encoding)
            except UnicodeDecodeError:
                pass
            else:
                available.append(encoding)
        if len(available) >= 1:
            self.encoding=available[0]
            return available[0]
        else:
            return "Not Found"