from header_skins import *
from ID_particle_systems import *
####################################################################################################################
#  Each skin record contains the following fields:
#  1) Skin id: used for referencing skins.
#  2) Skin flags. Not used yet. Should be 0.
#  3) Body mesh.
#  4) Calf mesh (left one).
#  5) Hand mesh (left one).
#  6) Head mesh.
#  7) Face keys (list)
#  8) List of hair meshes.
#  9) List of beard meshes.
# 10) List of hair textures.
# 11) List of beard textures.
# 12) List of face textures.
# 13) List of voices.
# 14) Skeleton name
# 15) Scale (doesn't fully work yet)
# 16) Blood particles 1 (do not add this if you wish to use the default particles)
# 17) Blood particles 2 (do not add this if you wish to use the default particles)
# 17) Face key constraints (do not add this if you do not wish to use it)
####################################################################################################################

man_face_keys = [
(20,0,0.75,-0.9, "Pucker"), 
(260,0,-0.4,0.75, "Chin Shape"), 
(10,0,-0.0,0.6, "Chin Forward"),
(240,0,-0.33,0.9, "Jaw Position"),
(210,0, -0.50, 1.0, "Jaw Width"), 
(250,0,0.75,-0.5, "Mouth-Nose Distance"),
(200,0,-0.66,0.66, "Mouth Width"),
(50,0, -0.66,0.66, "Cheeks"),

(60,0,-0.4,0.66, "Nose Height"),
(70,0,-0.25,0.75, "Nose Width"),
(80,0,0.66,-0.66, "Nose Size"),
(270,0,-0.20,0.66, "Nose Shape"),
(90,0, -0.25,0.75, "Nose Bridge"),

(100,0,-0.66,0.75, "Cheek Bones"),
(150,0,-0.5,0.75, "Eye Width"),
(110,0,0.5,-0.33, "Eye to Eye Dist"),
(120,0,-0.75,0.75, "Eye Shape"),
(130,0,0.75,0.0, "Eye Depth"),
(140,0,0.75,-0.20, "Eyelids"),

(170,0,-0.5,0.75, "Eyebrow Position"),
(160,0,0.75,-0.5, "Eyebrow Height"),
(220,0,0.75,-0.75, "Eyebrow Depth"),
(180,0,-0.5,0.75, "Eyebrow Shape"),
(230,0,0.66,-0.4, "Temple Width"),

(30,0,-0.25,0.75, "Face Depth"),
(40,0,0.33,-0.8, "Face Ratio"),
(190,0,-0.25,0.66, "Face Width"),

(280,0,-0.5,0.75, "Post-Edit"),
]

# Face width-Jaw width Temple width
woman_face_keys = [
(260,0,1.0,-0.33, "Chin Shape"), 
(20,0,1.0,-1.0, "Pucker"), 
(10,0,-0.5,1.0, "Chin Forward"),
(210,0, 1.0, -0.25, "Jaw Width"), 
(240,0,-0.75,0.75, "Jaw Position"),
(250,0,0.66,-0.33, "Mouth-Nose Distance"),
(200,0,-0.2,1.0, "Mouth Width"),
(50,0, -0.4,0.8, "Cheeks"),

(60,0,-0.66,0.75, "Nose Height"),
(70,0,-1.0,0.75, "Nose Width"),
(80,0,-0.75,1.0, "Nose Size"),
(270,0,-0.4,0.6, "Nose Shape"),
(90,0, -0.66,0.9, "Nose Bridge"),

(100,0,-0.6,1.0, "Cheek Bones"),
(150,0,-0.75,0.6, "Eye Width"),
(110,0,0.5,-0.5, "Eye to Eye Dist"),
(120,0,-0.5,0.75, "Eye Shape"),
(130,0,1.00,-0.66, "Eye Depth"),
(140,0,1.0,0.1, "Eyelids"),

(180,0,-0.3,1.0, "Eyebrow Position"),
(160,0,1.2,-0.4, "Eyebrow Height"),
(220,0,-0.75,0.9, "Eyebrow Depth"),
(170,0,-0.8,0.3, "Eyebrow Shape"),
(230,0,0.70,-0.1, "Temple Width"),

(30,0,-1.0,1.0, "Face Depth"),
(40,0,1.0,-0.75, "Face Ratio"),
(190,0,0.5,-0.4, "Face Width"),

(280,0,-0.5,0.75, "Post-Edit"),
]

###man alto chief
alto_face_keys = [
(20,0,0.75,-0.9, "Pucker"), 
(260,0,-0.4,0.75, "Chin Shape"), 
(10,0,-0.0,0.6, "Chin Forward"),
(240,0,-0.33,0.9, "Jaw Position"),
(210,0, -0.50, 1.0, "Jaw Width"), 
(250,0,0.75,-0.5, "Mouth-Nose Distance"),
(200,0,-0.66,0.66, "Mouth Width"),
(50,0, -0.66,0.66, "Cheeks"),

(60,0,-0.4,0.66, "Nose Height"),
(70,0,-0.25,0.75, "Nose Width"),
(80,0,0.66,-0.66, "Nose Size"),
(270,0,-0.20,0.66, "Nose Shape"),
(90,0, -0.25,0.75, "Nose Bridge"),

(100,0,-0.66,0.75, "Cheek Bones"),
(150,0,-0.5,0.75, "Eye Width"),
(110,0,0.5,-0.33, "Eye to Eye Dist"),
(120,0,-0.75,0.75, "Eye Shape"),
(130,0,0.75,0.0, "Eye Depth"),
(140,0,0.75,-0.20, "Eyelids"),

(170,0,-0.5,0.75, "Eyebrow Position"),
(160,0,0.75,-0.5, "Eyebrow Height"),
(220,0,0.75,-0.75, "Eyebrow Depth"),
(180,0,-0.5,0.75, "Eyebrow Shape"),
(230,0,0.66,-0.4, "Temple Width"),

(30,0,-0.25,0.75, "Face Depth"),
(40,0,0.33,-0.8, "Face Ratio"),
(190,0,-0.25,0.66, "Face Width"),

(280,0,-0.5,0.75, "Post-Edit"),
]

