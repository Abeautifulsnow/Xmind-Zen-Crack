class Crack(object):
    def __init__(self, f_name: str):
        self.f_name = f_name

    # 替换掉str
    def replace_str(self, old, new):
        with open(self.f_name) as f1:
            content = f1.read()
            f1.close()
        rep = content.replace(old, new)
        with open(self.f_name, "wb") as f2:
            f2.write(rep.encode())
            f2.close()

    # 添加css
    def add_css(self, k_word, new_css):
        with open(self.f_name) as f2:
            content = f2.read()
            pos = content.find(k_word)
            if pos != -1:
                content = content[:pos+len(k_word)] + new_css + content[pos+len(k_word):]
                f2 = open(self.f_name, "wb")
                f2.write(content.encode())
            f2.close()

    # 删除所有文件
    def del_all(self):
        open(self.f_name, "wb").close()
