import asyncio
from RandomGenerator import *


def pin_value_is_beef(dut: DUTRandomGenerator):
    def is_beef() -> bool:
        return dut.random_number.value == 0xBEEF

    return is_beef # 返回的不是 is_beef()


async def example_async(dut: DUTRandomGenerator):
    print("Reset start.")
    dut.seed.value = 0xBEEF
    dut.reset.value = 1

    print("Wait condition")
    await dut.ACondition(pin_value_is_beef(dut))  # 等待引脚信号变为0xBEEF

    dut.reset.value = 0
    print("Wait 1 clock")
    await dut.AStep(1)  # 等待时钟经过1个周期, 与 `dut.xclock.AStep(1)` 等价
    print("Reset done.")


async def main(dut: DUTRandomGenerator):
    asyncio.create_task(example_async(dut))
    await asyncio.create_task(dut.RunStep(100))  # 让时钟持续推进 10 个周期


if __name__ == "__main__":
    dut = DUTRandomGenerator()
    dut.InitClock("clk")  # 初始化时钟，参数时钟引脚对应的名称，例如clk
    asyncio.run(main(dut)) # 运行主函数
    dut.Finish()