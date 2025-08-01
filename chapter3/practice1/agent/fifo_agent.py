from toffee import Agent, driver_method, monitor_method

class FIFOAgent(Agent):
    def __init__(self, read_bundle, write_bundle, internal_bundle):
        # 将 read_bundle 传给父类以获取时钟
        super().__init__(read_bundle)
        self.read = read_bundle
        self.write = write_bundle
        self.internal = internal_bundle

    @driver_method()
    async def reset(self):
        self.internal.resetn.value = 0
        await self.internal.step()
        await self.internal.step()
        self.internal.resetn.value = 1
        await self.internal.step()

    @driver_method()
    async def enqueue(self, data):
        await self.write.enqueue(data)

    @driver_method()
    async def dequeue(self):
        return await self.read.dequeue()

    @monitor_method()
    async def monitor_once(self):
        return {
            "full": self.internal.full_o.value,
            "empty": self.internal.empty_o.value
        }
