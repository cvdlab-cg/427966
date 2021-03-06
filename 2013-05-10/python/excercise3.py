
from pyplasm import *
import scipy
from scipy import *

#---------------------------------------------------------
def VERTEXTRUDE((V,coords)):
    """
        Utility function to generate the output model vertices in a 
        multiple extrusion of a LAR model.
        V is a list of d-vertices (each given as a list of d coordinates).
        coords is a list of absolute translation parameters to be applied to 
        V in order to generate the output vertices.
        
        Return a new list of (d+1)-vertices.
    """
    return CAT(AA(COMP([AA(AR),DISTR]))(DISTL([V,coords])))

def cumsum(iterable):
    # cumulative addition: list(cumsum(range(4))) => [0, 1, 3, 6]
    iterable = iter(iterable)
    s = iterable.next()
    yield s
    for c in iterable:
        s = s + c
        yield s

def larExtrude(model,pattern):
    V,FV = model
    d = len(FV[0])
    offset = len(V)
    m = len(pattern)
    outcells = []
    for cell in FV:
        # create the indices of vertices in the cell "tube"
        tube = [v + k*offset for k in range(m+1) for v in cell]
        # take groups of d+1 elements, via shifting by one
        rangelimit = len(tube)-d
        cellTube = [tube[k:k+d+1] for k in range(rangelimit)]
        outcells += [scipy.reshape(cellTube,newshape=(m,d,d+1)).tolist()]
    outcells = AA(CAT)(TRANS(outcells))
    outcells = [group for k,group in enumerate(outcells) if pattern[k]>0 ]
    coords = list(cumsum([0]+(AA(ABS)(pattern))))
    outVerts = VERTEXTRUDE((V,coords))
    newModel = outVerts, CAT(outcells)
    return newModel

def GRID(args):
    model = ([[]],[[0]])
    for k,steps in enumerate(args):
        model = larExtrude(model,steps*[1])
    V,cells = model
    verts = AA(list)(scipy.array(V) / AA(float)(args))
    return MKPOL([verts, AA(AA(lambda h:h+1))(cells), None])
def semicircle_a(x1,y1,z,tx,ty,tz1,tz2):
	semix = float(x1)/2
	semia = BEZIER(S1)([[tx+semix,ty,z+tz1],[tx+semix,ty+y1,z+tz2],[tx-semix,ty+y1,z+tz2],[tx-semix,ty,z+tz1]])
	return semia

def semicircle_b(x1,y1,z,tx,ty,tz1,tz2):
	semix = float(x1)/2
	semib = BEZIER(S1)([[tx+semix,ty,z+tz1],[tx+semix,-y1+ty,z+tz2],[tx-semix,-y1+ty,z+tz2],[tx-semix,ty,z+tz1]])
	return semib





#the skeleton of the car for mounting the wheels

domain1D = GRID([10]);
domain2D = GRID([10,10])
domain1 = domain2D
domaininv = MAP([S2,S1])(domain1)


ControlPoints = [[-12.8,0],[-6,0],[-6,0],[-6,3],[-2,3],[-2,0],[-2,0],[11,0],[11,0],[11,3],
				 [15,3],[15,0],[15,0],[18,1],[19,1.5],[19,2.5],[19,2.5],[18,2.5],[18,2.5],[18,3.5],
				 [18,3.5],[18.5,3.5],[18.5,3.5],[18.5,4]]
lateral_down = NUBSPLINE(3)([0,0,0,0, 1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,20,21,21,21,21])(ControlPoints)

ControlPoints2 = [[18.5,4],[17.5,4],[17.5,4],[11,6.5],[11,6.5],[10.8,6.8],[10.8,6.8],[7,7.5],[3,7.5],[3,7.5]
				,[-3,5],[-3,5],[-3.8,5],[-8,4.5],[-9.5,4],[-9.5,4],[-13,3.3],[-13,3.3],[-13,3],[-13,3],
				[-13,1.7],[-13,1.7],[-12.5,1.4],[-12.8,0.9],[-12.8,0.9],[-12.8,0.9],[-12.8,0],[-12.8,0],[-12.8,0],[-12.8,0]]

lateral_up = NUBSPLINE(3)([0,0,0,0,1,2,3,4,5,6,   7,8,9,10,11,12,13,14,15,16,    17,18,19,20,21,22,23,24,25,26,27,27,27,27])(ControlPoints2)
lateralSection = T([2,1])(-4)(T([1,2])(-4)(STRUCT([lateral_down,lateral_up])))



