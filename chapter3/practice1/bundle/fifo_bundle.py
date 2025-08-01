from toffee import Bundle
from .write_bundle import WriteBundle
from .read_bundle import ReadBundle
from .internal_bundle import InternalBundle

class FIFOBundle(Bundle):
    # 将每个小 Bundle 作为子 Bundle，并绑定对应的 DUT 端口前缀
    write = WriteBundle.from_prefix("write_")
    read = ReadBundle.from_prefix("read_")
    internal = InternalBundle.from_prefix("internal_")
