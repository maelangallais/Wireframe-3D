#Créé le 25 Juin 2025
from math import cos,sin,tan,radians as ra,fabs as va,floor
from kandinsky import fill_rect as fr,set_pixel as sp
from ion import keydown as kd
from time import sleep as sl
from random import randint as rd

n,wh,re,gr,bl=(0,)*3,(255,)*3,(255,0,0),(0,255,0),(0,0,255)
colors=[wh,n,re,gr,bl]

#Vertex and Edge Tables
vcube=[[1,2,2],[-1,2,2],[1,0,2],[-1,0,2],[1,2,4],[-1,2,4],[1,0,4],[-1,0,4]]
ecube=[[1,0],[0,2],[2,3],[3,1],[6,7],[7,5],[5,4],[4,6],[0,4],[1,5],[2,6],[3,7]]
ccube=[rd(1,len(colors)-1)]*len(ecube)

vlol=[[-3,3,1],[-3,0,1],[-2,0,1],[-1,3,1],[-1,0,1],[1,0,1],[1,3,1],[2,3,1],[2,0,1],[3,0,1]]
elol=[[0,1],[1,2],[3,4],[4,5],[5,6],[6,3],[7,8],[8,9]]
clol=[rd(1,len(colors)-1)]*len(ecube)

rn=["cube","lol"] #Right Now (to draw on screen)
rnt=[] #Right Now Table
for name in rn:
 vt=eval("v"+name)
 et=eval("e"+name)
 ct=eval("c"+name)
 rnt.append([vt,et,ct])

def ent(n):
 n=floor(n) if n-floor(n)<0.5 else floor(n)+1
 return int(n)
def dl(x1,y1,x2,y2,cl=gr):
 dx=min(max((x2-x1)/va(y2-y1) if va(y2-y1)!=0 else x2-x1,-1),1)
 dy=min(max((y2-y1)/va(x2-x1) if va(x2-x1)!=0 else y2-y1,-1),1)
 c=va(x2-x1) if va(x2-x1)>va(y2-y1) else va(y2-y1)
 for i in range(c):sp(ent(x1+dx*i),ent(y1+dy*i),cl)
C,S=lambda a:cos(ra(a)),lambda a:sin(ra(a))

x,y,z=0,0,0 #Coordonnées
tp,efo=1.8,0.12  #Taille Personnage et Ecart Front-Oeil
ty=tp-efo #Hauteur yeux
w,l=320,222 #Dimensions écran
Y,P,R=0,0,0 #Yaw and Pitch
FOV=60  #Field Of View
f=w/(2*tan(ra(FOV/2)))  #distance focale
epsilon=0.1

def GBV(): #GetBasisVectors
 ihat_yaw=(C(Y),0,S(Y))
 jhat_yaw=(0,1,0)
 khat_yaw=(-S(Y),0,C(Y))

 ihat_pitch=(1,0,0)
 jhat_pitch=(0,C(P),-S(P))
 khat_pitch=(0,S(P),C(P))

 ihat_roll=(C(R),S(R),0)
 jhat_roll=(-S(R),C(R),0)
 khat_roll=(0,0,1)

 ihat_pitchYaw=DP(ihat_yaw,jhat_yaw,khat_yaw,ihat_pitch)
 jhat_pitchYaw=DP(ihat_yaw,jhat_yaw,khat_yaw,jhat_pitch)
 khat_pitchYaw=DP(ihat_yaw,jhat_yaw,khat_yaw,khat_pitch)

 ihat=DP(ihat_pitchYaw,jhat_pitchYaw,khat_pitchYaw,ihat_roll)
 jhat=DP(ihat_pitchYaw,jhat_pitchYaw,khat_pitchYaw,jhat_roll)
 khat=DP(ihat_pitchYaw,jhat_pitchYaw,khat_pitchYaw,khat_roll)
 return(ihat,jhat,khat);
def GIBV(): #GetInverseBasisVectors
 (ihat,jhat,khat)=GBV();
 ihat_inverse=(ihat[0],jhat[0],khat[0])
 jhat_inverse=(ihat[1],jhat[1],khat[1])
 khat_inverse=(ihat[2],jhat[2],khat[2])
 return(ihat_inverse,jhat_inverse,khat_inverse)
