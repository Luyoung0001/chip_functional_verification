#coding=utf8

try:
    from . import xspcomm as xsp
except Exception as e:
    import xspcomm as xsp

if __package__ or "." in __name__:
    from .libUT_SyncFIFO import *
else:
    from libUT_SyncFIFO import *


class DUTSyncFIFO(object):

    # initialize
    def __init__(self, *args, **kwargs):
        self.dut = DutUnifiedBase(*args)
        self.xclock = xsp.XClock(self.dut.pxcStep, self.dut.pSelf)
        self.xport  = xsp.XPort()
        self.xclock.Add(self.xport)
        self.event = self.xclock.getEvent()
        self.internal_signals = {}
        self.xcfg = xsp.XSignalCFG(self.dut.GetXSignalCFGPath(), self.dut.GetXSignalCFGBasePtr())

        # set output files
        if kwargs.get("waveform_filename"):
            self.dut.SetWaveform(kwargs.get("waveform_filename"))
        if kwargs.get("coverage_filename"):
            self.dut.SetCoverage(kwargs.get("coverage_filename"))

        # all Pins
        self.clk = xsp.XPin(xsp.XData(0, xsp.XData.In), self.event)
        self.rst_n = xsp.XPin(xsp.XData(0, xsp.XData.In), self.event)
        self.we_i = xsp.XPin(xsp.XData(0, xsp.XData.In), self.event)
        self.re_i = xsp.XPin(xsp.XData(0, xsp.XData.In), self.event)
        self.data_i = xsp.XPin(xsp.XData(32, xsp.XData.In), self.event)
        self.data_o = xsp.XPin(xsp.XData(32, xsp.XData.Out), self.event)
        self.full_o = xsp.XPin(xsp.XData(0, xsp.XData.Out), self.event)
        self.empty_o = xsp.XPin(xsp.XData(0, xsp.XData.Out), self.event)


        # BindDPI
        self.clk.BindDPIPtr(self.dut.GetDPIHandle("clk", 0), self.dut.GetDPIHandle("clk", 1))
        self.rst_n.BindDPIPtr(self.dut.GetDPIHandle("rst_n", 0), self.dut.GetDPIHandle("rst_n", 1))
        self.we_i.BindDPIPtr(self.dut.GetDPIHandle("we_i", 0), self.dut.GetDPIHandle("we_i", 1))
        self.re_i.BindDPIPtr(self.dut.GetDPIHandle("re_i", 0), self.dut.GetDPIHandle("re_i", 1))
        self.data_i.BindDPIPtr(self.dut.GetDPIHandle("data_i", 0), self.dut.GetDPIHandle("data_i", 1))
        self.data_o.BindDPIPtr(self.dut.GetDPIHandle("data_o", 0), self.dut.GetDPIHandle("data_o", 1))
        self.full_o.BindDPIPtr(self.dut.GetDPIHandle("full_o", 0), self.dut.GetDPIHandle("full_o", 1))
        self.empty_o.BindDPIPtr(self.dut.GetDPIHandle("empty_o", 0), self.dut.GetDPIHandle("empty_o", 1))


        # Add2Port
        self.xport.Add("clk", self.clk.xdata)
        self.xport.Add("rst_n", self.rst_n.xdata)
        self.xport.Add("we_i", self.we_i.xdata)
        self.xport.Add("re_i", self.re_i.xdata)
        self.xport.Add("data_i", self.data_i.xdata)
        self.xport.Add("data_o", self.data_o.xdata)
        self.xport.Add("full_o", self.full_o.xdata)
        self.xport.Add("empty_o", self.empty_o.xdata)


        # Cascaded ports
        self.data = self.xport.NewSubPort("data_")


    def __del__(self):
        self.Finish()

    ################################
    #         User APIs            #
    ################################
    def InitClock(self, name: str):
        self.xclock.Add(self.xport[name])

    def Step(self, i:int = 1):
        self.xclock.Step(i)

    def StepRis(self, callback, args=(), kwargs={}):
        self.xclock.StepRis(callback, args, kwargs)

    def StepFal(self, callback, args=(), kwargs={}):
        self.xclock.StepFal(callback, args, kwargs)

    def OpenWaveform(self):
        return self.dut.OpenWaveform()

    def CloseWaveform(self):
        return self.dut.CloseWaveform()

    def GetXPort(self):
        return self.xport

    def GetXClock(self):
        return self.xclock

    def SetWaveform(self, filename: str):
        self.dut.SetWaveform(filename)
    
    def FlushWaveform(self):
        self.dut.FlushWaveform()

    def SetCoverage(self, filename: str):
        self.dut.SetCoverage(filename)
    
    def CheckPoint(self, name: str) -> int:
        self.dut.CheckPoint(name)

    def Restore(self, name: str) -> int:
        self.dut.Restore(name)

    def GetInternalSignal(self, name: str, index=-1, is_array=False, use_vpi=False):
        if name not in self.internal_signals:
            signal = None
            if self.dut.GetXSignalCFGBasePtr() != 0 and not use_vpi:
                xname = "CFG:" + name
                if is_array:
                    assert index < 0, "Index is not supported for array signal"
                    signal = self.xcfg.NewXDataArray(name, xname)
                elif index >= 0:
                    signal = self.xcfg.NewXData(name, index, xname)
                else:
                    signal = self.xcfg.NewXData(name, xname)
            else:
                assert index < 0, "Index is not supported for VPI signal"
                assert not is_array, "Array is not supported for VPI signal"
                signal = xsp.XData.FromVPI(self.dut.GetVPIHandleObj(name),
                                           self.dut.GetVPIFuncPtr("vpi_get"),
                                           self.dut.GetVPIFuncPtr("vpi_get_value"),
                                           self.dut.GetVPIFuncPtr("vpi_put_value"), "VPI:" + name)
                if use_vpi:
                    assert signal is not None, f"Internal signal {name} not found (Check VPI is enabled)"
            if signal is None:
                return None
            if not isinstance(signal, xsp.XData):
                self.internal_signals[name] = [xsp.XPin(s, self.event) for s in signal]
            else:
                self.internal_signals[name] = xsp.XPin(signal, self.event)
        return self.internal_signals[name]

    def GetInternalSignalList(self, prefix="", deep=99, use_vpi=False):
        if self.dut.GetXSignalCFGBasePtr() != 0 and not use_vpi:
            return self.xcfg.GetSignalNames(prefix)
        else:
            return self.dut.VPIInternalSignalList(prefix, deep)

    def VPIInternalSignalList(self, prefix="", deep=99):
        return self.dut.VPIInternalSignalList(prefix, deep)

    def Finish(self):
        self.dut.Finish()

    def RefreshComb(self):
        self.dut.RefreshComb()

    ################################
    #      End of User APIs        #
    ################################

    def __getitem__(self, key):
        return xsp.XPin(self.port[key], self.event)

    # Async APIs wrapped from XClock
    async def AStep(self,i: int):
        return await self.xclock.AStep(i)

    async def ACondition(self,fc_cheker):
        return await self.xclock.ACondition(fc_cheker)

    def RunStep(self,i: int):
        return self.xclock.RunStep(i)

    def __setattr__(self, name, value):
        assert not isinstance(getattr(self, name, None),
                              (xsp.XPin, xsp.XData)), \
        f"XPin and XData of DUT are read-only, do you mean to set the value of the signal? please use `{name}.value = ` instead."
        return super().__setattr__(name, value)


if __name__=="__main__":
    dut=DUTSyncFIFO()
    dut.Step(100)
