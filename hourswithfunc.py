def computepay(hours, rate):
    if hours > 40:
        pay = 1.5 * rate * (hours - 40) + (40 * rate)
    else:
        pay = hours * rate
    return pay


enter_hours = input("Enter Hours:")
hour_conv = float(enter_hours)
rate_per_hour = input("Enter rate per hour:")
rphr_conv = float(rate_per_hour)

total = computepay(hour_conv, rphr_conv)
print('Pay', total)
