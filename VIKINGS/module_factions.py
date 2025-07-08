from header_factions import *

####################################################################################################################
#  Each faction record contains the following fields:
#  1) Faction id: used for referencing factions in other files.
#     The prefix fac_ is automatically added before each faction id.
#  2) Faction name.
#  3) Faction flags. See header_factions.py for a list of available flags
#  4) Faction coherence. Relation between members of this faction.
#  5) Relations. This is a list of relation records.
#     Each relation record is a tuple that contains the following fields:
#    5.1) Faction. Which other faction this relation is referring to
#    5.2) Value: Relation value between the two factions.
#         Values range between -1 and 1.
#  6) Ranks
#  7) Faction color (default is gray)
####################################################################################################################

default_kingdom_relations = [("outlaws",-0.02),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.02),("forest_bandits", -0.02)]
raider_relation = -0.15
factions = [
  ("no_faction","No Faction",0, 0.9, [], []),
  ("commoners","Commoners",0, 0.1,[("player_faction",0.1)], []),
  ("outlaws","Outlaws", max_player_rating(-30), 0.5,[("commoners",-0.6),("player_faction",-0.15),("christians",-0.15),("pagans",-0.15),
                                                     ("kingdom_1", raider_relation),("kingdom_2",  raider_relation),("kingdom_3",  raider_relation),("kingdom_4",  raider_relation),("kingdom_5",  raider_relation),
                                                     ("kingdom_6", raider_relation),("kingdom_7",  raider_relation),("kingdom_8",  raider_relation),("kingdom_9",  raider_relation),("kingdom_10",  raider_relation),
                                                     ("kingdom_11", raider_relation),("kingdom_12",  raider_relation),("kingdom_13",  raider_relation),("kingdom_14",  raider_relation),("kingdom_15",  raider_relation),
                                                     ("kingdom_16", raider_relation),("kingdom_17",  raider_relation),("kingdom_18",  raider_relation),("kingdom_19",  raider_relation),("kingdom_20",  raider_relation),("kingdom_21",  raider_relation)], [], 0x888888),
# Factions before this point are hardwired into the game end their order should not be changed.

  ("neutral","Neutral",0, 0.1,[("player_faction",0.0)], [],0xFFFFFF),
  ("innocents","Innocents", ff_always_hide_label, 0.5,[("outlaws",-0.05)], []),
  ("merchants","Merchants", ff_always_hide_label, 0.5,[("outlaws",-0.5),], []),

  ("dark_knights","{!}Dark Knights", 0, 0.5,[("innocents",-0.9),("player_faction",-0.9)], []), #enemigos de player siempre? para quest.

  ("culture_norse",  "Norse", 0, 0.9, [], []),
  ("culture_saxon",  "Saxon", 0, 0.9, [], []),
  ("culture_angle",  "Angle", 0, 0.9, [], []),
  ("culture_welsh",  "Brittonic", 0, 0.9, [], []),
  ("culture_irish",  "Goidelic", 0, 0.9, [], []),
  ("culture_scotch",  "Pictish", 0, 0.9, [], []),
  ("cultures_end","{!}cultures_end", 0, 0,[], []),

#  ("caza_animales","Animals",0, 0.1,[("player_faction",-0.85)], [],0xFFFFFF),
  ("player_faction","Player Faction",0, 0.9, [], [],0xE12126),  #for relations with player
  ("player_supporters_faction","Player's Supporters",0, 0.9, [("player_faction",1.00),("outlaws",-0.08),("peasant_rebels", -0.1),("deserters", -0.08),("mountain_bandits", -0.08),("forest_bandits", -0.08)], [], 0xE12126),  #for relations with player's kingdom
# Reinos de chief.

  ("kingdom_1", "Kingdom of Danmark",		0, 0.9, [("outlaws",-0.02),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("kingdom_8", 0.9),("kingdom_3", 0.5),("kingdom_2", 0.5),("kingdom_7", -0.9),("kingdom_5", -0.9),("christians",-0.05)], [], 0x800000),
  ("kingdom_2", "Kingdom of Northvegr",		0, 0.9, [("outlaws",-0.02),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("kingdom_8", 0.5),("kingdom_1", 0.5),("kingdom_3", 0.9),("kingdom_20", -0.5),("christians",-0.05)], [], 0x999999),		#was 0xFFD700
  ("kingdom_3", "Kingdom of Laithlind",		0, 0.9, [("outlaws",-0.02),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("kingdom_8", 0.5),("kingdom_1", 0.5),("kingdom_2", 0.9),("christians",-0.05)], [], 0xE24E2B),	#was 0xBBFF00
  ("kingdom_4", "Kingdom of Friese",		0, 0.9, [("outlaws",-0.02),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xFF0088),	#0x3355FF
  ("kingdom_5", "Kingdom of West Seaxe",	0, 0.9, [("outlaws",-0.02),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("kingdom_7", 0.9),("kingdom_1", -0.5),("kingdom_8", -0.9),("kingdom_4", -0.1)], [], 0xFF4F38),	#was 0x008000
  ("kingdom_6", "Kingdom of East Engle",	0, 0.9, [("outlaws",-0.02),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("kingdom_1", -0.5),("kingdom_8", -0.09)], [], 0x303DA8),	#was 0x88CC00
  ("kingdom_7", "Kingdom of Mierce",		0, 0.9, [("outlaws",-0.02),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("kingdom_5", 0.9),("kingdom_1", -0.5),("kingdom_8", -0.9)], [], 0x96ADFF),	#was 0xFF0088
  ("kingdom_8", "Kingdom of Northhymbre",	0, 0.9, [("outlaws",-0.02),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("kingdom_7", -0.9),("kingdom_5", -0.7),("kingdom_3", 0.5),("kingdom_1", 0.9),("kingdom_20", -0.05),("christians",-0.05)], [], 0xFF8899),		#was 0x88FFFF
  ("kingdom_9", "Kingdom of Gwynedd",		0, 0.9, [("outlaws",-0.02),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("kingdom_10", 0.0),("kingdom_12", 0.5),("kingdom_7", -0.5),("kingdom_3", -0.9),("kingdom_5", -0.02)], [], 0x008000),	#was 0xFF8899
  ("kingdom_10", "Kingdom of Brycheiniog",	0, 0.9, [("outlaws",-0.02),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("kingdom_13", -0.9),("kingdom_9", 0.0)], [],  0xFFFF00),
  ("kingdom_11", "Kingdom of Alt Clut",		0, 0.9, [("outlaws",-0.02),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("kingdom_3", -0.9),("kingdom_8", -0.5),("kingdom_9", 0.5),("kingdom_12", 0.5)], [], 0x88CC00),	#was 0xFFDD00
  ("kingdom_12", "Kingdom of Cornubia",		0, 0.9, [("outlaws",-0.02),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("kingdom_5", -0.5)], [], 0x3355FF),
  ("kingdom_13", "Kingdom of Glywyssing",	0, 0.9, [("outlaws",-0.02),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("kingdom_10", -0.9),("kingdom_8", -0.5),("kingdom_12", 0.03),("pagans",-0.05)], [], 0xFF88DD),
  ("kingdom_14", "Kingdom of Uladh",		0, 0.9, [("outlaws",-0.02),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("kingdom_19", -0.5),("kingdom_18", 0.5),("kingdom_3", -0.5)], [], 0xDDDD00),	#was 0xFFDD00 #before it was 0xFF8800
  ("kingdom_15", "Kingdom of Laigin",		0, 0.9, [("outlaws",-0.02),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("kingdom_18", -0.9),("kingdom_16", -0.9),("kingdom_3", -0.5),("kingdom_17", 0.5)], [], 0xE2007C),	#was 0xBB99FF #before it was 0x0000FF
  ("kingdom_16", "Kingdom of Mumain",		0, 0.9, [("outlaws",-0.02),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("kingdom_18", -0.5),("kingdom_15", -0.5),("kingdom_3", -0.5)], [], 0xDDFFCC),
  ("kingdom_17", "Kingdom of Connachta",	0, 0.9, [("outlaws",-0.02),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("kingdom_18", -0.5),("kingdom_3", -0.5)], [], 0x66BBFF),	#was 0xBBFF00 #before it was 0xAA00FF
  ("kingdom_18", "Ui Neill of Aileach", 	0, 0.9, [("outlaws",-0.02),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("kingdom_15", -0.5),("kingdom_17", -0.5),("kingdom_3", -0.5),("kingdom_2", -0.5)], [], 0xDD2244),
  ("kingdom_19", "Kingdom of Mide",			0, 0.9, [("outlaws",-0.02),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("kingdom_14", -0.5),("kingdom_18", 0.5),("kingdom_3", -0.5)], [], 0x3B3EB4),	#was 0xFF00EE
  ("kingdom_20", "Kingdom of Alban",		0, 0.9, [("outlaws",-0.02),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("kingdom_3", -0.9),("kingdom_2", -0.5),("kingdom_8", -0.5),("kingdom_1", -0.5)], [], 0x3333FF),	#was 0xBB99FF
  ("kingdom_21", "Tribe of Osraige",		0, 0.9, [("outlaws",-0.02),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("kingdom_16", -0.5),("kingdom_15", -0.5),("kingdom_19", 0.5)], [], 0xD7A554),	#was 0x66BBFF
  ##chief acaba

  ("kingdoms_end","{!}kingdoms_end", 0, 0,[], []),

  ("robber_knights",  "{!}robber_knights", 0, 0.1, [], []),

  ("khergits","{!}Khergits", 0, 0.5,[("player_faction",0.0)], []),
  ("black_khergits","{!}Black Khergits", 0, 0.5,[("player_faction",-0.3),("kingdom_1",-0.02),("kingdom_2",-0.02)], []),

#  ("neko","Neko", 0, 0.5,[("player_faction",-1.0),("kingdom_5",-0.05),("kingdom_7", -0.1),("kingdom_8", -0.02),("kingdom_6", -0.05),], [], 0x888888), ##puesto con chief
#  ("arrians","Arrians", 0, 0.5,[("player_faction",-1.0)], []), #puesto con chief
#  ("eadfrith","Eadfrith", 0, 0.5,[("player_faction",-1.0)], []), #puesto con chief
  ("christians","Christians", 0, 0.5,[("outlaws",-0.05),("pagans",-0.05),("mountain_bandits", -0.05),("forest_bandits", -0.05)], []),
  ("pagans","Pagans", 0, 0.5,[("outlaws",-0.05),("christians",-0.05),("mountain_bandits", -0.05),("forest_bandits", -0.05)], []),

#cambiado chief
  ("manhunters","Manhunters", 0, 0.5,[("outlaws",-0.6),("player_faction",0.1)], []),
  ("deserters","Deserters", 0, 0.5,[("outlaws",-0.02),("manhunters",-0.6),("commoners",-0.6),("merchants",-0.5),("player_faction",-0.1),("kingdom_1",-0.1),("kingdom_2", -0.1),("kingdom_3", -0.1),("kingdom_4", -0.1),("kingdom_5", -0.1),
                                                     ("kingdom_6",-0.1),("kingdom_7", -0.1),("kingdom_8", -0.1),("kingdom_9", -0.1),("kingdom_10", -0.1),
                                                     ("kingdom_11",-0.1),("kingdom_12", -0.1),("kingdom_13", -0.1),("kingdom_14", -0.1),("kingdom_15", -0.1),
                                                     ("kingdom_16",-0.1),("kingdom_17", -0.1),("kingdom_18", -0.1),("kingdom_19", -0.1),("kingdom_20", -0.1),("kingdom_21", -0.1)], [], 0x888888),
#Ponemos mountain bandit como faccion para scoti, frank and Dena pirates.
  ("mountain_bandits","Sea Warriors", 0, 0.5,[("outlaws",-0.05),("commoners",-0.6),("merchants",-0.5),("manhunters",-0.3),("player_faction",-0.15),("christians",-0.15),("pagans",0.15),
                                                     ("kingdom_1", raider_relation),("kingdom_2",  raider_relation),("kingdom_3",  raider_relation),("kingdom_4",  raider_relation),("kingdom_5",  raider_relation),
                                                     ("kingdom_6", raider_relation),("kingdom_7",  raider_relation),("kingdom_8",  raider_relation),("kingdom_9",  raider_relation),("kingdom_10",  raider_relation),
                                                     ("kingdom_11", raider_relation),("kingdom_12",  raider_relation),("kingdom_13",  raider_relation),("kingdom_14",  raider_relation),("kingdom_15",  raider_relation),
                                                     ("kingdom_16", raider_relation),("kingdom_17",  raider_relation),("kingdom_18",  raider_relation),("kingdom_19",  raider_relation),("kingdom_20",  raider_relation),("kingdom_21",  raider_relation)], [], 0x888888),
  ("forest_bandits","Forest Bandits", 0, 0.5,[("outlaws",-0.05),("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15),("christians",-0.15),("pagans",-0.15),
                                                                                                   ("kingdom_1",-0.05),("kingdom_2", -0.1),("kingdom_3", -0.02),("kingdom_4", -0.05),("kingdom_5", -0.05),
                                                     ("kingdom_6",-0.05),("kingdom_7", -0.1),("kingdom_8", -0.02),("kingdom_9", -0.05),("kingdom_10", -0.05),
                                                     ("kingdom_11",-0.05),("kingdom_12", -0.1),("kingdom_13", -0.02),("kingdom_14", -0.05),("kingdom_15", -0.05),
                                                     ("kingdom_16",-0.05),("kingdom_17", -0.1),("kingdom_18", -0.02),("kingdom_19", -0.05),("kingdom_20", -0.05),("kingdom_21", -0.05)], [], 0x888888),
#cambiado chief acaba
  ("undeads","{!}Undeads", max_player_rating(-30), 0.5,[("commoners",-0.7),("player_faction",-0.5)], []),
  ("slavers","{!}Slavers", 0, 0.1, [], []),
  ("peasant_rebels","{!}Peasant Rebels", 0, 1.0,[("noble_refugees",-1.0),("player_faction",-0.4)], []),
  ("noble_refugees","{!}Noble Refugees", 0, 0.5,[], []),
  ("apoyoplayer","Neutral",0, 0.9,[("player_faction",1.00)], [],0xFFFFFF),
  ("adventurers","Adventurers",0, 0.9, [("player_faction",0.00),("outlaws",-0.5),("peasant_rebels", -0.1),("deserters", -0.3),("mountain_bandits", -0.3),("forest_bandits", -0.3), ("manhunters", 0.1)], [], 0xDDFF00), #changed name so that can tell difference if shows up on map
]
