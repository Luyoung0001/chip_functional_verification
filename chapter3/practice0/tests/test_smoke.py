from SyncFIFO import DUTSyncFIFO
import toffee
import toffee_test

from toffee_test import ToffeeRequest

@toffee_test.testcase
async def test_with_ref(dut: DUTSyncFIFO):
    # 复位
    dut.rst_n.value = 0
    await dut.AStep(1)
    dut.rst_n.value = 1
    await dut.AStep(1)

    # 向 FIFO 分别写入两个数据

    # 写第一个数据
    dut.we_i.value = 1
    dut.data_i.value = 0x114
    await dut.AStep(1)
    dut.we_i.value = 0
    await dut.AStep(1)

    assert dut.empty_o.value == 0,"Mismatch"
    assert dut.full_o.value == 0,"Mismatch"
    # 写第二个数据
    dut.we_i.value = 1
    dut.data_i.value = 0x514
    await dut.AStep(1)
    dut.we_i.value = 0
    await dut.AStep(1)

    # 从 FIFO 读出两个数据
    # 读第一个数据
    dut.we_i.value = 0
    dut.re_i.value = 1
    await dut.AStep(1)
    dut.re_i.value = 1
    await dut.AStep(1)

    assert dut.data_o.value == 0x114,"Mismatch"
    # 读取第二个数据
    dut.we_i.value = 0
    dut.re_i.value = 1
    await dut.AStep(1)
    dut.we_i.value = 0
    dut.re_i.value = 0
    await dut.AStep(1)
    assert dut.data_o.value == 0x514,"Mismatch"
    assert dut.empty_o.value == 1,"Mismatch"


@toffee_test.fixture
async def dut(toffee_request: ToffeeRequest):
    rand_dut = toffee_request.create_dut(DUTSyncFIFO, "clk")

    toffee.start_clock(rand_dut)  # 让toffee驱动时钟，只能在异步函数中调用
    return rand_dut