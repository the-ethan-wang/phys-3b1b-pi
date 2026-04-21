import math

try:
    m1 = int(input())
    assert 0<m1<10**20
except:
    m1 = 100

sparse_printing=False
extra_sparse_printing=False
if m1>=1000:
    sparse_printing=True
if m1>=10000:
    extra_sparse_printing=True

m2 = 1
t = 0.0
v1 = 1.0
v2 = 0.0
x1 = -1.0
x2 = -1.0
next_box = True
c_count = 1

predicted_c_count = math.pi * m1 // 1

def boxbox(m1,m2,u1,u2):
    rel_v=u1-u2
    init_m=m1**2*u1+m2**2*u2
    v1=(init_m-m2*rel_v)/(m1**2+m2**2)
    v2=v1+rel_v
    return(v1, v2)

def boxwall(u2):
    v2=-u2
    return v2

def display(t,v1,v2,x1,x2,next_box,c_count):
    print(f"{t:>5.2f} {v1:>7.2f} {v2:>7.2f} {x1:>5.2f} {x2:>5.2f} {'boxbox ' if next_box else 'boxwall'} {c_count}")

def move_boxbox(t, v1, v2, x1, x2):
    rel_v=v1-v2
    disp=x2-x1
    delta_t=disp/rel_v
    t+=delta_t
    x1+=delta_t*v1
    x2+=delta_t*v2
    return(t,v1,v2,x1,x2)

def move_boxwall(t, v1, v2, x1, x2):
    delta_t=-x2/v2
    t+=delta_t
    x1+=delta_t*v1
    x2+=delta_t*v2
    return(t,v1,v2,x1,x2)

print("  t     v1    v2    x1    x2   coll   c")
while not (v1<=v2<=0):
    if next_box:
        t,v1,v2,x1,x2=move_boxbox(t,v1,v2,x1,x2)
        if not sparse_printing:
            display(t,v1,v2,x1,x2,next_box,c_count)
        v1,v2=boxbox(m1,m2,v1,v2)
        if not extra_sparse_printing:
            display(t,v1,v2,x1,x2,next_box,c_count)
        else:
            if abs(c_count-predicted_c_count) <= 20:
                display(t,v1,v2,x1,x2,next_box,c_count)
    else:
        t,v1,v2,x1,x2=move_boxwall(t,v1,v2,x1,x2)
        if not sparse_printing:
            display(t,v1,v2,x1,x2,next_box,c_count)
        v2=boxwall(v2)
        if not extra_sparse_printing:
            display(t,v1,v2,x1,x2,next_box,c_count)
        else:
            if (c_count-predicted_c_count)%predicted_c_count <= 20:
                display(t,v1,v2,x1,x2,next_box,c_count)

    next_box = not next_box
    c_count+=1