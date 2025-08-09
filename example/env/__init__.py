from .agent import AdderAgent
from .refmodel import AdderModelWithDriverHook
from .refmodel import AdderModelWithMonitorHook
from toffee import *


class AdderEnv(Env):
    def __init__(self, adder_bundle):
        super().__init__()
        self.add_agent = AdderAgent(adder_bundle)

        self.attach(AdderModelWithDriverHook())
        self.attach(AdderModelWithMonitorHook())