# mujer alta
alta_face_keys = [
(260,0,1.0,-0.33, "Chin Shape"), 
(20,0,1.0,-1.0, "Pucker"), 
(10,0,-0.5,1.0, "Chin Forward"),
(210,0, 1.0, -0.25, "Jaw Width"), 
(240,0,-0.75,0.75, "Jaw Position"),
(250,0,0.66,-0.33, "Mouth-Nose Distance"),
(200,0,-0.2,1.0, "Mouth Width"),
(50,0, -0.4,0.8, "Cheeks"),

(60,0,-0.66,0.75, "Nose Height"),
(70,0,-1.0,0.75, "Nose Width"),
(80,0,-0.75,1.0, "Nose Size"),
(270,0,-0.4,0.6, "Nose Shape"),
(90,0, -0.66,0.9, "Nose Bridge"),

(100,0,-0.6,1.0, "Cheek Bones"),
(150,0,-0.75,0.6, "Eye Width"),
(110,0,0.5,-0.5, "Eye to Eye Dist"),
(120,0,-0.5,0.75, "Eye Shape"),
(130,0,1.00,-0.66, "Eye Depth"),
(140,0,1.0,0.1, "Eyelids"),

(180,0,-0.3,1.0, "Eyebrow Position"),
(160,0,1.2,-0.4, "Eyebrow Height"),
(220,0,-0.75,0.9, "Eyebrow Depth"),
(170,0,-0.8,0.3, "Eyebrow Shape"),
(230,0,0.70,-0.1, "Temple Width"),

(30,0,-1.0,1.0, "Face Depth"),
(40,0,1.0,-0.75, "Face Ratio"),
(190,0,0.5,-0.4, "Face Width"),

(280,0,-0.5,0.75, "Post-Edit"),
]

#man bajo chief
bajo_face_keys = [
(20,0,0.75,-0.9, "Pucker"), 
(260,0,-0.4,0.75, "Chin Shape"), 
(10,0,-0.0,0.6, "Chin Forward"),
(240,0,-0.33,0.9, "Jaw Position"),
(210,0, -0.50, 1.0, "Jaw Width"), 
(250,0,0.75,-0.5, "Mouth-Nose Distance"),
(200,0,-0.66,0.66, "Mouth Width"),
(50,0, -0.66,0.66, "Cheeks"),

(60,0,-0.4,0.66, "Nose Height"),
(70,0,-0.25,0.75, "Nose Width"),
(80,0,0.66,-0.66, "Nose Size"),
(270,0,-0.20,0.66, "Nose Shape"),
(90,0, -0.25,0.75, "Nose Bridge"),

(100,0,-0.66,0.75, "Cheek Bones"),
(150,0,-0.5,0.75, "Eye Width"),
(110,0,0.5,-0.33, "Eye to Eye Dist"),
(120,0,-0.75,0.75, "Eye Shape"),
(130,0,0.75,0.0, "Eye Depth"),
(140,0,0.75,-0.20, "Eyelids"),

(170,0,-0.5,0.75, "Eyebrow Position"),
(160,0,0.75,-0.5, "Eyebrow Height"),
(220,0,0.75,-0.75, "Eyebrow Depth"),
(180,0,-0.5,0.75, "Eyebrow Shape"),
(230,0,0.66,-0.4, "Temple Width"),

(30,0,-0.25,0.75, "Face Depth"),
(40,0,0.33,-0.8, "Face Ratio"),
(190,0,-0.25,0.66, "Face Width"),

(280,0,-0.5,0.75, "Post-Edit"),
]

# mujer baja
baja_face_keys = [
(260,0,1.0,-0.33, "Chin Shape"), 
(20,0,1.0,-1.0, "Pucker"), 
(10,0,-0.5,1.0, "Chin Forward"),
(210,0, 1.0, -0.25, "Jaw Width"), 
(240,0,-0.75,0.75, "Jaw Position"),
(250,0,0.66,-0.33, "Mouth-Nose Distance"),
(200,0,-0.2,1.0, "Mouth Width"),
(50,0, -0.4,0.8, "Cheeks"),

(60,0,-0.66,0.75, "Nose Height"),
(70,0,-1.0,0.75, "Nose Width"),
(80,0,-0.75,1.0, "Nose Size"),
(270,0,-0.4,0.6, "Nose Shape"),
(90,0, -0.66,0.9, "Nose Bridge"),

(100,0,-0.6,1.0, "Cheek Bones"),
(150,0,-0.75,0.6, "Eye Width"),
(110,0,0.5,-0.5, "Eye to Eye Dist"),
(120,0,-0.5,0.75, "Eye Shape"),
(130,0,1.00,-0.66, "Eye Depth"),
(140,0,1.0,0.1, "Eyelids"),

(180,0,-0.3,1.0, "Eyebrow Position"),
(160,0,1.2,-0.4, "Eyebrow Height"),
(220,0,-0.75,0.9, "Eyebrow Depth"),
(170,0,-0.8,0.3, "Eyebrow Shape"),
(230,0,0.70,-0.1, "Temple Width"),

(30,0,-1.0,1.0, "Face Depth"),
(40,0,1.0,-0.75, "Face Ratio"),
(190,0,0.5,-0.4, "Face Width"),

(280,0,-0.5,0.75, "Post-Edit"),
]

