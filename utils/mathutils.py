import math


def round_to_tick(number: float, tick: float) -> float:
    dp = round(-1 * math.log(tick, 10))
    return round(number, dp)


def ceil_amount(amount: float, precision: int) -> float:
    multiplier = pow(10, precision)
    rounded_amount = round(math.ceil(amount * multiplier) / multiplier, precision)
    return rounded_amount


def floor_amount(amount: float, precision: int) -> float:
    multiplier = pow(10, precision)
    rounded_amount = round(math.floor(amount * multiplier) / multiplier, precision)
    return rounded_amount
