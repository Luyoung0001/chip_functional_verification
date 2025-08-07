from toffee import *


class AdderBundle(Bundle):
    a, b, cin, sum, cout = Signals(5)

# self.bundle 是 AdderAgent 的一个实例变量，表示要操作的信号。
class AdderAgent(Agent):
    @driver_method()
    async def exec_add(self, a, b, cin):
        self.bundle.a.value = a
        self.bundle.b.value = b
        self.bundle.cin.value = cin
        await self.bundle.step()
        return self.bundle.sum.value, self.bundle.cout.value

    @monitor_method()
    async def monitor_once(self):
        return self.bundle.as_dict()