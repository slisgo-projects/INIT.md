---
name: youtube-transcript
description: Fetch a YouTube video's English captions with yt-dlp and convert them to plain text. Use when the user asks for a transcript of a YouTube URL.
---

# YouTube transcript

## Prerequisites

- yt-dlp from pip, not apt: `pip install --user -U --break-system-packages yt-dlp`. The apt build (`/usr/lib/python3/dist-packages`) lags YouTube API changes and fails.
- Check `yt-dlp --version` is recent. Update with the pip command above; `yt-dlp -U` refuses on apt-shadowed installs.
- Updating needs no sudo. sudo cannot read a password from Claude Code's `!` prompt; use `SUDO_ASKPASS=/bin/ssh-askpass sudo -A ...` if sudo is unavoidable.

## Fetch

Write output to a fresh scratchpad directory `$D`.

```
yt-dlp --skip-download --write-auto-subs --write-subs --sub-langs "en.*" --sub-format vtt -o "$D/%(id)s.%(ext)s" "<URL>"
```

- Prefer `<id>.en-orig.vtt` (original-language auto-captions); fall back to `<id>.en.vtt`.
- Warnings about missing JS runtime or impersonation target are non-fatal for subtitles.

## Convert to plain text

```
python3 -I -c '
import re,sys
seen=set();out=[]
for l in open(sys.argv[1],encoding="utf-8"):
    l=l.strip()
    if not l or "-->" in l or l.startswith(("WEBVTT","Kind:","Language:")): continue
    l=re.sub(r"<[^>]+>","",l).strip()
    if l and l not in seen: seen.add(l); out.append(l)
open(sys.argv[2],"w").write(" ".join(out))
' "$D/<id>.en-orig.vtt" "$D/transcript.txt"
```

## Failure modes

- `HTTP Error 400: Precondition check failed` / `Only images are available` → yt-dlp too old; update via pip.
- `The following content is not available on this app` / `This video is unavailable` on some player clients → yt-dlp too old; switching `player_client` (android) lists only translated tracks and needs a PO token. Update rather than chase clients.
- Control before declaring a video caption-less: run `--list-subs` on a known captioned video (e.g. `dQw4w9WgXcQ`) to separate tool failure from video-specific failure.
- Auto-captions misspell proper names; flag them when quoting.
- Do not clean the scratchpad with bare-glob `rm`; use a fresh directory per fetch.
