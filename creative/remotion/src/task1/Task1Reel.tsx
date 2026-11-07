import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate} from 'remotion';
export type Task1Props={example?:boolean;hook:string;clubs:{name:string;suburb:string;x:number;y:number;outside:boolean;source:string}[]};
const pink='#ff638d', cream='#fff5df';
const label:React.CSSProperties={fontSize:28,letterSpacing:4,textTransform:'uppercase',fontWeight:700};
export const Task1Reel:React.FC<Task1Props>=({hook,clubs})=>{
 const f=useCurrentFrame(); const {fps}=useVideoConfig();const t=f/fps;
 const clubIndex=Math.min(clubs.length-1,Math.max(0,Math.floor((t-8)/0.86)));
 const current=clubs[clubIndex];
 const showText=f>0;
 const Map=()=> <svg width="1080" height="1400" viewBox="0 0 1080 1400" style={{position:'absolute',top:220,left:0}}>
 <defs><pattern id="grid" width="60" height="60" patternUnits="userSpaceOnUse"><path d="M 60 0 L 0 0 0 60" fill="none" stroke="#ffffff" strokeOpacity=".045"/></pattern></defs>
 <rect width="1080" height="1400" fill="#162f38"/><path d="M0 0H760L750 140 640 220 700 270 620 310 640 390 740 400 800 360 870 450 890 650 920 800 930 1100 1000 1400H0Z" fill="#253d37"/>
 <path d="M0 280L170 350 250 290 360 330 430 270 460 340 550 310 600 370 660 340 700 410 620 440 530 395 460 430 350 390 250 440 130 400 0 460Z" fill="#162f38"/>
 <path d="M400 290L430 440" stroke="#d0cab6" strokeWidth="7" opacity=".5"/>
 <path d="M300 470L450 680 520 920 670 1200 M160 650L560 580 850 760 M140 900L700 1050" stroke="#a8b5a0" opacity=".13" strokeWidth="12" fill="none"/>
 <rect width="1080" height="1400" fill="url(#grid)"/>
 {showText&&<><text x="670" y="1280" fill="#9dbac0" fontSize="25">PACIFIC OCEAN</text></>}
 {t>=8&&clubs.map((c,i)=>{const local=(t-8-i*.86)*fps; if(local<0)return null;const s=interpolate(local,[0,10],[0,1],{extrapolateRight:'clamp'});return <g key={c.name} opacity={s} transform={`translate(${c.x},${c.y-40*(1-s)})`}><circle r={i===clubIndex?40:30} fill={c.outside?'#87969c':pink} fillOpacity=".24" stroke={c.outside?'#a1aaaf':pink} strokeWidth="3" strokeDasharray="6 5"/><circle r="8" fill={c.outside?'#b6bfc4':pink}/><text x="0" y="-43" textAnchor="middle" fill={cream} fontSize="24" fontWeight="700">{i+1}</text></g>})}
 </svg>;
 return <AbsoluteFill style={{background:'#10242c',color:cream,fontFamily:'Arial, sans-serif'}}>
 <Map/>
 <AbsoluteFill style={{background:'linear-gradient(#10242c 0%, transparent 36%,transparent 64%,#10242c 90%)'}}/>
 {showText&&<>
 <div style={{position:'absolute',top:105,left:76,right:76,...label,color:pink}}>SYDNEY / RUN CLUBS × DATING</div>
 {t<3&&<><div style={{position:'absolute',top:240,left:75,right:75,fontSize:99,fontWeight:900,lineHeight:1.03,letterSpacing:-4,whiteSpace:'pre-line'}}>{hook}</div><div style={{position:'absolute',bottom:230,left:78,fontSize:30}}>The joke is Love Island. The question is real.</div></>}
 {t>=3&&t<8&&<><div style={{position:'absolute',inset:0,background:'#10242cef'}}/><div style={{position:'absolute',top:260,left:78,right:78}}><div style={{...label,color:pink}}>THE GLOBAL SIGNAL</div><div style={{fontSize:126,fontWeight:900,lineHeight:1.05,marginTop:42}}>Nearly<br/>1 in 5</div><div style={{fontSize:54,lineHeight:1.16,marginTop:35}}>Gen Z survey respondents had dated someone they met through exercise</div></div><div style={{position:'absolute',bottom:235,left:78,right:78,fontSize:30,lineHeight:1.4,color:'#b3c6c8'}}>Strava Year in Sport 2024<br/>Global survey · exercise overall<br/>Not run-club-specific. Not your odds.</div></>}
 {t>=8&&t<22&&<><div style={{position:'absolute',top:220,left:76,right:76,fontSize:70,fontWeight:900,lineHeight:1.05}}>13 clubs.<br/>No soulmate score.</div><div style={{position:'absolute',top:395,left:78,fontSize:26,color:'#b3c6c8'}}>Schematic Sydney map · suburb-level markers</div><div style={{position:'absolute',bottom:285,left:70,right:70,padding:'30px 35px',background:'#10242cf5',borderLeft:`7px solid ${current.outside?'#a1aaaf':pink}`}}><div style={{...label,color:current.outside?'#b6bfc4':pink}}>CLUB {clubIndex+1} / 13</div><div style={{fontSize:52,lineHeight:1.1,fontWeight:800,marginTop:16}}>{current.name}</div><div style={{fontSize:29,marginTop:16,color:'#b3c6c8'}}>{current.suburb}</div>{current.outside&&<div style={{fontSize:27,marginTop:14,color:'#d6dadd'}}>Outside City of Sydney</div>}</div><div style={{position:'absolute',bottom:170,left:76,right:76,fontSize:25,lineHeight:1.4}}>Pink: local area · Grey: outside City of Sydney<br/>All circles are approximate areas, not meeting pins.<br/>Source: 13 unique clubs in run-clubs.csv</div></>}
 {t>=22&&t<27&&<><div style={{position:'absolute',inset:0,background:'#10242ce8'}}/><div style={{position:'absolute',top:350,left:78,right:78,fontSize:82,lineHeight:1.12,fontWeight:900}}>Your soulmate odds?<br/><span style={{color:pink}}>Unknown.</span><br/><br/>Your 6am alarm?<br/><span style={{color:pink}}>Guaranteed.</span></div><div style={{position:'absolute',bottom:220,left:78,right:78,fontSize:28,color:'#b3c6c8'}}>A punchline, not a schedule. Check your club.</div></>}
 {t>=27&&<><div style={{position:'absolute',inset:0,background:'#10242c'}}/><div style={{position:'absolute',top:235,left:78,right:78}}><div style={{...label,color:pink}}>SOURCES / NO MADE-UP ODDS</div><h1 style={{fontSize:83,lineHeight:1.05}}>Meet people.<br/>Not a probability.</h1><div style={{fontSize:34,lineHeight:1.55,color:'#c6d3d0'}}>Strava Year in Sport 2024<br/>press.strava.com<br/><br/>13 unique clubs: official club pages<br/>and directories in run-clubs.csv<br/>Full links + caveats in README<br/><br/>Map: schematic, not navigation<br/>Microburbs: no local data used<br/>Love Island: joke only</div></div></>}
 </>}
 </AbsoluteFill>;
};
