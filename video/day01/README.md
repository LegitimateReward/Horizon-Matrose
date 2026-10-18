# Random Sailor — Random Day 01 (YouTube Short)

60 s, 1080×1920, 30 fps, H.264 + AAC, about −15 LUFS. Built from 15 Ray-Ban Meta POV clips
(batch_2_134–148, recorded 2026-10-12, 17:37–18:18 UTC). The footage is a night walk along a river
promenade. No vessel work appears in it, and the clips carry no GPS data.

## Pipeline (run in order, from a working dir; `segs.py` points at the source clips)
1. `render_segs.py` — trims each segment, stabilizes it (vidstab, two passes), denoises it (hqdn3d), crops 3:4 to 9:16 with a per-shot offset,
   upscales it (lanczos), grades it, and cleans the audio (high-pass for wind, FFT denoise, presence EQ, dynamic normalization). Then it concatenates the segments.
2. `hud.py` — draws the original HUD cards as PNGs (Inter font, teal accent).
3. `sfx.sh` — synthesizes the original UI cues and the ambient pad. No third-party audio is used.
4. `compose.py` — overlays the HUD with fades and slides, mixes the audio and sets the loudness.

## Timeline
| Time | Shot | Overlay / sound |
|---|---|---|
| 0:00–0:02 | Clock tower and lit terraces (hook) | — |
| 0:02–0:07 | Blue-hour skyline | RANDOM DAY 01 title, sub swell |
| 0:07–0:11 | Glowing glass hall | — |
| 0:11–0:15.5 | Group heads out under the canopy | NEW OBJECTIVE · Walk the river promenade, two-tone blip |
| 0:15.5–0:20.5 | River, purple-lit tower | LOCATION · River Promenade · Night walk · 12 Oct 2026, low whoosh |
| 0:20.5–0:27 | Walking the promenade with the group | — |
| 0:27–0:39 | Cobbles, terrace walkway, terraces and clock tower | — |
| 0:39–0:50.5 | Steps, railing, water reflections | — |
| 0:50.5–0:56 | Final stretch | TASK COMPLETE (strike-through), three-note chime |
| 0:56–1:00 | Walk into the distance | End card: RANDOM SAILOR · Real Days · River Ways · Day 01 · Logged, fade out |
