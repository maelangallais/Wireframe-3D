#Cree le 12 Mars 2024
from math import cos,sin,radians as ra,fabs as va,floor
from kandinsky import fill_rect as fr,set_pixel as sp
from ion import keydown as kd
from time import sleep as sl

n,wh,gr,bl=(0,)*3,(255,)*3,(0,255,0),(0,0,255)

vcube=[[1,2,2],[-1,2,2],[1,2,0],[-1,2,0],[1,4,2],[-1,4,2],[1,4,0],[-1,4,0]]
ecube=[[1,0],[0,2],[2,3],[3,1],[6,7],[7,5],[5,4],[4,6],[0,4],[1,5],[2,6],[3,7]]
vlol=[[-3,1,3],[-3,1,0],[-2,1,0],[-1,1,3],[-1,1,0],[1,1,0],[1,1,3],[2,1,3],[2,1,0],[3,1,0]]
elol=[[0,1],[1,2],[3,4],[4,5],[5,6],[6,3],[7,8],[8,9]]
vt=vlol
et=elol
x,y,z,tp,w,l=0,-10,0,1.8,320,222

def ent(n):
 n=floor(n) if n-floor(n)<0.5 else floor(n)+1
 return int(n)
def dl(x1,y1,x2,y2):
 dx=min(max((x2-x1)/va(y2-y1) if va(y2-y1)!=0 else x2-x1,-1),1)
 dy=min(max((y2-y1)/va(x2-x1) if va(x2-x1)!=0 else y2-y1,-1),1)
 c=va(x2-x1) if va(x2-x1)>va(y2-y1) else va(y2-y1)
 for i in range(c):sp(ent(x1+dx*i),ent(y1+dy*i),gr)

mx,my,mz=sum(v[0]for v in vt)/len(vt),sum(v[1]for v in vt)/len(vt),sum(v[2]for v in vt)/len(vt)
cvt=[[v[0]-mx,v[1]-my,v[2]-mz]for v in vt]
def rotation(l,a,t):
 rl,c,s=[],cos(ra(t)),sin(ra(t))
 for x,y,z in l:
  if a==1:nx,ny,nz=x,y*c-z*s,y*s+z*c
  elif a==2:nx,ny,nz=x*c-z*s,y,x*s+z*c
  elif a==3:nx,ny,nz=x*c-y*s,x*s+y*c,z
  rl.append((nx,ny,nz))
 tvt=[[v[0]+mx,v[1]+my,v[2]+mz]for v in rl]
 return tvt

def draw(vt=vt,et=et):
 fr(0,0,320,222,wh)
 xp,yp=[],[]
 for i in range(len(vt)):
  m=va(1/(y-vt[i][1])*800) if y-vt[i][1]!=0 else 300
  xp.append(w//2+(vt[i][0]-x)/(vt[i][1]+4)*m)
  yp.append(l//2-(vt[i][2]-(z+tp-0.12))/(vt[i][1]+4)*m)
  sp(ent(xp[i]),ent(yp[i]),n)
 for i in range(len(et)):
  dl(xp[et[i][0]],yp[et[i][0]],xp[et[i][1]],yp[et[i][1]])

draw()
p,a,i,di=0.5,3,0,1
while True:
 nvt,i=rotation(cvt,a,i),i+di if i<360 else i-360
 if kd(0):x-=p
 elif kd(3):x+=p
 if kd(1) and y<0:y+=p
 elif kd(2):y-=p
 if kd(17):z+=p
 elif kd(23):z-=p
 a=1 if kd(12) else 2 if kd(13) else 3 if kd(14) else a
 if kd(18) and di>0:di-=1
 elif kd(19) and di<15:di+=1
 draw(nvt),sl(0)
