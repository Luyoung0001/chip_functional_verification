from toffee.funcov import CovGroup
from agent.fifo_agent import FIFOAgent  # 假设已有 FIFOAgent
from toffee.funcov import *

from toffee import CovGroup, CovEq

# 写操作检查
def check_write_operation(agent: FIFOAgent) -> bool:
    return agent.write.we.value and not agent.internal.full.value

# 读操作检查
def check_read_operation(agent: FIFOAgent) -> bool:
    return agent.read.re.value and not agent.internal.empty.value

# 没有操作检查
def check_none_operation(agent: FIFOAgent) -> bool:
    return not agent.write.we.value and not agent.read.re.value

# 边界情况检查
def check_read_when_empty(agent: FIFOAgent) -> bool:
    return check_read_operation(agent) and agent.internal.empty.value

def check_write_when_full(agent: FIFOAgent) -> bool:
    return check_write_operation(agent) and agent.internal.full.value

def check_write_when_empty(agent: FIFOAgent) -> bool:
    return check_write_operation(agent) and agent.internal.empty.value

def check_read_when_full(agent: FIFOAgent) -> bool:
    return check_read_operation(agent) and agent.internal.full.value

# 监控 FIFO 状态（满和空）
def get_cover_group_fifo_state(agent: FIFOAgent) -> CovGroup:
    group = CovGroup("FIFO State")
    group.add_watch_point(agent.internal.full, {
        "full": CovEq(1),
        "not_full": CovEq(0),
    }, name="Full signal")
    group.add_watch_point(agent.internal.empty, {
        "empty": CovEq(1),
        "not_empty": CovEq(0),
    }, name="Empty signal")
    return group

# 边界情况覆盖组
def get_cover_group_boundary_conditions(agent: FIFOAgent) -> CovGroup:
    group = CovGroup("Boundary conditions")
    group.add_watch_point(agent, {
        "read_when_empty": check_read_when_empty,
        "write_when_full": check_write_when_full,
        "write_when_empty": check_write_when_empty,
        "read_when_full": check_read_when_full,
    }, name="Boundary Conditions")
    return group

# 监控指针行为（写指针和读指针）
def check_wptr_wraparound(agent: FIFOAgent) -> bool:
    return agent.wptr.value == 16

def check_rptr_wraparound(agent: FIFOAgent) -> bool:
    return agent.rptr.value == 16

def check_wptr_equals_rptr(agent: FIFOAgent) -> bool:
    return agent.wptr.value == agent.rptr.value

def get_cover_group_pointer_behavior(agent: FIFOAgent) -> CovGroup:
    group = CovGroup("Pointer behavior")
    group.add_watch_point(agent, {
        "wptr_wraparound": check_wptr_wraparound,
        "rptr_wraparound": check_rptr_wraparound,
        "wptr_equals_rptr": check_wptr_equals_rptr,
    }, name="Pointer behavior")
    return group

# 数据完整性检查
def check_data_written_and_read(agent: FIFOAgent) -> bool:
    return agent.write.we.value and agent.read.re.value and agent.read.data.value == agent.write.data.value

def get_cover_group_data_integrity(agent: FIFOAgent) -> CovGroup:
    group = CovGroup("Data Integrity")
    group.add_watch_point(agent, {
        "data_written_and_read": check_data_written_and_read,
    }, name="Data Integrity")
    return group

# 复位行为检查
def check_fifo_empty_after_reset(agent: FIFOAgent) -> bool:
    return agent.internal.empty.value == 1

def check_pointer_reset(agent: FIFOAgent) -> bool:
    return agent.wptr.value == 0 and agent.rptr.value == 0

def get_cover_group_reset_behavior(agent: FIFOAgent) -> CovGroup:
    group = CovGroup("Reset behavior")
    group.add_watch_point(agent, {
        "fifo_empty_after_reset": check_fifo_empty_after_reset,
        "pointer_reset": check_pointer_reset,
    }, name="Reset behavior")
    return group

# 基本操作覆盖组（写操作和读操作）
def get_cover_group_basic_operations(agent: FIFOAgent) -> CovGroup:
    group = CovGroup("Basic operations")
    group.add_watch_point(agent.write, {"write_occurs": check_write_operation}, name="Write operation")
    group.add_watch_point(agent.read, {"read_occurs": check_read_operation}, name="Read operation")
    group.add_watch_point(agent, {"no_operation": check_none_operation}, name="No operation")
    return group
