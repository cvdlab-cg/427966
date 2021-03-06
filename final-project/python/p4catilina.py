
def semicircle_a(x1,y1,z,tx,ty,tz1,tz2):
	semix = float(x1)/2
	semia = BEZIER(S1)([[tx+semix,ty,z+tz1],[tx+semix,ty+y1,z+tz2],[tx-semix,ty+y1,z+tz2],[tx-semix,ty,z+tz1]])
	return semia

def semicircle_b(x1,y1,z,tx,ty,tz1,tz2):
	semix = float(x1)/2
	semib = BEZIER(S1)([[tx+semix,ty,z+tz1],[tx+semix,-y1+ty,z+tz2],[tx-semix,-y1+ty,z+tz2],[tx-semix,ty,z+tz1]])
	return semib

domain1 = INTERVALS(1)(32);
domain2 =  PROD([domain1,domain1])
domaininv = MAP([S2,S1])(domain2)
darkwood_color = [0.36,0.25,0.2]

#####################################################P4 CATILINA CHAIR###############################################################

#####################################THE BASE OF THE CHAIR#######################################

#THE CURVES OF THE BASE#
curve1_base = BEZIER(S1)([[0.6,-1,0],[1,-0.9,0],[1,0,0],[1,0.9,0],[-1,0.9,0],[-1,0,0],[-1,-0.9,0],[-0.6,-1,0]])
curve2_base = BEZIER(S1)([[0.6,-1.12,0],[1.1,-1,0],[1.2,0,0],[1.2,1.1,0],[-1.2,1.1,0],[-1.2,0,0],[-1.1,-1,0],[-0.6,-1.12,0]])
curve3_base = BEZIER(S1)([[0.6,-1,0.02],[1,-0.9,0.02],[1,0,0.02],[1,0.9,0.02],[-1,0.9,0.02],[-1,0,0.02],[-1,-0.9,0.02],[-0.6,-1,0.02]])
curve4_base = BEZIER(S1)([[0.6,-1.12,0.02],[1.1,-1,0.02],[1.2,0,0.02],[1.2,1.1,0.02],[-1.2,1.1,0.02],[-1.2,0,0.02],[-1.1,-1,0.02],[-0.6,-1.12,0.02]])

#THE MAPS OF THE BASE#
map1_base = MAP(BEZIER(S2)([curve1_base,curve2_base]))(domain2)
map2_base = MAP(BEZIER(S2)([curve3_base,curve4_base]))(domain2)
map3_base = MAP(BEZIER(S2)([curve1_base,curve3_base]))(domain2)
map4_base = MAP(BEZIER(S2)([curve2_base,curve4_base]))(domain2)

#THE MODEL OF THE BASE#
base = COLOR(darkwood_color)(S([1,2,3])([1.03,1.03,1.03])(STRUCT([map1_base,map2_base,map3_base,map4_base])))

###########################################THE PILLOW#########################################################

#THE CURVES OF THE PILLOW#
curve1a_pillow = semicircle_a(1.75,1,0.9,0,0,0,0)
curve1b_pillow = semicircle_b(1.75,1,0.9,0,0,0,0)
curve2a_pillow = semicircle_a(1.81,1.04,1.15,0,0,0,0)
curve2b_pillow = semicircle_b(1.81,1.04,1.15,0,0,0,0)
curve3a_pillow = semicircle_a(1.75,1,1.18,0,0,0,0)
curve3b_pillow = semicircle_b(1.75,1,1.18,0,0,0,0)
curve4a_pillow = semicircle_a(1.65,0.9,1.23,0,0,0,0)
curve4b_pillow = semicircle_b(1.65,0.9,1.23,0,0,0,0)
curve5a_pillow = semicircle_a(1.65,0.9,0.85,0,0,0,0)
curve5b_pillow = semicircle_b(1.65,0.9,0.85,0,0,0,0)
curve6a_pillow = semicircle_a(0,0,1.235,0,0,0,0)
curve6b_pillow = semicircle_b(0,0,1.235,0,0,0,0)
curve7a_pillow = semicircle_a(0,0,0.845,0,0,0,0)
curve7b_pillow = semicircle_b(0,0,0.845,0,0,0,0)

#THE MAPS OF THE PILLOW#
map1_pillow = MAP(BEZIER(S2)([curve7a_pillow,curve5a_pillow,curve1a_pillow]))(domain2)
map2_pillow = MAP(BEZIER(S2)([curve7b_pillow,curve5b_pillow,curve1b_pillow]))(domain2)
map3_pillow = MAP(BEZIER(S2)([curve6a_pillow,curve6b_pillow]))(domain2)
map4_pillow = MAP(BEZIER(S2)([curve1a_pillow,curve2a_pillow,curve3a_pillow,curve4a_pillow,curve6a_pillow]))(domain2)
map5_pillow = MAP(BEZIER(S2)([curve1b_pillow,curve2b_pillow,curve3b_pillow,curve4b_pillow,curve6b_pillow]))(domain2)

