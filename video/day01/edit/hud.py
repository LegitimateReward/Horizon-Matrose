from PIL import Image, ImageDraw, ImageFont, ImageFilter
W,H=1080,1920
F="/usr/share/fonts/opentype/inter/"
def font(n,s): return ImageFont.truetype(F+n,s)
TEAL=(95,211,198,255); WHITE=(245,245,240,255); DIM=(220,225,222,200)
def spaced(d,xy,text,f,fill,sp=0,anchor="la"):
    x,y=xy
    if anchor=="ma":
        w=sum(d.textlength(c,font=f)+sp for c in text)-sp; x-=w/2
    for c in text:
        d.text((x,y),c,font=f,fill=fill); x+=d.textlength(c,font=f)+sp
def canvas(): return Image.new("RGBA",(W,H),(0,0,0,0))
def band(img,y0,y1):
    b=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(b).rectangle([0,y0,W,y1],fill=(4,8,12,120))
    return Image.alpha_composite(b.filter(ImageFilter.GaussianBlur(60)),img)
def finish(img,name):
    a=img.split()[3]
    sh=Image.new("RGBA",(W,H),(0,0,0,0)); sh.putalpha(a.point(lambda v:int(v*0.75)))
    sh=sh.filter(ImageFilter.GaussianBlur(7))
    out=Image.alpha_composite(sh,img); out.save(name)
def diamond(d,cx,cy,r,fill=None,outline=TEAL,w=3):
    d.polygon([(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy)],fill=fill,outline=outline,width=w)

# title
im=canvas(); d=ImageDraw.Draw(im)
spaced(d,(W/2,640),"RANDOM SAILOR",font("Inter-SemiBold.otf",34),TEAL,sp=12,anchor="ma")
spaced(d,(W/2,700),"RANDOM DAY 01",font("InterDisplay-Bold.otf",112),WHITE,sp=4,anchor="ma")
d.line([(W/2-170,850),(W/2-20,850)],fill=DIM,width=2); diamond(d,W/2,850,8,fill=TEAL,w=1)
d.line([(W/2+20,850),(W/2+170,850)],fill=DIM,width=2)
spaced(d,(W/2,882),"REAL DAYS · RIVER WAYS",font("Inter-Medium.otf",32),DIM,sp=8,anchor="ma")
finish(im,"h_title.png"); Image.alpha_composite(band(canvas(),600,960),Image.open("h_title.png")).save("h_title.png")

# objective (top-left, inside Shorts safe area)
X,Y=72,250
im=canvas(); d=ImageDraw.Draw(im)
d.rectangle([X,Y,X+5,Y+112],fill=TEAL)
diamond(d,X+38,Y+22,11)
spaced(d,(X+62,Y+6),"NEW OBJECTIVE",font("Inter-SemiBold.otf",28),TEAL,sp=6)
d.text((X+28,Y+50),"Walk the river promenade",font=font("Inter-Medium.otf",46),fill=WHITE)
finish(im,"h_objective.png")

# task complete (same anchor as objective)
im=canvas(); d=ImageDraw.Draw(im)
d.rectangle([X,Y,X+5,Y+112],fill=TEAL)
d.ellipse([X+26,Y+8,X+52,Y+34],outline=TEAL,width=3)
d.line([(X+32,Y+21),(X+38,Y+28),(X+47,Y+14)],fill=TEAL,width=3)
spaced(d,(X+62,Y+6),"TASK COMPLETE",font("Inter-SemiBold.otf",28),TEAL,sp=6)
f=font("Inter-Medium.otf",46); t="Walk the river promenade"
d.text((X+28,Y+50),t,font=f,fill=DIM); tw=d.textlength(t,font=f)
d.line([(X+28,Y+80),(X+28+tw,Y+80)],fill=DIM,width=3)
finish(im,"h_complete.png")

# location reveal (lower-left, above Shorts caption area)
X2,Y2=72,1180
im=canvas(); d=ImageDraw.Draw(im)
spaced(d,(X2,Y2),"LOCATION",font("Inter-SemiBold.otf",28),TEAL,sp=8)
d.line([(X2,Y2+46),(X2+420,Y2+46)],fill=DIM,width=2)
d.text((X2,Y2+62),"River Promenade",font=font("InterDisplay-Bold.otf",72),fill=WHITE)
spaced(d,(X2,Y2+156),"NIGHT WALK · 12 OCT 2026",font("Inter-Medium.otf",28),DIM,sp=5)
finish(im,"h_location.png")

# end card
im=canvas(); d=ImageDraw.Draw(im)
spaced(d,(W/2,720),"RANDOM SAILOR",font("InterDisplay-Bold.otf",96),WHITE,sp=6,anchor="ma")
d.line([(W/2-170,860),(W/2-20,860)],fill=DIM,width=2); diamond(d,W/2,860,8,fill=TEAL,w=1)
d.line([(W/2+20,860),(W/2+170,860)],fill=DIM,width=2)
spaced(d,(W/2,892),"REAL DAYS · RIVER WAYS",font("Inter-Medium.otf",34),DIM,sp=8,anchor="ma")
spaced(d,(W/2,990),"DAY 01 · LOGGED",font("Inter-SemiBold.otf",28),TEAL,sp=8,anchor="ma")
finish(im,"h_end.png"); Image.alpha_composite(band(canvas(),680,1050),Image.open("h_end.png")).save("h_end.png")
