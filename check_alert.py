from temp_breach_classify import classify_temperature_breach

def check_and_alert(alertTarget, batteryChar, temperatureInC):
    breachType = classify_temperature_breach(batteryChar['coolingType'], temperatureInC)
    
    if alertTarget == 'TO_CONTROLLER':
        send_to_controller(breachType)
    elif alertTarget == 'TO_EMAIL':
        send_to_email(breachType)
    else:
        raise ValueError(f"Unknown alert target: {alertTarget}")

def send_to_controller(breachType):
  header = 0xfeed
  print(f'{header}, {breachType}')