upsec1 = BEZIER(S1)([[0,0,0],[0.4,0,0.5],[4.8,0,0.5],[7,0,0.3]])
upsec2 = BEZIER(S1)([[0,0,0],[-0.5,0,-0.5],[-0.5,0,-8],[0,0,-8]])
upsec3 = BEZIER(S1)([[7,0,0.3],[8.5,0,0.3]])
upsec4 = BEZIER(S1)([[8.5,0,0.3],[10.5,0,0.4]])
upsec5 = BEZIER(S1)([[10.5,0,0.4],[16,0,1],[17,0,0.8]])
upsec6 = BEZIER(S1)([[17,0,0.8],[17,0,0.75],[19,0,0.75],[19,0,0.8]])
upsec7 = BEZIER(S1)([[19,0,0.8],[22,0,1.2]])
upsec8 = BEZIER(S1)([[22,0,1.2],[22.8,0,1.2],[22.8,0,-9.2],[22,0,-9.2],[22,0,-9.2]])
upmap1 = MAP(BEZIER(S2)([upsec1]))(domain2D)
upmap2 = MAP(BEZIER(S2)([upsec2]))(domain2D)
upmap3 = MAP(BEZIER(S2)([upsec3]))(domain2D)
upmap4 = MAP(BEZIER(S2)([upsec4]))(domain2D)
upmap5 = MAP(BEZIER(S2)([upsec5]))(domain2D)
upmap6 = MAP(BEZIER(S2)([upsec6]))(domain2D)
upmap7 = MAP(BEZIER(S2)([upsec7]))(domain2D)
upmap8 = MAP(BEZIER(S2)([upsec8]))(domain2D)

uplateral = STRUCT([upmap1,upmap3,upmap4,upmap5,upmap6,upmap7])
upSection = T([3,1])(4)(T([1,3])(-12)(STRUCT([uplateral,T([3,1])(-8)(R([2,3])(PI)(uplateral)),upmap2,upmap8])))

backsec1 = BEZIER(S1)([[0,0,-0.3],[0,-1,-0.3],[0,-2,-0.3],[0,-2,-0.3],[0,-2,6],[0,-2,6],[0,-1,6],[0,0,6]])
backsec2 = BEZIER(S1)([[0,0,6],[0,0,6]])
backsec3 = BEZIER(S1)([[0,0,6],[0,0.15,5.4]])
backsec4 = BEZIER(S1)([[0,0.15,5.4],[0,0.8,5.2]])
backsec5 = BEZIER(S1)([[0,0.8,5.2],[0,1.2,5],[0,1.2,5],[0,1.2,0.5],[0,1.2,0.5],[0,0.8,0.5],[0,0.15,0.3]])
backsec6 = BEZIER(S1)([[0,0.15,0.3],[0,0,-0.3]])


backmap1 = MAP(BEZIER(S2)([backsec1]))(domain2D)
backmap2 = MAP(BEZIER(S2)([backsec2]))(domain2D)
backmap3 = MAP(BEZIER(S2)([backsec3]))(domain2D)
backmap4 = MAP(BEZIER(S2)([backsec4]))(domain2D)
backmap5 = MAP(BEZIER(S2)([backsec5]))(domain2D)

backmap6 = MAP(BEZIER(S2)([backsec6]))(domain2D)
backSection = T([2,1])(0.5)(T([3,1])(-2.7)(STRUCT([backmap1,backmap2,backmap3,backmap4,backmap5,backmap6])))

skeleton = STRUCT([S([1,2,3])([1.38,1,1])(upSection),lateralSection,S([1,2,3])([1.7,1.7,1.7])(backSection)])


#wheels part

wheel1a = semicircle_a(1.8,1.2,0,0,0,0,0)
wheel1b = semicircle_b(1.8,1.2,0,0,0,0,0)

wheel2a = semicircle_a(1.5,1,0,0,0,0,0) 
wheel2b = semicircle_b(1.5,1,0,0,0,0,0)

wheel3a = semicircle_a(1.8,1.2,1,0,0,0,0)
wheel3b = semicircle_b(1.8,1.2,1,0,0,0,0)

wheel4a = semicircle_a(1.5,1,1,0,0,0,0) 
wheel4b = semicircle_b(1.5,1,1,0,0,0,0)

