set -e
A="-v error -y"
# title: soft sub swell + airy whoosh
ffmpeg $A -f lavfi -i "aevalsrc='0.5*sin(2*PI*55*t)*(1-exp(-6*t))*exp(-1.6*t)|0.5*sin(2*PI*55*t)*(1-exp(-6*t))*exp(-1.6*t)':s=48000:d=2.5" \
  -f lavfi -i "anoisesrc=c=pink:d=2.5:a=0.25:r=48000" -filter_complex "[1]lowpass=f=1800,highpass=f=300,afade=t=in:d=1.0,afade=t=out:st=1.0:d=1.4,aformat=channel_layouts=stereo[n];[0][n]amix=inputs=2:normalize=0" sfx_title.wav
# objective: two-tone blip
ffmpeg $A -f lavfi -i "aevalsrc='0.22*(sin(2*PI*880*t)*exp(-16*t)+gte(t,0.1)*sin(2*PI*1318.5*(t-0.1))*exp(-11*(t-0.1)))':s=48000:d=1.2" -af "aecho=0.8:0.6:90|160:0.25|0.15,aformat=channel_layouts=stereo" sfx_obj.wav
# location: low filtered whoosh + soft tone
ffmpeg $A -f lavfi -i "anoisesrc=c=brown:d=1.8:a=0.5:r=48000" -f lavfi -i "aevalsrc='0.12*sin(2*PI*329.6*t)*exp(-3*t)':s=48000:d=1.8" -filter_complex "[0]lowpass=f=900,afade=t=in:d=0.6,afade=t=out:st=0.6:d=1.2[a];[a][1]amix=inputs=2:normalize=0,aformat=channel_layouts=stereo" sfx_loc.wav
# task complete: rising three-note chime
ffmpeg $A -f lavfi -i "aevalsrc='0.18*(sin(2*PI*1046.5*t)*exp(-7*t)+gte(t,0.09)*sin(2*PI*1318.5*(t-0.09))*exp(-7*(t-0.09))+gte(t,0.18)*(sin(2*PI*1568*(t-0.18))+0.3*sin(2*PI*523.25*(t-0.18)))*exp(-4*(t-0.18)))':s=48000:d=2.0" -af "aecho=0.8:0.7:110|190:0.3|0.18,aformat=channel_layouts=stereo" sfx_done.wav
# ambient pad (original), very low
ffmpeg $A -f lavfi -i "aevalsrc='0.06*(sin(2*PI*110*t)+0.7*sin(2*PI*164.81*t)+0.5*sin(2*PI*220.6*t)*(0.6+0.4*sin(2*PI*0.1*t))+0.35*sin(2*PI*261.63*t)*(0.5+0.5*sin(2*PI*0.07*t)))|0.06*(sin(2*PI*110.3*t)+0.7*sin(2*PI*164.6*t)+0.5*sin(2*PI*219.8*t)*(0.6+0.4*sin(2*PI*0.09*t))+0.35*sin(2*PI*261.9*t)*(0.5+0.5*sin(2*PI*0.08*t)))':s=48000:d=60" \
  -af "lowpass=f=1100,aecho=0.8:0.85:400|700:0.35|0.25,afade=t=in:d=4,afade=t=out:st=55:d=5" pad.wav
