# -----------------------------------------------------------------------------
# Copyright 2024 Arkadiusz Cholewinski. Licensed under the Apache License, Version 2.0.
# See: http://www.apache.org/licenses/LICENSE-2.0
# Author: Arkadiusz Cholewinski
# Date: 2024-11-22
# -----------------------------------------------------------------------------

from powerMonitor import *
        
if __name__ == "__main__":

    powermonitor_device = '<path_to_usb_power_shield_virtual_comport>'
    power_monitor = PowerMonitor()
    power_monitor.setup(power_device_path=powermonitor_device)
    power_monitor.measure(time=200, unit='ms', reset=False)