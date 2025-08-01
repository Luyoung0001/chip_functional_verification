try:
    from UT_RandomGenerator import *
except:
    try:
        from RandomGenerator import *
    except:
        from __init__ import *


if __name__ == "__main__":
    dut = DUTRandomGenerator()
    # dut.InitClock("clk")

    dut.Step(1)

    dut.Finish()
