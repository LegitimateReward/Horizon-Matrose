U="/root/.claude/uploads/11b9ab98-15c5-5745-8ce8-f0215f934db2/"
CLIP={134:"4ec56baf-batch_2_134.mp4",136:"fa8c939e-batch_2_136.mp4",138:"75766f0b-batch_2_138.mp4",
139:"30c62bd3-batch_2_139.mp4",140:"ed347339-batch_2_140.mp4",142:"b5bf2a04-batch_2_142.mp4",
144:"a906cc5d-batch_2_144.mp4",146:"0fb33149-batch_2_146.mp4",148:"94eec6ea-batch_2_148.mp4"}
# (clip, start, dur, crop-x fraction, gamma)  -> total 60.0s
SEGS=[
 (142, 9.8, 2.0, 0.55, 1.25),  # cold-open hook: clock tower + lit terraces
 (134, 2.5, 5.0, 0.20, 1.35),  # blue-hour skyline -> title
 (136, 0.0, 4.0, 0.55, 1.20),  # glowing glass hall under canopy
 (136, 6.0, 4.5, 0.25, 1.25),  # friends heading out toward the river -> objective
 (138, 8.5, 5.0, 0.55, 1.45),  # river at night, purple-lit tower -> location
 (139, 0.0, 6.5, 0.50, 1.20),  # walking the promenade with the group
 (140, 1.0, 4.0, 0.45, 1.25),  # cobbles toward the red-lit waterfront
 (142, 0.5, 2.0, 0.60, 1.15),  # terrace walkway
 (142, 11.9, 6.0, 0.65, 1.15), # terraces and clock tower
 (144, 15.5, 4.0, 0.50, 1.35), # steps along the promenade
 (146, 0.0, 7.5, 0.35, 1.40),  # railing, water reflections
 (148, 4.0, 5.5, 0.65, 1.45),  # final stretch -> TASK COMPLETE
 (148, 9.5, 4.0, 0.50, 1.45),  # walk into the distance -> end card
]
