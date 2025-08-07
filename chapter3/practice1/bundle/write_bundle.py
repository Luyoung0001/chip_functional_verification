from toffee import Bundle, Signals

class WriteBundle(Bundle):
    we, data = Signals(2)

    async def enqueue(self, data):
        self.data.value = data
        self.we.value = 1
        await self.step()
        self.we.value = 0
        await self.step()
    def is_full(self) -> bool:
        return self.agent.internal_bundle.full