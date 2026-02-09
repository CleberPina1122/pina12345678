from datetime import datetime, timezone
import xml.etree.ElementTree as ET

def parse_xmltv_datetime(dt: str) -> datetime:
    dt = (dt or "").strip()
    base = dt[:14]
    if len(base) != 14:
        # fallback
        return datetime.now(timezone.utc)
    # treat as UTC for simplicity
    return datetime.strptime(base, "%Y%m%d%H%M%S").replace(tzinfo=timezone.utc)

def parse_xmltv(xml_text: str):
    root = ET.fromstring(xml_text)
    channels = []
    programs = []

    for ch in root.findall("channel"):
        xml_id = (ch.attrib.get("id","") or "").strip()
        dn = ch.findtext("display-name")
        channels.append({"xmltv_channel_id": xml_id, "display_name": dn})

    for p in root.findall("programme"):
        xml_id = (p.attrib.get("channel","") or "").strip()
        start = parse_xmltv_datetime(p.attrib.get("start",""))
        stop = parse_xmltv_datetime(p.attrib.get("stop",""))
        title = (p.findtext("title") or "").strip() or "Sem título"
        desc = (p.findtext("desc") or "").strip() or None
        cat = (p.findtext("category") or "").strip() or None
        programs.append({
            "xmltv_channel_id": xml_id,
            "start_utc": start,
            "end_utc": stop,
            "title": title,
            "desc": desc,
            "category": cat
        })
    return channels, programs
