# power_monitor_stm32l562e_dk

### Usage
```
from powerMonitor import *

if __name__=="__main__:
    powermonitor_device = '<path_to_usb_power_shield_virtual_comport>'
    power_monitor = PowerMonitor()
    power_monitor.setup(power_device_path=powermonitor_device)
    power_monitor.measure(time=200, unit='ms', reset=False)
```
