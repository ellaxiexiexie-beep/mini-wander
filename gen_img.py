from PIL import Image, ImageDraw, ImageFont
import os

W,H=800,550
bg=(50,68,52);gold=(255,166,30);grey=(175,190,173)

fp=None
for p in ['/System/Library/Fonts/PingFang.ttc','/Library/Fonts/Arial.ttf']:
    if os.path.exists(p):
        fp=p;break
f14=ImageFont.truetype(fp,14) if fp else ImageFont.load_default()
f12=ImageFont.truetype(fp,12) if fp else ImageFont.load_default()

# === Classification Framework ===
img=Image.new('RGB',(W,H),bg)
d=ImageDraw.Draw(img)
d.text((40,30),'三维企业分类框架',fill=gold,font=f14)
d.line([(40,70),(760,70)],fill=gold,width=1)

industries=['数字经济','智能制造','新材料','生物医药']
for i,ind in enumerate(industries):
    y=115+i*35
    d.rectangle([40,y,230,y+28],outline=gold,width=1)
    d.text((50,y+5),ind,fill=grey,font=f12)

stages=[('初创','种子轮'),('成长','A/B轮'),('成熟','规上'),('拟上市','Pre-IPO')]
for j,(sn,ss) in enumerate(stages):
    x=270+j*80
    d.rectangle([x,115,x+73,165],fill=(61+j*12,80+j*14,64+j*12),outline=grey,width=1)
    d.text((x+6,123),sn,fill=gold if j==3 else grey,font=f12)

comp=['未规范','培育中','已规范','标杆']
for k,cn in enumerate(comp):
    cx=520+k*48
    d.rectangle([cx,115,cx+42,150],fill=(61+k*12,80+k*14,64+k*12),outline=gold if k==3 else grey,width=1)
    d.text((cx+4,125),cn,fill=gold if k==3 else grey,font=f12)

# Matrix
mx0,my0=75,275
for j,sn in enumerate(['初创','成长','成熟','拟上市']):
    x=mx0+100+j*85
    d.rectangle([x,my0,x+80,my0+22],outline=grey,width=1)
    d.text((x+10,my0+2),sn,fill=grey,font=f12)

for i,ind in enumerate(industries):
    y=my0+22+i*26
    d.rectangle([mx0,y,mx0+95,y+22],outline=grey,width=1)
    d.text((mx0+5,y+2),ind,fill=grey,font=f12)
    for j in range(4):
        x=mx0+100+j*85;ci=(i+j)%4
        d.rectangle([x,y,x+80,y+22],fill=(61+ci*12,80+ci*14,64+ci*12),outline=grey,width=1)

d.text((40,510),'应用场景：企业分层分类 | 精准招商方向识别',fill=grey,font=f12)
img.save('/Users/xyh/Documents/作品集/mini-wander/classification-framework.png')
print('classification-framework.png OK')

# === Industry Chain Map ===
img2=Image.new('RGB',(W,H),bg)
d2=ImageDraw.Draw(img2)
d2.text((40,30),'产业链图谱',fill=gold,font=f14)
d2.line([(40,70),(760,70)],fill=gold,width=1)

d2.text((40,90),'上游',fill=grey,font=f12)
for k,(nm,sub) in enumerate([('钢铁/有色金属','原材料'),('铸造毛坯','铸造工艺')]):
    x=100+k*170
    d2.rectangle([x,115,x+150,163],outline=gold,width=2)
    d2.text((x+8,120),nm,fill=grey,font=f12)
    if k<1:
        d2.line([x+150,139,x+162,139],fill=gold,width=2)

d2.text((40,185),'中游',fill=grey,font=f12)
for k,(nm,sub) in enumerate([('精密加工','CNC/热处理'),('轴承制造','核心零部件'),('汽配零部件','发动机/底盘')]):
    x=100+k*155
    d2.rectangle([x,210,x+140,258],outline=gold,width=2)
    d2.text((x+8,215),nm,fill=grey,font=f12)
    if k<2:
        d2.line([x+140,234,x+148,234],fill=gold,width=2)

d2.text((40,280),'下游',fill=grey,font=f12)
for k,(nm,sub) in enumerate([('高端装备','新能源/智能'),('整车装配','新能源汽车'),('终端市场','国内/海外')]):
    x=100+k*155
    if nm=='终端市场':
        d2.rectangle([x,305,x+140,353],fill=gold)
        d2.text((x+8,310),nm,fill=bg,font=f12)
    else:
        d2.rectangle([x,305,x+140,353],outline=gold,width=2)
        d2.text((x+8,310),nm,fill=grey,font=f12)
    if k<2:
        d2.line([x+140,329,x+148,329],fill=gold,width=2)

d2.line([185,163,185,200],fill=gold,width=1)
d2.line([185,258,185,295],fill=gold,width=1)

d2.line([610,70,610,450],fill=grey,width=1)
d2.text((625,75),'配套支撑',fill=gold,font=f14)
for k,(enm,esub) in enumerate([('设备供应商','数控机床/产线'),('检测认证','质量认证'),('物流仓储','供应链管理'),('金融服务','供应链融资')]):
    ey=110+k*60
    d2.rectangle([625,ey,760,ey+40],outline=grey,width=1)
    d2.text((635,ey+5),enm,fill=grey,font=f12)

d2.text((40,510),'方法：基于产业链调研，识别补链方向',fill=grey,font=f12)
img2.save('/Users/xyh/Documents/作品集/mini-wander/industry-chain-map.png')
print('industry-chain-map.png OK')
