from RandomGenerator import *

def callback(cycles, reset):
    print(f"The current clock cycle is {cycles}")
    if reset.value:
        print("DUT reset.")

if __name__ == "__main__":
    dut = DUTRandomGenerator()
    # 初始化时钟，参数时钟引脚对应的名称，例如clk
    dut.InitClock("clk")
    # 注意！传入的是 callback，不是 callback()
    dut.StepRis(callback, [dut.reset])

    # 驱动时钟
    dut.Step()
    dut.reset.value = 1
    dut.Step(5)
    dut.reset.value = 0
    dut.Step(4)
    dut.Finish()