import httpx

def detect_stream_type(url: str) -> str:
    u = (url or "").lower()
    if ".m3u8" in u:
        return "hls"
    if u.endswith(".ts") or "mpegts" in u:
        return "mpegts"
    if u.endswith(".mp4"):
        return "mp4"
    if u.endswith(".m3u"):
        return "m3u"
    return "unknown"

async def resolve_url(url: str) -> dict:
    async with httpx.AsyncClient(follow_redirects=True, timeout=25.0) as client:
        r = await client.get(url, headers={"User-Agent":"CarbiPlay/1.0"})
        final_url = str(r.url)
        ctype = r.headers.get("content-type","")
        detected = detect_stream_type(final_url)
        if detected == "unknown" and ("mpegurl" in ctype or "m3u8" in ctype):
            detected = "hls"
        return {"input_url": url, "resolved_url": final_url, "content_type": ctype, "detected": detected}
