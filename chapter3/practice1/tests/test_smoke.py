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

# from SyncFIFO import DUTSyncFIFO
# import toffee
# import toffee_test
# from toffee_test import ToffeeRequest
# from coverage import get_cover_group_fifo_state, get_cover_group_basic_operations

# from bundle.write_bundle import WriteBundle
# from bundle.read_bundle import ReadBundle
# from bundle.internal_bundle import InternalBundle
# from agent.fifo_agent import FIFOAgent  # 你写的 FIFOAgent

# @toffee_test.testcase
# async def test_agent(dut):
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
#         "empty": "empty_o",
#         "resetn": "rst_n"
#     })

#     # 然后分别绑定：
#     write_bundle.bind(dut)
#     read_bundle.bind(dut)
#     internal_bundle.bind(dut)

#     agent = FIFOAgent(read_bundle,write_bundle,internal_bundle)

#     await agent.reset()
#     await agent.enqueue(42)
#     val = await agent.dequeue()
#     assert val == 42, f"Expected 42, got {val}"


# @toffee_test.testcase
# async def test_full_empty(dut):
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
#         "empty": "empty_o",
#         "resetn": "rst_n"
#     })

#     # 然后分别绑定：
#     write_bundle.bind(dut)
#     read_bundle.bind(dut)
#     internal_bundle.bind(dut)

#     agent = FIFOAgent(read_bundle,write_bundle,internal_bundle)

#     await agent.reset()

#     input_seq = list(range(16))

#     for val in input_seq:
#         await agent.enqueue(val)

#     assert internal_bundle.full.value == 1, "FIFO should be full"

#     output_seq = []
#     for _ in input_seq:
#         val = await agent.dequeue()
#         output_seq.append(val)

#     assert internal_bundle.empty.value == 1, "FIFO should be empty"
#     assert input_seq == output_seq, f"Mismatch: {input_seq} != {output_seq}"


# @toffee_test.fixture
# async def dut(toffee_request: ToffeeRequest):
#     dut = toffee_request.create_dut(DUTSyncFIFO, "clk")
#     toffee.start_clock(dut)
#     return dut
from SyncFIFO import DUTSyncFIFO
import toffee
import toffee_test
from toffee_test import ToffeeRequest

from bundle.write_bundle import WriteBundle
from bundle.read_bundle import ReadBundle
from bundle.internal_bundle import InternalBundle
from agent.fifo_agent import FIFOAgent  # 假设已有 FIFOAgent

from cover.fifo_coverage import get_cover_group_fifo_state, get_cover_group_basic_operations, get_cover_group_boundary_conditions, get_cover_group_data_integrity


# FIFO Agent Test Case: 基本操作
@toffee_test.testcase
async def test_agent(fifo_agent):
    # Reset FIFO and test basic enqueue/dequeue functionality
    await fifo_agent.reset()
    await fifo_agent.enqueue(42)  # 写入数据 42
    val = await fifo_agent.dequeue()  # 读取数据
    assert val == 42, f"Expected 42, but got {val}"

# FIFO Full and Empty Conditions Test Case: 边界状态测试（FIFO 满/空）
@toffee_test.testcase
async def test_full_empty(fifo_agent):
    await fifo_agent.reset()

    # Enqueue elements until FIFO is full
    input_seq = list(range(16))  # 生成16个元素
    for val in input_seq:
        await fifo_agent.enqueue(val)

    # Dequeue all elements
    output_seq = []
    for _ in input_seq:
        val = await fifo_agent.dequeue()
        output_seq.append(val)

    # Check if data consistency is maintained (First-in, First-out order)
    assert input_seq == output_seq, f"Expected {input_seq}, but got {output_seq}"

# FIFO Boundary Test: 边界情况测试（FIFO 空时读取、FIFO 满时写入等）
@toffee_test.testcase
async def test_fifo_boundary(fifo_agent):
    await fifo_agent.reset()

    # Enqueue until FIFO is full
    for i in range(16):
        await fifo_agent.enqueue(i)

    # Now dequeue all elements
    output_seq = []
    for i in range(16):
        val = await fifo_agent.dequeue()
        output_seq.append(val)

    # Assert data integrity and order
    assert output_seq == list(range(16)), f"Expected output to be {list(range(16))}, but got {output_seq}"

# FIFO Reset Behavior Test: 复位行为测试
@toffee_test.testcase
async def test_reset_behavior(fifo_agent):
    # Enqueue some data
    await fifo_agent.enqueue(100)

    # Now reset the FIFO
    await fifo_agent.reset()

    # Check if FIFO is empty and read operation returns None or an expected default value
    val = await fifo_agent.dequeue()
    assert val is None, f"Expected None (empty FIFO), but got {val}"

# Fixture for FIFO Agent: 为每个测试用例准备 FIFO Agent
@toffee_test.fixture
async def fifo_agent(toffee_request: ToffeeRequest):
    dut = toffee_request.create_dut(DUTSyncFIFO, "clk")
    toffee.start_clock(dut)

    # 绑定 Bundle
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

    write_bundle.bind(dut)
    read_bundle.bind(dut)
    internal_bundle.bind(dut)

    # 创建 FIFO Agent
    fifo_agent = FIFOAgent(read_bundle, write_bundle, internal_bundle)

    # 添加覆盖组
    toffee_request.add_cov_groups([
        get_cover_group_fifo_state(fifo_agent),
        get_cover_group_basic_operations(fifo_agent),
        get_cover_group_boundary_conditions(fifo_agent),
        get_cover_group_data_integrity(fifo_agent)
    ])

    return fifo_agent