#THE CURVES OF THE BASE OF THE PILLOW#
curve1a_basepillow = semicircle_a(1.78,1.04,0.845,0,0,0,0)
curve1b_basepillow = semicircle_b(1.78,1.04,0.845,0,0,0,0)
curve2a_basepillow = semicircle_a(1.83,1.04,0.82,0,0,0,0)
curve2b_basepillow = semicircle_b(1.83,1.04,0.82,0,0,0,0)
curve3a_basepillow = semicircle_a(1.78,1.04,0.785,0,0,0,0)
curve3b_basepillow = semicircle_b(1.78,1.04,0.785,0,0,0,0)
curve4a_basepillow = semicircle_a(1.7,1,0.845,0,0,0,0)
curve4b_basepillow = semicircle_b(1.7,1,0.845,0,0,0,0)
curve5a_basepillow = semicircle_a(1.7,1,0.785,0,0,0,0)
curve5b_basepillow = semicircle_b(1.7,1,0.785,0,0,0,0)

#THE MAPS OF THE BASE OF THE PILLOW#
map1_basepillow = MAP(BEZIER(S2)([curve1a_basepillow,curve2a_basepillow,curve3a_basepillow]))(domain2)
map2_basepillow = MAP(BEZIER(S2)([curve1b_basepillow,curve2b_basepillow,curve3b_basepillow]))(domain2)
map3_basepillow = MAP(BEZIER(S2)([curve1a_basepillow,curve4a_basepillow]))(domain2)
map4_basepillow = MAP(BEZIER(S2)([curve1b_basepillow,curve4b_basepillow]))(domain2)
map5_basepillow = MAP(BEZIER(S2)([curve3a_basepillow,curve5a_basepillow]))(domain2)
map6_basepillow = MAP(BEZIER(S2)([curve3b_basepillow,curve5b_basepillow]))(domain2)
map7_basepillow = MAP(BEZIER(S2)([curve4a_basepillow,curve5a_basepillow]))(domain2)
map8_basepillow = MAP(BEZIER(S2)([curve4b_basepillow,curve5b_basepillow]))(domain2)

#THE MODEL OF THE BASE PILLOW#
basepillow = COLOR([0,0,0])(T([3])([0.235])(T([2])([-0.394])(STRUCT([map1_basepillow,map2_basepillow,map3_basepillow,
map4_basepillow,map5_basepillow,map6_basepillow,map7_basepillow,map8_basepillow]))))
#THE MODEL OF THE PILLOW#
pillow = COLOR([0.545,0.27,0.07])(T([2])([-0.394])(STRUCT([map1_pillow,map2_pillow,map3_pillow,map4_pillow,map5_pillow])))

###################################################THE LEGS OF THE CHAIR###########################################################

#THE CURVES OF THE LEGS#
curve1a_leg = semicircle_a(0.06,0.04,0.02,0,0,0,0)
curve1b_leg = semicircle_b(0.06,0.04,0.02,0,0,0,0)
curve2a_leg = semicircle_a(0.06,0.04,2.2,0,0,0,0)
curve2b_leg = semicircle_b(0.06,0.04,2.2,0,0,0,0)

#THE MAPS OF THE LEGS#
map1_leg = MAP(BEZIER(S2)([curve1a_leg,curve2a_leg]))(domain2)
map2_leg = MAP(BEZIER(S2)([curve1b_leg,curve2b_leg]))(domain2)
map3_leg = MAP(BEZIER(S2)([curve2a_leg,curve2b_leg]))(domain2)

#THE MODEL OF THE LEG#
leg = STRUCT([map1_leg,map2_leg,map3_leg])

#THE MODEL OF THE LEGS#
legs = COLOR(darkwood_color)(STRUCT([T([2])([0.42])(S([1,2,3])([1,1,1.12])(leg)),T([1])([0.93])(T([2])([-0.5])(leg)),
	T([1])([-0.93])(T([2])([-0.5])(leg))]))

#############################THE SUPPORT LEG################################

#THE CURVES OF THE SUPPORT LEG#
curve1a_support = semicircle_a(0.04,0.03,0,0,0,0,0)
curve1b_support = semicircle_b(0.04,0.03,0,0,0,0,0)
curve2a_support = semicircle_a(0.04,0.03,1.85,0,0,0,0)
curve2b_support = semicircle_b(0.04,0.03,1.85,0,0,0,0)

