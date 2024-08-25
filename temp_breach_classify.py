from breach_infer import infer_breach

def classify_temperature_breach(coolingType, temperatureInC):
    limits = {
        'PASSIVE_COOLING': (0, 35),
        'HI_ACTIVE_COOLING': (0, 45),
        'MED_ACTIVE_COOLING': (0, 40)
    }
    
    if coolingType not in limits:
        raise ValueError(f"Unknown cooling type: {coolingType}")
    
    lowerLimit, upperLimit = limits[coolingType]
    return infer_breach(temperatureInC, lowerLimit, upperLimit)
