from toffee import Bundle, Signals

class ReadBundle(Bundle):
    re, data = Signals(2)

    async def dequeue(self):
        self.re.value = 1
        await self.step()
        self.re.value = 0
        await self.step()
        return self.data.value
