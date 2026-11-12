#Cree le 12 Mars 2024
from math import cos,sin,degrees as dg,fabs as va,floor
from kandinsky import fill_rect as fr,set_pixel as sp
from ion import keydown as kd
from time import sleep as sl

n,gr,bl=(0,)*3,(0,255,0),(0,0,255)

vt=[[1,2,2],[-1,2,2],[1,2,0],[-1,2,0],[1,4,2],[-1,4,2],[1,4,0],[-1,4,0]]
et=[[1,0],[0,2],[2,3],[3,1],[6,7],[7,5],[5,4],[4,6],[0,4],[1,5],[2,6],[3,7]]
x,y,z,av,w,l=0,0,1.8-0.12,90,320,222
fr(0,l//2,w,1,bl),fr(w//2,0,1,l,bl)

def ent(n):
  n=floor(n) if n-floor(n)<0.5 else floor(n)+1
  return int(n)
def dl(x1,y1,x2,y2):
  dx=min(max((x2-x1)/va(y2-y1) if va(y2-y1)!=0 else x2-x1,-1),1)
  dy=min(max((y2-y1)/va(x2-x1) if va(x2-x1)!=0 else y2-y1,-1),1)
  c=va(x2-x1) if va(x2-x1)>va(y2-y1) else va(y2-y1)
  for i in range(c):sp(ent(x1+dx*i),ent(y1+dy*i),gr)

xp,yp=[],[]
for i in range(len(vt)):
  m=va(1/(y-vt[i][1])*800) if y-vt[i][1]!=0 else 2100
  xp.append(w//2+(vt[i][0]-x)/(vt[i][1]+4)*m)
  yp.append(l//2-(vt[i][2]-z)/(vt[i][1]+4)*m)
  sp(ent(xp[i]),ent(yp[i]),n)
for i in range(len(et)):
  dl(xp[et[i][0]],yp[et[i][0]],xp[et[i][1]],yp[et[i][1]])
