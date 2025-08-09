from toffee import *


class AdderModelWithDriverHook(Model):
    @driver_hook(agent_name="add_agent")
    def exec_add(self, a, b, cin):
        result = a + b + cin
        sum = result & ((1 << 64) - 1)
        cout = result >> 64
        return sum, cout


class AdderModelWithMonitorHook(Model):
    @monitor_hook(agent_name="add_agent")
    def monitor_once(self, item):
        sum = item["a"] + item["b"] + item["cin"]
        assert sum & ((1 << 64) - 1) == item["sum"]
        assert sum >> 64 == item["cout"]