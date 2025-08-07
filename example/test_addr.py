from toffee import *

# 创建 bundle
# 我们可以在验证代码中预先定义好需要驱动的接口信号结构，
# 而不需要关心 DUT 具体的接口信号名称。通过 Bundle 提供的映射方法，可
# 以将信号映射至任意具有相同结构的 DUT 接口信号上，从而实现验证代码与 DUT 的解耦。
class AdderBundle(Bundle):
    a, b, cin, sum, cout = Signals(5)

# 创建 Agent
# 继续对 bundle 进行封装，使其变成更抽象的驱动方法和观测方法
class AdderAgent(Agent):
    @driver_method()
    async def exec_add(self, a, b, cin):
        self.bundle.a.value = a
        self.bundle.b.value = b
        self.bundle.cin.value = cin
        await self.bundle.step()
        return self.bundle.sum.value, self.bundle.cout.value


# test_adder.py (continued)
import toffee_test
from picker_out_adder import DUTAdder

@toffee_test.testcase
async def test_adder():
    adder = DUTAdder()                                        # 实例化加法器
    start_clock(adder)                                        # 启动 toffee 内置时钟
    adder_bundle = AdderBundle.from_prefix("io_").bind(adder) # 利用前缀映射方法将 Bundle 与 DUT 进行绑定
    adder_agent = AdderAgent(adder_bundle)                    # 实例化 Agent
    sum, cout = await adder_agent.exec_add(1, 2, 0)           # 调用驱动方法
    assert sum == 3 and cout == 0                             # 验证输出结果
