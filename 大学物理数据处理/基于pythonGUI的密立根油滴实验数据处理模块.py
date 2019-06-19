import tkinter
import math


class FindLocation(object):
    flag = 0
    data = 0.0
    def __init__(self):
        # 创建主窗口,用于容纳其它组件
        self.root = tkinter.Tk()
        self.root.geometry('600x450')
        # 给主窗口设置标题内容
        self.root.title(" 密立根油滴实验数据处理程序 V1.1 ———————— by：mmciel")
        self.lab1 = tkinter.Label(text='电压(V)')
        self.lab2 = tkinter.Label(text='时间(s)')
        self.lab3 = tkinter.Label(text='使用说明：\n1.连续输入六组数据，最后一组数据计算成功之后自动计算误差\n2.小数点请使用英文状态下标点\n3.提示数据异常请按照要求操作，否则误差和均值计算数据异常')
        # 创建一个输入框,并设置尺寸
        self.ip_input = tkinter.Entry(self.root,width=30)
        self.ip_input2 = tkinter.Entry(self.root,width=30)
        # 创建一个回显列表
        self.display_info = tkinter.Listbox(self.root, width=50)

        # 创建一个查询结果的按钮
        self.result_button = tkinter.Button(self.root, command = self.find_position, text = "计算")

    # 完成布局
    def gui_arrang(self):
        self.lab1.pack()
        self.ip_input.pack()
        self.lab2.pack()
        self.ip_input2.pack()
        self.display_info.pack()
        self.result_button.pack()
        self.lab3.pack()

    # 根据ip查找地理位置
    def find_position(self):
        # 获取输入信息
        self.u0 = self.ip_input.get()
        self.t0 = self.ip_input2.get()
        u = 1.0 * float(self.u0)
        t = 1.0 * float(self.t0)
        print(u)
        print(t)
        '''数据'''
        n = 1.83 * 1e-5
        g = 9.83
        d = 5 * 1e-3
        l = 1.5 * 1e-3
        b = 8.22 * 1e-3
        p = 1.013 * 1e5
        rou = 981
        e = 1.602 * 1e-19
        '''油滴半径'''
        a = math.sqrt(4.5 * n * (l / t) / rou / g)
        # print("======================正在计算！======================")
        # print("==========油滴半径：", a)
        zhongjian = (n * l) / (t * (1 + b / (p * a)))
        zhongjian = zhongjian * zhongjian * zhongjian
        zhongjian = math.sqrt(zhongjian)
        q = ((18 * 3.14) / (math.sqrt(2 * rou * g))) * (d / u) * zhongjian
        # print("==========Q:", q)
        num = q / e
        num = int(num)
        # print("==========电荷数：", num)
        num = float(num)
        if num == 0:
            self.display_info.insert(0, "数据异常，请重新输入")
            return
        else:
            nums = q / num * 1e19
        # print("==========基本电荷测量值：", nums)
        print("=====================================================")
        listdata = ["=====================================================", '油滴半径='+str(a), 'Q='+str(q), '电荷='+str(num), '基本电荷测量值='+str(nums), '电压为：'+str(u)+';时间为'+str(t)+'的数据下', "====================================================="]
        for item in listdata:
            self.display_info.insert(0, item)
        self.flag = self.flag + 1
        self.data = self.data + nums
        if self.flag == 6:
            self.flag = 0
            print(self.data)
            da = (self.data / 6)
            dt = da - 1.602
            print(da)
            if dt < 0:
                dt = -dt
            wucha = dt / 1.602
            s1 = '基本电荷测量值均值：' + str(da)
            s2 = '误差：' + str(wucha)
            self.display_info.insert(0, '************************')
            self.display_info.insert(0, s1)
            self.display_info.insert(0, s2)
            self.display_info.insert(0, '************************')
            self.data = 0.0

def main():
    # 初始化对象
    sfl = FindLocation()
    # 进行布局
    sfl.gui_arrang()
    # 主程序执行
    tkinter.mainloop()
    pass


if __name__ == "__main__":
    main()
	