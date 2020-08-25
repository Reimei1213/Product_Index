import tkinter as tk
import tkinter.font as tkFont
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
        self.select_product = 0 #現在選択しているプロダクト
        self.font = tkFont.Font(size=25)

        #要素の追加・削除ボタンの配置
        self.baseControlleFrame = tk.Frame(master, width=1000, height=50,borderwidth=1, relief='groove')  #基本操作ボタンをまとめるフレーム
        self.addButton = tk.Button(self.baseControlleFrame, text='追加', width=5, height=2, command=self.addProduct)  #要素の追加をするボタン
        self.addButton.pack(fill='x', padx=20, side='left')
        #self.delButton = tk.Button(self.baseControlleFrame, text='削除', width=5, height=2, command=self.deleteProduct)  #要素の削除をするボタン
        #self.delButton.pack(fill='x', padx=20, side='left')

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

        #プロダクト名の一覧をボタンで表示
        self.productList = []
        for i in range(0, self.product_count):
            #f = open(fnmatch.filter(os.listdir(self.product_list_path), '*.txt')[i], 'r')
            #product_name = f.readline()
            product_name = fnmatch.filter(os.listdir(self.product_list_path), '*.txt')[i]
            f = open(self.product_list_path + product_name)
            name = f.readline()
            self.productList.append(tk.Button(self.productListFrame, text=name, width=25, height=3, command=partial(self.desplayContent, i)))
            self.productList[i].pack()

        #プロダクトの説明##############################################################
        self.productContent_frame = tk.Frame(master, width=710)
        self.productName_label = tk.Label(self.productContent_frame, text='作品名', font=self.font)
        self.productName_label.pack(anchor="nw")
        self.product_name = tk.Text(self.productContent_frame, width=100, height=1, font=self.font)
        self.product_name.pack(anchor="nw")
        self.productName_label = tk.Label(self.productContent_frame, text='作品 製作年月', font=self.font)
        self.productName_label.pack(anchor="nw")

        #プロダクトの製造年月の入力
        self.productDay_Frame = tk.Frame(self.productContent_frame, width=710)
        self.productYear_text = tk.Text(self.productDay_Frame, width=10, height=1, font=self.font)
        self.productYear_text.pack(side='left')
        self.productYear_label = tk.Label(self.productDay_Frame, text='年     ', font=self.font)
        self.productYear_label.pack(side='left')
        self.productMonth_text = tk.Text(self.productDay_Frame, width=10, height=1, font=self.font)
        self.productMonth_text.pack(side='left')
        self.productMonth_label = tk.Label(self.productDay_Frame, text='月', font=self.font)
        self.productMonth_label.pack(side='left')
        self.productDay_Frame.pack(anchor="nw")

        #プロダクトの説明の入力
        self.productContent_label = tk.Label(self.productContent_frame, text='作品説明', font=self.font)
        self.productContent_label.pack(anchor="nw")
        self.productContent_textFrame = tk.Frame(self.productContent_frame, width=710)
        self.productContent_text = tk.Text(self.productContent_textFrame, width=42, height=13, font=self.font)
        self.productContent_text.pack(side='left')
        self.productContent_scroll = tk.Scrollbar(self.productContent_textFrame, orient=tk.VERTICAL, command=self.productContent_text.yview)
        self.productContent_scroll.pack(side='right', fill="y")
        self.productContent_text.config(yscrollcommand=self.productContent_scroll.set)
        self.productContent_textFrame.pack(anchor="nw")
        self.save = tk.Button(self.productContent_frame, text='保存', width=5, height=2, command=self.saveContent)
        self.save.pack(anchor="se")


        #フレームをまとめる
        self.baseControlleFrame.pack(fill='x', padx=10, pady=10, ipady=5)
        self.canvas.pack(fill='y', side='left')
        self.productList_baseFrame.pack(fill='y', side='left')
        self.productContent_frame.pack(fill='y', side='left', padx=10, pady=10)


    #プロダクトを追加
    def addProduct(self):
        product_path = pathlib.Path(self.product_list_path + 'test' + str(self.product_count+1) + '.txt')
        product_path.touch()
        self.product_count += 1
        self.productList.append(tk.Button(self.productListFrame, text='Product', width=25, height=3, command=partial(self.desplayContent, self.product_count-1)))
        self.productList[self.product_count-1].pack()
        self.canvas.config(scrollregion=(0, 0, 250, self.product_count * 60))

    #プロダクトを削除
    #def deleteProduct(self):
        #os.remove(self.product_list_path + 'test' + str(self.select_product + 1) + '.txt')
        #return

    #プロダクトの内容を表示
    def desplayContent(self, idx):
        self.product_name.delete(1.0, tk.END)
        self.productYear_text.delete(1.0, tk.END)
        self.productMonth_text.delete(1.0, tk.END)
        self.productContent_text.delete(1.0, tk.END)

        self.select_product = idx
        f = open(self.product_list_path + 'test' + str(self.select_product + 1) + '.txt', "r")
        file = f.readline()
        product_name = file.rstrip('¥n')
        file = f.readline()
        product_year = file.rstrip('¥n')
        file = f.readline()
        product_month = file.rstrip('¥n')
        for line in f.readlines():
            product_content = line
            self.productContent_text.insert(tk.END, product_content)
        f.close()

        self.product_name.insert(tk.END, product_name)
        self.productYear_text.insert(tk.END, product_year)
        self.productMonth_text.insert(tk.END, product_month)

        return

    #入力したプロダクトの内容を保存
    def saveContent(self):
        product_name = self.product_name.get("1.0", "end")
        product_year = self.productYear_text.get("1.0", "end")
        product_month = self.productMonth_text.get("1.0", "end")
        product_content = self.productContent_text.get("1.0", "end")

        f = open(self.product_list_path + 'test' + str(self.select_product+1) + '.txt', "w")
        f.write(product_name)
        f.close()
        f = open(self.product_list_path + 'test' + str(self.select_product+1) + '.txt', "a")
        f.write(product_year)
        f.write(product_month)
        f.write(product_content)
        f.close()

        #作品名をボタンにも反映
        self.productList[self.select_product].config(text=product_name.rstrip('¥n'))
        return

def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()

