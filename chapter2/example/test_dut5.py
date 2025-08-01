from RandomGenerator import *
import random

# 定义参考模型
class LFSR_16:
    def __init__(self, seed):
        self.state = seed & ((1 << 16) - 1)

    def Step(self):
        new_bit = (self.state >> 15) ^ (self.state >> 14) & 1
        self.state = ((self.state << 1) | new_bit ) & ((1 << 16) - 1)

if __name__ == "__main__":
    dut = DUTRandomGenerator()            # 创建DUT
    dut.InitClock("clk")                  # 指定时钟引脚，初始化时钟
    seed = random.randint(0, 2**16 - 1)   # 生成随机种子
    dut.seed.value = seed                 # 设置DUT种子
    # reset DUT
    dut.reset.value = 1                   # reset 信号置1
    dut.Step()                            # 推进一个时钟周期（DUTRandomGenerator是时序电路，需要通过Step推进）
    dut.reset.value = 0                   # reset 信号置0
    dut.Step()                            # 推进一个时钟周期

    ref = LFSR_16(seed)                   # 创建参考模型用于对比

    for i in range(65536):                # 循环65536次
        dut.Step()                        # dut 推进一个时钟周期，生成随机数
        ref.Step()                        # ref 推进一个时钟周期，生成随机数
        rand = dut.random_number.value
        assert rand == ref.state, "Mismatch"  # 对比DUT和参考模型生成的随机数
        print(f"Cycle {i}, DUT: {rand:x}, REF: {ref.state:x}") # 打印结果
    # 完成测试
    print("Test Passed")
    dut.Finish()    # Finish函数会完成波形、覆盖率等文件的写入