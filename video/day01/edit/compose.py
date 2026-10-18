import subprocess
H=[("h_title.png",2.3,6.6,0),("h_objective.png",11.6,15.2,-36),("h_location.png",16.0,20.0,-36),
   ("h_complete.png",51.8,55.4,-36),("h_end.png",56.4,60.0,0)]
S=[("sfx_title.wav",2.0,1.0),("sfx_obj.wav",11.6,0.9),("sfx_loc.wav",15.8,0.8),("sfx_done.wav",51.8,0.9)]
args=["ffmpeg","-v","error","-y","-i","base.mov"]
fc=[]; v="[0:v]"
for i,(p,a,b,dx) in enumerate(H):
    d=b-a; args+=["-loop","1","-t",str(d),"-i",p]; n=i+1
    fc.append(f"[{n}:v]format=rgba,fade=in:st=0:d=0.35:alpha=1,fade=out:st={d-0.45}:d=0.45:alpha=1,setpts=PTS-STARTPTS+{a}/TB[o{i}]")
    x=f"'if(lt(t-{a},0.4),{dx}*(1-(t-{a})/0.4),0)'" if dx else "0"
    fc.append(f"{v}[o{i}]overlay=x={x}:y=0:enable='between(t,{a},{b})':eof_action=pass[v{i}]"); v=f"[v{i}]"
fc.append(f"{v}fade=t=in:d=0.25,fade=t=out:st=59.0:d=1.0,format=yuv420p[vout]")
base=len(H)+1
args+=["-i","pad.wav"]; fc.append(f"[{base}:a]volume=0.28[pad]")
mix=["[0:a]","[pad]"]
for j,(p,t,g) in enumerate(S):
    args+=["-i",p]; k=base+1+j
    fc.append(f"[{k}:a]volume={g},adelay={int(t*1000)}:all=1[s{j}]"); mix.append(f"[s{j}]")
fc.append("".join(mix)+f"amix=inputs={len(mix)}:normalize=0:duration=first,afade=t=out:st=58.8:d=1.2,"
          "acompressor=threshold=0.05:ratio=3:attack=8:release=200,volume=18.5dB,alimiter=limit=0.84:level=false,aresample=48000[aout]")
args+=["-filter_complex",";".join(fc),"-map","[vout]","-map","[aout]","-t","60",
       "-c:v","libx264","-preset","slow","-crf","18","-profile:v","high","-pix_fmt","yuv420p","-r","30",
       "-c:a","aac","-b:a","192k","-movflags","+faststart","RandomSailor_Day01_Short.mp4"]
subprocess.run(args,check=True)
