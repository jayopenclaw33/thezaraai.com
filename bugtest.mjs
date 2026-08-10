import { spawn } from 'node:child_process';
import { rmSync } from 'node:fs';
import { setTimeout as sleep } from 'node:timers/promises';
import path from 'node:path';
const HERE=path.dirname(new URL(import.meta.url).pathname), PORT=9370;
const CHROME='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const profile=path.join(HERE,'.bug-profile'); try{rmSync(profile,{recursive:true,force:true});}catch{}
const chrome=spawn(CHROME,['--headless=new','--disable-gpu','--hide-scrollbars','--no-first-run',
 '--force-device-scale-factor=1',`--user-data-dir=${profile}`,`--remote-debugging-port=${PORT}`,'about:blank'],{stdio:'ignore'});
let ws_=null;
for(let i=0;i<60;i++){await sleep(250);try{const r=await fetch(`http://127.0.0.1:${PORT}/json/list`);
 const t=(await r.json()).find(x=>x.type==='page');if(t?.webSocketDebuggerUrl){ws_=t.webSocketDebuggerUrl;break;}}catch{}}
const ws=new WebSocket(ws_);await new Promise((s,j)=>{ws.onopen=s;ws.onerror=j;});
let id=0;const p=new Map();
ws.onmessage=e=>{const m=JSON.parse(e.data);if(m.id&&p.has(m.id)){const{resolve}=p.get(m.id);p.delete(m.id);resolve(m.result);}};
const send=(m,pr={})=>new Promise(r=>{const i=++id;p.set(i,{resolve:r});ws.send(JSON.stringify({id:i,method:m,params:pr}));});
const js=async e=>(await send('Runtime.evaluate',{expression:e,returnByValue:true,awaitPromise:true})).result.value;
await send('Page.enable');await send('Runtime.enable');
await send('Emulation.setDeviceMetricsOverride',{width:1440,height:900,deviceScaleFactor:1,mobile:false});
await send('Page.navigate',{url:'http://127.0.0.1:8899/'});
await sleep(3000);
console.log(JSON.stringify(await js(`(() => {
  const w = document.querySelector('.work');
  const d = w.querySelector('.work-detail');
  const before = { h: Math.round(d.getBoundingClientRect().height), maxH: getComputedStyle(d).maxHeight,
                   expanded: w.getAttribute('aria-expanded') };
  w.click();
  const mid = { expanded: w.getAttribute('aria-expanded'), maxH: getComputedStyle(d).maxHeight };
  return { tag: w.tagName, detailParent: d.parentElement.tagName + '.' + d.parentElement.className,
           detailStillInsideWork: w.contains(d),
           childrenOfWork: [...w.children].map(c=>c.tagName+'.'+(c.className||'')),
           before, mid,
           scrollHeightOfDetail: d.scrollHeight };
})()`),null,2));
await sleep(900);
console.log("AFTER 900ms:", JSON.stringify(await js(`(() => { const d=document.querySelector('.work .work-detail');
  return { renderedHeight: Math.round(d.getBoundingClientRect().height), maxH: getComputedStyle(d).maxHeight,
           visible: d.getBoundingClientRect().height > 10 }; })()`)));
ws.close();chrome.kill();try{rmSync(profile,{recursive:true,force:true});}catch{}
process.exit(0);
