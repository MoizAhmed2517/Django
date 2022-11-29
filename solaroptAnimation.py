solar = 3200
grid = 0
bess = 120
genset = 0
load = 3209
net_metering = False
SOC = 11

# Choose your own variables or use from Inverter or different energy assets

control_vals = {'solarVal': 0, 'solarGridVal': 0, 'SolarBatteryVal': 0, 'gridVal': 0, 'batteryVal': 0,
                'generatorVal': 0, 'loadVal': 1, 'gridBatVal': 0, 'genVatVal': 0, 'genGridVal': -1,
                'Comments': 'Comment will be updated Case wise'}

def operation(solar, grid, bess, genset, load):
    """
    This function return the animation control values based on different scenarios.
    :param solar: Takes current value of solar to check either it is available or not.
    :param grid: Takes current value of grid to check either it is available or not.
    :param bess: Takes current value of bess, make it absolute to check either it is available or not.
    :param genset: Takes current value of genset to check either it is available or not.
    :param load: Always available.
    :return: The mapping for variables as -1, 0, 1s
    """

    # Case#A:
    if solar > 0 and grid > 0:
        if net_metering:
            if solar > load:
                control_vals.update(
                    {'solarVal': 1, 'solarGridVal': 1, 'SolarBatteryVal': -1, 'gridVal': 0, 'batteryVal': -1,
                     'generatorVal': -1, 'loadVal': 1, 'gridBatVal': -1, 'genVatVal': -1, 'genGridVal': -1})
                return control_vals
            elif solar < load:
                control_vals.update(
                    {'solarVal': 1, 'solarGridVal': 0, 'SolarBatteryVal': -1, 'gridVal': 1, 'batteryVal': -1,
                     'generatorVal': -1, 'loadVal': 1, 'gridBatVal': -1, 'genVatVal': -1, 'genGridVal': -1})
                return control_vals
        else:
            control_vals.update(
                {'solarVal': 1, 'solarGridVal': -1, 'SolarBatteryVal': -1, 'gridVal': 1, 'batteryVal': -1,
                 'generatorVal': -1, 'loadVal': 1, 'gridBatVal': -1, 'genVatVal': -1, 'genGridVal': -1})
            return control_vals

    # Case D:
    elif solar > 0 and genset > 0:
        if solar > load:
            control_vals.update(
                {'solarVal': 1, 'solarGridVal': -1, 'SolarBatteryVal': -1, 'gridVal': -1, 'batteryVal': -1,
                 'generatorVal': 1, 'loadVal': 1, 'gridBatVal': -1, 'genVatVal': -1, 'genGridVal': -1})
            return control_vals
        elif solar < load:
            control_vals.update(
                {'solarVal': 1, 'solarGridVal': -1, 'SolarBatteryVal': -1, 'gridVal': -1, 'batteryVal': -1,
                 'generatorVal': 1, 'loadVal': 1, 'gridBatVal': -1, 'genVatVal': -1, 'genGridVal': -1})
            return control_vals

    # Case E:
    elif solar > 0 and bess > 0:
        if solar > load:
            if SOC < 90:
                control_vals.update(
                    {'solarVal': 1, 'solarGridVal': -1, 'SolarBatteryVal': 1, 'gridVal': -1, 'batteryVal': 0,
                     'generatorVal': -1, 'loadVal': 1, 'gridBatVal': -1, 'genVatVal': -1, 'genGridVal': -1})
                return control_vals
            elif SOC > 90:
                control_vals.update(
                    {'solarVal': 1, 'solarGridVal': -1, 'SolarBatteryVal': 0, 'gridVal': -1, 'batteryVal': 0,
                     'generatorVal': -1, 'loadVal': 1, 'gridBatVal': -1, 'genVatVal': -1, 'genGridVal': -1})
                return control_vals

        elif (solar < load) and (SOC > 11):
            control_vals.update(
                {'solarVal': 1, 'solarGridVal': -1, 'SolarBatteryVal': 0, 'gridVal': -1, 'batteryVal': 1,
                 'generatorVal': -1, 'loadVal': 1, 'gridBatVal': -1, 'genVatVal': -1, 'genGridVal': -1})
            return control_vals

        else:
            control_vals.update(
                {'solarVal': 1, 'solarGridVal': -1, 'SolarBatteryVal': 0, 'gridVal': -1, 'batteryVal': 0,
                 'generatorVal': -1, 'loadVal': 1, 'gridBatVal': -1, 'genVatVal': -1, 'genGridVal': -1})
            return control_vals

    # Case C:
    elif solar > 0 and grid > 0 and genset > 0:
        if (solar > load) and (solar < load) and (solar == load):
            control_vals.update(
                {'solarVal': 1, 'solarGridVal': -1, 'SolarBatteryVal': 0, 'gridVal': -1, 'batteryVal': 0,
                 'generatorVal': -1, 'loadVal': 1, 'gridBatVal': -1, 'genVatVal': -1, 'genGridVal': -1})
            return control_vals

    # Case B:
    if solar > 0 and grid > 0 and bess > 0:
        if solar > load:
            if (net_metering == True) and (SOC < 90):
                control_vals.update(
                    {'solarVal': 1, 'solarGridVal': 0, 'SolarBatteryVal': 1, 'gridVal': 0, 'batteryVal': 0,
                     'generatorVal': -1, 'loadVal': 1, 'gridBatVal': -1, 'genVatVal': -1, 'genGridVal': -1})
                return control_vals
            elif (net_metering == True) and (SOC > 90):
                control_vals.update(
                    {'solarVal': 1, 'solarGridVal': 1, 'SolarBatteryVal': 0, 'gridVal': 0, 'batteryVal': 0,
                     'generatorVal': -1, 'loadVal': 1, 'gridBatVal': -1, 'genVatVal': -1, 'genGridVal': -1})
                return control_vals
            elif (net_metering == False) and (SOC > 90):
                control_vals.update(
                    {'solarVal': 1, 'solarGridVal': -1, 'SolarBatteryVal': 1, 'gridVal': 0, 'batteryVal': 0,
                     'generatorVal': -1, 'loadVal': 1, 'gridBatVal': -1, 'genVatVal': -1, 'genGridVal': -1})
                return control_vals
        elif solar < load:
            if (SOC <=100) and (SOC > 10):
                control_vals.update(
                    {'solarVal': 1, 'solarGridVal': -1, 'SolarBatteryVal': -1, 'gridVal': 0, 'batteryVal': 1,
                     'generatorVal': -1, 'loadVal': 1, 'gridBatVal': -1, 'genVatVal': -1, 'genGridVal': -1})
                return control_vals
            elif (SOC <= 50) and (SOC > 10):
                control_vals.update(
                    {'solarVal': 1, 'solarGridVal': -1, 'SolarBatteryVal': -1, 'gridVal': 1, 'batteryVal': 1,
                     'generatorVal': -1, 'loadVal': 1, 'gridBatVal': -1, 'genVatVal': -1, 'genGridVal': -1})
                return control_vals
            elif SOC <= 10:
                control_vals.update(
                    {'solarVal': 1, 'solarGridVal': -1, 'SolarBatteryVal': -1, 'gridVal': 1, 'batteryVal': -1,
                     'generatorVal': -1, 'loadVal': 1, 'gridBatVal': 1, 'genVatVal': -1, 'genGridVal': -1})
                return control_vals

    # Case F:
    elif solar > 0 and genset > 0 and bess > 0:
        if (solar > load) and (SOC == 90):
            control_vals.update(
                {'solarVal': 1, 'solarGridVal': -1, 'SolarBatteryVal': -1, 'gridVal': -1, 'batteryVal': 0,
                 'generatorVal': 1, 'loadVal': 1, 'gridBatVal': -1, 'genVatVal': -1, 'genGridVal': -1})
            return control_vals
        elif (solar > load) and (SOC < 100):
            control_vals.update(
                {'solarVal': 1, 'solarGridVal': -1, 'SolarBatteryVal': 1, 'gridVal': -1, 'batteryVal': 0,
                 'generatorVal': 1, 'loadVal': 1, 'gridBatVal': -1, 'genVatVal': -1, 'genGridVal': -1})
            return control_vals
        elif (solar < load) and (SOC <= 100) and (SOC > 10):
            control_vals.update(
                {'solarVal': 1, 'solarGridVal': -1, 'SolarBatteryVal': -1, 'gridVal': -1, 'batteryVal': 1,
                 'generatorVal': 1, 'loadVal': 1, 'gridBatVal': -1, 'genVatVal': -1, 'genGridVal': -1})
            return control_vals
        elif (solar < load) and (SOC <= 10):
            control_vals.update(
                {'solarVal': 1, 'solarGridVal': -1, 'SolarBatteryVal': -1, 'gridVal': -1, 'batteryVal': 0,
                 'generatorVal': 1, 'loadVal': 1, 'gridBatVal': -1, 'genVatVal': 1, 'genGridVal': -1})
            return control_vals

print(operation(solar, grid, bess, genset, load))
