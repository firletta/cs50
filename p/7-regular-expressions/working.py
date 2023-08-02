import re

def convert(time_str):
    pattern = r"(\d{1,2})(?::(\d{1,2}))?\s*(AM|PM) to (\d{1,2})(?::(\d{1,2}))?\s*(AM|PM)"
    match = re.fullmatch(pattern, time_str)
    
    if not match:
        raise ValueError("Invalid time string")
        
    start_hour, start_min, start_ampm, end_hour, end_min, end_ampm = match.groups()
    start_hour, start_min, end_hour, end_min = int(start_hour), int(start_min) if start_min else 0, int(end_hour), int(end_min) if end_min else 0
    
    if any(x > 12 for x in [start_hour, end_hour]) or any(x > 59 for x in [start_min, end_min]):
        raise ValueError("Invalid time string")

    start_hour = start_hour + 12 if start_ampm == 'PM' and start_hour < 12 else start_hour
    end_hour = end_hour + 12 if end_ampm == 'PM' and end_hour < 12 else end_hour
    
    start_time = f"{start_hour:02d}:{start_min:02d}"
    end_time = f"{end_hour:02d}:{end_min:02d}"
    
    return f"{start_time} to {end_time}"

def main():
    print(convert(input("Hours: ")))
    
if __name__ == "__main__":
    main()