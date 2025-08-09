from .fifoAgent import FIFOAgent
from .refmodle import FIFOModle
from toffee import *


class FIFOEnv(Env):
    def __init__(self,read_bundle, write_bundle, internal_bundle, resetn_bundle):
        super().__init__()
        self.fifo_agent = FIFOAgent(read_bundle, write_bundle, internal_bundle, resetn_bundle)
        # 添加 hook
        self.attach(FIFOModle())