def rim_star(z,shadow,tz):
	domain1 = GRID([10,10])
	domaininv = MAP([S2,S1])(GRID([10,10]))

	d = domain1
	if shadow == 1:
		domain1 = domaininv
		domaininv = d
	
	rim1a = semicircle_a(0.5,0.35,z,0,0,0,0)
	rim1b = semicircle_b(0.5,0.35,z,0,0,0,0)
	rimDouble1a = semicircle_a(0.5,0.35,z-tz,0,0,0,0)
	rimDouble1b = semicircle_b(0.5,0.35,z-tz,0,0,0,0)

	rim2a = semicircle_a(0.3,0.2,z,0,0,0,0)
	rim2b = semicircle_b(0.3,0.2,z,0,0,0,0)
	rimDouble2a = semicircle_a(0.3,0.2,z-tz,0,0,0,0)
	rimDouble2b = semicircle_b(0.3,0.2,z-tz,0,0,0,0)	
	
	rim3a = semicircle_a(1.5,1,z,0,0,0,0) 
	rim3b = semicircle_b(1.5,1,z,0,0,0,0)
	rimDouble3a = semicircle_a(1.5,1,z-tz,0,0,0,0) 
	rimDouble3b = semicircle_b(1.5,1,z-tz,0,0,0,0)
	
	rim4a = semicircle_a(1.3,0.8,z,0,0,0,0) 
	rim4b = semicircle_b(1.3,0.8,z,0,0,0,0)
	rimDouble4a = semicircle_a(1.3,0.8,z-tz,0,0,0,0) 
	rimDouble4b = semicircle_b(1.3,0.8,z-tz,0,0,0,0)

	rim5a = BEZIER(S1)([[0.15,0.16,z],[0.05,0.6,z]])
	rim5b = BEZIER(S1)([[-0.15,0.16,z],[-0.05,0.6,z]])
	rimDouble5a = BEZIER(S1)([[0.15,0.16,z-tz],[0.05,0.6,z-tz]])
	rimDouble5b = BEZIER(S1)([[-0.15,0.16,z-tz],[-0.05,0.6,z-tz]])

	
	a9 = MAP(BEZIER(S2)([rim1a,rim2a]))(domaininv)
	a10 = MAP(BEZIER(S2)([rim1b,rim2b]))(domain1)
	a11 = MAP(BEZIER(S2)([rim3a,rim4a]))(domaininv)
	a12 = MAP(BEZIER(S2)([rim3b,rim4b]))(domain1)
	a13 = MAP(BEZIER(S2)([rim5a,rim5b]))(domaininv)
	
	a17 = MAP(BEZIER(S2)([rim1a,rimDouble1a]))(domaininv)
	a18 = MAP(BEZIER(S2)([rim2a,rimDouble2a]))(domain1)
	a19 = MAP(BEZIER(S2)([rim3a,rimDouble3a]))(domaininv)
	a20 = MAP(BEZIER(S2)([rim4a,rimDouble4a]))(domain1)
	a21 = MAP(BEZIER(S2)([rim5a,rimDouble5a]))(domaininv)

	a22 = MAP(BEZIER(S2)([rim1b,rimDouble1b]))(domaininv)
	a23 = MAP(BEZIER(S2)([rim2b,rimDouble2b]))(domain1)
	a24 = MAP(BEZIER(S2)([rim3b,rimDouble3b]))(domaininv)
	a25 = MAP(BEZIER(S2)([rim4b,rimDouble4b]))(domain1)
	a26 = MAP(BEZIER(S2)([rim5b,rimDouble5b]))(domaininv)
	
	a27 = MAP(BEZIER(S2)([rimDouble1a,rimDouble2a]))(domaininv)
	a28 = MAP(BEZIER(S2)([rimDouble1b,rimDouble2b]))(domain1)
	a29 = MAP(BEZIER(S2)([rimDouble3a,rimDouble4a]))(domaininv)
	a30 = MAP(BEZIER(S2)([rimDouble3b,rimDouble4b]))(domain1)
	a31 = MAP(BEZIER(S2)([rimDouble5a,rimDouble5b]))(domaininv)
	
	radius = STRUCT([a13,a21,a26,a31])
	a14 = T([1,2])(-0.05)(R([1,2])(PI/2)(radius))
	a15 = R([1,2])(PI)(radius)
	a16 = T([1,2])(0.05)(R([1,2])(3*PI/2)(radius))

	a32 = T([1,2])(-0.05)(R([1,2])(PI/2)(radius))
	a33 = R([1,2])(PI)(radius)
	a34 = T([1,2])(0.05)(R([1,2])(3*PI/2)(radius))
	
	part1 = STRUCT([a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20])
	part2 = STRUCT([a21,a22,a23,a24,a25,a26,a27,a28,a29,a30,a31,a32,a33,a34])
	return STRUCT([part1,part2])



a1 = MAP(BEZIER(S2)([wheel1a,wheel2a]))(domain1)
a2 = MAP(BEZIER(S2)([wheel1b,wheel2b]))(domaininv)
a3 = MAP(BEZIER(S2)([wheel3a,wheel1a]))(domain1)
a4 = MAP(BEZIER(S2)([wheel3b,wheel1b]))(domaininv)
a5 = MAP(BEZIER(S2)([wheel3a,wheel4a]))(domaininv)

a6 = MAP(BEZIER(S2)([wheel3b,wheel4b]))(domain1)
a7 = MAP(BEZIER(S2)([wheel2b,wheel4b]))(domain1)
a8 = MAP(BEZIER(S2)([wheel2a,wheel4a]))(domaininv)

rim1 = rim_star(0,0,0.1)
rim2 = rim_star(1,1,0.1)

wheel = S([1,2,3])([2,2,2])(STRUCT([a1,a2,a3,a4,a5,a6,a7,a8,T([3,1])(0.1)(rim1),rim2]))

skeleton_and_wheels = STRUCT([T([3,1])(-4.6)(T([1,2])(-8)(T([2,1])(-3.3)(wheel))),T([3,1])(2.5)(T([1,2])(-8)(T([2,1])(-3.3)(wheel))),
	T([3,1])(2.5)(T([1,2])(9)(T([2,1])(-3.3)(wheel))),skeleton,T([3,1])(-4.6)(T([1,2])(9)(T([2,1])(-3.3)(wheel)))])

VIEW(skeleton_and_wheels)


