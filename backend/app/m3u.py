import re
from typing import List, Dict

EXTINF_RE = re.compile(r'#EXTINF:.*?,(.*)$')
LOGO_RE = re.compile(r'tvg-logo="([^"]*)"')
GROUP_RE = re.compile(r'group-title="([^"]*)"')
TVGID_RE = re.compile(r'tvg-id="([^"]*)"')
TVGNAME_RE = re.compile(r'tvg-name="([^"]*)"')

def parse_m3u(text: str) -> List[Dict]:
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    out = []
    cur = None
    for line in lines:
        if line.startswith("#EXTINF"):
            name = (EXTINF_RE.search(line).group(1).strip() if EXTINF_RE.search(line) else "Sem nome")
            logo = (LOGO_RE.search(line).group(1) if LOGO_RE.search(line) else None)
            group = (GROUP_RE.search(line).group(1) if GROUP_RE.search(line) else "Sem grupo")
            tvg_id = (TVGID_RE.search(line).group(1) if TVGID_RE.search(line) else None)
            tvg_name = (TVGNAME_RE.search(line).group(1) if TVGNAME_RE.search(line) else None)
            cur = {"name": name, "logo": logo, "group": group, "url": None, "tvg_id": tvg_id, "tvg_name": tvg_name}
        elif line.startswith("#"):
            continue
        else:
            if cur:
                cur["url"] = line
                out.append(cur)
                cur = None
    return out
