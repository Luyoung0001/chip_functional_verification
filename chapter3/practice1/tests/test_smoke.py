# from SyncFIFO import DUTSyncFIFO
# import toffee
# import toffee_test

# from toffee_test import ToffeeRequest
# from bundle.write_bundle import WriteBundle
# from bundle.read_bundle import ReadBundle
# from bundle.internal_bundle import InternalBundle


# @toffee_test.testcase
# async def test_bundle(dut):
#     # 复位
#     dut.rst_n.value = 0
#     await dut.AStep(1)
#     dut.rst_n.value = 1
#     await dut.AStep(1)

#     write_bundle = WriteBundle.from_dict({
#         "we": "we_i",
#         "data": "data_i"
#     })
#     read_bundle = ReadBundle.from_dict({
#         "re": "re_i",
#         "data": "data_o"
#     })
#     internal_bundle = InternalBundle.from_dict({
#         "full": "full_o",
#         "empty": "empty_o"
#     })

#     # 然后分别绑定：
#     write_bundle.bind(dut)
#     read_bundle.bind(dut)
#     internal_bundle.bind(dut)

#     await write_bundle.enqueue(42)
#     val = await read_bundle.dequeue()
#     assert val == 42, f"Expected 42, got {val}"


# @toffee_test.testcase
# async def test_full_empty(dut):
#     # 复位
#     dut.rst_n.value = 0
#     await dut.AStep(1)
#     dut.rst_n.value = 1
#     await dut.AStep(1)

#     write_bundle = WriteBundle.from_dict({
#         "we": "we_i",
#         "data": "data_i"
#     })
#     read_bundle = ReadBundle.from_dict({
#         "re": "re_i",
#         "data": "data_o"
#     })
#     internal_bundle = InternalBundle.from_dict({
#         "full": "full_o",
#         "empty": "empty_o"
#     })

#     # 然后分别绑定：
#     write_bundle.bind(dut)
#     read_bundle.bind(dut)
#     internal_bundle.bind(dut)

#     input_seq = list(range(16))

#     # 装满 FIFO
#     for val in input_seq:
#         await write_bundle.enqueue(val)

#     assert internal_bundle.full.value == 1, "FIFO should be full"

#     # 清空 FIFO
#     output_seq = []
#     for _ in input_seq:
#         val = await read_bundle.dequeue()
#         output_seq.append(val)

#     assert internal_bundle.empty.value == 1, "FIFO should be empty"

#     assert input_seq == output_seq, f"Mismatch: {input_seq} != {output_seq}"

# @toffee_test.fixture
# async def dut(toffee_request: ToffeeRequest):
#     dut = toffee_request.create_dut(DUTSyncFIFO, "clk")
#     toffee.start_clock(dut) # 异步驱动时钟
#     return dut

from SyncFIFO import DUTSyncFIFO
import toffee
import toffee_test
from toffee_test import ToffeeRequest

from bundle.write_bundle import WriteBundle
from bundle.read_bundle import ReadBundle
from bundle.internal_bundle import InternalBundle
from agent.fifo_agent import FIFOAgent  # 你写的 FIFOAgent

@toffee_test.testcase
async def test_agent(dut):
    write_bundle = WriteBundle.from_dict({
        "we": "we_i",
        "data": "data_i"
    })
    read_bundle = ReadBundle.from_dict({
        "re": "re_i",
        "data": "data_o"
    })
    internal_bundle = InternalBundle.from_dict({
        "full": "full_o",
        "empty": "empty_o",
        "resetn": "rst_n"
    })

    # 然后分别绑定：
    write_bundle.bind(dut)
    read_bundle.bind(dut)
    internal_bundle.bind(dut)

    agent = FIFOAgent(read_bundle,write_bundle,internal_bundle)

    await agent.reset()
    await agent.enqueue(42)
    val = await agent.dequeue()
    assert val == 42, f"Expected 42, got {val}"


@toffee_test.testcase
async def test_full_empty(dut):
    write_bundle = WriteBundle.from_dict({
        "we": "we_i",
        "data": "data_i"
    })
    read_bundle = ReadBundle.from_dict({
        "re": "re_i",
        "data": "data_o"
    })
    internal_bundle = InternalBundle.from_dict({
        "full": "full_o",
        "empty": "empty_o",
        "resetn": "rst_n"
    })

    # 然后分别绑定：
    write_bundle.bind(dut)
    read_bundle.bind(dut)
    internal_bundle.bind(dut)

    agent = FIFOAgent(read_bundle,write_bundle,internal_bundle)

    await agent.reset()

    input_seq = list(range(16))

    for val in input_seq:
        await agent.enqueue(val)

    assert internal_bundle.full.value == 1, "FIFO should be full"

    output_seq = []
    for _ in input_seq:
        val = await agent.dequeue()
        output_seq.append(val)

    assert internal_bundle.empty.value == 1, "FIFO should be empty"
    assert input_seq == output_seq, f"Mismatch: {input_seq} != {output_seq}"


@toffee_test.fixture
async def dut(toffee_request: ToffeeRequest):
    dut = toffee_request.create_dut(DUTSyncFIFO, "clk")
    toffee.start_clock(dut)
    return dut