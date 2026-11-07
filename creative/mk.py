from PIL import Image, ImageDraw, ImageFont
W,H=1920,1080
F="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"; FB="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
def base(title):
    im=Image.new("RGB",(W,H),(14,18,28)); d=ImageDraw.Draw(im)
    d.text((100,80),title,font=ImageFont.truetype(FB,64),fill=(255,120,90)); return im,d
def lines(d,ls,y=230,s=44):
    f=ImageFont.truetype(F,s)
    for l in ls: d.text((100,y),l,font=f,fill=(235,235,240)); y+=s+28
S=[]
im,d=base("");d.text((W//2,H//2),"Is your run club\nthe new Love Island?",font=ImageFont.truetype(FB,110),fill="white",anchor="mm",align="center");S.append(im)
im,d=base("The finding");lines(d,["Nearly 1 in 5 Gen Z survey respondents","had dated someone they met through exercise.","","Source: Strava Year in Sport 2024 trend report.","Global survey. Exercise overall, not run clubs only."]);S.append(im)
im,d=base("Method");lines(d,["13 Sydney run clubs mapped from public sources","(official sites, club pages, directories, checked 7 Nov 2026).","","Clubs meeting outside City of Sydney","(Bondi, Bronte, Centennial Park, Kirribilli) are flagged.","Approximate locations are not shown as precise pins."]);S.append(im)
for p in ["/workspace/hackathon-data/task1/data-flow.png","/workspace/hackathon-video/task1/video-flow.png"]:
    im,d=base("Data flow");g=Image.open(p).convert("RGB");g.thumbnail((1720,640));im.paste(g,((W-g.width)//2,190));S.append(im)
im,d=base("Limits");lines(d,["No local Microburbs demographic finding:","API access was blocked from our build machine.","","No love-odds score. Love Island is the joke, not a statistic.","\"Never married\" does not mean single."]);S.append(im)
im,d=base("Sources");lines(d,["Strava press: press.strava.com/articles/","  strava-releases-annual-year-in-sport-trend","Run clubs: run-clubs.csv + run-clubs-sources.md (repo)","Microburbs API docs: microburbs.com.au/developers/api-docs","Brief: microburbs.com.au/p/hackathon-task-social-post"],s=38);S.append(im)
for i,im in enumerate(S): im.save(f"s{i}.png")
