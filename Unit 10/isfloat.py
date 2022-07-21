def checkFloat(userDistance):
    try:
        float(userDistance)
        return True
    except ValueError:
        return False