##oso face keys chief
oso_face_keys = [
(20,0,0.75,-0.9, "Pucker"), 
(260,0,-0.4,0.75, "Chin Shape"), 
(10,0,-0.0,0.6, "Chin Forward"),
(240,0,-0.33,0.9, "Jaw Position"),
(210,0, -0.50, 1.0, "Jaw Width"), 
(250,0,0.75,-0.5, "Mouth-Nose Distance"),
(200,0,-0.66,0.66, "Mouth Width"),
(50,0, -0.0,0.66, "Cheeks"),

(60,0,-0.4,0.66, "Nose Height"),
(70,0,-0.25,0.75, "Nose Width"),
(80,0,0.66,-0.66, "Nose Size"),
(270,0,-0.20,0.66, "Nose Shape"),
(90,0, -0.25,0.75, "Nose Bridge"),

(100,0,-0.66,0.75, "Cheek Bones"),
(150,0,-0.5,0.75, "Eye Width"),
(110,0,0.5,-0.33, "Eye to Eye Dist"),
(120,0,-0.75,0.75, "Eye Shape"),
(130,0,0.75,0.0, "Eye Depth"),
(140,0,0.75,-0.20, "Eyelids"),

(170,0,-0.5,0.75, "Eyebrow Position"),
(160,0,0.75,-0.5, "Eyebrow Height"),
(220,0,0.75,-0.75, "Eyebrow Depth"),
(180,0,-0.5,0.75, "Eyebrow Shape"),
(230,0,0.66,-0.4, "Temple Width"),

(30,0,-0.25,0.75, "Face Depth"),
(40,0,0.33,-0.8, "Face Ratio"),
(190,0,-0.25,0.66, "Face Width"),

(280,0,-0.5,0.75, "Post-Edit"),
]

##osa face keys chief
osa_face_keys = [
(260,0,1.0,-0.33, "Chin Shape"), 
(20,0,1.0,-1.0, "Pucker"), 
(10,0,-0.5,1.0, "Chin Forward"),
(210,0, 1.0, -0.25, "Jaw Width"), 
(240,0,-0.75,0.75, "Jaw Position"),
(250,0,0.66,-0.33, "Mouth-Nose Distance"),
(200,0,-0.2,1.0, "Mouth Width"),
(50,0, -0.4,0.8, "Cheeks"),

(60,0,-0.66,0.75, "Nose Height"),
(70,0,-1.0,0.75, "Nose Width"),
(80,0,-0.75,1.0, "Nose Size"),
(270,0,-0.4,0.6, "Nose Shape"),
(90,0, -0.66,0.9, "Nose Bridge"),

(100,0,-0.6,1.0, "Cheek Bones"),
(150,0,-0.75,0.6, "Eye Width"),
(110,0,0.5,-0.5, "Eye to Eye Dist"),
(120,0,-0.5,0.75, "Eye Shape"),
(130,0,1.00,-0.66, "Eye Depth"),
(140,0,1.0,0.1, "Eyelids"),

(180,0,-0.3,1.0, "Eyebrow Position"),
(160,0,1.2,-0.4, "Eyebrow Height"),
(220,0,-0.75,0.9, "Eyebrow Depth"),
(170,0,-0.8,0.3, "Eyebrow Shape"),
(230,0,0.70,-0.1, "Temple Width"),

(30,0,-1.0,1.0, "Face Depth"),
(40,0,1.0,-0.75, "Face Ratio"),
(190,0,0.5,-0.4, "Face Width"),

(280,0,-0.5,0.75, "Post-Edit"),
]

#nino chief
nino_face_keys = [
(20,0,0.75,-0.25, "Pucker"), 
(260,0,-0.2,0.4, "Chin Shape"), 
(10,0,-0.3,0.3, "Chin Forward"),
(240,0,0.4,0.75, "Jaw Position"),
(210,0, 0.4, 0.8, "Jaw Width"), 
(250,0,-0.5,0.0, "Mouth-Nose Distance"),
(200,0,-0.50,0.20, "Mouth Width"),
(50,0, -0.4,0.4, "Cheeks"),

(60,0,-0.3,0.4, "Nose Height"),
(70,0,-0.4,0.1, "Nose Width"),
(80,0,0.75,-0.00, "Nose Size"),
(270,0,-0.30,0.20, "Nose Shape"),
(90,0, -0.25,0.20, "Nose Bridge"),

(100,0,-0.75,0.00, "Cheek Bones"),
(150,0,0.0,1.2, "Eye Width"),
(110,0,0.5,0.00, "Eye to Eye Dist"),
(120,0,-0.75,0.75, "Eye Shape"),
(130,0,0.75,0.0, "Eye Depth"),
(140,0,0.25,-0.40, "Eyelids"),

(170,0,-0.5,0.75, "Eyebrow Position"),
(160,0,0.75,-0.5, "Eyebrow Height"),
(220,0,0.75,-0.4, "Eyebrow Depth"),
(180,0,-0.5,0.2, "Eyebrow Shape"),
(230,0,0.00,-0.75, "Temple Width"),

(30,0,-0.33,0.20, "Face Depth"),
(40,0,1.0,0.2, "Face Ratio"),
(190,0,0.30,0.8, "Face Width"),

(280,0,-0.5,0.75, "Post-Edit"),
]

