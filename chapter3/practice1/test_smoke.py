from picker_out_SyncFIFO import DUTSyncFIFO
import toffee
import toffee_test
from toffee_test import ToffeeRequest

from bundle.write_bundle import WriteBundle
from bundle.read_bundle import ReadBundle
from bundle.internal_bundle import InternalBundle
from bundle.resetn_bundle import ResetnBundle
from env import FIFOEnv

from toffee import *
@toffee_test.testcase
async def test_full_empty(fifo_env):
    await fifo_env.fifo_agent.reset()
    input_seq = list(range(16))  # 生成16个元素
    for val in input_seq:
        await fifo_env.fifo_agent.enqueue(val)

    output_seq = []
    for _ in input_seq:
        val = await fifo_env.fifo_agent.dequeue()
        output_seq.append(val)

@toffee_test.testcase
async def test_fifo_boundary(fifo_env):
    await fifo_env.fifo_agent.reset()

    for i in range(16):
        await fifo_env.fifo_agent.enqueue(i)

    # Now dequeue all elements
    for i in range(16):
        await fifo_env.fifo_agent.dequeue()


@toffee_test.testcase
async def test_reset_behavior(fifo_env):
    await fifo_env.fifo_agent.reset()
    await fifo_env.fifo_agent.enqueue(100)
    # Now reset the FIFO
    await fifo_env.fifo_agent.reset()

    # await fifo_env.fifo_agent.dequeue()

import toffee.funcov as fc
from toffee.funcov import CovGroup


def fifo_cover_point(fifo):
    # 创建测试组
    g = CovGroup("FIFO addition function")

    # 添加测试点
    g.add_cover_point(fifo.rst_n, {"rst_n is 0": fc.Eq(0)}, name="rst_n is 0")
    g.add_cover_point(fifo.rst_n, {"rst_n is 1": fc.Eq(1)}, name="rst_n is 1")

    g.add_cover_point(fifo.we_i,  {"we_i is 0": fc.Eq(0)}, name="we_i is 0")
    g.add_cover_point(fifo.we_i,  {"we_i is 1": fc.Eq(1)}, name="we_i is 1")

    g.add_cover_point(fifo.re_i, {"re_i is 0": fc.Eq(0)}, name="re_i is 0")
    g.add_cover_point(fifo.re_i, {"re_i is 1": fc.Eq(1)}, name="re_i is 1")

    g.add_cover_point(fifo.full_o, {"full_o is 0": fc.Eq(0)}, name="full_o is 0")
    g.add_cover_point(fifo.full_o, {"full_o is 1": fc.Eq(1)}, name="full_o is 1")

    g.add_cover_point(fifo.empty_o, {"empty_o is 0": fc.Eq(0)}, name="empty_o is 0")
    g.add_cover_point(fifo.empty_o, {"empty_o is 1": fc.Eq(1)}, name="empty_o is 1")

    return g


# Fixture for FIFO Agent: 为每个测试用例准备 FIFO Agent
@toffee_test.fixture
async def fifo_env(toffee_request: toffee_test.ToffeeRequest):
    dut = toffee_request.create_dut(DUTSyncFIFO, "clk")
    # 添加测试组
    toffee_request.add_cov_groups(fifo_cover_point(dut))

    # 绑定 Bundle
    read_bundle = ReadBundle.from_dict({
        "re": "re_i",
        "data": "data_o"
    })
    write_bundle = WriteBundle.from_dict({
        "we": "we_i",
        "data": "data_i"
    })
    internal_bundle = InternalBundle.from_dict({
        "full": "full_o",
        "empty": "empty_o"
    })
    resetn_bundle = ResetnBundle.from_dict({
        "resetn" : "rst_n"
    })

    read_bundle.bind(dut)
    write_bundle.bind(dut)
    internal_bundle.bind(dut)
    resetn_bundle.bind(dut)

    toffee.start_clock(dut)

    # 创建 FIFO Agent
    return FIFOEnv(read_bundle, write_bundle, internal_bundle, resetn_bundle)
