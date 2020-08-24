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
        self.product_count = len(fnmatch.filter(os.listdir(self.product_list_path), '*.txt'))

        #要素の追加・削除ボタンの配置
        self.baseControlleFrame = tk.Frame(master, width=1000, height=50,borderwidth=1, relief='groove')  #基本操作ボタンをまとめるフレーム
        self.addButton = tk.Button(self.baseControlleFrame, text='追加', width=5, height=2, command=self.addProduct)  #要素の追加をするボタン
        self.addButton.pack(fill='x', padx=20, side='left')
        self.delButton = tk.Button(self.baseControlleFrame, text='削除', width=5, height=2)  #要素の削除をするボタン
        self.delButton.pack(fill='x', padx=20, side='left')

        #プロダクト一覧の配置
        self.productList_baseFrame = tk.Frame(master, width=250)
        self.canvas = tk.Canvas(self.productList_baseFrame, width=250)
        self.List_bar = tk.Scrollbar(self.productList_baseFrame, orient=tk.VERTICAL)
        self.List_bar.pack(side='right', fill='y')
        self.List_bar.config(command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.List_bar.set)
        self.canvas.config(scrollregion=(0, 0, 250, self.product_count*60))
        self.productListFrame = tk.Frame(self.canvas, borderwidth=1, relief='groove')
        self.canvas.create_window((0, 0), window=self.productListFrame, anchor=tk.NW, width=self.canvas.cget('width'))

        self.productList = []
        for i in range(0, self.product_count):
            #self.product_element = tk.Button(self.productListFrame, text='aa', width=25, height=3, command=self.buttonPressed)
            self.productList.append(tk.Button(self.productListFrame, text='Product', width=25, height=3, command=self.buttonPressed))
            self.productList[i].pack()


        self.baseControlleFrame.pack(fill='x', padx=10, pady=10, ipady=5)
        self.canvas.pack(fill='y', side='left')
        self.productList_baseFrame.pack(fill='y', side='left')

    def buttonPressed(self):
        self.Button.config(bg='#FF0000')

    def addProduct(self):
        product_path = pathlib.Path(self.product_list_path + 'test' + str(self.product_count+1) + '.txt')
        product_path.touch()
        self.product_count += 1
        self.productList.append(tk.Button(self.productListFrame, text='aa', width=25, height=3, command=self.buttonPressed))
        self.productList[self.product_count-1].pack()
        self.canvas.config(scrollregion=(0, 0, 250, self.product_count * 60))

def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()