#nina
nina_face_keys = [
(260,0,0.66,-0.33, "Chin Shape"), 
(20,0,1.0,-1.0, "Pucker"), 
(10,0,-0.5,0.5, "Chin Forward"),
(210,0, 0.50, -0.25, "Jaw Width"), 
(240,0,-0.5,0.5, "Jaw Position"),
(250,0,0.66,-0.33, "Mouth-Nose Distance"),
(200,0,-0.2,1.0, "Mouth Width"),
(50,0, 0.2,1.0, "Cheeks"),

(60,0,-0.75,0.00, "Nose Height"),
(70,0,-1.0,0.00, "Nose Width"),
(80,0,-0.75,1.0, "Nose Size"),
(270,0,-0.6,0.0, "Nose Shape"),
(90,0, -0.75,0.30, "Nose Bridge"),

(100,0,-1.0,0.0, "Cheek Bones"),
(150,0,0.5,1.5, "Eye Width"),
(110,0,0.5,-0.5, "Eye to Eye Dist"),
(120,0,-0.5,0.75, "Eye Shape"),
(130,0,1.00,-0.66, "Eye Depth"),
(140,0,0.5,0.5, "Eyelids"),

(180,0,-0.3,1.0, "Eyebrow Position"),
(160,0,1.2,-0.4, "Eyebrow Height"),
(220,0,-0.75,0.9, "Eyebrow Depth"),
(170,0,-0.8,0.3, "Eyebrow Shape"),
(230,0,0.30,-0.2, "Temple Width"),

(30,0,-1.0,0.0, "Face Depth"),
(40,0,1.5,0.5, "Face Ratio"),
(190,0,0.0,-1.0, "Face Width"),

(280,0,-0.5,0.75, "Post-Edit"),
]

#undead_face_keys = []

###nino 
undead_face_keys = [
(20,0,0.75,-0.9, "Chin Shape"), 
(260,0,-0.4,0.75, "Chin Size"), 
(10,0,-0.60,1.20, "Chin Forward"),
(240,0,-0.33,0.9, "Jaw Position"),
(210,0, -0.50, 1.0, "Jaw Width"), 
(250,0,0.75,-0.5, "Mouth-Nose Distance"),
(200,0,-0.66,0.66, "Mouth Width"),
(50,0, -0.66,0.66, "Cheeks"),

(60,0,-0.4,0.66, "Nose Height"),
(70,0,-0.25,0.75, "Nose Width"),
(80,0,0.66,-0.66, "Nose Size"),
(270,0,-0.20,0.66, "Nose Shape"),
(90,0, -0.25,0.75, "Nose Bridge"),

(100,0,-0.66,0.75, "Cheek Bones"),
(150,0,-0.5,0.75, "Eye Width"),
(110,0,0.5,-0.33, "Eye to Eye Dist"),
(120,0,-0.75,0.75, "Eye Shape"),
(130,0,0.75,0.0, "Eye Depth"),
(140,0,0.75,-0.20, "Eyelids"),


(170,0,-0.5,0.75, "Eyebrow Position"),
(160,0,0.75,-0.5, "Eyebrow Height"),
(220,0,0.75,-0.75, "Eyebrow Depth"),
(180,0,-0.5,0.75, "Eyebrow Shape"),
(230,0,0.66,-0.4, "Temple Width"),

(30,0,-0.25,0.75, "Face Depth"),
(40,0,0.33,-0.8, "Face Ratio"),
(190,0,-0.25,0.66, "Face Width"),

(280,0,-0.5,0.75, "Post-Edit"),
]


chin_size = 0
chin_shape = 1
chin_forward = 2
jaw_width = 3
jaw_position = 4
mouth_nose_distance = 5
mouth_width = 6
cheeks = 7
nose_height = 8
nose_width = 9
nose_size = 10
nose_shape = 11
nose_bridge = 12
cheek_bones = 13
eye_width = 14
eye_to_eye_dist = 15
eye_shape = 16
eye_depth = 17
eyelids = 18
eyebrow_position = 19
eyebrow_height = 20
eyebrow_depth = 21
eyebrow_shape = 22
temple_width = 23
face_depth = 24
face_ratio = 25
face_width = 26

all_beards = [
	"VC_Beard01","VC_Beard02","VC_Beard03","VC_Beard04","VC_Beard05","VC_Beard06","VC_Beard07","VC_Beard08","VC_Beard10","VC_Beard11","VC_Beard12","VC_Beard14","VC_Beard16","VC_Beard18",
	"VC_Beard22","VC_Beard23","VC_Beard26","VC_Beard28","VC_Beard29","VC_Beard30","VC_Beard31","VC_Beard32","VC_Beard33","VC_Beard35","VC_Beard36","VC_Beard39","VC_Beard40","VC_Beard46",
	"VC_Beard47","VC_Beard48","VC_Beard49",
	#Next line of beards is to much for OpenBrf:
	#"VC_Beard45","VC_Beard42","VC_Beard37","VC_Beard24","VC_Beard27","VC_Beard25","VC_Beard38","VC_Beard34","VC_Beard21","VC_Beard19","VC_Beard20","VC_Beard9","VC_Beard13","VC_Beard15","VC_Beard17",
	]

