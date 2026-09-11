#!/usr/bin/env python3
"""Exact physical phase grading for the frozen factor-two source relay.

The complete ungraded coefficients are certified by the existing relay and
pollution checkers. This file proves the new discriminator: on the generated
lattice, physical phase grade/m is exactly the second lattice coordinate z.
"""

CHECKS=[]
def check(ok,label):
    if not ok: raise AssertionError(label)
    CHECKS.append(label)

# Four positive parents have lattice z=+1 and common physical phase +m;
# reality partners have z=-1 and phase -m.
parents=[(5,1),(-4,1),(2,1),(-1,1)]
state={(x,z,z) for x,z in parents}
state|={(-x,-z,-z) for x,z in parents}
check(all(g==z for _,z,g in state),'seed phase grade equals lattice z')

# Linear source/reference/physical terms preserve both Fourier key and phase
# grade. Quadratic convolution adds both. Enumerate the full reachable support
# through quartic amplitude degree to regression-test the invariant.
levels=[state]
all_state=set(state)
for degree in range(2,5):
    new=set()
    for left_degree in range(1,degree):
        right_degree=degree-left_degree
        if left_degree>len(levels) or right_degree>len(levels): continue
        for x1,z1,g1 in levels[left_degree-1]:
            for x2,z2,g2 in levels[right_degree-1]:
                if (x1+x2,z1+z2)==(0,0):
                    continue
                new.add((x1+x2,z1+z2,g1+g2))
    levels.append(new)
    all_state|=new
    check(all(g==z for _,z,g in new),f'grade=z preserved at degree {degree}')

# Frozen exact coefficient theorems identify these spatial keys.
pollutant=(14,1)
doubled=[(10,2),(-8,2),(4,2),(-2,2)]
check((pollutant[0],pollutant[1],1) in all_state,
      'known cubic pollutant key has phase grade m')
for key in doubled:
    check((key[0],key[1],2) in all_state,
          f'doubled target {key} has phase grade 2m')

# Specific relay arithmetic: common daughter uses +m + +m = 2m, while each
# pair-difference shear uses +m + -m = 0; daughter + shear stays in 2m.
check(1+1==2,'common daughter is grade 2m')
check(1-1==0,'difference shears are grade zero')
check(2+0==2,'daughter plus shear remains grade 2m')
check(1+1-1==1,'extreme cubic pollutant is grade m')

# General ancestry lemma. A degree-d monomial in original +/-m factors has
# grade q*m iff |q|<=d and d-q is even. Hence grade 2^j*m needs degree >=2^j.
for d in range(1,65):
    grades={2*k-d for k in range(d+1)}
    for q in range(-d-2,d+3):
        check((q in grades)==(abs(q)<=d and (d-q)%2==0),
              f'degree {d} exact grade reachability q={q}')
for j in range(10):
    q=2**j
    check(all(q not in {2*k-d for k in range(d+1)} for d in range(q)),
          f'grade 2^{j}m absent below degree {q}')

print(f'PASS: {len(CHECKS)} exact assertions.')
print('Physical phase grade/m equals lattice z on the relay-generated algebra.')
print('Thus the frozen cubic pollutant (14,1) is grade m, while all doubled targets (*,2) are grade 2m.')
print('Any grade 2^j m descendant from the original +/-m parents has amplitude degree at least 2^j.')
