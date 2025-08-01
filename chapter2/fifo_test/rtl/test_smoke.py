from SyncFIFO import *
import asyncio
    #创建test_reset_dut 函数作为的测试用例：把rst_n信号拉低 5 个周期后，再拉高 2 个周期，导出波形信号
async def test_reset_dut(dut: DUTSyncFIFO):
    # 复位
    dut.rst_n.value = 0
    await dut.AStep(1)
    dut.rst_n.value = 1
    await dut.AStep(1)

    # 向 FIFO 分别写入两个数据：
    dut.wr_en.value = 1
    dut.wdata.value = 0x14
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
    # 从 FIFO 读出两个数据：
    # 给we_i置低、re_i置高，保持一个周期，之后读取data_o，判断结果是否为0x114
    # 给we_i置低、re_i置高，保持一个周期，之后读取data_o，判断结果是否为0x514、empty_o是否为 1
    dut.wr_en.value = 0
    dut.rd_en.value = 1
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

async def main(dut: DUTSyncFIFO):
    asyncio.create_task(test_reset_dut(dut))
    await asyncio.create_task(dut.RunStep(10))  # 让时钟持续推进 10 个周期

if __name__ == "__main__":
    #创建同步 FIFO 的 DUT 类
    dut = DUTSyncFIFO()
    dut.InitClock("clk")
    asyncio.run(main(dut))
    dut.Finish()