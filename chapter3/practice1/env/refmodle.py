from toffee import *

# 不使用独立执行流，为什么这样不好？
# 因为如果用独立执行流来写 REF_modle，这意味着要用 python 来模拟一个模块。
# 这就陷入了套娃，因为 python 模拟出来的模块并不知道正确与否，还得验证这个模拟的模块

# 因此，最好的验证思路就是直接对标 Agent 提供的驱动函数或者检测函数，每次回调的时候就简单的检查预期效果就行
# 验证步骤没有必要去验证系统功能的正确性，只需要验证子模块的正确性，这已经是最高层次了。
# 如果要上升到系统功能的正确性，就得跑仿真，这就是另一个话题了。


# 由于这是一个 FIFO，很难对其进行对比，因为驱动函数以及检测函数给出的数据都是一个 FIFO 给出的，
# 这里想要验证它，就得模拟一个
class FIFOModleWithDriverHook(Model):
    @driver_hook(agent_name="fifo_agent")
    def reset(self):
        return 0,0

