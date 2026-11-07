import os,requests,base64,json,re,sys
segs=json.load(open(sys.argv[1])); out=sys.argv[2]
text=" ".join(segs)
r=requests.post("https://api.elevenlabs.io/v1/text-to-speech/IKne3meq5aSn9XLyUdCD/with-timestamps",
 headers={"xi-api-key":os.environ["ELEVENLABS_API_KEY"]},
 json={"text":text,"model_id":"eleven_multilingual_v2","voice_settings":{"stability":0.6,"similarity_boost":0.75}})
(r.ok or sys.exit(r.text[:400])); j=r.json()
open(out+".mp3","wb").write(base64.b64decode(j["audio_base64"]))
a=j["alignment"]; ch,st,en=a["characters"],a["character_start_times_seconds"],a["character_end_times_seconds"]
words=[];cur=None
for c,s,e in zip(ch,st,en):
    if c.isspace():
        if cur: words.append(cur);cur=None
    else:
        if not cur: cur={"word":"","start":s,"end":e}
        cur["word"]+=c;cur["end"]=e
if cur: words.append(cur)
# segment boundaries
bounds=[];i=0
for sg in segs:
    n=len(sg.split()); bounds.append({"text":sg,"start":words[i]["start"],"end":words[i+n-1]["end"]}); i+=n
json.dump({"voice":"Charlie (premade, Australian) IKne3meq5aSn9XLyUdCD","model":"eleven_multilingual_v2","words":words,"segments":bounds},open(out+".json","w"),indent=1)
print(out,words[-1]["end"])
