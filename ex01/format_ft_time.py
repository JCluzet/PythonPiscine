from datetime import datetime

timestamp = datetime.now().timestamp()
formatted_timestamp = f"{timestamp:,.4f}"
formatted_timestampExp = f"{timestamp:.2e}"

print("Seconds since January 1, 1970:", formatted_timestamp + " or " + formatted_timestampExp + " in scientific notation")
print(datetime.now().strftime("%b %d %Y"))