def DP(ihat,jhat,khat,v): #Dot Product
 vx=v[0]*ihat[0]+v[1]*jhat[0]+v[2]*khat[0]
 vy=v[0]*ihat[1]+v[1]*jhat[1]+v[2]*khat[1]
 vz=v[0]*ihat[2]+v[1]*jhat[2]+v[2]*khat[2]
 return(vx,vy,vz)

def TCS(vx,vy,vz): #To Camera Space
 ihat,jhat,khat=GIBV()
 v=(vx-x,vy-(y+ty),vz-z)
 (cx,cy,cz)=DP(ihat,jhat,khat,v)
 return(cx,cy,cz)

def PWC(a,b): #Project With Clipping
 cx1,cy1,cz1=a
 cx2,cy2,cz2=b
 if cz1<=epsilon and cz2<=epsilon:return None
 if cz1<=epsilon<cz2:
  t=(epsilon-cz1)/(cz2-cz1)
  cx1=cx1+t*(cx2-cx1)
  cy1=cy1+t*(cy2-cy1)
  cz1=epsilon
 elif cz2 <= epsilon < cz1:
  t=(epsilon-cz2)/(cz1-cz2)
  cx2=cx2+t*(cx1-cx2)
  cy2=cy2+t*(cy1-cy2)
  cz2=epsilon
 xp1=int(w//2+(cx1*f)/cz1)
 yp1=int(l//2-(cy1*f)/cz1)
 xp2=int(w//2+(cx2*f)/cz2)
 yp2=int(l//2-(cy2*f)/cz2)
 return (xp1,yp1),(xp2,yp2)

def draw():
 fr(0,0,w,l,wh)
 for vt,et,ct in rnt:
  CP=[TCS(vx,vy,vz)for vx,vy,vz in vt]
  for i,(a,b)in enumerate(et):
   p1=CP[a]
   p2=CP[b]
   proj=PWC(p1,p2)
   if proj:
    (x1,y1),(x2,y2)=proj
    dl(x1,y1,x2,y2,colors[ct[i]])

def rotation(l,a,t):
 mx,my,mz=sum(v[0]for v in l)/len(l),sum(v[1]for v in l)/len(l),sum(v[2]for v in l)/len(l)
 cvt=[[v[0]-mx,v[1]-my,v[2]-mz]for v in l]
 rl,c,s=[],C(t),S(t)
 for x,y,z in cvt:
  if a==1:nx,ny,nz=x,y*c-z*s,y*s+z*c #Yaw
  elif a==2:nx,ny,nz=x*c-z*s,y,x*s+z*c #Pitch
  elif a==3:nx,ny,nz=x*c-y*s,x*s+y*c,z #Roll
  rl.append((nx,ny,nz))
 tvt=[[v[0]+mx,v[1]+my,v[2]+mz]for v in rl]
 return tvt
def rotate(vt,yaw=1,pitch=1,roll=1):
 if yaw!=0:vt=rotation(vt,1,yaw)
 if pitch!=0:vt=rotation(vt,2,pitch)
 if roll!=0:vt=rotation(vt,3,roll)
 return vt

draw()
p,vp,ok=0.5,5,False
it=1
while True:
 Right,Up,Forward=GBV()
 if kd(12):ok=False if ok else True;sl(0.2)
 if not ok:
  if kd(0):
   x-=Right[0]*p
   y-=Right[1]*p
   z-=Right[2]*p
   draw()
  if kd(1):
   x+=Forward[0]*p
   y+=Forward[1]*p
   z+=Forward[2]*p
   draw()
  if kd(2):
   x-=Forward[0]*p
   y-=Forward[1]*p
   z-=Forward[2]*p
   draw()
  if kd(3):
   x+=Right[0]*p
   y+=Right[1]*p
   z+=Right[2]*p
   draw()
 else:
  if kd(0):Y+=vp;draw()
  elif kd(3):Y-=vp;draw()
  if kd(1):P=max(min(P+vp,90),-90);draw()
  elif kd(2):P=max(min(P-vp,90),-90);draw()
 if kd(17):
   x+=Up[0]*p
   y+=Up[1]*p
   z+=Up[2]*p
   draw()
 elif kd(23):
   x-=Up[0]*p
   y-=Up[1]*p
   z-=Up[2]*p
   draw()
 rnt[0][0]=rotate(rnt[0][0],1,2,1)
 draw()
# sl(0.1)