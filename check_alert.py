from temp_breach_classify import classify_temperature_breach
from alert_send import send_to_controller,send_to_email

def check_and_alert(alertTarget, batteryChar, temperatureInC):
    breachType = classify_temperature_breach(batteryChar['coolingType'], temperatureInC)
    
    if alertTarget == 'TO_CONTROLLER':
        send_to_controller(breachType)
    elif alertTarget == 'TO_EMAIL':
        send_to_email(breachType)
    else:
        raise ValueError(f"Unknown alert target: {alertTarget}")

