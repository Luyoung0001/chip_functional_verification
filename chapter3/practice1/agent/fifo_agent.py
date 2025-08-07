from toffee import Agent, driver_method, monitor_method, Signal

class FIFOAgent(Agent):
    def __init__(self, read_bundle, write_bundle, internal_bundle):
        # 将 read_bundle 传给父类以获取时钟
        super().__init__(read_bundle)
        self.read = read_bundle
        self.write = write_bundle
        self.internal = internal_bundle

        # 假设指针是内部信号，需要手动定义它们
        self.wptr = Signal()  # 写指针信号
        self.rptr = Signal()  # 读指针信号

    @driver_method()
    async def reset(self):
        self.internal.resetn.value = 0
        await self.internal.step()
        await self.internal.step()
        self.internal.resetn.value = 1
        await self.internal.step()

        # 复位后清空指针值
        self.wptr.value = 0
        self.rptr.value = 0


    @driver_method()
    async def enqueue(self, data):
        await self.write.enqueue(data)
        # 更新写指针
        self.wptr.value += 1  # 假设每次写入后，写指针增加 1

    @driver_method()
    async def dequeue(self):
        self.rptr.value += 1  # 假设每次读取后，读指针增加 1
        return await self.read.dequeue()

    @monitor_method()
    async def monitor_once(self):
        return {
            "full": self.internal.full.value,
            "empty": self.internal.empty.value,
            "wptr": self.wptr.value,  # 返回写指针
            "rptr": self.rptr.value   # 返回读指针
        }
