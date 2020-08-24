import tkinter as tk
import pathlib
import fnmatch
import os
from functools import partial


class Application(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.pack()

        master.title("Product_Index")
        master.geometry("1000x700")

        self.product_list_path = '../product_list/'
        self.files = os.listdir(self.product_list_path)
        #self.product_count = len(self.files)
        self.product_count = len(fnmatch.filter(os.listdir(self.product_list_path), '*.txt'))

        print(self.product_count)

        #要素の追加・削除ボタンの配置
        self.baseControlleFrame = tk.Frame(master, width=1000, height=50,borderwidth=1, relief='groove')  #基本操作ボタンをまとめるフレーム
        self.addButton = tk.Button(self.baseControlleFrame, text='追加', width=5, height=2, command=self.addProduct)  #要素の追加をするボタン
        self.addButton.pack(fill='x', padx=20, side='left')
        self.delButton = tk.Button(self.baseControlleFrame, text='削除', width=5, height=2)  #要素の削除をするボタン
        self.delButton.pack(fill='x', padx=20, side='left')

        #プロダクト一覧の配置
        self.productListFrame = tk.Frame(master, width=250, borderwidth=1, relief='groove')
        self.productList = []
        for i in range(0, self.product_count):
            #self.product_element = tk.Button(self.productListFrame, text='aa', width=25, height=3, command=self.buttonPressed)
            self.productList.append(tk.Button(self.productListFrame, text='aa', width=25, height=3, command=self.buttonPressed))
            self.productList[i].pack()


        '''''
        self.Button = tk.Button(self.productListFrame, text='aa', width=25, height=3, command=self.buttonPressed)
        #self.Button.pack()
        self.Button2 = tk.Button(self.productListFrame, text='bb', width=25, height=3)
        #self.Button2.pack()
        self.Button_list.append(self.Button)
        self.Button_list.append(self.Button2)
        self.Button_list[0].pack()
        self.Button_list[1].pack()
        '''''

        #self.txtBox = tk.Entry()
        # txtBox.configure(state='normal', width=50, height=30)
        #self.txtBox.place(x=500, y=10, width=500, height=100)

        #self.button = tk.Button(text='ボタン', width=30, command=self.outputWords)
        #self.button.pack(anchor='w')

        self.baseControlleFrame.pack(fill='x', padx=10, pady=10, ipady=5)
        self.productListFrame.pack(fill='y', side='left', padx=10, pady=10, ipadx=5, ipady=5)

    #def outputWords(self):
        #self.txtBox.insert(tk.END, "Hello!!")

    def buttonPressed(self):
        self.Button.config(bg='#FF0000')

    def addProduct(self):
        product_path = pathlib.Path(self.product_list_path + 'test' + str(self.product_count+1) + '.txt')
        #product_path = pathlib.Path('../product_list/test.txt')
        product_path.touch()
        self.product_count += 1
        self.productList.append(tk.Button(self.productListFrame, text='aa', width=25, height=3, command=self.buttonPressed))
        self.productList[self.product_count-1].pack()

def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()