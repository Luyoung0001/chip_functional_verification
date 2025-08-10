from toffee import Agent, driver_method, monitor_method

# 这里仅仅设置了一个 FIFOAgent，它绑定了 4 个 bundle
# 它是 Bundle 的上层，这里实现基本的驱动方法和观测方法
class FIFOAgent(Agent):
    def __init__(self, read_bundle, write_bundle, internal_bundle, resetn_bundle):
        # 将 read_bundle 传给父类以获取时钟
        super().__init__(read_bundle)
        self.read = read_bundle
        self.write = write_bundle
        self.internal = internal_bundle
        self.resetn = resetn_bundle

        self.wptr = 0  # 写指针信号
        self.rptr = 0  # 读指针信号

    @driver_method()
    async def reset(self):
        self.resetn.resetn.value = 0
        # 复位两个周期
        await self.read.step()
        await self.read.step()
        self.resetn.resetn.value = 1
        await self.internal.step()

        # 复位后清空指针值
        self.wptr = 0
        self.rptr = 0

        return self.wptr, self.rptr

    @driver_method()
    async def enqueue(self, data):
        self.write.we.value = 1
        self.write.data.value = data
        await self.read.step()
        self.write.we.value = 0
        await self.read.step()

        # 更新写指针
        self.wptr += 1  # 假设每次写入后，写指针增加 1

    @driver_method()
    async def dequeue(self):
        self.read.re.value = 1
        await self.read.step()

        self.read.re.value = 0
        await self.read.step()

        self.rptr += 1  # 假设每次读取后，读指针增加 1
        return self.read.data.value

    @monitor_method()
    async def monitor_once(self):
        return {
            "full": self.internal.full.value,
            "empty": self.internal.empty.value,
            "wptr": self.wptr,  # 返回写指针
            "rptr": self.rptr,   # 返回读指针
            "dequeue_data": self.read.data.value # 返回的数据
        }
