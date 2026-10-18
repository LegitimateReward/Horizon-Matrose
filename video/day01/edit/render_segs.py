import subprocess,sys,os
exec(open('segs.py').read())
print("total",sum(x[2] for x in SEGS))
def run(a): subprocess.run(a,check=True)
for i,(c,s,d,cx,g) in enumerate(SEGS):
    src=U+CLIP[c]; out=f"seg{i:02d}.mp4"; trf=f"seg{i:02d}.trf"
    trim=["-ss",str(s),"-t",str(d),"-i",src]
    run(["ffmpeg","-v","error","-y",*trim,"-vf",f"vidstabdetect=shakiness=6:accuracy=12:result={trf}","-f","null","-"])
    vf=(f"vidstabtransform=input={trf}:smoothing=18:zoom=4:optzoom=0:interpol=bicubic,"
        f"hqdn3d=4:3:6:4,crop=trunc(ih*9/32)*2:ih:(iw-ow)*{cx}:0,scale=1080:1920:flags=lanczos,fps=30,"
        f"eq=gamma={g}:saturation=1.3:contrast=1.08,colorbalance=rs=-0.04:bs=0.05:rh=0.05:bh=-0.03,"
        "curves=master='0/0 0.06/0.04 0.5/0.54 1/1',unsharp=5:5:0.45,vignette=PI/5,"
        "noise=alls=3:allf=t,format=yuv420p,setsar=1")
    af=(f"highpass=f=110,lowpass=f=12000,afftdn=nf=-30:nr=12,"
        f"equalizer=f=2500:t=q:w=1.2:g=3,dynaudnorm=f=300:g=21:m=15:p=0.7,"
        f"aresample=48000,aformat=channel_layouts=stereo,afade=t=in:d=0.04,afade=t=out:st={d-0.06}:d=0.06")
    run(["ffmpeg","-v","error","-y",*trim,"-vf",vf,"-af",af,"-c:v","libx264","-preset","medium","-crf","16",
         "-c:a","pcm_s16le","-t",str(d),out.replace(".mp4",".mov")])
    print("done",i,flush=True)
open("list.txt","w").write("".join(f"file 'seg{i:02d}.mov'\n" for i in range(len(SEGS))))
run(["ffmpeg","-v","error","-y","-f","concat","-safe","0","-i","list.txt","-c","copy","base.mov"])