comp_less_than = -1;
comp_greater_than = 1;

# VC2.060 it turns out the skel_* system was largely (but not completely) replaced by undocumented hard-coded model sizes

skins = [
  (
    "man", 0,
    "man_body_new", "man_calf_l", "m_handL",
    "male_head", man_face_keys,
    ["VC_Hair_Male_01","VC_Hair_Male_02","VC_Hair_Male_03","VC_Hair_Male_04","VC_Hair_Male_05","VC_Hair_Male_06","VC_Hair_Male_07","VC_Hair_Male_08","VC_Hair_Male_09","VC_Hair_Male_10",
     "VC_Hair_Male_11","VC_Hair_Male_12","VC_Hair_Male_13","VC_Hair_Male_14","VC_Hair_Male_15","VC_Hair_Male_16","VC_Hair_Male_17","VC_Hair_Male_18","VC_Hair_Male_19","VC_Hair_Male_20","VC_Hair_Male_21",], #man_hair_meshes ,"man_hair_y5","man_hair_y8",
    all_beards, 
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"], #hair textures
    ["beard_blonde","beard_red","beard_brunette","beard_black","beard_white"], #beard_materials
    [
     ("manface_basic",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("manface_basic2",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("manface_warrior",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("manface_warriorb",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("manface_warrior2",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("manface_warrior2b",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("manface_thin",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),     
     ("manface_thin2",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),     
     ("manface_thin2b",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),     
     ("manface_old",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
##painted only pictish
     ("manface_basicb",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("manface_basic2b",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("manface_thinb",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),     
     ], #man_face_textures,
    [(voice_die,"snd_man_die"),(voice_hit,"snd_man_hit"),(voice_grunt,"snd_man_grunt"),(voice_grunt_long,"snd_man_grunt_long"),(voice_yell,"snd_man_yell"),(voice_stun,"snd_man_stun"),(voice_victory,"snd_man_victory")], #voice sounds
    "skel_human", 0.96,
    psys_game_blood,psys_game_blood_2,
    [[1.7, comp_greater_than, (1.0,face_width), (1.0,temple_width)], #constraints: ex: 1.7 > (face_width + temple_width)
     [0.3, comp_less_than, (1.0,face_width), (1.0,temple_width)],
     [1.7, comp_greater_than, (1.0,face_width), (1.0,face_depth)],
     [0.3, comp_less_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [1.7, comp_greater_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [-0.7, comp_less_than, (1.0,nose_size), (-1.0,nose_shape)],
     [0.7, comp_greater_than, (1.0,nose_size), (-1.0,nose_shape)],
     [2.7, comp_greater_than, (1.0,chin_size), (1.0,mouth_nose_distance), (1.0,nose_height), (-1.0,face_width)],
     ]
  ),

  (
    "woman", skf_use_morph_key_10,
    "woman_body_new",  "woman_calf_l", "f_handL",
    "female_head", woman_face_keys,
    ["VC_Hair_Female_01","VC_Hair_Female_02","VC_Hair_Female_03","VC_Hair_Female_04","VC_Hair_Female_05","VC_Hair_Female_06","VC_Hair_Female_07","VC_Hair_Female_08","VC_Hair_Female_09","VC_Hair_Female_10",
     "VC_Hair_Female_11","VC_Hair_Female_12","VC_Hair_Female_13","VC_Hair_Female_14","VC_Hair_Female_15","VC_Hair_Female_16","VC_Hair_Female_17","VC_Hair_Female_18","VC_Hair_Female_19","VC_Hair_Female_20",
     "VC_Hair_Female_21","VC_Hair_Female_22","VC_Hair_Female_23","VC_Hair_Female_24","VC_Hair_Female_25",], #woman_hair_meshes
#    ["woman_hair_a","woman_hair_b","woman_hair_c","woman_hair_d","woman_hair_e","woman_hair_f","woman_hair_g"], #woman_hair_meshes
    [],
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"], #hair textures
    [],
    [
     ("womanface_basic",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("womanface_basic2",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("womanface_old",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("womanface_warrior",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("womanface_warrior2",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("womanface_thin",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("womanface_thin2",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ],#woman_face_textures
    [(voice_die,"snd_woman_die"),(voice_hit,"snd_woman_hit"),(voice_yell,"snd_woman_yell")], #voice sounds
    "skel_human", 0.89,
    psys_game_blood,psys_game_blood_2,
  ),


  (
    "alto", 0,
    "man_body_new", "man_calf_l", "m_handL",
    "male_head", alto_face_keys,
    ["VC_Hair_Male_01","VC_Hair_Male_02","VC_Hair_Male_03","VC_Hair_Male_04","VC_Hair_Male_05","VC_Hair_Male_06","VC_Hair_Male_07","VC_Hair_Male_08","VC_Hair_Male_09","VC_Hair_Male_10",
     "VC_Hair_Male_11","VC_Hair_Male_12","VC_Hair_Male_13","VC_Hair_Male_14","VC_Hair_Male_15","VC_Hair_Male_16","VC_Hair_Male_17","VC_Hair_Male_18","VC_Hair_Male_19","VC_Hair_Male_20","VC_Hair_Male_21",], #man_hair_meshes ,"man_hair_y5","man_hair_y8",
    all_beards, #beard meshes ,"beard_q"
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"], #hair textures
    ["beard_blonde","beard_red","beard_brunette","beard_black","beard_white"], #beard_materials
    [
     ("manface_basic",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("manface_basic2",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("manface_warrior",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("manface_warriorb",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("manface_warrior2",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("manface_warrior2b",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("manface_thin",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),     
     ("manface_thin2",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),     
     ("manface_thin2b",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),     
     ("manface_old",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
##painted only pictish
     ("manface_basicb",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("manface_basic2b",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("manface_thinb",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),     
     ], #man_face_textures,
    [(voice_die,"snd_man_die"),(voice_hit,"snd_man_hit"),(voice_grunt,"snd_man_grunt"),(voice_grunt_long,"snd_man_grunt_long"),(voice_yell,"snd_man_yell"),(voice_stun,"snd_man_stun"),(voice_victory,"snd_man_victory")], #voice sounds
    "skel_human", 1.0,
    psys_game_blood,psys_game_blood_2,
    [[1.7, comp_greater_than, (1.0,face_width), (1.0,temple_width)], #constraints: ex: 1.7 > (face_width + temple_width)
     [0.3, comp_less_than, (1.0,face_width), (1.0,temple_width)],
     [1.7, comp_greater_than, (1.0,face_width), (1.0,face_depth)],
     [0.3, comp_less_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [1.7, comp_greater_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [-0.7, comp_less_than, (1.0,nose_size), (-1.0,nose_shape)],
     [0.7, comp_greater_than, (1.0,nose_size), (-1.0,nose_shape)],
     [2.7, comp_greater_than, (1.0,chin_size), (1.0,mouth_nose_distance), (1.0,nose_height), (-1.0,face_width)],
     ]
  ),

  (
    "alta", skf_use_morph_key_10,
    "woman_body_new",  "woman_calf_l", "f_handL",
    "female_head", alta_face_keys,
    ["VC_Hair_Female_01","VC_Hair_Female_02","VC_Hair_Female_03","VC_Hair_Female_04","VC_Hair_Female_05","VC_Hair_Female_06","VC_Hair_Female_07","VC_Hair_Female_08","VC_Hair_Female_09","VC_Hair_Female_10",
     "VC_Hair_Female_11","VC_Hair_Female_12","VC_Hair_Female_13","VC_Hair_Female_14","VC_Hair_Female_15","VC_Hair_Female_16","VC_Hair_Female_17","VC_Hair_Female_18","VC_Hair_Female_19","VC_Hair_Female_20",
     "VC_Hair_Female_21","VC_Hair_Female_22","VC_Hair_Female_23","VC_Hair_Female_24","VC_Hair_Female_25",], #woman_hair_meshes
    [],
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"], #hair textures
    [],
    [
     ("womanface_basic",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("womanface_basic2",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("womanface_old",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("womanface_warrior",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("womanface_warrior2",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("womanface_thin",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("womanface_thin2",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
    ],#woman_face_textures
    [(voice_die,"snd_woman_die"),(voice_hit,"snd_woman_hit"),(voice_yell,"snd_woman_yell")], #voice sounds
    "skel_human", 0.93,
    psys_game_blood,psys_game_blood_2,
  ),

  (
    "bajo", 0,
    "man_body_new", "man_calf_l", "m_handL",
    "male_head", bajo_face_keys,
    ["VC_Hair_Male_01","VC_Hair_Male_02","VC_Hair_Male_03","VC_Hair_Male_04","VC_Hair_Male_05","VC_Hair_Male_06","VC_Hair_Male_07","VC_Hair_Male_08","VC_Hair_Male_09","VC_Hair_Male_10",
     "VC_Hair_Male_11","VC_Hair_Male_12","VC_Hair_Male_13","VC_Hair_Male_14","VC_Hair_Male_15","VC_Hair_Male_16","VC_Hair_Male_17","VC_Hair_Male_18","VC_Hair_Male_19","VC_Hair_Male_20","VC_Hair_Male_21",], #man_hair_meshes ,"man_hair_y5","man_hair_y8",
    all_beards, #beard meshes ,"beard_q"
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"], #hair textures
    ["beard_blonde","beard_red","beard_brunette","beard_black","beard_white"], #beard_materials
    [
     ("manface_basic",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("manface_basic2",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("manface_warrior",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("manface_warriorb",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("manface_warrior2",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("manface_warrior2b",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("manface_thin",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),     
     ("manface_thin2",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),     
     ("manface_thin2b",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),     
     ("manface_old",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
##painted only pictish
     ("manface_basicb",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("manface_basic2b",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("manface_thinb",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),     
     ], #man_face_textures,
    [(voice_die,"snd_man_die"),(voice_hit,"snd_man_hit"),(voice_grunt,"snd_man_grunt"),(voice_grunt_long,"snd_man_grunt_long"),(voice_yell,"snd_man_yell"),(voice_stun,"snd_man_stun"),(voice_victory,"snd_man_victory")], #voice sounds
    "skel_human", 0.92,
    psys_game_blood,psys_game_blood_2,
    [[1.7, comp_greater_than, (1.0,face_width), (1.0,temple_width)], #constraints: ex: 1.7 > (face_width + temple_width)
     [0.3, comp_less_than, (1.0,face_width), (1.0,temple_width)],
     [1.7, comp_greater_than, (1.0,face_width), (1.0,face_depth)],
     [0.3, comp_less_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [1.7, comp_greater_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [-0.7, comp_less_than, (1.0,nose_size), (-1.0,nose_shape)],
     [0.7, comp_greater_than, (1.0,nose_size), (-1.0,nose_shape)],
     [2.7, comp_greater_than, (1.0,chin_size), (1.0,mouth_nose_distance), (1.0,nose_height), (-1.0,face_width)],
     ]
  ),

  (
    "baja", skf_use_morph_key_10,
    "woman_body_new",  "woman_calf_l", "f_handL",
    "female_head", baja_face_keys,
    ["VC_Hair_Female_01","VC_Hair_Female_02","VC_Hair_Female_03","VC_Hair_Female_04","VC_Hair_Female_05","VC_Hair_Female_06","VC_Hair_Female_07","VC_Hair_Female_08","VC_Hair_Female_09","VC_Hair_Female_10",
     "VC_Hair_Female_11","VC_Hair_Female_12","VC_Hair_Female_13","VC_Hair_Female_14","VC_Hair_Female_15","VC_Hair_Female_16","VC_Hair_Female_17","VC_Hair_Female_18","VC_Hair_Female_19","VC_Hair_Female_20",
     "VC_Hair_Female_21","VC_Hair_Female_22","VC_Hair_Female_23","VC_Hair_Female_24","VC_Hair_Female_25",], #woman_hair_meshes
    [],
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"], #hair textures
    [],
    [
     ("womanface_basic",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("womanface_basic2",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("womanface_old",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("womanface_warrior",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("womanface_warrior2",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("womanface_thin",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("womanface_thin2",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ],#woman_face_textures
    [(voice_die,"snd_woman_die"),(voice_hit,"snd_woman_hit"),(voice_yell,"snd_woman_yell")], #voice sounds
    "skel_human", 0.86,
    psys_game_blood,psys_game_blood_2,
  ),


####ninos chief
    (
    "nino", 0,
    "man_body_new", "man_calf_l", "m_handL",
    "male_head", nino_face_keys,
    ["VC_Hair_Male_01","VC_Hair_Male_02","VC_Hair_Male_03","VC_Hair_Male_04","VC_Hair_Male_05",], #man_hair_meshes ,"man_hair_y5","man_hair_y8",
    [], #beard meshes ,"beard_q"
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"], #hair textures
    [], #beard_materials
    [
     ("manface_basic2",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("manface_thin",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),     
    ], #man_face_textures,
    [(voice_die,"snd_man_die"),(voice_hit,"snd_man_hit"),(voice_grunt,"snd_man_grunt"),(voice_grunt_long,"snd_man_grunt_long"),(voice_yell,"snd_man_yell"),(voice_stun,"snd_man_stun"),(voice_victory,"snd_man_victory")], #voice sounds
    "skel_human", 0.72,
    psys_no_blood,psys_no_blood,
    [[1.7, comp_greater_than, (1.0,face_width), (1.0,temple_width)], #constraints: ex: 1.7 > (face_width + temple_width)
     [0.3, comp_less_than, (1.0,face_width), (1.0,temple_width)],
     [1.7, comp_greater_than, (1.0,face_width), (1.0,face_depth)],
     [0.3, comp_less_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [1.7, comp_greater_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [-0.7, comp_less_than, (1.0,nose_size), (-1.0,nose_shape)],
     [0.7, comp_greater_than, (1.0,nose_size), (-1.0,nose_shape)],
     [2.7, comp_greater_than, (1.0,chin_size), (1.0,mouth_nose_distance), (1.0,nose_height), (-1.0,face_width)],
     ]
  ),

  (
#    "nina", skf_use_morph_key_10,
    "nina", skf_use_morph_key_10,
    "woman_body_new",  "woman_calf_l", "f_handL",
    "female_head", nina_face_keys,
    ["VC_Hair_Female_01","VC_Hair_Female_02","VC_Hair_Female_03","VC_Hair_Female_04","VC_Hair_Female_05","VC_Hair_Female_06","VC_Hair_Female_07","VC_Hair_Female_08","VC_Hair_Female_09","VC_Hair_Female_10",
     "VC_Hair_Female_11","VC_Hair_Female_12","VC_Hair_Female_13","VC_Hair_Female_14","VC_Hair_Female_15","VC_Hair_Female_16","VC_Hair_Female_17","VC_Hair_Female_18","VC_Hair_Female_19","VC_Hair_Female_20",
     "VC_Hair_Female_21","VC_Hair_Female_22","VC_Hair_Female_23","VC_Hair_Female_24","VC_Hair_Female_25",], #woman_hair_meshes
    [],
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"], #hair textures
    [],
    [
     ("womanface_basic",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("womanface_basic2",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("womanface_warrior",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("womanface_thin",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("womanface_thin2",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ],#woman_face_textures
    [(voice_die,"snd_woman_die"),(voice_hit,"snd_woman_hit"),(voice_yell,"snd_woman_yell")], #voice sounds
    "skel_human", 0.72,
    psys_game_blood,psys_game_blood_2,
  ),
#####ninos acaba

  (
    "oso", 0,
    "man_body_new", "man_calf_l", "m_handL",
    "male_head", oso_face_keys,
    ["VC_Hair_Male_01","VC_Hair_Male_02","VC_Hair_Male_03","VC_Hair_Male_04","VC_Hair_Male_05","VC_Hair_Male_06","VC_Hair_Male_07","VC_Hair_Male_08","VC_Hair_Male_09","VC_Hair_Male_10",
     "VC_Hair_Male_11","VC_Hair_Male_12","VC_Hair_Male_13","VC_Hair_Male_14","VC_Hair_Male_15","VC_Hair_Male_16","VC_Hair_Male_17","VC_Hair_Male_18","VC_Hair_Male_19","VC_Hair_Male_20","VC_Hair_Male_21",], #man_hair_meshes ,"man_hair_y5","man_hair_y8",
    all_beards, #beard meshes ,"beard_q"
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"], #hair textures
    ["beard_blonde","beard_red","beard_brunette","beard_black","beard_white"], #beard_materials
    [
     ("manface_basic",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("manface_basic2",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("manface_warrior",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("manface_warriorb",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("manface_warrior2",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("manface_warrior2b",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("manface_thin",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),     
     ("manface_thin2",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),     
     ("manface_thin2b",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),     
     ("manface_old",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
##painted only pictish
     ("manface_basicb",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("manface_basic2b",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("manface_thinb",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),     
     ], #man_face_textures,
    [(voice_die,"snd_man_die"),(voice_hit,"snd_man_hit"),(voice_grunt,"snd_man_grunt"),(voice_grunt_long,"snd_man_grunt_long"),(voice_yell,"snd_man_yell"),(voice_stun,"snd_man_stun"),(voice_victory,"snd_man_victory")], #voice sounds
    "skel_human", 1.04,
    psys_game_blood,psys_game_blood_2,
    [[1.7, comp_greater_than, (1.0,face_width), (1.0,temple_width)], #constraints: ex: 1.7 > (face_width + temple_width)
     [0.3, comp_less_than, (1.0,face_width), (1.0,temple_width)],
     [1.7, comp_greater_than, (1.0,face_width), (1.0,face_depth)],
     [0.3, comp_less_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [1.7, comp_greater_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [-0.7, comp_less_than, (1.0,nose_size), (-1.0,nose_shape)],
     [0.7, comp_greater_than, (1.0,nose_size), (-1.0,nose_shape)],
     [2.7, comp_greater_than, (1.0,chin_size), (1.0,mouth_nose_distance), (1.0,nose_height), (-1.0,face_width)],
     ]
  ),
    
  (
    "osa", skf_use_morph_key_10,
    "woman_body_new",  "woman_calf_l", "f_handL",
    "female_head", osa_face_keys,
    ["VC_Hair_Female_01","VC_Hair_Female_02","VC_Hair_Female_03","VC_Hair_Female_04","VC_Hair_Female_05","VC_Hair_Female_06","VC_Hair_Female_07","VC_Hair_Female_08","VC_Hair_Female_09","VC_Hair_Female_10",
     "VC_Hair_Female_11","VC_Hair_Female_12","VC_Hair_Female_13","VC_Hair_Female_14","VC_Hair_Female_15","VC_Hair_Female_16","VC_Hair_Female_17","VC_Hair_Female_18","VC_Hair_Female_19","VC_Hair_Female_20",
     "VC_Hair_Female_21","VC_Hair_Female_22","VC_Hair_Female_23","VC_Hair_Female_24","VC_Hair_Female_25",], #woman_hair_meshes
    [],
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"], #hair textures
    [],
    [
     ("womanface_basic",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("womanface_basic2",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("womanface_old",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("womanface_warrior",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("womanface_warrior2",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("womanface_thin",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("womanface_thin2",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ],#woman_face_textures
    [(voice_die,"snd_woman_die"),(voice_hit,"snd_woman_hit"),(voice_yell,"snd_woman_yell")], #voice sounds
    "skel_human", 0.97,
    psys_game_blood,psys_game_blood_2,
  ),

##  (
##    "undead", 0,
##    "undead_body", "undead_calf_l", "undead_handL",
##    "undead_head", undead_face_keys,
##    [],
##    [],
##    [],
##    [],
##    [("undeadface_a",0xffffffff,[]),
##     ("undeadface_b",0xffcaffc0,[]),
##     ], #undead_face_textures
##    [], #voice sounds
##    "skel_human", 1.0,
##  ),
#hacemos nino como undead
    (
    "undead", 0,
    "empty", "empty", "empty",
    "empty", undead_face_keys,
    [], #man_hair_meshes ,"man_hair_y5","man_hair_y8",
    [], #beard meshes ,"beard_q"
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"], #hair textures
#    ["hair_white"], #hair textures
    [], #beard_materials
    [
     ("manface_basic2",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("manface_thin",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),     
    ], #man_face_textures,
    [(voice_die,"snd_dog_whine"),(voice_hit,"snd_dog_whine"),(voice_grunt,"snd_dog_whine"),(voice_grunt_long,"snd_dog_whine"),(voice_yell,"snd_dog_growl"),(voice_stun,"snd_dog_bark"),(voice_victory,"snd_dog_bark")], #voice sounds
    "skel_human_reduced", 0.6,
    psys_no_blood,psys_no_blood,
    [[1.7, comp_greater_than, (1.0,face_width), (1.0,temple_width)], #constraints: ex: 1.7 > (face_width + temple_width)
     [0.3, comp_less_than, (1.0,face_width), (1.0,temple_width)],
     [1.7, comp_greater_than, (1.0,face_width), (1.0,face_depth)],
     [0.3, comp_less_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [1.7, comp_greater_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [-0.7, comp_less_than, (1.0,nose_size), (-1.0,nose_shape)],
     [0.7, comp_greater_than, (1.0,nose_size), (-1.0,nose_shape)],
     [2.7, comp_greater_than, (1.0,chin_size), (1.0,mouth_nose_distance), (1.0,nose_height), (-1.0,face_width)],
     ]
  ),

]

