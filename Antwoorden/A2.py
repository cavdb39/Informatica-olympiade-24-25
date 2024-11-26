# Take inputs
begin_raw = input().replace(",", ".")
end_raw = input().replace(",", ".")

# Unpack lists
begin_inputs = [float(i) for i in begin_raw.split(":")]
begin_inputs = [0.0] * (3 - len(begin_inputs)) + begin_inputs

# Ensure input length of 3
end_inputs = [float(i) for i in end_raw.split(":")]
end_inputs = [0.0] * (3 - len(end_inputs)) + end_inputs

# Calculate total seconds and difference
begin_total_ms = int(
    1000 * (begin_inputs[0] * 3600 + begin_inputs[1] * 60 + begin_inputs[2])
)
end_total_ms = int(1000 * (end_inputs[0] * 3600 + end_inputs[1] * 60 + end_inputs[2]))
net_total_ms = end_total_ms - begin_total_ms

# Convert back to hours, minutes, seconds
hours = net_total_ms // 3600000
minutes = net_total_ms % 3600000 // 60000
seconds = net_total_ms % 60000 // 1000
centiseconds = round((net_total_ms % 1000) / 10)

# Convert floats into string format with colon
if hours > 0:
    time_str = f"{hours}:{minutes:02}:{seconds:02},{centiseconds:02}"
elif minutes > 0:
    time_str = f"{minutes}:{seconds:02},{centiseconds:02}"
elif seconds > 0:
    time_str = f"{seconds},{centiseconds:02}"
else:
    time_str = f"0,{centiseconds:02}"

# Print result
print(time_str)
