import json,sys
j=json.load(open(sys.argv[1]));W,H,fs,mv=map(int,sys.argv[3:7])
K=int(sys.argv[7]) if len(sys.argv)>7 else 4
def t(x):x=max(0,x);return f"{int(x//3600)}:{int(x%3600//60):02d}:{x%60:05.2f}"
o=f"""[Script Info]
ScriptType: v4.00+
WrapStyle: 2
PlayResX: {W}
PlayResY: {H}
[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: C,DejaVu Sans,{fs},&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,1,0,0,0,100,100,0,0,3,14,0,2,40,40,{mv},1
[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
w=j["words"];segs=j["segments"]
# chunk by segment, <=4 words
chunks=[];i=0
for s in segs:
    n=len(s["text"].split());idx=list(range(i,i+n));i+=n
    for k in range(0,n,K):chunks.append(idx[k:k+K])
for c in chunks:
    for p,wi in enumerate(c):
        st=w[wi]["start"]; en=w[c[p+1]]["start"] if p+1<len(c) else w[wi]["end"]+0.25
        txt=" ".join(("{\\c&H5A78FF&}"+w[x]["word"].lower()+"{\\c&HFFFFFF&}") if x==wi else w[x]["word"].lower() for x in c)
        o+=f"Dialogue: 0,{t(st)},{t(en)},C,,0,0,0,,{txt}\n"
open(sys.argv[2],"w").write(o)
