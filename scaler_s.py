

class Scaler:
    scaler = None

def set_scaler(obj):
    Scaler.scaler = obj

def get_scaler():
    return Scaler.scaler
