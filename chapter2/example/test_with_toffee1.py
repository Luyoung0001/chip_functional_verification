from RandomGenerator import DUTRandomGenerator
import random
import toffee
import toffee_test

from toffee_test import ToffeeRequest


class LFSR_16:
    def __init__(self, seed):
        self.state = seed & ((1 << 16) - 1)

    def Step(self):
        new_bit = (self.state >> 15) ^ (self.state >> 14) & 1
        self.state = ((self.state << 1) | new_bit) & ((1 << 16) - 1)


@toffee_test.testcase
async def test_with_ref(dut: DUTRandomGenerator):
    seed = random.randint(0, 2**16 - 1)
    dut.seed.value = seed
    ref = LFSR_16(seed)

    dut.reset.value = 1
    await dut.AStep(1)  # 等待时钟经过一个周期
    dut.reset.value = 0
    await dut.AStep(1)  # 更新DUT状态

    for i in range(65536):
        await dut.AStep(1)
        ref.Step()
        assert dut.random_number.value == ref.state, "Mismatch"


@toffee_test.fixture
async def dut(toffee_request: ToffeeRequest):
    rand_dut = toffee_request.create_dut(DUTRandomGenerator, "clk")

    toffee.start_clock(rand_dut)  # 让toffee驱动时钟，只能在异步函数中调用
    return rand_dut