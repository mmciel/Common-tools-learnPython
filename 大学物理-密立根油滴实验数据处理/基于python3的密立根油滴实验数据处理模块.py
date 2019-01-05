
"""
说明：根据密立根油滴实验的实验数据，完成数据计算
作者：mmciel
版本：V1.0
"""
import math


def solve():
    """."""
    data = 0.0

    for i in range(0, 6):

        u0 = input("请输入电压：")
        t0 = input("请输入平均时间：")
        u = 1.0 * float(u0)
        t = 1.0 * float(t0)

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
        print("======================正在计算！======================")
        print("==========油滴半径：", a)
        zhongjian = (n * l) / (t * (1 + b / (p * a)))
        zhongjian = zhongjian * zhongjian * zhongjian
        zhongjian = math.sqrt(zhongjian)
        q = ((18 * 3.14) / (math.sqrt(2 * rou * g))) * (d / u) * zhongjian
        print("==========Q:", q)
        num = q / e
        num = int(num)
        print("==========电荷数：", num)
        num = float(num)
        nums = q / num * 1e19
        data = data + nums
        print("==========基本电荷测量值：", nums)
        print("=====================================================")
        pass
    data = data / 6
    print("=======基本电荷测量值均值：", data)
    dt = data - 1.602
    if dt < 0:
        dt = -dt
    wucha = dt / 1.602
    print("=======误差：", wucha)
    a = input('按任意键退出')
    pass


if __name__ == '__main__':
    print("PS：电荷数是用整数计算的，因为我也不知道怎么算。。。不用整数计算可以注释掉line40和line42")
    solve()
    
