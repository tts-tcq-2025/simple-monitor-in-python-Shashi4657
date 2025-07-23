
def is_temperature_ok(temperature):
  return 0 <= temperature <= 45

def is_soc_ok(soc):
  return 20 <= soc <= 80

def is_charge_rate_ok(charge_rate):
  return charge_rate <= 0.8

def battery_is_ok(temperature, soc, charge_rate):
  if not is_temperature_ok(temperature):
    print('Temperature is out of range!')
    return False
  if not is_soc_ok(soc):
    print('State of Charge is out of range!')
    return False
  if not is_charge_rate_ok(charge_rate):
    print('Charge rate is out of range!')
    return False
  return True

if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
