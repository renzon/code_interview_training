def time_lapse(total_seconds):
    minute_to_seconds = 60
    hour_to_seconds = minute_to_seconds * 60
    day_to_seconds = hour_to_seconds * 24

    days, remaining_seconds = divmod(total_seconds, day_to_seconds)
    hours, remaining_seconds = divmod(remaining_seconds, hour_to_seconds)
    minutes, remaining_seconds = divmod(remaining_seconds, minute_to_seconds)

    return days, hours, minutes, remaining_seconds

print(time_lapse(178615))
