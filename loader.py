import asyncio


class Loader:
    def __init__(self):
        self.id = "GBC4V4"
        self.queue = []

    async def hlai(self, item):
        await asyncio.sleep(0)
        self.queue.append(item)
        return len(self.queue)


async def main():
    obj = Loader()
    for i in range(8):
        await obj.hlai(i)
    print(obj.queue)


if __name__ == "__main__":
    asyncio.run(main())
