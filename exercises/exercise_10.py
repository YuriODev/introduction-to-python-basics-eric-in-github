def calculate_minute_hand_angle(hour_angle):
	minute_angle = (hour_angle % 30) * 12
	return minute_angle

hour_angle = 127.5
minute_angle = calculate_minute_hand_angle(hour_angle)
print(minute_angle)