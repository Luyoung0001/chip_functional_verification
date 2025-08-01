from RandomGenerator import *

if __name__ == "__main__":
    dut = DUTRandomGenerator()           # 创建DUT
    # rand = dut.random_number.value       # 读取引脚random_number的值, 与 `rand = dut.random_number.U()` 等价
    # rand_lsb = dut.random_number[0]      # 读取引脚random_number的最低位
    # rand_signed = dut.random_number.S()  # 按有符号类型读取引脚random_number的值

    # dut.seed.value = 12345        # 十进制赋值
    # dut.seed.value = 0b11011      # 二进制赋值
    # dut.seed.value = 0o12345      # 八进制赋值
    # dut.seed.value = 0x12345      # 十六进制赋值
    # dut.seed.value = -1           # 所有bit赋值1
    # x = 3
    # dut.seed.value = x            # 与 a.Set(x) 等价
    # dut.seed[1] = 0               # 对第1位进行赋值
    # dut.seed.value = "x"          # 赋值高阻态
    # dut.seed.value = "z"          # 赋值不定态

    # dut.seed.AsRiseWrite()     # seed切换为上升沿写入，默认模式
    # dut.seed.AsFallWrite()     # seed切换为下降沿写入
    # dut.seed.AsImmWrite()      # seed切换为立即写入

    dut.InitClock("clk")
    dut.seed.value = 10        # 十进制赋值

    dut.reset.value = 1
    dut.Step()
    dut.reset.value = 0
    # 打印 5 个随机数字
    for i in range(5):
        # 读 random_number 的值
        rand = dut.random_number.value
        lftr = dut.RandomGenerator_lfsr.value
        print(f"Random number {i+1}: {rand:#x}")
        print(f"LFSR value {i+1}: {lftr:#x}")

        dut.Step()

    dut.Finish()