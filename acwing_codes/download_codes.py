#!/usr/bin/env python3
"""Download all AC codes from AcWing grammar basic course."""
import json
import os
import re
import time
import requests

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MAPPING_FILE = os.path.join(BASE_DIR, "mapping.json")

COOKIES = {
    "csrftoken": "KL03dlexHbMlKtBRbuK8KTUStLjpiBWP6TUpji1k8uCXR23R2ouDXMEf8u6p5Pl4",
    "sessionid": "sahkgb8th6skmh2ypj6obxo991d1hstz",
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}

session = requests.Session()
session.cookies.update(COOKIES)
session.headers.update(HEADERS)

def sanitize_filename(name):
    """Remove chars that are invalid in filenames."""
    return re.sub(r'[\\/:*?"<>|]', '_', name)

def fetch_code(code_id):
    """Fetch the code content from AcWing code page."""
    url = f"https://www.acwing.com/activity/content/code/content/{code_id}/"
    try:
        resp = session.get(url, timeout=30)
        resp.raise_for_status()
        # Extract code from <code> element
        match = re.search(r'<code[^>]*>(.*?)</code>', resp.text, re.DOTALL)
        if match:
            # Decode HTML entities and strip tags
            code_html = match.group(1)
            # Replace <br> or <br/> with newlines
            code_html = re.sub(r'<br\s*/?>', '\n', code_html)
            # Remove HTML tags
            code_text = re.sub(r'<[^>]+>', '', code_html)
            # Unescape HTML entities
            code_text = code_text.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&').replace('&quot;', '"').replace('&#39;', "'")
            return code_text.strip()
        return None
    except Exception as e:
        print(f"  Error fetching {code_id}: {e}")
        return None

def main():
    with open(MAPPING_FILE, 'r', encoding='utf-8') as f:
        problems = json.load(f)

    print(f"Total problems: {len(problems)}")

    success = 0
    failed = 0

    for i, p in enumerate(problems):
        lecture = p["lecture"]
        section = p["section"]
        problem = p["problem"]
        code_id = p["codeId"]

        # Create directory structure
        # Short lecture name for folder
        lecture_short = lecture.split()[0] + "_" + lecture.split(maxsplit=1)[1] if ' ' in lecture else lecture
        dir_path = os.path.join(BASE_DIR, sanitize_filename(lecture_short), section)
        os.makedirs(dir_path, exist_ok=True)

        # Filename from problem name
        filename = sanitize_filename(problem) + ".cpp"
        filepath = os.path.join(dir_path, filename)

        # Skip if already downloaded
        if os.path.exists(filepath):
            print(f"[{i+1}/{len(problems)}] SKIP {problem} (exists)")
            success += 1
            continue

        # Fetch code
        code = fetch_code(code_id)

        if code:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(code)
            print(f"[{i+1}/{len(problems)}] OK   {problem} -> {filepath}")
            success += 1
        else:
            print(f"[{i+1}/{len(problems)}] FAIL {problem} (no code found)")
            failed += 1

        # Rate limiting
        time.sleep(0.5)

    print(f"\nDone! Success: {success}, Failed: {failed}")

if __name__ == "__main__":
    main()
