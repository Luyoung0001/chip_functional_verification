from RandomGenerator import DUTRandomGenerator
import random
from toffee import start_clock
from toffee_test import ToffeeRequest
import toffee_test  # 用来引用装饰器等


# 定义参考模型
class LFSR_16:
    def __init__(self, seed):
        self.state = seed & ((1 << 16) - 1)

    def Step(self):
        new_bit = ((self.state >> 15) ^ (self.state >> 14)) & 1
        self.state = ((self.state << 1) | new_bit) & ((1 << 16) - 1)


@toffee_test.testcase
async def test_with_ref(dut: DUTRandomGenerator):
    ref = LFSR_16(dut.seed.value)  # 用 dut 的种子初始化参考模型

    for i in range(65536):
        dut.Step()
        ref.Step()
        rand = dut.random_number.value
        assert rand == ref.state, "Mismatch"


@toffee_test.fixture
async def dut(toffee_request: ToffeeRequest):
    # 先实例化 ToffeeRequest
    req = toffee_request

    # 使用实例方法创建 dut
    dut = req.create_dut(DUTRandomGenerator, "clk")

    seed = random.randint(0, 2**16 - 1)
    dut.seed.value = seed

    # reset DUT
    dut.reset.value = 1
    dut.Step()
    dut.reset.value = 0
    dut.Step()

    return dut