#THE MAPS OF THE SUPPORT LEG#
map1_support = MAP(BEZIER(S2)([curve1a_support,curve2a_support]))(domain2)
map2_support = MAP(BEZIER(S2)([curve1b_support,curve2b_support]))(domain2)

#THE MODEL OF THE SUPPORT LEG#
support = COLOR(darkwood_color)(T([1])([0.95])(T([2])([-0.5])(T([3])([1])(R([1,3])(PI/2)(STRUCT([map1_support,map2_support]))))))

###########################################################THE ARMREST#############################################

#THE CURVES OF THE ARMREST#
curve1_armrest = BEZIER(S1)([[1,-0.8,0],[1,0,0],[1,0.8,0.2],[-1,0.8,0.2],[-1,0,0],[-1,-0.8,0]])
curve2_armrest = BEZIER(S1)([[1.13,-0.8,0],[1.15,0,0],[1.2,0.8,0.45],[-1.2,0.8,0.45],[-1.15,0,0],[-1.13,-0.8,0]])
curve3_armrest = BEZIER(S1)([[1.13,-0.82,-0.1],[1.13,-0.84,-0.08],[1.13,-0.8,0]])
curve4_armrest = BEZIER(S1)([[1,-0.82,-0.1],[1,-0.84,-0.08],[1,-0.8,0]])
curve5_armrest = BEZIER(S1)([[-1.13,-0.82,-0.1],[-1.13,-0.84,-0.08],[-1.13,-0.8,0]])
curve6_armrest = BEZIER(S1)([[-1,-0.82,-0.1],[-1,-0.84,-0.08],[-1,-0.8,0]])
curve7_armrest = BEZIER(S1)([[1,-0.8,-0.03],[1,0,-0.05],[1,0.9,0.25],[-1,0.9,0.25],[-1,0,-0.05],[-1,-0.8,-0.03]])
curve8_armrest = BEZIER(S1)([[1.13,-0.8,-0.03],[1.15,0,-0.05],[1.2,0.9,0.5],[-1.2,0.9,0.5],[-1.15,0,-0.05],[-1.13,-0.8,-0.03]])
curve9_armrest = BEZIER(S1)([[1.13,-0.8,-0.1],[1.13,-0.82,-0.07],[1.13,-0.8,-0.03]])
curve10_armrest = BEZIER(S1)([[1,-0.8,-0.1],[1,-0.82,-0.07],[1,-0.8,-0.03]])
curve11_armrest = BEZIER(S1)([[-1.13,-0.8,-0.1],[-1.13,-0.82,-0.07],[-1.13,-0.8,-0.03]])
curve12_armrest = BEZIER(S1)([[-1,-0.8,-0.1],[-1,-0.82,-0.07],[-1,-0.8,-0.03]])

#THE MAPS OF THE ARMREST#
map1_armrest = MAP(BEZIER(S2)([curve1_armrest,curve2_armrest]))(domain2)
map2_armrest = MAP(BEZIER(S2)([curve3_armrest,curve4_armrest]))(domain2)
map3_armrest = MAP(BEZIER(S2)([curve5_armrest,curve6_armrest]))(domain2)
map4_armrest = MAP(BEZIER(S2)([curve7_armrest,curve1_armrest]))(domain2)
map5_armrest = MAP(BEZIER(S2)([curve8_armrest,curve2_armrest]))(domain2)
map6_armrest = MAP(BEZIER(S2)([curve7_armrest,curve8_armrest]))(domain2)
map7_armrest = MAP(BEZIER(S2)([curve9_armrest,curve10_armrest]))(domain2)
map8_armrest = MAP(BEZIER(S2)([curve11_armrest,curve12_armrest]))(domain2)
map9_armrest = MAP(BEZIER(S2)([curve3_armrest,curve9_armrest]))(domain2)
map10_armrest = MAP(BEZIER(S2)([curve4_armrest,curve10_armrest]))(domain2)
map11_armrest = MAP(BEZIER(S2)([curve5_armrest,curve11_armrest]))(domain2)
map12_armrest = MAP(BEZIER(S2)([curve6_armrest,curve12_armrest]))(domain2)

#THE MODEL OF THE ARMREST#
armrest = COLOR(darkwood_color)(STRUCT([map1_armrest,map2_armrest,map3_armrest,map4_armrest,map5_armrest
,map6_armrest,map7_armrest,map8_armrest,map9_armrest,map10_armrest,map11_armrest,map12_armrest]))
 
####################THE P4 CATILINA MODEL#######################
p4catilina_finalmodel = STRUCT([base,S([1,2,3])([1,1,1.2])(pillow),legs,basepillow,support,
T([2])([-0.07])(T([3])([2.2])(S([1,2,3])([0.9,0.9,0.9])(armrest)))])

