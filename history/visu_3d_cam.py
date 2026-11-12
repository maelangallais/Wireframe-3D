#Cree le 27 Janvier 2025
from math import cos,sin,tan,radians as ra,fabs as va,floor
from kandinsky import fill_rect as fr,set_pixel as sp
from kandinsky import draw_string as ds
from ion import keydown as kd
from time import sleep as sl

n,wh,gr,bl=(0,)*3,(255,)*3,(0,255,0),(0,0,255)

#Vertex and Edge Tables
vt=[[1,2,2],[-1,2,2],[1,2,0],[-1,2,0],[1,4,2],[-1,4,2],[1,4,0],[-1,4,0]]
et=[[1,0],[0,2],[2,3],[3,1],[6,7],[7,5],[5,4],[4,6],[0,4],[1,5],[2,6],[3,7]]

x,y,z=0,0,0 #Coordonnées
tp,efo=1.8,0.12  #Taille Personnage et Ecart Front-Oeil
ty=tp-efo #Hauteur yeux
w,l=320,222 #Dimensions écran
Y,P=0,0 #Yaw and Pitch
FOV=90  #Field Of View
f=w/(2*tan(ra(FOV/2)))  #distance focale

def ent(n):
 n=floor(n) if n-floor(n)<0.5 else floor(n)+1
 return int(n)
def dl(x1,y1,x2,y2):
 dx=min(max((x2-x1)/va(y2-y1) if va(y2-y1)!=0 else x2-x1,-1),1)
 dy=min(max((y2-y1)/va(x2-x1) if va(x2-x1)!=0 else y2-y1,-1),1)
 c=va(x2-x1) if va(x2-x1)>va(y2-y1) else va(y2-y1)
 for i in range(c):sp(ent(x1+dx*i),ent(y1+dy*i),gr)
C,S=lambda a:cos(ra(a)),lambda a:sin(ra(a))

def rotation(l,Y,P):
 rl,cy,sy,cp,sp=[],C(Y),S(Y),C(P),S(P)
 for px,py,pz in l:
  dx,dy,dz=px-x,py-y,pz-z
  nx=dx*cy-dy*sy*cp+dz*sy*sp
  ny=dx*sy+dy*cy*cp-dz*cy*sp
  nz=dy*sp+dz*cp
  rl.append((nx,ny,nz))
 return rl

def draw(vt=vt,et=et):
 vt=rotation(vt,Y,P)
 fr(0,0,320,222,wh)
 xp,yp=[],[] #X projected and Y projected
 for i in range(len(vt)):
  dx,dy,dz=vt[i][0]-x,vt[i][1]-y,vt[i][2]-z
  c=((dx*S(Y))**2+(dy*C(Y))**2+(dz*S(P))**2)**(1/2)
  if c==0:c+=0.001
  m=f/c  #multiplicateur
  xp.append(w//2+((dx*C(Y)+dy*S(Y))*f)/(c+f)*m)
  yp.append(w//2-((dz-ty)*f)/(c+f)*m)
  sp(ent(xp[i]),ent(yp[i]),n)
 for i in range(len(et)):
  dl(xp[et[i][0]],yp[et[i][0]],xp[et[i][1]],yp[et[i][1]])
 ds(str(Y),0,0)
 ds(str(P),0,18)
 ds(str(x),30,0)
 ds(str(y),30,18)
 ds(str(z),30,36)
# sl(0)

draw()
p,vp,ok=0.5,5,False
while True:
 if kd(12):ok=False if ok else True;sl(0.2)
 if not ok:
  #dx=S(Y+90) et dy=C(Y+90)
  #or: S(Y+90)=C(Y) et C(Y+90)=-S(Y)
  if kd(0):x,y=x-C(Y)*p,y+S(Y)*p;draw()
  elif kd(3):x,y=x+C(Y)*p,y-S(Y)*p;draw()
  #dx=S(Y)*C(P), dy=C(Y)*C(P) et dz=S(P)
  if kd(1):x,y,z=x+S(Y)*C(P)*p,y+C(Y)*C(P)*p,z*S(P);draw()
  elif kd(2):x,y,z=x-S(Y)*C(P)*p,y-C(Y)*C(P)*p,z*S(P);draw()
 else:
  if kd(0):Y-=vp;draw()
  elif kd(3):Y+=vp;draw()
  if kd(1):P=max(min(P-vp,90),-90);draw()
  elif kd(2):P=max(min(P+vp,90),-90);draw()
 if kd(17):z+=p;draw()
 elif kd(23):z-=p;draw()
