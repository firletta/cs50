import re

def main():
    print(parse(input("HTML: ")))

def parse(html):
    iframe_pattern = r'<iframe.*?src="(.+?)"' 
    match = re.search(iframe_pattern, html)

    if match:
        src = match.group(1)
        if "youtube" in src and "/embed/" in src:
            video_id = src.split("/embed/")[1]
            return f"https://youtu.be/{video_id}"
        
    return None


if __name__ == "__main__":
    main()