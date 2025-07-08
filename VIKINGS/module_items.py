from ID_factions import *
from header_items import  *
from header_operations import *
from header_triggers import *

####################################################################################################################
#  Each item record contains the following fields:
#  1) Item id: used for referencing items in other files.
#     The prefix itm_ is automatically added before each item id.
#  2) Item name. Name of item as it'll appear in inventory window
#  3) List of meshes.  Each mesh record is a tuple containing the following fields:
#    3.1) Mesh name.
#    3.2) Modifier bits that this mesh matches.
#     Note that the first mesh record is the default.
#  4) Item flags. See header_items.py for a list of available flags.
#  5) Item capabilities. Used for which animations this item is used with. See header_items.py for a list of available flags.
#  6) Item value.
#  7) Item stats: Bitwise-or of various stats about the item such as:
#      weight, abundance, difficulty, head_armor, body_armor,leg_armor, etc...
#  8) Modifier bits: Modifiers that can be applied to this item.
#  9) [Optional] Triggers: List of simple triggers to be associated with the item.
#  10) [Optional] Factions: List of factions that item can be found as merchandise.
####################################################################################################################

# Some constants for ease of use.
imodbits_none = 0
imodbits_horse_basic = imodbit_swaybacked|imodbit_lame|imodbit_spirited|imodbit_timid|imodbit_stubborn|imodbit_champion#|imodbit_heavy
imodbits_cloth = imodbit_tattered | imodbit_ragged | imodbit_crude | imodbit_sturdy | imodbit_thick
imodbits_leather = imodbits_cloth | imodbit_hardened
imodbits_mail = imodbit_rusty | imodbit_battered | imodbit_thick | imodbit_reinforced 
imodbits_plate = imodbits_mail | imodbit_cracked
imodbits_polearm = imodbit_cracked | imodbit_bent | imodbit_balanced
imodbits_shield = imodbit_cracked | imodbit_battered | imodbit_thick | imodbit_reinforced
imodbits_club = imodbit_cracked | imodbit_crude | imodbit_heavy
imodbits_tool = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_sword = imodbits_tool | imodbit_balanced | imodbit_tempered
imodbits_sword_high = imodbits_sword 
imodbits_axe = imodbits_tool
imodbits_mace = imodbit_rusty | imodbit_crude | imodbit_heavy
imodbits_pick = imodbits_tool | imodbit_balanced
#imodbits_bow = imodbit_cracked | imodbit_bent | imodbit_strong |imodbit_masterwork
imodbits_bow = imodbit_cracked | imodbit_bent | imodbit_strong
imodbits_crossbow = imodbit_cracked | imodbit_bent 
imodbits_missile = imodbit_bent | imodbit_large_bag
imodbits_thrown_minus_heavy = imodbit_bent | imodbit_cracked | imodbit_balanced | imodbit_large_bag
imodbits_thrown = imodbits_thrown_minus_heavy | imodbit_heavy

imodbits_horse_good = imodbit_spirited|imodbit_meek|imodbit_champion|imodbit_heavy
imodbits_good   = imodbit_sturdy | imodbit_thick | imodbit_hardened | imodbit_reinforced
imodbits_bad    = imodbit_rusty | imodbit_chipped | imodbit_tattered | imodbit_ragged | imodbit_cracked | imodbit_bent

norse_fac = [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_8]
frisia_fac = [fac_kingdom_4]
saxon_fac = [fac_kingdom_5]
angle_fac = [fac_kingdom_6, fac_kingdom_7]
briton_fac = [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]
irish_fac = [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]
pict_fac = [fac_kingdom_20]

# Replace winged mace/spiked mace with: Flanged mace / Knobbed mace?
# Fauchard (majowski glaive) 
items = [
# item_name, mesh_name, item_properties, item_capabilities, slot_no, cost, bonus_flags, weapon_flags, scale, view_dir, pos_offset
 ["no_item","INVALID ITEM", [("invalid_item",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],

 ["tutorial_spear", "Spear", [("Spear_S_01",0)], itp_type_polearm| itp_offset_lance|itp_primary|itp_no_blur|itp_wooden_parry, itc_spear|itcf_carry_spear,
380 , weight(2.3)|abundance(100)|difficulty(3)|spd_rtng(95) | weapon_length(113)|swing_damage(16 , blunt) | thrust_damage(28 ,  pierce),imodbits_polearm ],
 ["tutorial_club", "Club", [("wooden_stick",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry|itp_wooden_attack, itc_scimitar, 
12 , weight(2)|difficulty(0)|spd_rtng(95) | weapon_length(80)|swing_damage(12 , blunt) | thrust_damage(0 ,  pierce),imodbits_club ], 
 ["tutorial_battle_axe", "Long Battle Axe", [("Axt02-5",0)], itp_type_two_handed_wpn|itp_primary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry|itp_cant_use_on_horseback|itp_penalty_with_shield, itc_bastardsword|itcf_carry_axe_left_hip, 
 480 , weight(1.75)|difficulty(4)|spd_rtng(85) | weapon_length(81)|swing_damage(31 , cut) | thrust_damage(18 ,  pierce),imodbits_axe],
 ["tutorial_arrows","Arrows", [("arrow",0),("flying_arrow",ixmesh_flying_ammo),("quiver3", ixmesh_carry)], itp_type_arrows|itp_default_ammo, itcf_carry_bowcase_left,
  100,weight(1)|abundance(110)|weapon_length(95)|thrust_damage(1,pierce)|max_ammo(40),imodbits_missile],
 ["tutorial_bolts","Bolts", [("bolt",0),("flying_bolt",ixmesh_flying_ammo),("boltQuiver1", ixmesh_carry),("boltQuiver1", ixmesh_carry|imodbit_large_bag)],  itp_type_bolts|itp_default_ammo|itp_can_penetrate_shield, itcf_carry_bowcase_left,
  164,weight(1.5)|abundance(100)|weapon_length(63)|thrust_damage(2,pierce)|max_ammo(20),imodbits_missile, [], [fac_kingdom_20]], #chief cambiado
 ["tutorial_short_bow", "Long Bow", [("LongBow",0),("LongBow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed|itp_cant_use_on_horseback ,itcf_shoot_bow|itcf_carry_bow_back, 
530 , weight(1)|difficulty(0)|spd_rtng(90) | shoot_speed(55) | thrust_damage(20 ,  pierce)|accuracy(99),imodbits_bow ],
 ["tutorial_crossbow", "Crossbow", [("crossbow",0),], itp_type_crossbow |itp_primary|itp_cant_use_on_horseback|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
250 , weight(2.25)|difficulty(0)|spd_rtng(43) | shoot_speed(65) | thrust_damage(25 ,  pierce)|max_ammo(1)|accuracy(85),imodbits_crossbow],
 ["tutorial_throwing_daggers",  "Javelins", [("javelin",0),("javelin_carry", ixmesh_carry)],  itp_type_thrown |itp_primary|itp_bonus_against_shield ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 
200, weight(1)|difficulty(0)|spd_rtng(90) | shoot_speed(28) | thrust_damage(24 ,  pierce)|max_ammo(4)|weapon_length(65)|accuracy(99),imodbits_thrown ], #chief cambiado max_ammo
 ["tutorial_saddle_horse", "Saddle Pony", [("Horse_01",0),("Horse_01",imodbits_horse_good)], itp_type_horse, 0,
  1700,abundance(50)|hit_points(70)|body_armor(10)|difficulty(0)|horse_speed(40)|horse_maneuver(36)|horse_charge(12)|horse_scale(94),imodbits_horse_basic],
 ["tutorial_shield", "Round Shield", [("Roundshield_01",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  330 , weight(4.5)|hit_points(310)|body_armor(20)|spd_rtng(85)|shield_width(43),imodbits_shield], 

 ["tutorial_staff_no_attack","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_no_blur|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_staff|itcf_carry_spear,
 60 , weight(3.3)|difficulty(0)|spd_rtng(85) | weapon_length(210)|swing_damage(16 , blunt) | thrust_damage(16 ,  blunt),imodbits_polearm ], #cambiado chief
 ["tutorial_staff","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_no_blur|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_staff|itcf_carry_spear,
 60 , weight(3.3)|difficulty(0)|spd_rtng(85) | weapon_length(210)|swing_damage(16 , blunt) | thrust_damage(16 ,  blunt),imodbits_polearm ], #cambiado chief
 ["tutorial_sword", "Common Sword", [("Sword03",0),("Scabbard03", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 790 , weight(1.25)|difficulty(3)|spd_rtng(90) | weapon_length(95)|swing_damage(25 , cut) | thrust_damage(16 ,  pierce),imodbits_sword], 

 ["tutorial_axe", "Axe", [("Axt01-2",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 370 , weight(1)|difficulty(4)|spd_rtng(92) | weapon_length(62)|swing_damage(25 , cut) | thrust_damage(0 ,  pierce),imodbits_axe],

 ["tutorial_dagger","Seax", [("Seax1",0),("Seax1_Scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_blur|itp_no_parry, itc_dagger|itcf_carry_quiver_back_right|itcf_show_holster_when_drawn,
 280 , weight(0.5)|difficulty(0)|spd_rtng(99) | weapon_length(40)|swing_damage(15 , cut) | thrust_damage(25 ,  pierce),imodbits_sword], 

 ["horse_meat","Horse Meat", [("raw_meat",0)], itp_type_goods|itp_consumable|itp_food, 0, 12,weight(40)|food_quality(30)|max_ammo(40),imodbits_none],
# Items before this point are hardwired and their order should not be changed!
#cambiados chief
 ["practice_sword","Common Sword", [("Sword03",0),("Scabbard03", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 790 , weight(1.25)|difficulty(3)|spd_rtng(90) | weapon_length(95)|swing_damage(25 , cut) | thrust_damage(16 ,  pierce),imodbits_sword],
 ["heavy_practice_sword","Goidelic Champion Sword", [("GP_swords04",0),("GP_swords04_Scabbard", ixmesh_carry)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback, itc_greatsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 1030 , weight(2)|difficulty(4)|spd_rtng(85) | weapon_length(105)|swing_damage(45 , cut) | thrust_damage(16 ,  pierce),imodbits_sword], 
 ["practice_dagger","Seax", [("Seax1",0),("Seax1_Scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_blur|itp_no_parry, itc_dagger|itcf_carry_quiver_back_right|itcf_show_holster_when_drawn,
 880 , weight(0.5)|difficulty(0)|spd_rtng(96) | weapon_length(40)|swing_damage(15 , cut) | thrust_damage(25 ,  pierce),imodbits_sword],
 ["practice_axe", "Axe", [("Axt01-2",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 370 , weight(1)|difficulty(4)|spd_rtng(92) | weapon_length(62)|swing_damage(25 , cut) | thrust_damage(0 ,  pierce),imodbits_axe],
 ["arena_axe", "Short Axe", [("Axt01-3",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 370 , weight(1)|difficulty(3)|spd_rtng(94) | weapon_length(52)|swing_damage(23 , cut) | thrust_damage(0 ,  pierce),imodbits_axe],
 ["arena_sword", "Common Sword", [("Sword03",0),("Scabbard03", ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 790 , weight(1.25)|difficulty(3)|spd_rtng(90) | weapon_length(95)|swing_damage(25 , cut) | thrust_damage(16 ,  pierce),imodbits_sword],
 ["arena_sword_two_handed",  "Goidelic Champion Sword", [("GP_swords04",0),("GP_swords04_Scabbard", ixmesh_carry)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback, itc_greatsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 1030 , weight(2)|difficulty(4)|spd_rtng(85) | weapon_length(105)|swing_damage(45 , cut) | thrust_damage(16 ,  pierce),imodbits_sword], 
 ["arena_lance",         "Spear", [("Spear_S_05",0)], itp_type_polearm| itp_offset_lance|itp_primary|itp_no_blur|itp_wooden_parry, itc_spear|itcf_carry_spear,
 380 , weight(2.3)|abundance(100)|difficulty(3)|spd_rtng(95) | weapon_length(121)|swing_damage(16 , blunt) | thrust_damage(28 ,  pierce),imodbits_polearm ],
 ["practice_staff","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_no_blur|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_staff|itcf_carry_spear,
 60 , weight(3.3)|difficulty(0)|spd_rtng(85) | weapon_length(210)|swing_damage(16 , blunt) | thrust_damage(16 ,  blunt),imodbits_polearm ], #cambiado chief
 ["practice_lance", "Spear", [("Spear_S_04",0)], itp_type_polearm| itp_offset_lance|itp_primary|itp_no_blur|itp_wooden_parry, itc_spear|itcf_carry_spear,
 380 , weight(2.3)|abundance(100)|difficulty(3)|spd_rtng(95) | weapon_length(107)|swing_damage(16 , blunt) | thrust_damage(28 ,  pierce),imodbits_polearm ],
["practice_shield","Practice Shield", [("Roundshield_01",0)],  itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  330 , weight(4.5)|hit_points(310)|body_armor(20)|spd_rtng(85)|shield_width(43),imodbits_shield],
 ["practice_bow","Long Bow", [("LongBow",0),("LongBow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 
530 , weight(1)|difficulty(0)|spd_rtng(90) | shoot_speed(50) | thrust_damage(20 ,  pierce)|accuracy(99),imodbits_bow ],
 ["practice_crossbow", "Sling", [("Sling",0)], itp_type_pistol|itp_primary|itp_cant_use_on_horseback, itcf_shoot_pistol, 
250 , weight(0.5)|difficulty(0)|spd_rtng(85) | shoot_speed(55) | thrust_damage(20, blunt)|max_ammo(1)|accuracy(90),0,[],[fac_kingdom_20]], #chief cambiado
 
 ["practice_javelin", "Javelins", [("javelin",0),("javelin_carry", ixmesh_carry)], itp_type_thrown |itp_primary|itp_bonus_against_shield|itp_next_item_as_melee ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 
200, weight(1)|difficulty(0)|spd_rtng(90) | shoot_speed(28) | thrust_damage(24 ,  pierce)|max_ammo(4)|weapon_length(65)|accuracy(99),imodbits_thrown ], #chief cambiado max_ammo
 ["practice_javelin_melee", "Javelin", [("javelin",0)], itp_type_polearm|itp_primary|itp_secondary|itp_wooden_parry , itc_jav_melee, 
200, weight(1)|difficulty(0)|spd_rtng(90) |swing_damage(11, blunt)| thrust_damage(21,  pierce)|weapon_length(65),imodbits_polearm ], #chief cambiado
 ["practice_throwing_daggers", "Javelins", [("javelin",0),("javelin_carry", ixmesh_carry)], itp_type_thrown |itp_primary|itp_bonus_against_shield ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 
200, weight(1)|difficulty(0)|spd_rtng(90) | shoot_speed(28) | thrust_damage(24 ,  pierce)|max_ammo(4)|weapon_length(65)|accuracy(99),imodbits_thrown ], #chief cambiado max_ammo
 ["practice_throwing_daggers_100_amount", "Javelins", [("javelin",0),("javelin_carry", ixmesh_carry)], itp_type_thrown |itp_primary|itp_bonus_against_shield ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 
200, weight(1)|difficulty(0)|spd_rtng(90) | shoot_speed(28) | thrust_damage(24 ,  pierce)|max_ammo(100)|weapon_length(65)|accuracy(99),imodbits_thrown ], #chief cambiado max_ammo
# ["cheap_shirt","Cheap Shirt", [("shirt",0)], itp_type_body_armor|itp_covers_legs, 0, 4,weight(1.25)|body_armor(3),imodbits_none],
 ["practice_horse","Saddle Pony", [("Horse_01",0),("Horse_01",imodbits_horse_good)], itp_type_horse, 0,
  1700,abundance(50)|hit_points(70)|body_armor(10)|difficulty(0)|horse_speed(40)|horse_maneuver(36)|horse_charge(12)|horse_scale(94),imodbits_horse_basic],
 ["practice_arrows","Arrows", [("arrow",0),("flying_arrow",ixmesh_flying_ammo),("quiver3", ixmesh_carry)], itp_type_arrows|itp_default_ammo, itcf_carry_bowcase_left,
  100,weight(1)|abundance(110)|weapon_length(95)|thrust_damage(1,pierce)|max_ammo(40),imodbits_missile],
 ["practice_bolts","Sling Rocks", [("throwing_stone",0),("throwing_stone",ixmesh_flying_ammo)], itp_type_bullets, 0,
  50,weight(0.5)|abundance(100)|weapon_length(3)|thrust_damage(2,blunt)|max_ammo(50),imodbits_missile], #chief cambiado
 ["practice_arrows_10_amount","Arrows", [("arrow",0),("flying_arrow",ixmesh_flying_ammo),("quiver3", ixmesh_carry)],itp_type_arrows|itp_default_ammo, itcf_carry_bowcase_left,
  100,weight(2)|abundance(110)|weapon_length(95)|thrust_damage(1,pierce)|max_ammo(40),imodbits_missile],
 ["practice_arrows_100_amount","Arrows", [("arrow",0),("flying_arrow",ixmesh_flying_ammo),("quiver3", ixmesh_carry)], itp_type_arrows|itp_default_ammo, itcf_carry_bowcase_left,
  100,weight(3)|abundance(110)|weapon_length(95)|thrust_damage(1,pierce)|max_ammo(40),imodbits_missile],
 ["practice_bolts_9_amount","Practice Bolts", [("bolt",0),("flying_bolt",ixmesh_flying_ammo),("boltQuiver1", ixmesh_carry),("boltQuiver1", ixmesh_carry|imodbit_large_bag)], itp_type_bolts|itp_default_ammo|itp_can_penetrate_shield, itcf_carry_bowcase_left,
  164,weight(2)|abundance(100)|weapon_length(63)|thrust_damage(2,pierce)|max_ammo(20),imodbits_missile], #chief cambiado
 ["practice_boots", "Boots", [("Trouser01",0)], itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 190 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(19)|difficulty(0) ,imodbits_cloth ], #cambiado chief
 
 ["red_tourney_armor","Red Tunic", [("Tunic01L_red",0)],  itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 225 , weight(0.4)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth], #cambiado chief
 ["blue_tourney_armor","Blue Tunic", [("Tunic01L_blue",0)],  itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 225 , weight(0.4)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth], #cambiado chief
 ["green_tourney_armor","Green Tunic", [("Tunic01L_green",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 225 , weight(0.4)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth], #cambiado chief
 ["gold_tourney_armor","White Tunic", [("Tunic01L_white",0)],  itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 225 , weight(0.4)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth], #cambiado chief

 ["red_tourney_helmet","Cap",[("Phrygian01-2",0)],itp_type_head_armor|itp_civilian|itp_covers_hair_partially,0,
 100, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth], 
 ["blue_tourney_helmet","Cap",[("Phrygian01-1",0)],itp_type_head_armor|itp_civilian|itp_covers_hair_partially,0,
 100, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth], 
 ["green_tourney_helmet","Cap",[("Phrygian02-1",0)],itp_type_head_armor|itp_civilian|itp_covers_hair_partially,0,
 100, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth], 
 ["gold_tourney_helmet","Cap",[("Phrygian02-2",0)],itp_type_head_armor|itp_civilian|itp_covers_hair_partially,0,
 100, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth], 

["arena_shield_red", "Light Round Shield", [("Basicshield_05",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  300 , weight(2.5)|hit_points(150)|body_armor(15)|spd_rtng(85)|shield_width(43),imodbits_shield],
["arena_shield_blue", "Light Round Shield", [("Basicshield_02",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  300 , weight(2.5)|hit_points(150)|body_armor(15)|spd_rtng(85)|shield_width(43),imodbits_shield],
["arena_shield_green", "Light Round Shield", [("Basicshield_03",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  300 , weight(2.5)|hit_points(150)|body_armor(15)|spd_rtng(85)|shield_width(43),imodbits_shield],
["arena_shield_yellow", "Light Round Shield", [("Basicshield_12",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  300 , weight(2.5)|hit_points(150)|body_armor(15)|spd_rtng(85)|shield_width(43),imodbits_shield],

["arena_armor_white", "White Tunic", [("Tunic01L_white",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 225 , weight(0.4)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth], #cambiado chief
["arena_armor_red", "Red Tunic", [("Tunic01L_red",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 225 , weight(0.4)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth], #cambiado chief
["arena_armor_blue", "Blue Tunic", [("Tunic01L_blue",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 225 , weight(0.4)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth], #cambiado chief
["arena_armor_green", "Green Tunic", [("Tunic01L_green",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 225 , weight(0.4)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth], #cambiado chief
["arena_armor_yellow", "Yellow Tunic", [("Tunic01L_yellow",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 225 , weight(0.4)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth], #cambiado chief
["arena_tunic_white", "White Tunic", [("Tunic01L_white",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 225 , weight(0.4)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth], #cambiado chief
["arena_tunic_red", "Red Tunic", [("Tunic01L_red",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 225 , weight(0.4)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth], #cambiado chief
["arena_tunic_blue", "Blue Tunic", [("Tunic01L_blue",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 225 , weight(0.4)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth], #cambiado chief
["arena_tunic_green", "Green Tunic", [("Tunic01L_green",0)],itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 225 , weight(0.4)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth], #cambiado chief
["arena_tunic_yellow", "Yellow Tunic", [("Tunic01L_yellow",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 225 , weight(0.4)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth], #cambiado chief

#headwear
["arena_helmet_red", "Helm with Nasal", [("Spangenhelm01-1",0)], itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 580 , weight(1.5)|abundance(40)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate], 
["arena_helmet_blue", "Helm with Nasal", [("Spangenhelm01-1",0)], itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 580 , weight(1.5)|abundance(40)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate],
["arena_helmet_green", "Helm with Nasal", [("Spangenhelm01-1",0)], itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 580 , weight(1.5)|abundance(40)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate],
["arena_helmet_yellow", "Helm with Nasal", [("Spangenhelm01-1",0)], itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 580 , weight(1.5)|abundance(40)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate],
["steppe_helmet_white", "Helm with Nasal", [("Spangenhelm01-1",0)], itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 580 , weight(1.5)|abundance(40)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate],
["steppe_helmet_red", "Helm with Nasal", [("Spangenhelm01-1",0)], itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 580 , weight(1.5)|abundance(40)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate],
["steppe_helmet_blue", "Helm with Nasal", [("Spangenhelm01-1",0)], itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 580 , weight(1.5)|abundance(40)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate],
["steppe_helmet_green", "Helm with Nasal", [("Spangenhelm01-1",0)], itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 580 , weight(1.5)|abundance(40)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate],
["steppe_helmet_yellow", "Helm with Nasal", [("Spangenhelm01-1",0)], itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 580 , weight(1.5)|abundance(40)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate],
["tourney_helm_white", "Helm with Nasal", [("Spangenhelm01-1",0)], itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 580 , weight(1.5)|abundance(40)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate],
["tourney_helm_red", "Helm with Nasal", [("Spangenhelm01-1",0)], itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 580 , weight(1.5)|abundance(40)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate],
["tourney_helm_blue", "Helm with Nasal", [("Spangenhelm01-1",0)], itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 580 , weight(1.5)|abundance(40)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate],
["tourney_helm_green", "Helm with Nasal", [("Spangenhelm01-1",0)], itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 580 , weight(1.5)|abundance(40)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate],
["tourney_helm_yellow", "Helm with Nasal", [("Spangenhelm01-1",0)], itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 580 , weight(1.5)|abundance(40)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate],
["arena_turban_red", "Cap",[("Phrygian01-2",0)],itp_type_head_armor|itp_civilian|itp_covers_hair_partially,0,
 100, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["arena_turban_blue", "Cap",[("Phrygian01-1",0)],itp_type_head_armor|itp_civilian|itp_covers_hair_partially,0,
 100, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["arena_turban_green", "Cap",[("Phrygian02-1",0)],itp_type_head_armor|itp_civilian|itp_covers_hair_partially,0,
 100, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["arena_turban_yellow", "Cap",[("Phrygian02-2",0)],itp_type_head_armor|itp_civilian|itp_covers_hair_partially,0,
 100, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
#termina cambiado chief
# A treatise on The Method of Mechanical Theorems Archimedes
#chief cambiados libros 
#This book must be at the beginning of readable books
 ["book_tactics","History of the Peloponnesian War, of Thucydides", [("book_a",0)], itp_type_book, 0, 4000,weight(2)|abundance(100),imodbits_none],
 ["book_persuasion","Rhetorica ad Herennium", [("book_b",0)], itp_type_book, 0, 5000,weight(2)|abundance(100),imodbits_none],
 ["book_leadership","The Life of Alexander the Great", [("book_d",0)], itp_type_book, 0, 4200,weight(2)|abundance(100),imodbits_none], #cambiar chief
 ["book_intelligence","Paedeia", [("book_e",0)], itp_type_book, 0, 2900,weight(2)|abundance(100),imodbits_none],
 ["book_trade","Oeconomica, of Aristotle", [("book_f",0)], itp_type_book, 0, 3100,weight(2)|abundance(100),imodbits_none],
 ["book_weapon_mastery", "Constitution of Sparta, of Xenophon", [("book_d",0)], itp_type_book, 0, 4200,weight(2)|abundance(100),imodbits_none],
 ["book_engineering","De architectura, of Vitrivius", [("book_open",0)], itp_type_book, 0, 4000,weight(2)|abundance(100),imodbits_none],

#Reference books
#This book must be at the beginning of reference books
 ["book_wound_treatment_reference","De Materia Medica, of Dioscorides", [("book_c",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],
 ["book_training_reference","Epitoma Rei Militaris", [("book_open",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],
 ["book_surgery_reference","Synopsis of Aelius Galenus", [("book_c",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],
#chief cambiados libros acaba
#puesto chief mainquest, da persuasion.
 ["relic","The Cathach of Colum Cille", [("book_e",0)], itp_type_book, 0, 5000,weight(2)|abundance(10),imodbits_none],
 #other trade goods (first one is spice)
 ["mead","Mead", [("vc_Mead",0)],						itp_merchandise|itp_type_goods|itp_consumable|itp_food,	0, 350,weight(50)|abundance(100)|food_quality(50)|max_ammo(40),imodbits_none], #  ,[],[fac_kingdom_1]  ???
 ["salt","Salt", [("vc_salt",0)],						itp_merchandise|itp_type_goods,							0, 305,weight(50)|abundance(120),imodbits_none,[],[fac_kingdom_4]],
 ["tar","Tar", [("vc_tar",0)],							itp_merchandise|itp_type_goods,							0, 380,weight(50)|abundance(90),imodbits_none,[],[fac_kingdom_2]],
 ["jewelry","Jewellery", [("vc_jewelry",0)],			itp_merchandise|itp_type_goods|itp_consumable,			0,1000,weight( 5)|abundance(100)|max_ammo(100),imodbits_none,[],[fac_kingdom_4]],
 ["raw_flax","Flax Bundle", [("raw_flax",0)],			itp_merchandise|itp_type_goods,							0, 280,weight(40)|abundance(40),imodbits_none],
 ["linen","Linen", [("vc_linen",0)],					itp_merchandise|itp_type_goods,							0, 365,weight(40)|abundance(40),imodbits_none],
 ["wool","Wool", [("vc_wool",0)],						itp_merchandise|itp_type_goods,							0, 230,weight(40)|abundance(90),imodbits_none],
 ["vc_wool_cloth","Wool Cloth", [("vc_woodenCloth",0)], itp_merchandise|itp_type_goods,							0, 320,weight(40)|abundance(90),imodbits_none,[],[fac_kingdom_4]],
 ["amber","Amber", [("vc_amber",0)],					itp_merchandise|itp_type_goods,							0, 575,weight( 7)|abundance(100),imodbits_none,[],[fac_kingdom_1]],
 ["ivory","Walrus Ivory", [("vc_walrusIvory",0)],		itp_merchandise|itp_type_goods,							0, 400,weight( 7)|abundance(100),imodbits_none,[],[fac_kingdom_2]],
 ["silver","Silver", [("vc_silver",0)],					itp_merchandise|itp_type_goods,							0, 725,weight( 7)|abundance(100),imodbits_none],
 ["iron","Iron", [("vc_silver",0)],						itp_merchandise|itp_type_goods,							0, 304,weight(60)|abundance(50),imodbits_none],
 ["stone","Stone", [("vc_silver",0)],					itp_merchandise|itp_type_goods,							0, 104,weight(60)|abundance(30),imodbits_none],
 ["tools","Tools", [("vc_tools",0)],					itp_merchandise|itp_type_goods,							0, 410,weight(50)|abundance(50),imodbits_none],
 ["vc_raw_leather","Hides", [("vc_bearFur",0)],			itp_merchandise|itp_type_goods,							0, 320,weight(40)|abundance(90),imodbits_none],
 ["timber","Timber", [("vc_wood",0)],					itp_merchandise|itp_type_goods,							0, 300,weight(60)|abundance(90),imodbits_none],
 ["soapstone","Soapstone", [("vc_soapastone",0)],		itp_merchandise|itp_type_goods,							0, 320,weight(40)|abundance(90),imodbits_none], #  ,[],[fac_kingdom_6]  ???
 ["vc_furs","Furs", [("vc_foxFur",0)], 					itp_merchandise|itp_type_goods|itp_consumable,			0, 391,weight(40)|abundance(120)|max_ammo(30),imodbits_none], #  ,[],[fac_kingdom_20]  ???
 ["wine","Wine", [("vc_wine",0)], 						itp_merchandise|itp_type_goods|itp_consumable|itp_food,	0, 780,weight(60)|abundance(100)|food_quality(50)|max_ammo(40),imodbits_none,[],[fac_kingdom_4]],
 ["ale","Ale", [("vc_Ale",0)], 							itp_merchandise|itp_type_goods|itp_consumable|itp_food,	0, 280,weight(60)|abundance(100)|food_quality(50)|max_ammo(50),imodbits_none],
#foods (first one is smoked_fish)
 ["smoked_fish","Smoked Fish", [("vc_smokedFish",0)],	itp_merchandise|itp_type_goods|itp_consumable|itp_food,	0,  90,weight(15)|abundance(110)|food_quality(50)|max_ammo(150),imodbits_none],
 ["cheese","Cheese", [("vc_cheese",0)],					itp_merchandise|itp_type_goods|itp_consumable|itp_food,	0,  85,weight( 6)|abundance(110)|food_quality(50)|max_ammo(90),imodbits_none],
 ["vc_honey","Honey", [("vc_honey",0)],					itp_merchandise|itp_type_goods|itp_consumable|itp_food,	0, 220,weight( 5)|abundance(110)|food_quality(40)|max_ammo(90),imodbits_none],
 ["sausages","Sausages", [("vc_sausages",0)], 			itp_merchandise|itp_type_goods|itp_consumable|itp_food,	0,  35,weight(10)|abundance(110)|food_quality(70)|max_ammo(120),imodbits_none],
 ["cabbages","Vegetables", [("vc_vegies",0)], 			itp_merchandise|itp_type_goods|itp_consumable|itp_food,	0,  40,weight(15)|abundance(110)|food_quality(40)|max_ammo(150),imodbits_none],
 ["dried_meat","Dried Meat", [("vc_dryMeat",0)], 		itp_merchandise|itp_type_goods|itp_consumable|itp_food,	0, 150,weight(15)|abundance(100)|food_quality(60)|max_ammo(150),imodbits_none],
 ["apples","Fruit", [("vc_fruit",0)],					itp_merchandise|itp_type_goods|itp_consumable|itp_food,	0,  40,weight(20)|abundance(110)|food_quality(40)|max_ammo(150),imodbits_none],
 ["barley","Barley", [("vc_barley",0)],					itp_merchandise|itp_type_goods|itp_consumable, 			0,  18,weight(30)|abundance( 60)|food_quality(20)|max_ammo(150),imodbits_none], #x2 for wine
 ["venison","Boar Meat", [("vc_huntedMeat",0)], 		itp_merchandise|itp_type_goods|itp_consumable|itp_food,	0, 110,weight(20)|abundance(100)|food_quality(70)|max_ammo(120),imodbits_none], #x3 for oil
 ["grain","Wheat", [("vc_Wheat",0)],					itp_merchandise|itp_type_goods|itp_consumable, 			0,  20,weight(30)|abundance(110)|food_quality(30)|max_ammo(150),imodbits_none],
 ["cattle_meat","Beef", [("vc_beef",0)],				itp_merchandise|itp_type_goods|itp_consumable|itp_food,	0, 120,weight(20)|abundance(100)|food_quality(80)|max_ammo(150),imodbits_none],
 ["bread","Bread", [("vc_bread",0)],					itp_merchandise|itp_type_goods|itp_consumable|itp_food,	0,  25,weight(15)|abundance(110)|food_quality(40)|max_ammo(150),imodbits_none],
 ["chicken","Chicken", [("vc_chicken",0)],				itp_merchandise|itp_type_goods|itp_consumable|itp_food,	0,  65,weight(10)|abundance(110)|food_quality(40)|max_ammo(150),imodbits_none],
 ["pork","Pork", [("vc_pork",0)],						itp_merchandise|itp_type_goods|itp_consumable|itp_food,	0,  89,weight(15)|abundance(100)|food_quality(70)|max_ammo(150),imodbits_none],
 ["butter","Butter", [("vc_butter",0)],					itp_merchandise|itp_type_goods|itp_consumable|itp_food,	0, 100,weight( 6)|abundance(110)|food_quality(40)|max_ammo(90),imodbits_none],


 #Would like to remove flour altogether and reduce chicken, pork and butter (perishables) to non-trade items. Apples could perhaps become a generic "fruit", also representing dried fruit and grapes
 # Armagan: changed order so that it'll be easier to remove them from trade goods if necessary.
#************************************************************************************************
# ITEMS before this point are hardcoded into item_codes.h and their order should not be changed!
#************************************************************************************************

# Quest Items

 ["siege_supply","Supplies", [("ale_barrel",0)], itp_type_goods, 0, 96,weight(40)|abundance(70),imodbits_none],
 ["quest_wine","Wine", [("amphora_slim",0)], itp_type_goods, 0, 46,weight(40)|abundance(60)|max_ammo(50),imodbits_none],
 ["quest_ale","Ale", [("ale_barrel",0)], itp_type_goods, 0, 31,weight(40)|abundance(70)|max_ammo(50),imodbits_none],

 
####################HORSES chief caballos finales ##############################################################
#############################################################################################################

#horse normal, britons and irish
 ["common_horse","Horse", [("Horse_01",0),("Horse_01",imodbits_horse_good)], itp_merchandise|itp_type_horse, 0,
  6300,abundance(10)|body_armor(16)|hit_points(100)|difficulty(2)|horse_speed(50)|horse_maneuver(40)|horse_charge(18)|horse_scale(100),imodbits_horse_good],
 ["common_horse2","Horse", [("Horse_02",0),("Horse_02",imodbits_horse_good)], itp_merchandise|itp_type_horse, 0,
  6300,abundance(10)|body_armor(16)|hit_points(100)|difficulty(2)|horse_speed(50)|horse_maneuver(40)|horse_charge(18)|horse_scale(100),imodbits_horse_good],
#pony with saddle all factions
["common_pony","Pony", [("Pony_01",0),("Pony_01",imodbits_horse_basic)], itp_merchandise|itp_type_horse, 0,
  3700,abundance(30)|hit_points(90)|body_armor(10)|difficulty(1)|horse_speed(43)|horse_maneuver(36)|horse_charge(12)|horse_scale(94),imodbits_horse_basic],
 ["common_pony2","Pony", [("Pony_02",0),("Pony_02",imodbits_horse_basic)], itp_merchandise|itp_type_horse, 0,
  3700,abundance(30)|hit_points(90)|body_armor(10)|difficulty(1)|horse_speed(43)|horse_maneuver(36)|horse_charge(12)|horse_scale(94),imodbits_horse_basic],
#Wild pony -no saddle- pictish only
 ["wild_horse","Horse", [("Wild_Horse_01",0),("Wild_Horse_01",imodbits_horse_good)], itp_merchandise|itp_type_horse, 0,
  6300,abundance(10)|body_armor(16)|hit_points(100)|difficulty(2)|horse_speed(50)|horse_maneuver(40)|horse_charge(18)|horse_scale(100),imodbits_horse_good, [], [fac_kingdom_20]], #only pictish
 ["wild_horse2","Horse", [("Wild_Horse_02",0),("Wild_Horse_02",imodbits_horse_good)], itp_merchandise|itp_type_horse, 0,
  6300,abundance(10)|body_armor(16)|hit_points(100)|difficulty(2)|horse_speed(50)|horse_maneuver(40)|horse_charge(18)|horse_scale(100),imodbits_horse_good, [], [fac_kingdom_20]], #only pictish
 ["wild_pony","Pony", [("Wild_Pony_01",0),("Wild_Pony_01",imodbits_horse_basic)], itp_merchandise|itp_type_horse, 0,
  3600,abundance(30)|hit_points(95)|body_armor(10)|difficulty(1)|horse_speed(43)|horse_maneuver(31)|horse_charge(12)|horse_scale(93),imodbits_horse_basic, [], [fac_kingdom_20]], #only pictish
 ["wild_pony2","Pony", [("Wild_Pony_02",0),("Wild_Pony_02",imodbits_horse_basic)], itp_merchandise|itp_type_horse, 0,
  3600,abundance(30)|hit_points(95)|body_armor(10)|difficulty(1)|horse_speed(43)|horse_maneuver(31)|horse_charge(12)|horse_scale(93),imodbits_horse_basic, [], [fac_kingdom_20]], #only pictish
#cows alls factions. No vendible
  ["cow1","Cow", [("cow_1",0)], 0, 0,
   1200,abundance(40)|hit_points(60)|body_armor(6)|horse_speed(18)|horse_maneuver(26)|horse_charge(12)|horse_scale(100),imodbits_horse_basic],
  ["cow2","Cow", [("cow_2",0)], 0, 0,
   1200,abundance(40)|hit_points(60)|body_armor(6)|horse_speed(18)|horse_maneuver(26)|horse_charge(12)|horse_scale(100),imodbits_horse_basic],

###################caballos y monturas acaba finales chief####################################
###############################################################

 
##########FELCHAS CHIEF empieza finales #########################
 ####################################################################3
 ["arrows","Arrows", [("arrow",0),("flying_arrow",ixmesh_flying_ammo),("quiver3", ixmesh_carry)], itp_type_arrows|itp_merchandise|itp_default_ammo, itcf_carry_bowcase_left,
  200,weight(1)|abundance(110)|weapon_length(95)|thrust_damage(1,cut)|max_ammo(40),imodbits_missile], #chief cambiado
 ["khergit_arrows","Piercing Arrows", [("arrow2",0),("flying_arrow2",ixmesh_flying_ammo),("quiver2", ixmesh_carry)], itp_type_arrows, itcf_carry_bowcase_left,
  610,weight(1.5)|abundance(10)|weapon_length(95)|thrust_damage(3,cut)|max_ammo(30),imodbits_missile],
#hunting
 ["barbed_arrows","Barbed Arrows", [("barbed_arrow",0),("flying_barbed_arrow",ixmesh_flying_ammo),("quiver1", ixmesh_carry)], itp_type_arrows|itp_merchandise|itp_default_ammo, itcf_carry_bowcase_left,
  400,weight(1)|abundance(60)|weapon_length(95)|thrust_damage(2,cut)|max_ammo(35),imodbits_missile], #chief cambiado
#Bodkin for penetrating chain mail
 ["bodkin_arrows","Bodkin Arrows", [("bodkin_arrow",0),("flying_bodkin_arrow",ixmesh_flying_ammo),("quiver4", ixmesh_carry)], itp_type_arrows|itp_merchandise|itp_default_ammo, itcf_carry_bowcase_left,
  500,weight(1)|abundance(20)|weapon_length(95)|thrust_damage(3,cut)|max_ammo(30),imodbits_missile], #chief cambiado
 #pictish
 ["bolts","Bolts", [("bolt",0),("flying_bolt",ixmesh_flying_ammo),("boltQuiver1", ixmesh_carry),("boltQuiver1", ixmesh_carry|imodbit_large_bag)], itp_type_bolts|itp_merchandise|itp_default_ammo|itp_can_penetrate_shield, itcf_carry_bowcase_left,
  264,weight(1)|abundance(100)|weapon_length(63)|thrust_damage(2,pierce)|max_ammo(40),imodbits_missile, [], [fac_kingdom_20]], #chief cambiado
 ["bolts2","Piercing Bolts", [("bolt2",0),("flying_bolt2",ixmesh_flying_ammo),("boltQuiver2", ixmesh_carry),("boltQuiver2", ixmesh_carry|imodbit_large_bag)], itp_type_bolts|itp_merchandise|itp_default_ammo|itp_can_penetrate_shield, itcf_carry_bowcase_left,
  664,weight(1)|abundance(10)|weapon_length(63)|thrust_damage(5,pierce)|max_ammo(35),imodbits_missile, [], [fac_kingdom_20]], #chief cambiado
 ["bolts3","Barbed Bolts", [("barbed_bolt",0),("flying_barbed_bolt",ixmesh_flying_ammo),("boltQuiver3", ixmesh_carry),("boltQuiver3", ixmesh_carry|imodbit_large_bag)], itp_type_bolts|itp_merchandise|itp_default_ammo|itp_can_penetrate_shield, itcf_carry_bowcase_left,
  464,weight(1)|abundance(60)|weapon_length(63)|thrust_damage(4,pierce)|max_ammo(38),imodbits_missile, [], [fac_kingdom_20]], #chief cambiado
 ["bolts4","Bodkin Bolts", [("bodkin_bolt",0),("flying_bodkin_bolt",ixmesh_flying_ammo),("boltQuiver4", ixmesh_carry),("boltQuiver4", ixmesh_carry|imodbit_large_bag)], itp_type_bolts|itp_merchandise|itp_default_ammo|itp_can_penetrate_shield, itcf_carry_bowcase_left,
  564,weight(1)|abundance(10)|weapon_length(63)|thrust_damage(5,pierce)|max_ammo(35),imodbits_missile, [], [fac_kingdom_20]], #chief cambiado

#################flechas chief finales acaba############################333
 ##################################################################


####OTROSSSSSSS##############
 ["pilgrim_disguise", "Pilgrim Disguise", [("MonkTunic7",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_replaces_helm|itp_covers_hair,0,
 133 , weight(4.5)|abundance(100)|head_armor(6)|body_armor(15)|leg_armor(12)|difficulty(0) ,imodbits_cloth ], #chief cambiado
 ["pilgrim_hood", "Pilgrim Hood", [("Phrygian_basic01_black",0)], 0| itp_type_head_armor |itp_civilian|itp_covers_hair_partially  ,0,
  35 , weight(1.25)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ], #cambiado chief

# ARMOR 
#handwear

##########Guantes empieza chief #################################
["leather_gloves","Leather Gloves", [("leather_gloves_L",0)], itp_merchandise|itp_type_hand_armor,0,
 90, weight(0.25)|abundance(50)|body_armor(6)|difficulty(0),imodbits_leather],

##################Guantes acaba chief ###############################

###################Calzado botas empieza chief finales ###############################
###############################################################
######Calzado############
###Notas: irlandeses y pictos solo bare.
 
####VC Calzado#########
#class baja
["carbatinae_1", "Leather Shoes", [("Trouser01",0)],  itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 180 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth ], #cambiado chief
["carbatinae_2", "Wrapping Boots", [("Trouser05",0)],  itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 375 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(23)|difficulty(0) ,imodbits_cloth ], #cambiado chief
["carbatinae_3", "Leather Shoes", [("Trouser08",0)], itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 180 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth ], #cambiado chief
["carbatinae_4", "Leather Shoes", [("Trouser11",0)], itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 170 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth ], #cambiado chief
["carbatinae_5", "Wrapping Boots", [("Trouser15",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 365 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(23)|difficulty(0) ,imodbits_cloth ], #cambiado chief
["carbatinae_6", "Leather Shoes", [("Trouser21",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 190 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth ], #cambiado chief
["carbatinae_7", "Wrapping Boots", [("Trouser25",0)], itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 385 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(23)|difficulty(0) ,imodbits_cloth ], #cambiado chief
["carbatinae_8", "Leather Shoes", [("Trouser31",0)], itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 165 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth ], #cambiado chief
["carbatinae_9", "Wrapping Boots", [("Trouser35",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 355 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(23)|difficulty(0) ,imodbits_cloth ], #cambiado chief
["carbatinae_10", "Leather Shoes", [("Trouser38",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 160 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth ], #cambiado chief

["carbatinae_vc1", "Ankle Boots", [("Trouser02",0)], itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 220 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(19)|difficulty(0) ,imodbits_cloth ], #cambiado chief
["carbatinae_vc2", "Ankle Boots", [("Trouser12",0)], itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 210 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(19)|difficulty(0) ,imodbits_cloth ], #cambiado chief
["carbatinae_vc3", "Ankle Boots", [("Trouser14",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 210 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(19)|difficulty(0) ,imodbits_cloth ], #cambiado chief
["carbatinae_vc4", "Quality Wrapping Boots", [("Trouser20",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 445 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(24)|difficulty(0) ,imodbits_cloth ], #cambiado chief
["carbatinae_vc5", "Ankle Boots", [("Trouser22",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 230 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(19)|difficulty(0) ,imodbits_cloth ], #cambiado chief
["carbatinae_vc6", "Ankle Boots", [("Trouser32",0)], itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 190 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(19)|difficulty(0) ,imodbits_cloth ], #cambiado chief
#saxons, britons
["carbatinae_1s", "Leather Shoes", [("Trouser03",0)],itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 180 , weight(2)|abundance(40)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth,
  [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons

["carbatinae_2s", "Wrapping Boots", [("Trouser07",0)],itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 375 , weight(2)|abundance(40)|head_armor(0)|body_armor(0)|leg_armor(23)|difficulty(0) ,imodbits_cloth,
  [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons

["carbatinae_3s", "Wrapping Boots", [("Trouser16",0)],itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 365 , weight(2)|abundance(40)|head_armor(0)|body_armor(0)|leg_armor(23)|difficulty(0) ,imodbits_cloth,
  [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
["carbatinae_4s", "Rawhide Shoes", [("Trouser23",0)], itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 195 , weight(2)|abundance(40)|head_armor(0)|body_armor(0)|leg_armor(17)|difficulty(0) ,imodbits_cloth,
  [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
["carbatinae_5s", "Rawhide Shoes", [("Trouser33",0)], itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 175 , weight(2)|abundance(40)|head_armor(0)|body_armor(0)|leg_armor(17)|difficulty(0) ,imodbits_cloth,
  [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
["carbatinae_6s", "Ankle Boots", [("Trouser36",0)],itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 190 , weight(2)|abundance(40)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_cloth,
  [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons

["carbatinae_vc1s", "Quality Wrapping Boots", [("Trouser27",0)],itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 475 , weight(1.5)|abundance(40)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_cloth,
  [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
["carbatinae_vc2s", "Ankle Boots", [("Trouser34",0)], itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 190 , weight(1.5)|abundance(40)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_cloth,
  [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
 ["carbatinae_vc3s", "Quality Wrapping Boots", [("Trouser37",0)],itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 425 , weight(1.5)|abundance(40)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_cloth,
  [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
["carbatinae_vc4s", "Wrapping Boots", [("Trouser40",0)],  itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 345 , weight(1.5)|abundance(40)|head_armor(0)|body_armor(0)|leg_armor(23)|difficulty(0) ,imodbits_cloth,
  [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
#vikings
["carbatinae_1v", "Ankle Boots", [("Trouser04",0)], itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 220 , weight(2)|abundance(40)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_cloth,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["carbatinae_2v", "Wrapping Boots", [("Trouser06",0)],itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 375 , weight(2)|abundance(40)|head_armor(0)|body_armor(0)|leg_armor(23)|difficulty(0) ,imodbits_cloth,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["carbatinae_3v", "Wrapping Boots", [("Trouser10",0)], itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 375 , weight(2)|abundance(40)|head_armor(0)|body_armor(0)|leg_armor(23)|difficulty(0) ,imodbits_cloth,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
 ["carbatinae_4v", "Quality Wrapping Boots", [("Trouser17",0)],itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 445 , weight(2)|abundance(40)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_cloth,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["carbatinae_5v", "Rawhide Shoes", [("Trouser13",0)], itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 180 , weight(2)|abundance(40)|head_armor(0)|body_armor(0)|leg_armor(17)|difficulty(0) ,imodbits_cloth,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["carbatinae_6v", "Wrapping Boots", [("Trouser26",0)], itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 385 , weight(2)|abundance(40)|head_armor(0)|body_armor(0)|leg_armor(23)|difficulty(0) ,imodbits_cloth,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria

["carbatinae_vc1v", "Ankle Boots", [("Trouser24",0)],   itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 230 , weight(1.5)|abundance(40)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_cloth,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["carbatinae_vc2v", "Quality Wrapping Boots", [("Trouser30",0)],   itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 475 , weight(1.5)|abundance(40)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_cloth,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria

#clase alta
["carbatinae_11q", "Leather Shoes", [("Trouser18",0)], itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 170 , weight(2)|abundance(20)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth ], #cambiado chief
["carbatinae_12q", "Leather Shoes", [("Trouser28",0)], itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 190 , weight(2)|abundance(20)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth ], #cambiado chief

#saxons, britons
["carbatinae_11qs", "Quality Wrapping Boots", [("Trouser09",0)], itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 465 , weight(2)|abundance(20)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons

["carbatinae_12qs", "Quality Wrapping Boots", [("Trouser29",0)], itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 475 , weight(2)|abundance(20)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_cloth,
  [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons

["carbatinae_13qs", "Quality Wrapping Boots", [("Trouser39",0)], itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 425 , weight(2)|abundance(20)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_cloth,
  [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons


["carbatinae_14qs", "Quality Wrapping Boots", [("Trouser40",0)],  itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 405 , weight(1.5)|abundance(20)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_cloth,
  [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons

#vikings
["carbatinae_14qv", "Quality Wrapping Boots", [("Trouser19",0)],  itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 445 , weight(2)|abundance(20)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_cloth ], #cambiado chief
#no shoes, descalzo totalmente #No tocar moto fixed bare legs issue
 ["bare_foot_man", "Cheap Shoes", [("Legs08",0)],  itp_merchandise|itp_type_foot_armor|itp_civilian|itp_attach_armature, 0, 
 125, weight(0.5)|abundance(50)|head_armor(0)|body_armor(0)|leg_armor(13)|difficulty(0) ,imodbits_cloth], #cambiado chief 
###Clase baja Irlandeses y pictish
#bare legs, piernas desnudas
 ["just_man_boots_medium", "Rawhide Shoes", [("Legs03",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 165 , weight(0.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth,
  [], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops

["just_man_boots_light", "Light Ankle Boots", [("Legs04",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 150 , weight(0.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(18)|difficulty(0) ,imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops

["just_man_shoes", "Leather Shoes", [("Legs01",0)],  itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 150 , weight(0.5)|abundance(80)|head_armor(0)|body_armor(0)|leg_armor(15)|difficulty(0) ,imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
#clase alta
 ["just_man_boots_dark", "Light Ankle Boots", [("Legs02",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 265 , weight(0.5)|abundance(80)|head_armor(0)|body_armor(0)|leg_armor(18)|difficulty(0) ,imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
##### no tocar acaba
###irlandeses
 #elite
 ["gaelshoes_1", "Goidelic Shoes", [("GaelicTrouser01",0)],  itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 150 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(15)|difficulty(0) ,imodbits_cloth, 
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
["gaelshoes_2", "Goidelic Shoes", [("GaelicTrouser02",0)],  itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 150 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(15)|difficulty(0) ,imodbits_cloth, 
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
["gaelshoes_3", "Goidelic Boots", [("Legs06",0)], itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 300 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(19)|difficulty(0) ,imodbits_cloth, 
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
##["gaelshoes_3", "Goidelic Shoes", [("GaelicTrouser03",0)], itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
## 300 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_cloth, 
##[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
##["gaelshoes_4", "Goidelic Shoes", [("GaelicTrouser04",0)], itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
## 300 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_cloth, 
##[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
###basic
##["gaelshoes_5", "Goidelic Trousers", [("GaelicTrouser_black",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
## 170 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(17)|difficulty(0) ,imodbits_cloth, 
##[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
##["gaelshoes_6", "Goidelic Trousers", [("GaelicTrouser_blue",0)], itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 
## 170 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(17)|difficulty(0) ,imodbits_cloth, 
##[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
##["gaelshoes_7", "Goidelic Trousers", [("GaelicTrouser_green",0)], itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
## 170 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(17)|difficulty(0) ,imodbits_cloth, 
##[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
##["gaelshoes_8", "Goidelic Trousers", [("GaelicTrouser_orange",0)], itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
## 170 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(17)|difficulty(0) ,imodbits_cloth, 
##[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
##["gaelshoes_9", "Goidelic Trousers", [("GaelicTrouser_purple",0)], itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, #elite color
## 170 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(17)|difficulty(0) ,imodbits_cloth, 
##[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
##["gaelshoes_10", "Goidelic Trousers", [("GaelicTrouser_red",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
## 170 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(17)|difficulty(0) ,imodbits_cloth, 
##[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
## ["gaelshoes_11", "Goidelic Trousers", [("GaelicTrouser_white",0)],  itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
## 170 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(17)|difficulty(0) ,imodbits_cloth, 
##[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
##["gaelshoes_12", "Goidelic Trousers", [("GaelicTrouser_yellow",0)],  itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
## 170 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(17)|difficulty(0) ,imodbits_cloth, 
##[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
####women shoes
 #normal
 ["womenshoes_1", "Simple Shoes", [("Legs_female01",0)],  itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 150 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(15)|difficulty(0) ,imodbits_cloth ],
["womenshoes_2", "Simple Ankle Boots", [("Legs_female02",0)],  itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
300 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(18)|difficulty(0) ,imodbits_cloth ],
["womenshoes_3", "Simple Shoes", [("Legs_female03",0)],itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
150 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(15)|difficulty(0) ,imodbits_cloth ],
["womenshoes_4", "Simple Ankle Boots", [("Legs_female04",0)], itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 300 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(18)|difficulty(0) ,imodbits_cloth ],
#total bare legs #no tocar Moto fixed bare legs issue
["womenshoes_5", "Simple Boots", [("Legs_female05",0)], itp_type_foot_armor|itp_civilian|itp_attach_armature, 0, 
300, weight(1)|abundance(20)|head_armor(0)|body_armor(0)|leg_armor(22)|difficulty(0) ,imodbits_cloth], #cambiado chief
#gael and pictish
["womenshoes_6", "Simple Ankle Boots", [("Legs_female_gael01",0)], itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 300 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(18)|difficulty(0) ,imodbits_cloth ],
["womenshoes_7", "Simple Shoes", [("Legs_female_gael02",0)], itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 150 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(15)|difficulty(0) ,imodbits_cloth ],
#bare
["womenshoes_8", "Simple Shoes", [("Legs_female06",0)], itp_type_foot_armor|itp_civilian|itp_attach_armature, 0, 
130, weight(1)|abundance(50)|head_armor(0)|body_armor(0)|leg_armor(13)|difficulty(0) ,imodbits_cloth], #cambiado chief
 

####Calzado acaba chief finales ###############################################
######################################################################

######ROPA chief##########################################################

####tunicas largas finales ##############
 ###########################################

#########eliminar cuando tengamos las largas
#long

 #no long tunics in VC using for others
 ["long_tunic1", "Frisian Light Armor", [("Tunic_Frisian_04B",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 800 , weight(1.3)|abundance(40)|head_armor(0)|body_armor(21)|leg_armor(8), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
#saxon
 ["nobleman_outfit", "Saxon Light Armor", [("Tunic_Saxon_01C",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 600 , weight(1.1)|abundance(40)|head_armor(0)|body_armor(18)|leg_armor(6), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
##
##troll tunic
["troll_tunic", "Troll's Tunic", [("Tunic_Saxon_01C",0)], itp_unique  |itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 560 , weight(1)|abundance(10)|head_armor(70)|body_armor(85)|leg_armor(64), imodbits_cloth ,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_10, fac_kingdom_11]],

####sacerdotes
["priest1", "Priest Robe", [("PriestTunicNormal",0)], itp_type_body_armor  |itp_covers_legs ,0,
 350 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(19)|leg_armor(16)|difficulty(0) ,imodbits_cloth ], #chief cambiado
["priest2", "Priest Robe", [("PriestTunicDalmatic",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 350 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(19)|leg_armor(16)|difficulty(0) ,imodbits_cloth ], #chief cambiado

["robe", "Monk Robe", [("MonkTunic1",0)], itp_type_body_armor  |itp_covers_legs|itp_replaces_helm|itp_covers_hair,0,
 350 , weight(1.5)|abundance(1)|head_armor(12)|body_armor(19)|leg_armor(16)|difficulty(0) ,imodbits_cloth ], #chief cambiado
["robe2", "Monk Robe", [("MonkTunic2",0)], itp_type_body_armor  |itp_covers_legs ,0,
 350 , weight(1.5)|abundance(1)|head_armor(12)|body_armor(19)|leg_armor(16)|difficulty(0) ,imodbits_cloth ], #chief cambiado
["robe3", "Monk Robe", [("MonkTunic3",0)], itp_type_body_armor  |itp_covers_legs|itp_replaces_helm|itp_covers_hair,0,
 350 , weight(1.5)|abundance(1)|head_armor(12)|body_armor(19)|leg_armor(16)|difficulty(0) ,imodbits_cloth ], #chief cambiado
["robe4", "Monk Robe", [("MonkTunic4",0)], itp_type_body_armor  |itp_covers_legs ,0,
 350 , weight(1.5)|abundance(1)|head_armor(12)|body_armor(19)|leg_armor(16)|difficulty(0) ,imodbits_cloth ], #chief cambiado
["robe5", "Monk Robe", [("MonkTunic5",0)], itp_type_body_armor  |itp_covers_legs|itp_replaces_helm|itp_covers_hair,0,
 350 , weight(1.5)|abundance(1)|head_armor(12)|body_armor(19)|leg_armor(16)|difficulty(0) ,imodbits_cloth ], #chief cambiado
#pagan
["robe6", "Monk Robe", [("MonkTunic6",0)], itp_type_body_armor  |itp_covers_legs ,0,
 350 , weight(1.5)|abundance(1)|head_armor(12)|body_armor(19)|leg_armor(16)|difficulty(0) ,imodbits_cloth ], #chief cambiado
["robe7", "Monk Robe", [("MonkTunic7",0)], itp_type_body_armor  |itp_covers_legs|itp_replaces_helm|itp_covers_hair,0,
 350 , weight(1.5)|abundance(1)|head_armor(12)|body_armor(19)|leg_armor(16)|difficulty(0) ,imodbits_cloth ], #chief cambiado
#
["robe8", "Monk Robe", [("MonkTunic8",0)], itp_type_body_armor  |itp_covers_legs ,0,
 350 , weight(1.5)|abundance(100)|head_armor(12)|body_armor(19)|leg_armor(16)|difficulty(0) ,imodbits_cloth ], #chief cambiado
##healers tunics
["robe9", "Monk Robe", [("MonkTunic9",0)], itp_type_body_armor  |itp_covers_legs|itp_replaces_helm|itp_covers_hair,0,
 350 , weight(1.5)|abundance(100)|head_armor(12)|body_armor(19)|leg_armor(16)|difficulty(0) ,imodbits_cloth ], #chief cambiado
["robe10", "Monk Robe", [("MonkTunic10",0)], itp_type_body_armor  |itp_covers_legs ,0,
 350 , weight(1.5)|abundance(100)|head_armor(12)|body_armor(19)|leg_armor(16)|difficulty(0) ,imodbits_cloth ], #chief cambiado
###########
 
#####tunicas largas acaba chief##############
###########################################

##########tunicas cortas finales################
 #############################################
################################
#Angles
#basic...
 ["ptunic_1", "Simple Angle Tunic", [("Tunic_Angle_11",0)],  itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 270 , weight(0.5)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
 ["ptunic_2", "Angle Light Armor", [("Tunic_Angle_03B",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 1200 , weight(1.6)|abundance(100)|head_armor(0)|body_armor(26)|leg_armor(10), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
 ["ptunic_3", "Angle Tunic", [("Tunic_Angle_01B",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 330 , weight(0.5)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
 ["ptunic_4", "Angle Tunic", [("Tunic_Angle_06",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 450 , weight(0.6)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
 ["ptunic_5", "Simple Angle Tunic", [("Tunic_Angle_07",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 270 , weight(0.4)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
#rich
 ["ptunic_6", "Angle Tunic", [("Tunic_Angle_01",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 330 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
 ["ptunic_7", "Padded Angle Tunic", [("Tunic_Angle_02",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 375 , weight(0.6)|abundance(40)|head_armor(0)|body_armor(14)|leg_armor(5), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
 ["ptunic_8", "Padded Angle Tunic", [("Tunic_Angle_02B",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 375 , weight(0.6)|abundance(40)|head_armor(0)|body_armor(14)|leg_armor(5), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
 ["ptunic_9", "Angle Light Armor", [("Tunic_Angle_03",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 1200 , weight(1.6)|abundance(40)|head_armor(0)|body_armor(26)|leg_armor(10), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
 ["ptunic_10", "Angle Tunic", [("Tunic_Angle_04",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 300 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
 ["ptunic_11", "Angle Tunic", [("Tunic_Angle_05",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 330 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(14)|leg_armor(4), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
 ["ptunic_12", "Angle Light Armor", [("Tunic_Angle_02C",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 800 , weight(1.2)|abundance(40)|head_armor(0)|body_armor(20)|leg_armor(7), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
####################################################
#######################################################
#####Vikings ###...

###cortas basicas, clase baja vikings
 ["btunic_1", "Cloak", [("Cloak_Norse_01",0)],  itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 270 , weight(0.4)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(4), imodbits_cloth,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
 ["btunic_2", "Trousers", [("Bare_Norse_01",0)],  itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 150 , weight(0.4)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(4), imodbits_cloth,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
 ["btunic_3", "Norse Tunic", [("Tunic_Norse_08",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 330 , weight(0.5)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(6), imodbits_cloth,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
 ["btunic_4", "Norse Tunic", [("Tunic_Norse_09",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 300 , weight(0.5)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(4), imodbits_cloth,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
 ["btunic_5", "Norse Tunic", [("Tunic_Norse_10",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 375 , weight(0.6)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(4), imodbits_cloth,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
 ["btunic_6", "Norse Tunic", [("Tunic_Norse_11",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 270 , weight(0.5)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
 ["btunic_7", "Norse Tunic", [("Tunic_Norse_12",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 450 , weight(0.5)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria

 ["btunic_8", "Simple Norse Tunic", [("Tunic_Norse_05",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 300 , weight(0.5)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(4), imodbits_cloth,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
 ["btunic_9", "Simple Norse Tunic", [("Tunic_Norse_07",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 270 , weight(0.5)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
 ["btunic_10", "Simple Norse Tunic", [("Tunic_Norse_02",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 300 , weight(0.5)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(4), imodbits_cloth,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria

#clase media guerrera vikings
 ["btunic_11", "Norse Tunic", [("Tunic_Norse_01",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 450 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
 ["btunic_12", "Norse Light Armor", [("Tunic_Norse_01B",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 600 , weight(1.0)|abundance(40)|head_armor(0)|body_armor(18)|leg_armor(7), imodbits_cloth,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
 ["btunic_13", "Norse Tunic", [("Tunic_Norse_04",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 300 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
 ["btunic_14", "Norse Tunic", [("Tunic_Norse_06",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 450 , weight(0.6)|abundance(40)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
##clase alta vikings
 ["btunic_15", "Norse Light Armor", [("Tunic_Norse_03",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 800 , weight(1.3)|abundance(20)|head_armor(0)|body_armor(21)|leg_armor(8), imodbits_cloth,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
 ["btunic_16", "Norse Light Armor", [("Tunic_Norse_03B",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 1000 , weight(1.6)|abundance(20)|head_armor(0)|body_armor(24)|leg_armor(9), imodbits_cloth,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
###########################
####################################################### ...

##Generic tunics
["hoodtunic_01", "Tunic", [("Tunic_01",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 300 , weight(0.4)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth], #cambiado chief
["hoodtunic_02", "Tunic", [("Tunic_02",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 300 , weight(0.4)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth], #cambiado chief
["hoodtunic_03", "Tunic", [("Tunic_03",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 330 , weight(0.4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(4), imodbits_cloth], #cambiado chief
["hoodtunic_04", "Tunic", [("Tunic_04",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 330 , weight(0.4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(4), imodbits_cloth], #cambiado chief
["hoodtunic_05", "Tunic", [("Tunic_05",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 450 , weight(0.4)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth], #cambiado chief
["hoodtunic_06", "Tunic", [("Tunic_06",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 450 , weight(0.4)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth], #cambiado chief
["hoodtunic_07", "Tunic", [("Tunic_07",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 270 , weight(0.4)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth], #cambiado chief

###################################################
 #######SAXONS ###
###clase media sajones y anglos S son libres para addon
["hoodtunic_08", "Cloak", [("Cloak_Saxon_01",0)],  itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 270 , weight(0.4)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(4), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
 ["bl_tunic01", "Trousers", [("Bare_Saxon_01",0)],  itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 150 , weight(0.5)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(4), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
 ["bl_tunic02", "Saxon Light Armor", [("Tunic_Saxon_02C",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 800 , weight(1.2)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(7), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
 ["bl_tunic03", "Saxon Light Armor", [("Tunic_Saxon_03B",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 1200 , weight(1.6)|abundance(100)|head_armor(0)|body_armor(26)|leg_armor(10), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
 ["bl_tunic04", "Simple Saxon Tunic", [("Tunic_Saxon_06",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 450 , weight(0.6)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
 ["bl_tunic05", "Simple Saxon Tunic", [("Tunic_Saxon_07",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 270 , weight(0.5)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
#medium class
 ["bl_tunic06", "Saxon Tunic", [("Tunic_Saxon_05",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 300 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(14)|leg_armor(4), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
 ["bl_tunic07", "Saxon Tunic", [("Tunic_Saxon_04",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 300 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
["bl_tunic08", "Padded Saxon Tunic", [("Tunic_Saxon_02B",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 375 , weight(0.6)|abundance(40)|head_armor(0)|body_armor(14)|leg_armor(5), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
["bl_tunic09", "Saxon Light Armor", [("Tunic_Saxon_03",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 1200 , weight(1.6)|abundance(40)|head_armor(0)|body_armor(26)|leg_armor(10), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
["bl_tunic10", "Saxon Tunic", [("Tunic_Saxon_02",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 375 , weight(0.6)|abundance(40)|head_armor(0)|body_armor(14)|leg_armor(5), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
["bl_tunic11", "Saxon Tunic", [("Tunic_Saxon_01B",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 330 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
["bl_tunic12", "Saxon Tunic", [("Tunic_Saxon_01",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 330 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
["red_cloak", "Saxon Tunic", [("Tunic_Saxon_08",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 450 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
###########
########################################
 #Differents cultures
# tunics with cloaks
 #...
 ["yellow_cloak", "Elite Frisian Tunic", [("Tunic_Frisian_13",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 450 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(13)|leg_armor(6), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
# pictish armor
 ["green_cloak", "Pictish Light Armor", [("Tunic_Picts_04B",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0,
 1000 , weight(1.5)|abundance(20)|head_armor(0)|body_armor(24)|leg_armor(9), imodbits_cloth,
[], [fac_kingdom_20]], #pictish shops
#britons
["blue_cloak", "Tunic", [("Tunic_Briton_03",0)],itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 375 , weight(0.6)|abundance(20)|head_armor(0)|body_armor(16)|leg_armor(4), imodbits_cloth,
 [], [fac_kingdom_9]],  
["leather_cloak", "Tunic", [("Tunic_Briton_03C",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 375 , weight(0.6)|abundance(20)|head_armor(0)|body_armor(16)|leg_armor(4), imodbits_cloth,
 [], [fac_kingdom_9]],  
#
 ["yellow2_cloak", "Simple Angle Tunic", [("Tunic_Angle_09",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 300 , weight(0.5)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(4), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
#
####################################
###britons tunics
#basic
["briton_tunic1", "Cloak", [("Cloak_Briton_01",0)],  itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 300 , weight(0.5)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(4), imodbits_cloth,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #britons
 ["briton_tunic2", "Trousers", [("Bare_Briton_01",0)],  itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 150 , weight(0.4)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(4), imodbits_cloth,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #britons
 ["briton_tunic3", "Briton Tunic", [("Tunic_briton_04",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 300 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #britons
 ["briton_tunic4", "Simple Briton Tunic", [("Tunic_briton_05",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 300 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #britons
 ["briton_tunic5", "Simple Briton Tunic", [("Tunic_briton_06",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 300 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #britons
 ["briton_tunic6", "Simple Briton Tunic", [("Tunic_briton_07",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 300 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #britons
 ["briton_tunic7", "Briton Tunic", [("Tunic_Briton_03B",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 375 , weight(0.6)|abundance(20)|head_armor(0)|body_armor(16)|leg_armor(4), imodbits_cloth,
 [], [fac_kingdom_9]],
 ["briton_tunic8", "Briton Light Armor", [("Tunic_briton_09",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 1000 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(9), imodbits_cloth,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #britons
 ["briton_tunic9", "Briton Tunic", [("Tunic_Briton_02C",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 330 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(14)|leg_armor(5), imodbits_cloth,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #britons
#elite
 ["briton_tunic10", "Briton Tunic", [("Tunic_Briton_01",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 330 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #britons
 ["briton_tunic11", "Briton Tunic", [("Tunic_Briton_02",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 330 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(14)|leg_armor(5), imodbits_cloth,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #britons
 ["briton_tunic12", "Briton Tunic", [("Tunic_Briton_02B",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 330 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(14)|leg_armor(5), imodbits_cloth,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #britons
 ["briton_tunic13", "Briton Tunic", [("Tunic_Briton_02D",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 330 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(14)|leg_armor(5), imodbits_cloth,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #britons
 ["briton_tunic14", "Briton Tunic", [("Tunic_Briton_01C",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 375 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(14)|leg_armor(4), imodbits_cloth,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #britons
#####################################


################
 #Pictish 1 tunics
 ["briton_tunic15", "Pictish Tunic", [("Tunic_Picts_01",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 300 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_20]], #pictish shops
 ["briton_tunic16", "Pictish Tunic", [("Tunic_Picts_01D",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 300 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_20]], #pictish shops
 ["briton_tunic17", "Pictish Tunic", [("Tunic_Picts_02",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 300 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_20]], #pictish shops
 ["briton_tunic18", "Pictish Tunic", [("Tunic_Picts_02D",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 300 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_20]], #pictish shops
 ["briton_tunic19", "Pictish Light Armor", [("Tunic_Picts_04",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 1000 , weight(1.5)|abundance(40)|head_armor(0)|body_armor(24)|leg_armor(9), imodbits_cloth,
[], [fac_kingdom_20]], #pictish shops
########################

#irish
 #hoods
 ["briton_tunic20", "Goidelic Hooded Tunic", [("Hood_Irish_01",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 270 , weight(0.5)|abundance(20)|head_armor(0)|body_armor(12)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish shops
 ["briton_tunic21", "Goidelic Hooded Tunic", [("Hood_Irish_02",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian|itp_replaces_helm|itp_covers_hair ,0,
 225 , weight(0.5)|abundance(20)|head_armor(8)|body_armor(10)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish shops
 ["briton_tunic22", "Goidelic Hooded Tunic", [("Hood_Irish_03",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 225 , weight(0.5)|abundance(20)|head_armor(0)|body_armor(10)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish shops
 ["briton_tunic23", "Goidelic Hooded Tunic", [("Hood_Irish_04",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian|itp_replaces_helm|itp_covers_hair ,0,
 225 , weight(0.5)|abundance(20)|head_armor(8)|body_armor(10)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish shops

 #elite
 ["briton_tunic24", "Goidelic Tunic", [("Tunic_Irish_05",0)],  itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 450 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish shops
  ["briton_tunic25", "Goidelic Tunic", [("Tunic_Irish_01",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 300 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish shops
 ["briton_tunic26", "Goidelic Tunic", [("Tunic_Irish_01D",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 300 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish shops
 ["briton_tunic27", "Goidelic Tunic", [("Tunic_Irish_02",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 300 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish shops
 ["briton_tunic28", "Goidelic Tunic", [("Tunic_Irish_02D",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 300 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish shops

#basic
 ["celta_capa1", "Goidelic Tunic", [("Tunic_Irish_06",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0,
 450 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish shops
 ["celta_capa2", "Goidelic Long Cloak", [("Tunic_Irish_01B",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0,
 300 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish shops
 ["celta_capa3", "Goidelic Trousers", [("Bare_Irish_01",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 150 , weight(0.4)|abundance(20)|head_armor(0)|body_armor(8)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish shops
["celta_capa4", "Goidelic Trousers", [("Bare_Irish_02",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 150 , weight(0.4)|abundance(20)|head_armor(0)|body_armor(8)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish shops
#elite
 ["brat1", "Goidelic Rich Cloak", [("Cloak_Irish_01",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 270 , weight(0.4)|abundance(20)|head_armor(0)|body_armor(10)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish shops
 ["brat2", "Goidelic Rich Cloak", [("Cloak_Irish_02",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 300 , weight(0.5)|abundance(20)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish shops
 ["brat3", "Goidelic Light Armor", [("Tunic_Irish_04",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 880 , weight(1.3)|abundance(20)|head_armor(0)|body_armor(21)|leg_armor(8), imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish shops
 ["brat4", "Goidelic Light Armor", [("Tunic_Irish_04B",0)],itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 880 , weight(1.3)|abundance(20)|head_armor(0)|body_armor(21)|leg_armor(8), imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish shops

###tunic only for irish
#square big, pictish
 ["gael_tunic_01", "Pictish Tunic", [("Tunic_Picts_05",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0,
 450 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish shops
["gael_tunic_02", "Pictish Tunic", [("Tunic_Picts_06",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0,
 450 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish shops
#Angles...
["gael_tunic_03", "Angle Tunic", [("Tunic_Angle_08",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 300 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
["gael_tunic_04", "Angle Tunic", [("Tunic_Angle_10",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 375 , weight(0.6)|abundance(40)|head_armor(0)|body_armor(16)|leg_armor(4), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
####
 
#with cloak irish
["gael_tunic_05", "Cloaked Goidelic Tunic", [("Tunic_Irish_01C",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0,
 330 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(14)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish shops
 ["gael_tunic_06", "Cloaked Goidelic Tunic", [("Tunic_Irish_02C",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0,
 330 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(14)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish shops
["gael_tunic_07", "Goidelic Tunic", [("Tunic_Irish_02B",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0,
 300 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish shops


#tuncis with hood for irish 
["gael_tunic_08", "Hooded Goidelic Tunic", [("Tunic_Irish_03",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian|itp_replaces_helm|itp_covers_hair ,0,
 330 , weight(0.5)|abundance(40)|head_armor(8)|body_armor(14)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish shops
 ["gael_hoodtunic_09", "Hooded Goidelic Tunic", [("Tunic_Irish_03B",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian|itp_replaces_helm|itp_covers_hair ,0,
 330 , weight(0.5)|abundance(40)|head_armor(8)|body_armor(14)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish shops
["gael_hoodtunic_10", "Hooded Goidelic Tunic", [("Tunic_Irish_03C",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0,
 330 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(14)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish shops
["gael_hoodtunic_11", "Hooded Goidelic Tunic", [("Tunic_Irish_03D",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0,
 330 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(14)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish shops
["gael_hoodtunic_12", "Hooded Goidelic Light Armor", [("Tunic_Irish_04C",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian|itp_replaces_helm|itp_covers_hair ,0,
 880 , weight(1.3)|abundance(20)|head_armor(10)|body_armor(21)|leg_armor(8), imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish shops

#small square, pictish
["picts_tunic_09", "Norse Trousers", [("Bare_01",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0,
 150 , weight(0.4)|abundance(40)|head_armor(0)|body_armor(8)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4]], #norse
["picts_tunic_10", "Norse Trousers", [("Bare_02",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0,
 150 , weight(0.4)|abundance(40)|head_armor(0)|body_armor(8)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4]], #norse
#...
["picts_tunic_11", "Norse Cloak", [("Cloak_Norse_02",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0,
 270 , weight(0.4)|abundance(40)|head_armor(0)|body_armor(10)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4]], #norse
#
#...
["picts_tunic_12", "Briton Light Armor", [("Tunic_briton_08",0)],itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 1000 , weight(1.5)|abundance(20)|head_armor(0)|body_armor(24)|leg_armor(9), imodbits_cloth,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], 
["picts_tunic_13", "Briton Tunic", [("Tunic_Briton_01B",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 330 , weight(0.5)|abundance(20)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], 
["picts_tunic_14", "Trousers", [("Bare_03",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 150 , weight(0.4)|abundance(20)|head_armor(0)|body_armor(8)|leg_armor(4), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
["picts_tunic_15", "Trousers", [("Bare_04",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 150 , weight(0.4)|abundance(20)|head_armor(0)|body_armor(8)|leg_armor(4), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
["picts_tunic_16", "Frisian Trousers", [("Bare_Frisian_01",0)],  itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 150 , weight(0.4)|abundance(20)|head_armor(0)|body_armor(8)|leg_armor(4), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
#
###########################

###################################
 #pictish
#### #ritual equipament no merchandise no lootable
["pictish_painted1", "Pictish Naked", [("Bare_Picts_01",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0,
  150 , weight(0.3)|abundance(40)|head_armor(0)|body_armor(8)|leg_armor(4), imodbits_cloth ],
["pictish_painted2", "Pictish Naked", [("Bare_Picts_02",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0,
  150 , weight(0.3)|abundance(40)|head_armor(0)|body_armor(8)|leg_armor(4), imodbits_cloth ],
["pictish_painted3", "Pictish Naked", [("Bare_Picts_03",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0,
  150 , weight(0.3)|abundance(40)|head_armor(0)|body_armor(8)|leg_armor(4), imodbits_cloth ],
["pictish_painted4", "Pictish Naked", [("Bare_Picts_04",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0,
  150 , weight(0.3)|abundance(40)|head_armor(0)|body_armor(8)|leg_armor(4), imodbits_cloth ],
["picts_hoodtunic_01", "Pictish Cloak", [("Cloak_Picts_01",0)],  itp_unique|itp_type_body_armor  |itp_covers_legs ,0,
  270 , weight(0.4)|abundance(40)|head_armor(0)|body_armor(10)|leg_armor(4), imodbits_cloth ],
 ["picts_hoodtunic_02", "Pictish Cloak", [("Cloak_Picts_02",0)],  itp_unique|itp_type_body_armor  |itp_covers_legs ,0,
  300 , weight(0.4)|abundance(40)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],

# hoods and naked body only pictish
["picts_hoodtunic_03", "Pictish Hood", [("Hood_Picts_01",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0,
 225 , weight(0.4)|abundance(20)|head_armor(0)|body_armor(10)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_20]], #pictish shops
["picts_hoodtunic_04", "Pictish Hood", [("Hood_Picts_02",0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian|itp_replaces_helm|itp_covers_hair ,0,
 225 , weight(0.5)|abundance(20)|head_armor(8)|body_armor(10)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_20]], #pictish shops
["picts_hoodtunic_05", "Pictish Hood", [("Hood_Picts_03",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0,
 225 , weight(0.4)|abundance(20)|head_armor(0)|body_armor(10)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_20]], #pictish shops
["picts_hoodtunic_06", "Pictish Hood", [("Hood_Picts_04",0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian|itp_replaces_helm|itp_covers_hair ,0,
 270 , weight(0.5)|abundance(20)|head_armor(10)|body_armor(12)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_20]], #pictish shops
["picts_hoodtunic_07", "Pictish Hood", [("Tunic_Picts_01C",0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0,
 300 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_20]], #pictish shops

#tunics with cloaks
["picts_hoodtunic_11", "Cloaked Pictish Tunic", [("Tunic_Picts_02C",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0,
 330 , weight(0.7)|abundance(40)|head_armor(0)|body_armor(14)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_20]], #pictish shops
["picts_hoodtunic_12", "Cloaked Pictish Tunic", [("Tunic_Picts_01C",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0,
 330 , weight(0.7)|abundance(40)|head_armor(0)|body_armor(14)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_20]], #pictish shops
["picts_hoodtunic_13", "Cloaked Pictish Tunic", [("Tunic_Picts_02B",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0,
 300 , weight(0.7)|abundance(40)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_20]], #pictish shops

#tuncis with hood for pictish
["picts_hoodtunic_14", "Hooded Pictish Tunic", [("Tunic_Picts_03",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian|itp_replaces_helm|itp_covers_hair ,0,
 375 , weight(0.8)|abundance(40)|head_armor(10)|body_armor(16)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_20]], #pictish shops
["picts_hoodtunic_15", "Hooded Pictish Tunic", [("Tunic_Picts_03B",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian|itp_replaces_helm|itp_covers_hair ,0,
 330 , weight(0.8)|abundance(40)|head_armor(8)|body_armor(14)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_20]], #pictish shops
["picts_hoodtunic_16", "Hooded Pictish Tunic", [("Tunic_Picts_03C",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0,
 330 , weight(0.7)|abundance(40)|head_armor(0)|body_armor(14)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_20]], #pictish shops
["picts_hoodtunic_17", "Hooded Pictish Tunic", [("Tunic_Picts_03D",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0,
 330 , weight(0.7)|abundance(40)|head_armor(0)|body_armor(14)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_20]], #pictish shops
 ["picts_hoodtunic_18", "Pictish Light Armor", [("Tunic_Picts_04C",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0,
 1200 , weight(1.6)|abundance(20)|head_armor(0)|body_armor(26)|leg_armor(9), imodbits_cloth,
[], [fac_kingdom_20]], #pictish shops
###############


####especiales
["linen_tunic", "Pictish Tunic", [("Tunic_Picts_01B",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0,
 330 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(14)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_20]], #pictish shops
#tunicas cortas finales acaba###############
 ############################################

######vestuario mujeres chief ###
#anglo saxon women
 #basic
["woman_saxon1", "Saxon Dress", [("female_dress_anglosaxon3_black",0)],  itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 383 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(20)|difficulty(0) ,imodbits_cloth ], #cambiado chief 
["woman_saxon2", "Saxon Dress", [("female_dress_anglosaxon1_black",0)],  itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 383 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(20)|difficulty(0) ,imodbits_cloth ], #cambiado chief 
["woman_saxon3", "Saxon Dress", [("female_dress_anglosaxon1_white",0)],  itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 383 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(20)|difficulty(0) ,imodbits_cloth ], #cambiado chief 
["woman_saxon4", "Saxon Dress", [("female_dress_anglosaxon1_yellow",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 383 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(20)|difficulty(0) ,imodbits_cloth ], #cambiado chief 
["woman_saxon5", "Saxon Dress", [("female_dress_anglosaxon3_blue",0)],  itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 383 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(20)|difficulty(0) ,imodbits_cloth ], #cambiado chief 
["woman_saxon6", "Saxon Dress", [("female_dress_anglosaxon3_green",0)],  itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 383 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(20)|difficulty(0) ,imodbits_cloth ], #cambiado chief 
["woman_saxon7", "Saxon Dress", [("female_dress_anglosaxon3_orange",0)],  itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 383 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(20)|difficulty(0) ,imodbits_cloth ], #cambiado chief 
["woman_saxon8", "Saxon Dress", [("female_dress_anglosaxon3_purple",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 383 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(20)|difficulty(0) ,imodbits_cloth ], #cambiado chief 
["woman_saxon9", "Saxon Dress", [("female_dress_anglosaxon3_red",0)],  itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 383 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(20)|difficulty(0) ,imodbits_cloth ], #cambiado chief 
["woman_saxon10", "Saxon Dress", [("female_dress_anglosaxon3_white",0)],  itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 383 , weight(1.5)|abundance(20)|head_armor(0)|body_armor(20)|leg_armor(20)|difficulty(0) ,imodbits_cloth ], #cambiado chief 
["woman_saxon11", "Saxon Dress", [("female_dress_anglosaxon3_yellow",0)],  itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 383 , weight(1.5)|abundance(20)|head_armor(0)|body_armor(20)|leg_armor(20)|difficulty(0) ,imodbits_cloth ], #cambiado chief 
 #rich
["richwoman_saxon1", "Rich Saxon Dress", [("female_dress_anglosaxon1_purple",0)],  itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 423 , weight(1.7)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(22)|difficulty(0) ,imodbits_cloth ], #cambiado chief 
["richwoman_saxon2", "Rich Saxon Dress", [("female_dress_anglosaxon1_red",0)],  itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 423 , weight(1.7)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(22)|difficulty(0) ,imodbits_cloth ], #cambiado chief 
["richwoman_saxon3", "Rich Saxon Dress", [("female_dress_anglosaxon2",0)],  itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 423 , weight(1.7)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(22)|difficulty(0) ,imodbits_cloth ], #cambiado chief 
["richwoman_saxon4", "Rich Saxon Dress", [("female_dress_anglosaxon3",0)],  itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 423 , weight(1.7)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(22)|difficulty(0) ,imodbits_cloth ], #cambiado chief
["richwoman_saxon5", "Rich Saxon Dress", [("female_dress_anglosaxon1_orange",0)],  itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 423 , weight(1.7)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(22)|difficulty(0) ,imodbits_cloth ], #cambiado chief 
["richwoman_saxon6", "Rich Saxon Dress", [("female_dress_anglosaxon1_purple",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 423 , weight(1.7)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(22)|difficulty(0) ,imodbits_cloth ], #cambiado chief 
["richwoman_saxon7", "Rich Saxon Dress", [("female_dress_anglosaxon1_blue",0)],  itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 423 , weight(1.7)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(22)|difficulty(0) ,imodbits_cloth ], #cambiado chief 
["richwoman_saxon8", "Rich Saxon Dress", [("female_dress_anglosaxon1_green",0)],  itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 423 , weight(1.7)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(22)|difficulty(0) ,imodbits_cloth ], #cambiado chief 
["richwoman_saxon9", "Rich Saxon Dress", [("female_dress_anglosaxon1",0)],  itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 423 , weight(1.7)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(22)|difficulty(0) ,imodbits_cloth ], #cambiado chief 
 
["queenwoman_saxon", "Royal Saxon Dress", [("female_dress_anglosaxon4",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 423 , weight(1.7)|head_armor(0)|body_armor(22)|leg_armor(22)|difficulty(0) ,imodbits_cloth ], #cambiado chief 
##
#gael and pictish dress
#rich
["queenpict_long_tunic", "Rich Dress", [("female_dress_picts2",0)],itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 403 , weight(1.4)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(22), imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
["pict_richlong_tunic1", "Rich Dress", [("female_dress_picts1",0)],itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 403 , weight(1.4)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(22), imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
["pict_richlong_tunic2", "Rich Dress", [("female_dress_picts1_purple",0)],itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 403 , weight(1.4)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(22), imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
["pict_richlong_tunic3", "Rich Dress", [("female_dress_picts1_blue",0)],itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 403 , weight(1.4)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(22), imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops

#basic
["pict_long_tunic1", "Dress", [("female_dress_picts1_black",0)],itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 363 , weight(1.4)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(20), imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
["pict_long_tunic2", "Dress", [("female_dress_picts1_green",0)],itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 363 , weight(1.4)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(20), imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
["pict_long_tunic3", "Dress", [("female_dress_picts1_orange",0)],itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 363 , weight(1.4)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(20), imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
["pict_long_tunic4", "Dress", [("female_dress_picts1_red",0)],itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 363 , weight(1.4)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(20), imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
["pict_long_tunic5", "Dress", [("female_dress_picts1_white",0)],itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 363 , weight(1.4)|abundance(20)|head_armor(0)|body_armor(18)|leg_armor(20), imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
["pict_long_tunic6", "Dress", [("female_dress_picts1_yellow",0)],itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 363 , weight(1.4)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(20), imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops

##norse
["woman_norse1", "Norse Dress", [("female_dress_scandinavian1_black",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 383 , weight(1.5)|abundance(20)|head_armor(0)|body_armor(20)|leg_armor(20)|difficulty(0) ,imodbits_cloth ], #cambiado chief 
["woman_norse2", "Norse Dress", [("female_dress_scandinavian1_blue",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 383 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(20)|difficulty(0) ,imodbits_cloth ], #cambiado chief 
["woman_norse3", "Norse Dress", [("female_dress_scandinavian1_green",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 383 , weight(1.5)|abundance(20)|head_armor(0)|body_armor(20)|leg_armor(20)|difficulty(0) ,imodbits_cloth ], #cambiado chief 
["woman_norse4", "Norse Dress", [("female_dress_scandinavian1_orange",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 383 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(20)|difficulty(0) ,imodbits_cloth ], #cambiado chief 
["woman_norse5", "Norse Dress", [("female_dress_scandinavian1_white",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 383 , weight(1.5)|abundance(20)|head_armor(0)|body_armor(20)|leg_armor(20)|difficulty(0) ,imodbits_cloth ], #cambiado chief 
["woman_norse6", "Norse Dress", [("female_dress_scandinavian1_yellow",0)],  itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 383 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(20)|difficulty(0) ,imodbits_cloth ], #cambiado chief 
##rich
["richwoman_norse1", "Rich Norse Dress", [("female_dress_scandinavian2",0)],  itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 423 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(22)|difficulty(0) ,imodbits_cloth ], #cambiado chief 
["richwoman_norse2", "Rich Norse Dress", [("female_dress_scandinavian1",0)],  itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 423 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(22)|difficulty(0) ,imodbits_cloth ], #cambiado chief 
["richwoman_norse3", "Rich Norse Dress", [("female_dress_scandinavian1_purple",0)],  itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 423 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(22)|difficulty(0) ,imodbits_cloth ], #cambiado chief 
["richwoman_norse4", "Rich Norse Dress", [("female_dress_scandinavian1_red",0)],  itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 423 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(22)|difficulty(0) ,imodbits_cloth ], #cambiado chief 
 
##tunicas GENERIC
#common
["btunic_1woman", "Tunic", [("Tunic_08",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 270 , weight(0.5)|abundance(20)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth ],
#angle...
 ["btunic_2woman", "Angle Light Armor", [("Tunic_Angle_01C",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 600 , weight(1.1)|abundance(40)|head_armor(0)|body_armor(18)|leg_armor(6), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
#frisian... 
 ["btunic_3woman", "Frisian Tunic", [("Tunic_Frisian_09",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 330 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(13)|leg_armor(6), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
 ["btunic_4woman", "Frisian Tunic", [("Tunic_Frisian_10",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 300 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(14)|leg_armor(4), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
 ["btunic_5woman", "Frisian Tunic", [("Tunic_Frisian_11",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 375 , weight(0.6)|abundance(40)|head_armor(0)|body_armor(16)|leg_armor(4), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
 ["btunic_6woman", "Frisian Tunic", [("Tunic_Frisian_12",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 300 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(12)|leg_armor(6), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
#angle...
 ["btunic_7woman", "Angle Tunic", [("Tunic_Angle_12",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 450 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
#
##poor basic
 ["btunic_8woman", "Simple Tunic", [("Tunic_BanditL_yellow",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 225 , weight(0.4)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth], #cambiado chief
  ["ptunic_1woman", "Simple Tunic", [("Tunic_BanditL_black",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 225 , weight(0.4)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth], #cambiado chief
 ["ptunic_2woman", "Simple Tunic", [("Tunic_BanditL_blue",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 225 , weight(0.4)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth], #cambiado chief
 ["ptunic_3woman", "Simple Tunic", [("Tunic_BanditL_green",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 225 , weight(0.4)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth], #cambiado chief
 ["ptunic_4woman", "Simple Tunic", [("Tunic_BanditL_orange",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 225 , weight(0.4)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth], #cambiado chief
 ["ptunic_5woman", "Simple Tunic", [("Tunic_BanditL_purple",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 225 , weight(0.4)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth], #cambiado chief
 ["ptunic_6woman", "Simple Tunic", [("Tunic_BanditL_red",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 225 , weight(0.4)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth], #cambiado chief
 ["ptunic_7woman", "Simple Tunic", [("Tunic_BanditL_white",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 225 , weight(0.4)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth], #cambiado chief
#####
#Frisian...
   ["gaeltunic_1woman", "Frisian Tunic", [("Tunic_Frisian_01",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 330 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
 ["gaeltunic_2woman", "Frisian Tunic", [("Tunic_Frisian_02",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 300 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(14)|leg_armor(4), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
 ["gaeltunic_3woman", "Frisian Tunic", [("Tunic_Frisian_03",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 375 , weight(0.6)|abundance(40)|head_armor(0)|body_armor(16)|leg_armor(4), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
 ["gaeltunic_4woman", "Frisian Light Armor", [("Tunic_Frisian_04",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 800 , weight(1.3)|abundance(40)|head_armor(0)|body_armor(21)|leg_armor(8), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
 ["gaeltunic_5woman", "Frisian Tunic", [("Tunic_Frisian_05",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 300 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
 ["gaeltunic_6woman", "Frisian Tunic", [("Tunic_Frisian_06",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 300 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(14)|leg_armor(4), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
 ["gaeltunic_7woman", "Frisian Tunic", [("Tunic_Frisian_07",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 450 , weight(0.6)|abundance(40)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
 ["gaeltunic_8woman", "Frisian Tunic", [("Tunic_Frisian_08",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 270 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(13)|leg_armor(4), imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons 
###
 
#Berserkers skins
 ["britontunic_1woman", "Bear Skin", [("Berserkr01",0)], itp_type_body_armor|itp_force_show_body|itp_covers_legs|itp_civilian ,0,
 1350 , weight(2.9)|abundance(40)|head_armor(13)|body_armor(31)|leg_armor(9), imodbits_cloth], #cambiado chief
 ["britontunic_2woman", "Bear Skin", [("Berserkr02",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0,
 1500 , weight(3.0)|abundance(40)|head_armor(13)|body_armor(31)|leg_armor(10), imodbits_cloth], #britons
 ["britontunic_3woman", "Bear Skin", [("Berserkr03",0)], itp_type_body_armor|itp_force_show_body|itp_covers_legs|itp_civilian ,0,
 1350 , weight(2.9)|abundance(40)|head_armor(13)|body_armor(31)|leg_armor(9), imodbits_cloth], #cambiado chief
 ["britontunic_4woman", "Bear Skin", [("Berserkr04",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0,
 1500 , weight(3.0)|abundance(40)|head_armor(13)|body_armor(31)|leg_armor(10), imodbits_cloth], #britons
 ["britontunic_5woman", "Wolf Skin", [("Berserkr05",0)], itp_type_body_armor|itp_force_show_body |itp_covers_legs|itp_civilian ,0,
 1125 , weight(2.4)|abundance(40)|head_armor(12)|body_armor(29)|leg_armor(8), imodbits_cloth], #britons
 ["britontunic_6woman", "Wolf Skin", [("Berserkr06",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0,
 1350 , weight(2.9)|abundance(40)|head_armor(12)|body_armor(31)|leg_armor(9), imodbits_cloth], #cambiado chief
 ["britontunic_7woman", "Wolf Skin", [("Berserkr07",0)], itp_type_body_armor|itp_force_show_body |itp_covers_legs|itp_civilian ,0,
 1125 , weight(2.4)|abundance(40)|head_armor(12)|body_armor(29)|leg_armor(8), imodbits_cloth], #britons
 ["britontunic_8woman", "Wolf Skin", [("Berserkr08",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0,
 1350 , weight(2.9)|abundance(40)|head_armor(12)|body_armor(31)|leg_armor(9), imodbits_cloth], #cambiado chief
###

#todas las razas, veils para cabezas 
 #### PROVISIONAL BELOW

#common everybody
["veil_a", "Veil", [("Hood01c",0)],  itp_type_head_armor  |itp_civilian|itp_covers_hair_partially  ,0, 100 , weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["veil_b", "Veil", [("Hood01c_blue",0)],  itp_type_head_armor | itp_civilian|itp_covers_hair_partially  ,0, 100 , weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["veil_c", "Veil", [("Hood01c_orange",0)],  itp_type_head_armor | itp_civilian|itp_covers_hair_partially  ,0, 100 , weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["veil_d", "Veil", [("Hood01c_black",0)], itp_merchandise| itp_type_head_armor  |itp_civilian|itp_covers_hair_partially  ,0, 100 , weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["veil_e", "Veil", [("Hood01c_green",0)], itp_merchandise| itp_type_head_armor  |itp_civilian|itp_covers_hair_partially  ,0, 100 , weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["veil_f", "Veil", [("Hood01c_yellow",0)],  itp_type_head_armor  |itp_civilian|itp_covers_hair_partially  ,0, 100 , weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

#rich everybody
["elite_veil_1", "Rich Veil", [("Hood01a",0)],  itp_type_head_armor  |itp_civilian|itp_covers_hair_partially  ,0, 200 , weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["elite_veil_2", "Rich Veil", [("Hood01b",0)],  itp_type_head_armor  |itp_civilian|itp_covers_hair_partially  ,0, 200 , weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["elite_veil_3", "Rich Veil", [("Hood01c_purple",0)],  itp_type_head_armor  |itp_civilian|itp_covers_hair_partially  ,0, 200 , weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["elite_veil_4", "Rich Veil", [("Hood01c_red",0)],  itp_type_head_armor  |itp_civilian|itp_covers_hair_partially  ,0, 200 , weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

#saxon common
["common_veil_a", "Veil", [("Hood02c_orange",0)],  itp_type_head_armor  |itp_civilian  ,0, 100 , weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["common_veil_b", "Veil", [("Hood02c",0)],  itp_type_head_armor  |itp_civilian  ,0, 100 , weight(0.5)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["common_veil_c", "Veil", [("Hood02c_black",0)],  itp_type_head_armor  |itp_civilian  ,0, 100 , weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["common_veil_d", "Veil", [("Hood02c_blue",0)],  itp_type_head_armor  |itp_civilian  ,0, 100 , weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["common_veil_e", "Veil", [("Hood02c_green",0)], itp_type_head_armor  |itp_civilian  ,0, 100 , weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["common_veil_f", "Veil", [("Hood02c_orange",0)], itp_type_head_armor  |itp_civilian  ,0, 100 , weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
 
#saxon rich
["elite_veil_5", "Rich Veil", [("Hood02a",0)],  itp_type_head_armor  |itp_civilian  ,0, 200 , weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["elite_veil_6", "Rich Veil", [("Hood02b",0)],  itp_type_head_armor  |itp_civilian  ,0, 200 , weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["elite_veil_7", "Rich Veil", [("Hood02c_red",0)],  itp_type_head_armor  |itp_civilian  ,0, 200 , weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["elite_veil_8", "Rich Veil", [("Hood02c_purple",0)],  itp_type_head_armor  |itp_civilian  ,0, 200 , weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

####mujeres ropa acaba############
##########


##############ROPA acaba chief #############################################################
###################ARMADURAS MEDIAS CHIEF finales###########################################

#gambeson de lino, cubre torso, cualquier faccion
#gambeson corto
["gambeson1", "Saxon Gambeson", [("Gamb_Saxon_07",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1760 , weight(5.3)|abundance(40)|head_armor(0)|body_armor(31)|leg_armor(13)|difficulty(6) ,imodbits_cloth,
 [], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #saxons
["gambeson2", "Saxon Gambeson", [("Gamb_Saxon_06",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1600 , weight(5)|abundance(40)|head_armor(0)|body_armor(32)|leg_armor(12)|difficulty(6) ,imodbits_cloth,
 [], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #saxons
["gambeson3", "Saxon Gambeson", [("Gamb_Saxon_08",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1760 , weight(5)|abundance(40)|head_armor(0)|body_armor(31)|leg_armor(11)|difficulty(6) ,imodbits_cloth,
 [], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #saxons
["gambeson4", "Norse Gambeson", [("Gamb_Norse_12",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1200 , weight(4)|abundance(40)|head_armor(0)|body_armor(29)|leg_armor(11)|difficulty(6) ,imodbits_cloth,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4, fac_kingdom_8]], #norse
["gambeson5", "Norse Gambeson", [("Gamb_Norse_06",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1440 , weight(4)|abundance(40)|head_armor(0)|body_armor(29)|leg_armor(11)|difficulty(6) ,imodbits_cloth,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4, fac_kingdom_8]], #norse
["gambeson6", "Saxon Gambeson", [("Gamb_Saxon_02",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1440 , weight(4)|abundance(40)|head_armor(0)|body_armor(29)|leg_armor(11)|difficulty(6) ,imodbits_cloth,
 [], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #saxons
["gambeson7", "Saxon Gambeson", [("Gamb_Saxon_03",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 2000 , weight(5.6)|abundance(40)|head_armor(0)|body_armor(35)|leg_armor(13)|difficulty(6) ,imodbits_cloth,
 [], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #saxons
["gambeson8", "Norse Gambeson", [("Gamb_Norse_07",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1600 , weight(5)|abundance(40)|head_armor(0)|body_armor(31)|leg_armor(11)|difficulty(6) ,imodbits_cloth,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4, fac_kingdom_8]], #norse
["gambeson9", "Saxon Gambeson", [("Gamb_Saxon_04",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 2000 , weight(5)|abundance(40)|head_armor(0)|body_armor(32)|leg_armor(11)|difficulty(6) ,imodbits_cloth,
 [], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #saxons
["gambeson10", "Angle Gambeson", [("Gamb_Angle_01",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, #purple
 1600 , weight(4.8)|abundance(40)|head_armor(0)|body_armor(32)|leg_armor(11)|difficulty(6) ,imodbits_cloth,
 [], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #saxons
["gambeson11", "Angle Gambeson", [("Gamb_Angle_03",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1440 , weight(4.8)|abundance(40)|head_armor(0)|body_armor(31)|leg_armor(11)|difficulty(6) ,imodbits_cloth,
 [], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #saxons
["gambeson12", "Briton Gambeson", [("Gamb_Briton_02",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1440 , weight(4)|abundance(40)|head_armor(0)|body_armor(29)|leg_armor(11)|difficulty(6) ,imodbits_cloth,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
["gambeson13", "Norse Gambeson", [("Gamb_Norse_02",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 2000 , weight(5.6)|abundance(40)|head_armor(0)|body_armor(35)|leg_armor(13)|difficulty(6) ,imodbits_cloth,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4, fac_kingdom_8]], #norse
["gambeson14", "Norse Gambeson", [("Gamb_Norse_03",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1600 , weight(5)|abundance(40)|head_armor(0)|body_armor(31)|leg_armor(11)|difficulty(6) ,imodbits_cloth,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4, fac_kingdom_8]], #norse
["gambeson15", "Saxon Long Gambeson", [("Gamb_Saxon_05",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 2400 , weight(6)|abundance(40)|head_armor(0)|body_armor(37)|leg_armor(14)|difficulty(6) ,imodbits_cloth,
 [], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #saxons
["gambeson16", "Briton Gambeson", [("Gamb_Briton_08",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1440 , weight(4)|abundance(40)|head_armor(0)|body_armor(29)|leg_armor(11)|difficulty(6) ,imodbits_cloth,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
["gambeson17", "Angle Gambeson", [("Gamb_Angle_07",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1600 , weight(4.8)|abundance(40)|head_armor(0)|body_armor(32)|leg_armor(11)|difficulty(6) ,imodbits_cloth,
 [], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #saxons
["gambeson18", "Saxon Long Gambeson", [("Gamb_Saxon_01",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1440 , weight(4.8)|abundance(30)|head_armor(0)|body_armor(29)|leg_armor(12)|difficulty(7) ,imodbits_cloth ,
 [], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #saxons
["gambeson19", "Frisian Gambeson", [("Gamb_Frisian_03",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1440 , weight(4.8)|abundance(40)|head_armor(0)|body_armor(31)|leg_armor(11)|difficulty(6) ,imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5]], #frisa, saxons 
["gambeson20", "Frisian Gambeson", [("Gamb_Frisian_01",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1600 , weight(4.8)|abundance(40)|head_armor(0)|body_armor(32)|leg_armor(11)|difficulty(6) ,imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5]], #frisa, saxons 
["gambeson21", "Common Gambeson", [("Gambeson_01",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1440 , weight(4.4)|abundance(40)|head_armor(0)|body_armor(29)|leg_armor(11)|difficulty(6) ,imodbits_cloth,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
["gambeson22", "Common Gambeson", [("Gambeson_02",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1440 , weight(4.4)|abundance(40)|head_armor(0)|body_armor(29)|leg_armor(11)|difficulty(6) ,imodbits_cloth,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
["gambeson23", "Common Gambeson", [("Gambeson_03",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1600 , weight(4.8)|abundance(40)|head_armor(0)|body_armor(32)|leg_armor(11)|difficulty(6) ,imodbits_cloth,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
["gambeson24", "Common Gambeson", [("Gambeson_04",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 2000 , weight(5.3)|abundance(40)|head_armor(0)|body_armor(32)|leg_armor(13)|difficulty(6) ,imodbits_cloth,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons


####gambesones pictish
 ["gambeson1gael", "Pictish Gambeson", [("Gamb_Picts_01",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1600 , weight(4.4)|abundance(40)|head_armor(0)|body_armor(31)|leg_armor(11)|difficulty(6) ,imodbits_cloth,
 [], [fac_kingdom_20]],
["gambeson2gael", "Pictish Gambeson", [("Gamb_Picts_02",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1600 , weight(4.4)|abundance(40)|head_armor(0)|body_armor(31)|leg_armor(11)|difficulty(6) ,imodbits_cloth,
 [], [fac_kingdom_20]],
["gambeson3gael", "Pictish Gambeson", [("Gamb_Picts_05",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1200 , weight(4)|abundance(40)|head_armor(0)|body_armor(29)|leg_armor(11)|difficulty(6) ,imodbits_cloth,
 [], [fac_kingdom_20]],
["gambeson4gael", "Pictish Gambeson", [("Gamb_Picts_03",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1200 , weight(4)|abundance(40)|head_armor(0)|body_armor(29)|leg_armor(11)|difficulty(6) ,imodbits_cloth,
 [], [fac_kingdom_20]],
["gambeson5gael", "Pictish Gambeson", [("Gamb_Picts_06",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1440 , weight(4)|abundance(40)|head_armor(0)|body_armor(29)|leg_armor(11)|difficulty(6) ,imodbits_cloth,
 [], [fac_kingdom_20]],
["gambeson6gael", "Pictish Gambeson", [("Gamb_Picts_04",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1440 , weight(4)|abundance(40)|head_armor(0)|body_armor(29)|leg_armor(11)|difficulty(6) ,imodbits_cloth,
 [], [fac_kingdom_20]],
["gambeson7gael", "Pictish Gambeson", [("Gamb_Picts_07",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1200 , weight(4)|abundance(40)|head_armor(0)|body_armor(29)|leg_armor(11)|difficulty(6) ,imodbits_cloth,
 [], [fac_kingdom_20]],
["gambeson8gael", "Pictish Gambeson", [("Gamb_Picts_08",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1200 , weight(4)|abundance(40)|head_armor(0)|body_armor(29)|leg_armor(11)|difficulty(6) ,imodbits_cloth,
 [], [fac_kingdom_20]],
#irish only
["gambeson9gael", "Goidelic Gambeson", [("Gamb_Irish_08",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1200 , weight(4)|abundance(10)|head_armor(0)|body_armor(29)|leg_armor(11)|difficulty(6) ,imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish and pictish shops
["gambeson10gael", "Goidelic Gambeson", [("Gamb_Irish_03",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1200 , weight(4)|abundance(10)|head_armor(0)|body_armor(29)|leg_armor(11)|difficulty(6) ,imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish and pictish shops
["gambeson11gael", "Goidelic Gambeson", [("Gamb_Irish_04",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1440 , weight(4)|abundance(10)|head_armor(0)|body_armor(29)|leg_armor(11)|difficulty(6) ,imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish and pictish shops
#with cloak irish only
 ["gambeson12gael", "Goidelic Gambeson", [("Gamb_Irish_01",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1600 , weight(4.4)|abundance(10)|head_armor(0)|body_armor(31)|leg_armor(11)|difficulty(6) ,imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish and pictish shops
 ["gambeson13gael", "Goidelic Gambeson", [("Gamb_Irish_02",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1600 , weight(4.4)|abundance(10)|head_armor(0)|body_armor(31)|leg_armor(11)|difficulty(6) ,imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish and pictish shops
["gambeson14gael", "Goidelic Gambeson", [("Gamb_Irish_05",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1200 , weight(4)|abundance(10)|head_armor(0)|body_armor(29)|leg_armor(11)|difficulty(6) ,imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish and pictish shops
["gambeson15gael", "Goidelic Gambeson", [("Gamb_Irish_06",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1440 , weight(4)|abundance(10)|head_armor(0)|body_armor(29)|leg_armor(11)|difficulty(6) ,imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish and pictish shops
["gambeson16gael", "Goidelic Gambeson", [("Gamb_Irish_07",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1200 , weight(4)|abundance(10)|head_armor(0)|body_armor(29)|leg_armor(11)|difficulty(6) ,imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish and pictish shops
#################
#pictish
["gambeson1cloak", "Pictish Gambeson", [("Gamb_Picts_09",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1200 , weight(4)|abundance(40)|head_armor(0)|body_armor(29)|leg_armor(11)|difficulty(6) ,imodbits_cloth,
 [], [fac_kingdom_20]],
["gambeson2cloak", "Pictish Gambeson", [("Gamb_Picts_10",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1200 , weight(4)|abundance(40)|head_armor(0)|body_armor(29)|leg_armor(11)|difficulty(6) ,imodbits_cloth,
 [], [fac_kingdom_20]],

#irish
["gambeson5cloak", "Goidelic Gambeson", [("Gamb_Irish_09",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1200 , weight(4)|abundance(10)|head_armor(0)|body_armor(29)|leg_armor(11)|difficulty(6) ,imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish and pictish shops
["gambeson6cloak", "Goidelic Gambeson", [("Gamb_Irish_10",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1200 , weight(4)|abundance(10)|head_armor(0)|body_armor(29)|leg_armor(11)|difficulty(6) ,imodbits_cloth,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish and pictish shops

#gambeson
#Frisian...
["gambeson3cloak", "Frisian Gambeson", [("Gamb_Frisian_07",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1440 , weight(4.8)|abundance(30)|head_armor(0)|body_armor(31)|leg_armor(11)|difficulty(7) ,imodbits_cloth ,
 [], [fac_kingdom_4, fac_kingdom_5]], #frisa, saxons 
["gambeson4cloak", "Frisian Gambeson", [("Gamb_Frisian_08",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1600 , weight(6)|abundance(30)|head_armor(0)|body_armor(31)|leg_armor(13)|difficulty(7) ,imodbits_cloth ,
 [], [fac_kingdom_4, fac_kingdom_5]], #frisa, saxons 
#
["gambeson25", "Norse Long Gambeson", [("Gamb_Norse_11",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1600 , weight(4.8)|abundance(30)|head_armor(0)|body_armor(29)|leg_armor(12)|difficulty(7) ,imodbits_cloth ,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4, fac_kingdom_8]], #norse
["gambeson26", "Angle Long Gambeson", [("Gamb_Angle_05",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 2400 , weight(6)|abundance(30)|head_armor(0)|body_armor(37)|leg_armor(14)|difficulty(7) ,imodbits_cloth,
 [], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #saxons
["gambeson27", "Norse Long Gambeson", [("Gamb_Norse_01",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1440 , weight(4.8)|abundance(30)|head_armor(0)|body_armor(29)|leg_armor(12)|difficulty(7) ,imodbits_cloth,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4, fac_kingdom_8]], #norse
["gambeson28", "Angle Gambeson", [("Gamb_Angle_06",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1440 , weight(4.8)|abundance(30)|head_armor(0)|body_armor(31)|leg_armor(11)|difficulty(7) ,imodbits_cloth,
 [], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #saxons
["gambeson29", "Norse Long Gambeson", [("Gamb_Norse_04",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1760 , weight(5.6)|abundance(30)|head_armor(0)|body_armor(32)|leg_armor(14)|difficulty(7) ,imodbits_cloth,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4, fac_kingdom_8]], #norse
["gambeson30", "Common Long Gambeson", [("Gambeson_05",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1440 , weight(4.8)|abundance(30)|head_armor(0)|body_armor(29)|leg_armor(12)|difficulty(7) ,imodbits_cloth,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
["gambeson31", "Common Long Gambeson", [("Gambeson_06",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1440 , weight(4.8)|abundance(30)|head_armor(0)|body_armor(29)|leg_armor(12)|difficulty(7) ,imodbits_cloth,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons

#gamebeson largo
#long
["gambeson32", "Saxon Long Gambeson", [("Gamb_Saxon_09",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1760 , weight(5.3)|abundance(20)|head_armor(0)|body_armor(29)|leg_armor(14)|difficulty(8) ,imodbits_cloth,
 [], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #saxons
#
["gambeson33", "Frisian Long Gambeson", [("Gamb_Frisian_05",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 2000 , weight(5.6)|abundance(20)|head_armor(0)|body_armor(32)|leg_armor(15)|difficulty(8) ,imodbits_cloth,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
["gambeson34", "Angle Long Gambeson", [("Gamb_Angle_02",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1760 , weight(5)|abundance(20)|head_armor(0)|body_armor(32)|leg_armor(12)|difficulty(8) ,imodbits_cloth,
 [], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #saxons
#short
["gambeson35", "Norse Gambeson", [("Gamb_Norse_10",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 2000 , weight(5.6)|abundance(40)|head_armor(0)|body_armor(35)|leg_armor(11)|difficulty(6) ,imodbits_cloth,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4, fac_kingdom_8]], #norse
#
["gambeson36", "Briton Long Gambeson", [("Gamb_Briton_07",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1600 , weight(5)|abundance(20)|head_armor(0)|body_armor(29)|leg_armor(12)|difficulty(8) ,imodbits_cloth,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
["gambeson37", "Briton Gambeson", [("Gamb_Briton_03",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1440 , weight(4)|abundance(20)|head_armor(0)|body_armor(29)|leg_armor(11)|difficulty(8) ,imodbits_cloth,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
["gambeson38", "Briton Long Gambeson", [("Gamb_Briton_06",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1760 , weight(5.6)|abundance(20)|head_armor(0)|body_armor(31)|leg_armor(14)|difficulty(8) ,imodbits_cloth,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
["gambeson39", "Angle Long Gambeson", [("Gamb_Angle_04",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 2000 , weight(5.3)|abundance(20)|head_armor(0)|body_armor(33)|leg_armor(12)|difficulty(8) ,imodbits_cloth,
 [], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #saxons
["gambeson40", "Briton Long Gambeson", [("Gamb_Briton_05",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 2400 , weight(5.6)|abundance(20)|head_armor(0)|body_armor(31)|leg_armor(14)|difficulty(8) ,imodbits_cloth,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
["gambeson41", "Briton Long Gambeson", [("Gamb_Briton_04",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 2000 , weight(5)|abundance(20)|head_armor(0)|body_armor(31)|leg_armor(12)|difficulty(8) ,imodbits_cloth,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
["gambeson42", "Briton Gambeson", [("Gamb_Briton_01",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1600 , weight(4.8)|abundance(20)|head_armor(0)|body_armor(29)|leg_armor(12)|difficulty(8) ,imodbits_cloth,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
["gambeson43", "Norse Long Gambeson", [("Gamb_Norse_05",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 2400 , weight(6)|abundance(20)|head_armor(0)|body_armor(37)|leg_armor(13)|difficulty(8) ,imodbits_cloth,
 [], norse_fac + frisia_fac], #norse
["gambeson44", "Frisian Long Gambeson", [("Gamb_Frisian_04",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 2400 , weight(6)|abundance(20)|head_armor(0)|body_armor(33)|leg_armor(15)|difficulty(8) ,imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5]], #frisa, saxons 
#short
["gambeson45", "Angle Gambeson", [("Gamb_Angle_08",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 2000 , weight(5.3)|abundance(40)|head_armor(0)|body_armor(32)|leg_armor(13)|difficulty(6) ,imodbits_cloth,
 [], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #saxons
#
["gambeson46", "Frisian Long Gambeson", [("Gamb_Frisian_02",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1760 , weight(5)|abundance(20)|head_armor(0)|body_armor(32)|leg_armor(12)|difficulty(8) ,imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5]], #frisa, saxons 
["gambeson47", "Common Long Gambeson", [("Gambeson_07",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 1600 , weight(5)|abundance(30)|head_armor(0)|body_armor(32)|leg_armor(12)|difficulty(7) ,imodbits_cloth,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
["gambeson48", "Common Long Gambeson", [("Gambeson_08",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 2000 , weight(5.3)|abundance(20)|head_armor(0)|body_armor(32)|leg_armor(14)|difficulty(8) ,imodbits_cloth,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons


###################ARMADURAS MEDIAS CHIEF finales acaba#############################
 ################################################################################
#######################################chief armor acaba##########################

############# ARMOR armadura chief finales empieza ###############################################
###################################################################################################

#####Vc armors armaduras
#Brynie, mail medio muslo
 ###---common - all factions ---# Shirt mail
["mail_shirt", "Frisian Byrnie", [("Chain_Frisian_01",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 6750 , weight(16)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(22)|difficulty(9) ,imodbits_mail,
 [], [fac_kingdom_4, fac_kingdom_5]], #frisa, saxons 
["mail_shirt_1", "Common Byrnie", [("Chainmail_02",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 6750 , weight(16)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(22)|difficulty(9) ,imodbits_mail],
["mail_shirt_2", "Pictish Lorica", [("Chain_Picts_05",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 4500 , weight(16)|abundance(10)|head_armor(0)|body_armor(40)|leg_armor(22)|difficulty(9) ,imodbits_mail,
 [], [fac_kingdom_20]],
["mail_shirt_3", "Common Byrnie", [("Chainmail_04",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 8100 , weight(20)|abundance(10)|head_armor(0)|body_armor(44)|leg_armor(24)|difficulty(12) ,imodbits_mail],
#Pictish short mail
["mail_shirt_6", "Pictish Lorica", [("Chain_Picts_01",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 4500 , weight(16)|abundance(10)|head_armor(0)|body_armor(40)|leg_armor(22)|difficulty(9) ,imodbits_mail,
 [], [fac_kingdom_20]],
["mail_shirt_7", "Pictish Lorica", [("Chain_Picts_02",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 6750 , weight(17.6)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(22)|difficulty(10) ,imodbits_mail,
 [], [fac_kingdom_20]],
["mail_shirt_8", "Cloaked Pictish Lorica", [("Chain_Picts_03",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 9000 , weight(19)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(25)|difficulty(11) ,imodbits_mail,
 [], [fac_kingdom_20]],
["mail_shirt_9", "Cloaked Pictish Lorica", [("Chain_Picts_04",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 8100 , weight(17.6)|abundance(10)|head_armor(0)|body_armor(44)|leg_armor(22)|difficulty(10) ,imodbits_mail,
 [], [fac_kingdom_20]],
#Briton byrnie with fur
["mail_shirt_10", "Elite Briton Byrnie", [("Chain_Briton_06",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 9900 , weight(20)|abundance(10)|head_armor(0)|body_armor(45)|leg_armor(24)|difficulty(12) ,imodbits_mail,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
 ["mail_shirt_11", "Elite Briton Byrnie", [("Chain_Briton_08",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 13500 , weight(22.4)|abundance(10)|head_armor(0)|body_armor(50)|leg_armor(24)|difficulty(14) ,imodbits_mail,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
#frisian
 ["mail_shirt_11_2", "Frisian Byrnie", [("Chain_Frisian_06",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 9900 , weight(17.6)|abundance(10)|head_armor(0)|body_armor(44)|leg_armor(24)|difficulty(10) ,imodbits_mail,
 [], [fac_kingdom_4, fac_kingdom_5]], #frisa, saxons
["mail_shirt_11_3", "Pictish Lorica", [("Chain_Picts_06",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 6750 , weight(17.6)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(22)|difficulty(10) ,imodbits_mail,
 [], [fac_kingdom_20]],
#common mailshirt with gambeson
 ["mail_shirt_12", "Common Byrnie", [("Chainmail_06",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 8100 , weight(20)|abundance(10)|head_armor(0)|body_armor(45)|leg_armor(24)|difficulty(12) ,imodbits_mail],
 ["mail_shirt_13", "Common Byrnie", [("Chainmail_07",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 8100 , weight(20)|abundance(10)|head_armor(0)|body_armor(45)|leg_armor(24)|difficulty(12) ,imodbits_mail],
#malla normal con tunic visible saxons no cloaks
 ["mail_shirt_4", "Frisian Byrnie", [("Chain_Frisian_03",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 8100 , weight(20)|abundance(10)|head_armor(0)|body_armor(45)|leg_armor(24)|difficulty(12) ,imodbits_mail,
 [], [fac_kingdom_4, fac_kingdom_5]], #frisa, saxons 
["mail_shirt_5", "Pictish Lorica", [("Chain_Picts_07",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 4500 , weight(16)|abundance(10)|head_armor(0)|body_armor(40)|leg_armor(22)|difficulty(9) ,imodbits_mail,
 [], [fac_kingdom_20]],
["mail_shirt_5_1", "Elite Briton Byrnie", [("Chain_Briton_07",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 11250 , weight(21)|abundance(10)|head_armor(0)|body_armor(48)|leg_armor(24)|difficulty(13) ,imodbits_mail,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
["mail_shirt_5_2", "Elite Saxon Halsberg", [("Chain_Saxon_07",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 11250 , weight(21)|abundance(10)|head_armor(0)|body_armor(46)|leg_armor(26)|difficulty(13) ,imodbits_mail,
 [], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #saxons
#malla long common
["mail_shirt_12_1", "Common Halsberg", [("Chainmail_03",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 6750 , weight(19)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(24)|difficulty(11) ,imodbits_mail],
["mail_shirt_12_2", "Common Halsberg", [("Chainmail_05",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 9900 , weight(21)|abundance(10)|head_armor(0)|body_armor(44)|leg_armor(25)|difficulty(13) ,imodbits_mail],
["mail_shirt_12_3", "Common Halsberg", [("Chainmail_08",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 11250 , weight(21)|abundance(10)|head_armor(0)|body_armor(45)|leg_armor(25)|difficulty(13) ,imodbits_mail],
["mail_shirt_12_4", "Common Halsberg", [("Chainmail_09",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 11350 , weight(21)|abundance(10)|head_armor(0)|body_armor(45)|leg_armor(26)|difficulty(13) ,imodbits_mail],
#malla normal con tunic visible 
["mail_shirt_13_1", "Elite Saxon Halsberg", [("Chain_Saxon_08",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 13500 , weight(24)|abundance(10)|head_armor(0)|body_armor(50)|leg_armor(26)|difficulty(14) ,imodbits_mail,
 [], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #saxons 
["mail_shirt_13_2", "Saxon Halsberg", [("Chain_Saxon_05",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 9000 , weight(22.4)|abundance(10)|head_armor(0)|body_armor(48)|leg_armor(25)|difficulty(14) ,imodbits_mail,
 [], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #saxons
["mail_shirt_13_3", "Saxon Halsberg", [("Chain_Saxon_04",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 8100 , weight(21)|abundance(10)|head_armor(0)|body_armor(45)|leg_armor(25)|difficulty(13) ,imodbits_mail,
 [], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #saxons
["mail_shirt_13_4", "Elite Saxon Lorica", [("Chain_Saxon_06",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 9900 , weight(19)|abundance(10)|head_armor(0)|body_armor(44)|leg_armor(26)|difficulty(11) ,imodbits_mail,
 [], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #saxons



##mail shirt finish
#armadura penalties media acaba
#######Byrnie normal common
["byrnie", "Common Halsberg", [("Chainmail_01",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 6750 , weight(17.6)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(23)|difficulty(12) ,imodbits_mail],
["byrnie2", "Frisian Lorica", [("Chain_Frisian_02",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 6750 , weight(17.6)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(23)|difficulty(10) ,imodbits_mail,
 [], [fac_kingdom_4, fac_kingdom_5]], #frisa, saxons 
#malla normal con gambeson visible
["byrnie3", "Common Halsberg", [("Chainmail_10",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 11250 , weight(21)|abundance(10)|head_armor(0)|body_armor(45)|leg_armor(25)|difficulty(13) ,imodbits_mail],
["byrnie4", "Briton Byrnie", [("Chain_Briton_03",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 9000 , weight(19)|abundance(10)|head_armor(0)|body_armor(45)|leg_armor(24)|difficulty(11) ,imodbits_mail,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
["byrnie5", "Saxon Halsberg", [("Chain_Saxon_01",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 6750 , weight(17.6)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(23)|difficulty(10) ,imodbits_mail,
 [], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #saxons
["byrnie6", "Briton Byrnie", [("Chain_Briton_04",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 8100 , weight(20)|abundance(10)|head_armor(0)|body_armor(45)|leg_armor(24)|difficulty(12) ,imodbits_mail,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
#malla normal sin gambeson visible con piel en los hombros
["byrnie7", "Elite Frisian Lorica", [("Chain_Frisian_07",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 11250 , weight(20)|abundance(10)|head_armor(0)|body_armor(45)|leg_armor(23)|difficulty(12) ,imodbits_mail,
 [], [fac_kingdom_4, fac_kingdom_5]], #frisa, saxons 
["byrnie8", "Elite Frisian Halsberg", [("Chain_Frisian_08",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 13500 , weight(22.4)|abundance(10)|head_armor(0)|body_armor(50)|leg_armor(24)|difficulty(14) ,imodbits_mail,
 [], [fac_kingdom_4, fac_kingdom_5]], #frisa, saxons 
#Irish lorica
["byrnie9", "Goidelic Lorica", [("Chain_Irish_01",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 6750 , weight(17.6)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(23)|difficulty(10) ,imodbits_mail,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish and pictish shops
["byrnie10", "Goidelic Lorica", [("Chain_Irish_02",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 4500 , weight(16)|abundance(10)|head_armor(0)|body_armor(40)|leg_armor(23)|difficulty(9) ,imodbits_mail,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish and pictish shops
["byrnie11", "Cloaked Goidelic Lorica", [("Chain_Irish_03",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 9000 , weight(20)|abundance(10)|head_armor(0)|body_armor(44)|leg_armor(24)|difficulty(12) ,imodbits_mail,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish and pictish shops
["byrnie12", "Cloaked Goidelic Lorica", [("Chain_Irish_04",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 9000 , weight(20)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(25)|difficulty(12) ,imodbits_mail,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish and pictish shops
#Briton b
["byrnie13", "Briton Byrnie", [("Chain_Briton_01",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 6750 , weight(16)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(22)|difficulty(9) ,imodbits_mail,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
["byrnie14", "Briton Byrnie", [("Chain_Briton_02",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 6750 , weight(16)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(22)|difficulty(9) ,imodbits_mail,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
["byrnie15", "Cloaked Briton Byrnie", [("Chain_Briton_05",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 9000 , weight(19)|abundance(10)|head_armor(0)|body_armor(44)|leg_armor(24)|difficulty(11) ,imodbits_mail,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
###viking long mail simple
["byrnie16", "Norse Hringserks", [("Chain_Norse_01",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 6750 , weight(17.6)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(23)|difficulty(10) ,imodbits_mail,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4, fac_kingdom_8]],#norse
["byrnie17", "Norse Hringserks", [("Chain_Norse_02",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 6750 , weight(17.6)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(23)|difficulty(10) ,imodbits_mail,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4, fac_kingdom_8]],#norse
#viking + gambeson
["byrnie18", "Norse Hringserks", [("Chain_Norse_03",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 8100 , weight(21)|abundance(10)|head_armor(0)|body_armor(45)|leg_armor(25)|difficulty(13) ,imodbits_mail,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4, fac_kingdom_8]], #norse
["byrnie19", "Norse Hringserks", [("Chain_Norse_04",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 8100 , weight(21)|abundance(10)|head_armor(0)|body_armor(45)|leg_armor(25)|difficulty(13) ,imodbits_mail,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4, fac_kingdom_8]], #norse
#
["byrnie20", "Frisian Halsberg", [("Chain_Frisian_04",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 8100 , weight(20)|abundance(10)|head_armor(0)|body_armor(45)|leg_armor(25)|difficulty(12) ,imodbits_mail,
 [], [fac_kingdom_4, fac_kingdom_5]], #frisa, saxons 
#saxon
["byrnie21", "Saxon Lorica", [("Chain_Saxon_02",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 6750 , weight(17.6)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(23)|difficulty(10) ,imodbits_mail,
 [], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #saxons
["byrnie22", "Saxon Halsberg", [("Chain_Saxon_03",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 8100 , weight(20)|abundance(10)|head_armor(0)|body_armor(45)|leg_armor(24)|difficulty(12) ,imodbits_mail,
 [], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #saxons
#Angle...
["byrnie23", "Angle Halsberg", [("Chain_Angle_01",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 6750 , weight(17.6)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(23)|difficulty(10) ,imodbits_mail,
 [], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #saxons
["byrnie24", "Angle Halsberg", [("Chain_Angle_02",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 6750 , weight(17.6)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(23)|difficulty(10) ,imodbits_mail,
 [], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #saxons
["byrnie25", "Angle Halsberg", [("Chain_Angle_03",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 8100 , weight(21)|abundance(10)|head_armor(0)|body_armor(45)|leg_armor(25)|difficulty(13) ,imodbits_mail,
 [], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #saxons
["byrnie26", "Angle Halsberg", [("Chain_Angle_04",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 8100 , weight(21)|abundance(10)|head_armor(0)|body_armor(45)|leg_armor(25)|difficulty(13) ,imodbits_mail,
 [], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #saxons
["byrnie27", "Cloaked Angle Halsberg", [("Chain_Angle_05",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 9000 , weight(20)|abundance(10)|head_armor(0)|body_armor(46)|leg_armor(24)|difficulty(12) ,imodbits_mail,
 [], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #saxons
["byrnie28", "Angle Halsberg with Fur", [("Chain_Angle_06",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 11250 , weight(21)|abundance(10)|head_armor(0)|body_armor(46)|leg_armor(25)|difficulty(13) ,imodbits_mail,
 [], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #saxons
["byrnie29", "Cloaked Angle Halsberg", [("Chain_Angle_07",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 9000 , weight(22.4)|abundance(10)|head_armor(0)|body_armor(48)|leg_armor(25)|difficulty(14) ,imodbits_mail,
 [], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #saxons
["byrnie30", "Angle Halsberg with Fur", [("Chain_Angle_08",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 13500 , weight(24)|abundance(10)|head_armor(0)|body_armor(50)|leg_armor(25)|difficulty(14) ,imodbits_mail,
 [], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #saxons
#with cloaks vikings
["byrnie31", "Cloaked Norse Hringserks", [("Chain_Norse_05",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 9000 , weight(22.4)|abundance(10)|head_armor(0)|body_armor(48)|leg_armor(25)|difficulty(13) ,imodbits_mail,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4, fac_kingdom_8]], #norse
#viking no cloak
["byrnie32", "Norse Hringserks", [("Chain_Norse_06",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 9900 , weight(19)|abundance(10)|head_armor(0)|body_armor(44)|leg_armor(26)|difficulty(11) ,imodbits_mail,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4, fac_kingdom_8]], #norse
#viking with fur
["byrnie33", "Norse Hringserks with Fur", [("Chain_Norse_07",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 11250 , weight(24)|abundance(10)|head_armor(0)|body_armor(46)|leg_armor(24)|difficulty(14) ,imodbits_mail,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4, fac_kingdom_8]], #norse
["byrnie34", "Norse Hringserks with Fur", [("Chain_Norse_08",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 13500 , weight(26)|abundance(10)|head_armor(0)|body_armor(50)|leg_armor(26)|difficulty(14) ,imodbits_mail,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4, fac_kingdom_8]], #norse

 #frisian long mail
["byrnie35", "Frisian Halsberg", [("Chain_Frisian_05",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 9000 , weight(22.4)|abundance(10)|head_armor(0)|body_armor(48)|leg_armor(25)|difficulty(14) ,imodbits_mail,
 [], [fac_kingdom_4, fac_kingdom_5]], #frisa, saxons
 #chainmails with cloak  irish
["byrnie36", "Goidelic Lorica", [("Chain_Irish_05",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 6750 , weight(17.6)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(23)|difficulty(10) ,imodbits_mail,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish and pictish shops
["byrnie37", "Goidelic Lorica", [("Chain_Irish_06",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 4500 , weight(16)|abundance(10)|head_armor(0)|body_armor(40)|leg_armor(23)|difficulty(9) ,imodbits_mail,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish and pictish shops
["byrnie38", "Goidelic Lorica", [("Chain_Irish_07",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 6750 , weight(17.6)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(23)|difficulty(10) ,imodbits_mail,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish and pictish shops

####Mail especiales
["orm_byrnie", "Orm's Lorica", [("thor_armor",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 20440 , weight(19)|abundance(10)|head_armor(12)|body_armor(58)|leg_armor(28)|difficulty(11) ,imodbits_mail],
["lamellar_armor", "Scale Lorica", [("Scalemail01",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 12000 , weight(16)|abundance(10)|head_armor(0)|body_armor(46)|leg_armor(26)|difficulty(9) ,imodbits_mail],

########################################################################################
 ####armaduras pesadas finales acaba chief############################################

  
#Quest-specific - perhaps can be used for prisoners, 
["burlap_tunic", "Burlap Tunic", [("Tunic_Norse_12",0)], itp_type_body_armor  |itp_covers_legs ,0,
 125 , weight(1)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(1)|difficulty(0) ,imodbits_cloth ], #cambiado chief


###############################sombreros y yemos chief #######################################
####VC gorros
# hoods common
["hood_01", "Hood", [("Hood01c",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,
 120, weight(1)|abundance(100)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["hood_02", "Hood", [("Hood01c_black",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,
 120, weight(1)|abundance(100)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria

###############

###phrygian
 #basic
["phrygian1", "Phrygian", [("Phrygian_basic01_blue",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_covers_hair_partially,0,
 100, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
["phrygian2", "Phrygian", [("Phrygian_basic01_red",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_covers_hair_partially,0,
 100, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
["phrygian3", "Phrygian", [("Phrygian_basic01_green",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_covers_hair_partially,0,
 100, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
["phrygian4", "Phrygian", [("Phrygian_basic01_natural",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_covers_hair_partially,0,
 100, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
["phrygian5", "Phrygian", [("Phrygian_basic01_black",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_covers_hair_partially,0,
 100, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
["phrygian6", "Phrygian", [("Phrygian_basic01_white",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_covers_hair_partially,0,
 100, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
#quality
["phrygian7", "Quality Phrygian", [("Phrygian_basic02_blue",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_covers_hair_partially,0,
 140, weight(1)|abundance(100)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
["phrygian8", "Quality Phrygian", [("Phrygian_basic02_red",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_covers_hair_partially,0,
 140, weight(1)|abundance(100)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
["phrygian9", "Quality Phrygian", [("Phrygian_basic02_green",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_covers_hair_partially,0,
 140, weight(1)|abundance(100)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
["phrygian10", "Quality Phrygian", [("Phrygian_basic02_yellow",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_covers_hair_partially,0,
 140, weight(1)|abundance(100)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
["phrygian11", "Quality Phrygian", [("Phrygian_basic02_natural",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_covers_hair_partially,0,
 140, weight(1)|abundance(100)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
["phrygian12", "Quality Phrygian", [("Phrygian_basic02_black",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_covers_hair_partially,0,
 140, weight(1)|abundance(100)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
["phrygian13", "Quality Phrygian", [("Phrygian_basic02_white",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_covers_hair_partially,0,
 140, weight(1)|abundance(100)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
#decorated
 ["phrygian14", "Decorated Phrygian", [("Phrygian01-1",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_covers_hair_partially,0,
 160, weight(1)|abundance(100)|head_armor(13)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
["phrygian15", "Decorated Phrygian", [("Phrygian01-2",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_covers_hair_partially,0,
 160, weight(1)|abundance(100)|head_armor(13)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
["phrygian16", "Decorated Phrygian", [("Phrygian02-1",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_covers_hair_partially,0,
 160, weight(1)|abundance(100)|head_armor(13)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
["phrygian17", "Decorated Phrygian", [("Phrygian02-2",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_covers_hair_partially,0,
 160, weight(1)|abundance(100)|head_armor(13)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
####gorros acabados chief##########3
 ############################
####################capas finaliza chief########################
 ############################################################


###############yelmos finales chief#############################
 ################################################################

#########Yelmos VC###########
####BRITONS
#bowl Nose (0)/ neck (0)/ cheeck (0):
["briton_helm", "Simple Helm", [("Spangenhelm02-1",0), ("Spangenhelm_rusty02-1", imodbit_rusty), ("Spangenhelm_rusty02-1", imodbit_battered), ("Spangenhelm_rusty02-1", imodbit_cracked)], itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 2060 , weight(1.5)|abundance(10)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], # britons
["briton_helm2", "Simple Helm", [("Spangenhelm_C02-1",0), ("Spangenhelm_C_rusty02-1", imodbit_rusty), ("Spangenhelm_C_rusty02-1", imodbit_battered), ("Spangenhelm_C_rusty02-1", imodbit_cracked)], itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 2060 , weight(1.5)|abundance(10)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], # britons

["briton_helm3", "Old Simple Helm", [("Spangenhelm_rusty02-1",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 1020 , weight(1.5)|abundance(20)|head_armor(41)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], # britons
["briton_helm4", "Old Simple Helm", [("Spangenhelm_C_rusty02-1",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 1020 , weight(1.5)|abundance(20)|head_armor(41)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], # britons

#bowl+ cuero Nose (0)/ neck (1)/ cheeck (0):
["briton_helm5", "Simple Helm with Leather", [("Spangenhelm02-2",0), ("Spangenhelm_rusty02-2", imodbit_rusty), ("Spangenhelm_rusty02-2", imodbit_battered), ("Spangenhelm_rusty02-2", imodbit_cracked)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 2580 , weight(2)|abundance(10)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], # britons
["briton_helm6", "Simple Helm with Leather", [("Spangenhelm_C02-2",0), ("Spangenhelm_C_rusty02-2", imodbit_rusty), ("Spangenhelm_C_rusty02-2", imodbit_battered), ("Spangenhelm_C_rusty02-2", imodbit_cracked)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
2580 , weight(2)|abundance(10)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], # britons

["briton_helm7", "Old Simple Helm with Leather", [("Spangenhelm_rusty02-2",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 1540 , weight(2)|abundance(20)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], # britons
["briton_helm8", "Old Simple Helm with Leather", [("Spangenhelm_C_rusty02-2",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 1540 , weight(2)|abundance(20)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], # britons

#bowl + mail + carrilleras Nose (0)/ neck (2)/ cheeck (1):
 ["briton_helm9", "Complete Helm", [("Spangenhelm02-4",0), ("Spangenhelm_rusty02-4", imodbit_rusty), ("Spangenhelm_rusty02-4", imodbit_battered), ("Spangenhelm_rusty02-4", imodbit_cracked)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 3120 , weight(2.5)|abundance(10)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], # britons
 ["briton_helm10", "Complete Helm", [("Spangenhelm_C02-4",0), ("Spangenhelm_C_rusty02-4", imodbit_rusty), ("Spangenhelm_C_rusty02-4", imodbit_battered), ("Spangenhelm_C_rusty02-4", imodbit_cracked)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 3120 , weight(2.5)|abundance(10)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], # britons

 ["briton_helm11", "Old Complete Helm", [("Spangenhelm_rusty02-4",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 2580 , weight(2.5)|abundance(20)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], # britons
 ["briton_helm12", "Old Complete Helm", [("Spangenhelm_C_rusty02-4",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 2580 , weight(2.5)|abundance(20)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], # britons

#nasal + mail Nose (1)/ neck (2)/ cheeck (0):
 ["briton_helm13", "Complete Helm", [("Spangenhelm01-5",0), ("Spangenhelm_rusty01-5", imodbit_rusty), ("Spangenhelm_rusty01-5", imodbit_battered), ("Spangenhelm_rusty01-5", imodbit_cracked)], itp_type_head_armor|itp_fit_to_head   ,0,
 3620 , weight(2.5)|abundance(10)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], # britons
 ["briton_helm14", "Complete Helm", [("Spangenhelm_C01-5",0), ("Spangenhelm_C_rusty01-5", imodbit_rusty), ("Spangenhelm_C_rusty01-5", imodbit_battered), ("Spangenhelm_C_rusty01-5", imodbit_cracked)], itp_type_head_armor|itp_fit_to_head   ,0,
 3620 , weight(2.5)|abundance(10)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], # britons
 ["briton_helm15", "Complete Helm", [("Spangenhelm_C01-6",0), ("Spangenhelm_C_rusty01-6", imodbit_rusty), ("Spangenhelm_C_rusty01-6", imodbit_battered), ("Spangenhelm_C_rusty01-6", imodbit_cracked)], itp_type_head_armor|itp_fit_to_head   ,0,
 3620 , weight(2.5)|abundance(10)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], # britons

 ["briton_helm16", "Old Complete Helm", [("Spangenhelm_rusty01-5",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 2580 , weight(2.5)|abundance(20)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], # britons
 ["briton_helm17", "Old Complete Helm", [("Spangenhelm_C_rusty01-5",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 2580 , weight(2.5)|abundance(20)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], # britons
 ["briton_helm18", "Old Complete Helm", [("Spangenhelm_C_rusty01-6",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 2580 , weight(2.5)|abundance(20)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], # britons
#bowl con nasal Nose (1)/ neck (0)/ cheeck (0): 
 ["briton_helm19", "Helm with Nasal", [("Spangenhelm01-1",0), ("Spangenhelm_rusty01-1", imodbit_rusty), ("Spangenhelm_rusty01-1", imodbit_battered), ("Spangenhelm_rusty01-1", imodbit_cracked)], itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 2580 , weight(1.5)|abundance(10)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], # britons
 ["briton_helm20", "Helm with Nasal", [("Spangenhelm_C01-1",0), ("Spangenhelm_C_rusty01-1", imodbit_rusty), ("Spangenhelm_C_rusty01-1", imodbit_battered), ("Spangenhelm_C_rusty01-1", imodbit_cracked)], itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 2580 , weight(1.5)|abundance(10)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], # britons
 ["briton_helm21", "Helm with Nasal", [("Spangenhelm_C01-2",0), ("Spangenhelm_C_rusty01-2", imodbit_rusty), ("Spangenhelm_C_rusty01-2", imodbit_battered), ("Spangenhelm_C_rusty01-2", imodbit_cracked)], itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 2580 , weight(1.5)|abundance(10)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], # britons

 ["briton_helm22", "Old Helm with Nasal", [("Spangenhelm_rusty01-1",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 1540 , weight(1.5)|abundance(20)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], # britons
 ["briton_helm23", "Old Helm with Nasal", [("Spangenhelm_C_rusty01-1",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 1540 , weight(1.5)|abundance(20)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], # britons
 ["briton_helm24", "Old Helm with Nasal", [("Spangenhelm_C_rusty01-2",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 1540 , weight(1.5)|abundance(20)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], # britons
#cuero atras + nasal Nose (1)/ neck (1)/ cheeck (0):
 ["briton_helm25", "Helm with Leather", [("Spangenhelm01-3",0), ("Spangenhelm_rusty01-3", imodbit_rusty), ("Spangenhelm_rusty01-3", imodbit_battered), ("Spangenhelm_rusty01-3", imodbit_cracked)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 3100 , weight(2)|abundance(10)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], # britons
 ["briton_helm26", "Helm with Leather", [("Spangenhelm_C01-3",0), ("Spangenhelm_C_rusty01-3", imodbit_rusty), ("Spangenhelm_C_rusty01-3", imodbit_battered), ("Spangenhelm_C_rusty01-3", imodbit_cracked)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 3100 , weight(2)|abundance(10)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], # britons
 ["briton_helm27", "Helm with Leather", [("Spangenhelm_C01-4",0), ("Spangenhelm_C_rusty01-4", imodbit_rusty), ("Spangenhelm_C_rusty01-4", imodbit_battered), ("Spangenhelm_C_rusty01-4", imodbit_cracked)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 3100 , weight(2)|abundance(10)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], # britons

 ["briton_helm28", "Old Helm with Leather", [("Spangenhelm_rusty01-3",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 2060 , weight(2)|abundance(20)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], # britons
 ["briton_helm29", "Old Helm with Leather", [("Spangenhelm_C_rusty01-3",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 2060 , weight(2)|abundance(20)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], # britons
 ["briton_helm30", "Old Helm with Leather", [("Spangenhelm_C_rusty01-4",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 2060 , weight(2)|abundance(20)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], # britons
#malla atras + nasal Nose (0)/ neck (2)/ cheeck (0):
["briton_helm31", "Helm with Mail", [("Spangenhelm_C02-3",0), ("Spangenhelm_C_rusty02-3", imodbit_rusty), ("Spangenhelm_C_rusty02-3", imodbit_battered), ("Spangenhelm_C_rusty02-3", imodbit_cracked)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 3100 , weight(2)|abundance(10)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], # britons
["briton_helm32", "Helm with Mail", [("Spangenhelm02-3",0), ("Spangenhelm_rusty02-3", imodbit_rusty), ("Spangenhelm_rusty02-3", imodbit_battered), ("Spangenhelm_rusty02-3", imodbit_cracked)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 3100 , weight(2)|abundance(10)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], # britons
####NOBLE Briton helmets, complete protection # +2 special quality protection
["briton_helm33", "Helm with Mail", [("Spangenhelm_rich1",0)], itp_type_head_armor|itp_fit_to_head   ,0, #with nasal +1
 6060 , weight(2)|abundance(20)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], # britons
["briton_helm34", "Helm with Mail", [("Spangenhelm_rich2",0)], itp_type_head_armor|itp_fit_to_head   ,0,
 6060 , weight(2)|abundance(20)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], # britons
#####
#malla y carrilleras + nasal Nose (1)/ neck (2)/ cheeck (1):
["briton_helm35", "Complete Helm", [("Spangenhelm01-7",0), ("Spangenhelm_rusty01-7", imodbit_rusty), ("Spangenhelm_rusty01-7", imodbit_battered), ("Spangenhelm_rusty01-7", imodbit_cracked)], itp_type_head_armor|itp_fit_to_head   ,0,
 5180 , weight(2.5)|abundance(10)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], # britons
 ["briton_helm36", "Complete Helm", [("Spangenhelm_C01-7",0), ("Spangenhelm_C_rusty01-7", imodbit_rusty), ("Spangenhelm_C_rusty01-7", imodbit_battered), ("Spangenhelm_C_rusty01-7", imodbit_cracked)], itp_type_head_armor|itp_fit_to_head   ,0,
 5180 , weight(2.5)|abundance(10)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], # britons
 ["briton_helm37", "Complete Helm", [("Spangenhelm_C01-8",0), ("Spangenhelm_C_rusty01-8", imodbit_rusty), ("Spangenhelm_C_rusty01-8", imodbit_battered), ("Spangenhelm_C_rusty01-8", imodbit_cracked)], itp_type_head_armor|itp_fit_to_head   ,0,
 5180 , weight(2.5)|abundance(10)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], # britons

["briton_helm38", "Old Complete Helm", [("Spangenhelm_rusty01-7",0)], itp_type_head_armor|itp_fit_to_head   ,0,
 4140 , weight(2.5)|abundance(10)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], # britons
 ["briton_helm39", "Old Complete Helm", [("Spangenhelm_C_rusty01-7",0)], itp_type_head_armor|itp_fit_to_head   ,0,
 4140 , weight(2.5)|abundance(10)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], # britons
 ["briton_helm40", "Old Complete Helm", [("Spangenhelm_C_rusty01-8",0)], itp_type_head_armor|itp_fit_to_head   ,0,
 4140 , weight(2.5)|abundance(10)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], # britons
##################### 
 
 #######angles and saxons
#bowl Nose (0)/ neck (0)/ cheeck (0):
["spangenhelm_1", "Simple Helm", [("Spangenhelm02-1",0), ("Spangenhelm_rusty02-1", imodbit_rusty), ("Spangenhelm_rusty02-1", imodbit_battered), ("Spangenhelm_rusty02-1", imodbit_cracked)], itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 2060 , weight(1.5)|abundance(10)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and angles
["spangenhelm_2", "Simple Helm", [("Spangenhelm_B02-1",0), ("Spangenhelm_B_rusty02-1", imodbit_rusty), ("Spangenhelm_B_rusty02-1", imodbit_battered), ("Spangenhelm_B_rusty02-1", imodbit_cracked)], itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 2060 , weight(1.5)|abundance(10)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and angles
["spangenhelm_3", "Old Simple Helm", [("Spangenhelm_rusty02-1",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 1020 , weight(1.5)|abundance(20)|head_armor(41)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and angles
["spangenhelm_4", "Old Simple Helm", [("Spangenhelm_B_rusty02-1",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 1020 , weight(1.5)|abundance(20)|head_armor(41)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and angles

#bowl+ cuero Nose (0)/ neck (1)/ cheeck (0):
["spangenhelm_5", "Simple Helm with Mail", [("Spangenhelm02-2",0), ("Spangenhelm_rusty02-2", imodbit_rusty), ("Spangenhelm_rusty02-2", imodbit_battered), ("Spangenhelm_rusty02-2", imodbit_cracked)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 2580 , weight(2)|abundance(10)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and angles
["spangenhelm_6", "Simple Helm with Mail", [("Spangenhelm_B02-2",0), ("Spangenhelm_B_rusty02-2", imodbit_rusty), ("Spangenhelm_B_rusty02-2", imodbit_battered), ("Spangenhelm_B_rusty02-2", imodbit_cracked)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 2580 , weight(2)|abundance(10)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and angles
["spangenhelm_7", "Old Simple Helm with Leather", [("Spangenhelm_rusty02-2",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 1540 , weight(2)|abundance(20)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and angles
#bowl+ cuero Nose (0)/ neck (1)/ cheeck (0):
["spangenhelm_8", "Old Anglo Saxon Helm", [("Wollaston_rusty2",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 2060 , weight(2)|abundance(20)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and angles

#bowl + mail + carrilleras Nose (0)/ neck (2)/ cheeck (1): #seguir y revisar los yelmos asignados
 ["spangenhelm_9", "Complete Helm", [("Spangenhelm02-4",0), ("Spangenhelm_rusty02-4", imodbit_rusty), ("Spangenhelm_rusty02-4", imodbit_battered), ("Spangenhelm_rusty02-4", imodbit_cracked)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 3120 , weight(2.5)|abundance(10)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and angles
 ["spangenhelm_10", "Complete Helm", [("Spangenhelm_B02-4",0), ("Spangenhelm_B_rusty02-4", imodbit_rusty), ("Spangenhelm_B_rusty02-4", imodbit_battered), ("Spangenhelm_B_rusty02-4", imodbit_cracked)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 3120 , weight(2.5)|abundance(10)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and angles
#bowl + mail + carrilleras Nose (1)/ neck (2)/ cheeck (0):
 ["spangenhelm_11", "Old Anglo Saxon Helm", [("Wollaston_rusty3",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 2580 , weight(2.5)|abundance(20)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and angles
 ["spangenhelm_12", "Old Anglo Saxon Helm", [("Wollaston_rusty5",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 2580 , weight(2.5)|abundance(20)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and angles

#nasal + mail Nose (1)/ neck (2)/ cheeck (0):
 ["spangenhelm_13", "Complete Helm", [("Spangenhelm01-6",0), ("Spangenhelm_rusty01-6", imodbit_rusty), ("Spangenhelm_rusty01-6", imodbit_battered), ("Spangenhelm_rusty01-6", imodbit_cracked)], itp_type_head_armor|itp_fit_to_head   ,0,
 3620 , weight(2.5)|abundance(10)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and angles
 ["spangenhelm_14", "Complete Helm", [("Spangenhelm_B01-5",0), ("Spangenhelm_B_rusty01-5", imodbit_rusty), ("Spangenhelm_B_rusty01-5", imodbit_battered), ("Spangenhelm_B_rusty01-5", imodbit_cracked)], itp_type_head_armor|itp_fit_to_head   ,0,
 3620 , weight(2.5)|abundance(10)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and angles
 ["spangenhelm_15", "Complete Helm", [("Spangenhelm_B01-6",0), ("Spangenhelm_B_rusty01-6", imodbit_rusty), ("Spangenhelm_B_rusty01-6", imodbit_battered), ("Spangenhelm_B_rusty01-6", imodbit_cracked)],itp_type_head_armor|itp_fit_to_head   ,0,
 3620 , weight(2.5)|abundance(10)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and angles

 ["spangenhelm_16", "Elite Anglo Saxon Helm", [("Wollaston5",0), ("Wollaston_rusty5", imodbit_rusty), ("Wollaston_rusty5", imodbit_battered), ("Wollaston_rusty5", imodbit_cracked)], itp_type_head_armor|itp_fit_to_head   ,0,
 3620 , weight(2.5)|abundance(10)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and angles
 ["spangenhelm_17", "Elite Anglo Saxon Helm", [("Wollaston3",0), ("Wollaston_rusty3", imodbit_rusty), ("Wollaston_rusty3", imodbit_battered), ("Wollaston_rusty3", imodbit_cracked)], itp_type_head_armor|itp_fit_to_head   ,0,
 3620 , weight(2.5)|abundance(10)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and angles
#nasal + mail Nose (1)/ neck (0)/ cheeck (1):
 ["spangenhelm_18", "Saxon Helm", [("Wollaston4",0)], itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 3100 , weight(2)|abundance(10)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and angles

#bowl con nasal Nose (1)/ neck (0)/ cheeck (0):
 ["spangenhelm_19", "Helm with Nasal", [("Spangenhelm_B01-1",0), ("Spangenhelm_B_rusty01-1", imodbit_rusty), ("Spangenhelm_B_rusty01-1", imodbit_battered), ("Spangenhelm_B_rusty01-1", imodbit_cracked)], itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 2580 , weight(1.5)|abundance(10)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and angles
 ["spangenhelm_20", "Helm with Nasal", [("Spangenhelm01-2",0), ("Spangenhelm_rusty01-2", imodbit_rusty), ("Spangenhelm_rusty01-2", imodbit_battered), ("Spangenhelm_rusty01-2", imodbit_cracked)], itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 2580 , weight(1.5)|abundance(10)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and angles
 ["spangenhelm_21", "Helm with Nasal", [("Spangenhelm_B01-2",0), ("Spangenhelm_B_rusty01-2", imodbit_rusty), ("Spangenhelm_B_rusty01-2", imodbit_battered), ("Spangenhelm_B_rusty01-2", imodbit_cracked)], itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 2580 , weight(1.5)|abundance(10)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and angles

 ["spangenhelm_22", "Helm with Nasal", [("Wollaston1",0), ("Wollaston_rusty1", imodbit_rusty), ("Wollaston_rusty1", imodbit_battered), ("Wollaston_rusty1", imodbit_cracked)], itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 2580 , weight(1.5)|abundance(10)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and angles
 ["spangenhelm_23", "Old Helm", [("Wollaston_rusty1",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 1540 , weight(1.5)|abundance(20)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and angles
 ["spangenhelm_24", "Old Helm with Nasal", [("Spangenhelm_B_rusty01-2",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 1540 , weight(1.5)|abundance(20)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and angles
#cuero atras + nasal Nose (1)/ neck (1)/ cheeck (0):
 ["spangenhelm_25", "Helm with Leather", [("Spangenhelm01-4",0), ("Spangenhelm_rusty01-4", imodbit_rusty), ("Spangenhelm_rusty01-4", imodbit_battered), ("Spangenhelm_rusty01-4", imodbit_cracked)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 3100 , weight(2)|abundance(10)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and angles
 ["spangenhelm_26", "Helm with Leather", [("Spangenhelm_B01-3",0), ("Spangenhelm_B_rusty01-3", imodbit_rusty), ("Spangenhelm_B_rusty01-3", imodbit_battered), ("Spangenhelm_B_rusty01-3", imodbit_cracked)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 3100 , weight(2)|abundance(10)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and angles
 ["spangenhelm_27", "Helm with Leather", [("Spangenhelm_B01-4",0), ("Spangenhelm_B_rusty01-4", imodbit_rusty), ("Spangenhelm_B_rusty01-4", imodbit_battered), ("Spangenhelm_B_rusty01-4", imodbit_cracked)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 3100 , weight(2)|abundance(10)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and angles

 ["spangenhelm_28", "Old Helm with Leather", [("Spangenhelm_rusty01-4",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 2060 , weight(2)|abundance(20)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and angles
 ["spangenhelm_29", "Old Helm with Leather", [("Spangenhelm_B_rusty01-3",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 2060 , weight(2)|abundance(20)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and angles
 ["spangenhelm_30", "Saxon Helm with Leather", [("Wollaston2",0), ("Wollaston_rusty2", imodbit_rusty), ("Wollaston_rusty2", imodbit_battered), ("Wollaston_rusty2", imodbit_cracked)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 3100 , weight(2)|abundance(10)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and angles
#malla atras + nasal Nose (0)/ neck (2)/ cheeck (0):
["spangenhelm_31", "Helm with Mail", [("Spangenhelm_C02-3",0), ("Spangenhelm_C_rusty02-3", imodbit_rusty), ("Spangenhelm_C_rusty02-3", imodbit_battered), ("Spangenhelm_C_rusty02-3", imodbit_cracked)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 3100 , weight(2)|abundance(10)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and angles
["spangenhelm_32", "Helm with Mail", [("Spangenhelm_B02-3",0), ("Spangenhelm_B_rusty02-3", imodbit_rusty), ("Spangenhelm_B_rusty02-3", imodbit_battered), ("Spangenhelm_B_rusty02-3", imodbit_cracked)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 3100 , weight(2)|abundance(10)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and angles
["spangenhelm_33", "Old Helm with Mail", [("Spangenhelm_rusty02-3",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 2060 , weight(2)|abundance(20)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and angles
["spangenhelm_34", "Old Helm with Mail", [("Spangenhelm_B_rusty02-3",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 2060 , weight(2)|abundance(20)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and angles
#malla y carrilleras + nasal Nose (1)/ neck (2)/ cheeck (1):
["spangenhelm_35", "Complete Helm", [("Spangenhelm01-8",0), ("Spangenhelm_rusty01-8", imodbit_rusty), ("Spangenhelm_rusty01-8", imodbit_battered), ("Spangenhelm_rusty01-8", imodbit_cracked)], itp_type_head_armor|itp_fit_to_head   ,0,
 5180 , weight(2.5)|abundance(10)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and angles
 ["spangenhelm_36", "Complete Helm", [("Spangenhelm_B01-7",0), ("Spangenhelm_B_rusty01-7", imodbit_rusty), ("Spangenhelm_B_rusty01-7", imodbit_battered), ("Spangenhelm_B_rusty01-7", imodbit_cracked)], itp_type_head_armor|itp_fit_to_head   ,0,
 5180 , weight(2.5)|abundance(10)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and angles
 ["spangenhelm_37", "Complete Helm", [("Spangenhelm_B01-8",0), ("Spangenhelm_B_rusty01-8", imodbit_rusty), ("Spangenhelm_B_rusty01-8", imodbit_battered), ("Spangenhelm_B_rusty01-8", imodbit_cracked)], itp_type_head_armor|itp_fit_to_head   ,0,
 5180 , weight(2.5)|abundance(10)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and angles

["spangenhelm_38", "Old Complete Helm", [("Spangenhelm_rusty01-8",0)], itp_type_head_armor|itp_fit_to_head   ,0,
 4140 , weight(2.5)|abundance(10)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and angles
#####wollaston noble helm + quality
 ["spangenhelm_39", "Nobleman Anglo Saxon Helm", [("Wollaston_rich1",0)], itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 6140 , weight(2.5)|abundance(10)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and angles
 ["spangenhelm_40", "Nobleman Anglo Saxon Helm", [("Wollaston_rich2",0)], itp_type_head_armor|itp_fit_to_head   ,0,
 7180 , weight(2.5)|abundance(10)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and angles
#############

####NORSES ONLY #######
 #### Rusty
#Nose (0)/ neck (0)/ cheeck (0): bowl
["vikingold_helm", "Old Norse Helm", [("Stromvka1_rusty-9",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially ,0,
 1020 , weight(1.5)|abundance(20)|head_armor(41)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["vikingold_helm2", "Old Norse Helm", [("Stromvka2_rusty-9",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially ,0,
 1020 , weight(1.5)|abundance(20)|head_armor(41)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
#Nose (1)/ neck (0)/ cheeck (0): With nasal
["vikingold_helm3", "Old Norse Helm with Nasal", [("Stromvka1_rusty-1",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially ,0,
 2580 , weight(2)|abundance(20)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["vikingold_helm4", "Old Norse Helm with Nasal", [("Stromvka1_rusty-2",0)], itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially ,0,
 2580 , weight(2)|abundance(20)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["vikingold_helm5", "Old Norse Helm with Nasal", [("Stromvka2_rusty-1",0)], itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially ,0,
 2580 , weight(2)|abundance(20)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["vikingold_helm6", "Old Norse Helm with Nasal", [("Stromvka2_rusty-2",0)], itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially ,0,
 2580 , weight(2)|abundance(20)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
#Nose (0)/ neck (1)/ cheeck (0): with neck only
["vikingold_helm7", "Old Helm", [("Stromvka2_rusty-10",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0,
 2580 , weight(2)|abundance(20)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["vikingold_helm8", "Old Helm", [("Stromvka1_rusty-10",0)],  itp_type_head_armor|itp_fit_to_head ,0,
 2580 , weight(2)|abundance(20)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
#Nose (1)/ neck (1)/ cheeck (0): nasal more neck
["vikingold_helm9", "Old Norse Helm with Nasal", [("Stromvka1_rusty-3",0)], itp_type_head_armor|itp_fit_to_head ,0,
 2060 , weight(2)|abundance(20)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["vikingold_helm10", "Old Norse Helm with Nasal", [("Stromvka1_rusty-4",0)], itp_type_head_armor|itp_fit_to_head ,0,
 2060 , weight(2)|abundance(20)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["vikingold_helm11", "Old Norse Helm with Nasal", [("Stromvka2_rusty-3",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0,
 2060 , weight(2)|abundance(20)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["vikingold_helm12", "Old Norse Helm with Nasal", [("Stromvka2_rusty-4",0)], itp_type_head_armor|itp_fit_to_head ,0,
 2060 , weight(2)|abundance(20)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
#Nose (0)/ neck (2)/ cheeck (0): neck mail
["vikingold_helm13", "Old Norse Helm with Mail", [("Stromvka1_rusty-11",0)], itp_type_head_armor|itp_fit_to_head ,0,
 2060 , weight(2.5)|abundance(20)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["vikingold_helm14", "Old Norse Helm with Mail", [("Stromvka2_rusty-11",0)], itp_type_head_armor|itp_fit_to_head ,0,
 2060 , weight(2.5)|abundance(20)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
#Nose (1)/ neck (2)/ cheeck (0): nasal + neck mail
["vikingold_helm15", "Old Norse Helm with Mail", [("Stromvka1_rusty-5",0)], itp_type_head_armor|itp_fit_to_head ,0,
 2580 , weight(2.5)|abundance(20)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["vikingold_helm16", "Old Norse Helm with Mail", [("Stromvka1_rusty-6",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0,
 2580 , weight(2.5)|abundance(20)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["vikingold_helm17", "Old Norse Helm with Mail", [("Stromvka2_rusty-5",0)], itp_type_head_armor|itp_fit_to_head ,0,
 2580 , weight(2.5)|abundance(20)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["vikingold_helm18", "Old Norse Helm with Mail", [("Stromvka2_rusty-6",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0,
 2580 , weight(2.5)|abundance(20)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
#Nose (0)/ neck (2)/ cheeck (1): neck mail + cheeks
["vikingold_helm19", "Old Complete Norse Helm", [("Stromvka1_rusty-12",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0,
 2580 , weight(2.5)|abundance(20)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["vikingold_helm20", "Old Complete Norse Helm", [("Stromvka2_rusty-12",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0,
 2580 , weight(2.5)|abundance(20)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
#Nose (1)/ neck (2)/ cheeck (1): Complete
["vikingold_helm21", "Old Complete Norse Helm", [("Stromvka1_rusty-7",0)],  itp_type_head_armor|itp_fit_to_head ,0,
 3640 , weight(2.5)|abundance(10)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["vikingold_helm22", "Old Complete Norse Helm", [("Stromvka1_rusty-8",0)],  itp_type_head_armor|itp_fit_to_head ,0,
 3640 , weight(2.5)|abundance(10)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["vikingold_helm23", "Old Complete Norse Helm", [("Stromvka2_rusty-7",0)],  itp_type_head_armor|itp_fit_to_head ,0,
 3640 , weight(2.5)|abundance(10)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["vikingold_helm24", "Old Complete Norse Helm", [("Stromvka2_rusty-8",0)],  itp_type_head_armor|itp_fit_to_head ,0,
 3640 , weight(2.5)|abundance(10)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
####
 
 ##normal
#Nose (0)/ neck (0)/ cheeck (0): bowl
["viking_helm", "Simple Norse Helm", [("Stromvka1-9",0), ("Stromvka1_rusty-9", imodbit_rusty), ("Stromvka1_rusty-9", imodbit_battered), ("Stromvka1_rusty-9", imodbit_cracked)], itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially ,0,
 2060 , weight(1.5)|abundance(10)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["viking_helm2", "Simple Norse Helm", [("Stromvka2-9",0), ("Stromvka2_rusty-9", imodbit_rusty), ("Stromvka2_rusty-9", imodbit_battered), ("Stromvka2_rusty-9", imodbit_cracked)], itp_merchandise| itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially ,0,
 2060 , weight(1.5)|abundance(10)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
#Nose (1)/ neck (0)/ cheeck (0): With nasal
["viking_helm3", "Norse Helm with Nasal", [("Stromvka1-1",0), ("Stromvka1_rusty-1", imodbit_rusty), ("Stromvka1_rusty-1", imodbit_battered), ("Stromvka1_rusty-1", imodbit_cracked)], itp_merchandise| itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially ,0,
 2580 , weight(2)|abundance(10)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["viking_helm4", "Norse Helm with Nasal", [("Stromvka1-2",0), ("Stromvka1_rusty-2", imodbit_rusty), ("Stromvka1_rusty-2", imodbit_battered), ("Stromvka1_rusty-2", imodbit_cracked)], itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially ,0,
 2580 , weight(2)|abundance(10)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["viking_helm5", "Norse Helm with Nasal", [("Stromvka2-1",0),("Stromvka2_rusty-1", imodbit_rusty), ("Stromvka2_rusty-1", imodbit_battered), ("Stromvka2_rusty-1", imodbit_cracked)], itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially ,0,
 2580 , weight(2)|abundance(10)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["viking_helm6", "Norse Helm with Nasal", [("Stromvka2-2",0),("Stromvka2_rusty-2", imodbit_rusty), ("Stromvka2_rusty-2", imodbit_battered), ("Stromvka2_rusty-2", imodbit_cracked)], itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially ,0,
 2580 , weight(2)|abundance(10)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
#Nose (0)/ neck (1)/ cheeck (0): with neck only
["viking_helm7", "Norse Helm", [("Stromvka2-10",0),("Stromvka2_rusty-10", imodbit_rusty), ("Stromvka2_rusty-10", imodbit_battered), ("Stromvka2_rusty-10", imodbit_cracked)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0,
 2580 , weight(2)|abundance(10)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["viking_helm8", "Norse Helm", [("Stromvka1-10",0), ("Stromvka1_rusty-10", imodbit_rusty), ("Stromvka1_rusty-10", imodbit_battered), ("Stromvka1_rusty-10", imodbit_cracked)],  itp_type_head_armor|itp_fit_to_head ,0,
 2580 , weight(2)|abundance(10)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
#Nose (1)/ neck (1)/ cheeck (0): nasal more neck
["viking_helm9", "Norse Helm with Nasal", [("Stromvka1-3",0), ("Stromvka1_rusty-3", imodbit_rusty), ("Stromvka1_rusty-3", imodbit_battered), ("Stromvka1_rusty-3", imodbit_cracked)], itp_type_head_armor|itp_fit_to_head ,0,
 3100 , weight(2)|abundance(10)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["viking_helm10", "Norse Helm with Nasal", [("Stromvka1-4",0), ("Stromvka1_rusty-4", imodbit_rusty), ("Stromvka1_rusty-4", imodbit_battered), ("Stromvka1_rusty-4", imodbit_cracked)], itp_type_head_armor|itp_fit_to_head ,0,
 3100 , weight(2)|abundance(10)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["viking_helm11", "Norse Helm with Nasal", [("Stromvka2-3",0),("Stromvka2_rusty-3", imodbit_rusty), ("Stromvka2_rusty-3", imodbit_battered), ("Stromvka2_rusty-3", imodbit_cracked)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0,
 3100 , weight(2)|abundance(10)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["viking_helm12", "Norse Helm with Nasal", [("Stromvka2-4",0),("Stromvka2_rusty-4", imodbit_rusty), ("Stromvka2_rusty-4", imodbit_battered), ("Stromvka2_rusty-4", imodbit_cracked)], itp_type_head_armor|itp_fit_to_head ,0,
 3100 , weight(2)|abundance(10)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
#Nose (0)/ neck (2)/ cheeck (0): neck mail
["viking_helm13", "Norse Helm with Mail", [("Stromvka1-11",0), ("Stromvka1_rusty-11", imodbit_rusty), ("Stromvka1_rusty-11", imodbit_battered), ("Stromvka1_rusty-11", imodbit_cracked)], itp_type_head_armor|itp_fit_to_head ,0,
 3100 , weight(2)|abundance(10)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["viking_helm14", "Norse Helm with Mail", [("Stromvka2-11",0),("Stromvka2_rusty-11", imodbit_rusty), ("Stromvka2_rusty-11", imodbit_battered), ("Stromvka2_rusty-11", imodbit_cracked)], itp_type_head_armor|itp_fit_to_head ,0,
 3100 , weight(2)|abundance(10)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
#Nose (1)/ neck (2)/ cheeck (0): nasal + neck mail
["viking_helm15", "Norse Helm with Nasal", [("Stromvka1-5",0), ("Stromvka1_rusty-5", imodbit_rusty), ("Stromvka1_rusty-5", imodbit_battered), ("Stromvka1_rusty-5", imodbit_cracked)], itp_type_head_armor|itp_fit_to_head ,0,
 3620 , weight(2.5)|abundance(10)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["viking_helm16", "Norse Helm with Nasal", [("Stromvka1-6",0), ("Stromvka1_rusty-6", imodbit_rusty), ("Stromvka1_rusty-6", imodbit_battered), ("Stromvka1_rusty-6", imodbit_cracked)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0,
 3620 , weight(2.5)|abundance(10)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["viking_helm17", "Norse Helm with Nasal", [("Stromvka2-5",0)], itp_type_head_armor|itp_fit_to_head ,0,
 3620 , weight(2.5)|abundance(10)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["viking_helm18", "Norse Helm with Nasal", [("Stromvka2-6",0),("Stromvka2_rusty-6", imodbit_rusty), ("Stromvka2_rusty-6", imodbit_battered), ("Stromvka2_rusty-6", imodbit_cracked)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0,
 3620 , weight(2.5)|abundance(10)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
#Nose (0)/ neck (2)/ cheeck (1): neck mail + cheeks
["viking_helm19", "Complete Norse Helm", [("Stromvka1-12",0), ("Stromvka1_rusty-12", imodbit_rusty), ("Stromvka1_rusty-12", imodbit_battered), ("Stromvka1_rusty-12", imodbit_cracked)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0,
 3620 , weight(2.5)|abundance(10)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["viking_helm20", "Complete Norse Helm", [("Stromvka2-12",0),("Stromvka2_rusty-12", imodbit_rusty), ("Stromvka2_rusty-12", imodbit_battered), ("Stromvka2_rusty-12", imodbit_cracked)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0,
 3620 , weight(2.5)|abundance(10)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
#Nose (1)/ neck (2)/ cheeck (1): Complete
["viking_helm21", "Complete Norse Helm", [("Stromvka1-7",0), ("Stromvka1_rusty-7", imodbit_rusty), ("Stromvka1_rusty-7", imodbit_battered), ("Stromvka1_rusty-7", imodbit_cracked)],  itp_type_head_armor|itp_fit_to_head ,0,
 4380 , weight(2.5)|abundance(10)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["viking_helm22", "Complete Norse Helm", [("Stromvka1-8",0), ("Stromvka1_rusty-8", imodbit_rusty), ("Stromvka1_rusty-8", imodbit_battered), ("Stromvka1_rusty-8", imodbit_cracked)],  itp_type_head_armor|itp_fit_to_head ,0,
 4380 , weight(2.5)|abundance(10)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["viking_helm23", "Complete Norse Helm", [("Stromvka2-7",0),("Stromvka2_rusty-7", imodbit_rusty), ("Stromvka2_rusty-7", imodbit_battered), ("Stromvka2_rusty-7", imodbit_cracked)],  itp_type_head_armor|itp_fit_to_head ,0,
 4380 , weight(2.5)|abundance(10)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["viking_helm24", "Complete Norse Helm", [("Stromvka2-8",0), ("Stromvka2_rusty-8", imodbit_rusty), ("Stromvka2_rusty-8", imodbit_battered), ("Stromvka2_rusty-8", imodbit_cracked)],  itp_type_head_armor|itp_fit_to_head ,0,
 4380 , weight(2.5)|abundance(10)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
####

#rusty
#Nose (1)/ neck (0)/ cheeck (0): nasal
 ["vikingold_elitehelm1", "Old Norse Helm", [("Gjermundbu_rusty",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 2580 , weight(2)|abundance(20)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
 ["vikingold_elitehelm2", "Old Norse Helm", [("GjermundbuC_rusty",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 2580 , weight(2)|abundance(20)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
 ["vikingold_elitehelm3", "Old Norse Helm", [("GjermundbuB_rusty",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 2580 , weight(2)|abundance(20)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
#Nose (1)/ neck (1)/ cheeck (0): nasal + neck
["vikingold_elitehelm4", "Old Norse Helm with Leather", [("GjermundbuB_rusty2",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 3160 , weight(2)|abundance(20)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["vikingold_elitehelm5", "Old Norse Helm with Leather", [("GjermundbuC_rusty2",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 3160 , weight(2)|abundance(20)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["vikingold_elitehelm6", "Old Norse Helm with Mail", [("Gjermundbu_rusty2",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 3160 , weight(2)|abundance(20)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
#Nose (1)/ neck (2)/ cheeck (0): #nasal + neck mail
["vikingold_elitehelm7", "Old Norse Helm with Mail", [("GjermundbuB_rusty3",0)], itp_type_head_armor|itp_fit_to_head   ,0,
 4220 , weight(2)|abundance(20)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria

#####Nobleman helmet vikings##### +2 quality
["vikingold_elitehelm8", "Rich Norse Helm", [("GjermundbuC_rich1",0)], itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 4130 , weight(2)|abundance(10)|head_armor(49)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["vikingold_elitehelm9", "Rich Norse Helm", [("GjermundbuC_rich2",0)], itp_type_head_armor|itp_fit_to_head   ,0,
 5190 , weight(2)|abundance(10)|head_armor(51)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
######
#normal
#Nose (1)/ neck (0)/ cheeck (0): nasal
["viking_elitehelm1", "Norse Helm", [("Gjermundbu",0), ("Gjermundbu_rusty", imodbit_rusty), ("Gjermundbu_rusty", imodbit_battered), ("Gjermundbu_rusty", imodbit_cracked)], itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 3030 , weight(2)|abundance(10)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["viking_elitehelm2", "Norse Helm", [("GjermundbuC",0), ("GjermundbuC_rusty", imodbit_rusty), ("GjermundbuC_rusty", imodbit_battered), ("GjermundbuC_rusty", imodbit_cracked)], itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 3030 , weight(2)|abundance(10)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
#Nose (1)/ neck (1)/ cheeck (0): nasal + neck
["viking_elitehelm3", "Norse Helm with Leather", [("Gjermundbu2",0), ("Gjermundbu_rusty2", imodbit_rusty), ("Gjermundbu_rusty2", imodbit_battered), ("Gjermundbu_rusty2", imodbit_cracked)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 3690 , weight(2)|abundance(10)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["viking_elitehelm4", "Norse Helm", [("GjermundbuB",0), ("GjermundbuB_rusty", imodbit_rusty), ("GjermundbuB_rusty", imodbit_battered), ("GjermundbuB_rusty", imodbit_cracked)], itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,		#(GjermundbuB has no neck)
 3690 , weight(2)|abundance(10)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["viking_elitehelm5", "Norse Helm with Leather", [("GjermundbuB2",0), ("GjermundbuB_rusty2", imodbit_rusty), ("GjermundbuB_rusty2", imodbit_battered), ("GjermundbuB_rusty2", imodbit_cracked)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 3690 , weight(2)|abundance(10)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["viking_elitehelm6", "Norse Helm with Leather", [("GjermundbuC2",0), ("GjermundbuC_rusty2", imodbit_rusty), ("GjermundbuC_rusty2", imodbit_battered), ("GjermundbuC_rusty2", imodbit_cracked)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 3690 , weight(2)|abundance(10)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
#Nose (1)/ neck (2)/ cheeck (0): #nasal + neck mail
["viking_elitehelm7", "Norse Helm with Mail", [("GjermundbuB3",0), ("GjermundbuB_rusty3", imodbit_rusty), ("GjermundbuB_rusty3", imodbit_battered), ("GjermundbuB_rusty3", imodbit_cracked)], itp_type_head_armor|itp_fit_to_head   ,0,
 4150 , weight(2)|abundance(10)|head_armor(49)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["viking_elitehelm8", "Norse Helm with Mail", [("GjermundbuC3",0), ("GjermundbuC_rusty3", imodbit_rusty), ("GjermundbuC_rusty3", imodbit_battered), ("GjermundbuC_rusty3", imodbit_cracked)], itp_type_head_armor|itp_fit_to_head   ,0,
 4150 , weight(2)|abundance(10)|head_armor(49)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["viking_elitehelm9", "Norse Helm with Mail", [("Gjermundbu3",0), ("Gjermundbu_rusty3", imodbit_rusty), ("Gjermundbu_rusty3", imodbit_battered), ("Gjermundbu_rusty3", imodbit_cracked)], itp_type_head_armor|itp_fit_to_head   ,0,
 4150 , weight(2)|abundance(10)|head_armor(49)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria

#Elite
#Nose (1)/ neck (0)/ cheeck (0): nasal
 ["viking_noblehelm1", "Elite Norse Helm", [("Gjermundbu_noble",0)], itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 4830 , weight(2)|abundance(10)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
#Nose (1)/ neck (1)/ cheeck (0): nasal + neck
["viking_noblehelm2", "Elite Norse Helm with Leather", [("Gjermundbu_noble2",0)], itp_type_head_armor|itp_fit_to_head   ,0,
 5890 , weight(2)|abundance(10)|head_armor(49)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
#Nose (1)/ neck (2)/ cheeck (0): #nasal + neck mail
["viking_noblehelm3", "Elite Norse Helm with Mail", [("Gjermundbu_noble3",0)], itp_type_head_armor|itp_fit_to_head   ,0,
 6950 , weight(2)|abundance(10)|head_armor(51)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
####
#############
 
#########irish and pictish only
#bowl
#cuero atras + nasal Nose (1)/ neck (1)/ cheeck (0):
#Noble helmet, malla y carrilleras + nasal Nose (1)/ neck (2)/ cheeck (1) +2 quality
["angle_helmet1", "Noble Helm", [("Coppergate_rich",0)], itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 6680 , weight(2.5)|abundance(10)|head_armor(51)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
#bowl
#cuero atras + nasal Nose (1)/ neck (1)/ cheeck (0):
 ["angle_helmet2", "Helm with Leather", [("Coppergate2",0), ("Coppergate_rusty2", imodbit_rusty), ("Coppergate_rusty2", imodbit_battered), ("Coppergate_rusty2", imodbit_cracked)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 3220 , weight(2)|abundance(10)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops

#malla atras + nasal Nose (1)/ neck (2)/ cheeck (0):
["angle_helmet3", "Helm with Mail", [("Coppergate1",0), ("Coppergate_rusty1", imodbit_rusty), ("Coppergate_rusty1", imodbit_battered), ("Coppergate_rusty1", imodbit_cracked)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0,
 6680 , weight(2)|abundance(10)|head_armor(51)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
#malla atras + nasal Nose (1)/ neck (0)/ cheeck (0):
["angle_helmet4", "Helm with Mail", [("Coppergate",0), ("Coppergate_rusty", imodbit_rusty), ("Coppergate_rusty", imodbit_battered), ("Coppergate_rusty", imodbit_cracked)], itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially   ,0,
 3640 , weight(2.5)|abundance(10)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops

#malla y carrilleras + nasal Nose (1)/ neck (2)/ cheeck (1)
["angle_helmet5", "Old Complete Helm", [("Coppergate_rusty3",0)], itp_type_head_armor|itp_fit_to_head   ,0,
 3680 , weight(2.5)|abundance(10)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
["angle_helmet6", "Complete Helm", [("Coppergate3",0), ("Coppergate_rusty3", imodbit_rusty), ("Coppergate_rusty3", imodbit_battered), ("Coppergate_rusty3", imodbit_cracked)], itp_type_head_armor|itp_fit_to_head   ,0,
 4120 , weight(2.5)|abundance(10)|head_armor(49)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
#########


###Yelmos especiales
 ["elf_helmet", "Elf's Helm", [("Broa",0)], itp_unique|itp_type_head_armor|itp_fit_to_head   ,0,
 9120 , weight(2)|abundance(10)|head_armor(53)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate], #
#special smiths
["noble_helm_smith", "Noble Helm", [("Coppergate_rich2",0)], itp_type_head_armor|itp_fit_to_head   ,0,
 6680 , weight(2.5)|abundance(10)|head_armor(51)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate], #irish and pictish shops
["hersir_helm", "Hersir Helm", [("GjermundbuC_rich2",0)], itp_type_head_armor|itp_fit_to_head   ,0,
 9120 , weight(2.5)|abundance(10)|head_armor(53)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate], #frisa, norse and northumbria


############
#Coronas, solo reyes finales #### ESpeciales
 #################################
["crown1", "Crown", [("Crown",0)],itp_type_head_armor|itp_doesnt_cover_hair|itp_fit_to_head   ,0,
 10150 , weight(0.5)|abundance(10)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbit_lordly],#imdbit special removed strength requirement so that female characters can use it
###########coronas finales#############3
#para decapitaciones, casco chief invisible
["sarranid_horseman_helmet", "No head", [("empty",0)], itp_type_head_armor|itp_fit_to_head|itp_covers_head   ,0,
 180 , weight(2)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ],
#saco en cabeza Mainques chief
["saco_enlacabeza", "Sack", [("saco",0)], itp_unique|itp_type_head_armor|itp_fit_to_head|itp_covers_head   ,0,
 180 , weight(2)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ],


#######invisible items chief para animales sin jinete o animals walkers
## ["invisible_armor",  "No Armor", [("no_armor",0)], itp_type_body_armor  |itp_covers_legs ,0, 1259 , weight(18)|abundance(100)|head_armor(0)|body_armor(38)|leg_armor(19)|difficulty(7) ,imodbits_mail ],
##["invisible_boots",  "No Boots", [("no_boots",0)], itp_type_foot_armor | itp_attach_armature,0, 465 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(21)|difficulty(0) ,imodbits_cloth ],
##["invisible_gloves","N Gloves", [("no_gloves",0)], itp_type_hand_armor,0, 190, weight(0.25)|abundance(120)|body_armor(12)|difficulty(0),imodbits_cloth],

####Yelmos finales acaba#################################
 ############################################################

 
# Chief empieza########
####ARMAS DE ATAQUE#########


###armas de no filo, porras, mazas madera etc... finalizadas
 ####################### #revision
["wooden_stick",         "Wooden Stick", [("wooden_stick",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry|itp_wooden_attack, itc_scimitar, 
12 , weight(2)|difficulty(0)|spd_rtng(95) | weapon_length(80)|swing_damage(12 , blunt) | thrust_damage(0 ,  pierce),imodbits_club ], #chief cambiado
["club_hard",         "Club", [("club",0)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry|itp_wooden_attack, itc_scimitar, 
180 , weight(2)|difficulty(0)|spd_rtng(95) | weapon_length(71)|swing_damage(12 , blunt) | thrust_damage(0 ,  pierce),imodbits_club ], #chief cambiado
###special troll bridge 2handed axe
 ["club_troll","Troll's Axe", [("Axt08",0)], itp_unique|itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_bonus_against_shield|itp_wooden_parry, itc_greatsword|itcf_carry_axe_back, 
1570 , weight(4)|difficulty(21)|spd_rtng(70) | weapon_length(120)|swing_damage(50 , cut) | thrust_damage(10 ,  blunt),imodbits_axe ], #chief cambiado

#####no filo
 ##############################

####cuchillos y seax chief###################
 ###########################################
 #lengths set to models in this section
#irish, britons and pictish
["knife",         "Hunting Knife", [("Knife1",0),("Knife1_Scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_no_parry, itc_dagger|itcf_carry_quiver_back_right|itcf_show_holster_when_drawn,
 380 , weight(0.5)|difficulty(0)|spd_rtng(98) | weapon_length(31)|swing_damage(9 , cut) | thrust_damage(20 ,  pierce),imodbits_sword,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_11, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
["knife2",         "Hunting Knife", [("Knife2",0),("Knife2_Scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_no_parry, itc_dagger|itcf_carry_quiver_back_right|itcf_show_holster_when_drawn,
 380 , weight(0.5)|difficulty(0)|spd_rtng(98) | weapon_length(30)|swing_damage(9 , cut) | thrust_damage(20 ,  pierce),imodbits_sword,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_11, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
["knife3",         "Hunting Knife", [("Knife3",0),("Knife3_Scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_no_parry, itc_dagger|itcf_carry_quiver_back_right|itcf_show_holster_when_drawn,
 380 , weight(0.5)|difficulty(0)|spd_rtng(98) | weapon_length(30)|swing_damage(9 , cut) | thrust_damage(20 ,  pierce),imodbits_sword,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_11, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
["knife4",         "Hunting Knife", [("Knife4",0),("Knife4_Scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_no_parry, itc_dagger|itcf_carry_quiver_back_right|itcf_show_holster_when_drawn,
 380 , weight(0.5)|difficulty(0)|spd_rtng(98) | weapon_length(29)|swing_damage(9 , cut) | thrust_damage(20,  pierce),imodbits_sword,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_11, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
["knife5",         "Hunting Knife", [("Knife5",0),("Knife5_Scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_no_parry, itc_dagger|itcf_carry_quiver_back_right|itcf_show_holster_when_drawn,
 380 , weight(0.5)|difficulty(0)|spd_rtng(98) | weapon_length(30)|swing_damage(9 , cut) | thrust_damage(20 ,  pierce),imodbits_sword,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_11, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
#rest
 #long seax - Broadseax
["longseax1",         "Broadseax", [("Longseax1",0),("Longseax1_Scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_no_parry, itc_dagger|itcf_carry_quiver_back_right|itcf_show_holster_when_drawn,
 640 , weight(1)|difficulty(0)|abundance(100)|spd_rtng(93) | weapon_length(60)|swing_damage(20 , cut) | thrust_damage(15 ,  pierce),imodbits_sword,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, norse and northumbria, saxons
["longseax2",         "Broadseax", [("Longseax2",0),("Longseax2_Scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_no_parry, itc_dagger|itcf_carry_quiver_back_right|itcf_show_holster_when_drawn,
 640 , weight(1)|difficulty(0)|abundance(100)|spd_rtng(93) | weapon_length(60)|swing_damage(20 , cut) | thrust_damage(15 ,  pierce),imodbits_sword,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, norse and northumbria, saxons
["longseax3",         "Broadseax", [("Longseax3",0),("Longseax3_Scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_no_parry, itc_dagger|itcf_carry_quiver_back_right|itcf_show_holster_when_drawn,
 640 , weight(1)|difficulty(0)|abundance(100)|spd_rtng(93) | weapon_length(60)|swing_damage(20 , cut) | thrust_damage(15 ,  pierce),imodbits_sword,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, norse and northumbria, saxons
["longseax4",         "Broadseax", [("Longseax4",0),("Longseax4_Scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_no_parry, itc_dagger|itcf_carry_quiver_back_right|itcf_show_holster_when_drawn,
 640 , weight(1)|difficulty(0)|abundance(100)|spd_rtng(93) | weapon_length(60)|swing_damage(20 , cut) | thrust_damage(15 ,  pierce),imodbits_sword,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, norse and northumbria, saxons
["longseax5",         "Broadseax", [("Longseax5",0),("Longseax5_Scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_no_parry, itc_dagger|itcf_carry_quiver_back_right|itcf_show_holster_when_drawn,
 640 , weight(1)|difficulty(0)|abundance(100)|spd_rtng(93) | weapon_length(60)|swing_damage(20 , cut) | thrust_damage(15 ,  pierce),imodbits_sword,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, norse and northumbria, saxons
 #long seax - langseax
["longseax6",         "Langseax", [("langseax01",0),("langseax_scab01", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_no_parry, itc_dagger|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 1090 , weight(0.9)|abundance(10)|difficulty(4)|spd_rtng(95) | weapon_length(71)|swing_damage(26 , cut) | thrust_damage(16 ,  pierce),imodbits_sword,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4, fac_kingdom_8]], #frisa, vikings
["longseax7",         "Langseax", [("langseax02",0),("langseax_scab02", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_no_parry, itc_dagger|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 1090 , weight(0.9)|abundance(10)|difficulty(4)|spd_rtng(95) | weapon_length(71)|swing_damage(26 , cut) | thrust_damage(16 ,  pierce),imodbits_sword,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4, fac_kingdom_8]], #frisa, vikings
["longseax8",         "Langseax", [("langseax03",0),("langseax_scab03", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_no_parry, itc_dagger|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 1090 , weight(0.9)|abundance(10)|difficulty(4)|spd_rtng(95) | weapon_length(71)|swing_damage(26 , cut) | thrust_damage(16 ,  pierce),imodbits_sword,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4, fac_kingdom_8]], #frisa, vikings
["longseax9",         "Langseax", [("langseax04",0),("langseax_scab04", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_no_parry, itc_dagger|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 1090 , weight(0.9)|abundance(10)|difficulty(4)|spd_rtng(95) | weapon_length(71)|swing_damage(26 , cut) | thrust_damage(16 ,  pierce),imodbits_sword,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4, fac_kingdom_8]], #frisa, vikings
["longseax10",         "Langseax", [("langseax05",0),("langseax_scab05", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_no_parry, itc_dagger|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 1090 , weight(0.9)|abundance(10)|difficulty(4)|spd_rtng(95) | weapon_length(71)|swing_damage(26 , cut) | thrust_damage(16 ,  pierce),imodbits_sword,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4, fac_kingdom_8]], #frisa, vikings

#normal seax
["seax_1",         "Seax", [("Seax1",0),("Seax1_Scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_no_parry, itc_dagger|itcf_carry_quiver_back_right|itcf_show_holster_when_drawn,
 380 , weight(0.5)|difficulty(0)|spd_rtng(96) | weapon_length(37)|swing_damage(10 , cut) | thrust_damage(22 ,  pierce),imodbits_sword,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, norse and northumbria, saxons
["seax_2",         "Seax", [("Seax2",0),("Seax2_Scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_no_parry, itc_dagger|itcf_carry_quiver_back_right|itcf_show_holster_when_drawn,
 380 , weight(0.5)|difficulty(0)|spd_rtng(96) | weapon_length(37)|swing_damage(10 , cut) | thrust_damage(22 ,  pierce),imodbits_sword,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, norse and northumbria, saxons
["seax_3",         "Seax", [("Seax3",0),("Seax3_Scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_no_parry, itc_dagger|itcf_carry_quiver_back_right|itcf_show_holster_when_drawn,
 380 , weight(0.5)|difficulty(0)|spd_rtng(96) | weapon_length(37)|swing_damage(10 , cut) | thrust_damage(22 ,  pierce),imodbits_sword,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, norse and northumbria, saxons
["seax_4",         "Seax", [("Seax4",0),("Seax4_Scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_no_parry, itc_dagger|itcf_carry_quiver_back_right|itcf_show_holster_when_drawn,
 380 , weight(0.5)|difficulty(0)|spd_rtng(96) | weapon_length(37)|swing_damage(10 , cut) | thrust_damage(22,  pierce),imodbits_sword,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, norse and northumbria, saxons
["seax_5",         "Seax", [("Seax5",0),("Seax5_Scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_no_parry, itc_dagger|itcf_carry_quiver_back_right|itcf_show_holster_when_drawn,
 380 , weight(0.5)|difficulty(0)|spd_rtng(96) | weapon_length(37)|swing_damage(10 , cut) | thrust_damage(22 ,  pierce),imodbits_sword,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, norse and northumbria, saxons


 #mainquest special
["ragnar_seax",         "Ragnar's Langseax", [("Sword47_Ragnar",0),("Scabbard47",ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_no_blur|itp_no_parry, itc_dagger|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
3090 , weight(1.05)|difficulty(4)|spd_rtng(94) | weapon_length(76)|swing_damage(32 , cut) | thrust_damage(20 ,  pierce),imodbits_sword],
["elf_seax",         "Elf's Langseax", [("Sword41elf",0),("Scabbard41elf",ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_no_blur|itp_no_parry, itc_dagger|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
3090 , weight(1.05)|difficulty(4)|spd_rtng(94) | weapon_length(76)|swing_damage(34 , cut) | thrust_damage(18 ,  pierce),imodbits_sword],
###############cuchillos y seaxa caba chief#############################


####Espadas chief finales #####################
########################################
 #########VC Swords begin
#basica, anglo sajones and vikings
#lenght normal saxons
["spatha", "Sword", [("Sword02",0),("Scabbard02", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 2790 , weight(1.15)|abundance(10)|difficulty(6)|spd_rtng(92) | weapon_length(81)|swing_damage(23 , cut) | thrust_damage(18 ,  pierce),imodbits_sword,
  [], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #saxons
["spatha_2", "Sword", [("Sword07",0),("Scabbard07", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 2790 , weight(1.15)|abundance(10)|difficulty(6)|spd_rtng(92) | weapon_length(81)|swing_damage(23 , cut) | thrust_damage(18 ,  pierce),imodbits_sword,
  [], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #saxons
["spatha_3", "Sword", [("Sword12",0),("Scabbard12", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 2790 , weight(1.15)|abundance(10)|difficulty(6)|spd_rtng(92) | weapon_length(81)|swing_damage(23 , cut) | thrust_damage(18 ,  pierce),imodbits_sword,
  [], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #saxons
["spatha_4", "Sword", [("Sword17",0),("Scabbard17", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 2790 , weight(1.15)|abundance(10)|difficulty(6)|spd_rtng(92) | weapon_length(81)|swing_damage(23 , cut) | thrust_damage(18 ,  pierce),imodbits_sword,
  [], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #saxons
["spatha_5", "Sword", [("Sword22",0),("Scabbard22", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 2790 , weight(1.15)|abundance(10)|difficulty(6)|spd_rtng(92) | weapon_length(81)|swing_damage(23 , cut) | thrust_damage(18 ,  pierce),imodbits_sword,
  [], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #saxons
["spatha_6", "Sword", [("Sword42",0),("Scabbard42", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 2790 , weight(1.15)|abundance(10)|difficulty(6)|spd_rtng(92) | weapon_length(81)|swing_damage(23 , cut) | thrust_damage(18 ,  pierce),imodbits_sword,
  [], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #saxons
#lenght normal 2 vikings and saxons
["spatha_7", "Sword", [("Sword05",0),("Scabbard05", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 2790 , weight(1.15)|abundance(10)|difficulty(6)|spd_rtng(92) | weapon_length(81)|swing_damage(25 , cut) | thrust_damage(16 ,  pierce),imodbits_sword,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4,fac_kingdom_5, fac_kingdom_6, fac_kingdom_7,fac_kingdom_8]], #vikings
["spatha_8", "Sword", [("Sword10",0),("Scabbard10", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 2790 , weight(1.15)|abundance(10)|difficulty(6)|spd_rtng(92) | weapon_length(81)|swing_damage(25 , cut) | thrust_damage(16 ,  pierce),imodbits_sword,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4,fac_kingdom_5, fac_kingdom_6, fac_kingdom_7,fac_kingdom_8]], #vikings
["sword", "Sword", [("Sword15",0),("Scabbard15", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 2790 , weight(1.15)|abundance(10)|difficulty(6)|spd_rtng(92) | weapon_length(81)|swing_damage(25 , cut) | thrust_damage(16 ,  pierce),imodbits_sword,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4,fac_kingdom_5, fac_kingdom_6, fac_kingdom_7,fac_kingdom_8]], #vikings
["sword_2", "Sword", [("Sword20",0),("Scabbard20", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 2790 , weight(1.15)|abundance(10)|difficulty(6)|spd_rtng(92) | weapon_length(81)|swing_damage(25 , cut) | thrust_damage(16 ,  pierce),imodbits_sword,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4,fac_kingdom_5, fac_kingdom_6, fac_kingdom_7,fac_kingdom_8]], #vikings
["sword_3", "Sword", [("Sword25",0),("Scabbard25", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 2790 , weight(1.15)|abundance(10)|difficulty(6)|spd_rtng(92) | weapon_length(81)|swing_damage(25 , cut) | thrust_damage(16 ,  pierce),imodbits_sword,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4,fac_kingdom_5, fac_kingdom_6, fac_kingdom_7,fac_kingdom_8]], #vikings
["sword_4", "Sword", [("Sword45",0),("Scabbard45", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 2790 , weight(1.15)|abundance(10)|difficulty(6)|spd_rtng(92) | weapon_length(81)|swing_damage(25 , cut) | thrust_damage(16 ,  pierce),imodbits_sword,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4,fac_kingdom_5, fac_kingdom_6, fac_kingdom_7,fac_kingdom_8]], #vikings
#short swords vikings
["sword_5", "Short Sword", [("Sword04",0),("Scabbard04", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 1890 , weight(1.05)|abundance(10)|difficulty(6)|spd_rtng(93) | weapon_length(76)|swing_damage(21 , cut) | thrust_damage(20 ,  pierce),imodbits_sword,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and vikings
["sword_6", "Short Sword", [("Sword09",0),("Scabbard09", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 1890 , weight(1.05)|abundance(10)|difficulty(6)|spd_rtng(93) | weapon_length(76)|swing_damage(21 , cut) | thrust_damage(20 ,  pierce),imodbits_sword,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and vikings
 ["sword_7", "Short Sword", [("Sword14",0),("Scabbard14", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 1890 , weight(1.05)|abundance(10)|difficulty(6)|spd_rtng(93) | weapon_length(76)|swing_damage(21 , cut) | thrust_damage(20 ,  pierce),imodbits_sword,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and vikings
["sword_8", "Short Sword", [("Sword19",0),("Scabbard19", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 1890 , weight(1.05)|abundance(10)|difficulty(6)|spd_rtng(93) | weapon_length(76)|swing_damage(21 , cut) | thrust_damage(20 ,  pierce),imodbits_sword,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and vikings

["new_sword1", "Short Sword", [("Sword24",0),("Scabbard24", ixmesh_carry)],  itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 1890 , weight(1.05)|abundance(10)|difficulty(6)|spd_rtng(93) | weapon_length(76)|swing_damage(18 , cut) | thrust_damage(23 ,  pierce),imodbits_sword,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4, fac_kingdom_8]], #frisa, saxons and vikings
["new_sword2", "Short Sword", [("Sword29",0),("Scabbard29", ixmesh_carry)],  itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 1890 , weight(1.05)|abundance(10)|difficulty(6)|spd_rtng(93) | weapon_length(76)|swing_damage(18 , cut) | thrust_damage(23 ,  pierce),imodbits_sword,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4, fac_kingdom_8]], #frisa, saxons and vikings
 ["new_sword3", "Short Sword", [("Sword34",0),("Scabbard34", ixmesh_carry)],  itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 1890 , weight(1.05)|abundance(10)|difficulty(6)|spd_rtng(93) | weapon_length(76)|swing_damage(18 , cut) | thrust_damage(23 ,  pierce),imodbits_sword,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4, fac_kingdom_8]], #frisa, saxons and vikings
 ["new_sword4", "Short Sword", [("Sword39",0),("Scabbard39", ixmesh_carry)],  itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 1890 , weight(1.05)|abundance(10)|difficulty(6)|spd_rtng(93) | weapon_length(76)|swing_damage(18 , cut) | thrust_damage(23 ,  pierce),imodbits_sword,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4, fac_kingdom_8]], #frisa, saxons and vikings
["new_sword5", "Short Sword", [("Sword44",0),("Scabbard44", ixmesh_carry)],  itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 1890 , weight(1.05)|abundance(10)|difficulty(6)|spd_rtng(93) | weapon_length(76)|swing_damage(18 , cut) | thrust_damage(23 ,  pierce),imodbits_sword,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4, fac_kingdom_8]], #frisa, saxons and vikings
 ["new_sword6", "Sword", [("Sword32",0),("Scabbard32", ixmesh_carry)],  itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 2790 , weight(1.15)|abundance(10)|difficulty(6)|spd_rtng(92) | weapon_length(81)|swing_damage(25 , cut) | thrust_damage(16 ,  pierce),imodbits_sword,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4, fac_kingdom_8]], #frisa, saxons and vikings

#nobles saxons and vikings
#leght normal saxons
["noble_sword", "Rich Sword", [("Sword46",0),("Scabbard46", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 4960 , weight(1.15)|abundance(10)|difficulty(7)|spd_rtng(92) | weapon_length(81)|swing_damage(28 , cut) | thrust_damage(20 ,  pierce),imodbits_sword,
  [], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #saxons
["noble_sword_2", "Ulfberth Sword", [("Sword50_Ulfberht",0),("Scabbard50", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 6960 , weight(1.15)|abundance(10)|difficulty(7)|spd_rtng(92) | weapon_length(90)|swing_damage(31 , cut) | thrust_damage(22 ,  pierce),imodbits_sword,
  [], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #saxons
["noble_sword_3", "False Ulfberth Sword", [("Sword50_Ulfberht",0),("Scabbard50", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 4060 , weight(1.15)|abundance(10)|difficulty(7)|spd_rtng(92) | weapon_length(90)|swing_damage(27 , cut) | thrust_damage(19 ,  pierce),imodbits_sword,
  [], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #saxons
#lenght normal 2 vikings
["noble_sword_4", "Rich Sword", [("Sword30",0),("Scabbard30", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 4960 , weight(1.15)|abundance(10)|difficulty(7)|spd_rtng(92) | weapon_length(81)|swing_damage(30 , cut) | thrust_damage(18 ,  pierce),imodbits_sword,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4,fac_kingdom_8]], #vikings
["noble_sword_5", "Ulfberth Sword", [("Sword50_Ulfberht",0),("Scabbard50", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 6960 , weight(1.15)|abundance(10)|difficulty(7)|spd_rtng(92) | weapon_length(90)|swing_damage(31 , cut) | thrust_damage(22 ,  pierce),imodbits_sword,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4,fac_kingdom_8]], #vikings
["noble_sword_6", "False Ulfberth Sword", [("Sword50_Ulfberht",0),("Scabbard50", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 4060 , weight(1.15)|abundance(10)|difficulty(7)|spd_rtng(92) | weapon_length(90)|swing_damage(27 , cut) | thrust_damage(19 ,  pierce),imodbits_sword,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3,fac_kingdom_4,fac_kingdom_8]], #vikings

#briton sword common
["old_swordv", "Briton Sword", [("Sword03",0),("Scabbard03", ixmesh_carry)],  itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 2790 , weight(1.25)|abundance(10)|difficulty(7)|spd_rtng(90) | weapon_length(91)|swing_damage(28 , cut) | thrust_damage(13 ,  pierce),imodbits_sword,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #britons
 ["old_swordv2", "Briton Sword", [("Sword08",0),("Scabbard08", ixmesh_carry)],  itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 2790 , weight(1.25)|abundance(10)|difficulty(7)|spd_rtng(90) | weapon_length(91)|swing_damage(28 , cut) | thrust_damage(13 ,  pierce),imodbits_sword,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #britons
 ["old_swordv3", "Briton Sword", [("Sword13",0),("Scabbard13", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 2790 , weight(1.25)|abundance(10)|difficulty(7)|spd_rtng(90) | weapon_length(91)|swing_damage(28 , cut) | thrust_damage(13 ,  pierce),imodbits_sword,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #britons
["old_swordv4", "Briton Sword", [("Sword18",0),("Scabbard18", ixmesh_carry)],  itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 2790 , weight(1.25)|abundance(10)|difficulty(7)|spd_rtng(90) | weapon_length(91)|swing_damage(28 , cut) | thrust_damage(13 ,  pierce),imodbits_sword,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #britons
["old_swordv5", "Briton Sword", [("Sword23",0),("Scabbard23", ixmesh_carry)],  itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 2790 , weight(1.25)|abundance(10)|difficulty(7)|spd_rtng(90) | weapon_length(91)|swing_damage(28 , cut) | thrust_damage(13 ,  pierce),imodbits_sword,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #britons
 ["old_swordv6", "Briton Sword", [("Sword38",0),("Scabbard38", ixmesh_carry)],  itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 2790 , weight(1.25)|abundance(10)|difficulty(7)|spd_rtng(90) | weapon_length(91)|swing_damage(28 , cut) | thrust_damage(13 ,  pierce),imodbits_sword,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #britons
 ["old_swordv7", "Briton Sword", [("Sword43",0),("Scabbard43", ixmesh_carry)],  itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 2790 , weight(1.25)|abundance(10)|difficulty(7)|spd_rtng(90) | weapon_length(91)|swing_damage(28 , cut) | thrust_damage(13 ,  pierce),imodbits_sword,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #britons

#britons elite
#long
 ["noble_sword_7", "Rich Briton Sword", [("Sword28",0),("Scabbard28", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 3840 , weight(1.25)|abundance(10)|difficulty(7)|spd_rtng(90) | weapon_length(91)|swing_damage(31 , cut) | thrust_damage(15 ,  pierce),imodbits_sword,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
["noble_sword_8", "Rich Briton Sword", [("Sword33",0),("Scabbard33", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 3840 , weight(1.25)|abundance(10)|difficulty(7)|spd_rtng(90) | weapon_length(91)|swing_damage(31 , cut) | thrust_damage(15 ,  pierce),imodbits_sword,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
 ["noble_sword_9", "Rich Briton Sword", [("Sword38",0),("Scabbard38", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 3840 , weight(1.25)|abundance(10)|difficulty(7)|spd_rtng(90) | weapon_length(91)|swing_damage(31 , cut) | thrust_damage(15 ,  pierce),imodbits_sword,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
["noble_sword_10", "Rich Briton Sword", [("Sword13",0),("Scabbard13", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 3840 , weight(1.25)|abundance(10)|difficulty(7)|spd_rtng(90) | weapon_length(91)|swing_damage(31 , cut) | thrust_damage(15 ,  pierce),imodbits_sword,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
 ["noble_sword_11", "Rich Briton Sword", [("Sword43",0),("Scabbard43", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 3840 , weight(1.25)|abundance(10)|difficulty(7)|spd_rtng(90) | weapon_length(91)|swing_damage(31 , cut) | thrust_damage(15 ,  pierce),imodbits_sword,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
#normal
["noble_sword_12", "Rich Briton Sword", [("Sword20",0),("Scabbard20", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 4960 , weight(1.15)|abundance(10)|difficulty(7)|spd_rtng(92) | weapon_length(81)|swing_damage(30 , cut) | thrust_damage(18 ,  pierce),imodbits_sword,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #britons
["noble_sword_13", "Rich Briton Sword", [("Sword40",0),("Scabbard40", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 4960 , weight(1.15)|abundance(10)|difficulty(7)|spd_rtng(92) | weapon_length(81)|swing_damage(30 , cut) | thrust_damage(18 ,  pierce),imodbits_sword,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #britons
#only nobles
 ["noble_swordv", "False Ulfberth Sword", [("Sword50_Ulfberht",0),("Scabbard50", ixmesh_carry)],  itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 4060 , weight(1.15)|abundance(10)|difficulty(7)|spd_rtng(92) | weapon_length(90)|swing_damage(27 , cut) | thrust_damage(19 ,  pierce),imodbits_sword,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
 ["noble_swordv3", "False Ulfberth Sword", [("Sword50_Ulfberht",0),("Scabbard50", ixmesh_carry)],  itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 4060 , weight(1.15)|abundance(10)|difficulty(7)|spd_rtng(92) | weapon_length(90)|swing_damage(27 , cut) | thrust_damage(19 ,  pierce),imodbits_sword,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #britons
["noble_swordv4", "Ulfberth Sword", [("Sword50_Ulfberht",0),("Scabbard50", ixmesh_carry)],  itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 6960 , weight(1.15)|abundance(10)|difficulty(7)|spd_rtng(92) | weapon_length(90)|swing_damage(31 , cut) | thrust_damage(22 ,  pierce),imodbits_sword,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
["noble_swordv5", "Rich Sword", [("Sword35",0),("Scabbard35", ixmesh_carry)],  itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 4960 , weight(1.15)|abundance(10)|difficulty(7)|spd_rtng(92) | weapon_length(81)|swing_damage(30 , cut) | thrust_damage(18 ,  pierce),imodbits_sword,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
 ["noble_swordv6", "Rich Sword", [("Sword37",0),("Scabbard37", ixmesh_carry)],  itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 4960 , weight(1.15)|abundance(10)|difficulty(7)|spd_rtng(92) | weapon_length(81)|swing_damage(30 , cut) | thrust_damage(18 ,  pierce),imodbits_sword,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons
 ["noble_swordv7", "Rich Sword", [("Sword27",0),("Scabbard27", ixmesh_carry)],  itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 4960 , weight(1.15)|abundance(10)|difficulty(7)|spd_rtng(92) | weapon_length(81)|swing_damage(30 , cut) | thrust_damage(18 ,  pierce),imodbits_sword,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, saxons and britons

##Irish and pictish swords
#nobles
 ["irish_long_sword1", "Goidelic Noble Long Sword", [("GP_swords01",0),("GP_swords01_Scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 4960 , weight(1.35)|abundance(10)|difficulty(8)|spd_rtng(89) | weapon_length(94)|swing_damage(35 , cut) | thrust_damage(13 ,  pierce),imodbits_sword,
 [], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
 ["irish_long_sword2", "Goidelic Noble Long Sword", [("GP_swords10",0),("GP_swords10_Scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 4960 , weight(1.75)|abundance(10)|difficulty(9)|spd_rtng(87) | weapon_length(100)|swing_damage(33 , cut) | thrust_damage(13 ,  pierce),imodbits_sword,
 [], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
#common elite
 ["irish_long_sword3", "Goidelic Long Sword", [("GP_swords02",0),("GP_swords02_Scabbard", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 4790 , weight(1.35)|abundance(10)|difficulty(9)|spd_rtng(87) | weapon_length(100)|swing_damage(33 , cut) | thrust_damage(11 ,  pierce),imodbits_sword,
 [], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
 ["irish_long_sword4", "Goidelic Long Sword", [("GP_swords03",0),("GP_swords03_Scabbard", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 4790 , weight(1.35)|abundance(10)|difficulty(8)|spd_rtng(89) | weapon_length(94)|swing_damage(30 , cut) | thrust_damage(11 ,  pierce),imodbits_sword,
 [], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
 ["irish_long_sword5", "Goidelic Long Sword", [("GP_swords05",0),("GP_swords05_Scabbard", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 4790 , weight(1.35)|abundance(10)|difficulty(8)|spd_rtng(89) | weapon_length(94)|swing_damage(30 , cut) | thrust_damage(11 ,  pierce),imodbits_sword,
 [], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
 ["irish_long_sword6", "Goidelic Long Sword", [("GP_swords06",0),("GP_swords06_Scabbard", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 4790 , weight(1.35)|abundance(10)|difficulty(9)|spd_rtng(87) | weapon_length(100)|swing_damage(33 , cut) | thrust_damage(11 ,  pierce),imodbits_sword,
 [], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
 ["irish_long_sword7", "Goidelic Long Sword", [("GP_swords07",0),("GP_swords07_Scabbard", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 4790 , weight(1.35)|abundance(10)|difficulty(8)|spd_rtng(89) | weapon_length(94)|swing_damage(30 , cut) | thrust_damage(11 ,  pierce),imodbits_sword,
 [], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
 ["irish_long_sword8", "Goidelic Long Sword", [("GP_swords08",0),("GP_swords08_Scabbard", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 4790 , weight(1.35)|abundance(10)|difficulty(8)|spd_rtng(89) | weapon_length(94)|swing_damage(30 , cut) | thrust_damage(11 ,  pierce),imodbits_sword,
 [], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops

#short swords irish and pictish
 ["irish_short_sword1",         "Goidelic Short Sword", [("short_swords01",0),("short_swords01_Scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_blur|itp_no_parry, itc_dagger|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 2790 , weight(1)|difficulty(4)|spd_rtng(92) | weapon_length(70)|swing_damage(13 , cut) | thrust_damage(32 ,  pierce),imodbits_sword,
 [], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
 ["irish_short_sword2",         "Goidelic Short Sword", [("short_swords05",0),("short_swords05_Scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_blur|itp_no_parry, itc_dagger|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 2790 , weight(1)|difficulty(4)|spd_rtng(92) | weapon_length(70)|swing_damage(13 , cut) | thrust_damage(32 ,  pierce),imodbits_sword,
 [], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
 ["irish_short_sword3",         "Goidelic Short Sword", [("short_swords10",0),("short_swords10_Scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_blur|itp_no_parry, itc_dagger|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 2790 , weight(1)|difficulty(4)|spd_rtng(92) | weapon_length(70)|swing_damage(13 , cut) | thrust_damage(32 ,  pierce),imodbits_sword,
 [], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops

#champion sword 2h irish only. 1 elite unit
["championsword1", "Goidelic Champion Sword", [("GP_swords04",0),("GP_swords04_Scabbard", ixmesh_carry)], itp_merchandise|itp_type_two_handed_wpn|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_penalty_with_shield, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 5030 , weight(1.5)|difficulty(11)|abundance(10)|spd_rtng(86) | weapon_length(120)|swing_damage(38 , cut) | thrust_damage(13 ,  pierce),imodbits_sword,
 [], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #
["championsword2", "Goidelic Champion Sword", [("GP_swords09",0),("GP_swords09_Scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_primary|itp_no_blur|itp_cant_use_on_horseback|itp_penalty_with_shield, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 5030 , weight(1.5)|difficulty(11)|abundance(10)|spd_rtng(86) | weapon_length(120)|swing_damage(38 , cut) | thrust_damage(13 ,  pierce),imodbits_sword,
 [], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]],
#
################espadas especiales
 ["widow_maker", "Widow Maker", [("Sword50_Ulfberht",0),("Scabbard50", ixmesh_carry)],  itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 8360 , weight(1.25)|abundance(10)|difficulty(9)|spd_rtng(90) | weapon_length(90)|swing_damage(33 , cut) | thrust_damage(18 ,  pierce),imodbits_sword], 
["suttonhoosword2", "Bandit King Sword", [("Sword50_Ulfberht",0),("Scabbard50", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 8960 , weight(1.25)|difficulty(7)|spd_rtng(90) | weapon_length(90)|swing_damage(34 , cut) | thrust_damage(16 ,  pierce),imodbits_sword],
#siren song special smith
["siren_song", "Laufi", [("Sword49_Laufi",0),("Scabbard49", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 8960 , weight(1.25)|difficulty(9)|spd_rtng(86) | weapon_length(86)|swing_damage(30 , cut) | thrust_damage(19 ,  pierce),imodbits_sword],
###espada de Olvir White Hair mainquest chief
["sword_of_war", "Olvir's Sword", [("Sword52_Runesword",0),("Scabbard52", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 8960 , weight(1.25)|difficulty(7)|spd_rtng(92) | weapon_length(81)|swing_damage(28 , cut) | thrust_damage(22 ,  pierce),imodbits_sword], ###########espadas chief acaba
###espadas special scenes
["sword_premium1", "Nad", [("Sword51",0),("Scabbard51", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 8960 , weight(1.25)|difficulty(7)|spd_rtng(89) | weapon_length(96)|swing_damage(34 , cut) | thrust_damage(14 ,  pierce),imodbits_sword], ###########espadas chief acaba
["sword_premium2", "Draguandil", [("Sword52_Runesword",0),("Scabbard52", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 8960 , weight(1.25)|difficulty(7)|spd_rtng(92) | weapon_length(81)|swing_damage(28 , cut) | thrust_damage(22 ,  pierce),imodbits_sword], ###########espadas chief acaba
["sword_premium3", "Blynjubitr", [("Sword48_Brynjubitr",0),("Scabbard48", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_no_blur, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 8960 , weight(1.25)|difficulty(7)|spd_rtng(92) | weapon_length(81)|swing_damage(29 , cut) | thrust_damage(21 ,  pierce),imodbits_sword], ###########espadas chief acaba
  
#####Hachas finales################################# 
 ####################################################
###########hachas 1m chief#########################
#basicas Axe type B70
["hatchet","Axe", [("Axt01-1",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 370 , weight(1)|difficulty(6)|spd_rtng(91) | weapon_length(67)|swing_damage(26 , cut) | thrust_damage(0 ,  pierce),imodbits_axe,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, norse and vikings
 ["axe",  "Axe", [("Axt01-2",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 370 , weight(1)|difficulty(6)|spd_rtng(92) | weapon_length(62)|swing_damage(25 , cut) | thrust_damage(0 ,  pierce),imodbits_axe,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, norse and vikings
["axe_2", "Short Axe", [("Axt01-3",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 370 , weight(1)|difficulty(6)|spd_rtng(94) | weapon_length(52)|swing_damage(23 , cut) | thrust_damage(0 ,  pierce),imodbits_axe,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, norse and vikings
["hand_axe", "Short Axe", [("Axt01-4",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 370 , weight(1)|difficulty(6)|spd_rtng(94) | weapon_length(52)|swing_damage(23 , cut) | thrust_damage(0 ,  pierce),imodbits_axe,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, norse and vikings
###con mango mas largo Axe type B80
["axe_3", "Long Axe", [("Axt03-5",0)], itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry|itp_cant_use_on_horseback|itp_penalty_with_shield, itc_morningstar|itcf_carry_axe_back, 
 480 , weight(1.7)|difficulty(9)|spd_rtng(85) | weapon_length(83)|swing_damage(30 , cut) | thrust_damage(0 ,  pierce),imodbits_axe,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, norse and vikings
 ["axe_4", "Long Axe", [("Axt03-6",0)], itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry|itp_cant_use_on_horseback|itp_penalty_with_shield, itc_morningstar|itcf_carry_axe_back, 
 480 , weight(1.7)|difficulty(9)|spd_rtng(85) | weapon_length(83)|swing_damage(30 , cut) | thrust_damage(0 ,  pierce),imodbits_axe,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #frisa, norse and vikings
 
#Axe type D Cabeza grande
#These have thrusting "horn" and were the closest things to punching weapons (the swords were thin, meant for slicing). http://www.youtube.com/watch?v=juIw20z5p0c minute 4:40
["one_handed_war_axe_a", "Short Battle Axe", [("Axt02-1",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry, itc_longsword|itcf_carry_axe_left_hip, 
 440 , weight(1.5)|difficulty(7)|spd_rtng(92) | weapon_length(61)|swing_damage(25 , cut) | thrust_damage(15 ,  pierce),imodbits_axe,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, norse and vikings
 ["one_handed_war_axe_b", "Short Battle Axe", [("Axt02-2",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry, itc_longsword|itcf_carry_axe_left_hip, 
 440 , weight(1.5)|difficulty(7)|spd_rtng(92) | weapon_length(61)|swing_damage(25 , cut) | thrust_damage(15 ,  pierce),imodbits_axe,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, norse and vikings
["one_handed_war_axe_c", "Short Battle Axe", [("Axt02-3",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry, itc_longsword|itcf_carry_axe_left_hip, 
 440 , weight(1.45)|difficulty(7)|spd_rtng(93) | weapon_length(56)|swing_damage(24 , cut) | thrust_damage(15 ,  pierce),imodbits_axe,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, norse and vikings
["one_handed_war_axe_d", "Short Battle Axe", [("Axt02-4",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry, itc_longsword|itcf_carry_axe_left_hip, 
 440 , weight(1.35)|difficulty(7)|spd_rtng(94) | weapon_length(51)|swing_damage(23 , cut) | thrust_damage(15 ,  pierce),imodbits_axe,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, norse and vikings
#palo largo Axe type D Cabeza grande
["one_handed_war_axe_e", "Long Battle Axe", [("Axt02-5",0)], itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry|itp_cant_use_on_horseback|itp_penalty_with_shield, itc_bastardsword|itcf_carry_axe_back, 
 480 , weight(1.75)|abundance(20)|difficulty(9)|spd_rtng(85) | weapon_length(81)|swing_damage(31 , cut) | thrust_damage(18 ,  pierce),imodbits_axe,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, norse and vikings
 ["one_handed_war_axe_f", "Long Battle Axe", [("Axt02-6",0)], itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry|itp_cant_use_on_horseback|itp_penalty_with_shield, itc_bastardsword|itcf_carry_axe_back, 
 520 , weight(1.75)|abundance(20)|difficulty(9)|spd_rtng(84) | weapon_length(83)|swing_damage(32 , cut) | thrust_damage(18 ,  pierce),imodbits_axe,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, norse and vikings

#Axe type A Cabeza pequena
  ["axe_5", "Long Hand Axe", [("Axt03-1",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
 390 , weight(1.35)|difficulty(7)|spd_rtng(91) | weapon_length(67)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, norse and vikings
  ["axe_6", "Hand Axe", [("Axt03-2",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
 370 , weight(1.3)|difficulty(7)|spd_rtng(92) | weapon_length(62)|swing_damage(25 , cut) | thrust_damage(0 ,  pierce),imodbits_axe,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, norse and vikings
  ["axe_7", "Short Hand Axe", [("Axt03-3",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
 360 , weight(1.3)|difficulty(7)|spd_rtng(93) | weapon_length(57)|swing_damage(24 , cut) | thrust_damage(0 ,  pierce),imodbits_axe,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, norse and vikings
  ["axe_8", "Short Hand Axe", [("Axt03-4",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
 360 , weight(1.25)|difficulty(7)|spd_rtng(94) | weapon_length(52)|swing_damage(23 , cut) | thrust_damage(0 ,  pierce),imodbits_axe,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, norse and vikings
#palo largo Axe type A Cabeza pequena
  ["axe_9", "Hand Axe", [("Axt03-5A",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
 380 , weight(1.3)|difficulty(7)|spd_rtng(92) | weapon_length(62)|swing_damage(25 , cut) | thrust_damage(0 ,  pierce),imodbits_axe,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, norse and vikings
  ["axe_10", "Big Hand Axe", [("Axt03-5B",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
 390 , weight(1.35)|abundance(40)|difficulty(7)|spd_rtng(91) | weapon_length(67)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, norse and vikings

########pictos and irsh
 #cabeza ancha + damage
 ["pictish_hatchet", "Goidelic Axe", [("Axt04-1",0)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 420 , weight(1.35)|difficulty(7)|spd_rtng(91) | weapon_length(64)|swing_damage(28 , cut) | thrust_damage(0 ,  pierce),imodbits_axe,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
 ["pictish_hatchet2", "Goidelic Axe", [("Axt04-4",0)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 420 , weight(1.2)|difficulty(6)|spd_rtng(94) | weapon_length(54)|swing_damage(24 , cut) | thrust_damage(0 ,  pierce),imodbits_axe,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
#mango largo
 ["pictish_hatchet3", "Goidelic Long Axe", [("Axt04-5",0)], itp_merchandise|itp_type_two_handed_wpn|itp_primary|itp_secondary|itp_no_blur|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_wooden_parry|itp_penalty_with_shield, itc_morningstar|itcf_carry_axe_back,
 460 , weight(1.5)|abundance(20)|difficulty(9)|spd_rtng(87) | weapon_length(84)|swing_damage(33 , cut) | thrust_damage(0 ,  pierce),imodbits_axe,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
 ["pictish_hatchet4", "Goidelic Long Axe", [("Axt04-6",0)], itp_merchandise|itp_type_two_handed_wpn|itp_primary|itp_secondary|itp_no_blur|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_wooden_parry|itp_penalty_with_shield, itc_morningstar|itcf_carry_axe_back,
 460 , weight(1.5)|abundance(20)|difficulty(9)|spd_rtng(87) | weapon_length(84)|swing_damage(33 , cut) | thrust_damage(0 ,  pierce),imodbits_axe,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops

#cabeza pesada
 ["pictish_hatchet5", "Pictish Axe", [("Axt05-1",0)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 390 , weight(1.5)|difficulty(9)|spd_rtng(90) | weapon_length(68)|swing_damage(29 , cut) | thrust_damage(0 ,  pierce),imodbits_axe,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
 ["pictish_hatchet6", "Pictish Axe", [("Axt05-2",0)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 390 , weight(1.5)|difficulty(9)|spd_rtng(91) | weapon_length(64)|swing_damage(28 , cut) | thrust_damage(0 ,  pierce),imodbits_axe,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
 ["pictish_hatchet7", "Pictish Axe", [("Axt05-3",0)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 390 , weight(1.4)|difficulty(8)|spd_rtng(92) | weapon_length(59)|swing_damage(26 , cut) | thrust_damage(0 ,  pierce),imodbits_axe,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
 ["pictish_hatchet8", "Short Pictish Axe", [("Axt05-4",0)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 390 , weight(1.4)|difficulty(8)|spd_rtng(93) | weapon_length(54)|swing_damage(24 , cut) | thrust_damage(0 ,  pierce),imodbits_axe,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
#mango largo
 ["pictish_hatchet9", "Big Pictish Axe", [("Axt05-5",0)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_back,
 420 , weight(2)|abundance(40)|difficulty(9)|spd_rtng(87) | weapon_length(73)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_axe,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
 ["pictish_hatchet10", "Big Pictish Axe", [("Axt05-6",0)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_back,
 420 , weight(2)|abundance(40)|difficulty(9)|spd_rtng(88) | weapon_length(64)|swing_damage(29 , cut) | thrust_damage(0 ,  pierce),imodbits_axe,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops

#cabeza normal
 ["pictish_hatchet11", "Goidelic Hatchet", [("Axt06-1",0)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 370 , weight(1)|difficulty(5)|spd_rtng(91) | weapon_length(68)|swing_damage(26 , cut) | thrust_damage(0 ,  pierce),imodbits_axe,
 [], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
 ["pictish_hatchet12", "Goidelic Hatchet", [("Axt06-2",0)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 370 , weight(1)|difficulty(4)|spd_rtng(92) | weapon_length(63)|swing_damage(25 , cut) | thrust_damage(0 ,  pierce),imodbits_axe,
 [], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
 ["pictish_hatchet13", "Short Goidelic Hatchet", [("Axt06-3",0)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 370 , weight(1)|difficulty(4)|spd_rtng(94) | weapon_length(53)|swing_damage(23 , cut) | thrust_damage(0 ,  pierce),imodbits_axe,
 [], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
 ["pictish_hatchet14", "Short Goidelic Hatchet", [("Axt06-4",0)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 370 , weight(1)|difficulty(4)|spd_rtng(94) | weapon_length(53)|swing_damage(23 , cut) | thrust_damage(0 ,  pierce),imodbits_axe,
 [], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
#mango largo
 ["pictish_hatchet15", "Goidelic Long Hatchet", [("Axt06-5",0)], itp_merchandise|itp_type_two_handed_wpn|itp_primary|itp_secondary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry|itp_cant_use_on_horseback|itp_penalty_with_shield, itc_morningstar|itcf_carry_axe_back,
 390 , weight(1.8)|abundance(20)|difficulty(9)|spd_rtng(87) | weapon_length(84)|swing_damage(31 , cut) | thrust_damage(0 ,  pierce),imodbits_axe,
 [], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
 ["pictish_hatchet16", "Goidelic Long Hatchet", [("Axt06-6",0)], itp_merchandise|itp_type_two_handed_wpn|itp_primary|itp_secondary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry|itp_cant_use_on_horseback|itp_penalty_with_shield, itc_morningstar|itcf_carry_axe_back,
 390 , weight(1.8)|abundance(20)|difficulty(9)|spd_rtng(87) | weapon_length(84)|swing_damage(31 , cut) | thrust_damage(0 ,  pierce),imodbits_axe,
 [], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops

#decorated (usabel for special items)
  ["pictish_hatchet17", "Noble Goidelic Axe", [("Axt04-2",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 420 , weight(1.35)|difficulty(7)|spd_rtng(91) | weapon_length(65)|swing_damage(28 , cut) | thrust_damage(0 ,  pierce),imodbits_axe,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
 ["pictish_hatchet18", "Noble Goidelic Axe", [("Axt04-3",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 420 , weight(1.3)|difficulty(7)|spd_rtng(92) | weapon_length(60)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops


#Especial AXE special smiths
 ["long_axe_b", "Woodcutter", [("Axt07",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_secondary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry|itp_cant_use_on_horseback, itc_morningstar|itcf_carry_axe_back,
  820 , weight(3.5)|difficulty(11)|spd_rtng(75) | weapon_length(110)|swing_damage(42 , cut) | thrust_damage(0 ,  pierce),imodbits_axe], 
#special smiths
["frankish_axe", "Frankish Battle Axe", [("Axt02-5",0)], itp_type_two_handed_wpn|itp_primary|itp_secondary|itp_no_blur|itp_bonus_against_shield|itp_wooden_parry|itp_penalty_with_shield|itp_cant_use_on_horseback, itc_bastardsword|itcf_carry_axe_back,
 1380 , weight(1.75)|difficulty(9)|spd_rtng(86) | weapon_length(81)|swing_damage(34 , cut) | thrust_damage(18 ,  pierce),imodbits_axe], #frisa, norse and vikings

#############hachas acaba#########################################
 ####################################################################
 

################################spears lanzas y armas de asta empiezan###########################################################
 ###########################################################################################################
###todos palos
#quarter staves were 2-3m long (-50cm TW handle)
#TODO check lengths with model #revision
["staff",         "Staff", [("wooden_staff",0)], itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_staff,
 60 , weight(3.3)|difficulty(0)|spd_rtng(85) | weapon_length(167)|swing_damage(16 , blunt) | thrust_damage(11 ,  blunt),imodbits_polearm ], #cambiado chief
["quarter_staff", "Short Staff", [("quarter_staff",0)], itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_staff,
 70 , weight(3)|difficulty(0)|spd_rtng(85) | weapon_length(151)|swing_damage(18 , blunt) | thrust_damage(12 ,  blunt),imodbits_polearm ], #cambiado chief
#campesinos base
 ["pitch_fork",         "Pitch Fork", [("pitchfork",0)], itp_merchandise|itp_type_polearm|itp_offset_lance|itp_primary|itp_secondary|itp_no_blur|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_spear,
 70 ,weight(3.5)|difficulty(0)|spd_rtng(85) | weapon_length(157)|swing_damage(15 , blunt) | thrust_damage(14,  cut), imodbit_bent|imodbit_cracked ], #chief cambiado
 ["battle_fork",         "Shepherd's Crook", [("shepherd_crook",0)], itp_merchandise|itp_type_polearm|itp_offset_lance|itp_primary|itp_secondary|itp_no_blur|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_staff,
 60 ,weight(3)|difficulty(0)|spd_rtng(85) | weapon_length(164)|swing_damage(18 , blunt) | thrust_damage(10,  blunt), imodbit_bent|imodbit_cracked ], #chief cambiado


#todos
#normal spear
#thrust damage should all be the same -- it's the same tip
 ["light_spear1",         "Light Spear", [("Spear_S_01",0)], itp_type_polearm|itp_merchandise| itp_offset_lance|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear|itcf_carry_spear,
 380 , weight(2.3)|abundance(100)|difficulty(6)|spd_rtng(95) | weapon_length(113)|swing_damage(16 , blunt) | thrust_damage(28 ,  pierce),imodbits_polearm ],
 ["light_spear2",         "Light Spear", [("Spear_S_05",0)], itp_type_polearm|itp_merchandise| itp_offset_lance|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear|itcf_carry_spear,
 380 , weight(2.3)|abundance(100)|difficulty(6)|spd_rtng(95) | weapon_length(121)|swing_damage(16 , blunt) | thrust_damage(28 ,  pierce),imodbits_polearm ],
 ["light_spear3",         "Light Spear", [("Spear_S_03",0)], itp_type_polearm|itp_merchandise| itp_offset_lance|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear|itcf_carry_spear,
 380 , weight(2.3)|abundance(100)|difficulty(6)|spd_rtng(95) | weapon_length(107)|swing_damage(16 , blunt) | thrust_damage(28,  pierce),imodbits_polearm ],
 ["light_spear4",         "Light Spear", [("Spear_S_04",0)], itp_type_polearm|itp_merchandise| itp_offset_lance|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear|itcf_carry_spear,
 380 , weight(2.3)|abundance(100)|difficulty(6)|spd_rtng(95) | weapon_length(107)|swing_damage(16 , blunt) | thrust_damage(28 ,  pierce),imodbits_polearm ],

 ["war_spear1",         "War Spear", [("Spear_M_01",0)], itp_type_polearm|itp_merchandise| itp_offset_lance|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear,
 420 , weight(2.3)|abundance(80)|difficulty(6)|spd_rtng(93) | weapon_length(153)|swing_damage(18 , blunt) | thrust_damage(29 ,  pierce),imodbits_polearm ],
 ["war_spear2",         "War Spear", [("Spear_M_03",0)], itp_type_polearm|itp_merchandise| itp_offset_lance|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear,
  420 , weight(2.3)|abundance(80)|difficulty(6)|spd_rtng(93) | weapon_length(146)|swing_damage(18 , blunt) | thrust_damage(29 ,  pierce),imodbits_polearm ],
 ["war_spear3",         "War Spear", [("Spear_M_05",0)], itp_type_polearm|itp_merchandise| itp_offset_lance|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear,
 420 , weight(2.3)|abundance(80)|difficulty(6)|spd_rtng(93) | weapon_length(162)|swing_damage(18 , blunt) | thrust_damage(29 ,  pierce),imodbits_polearm ],

 ["heavy_spear1",         "Heavy Spear", [("Spear_M_02",0)], itp_type_polearm| itp_offset_lance|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear,
 460 , weight(2.8)|abundance(60)|difficulty(8)|spd_rtng(90) | weapon_length(161)|swing_damage(20 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm ],
 ["heavy_spear2",         "Heavy Spear", [("Spear_M_04",0)], itp_type_polearm| itp_offset_lance|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear,
 460 , weight(2.8)|abundance(60)|difficulty(8)|spd_rtng(90) | weapon_length(153)|swing_damage(20 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm ],
 ["heavy_spear3",         "Heavy Spear", [("Spear_M_06",0)], itp_type_polearm| itp_offset_lance|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear,
 460 , weight(2.8)|abundance(60)|difficulty(8)|spd_rtng(90) | weapon_length(171)|swing_damage(20 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm ],

#long spear
#pikes and long staves were 3.7m max http://en.wikipedia.org/wiki/Quarterstaff
["long_light_spear1",         "Light Long Spear", [("Spear_L_01",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear,
 400 , weight(3)|abundance(100)|difficulty(6)|spd_rtng(93) | weapon_length(174)|swing_damage(16 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm ],
["long_light_spear2",         "Light Long Spear", [("Spear_L_04",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear,
 400 , weight(3)|abundance(100)|difficulty(6)|spd_rtng(93) | weapon_length(167)|swing_damage(16 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm ],

["long_war_spear1",         "Long War Spear", [("Spear_L_02",0)],itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear,
 440 , weight(3.5)|abundance(80)|difficulty(6)|spd_rtng(91) | weapon_length(193)|swing_damage(18 , blunt) | thrust_damage(28 ,  pierce),imodbits_polearm ],
["long_war_spear2",         "Long War Spear", [("Spear_L_05",0)],itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_secondary|itp_no_blur|itp_penalty_with_shield|itp_wooden_parry, itc_spear,
 440 , weight(3.5)|abundance(80)|difficulty(6)|spd_rtng(91) | weapon_length(203)|swing_damage(18 , blunt) | thrust_damage(28 ,  pierce),imodbits_polearm ],

["long_heavy_spear1",         "Heavy Long Spear", [("Spear_L_03",0)], itp_type_polearm|itp_offset_lance|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear,
 480 , weight(4)|abundance(40)|difficulty(10)|spd_rtng(88) | weapon_length(205)|swing_damage(20 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm ],
["long_heavy_spear2",         "Heavy Long Spear", [("Spear_L_06",0)], itp_type_polearm|itp_offset_lance|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear,
 480 , weight(4)|abundance(40)|difficulty(10)|spd_rtng(88) | weapon_length(188)|swing_damage(20 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm ],

#Chief new mace - spear special smiths
["new_mace","Ray", [("Spear_L_05A",0)] ,  itp_type_polearm|itp_offset_lance|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear,
 1480 , weight(4)|abundance(40)|difficulty(10)|spd_rtng(88) | weapon_length(220)|swing_damage(21 , blunt) | thrust_damage(31 ,  pierce),imodbits_polearm ],
["premium_spear1","Gungnir", [("Spear_L_05B",0)] ,  itp_type_polearm|itp_offset_lance|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear,
 1480 , weight(4)|abundance(40)|difficulty(10)|spd_rtng(88) | weapon_length(220)|swing_damage(21 , blunt) | thrust_damage(31 ,  pierce),imodbits_polearm ],

#####estandartes finales chief####
 #############################
# These are actual standards. item_add_mesh needs to be fixed by TW
["standard", "Army Standard", [("standard_to_add_mesh",0)], itp_merchandise|itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_cant_use_on_horseback, itc_greatsword, 780, abundance(15)|weight(4.3)|difficulty(2)|spd_rtng(72)|weapon_length(247)|swing_damage(16,blunt)|thrust_damage(16,blunt), imodbits_none, [
  (ti_on_init_item, [
    (store_trigger_param_1, ":agent_no"),
    (store_trigger_param_2, ":troop_no"),
    (call_script, "script_troop_agent_set_standard", ":agent_no", ":troop_no"),
    ])]],
# ["standard_dragon", "Dragon Standard", [("standard_to_add_mesh",0)], itp_merchandise|itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_cant_use_on_horseback, itc_greatsword, 780, abundance(5)|weight(4.3)|difficulty(2)|spd_rtng(85)|weapon_length(220)|swing_damage(16,blunt)|thrust_damage(16,blunt), imodbits_none, [
  # (ti_on_init_item, [
    # (store_trigger_param_1, ":agent_no"),
    # (store_trigger_param_2, ":troop_no"),
    # (call_script, "script_troop_agent_set_dragon_standard", ":agent_no", ":troop_no"),
    # ])]],
# quick fix for dragon Standard:
  ["standard_dragon","Dragon Standard", [("standard_dragon2",0)], itp_merchandise|itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_cant_use_on_horseback, itc_greatsword, 780, abundance(5)|weight(4.3)|difficulty(2)|spd_rtng(85)|weapon_length(220)|swing_damage(16,blunt)|thrust_damage(16,blunt), imodbits_none],
#####estandartes finales acaba####

 ##############################
###############lanzas chief acaba #######################################
###########################################################################
 ###########
# ["horn", "Horn", [("horn_multi",0),("bolaf",0)], itp_type_thrown |itp_primary|itp_no_pick_up_from_ground, itcf_throw_knife, 145 , weight(1.5)|difficulty(0)|spd_rtng(50) | shoot_speed(54) | thrust_damage(3 ,  cut)|max_ammo(3)|weapon_length(0),imodbits_thrown
   # ,[
      # (ti_on_weapon_attack,
	    # [
          # (play_sound,"snd_horn2"),
	  	  # (call_script, "script_apply_courage_bonus", 2),
		# ])
	# ]
 # ],
["horn","Horn",[("horn_multi",0)],itp_type_one_handed_wpn|itp_primary|itp_no_parry,0,1000,weight(2.0),0], #itcf_carry_revolver_right
["horn_multi","Horn",[("horn_multi",0),("horn_multi", ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_no_parry,0,1000,weight(2.0),0], #multi SL

##chief armas acaba#########

# SHIELDS ESCUDOS
###Shields chief############################################################
##round shields definitivos Los usamos para vikings
#pequenos sin modelo nuevo todavia
["wooden_shield", "Round Shield", [("Roundshield_01",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 239 , weight(0.8)|hit_points(100)|body_armor(0)|spd_rtng(102)|shield_width(30)|difficulty(0),imodbits_shield],
#fin de armas principio de escudos, no usado en VC

############HEAVY SHIELDS
 #VIkings
#linen face smaller
["viking_shield_round_06", "Round Shield", [("Roundshield_01",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  460 , weight(3)|hit_points(280)|body_armor(16)|spd_rtng(88)|shield_width(40),imodbits_shield,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["viking_shield_round_07", "Round Shield", [("Roundshield_02",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  460 , weight(3)|hit_points(280)|body_armor(16)|spd_rtng(88)|shield_width(40),imodbits_shield,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["viking_shield_round_10", "Round Shield", [("Roundshield_05",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  460 , weight(3)|hit_points(280)|body_armor(16)|spd_rtng(88)|shield_width(40),imodbits_shield,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["viking_shield_round_11", "Round Shield", [("Roundshield_06",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  460 , weight(3)|hit_points(280)|body_armor(16)|spd_rtng(88)|shield_width(40),imodbits_shield,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
#Reforced linen back
["viking_shield_round_08", "Round Shield", [("Roundshield_03",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  480 , weight(3.5)|hit_points(290)|body_armor(18)|spd_rtng(87)|shield_width(40),imodbits_shield,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["viking_shield_round_09", "Round Shield", [("Roundshield_04",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  480 , weight(3.5)|hit_points(290)|body_armor(18)|spd_rtng(87)|shield_width(40),imodbits_shield,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["viking_shield_round_12", "Round Shield", [("Roundshield_07",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  480 , weight(3.5)|hit_points(290)|body_armor(18)|spd_rtng(87)|shield_width(40),imodbits_shield,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["viking_shield_round_13", "Round Shield", [("Roundshield_08",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  480 , weight(3.5)|hit_points(290)|body_armor(18)|spd_rtng(87)|shield_width(40),imodbits_shield,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
#rawhide face and back
["viking_shield_round_01", "Rawhide Shield", [("Roundshield_01vc",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  530 , weight(4.5)|hit_points(310)|body_armor(20)|spd_rtng(85)|shield_width(43),imodbits_shield,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["viking_shield_round_02", "Rawhide Shield", [("Roundshield_02vc",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  530 , weight(4.5)|hit_points(310)|body_armor(20)|spd_rtng(85)|shield_width(43),imodbits_shield,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["viking_shield_round_03", "Rawhide Shield", [("Roundshield_03vc",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  530 , weight(4.5)|hit_points(310)|body_armor(20)|spd_rtng(85)|shield_width(43),imodbits_shield,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["viking_shield_round_14", "Rawhide Shield", [("Roundshield_11",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  530 , weight(4.5)|hit_points(310)|body_armor(20)|spd_rtng(85)|shield_width(43),imodbits_shield,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["viking_shield_round_15", "Rawhide Shield", [("Roundshield_12",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  530 , weight(4.5)|hit_points(310)|body_armor(20)|spd_rtng(85)|shield_width(43),imodbits_shield,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
#rawhide face
["viking_shield_round_04", "Rawhide Round Shield", [("Roundshield_04vc",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  500 , weight(4)|hit_points(300)|body_armor(19)|spd_rtng(86)|shield_width(43),imodbits_shield,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria
["viking_shield_round_05", "Rawhide Round Shield", [("Roundshield_05vc",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  500 , weight(4)|hit_points(300)|body_armor(19)|spd_rtng(86)|shield_width(43),imodbits_shield,
  [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8]], #frisa, norse and northumbria


 #saxons
#rawhide face
["viking_shield_round_16", "Rawhide Round Shield", [("Roundshield_09",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  510 , weight(4)|hit_points(310)|body_armor(18)|spd_rtng(90)|shield_width(38),imodbits_shield,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and britons
["viking_shield_round_17", "Rawhide Round Shield", [("Roundshield_10",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  510 , weight(4)|hit_points(310)|body_armor(18)|spd_rtng(90)|shield_width(38),imodbits_shield,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and britons
["viking_shield_round_18", "Rawhide Round Shield", [("Roundshield_13",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  510 , weight(4)|hit_points(310)|body_armor(18)|spd_rtng(90)|shield_width(38),imodbits_shield,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and britons
["viking_shield_round_19", "Rawhide Round Shield", [("Roundshield_14",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  510 , weight(4)|hit_points(310)|body_armor(18)|spd_rtng(90)|shield_width(38),imodbits_shield,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and britons
["viking_shield_round_20", "Rawhide Round Shield", [("Roundshield_06vc",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  510 , weight(4)|hit_points(310)|body_armor(18)|spd_rtng(90)|shield_width(38),imodbits_shield,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and britons
["viking_shield_round_21", "Rawhide Round Shield", [("Roundshield_07vc",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  510 , weight(4)|hit_points(310)|body_armor(18)|spd_rtng(90)|shield_width(38),imodbits_shield,
 [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]], #frisa, saxons and britons
 
 ##### britons
#linen face
["shield_1", "Convex Shield", [("Convexshield_01",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  580 , weight(4)|hit_points(340)|body_armor(17)|spd_rtng(90)|shield_width(35),imodbits_shield,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #britons
["shield_2", "Convex Shield", [("Convexshield_02",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  580 , weight(4)|hit_points(340)|body_armor(17)|spd_rtng(90)|shield_width(35),imodbits_shield,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #britons
["shield_3", "Convex Shield", [("Convexshield_05",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  580 , weight(4)|hit_points(340)|body_armor(17)|spd_rtng(90)|shield_width(35),imodbits_shield,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #britons
["shield_4", "Convex Shield", [("Convexshield_06",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  580 , weight(4)|hit_points(340)|body_armor(17)|spd_rtng(90)|shield_width(35),imodbits_shield,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #britons
["shield_5", "Convex Shield", [("Convexshield_09",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  580 , weight(4)|hit_points(340)|body_armor(17)|spd_rtng(90)|shield_width(35),imodbits_shield,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #britons
["shield_6", "Convex Shield", [("Convexshield_10",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  580 , weight(4)|hit_points(340)|body_armor(17)|spd_rtng(90)|shield_width(35),imodbits_shield,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #britons
["shield_6_2", "Convex Shield", [("Convexshield_11",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  580 , weight(4)|hit_points(340)|body_armor(17)|spd_rtng(90)|shield_width(35),imodbits_shield,
 [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]], #britons

#Berserkers shields
["shield_7", "Berserkr Shield", [("Berserkrshield_01",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  580 , weight(4.5)|hit_points(330)|body_armor(20)|spd_rtng(85)|shield_width(43),imodbits_shield],
["shield_8", "Berserkr Shield", [("Berserkrshield_02",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  580 , weight(4.5)|hit_points(330)|body_armor(20)|spd_rtng(85)|shield_width(43),imodbits_shield],
["shield_9", "Berserkr Shield", [("Berserkrshield_03",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  580 , weight(4.5)|hit_points(330)|body_armor(20)|spd_rtng(85)|shield_width(43),imodbits_shield],

#Shields for bandits and mercenaries
["shield_10", "Round Shield", [("Basicshield_04",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  500 , weight(4)|hit_points(300)|body_armor(19)|spd_rtng(86)|shield_width(43),imodbits_shield],
["shield_11", "Rawhide Shield", [("Basicshield_05",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  530 , weight(4.5)|hit_points(310)|body_armor(20)|spd_rtng(85)|shield_width(43),imodbits_shield],
["shield_12", "Svear Shield", [("Basicshield_06",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  530 , weight(4.5)|hit_points(310)|body_armor(20)|spd_rtng(85)|shield_width(43),imodbits_shield],
["shield_13", "Round Shield", [("Basicshield_07",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  500 , weight(4)|hit_points(300)|body_armor(19)|spd_rtng(86)|shield_width(43),imodbits_shield],
["shield_14", "Round Shield", [("Basicshield_08",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  500 , weight(4)|hit_points(300)|body_armor(19)|spd_rtng(86)|shield_width(43),imodbits_shield],
["shield_15", "Rawhide Shield", [("Basicshield_09",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  530 , weight(4.5)|hit_points(310)|body_armor(20)|spd_rtng(85)|shield_width(43),imodbits_shield],
["shield_16", "Rawhide Shield", [("Basicshield_10",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  530 , weight(4.5)|hit_points(310)|body_armor(20)|spd_rtng(85)|shield_width(43),imodbits_shield],
["shield_17", "Round Shield", [("Basicshield_11",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  500 , weight(4)|hit_points(300)|body_armor(19)|spd_rtng(86)|shield_width(43),imodbits_shield],
["shield_18", "Round Shield", [("Basicshield_14",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  500 , weight(4)|hit_points(300)|body_armor(19)|spd_rtng(86)|shield_width(43),imodbits_shield],
["shield_19", "Danish Shield", [("Basicshield_13",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  500 , weight(4)|hit_points(300)|body_armor(19)|spd_rtng(86)|shield_width(43),imodbits_shield],
["shield_20", "Northmathr Shield", [("Basicshield_12",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  500 , weight(4)|hit_points(300)|body_armor(19)|spd_rtng(86)|shield_width(43),imodbits_shield],
#
["shield_21", "Round Shield", [("Basicshield_03",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  500 , weight(4)|hit_points(300)|body_armor(19)|spd_rtng(86)|shield_width(43),imodbits_shield],
 
##irish round shield big (viking type)
 ["gael_bigroundshield_01", "Gael Round Shield", [("Gael_BigRoundshield_01",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  490 , weight(3.5)|hit_points(300)|body_armor(17)|spd_rtng(92)|shield_width(35),imodbits_shield,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish  shops
 ["gael_bigroundshield_02", "Gael Round Shield", [("Gael_BigRoundshield_02",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  490 , weight(3.5)|hit_points(300)|body_armor(17)|spd_rtng(92)|shield_width(35),imodbits_shield,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish  shops
 ["gael_bigroundshield_03", "Gael Round Shield", [("Gael_BigRoundshield_03",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  490 , weight(3.5)|hit_points(300)|body_armor(17)|spd_rtng(92)|shield_width(35),imodbits_shield,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish  shops
 ["gael_bigroundshield_04", "Gael Round Shield", [("Gael_BigRoundshield_04",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  490 , weight(3.5)|hit_points(300)|body_armor(17)|spd_rtng(92)|shield_width(35),imodbits_shield,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish  shops
 ["gael_bigroundshield_05", "Gael Round Shield", [("Gael_BigRoundshield_05",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  490 , weight(3.5)|hit_points(300)|body_armor(17)|spd_rtng(92)|shield_width(35),imodbits_shield,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish  shops
 ["gael_bigroundshield_06", "Gael Round Shield", [("Gael_BigRoundshield_06",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  490 , weight(3.5)|hit_points(300)|body_armor(17)|spd_rtng(92)|shield_width(35),imodbits_shield,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish  shops
 ["gael_bigroundshield_07", "Gael Round Shield", [("Roundshield_08vc",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  490 , weight(3.5)|hit_points(300)|body_armor(17)|spd_rtng(92)|shield_width(35),imodbits_shield,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_21]], #irish  shops
#####

 #comunes
###escudos especiales
 ["elf_shield", "Elf's Shield", [("Convexshield_10",0)], itp_unique|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  880 , weight(4)|hit_points(380)|body_armor(20)|spd_rtng(90)|shield_width(35),imodbits_shield], #britons

#model to deprecate
["tab_shield_round_c", "Painted Convex Shield", [("Convexshield_11_tab_nodevice",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  580 , weight(4)|hit_points(340)|body_armor(17)|spd_rtng(90)|shield_width(35),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_vc_round_shield_11_nodevice", ":agent_no", ":troop_no")])]],

#stats all the same, just meshes/tableaux are different
#although convex shields should be at least 4x stronger and even more expensive than round (but one can't attack with them) http://www.youtube.com/watch?v=DJjZbVBkwSc
#saxons and angles
["tab_shield_round_01_device", "Painted Round Shield", [("Roundshield_01_tab_device",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  510 , weight(4)|hit_points(310)|body_armor(18)|spd_rtng(90)|shield_width(38),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_vc_round_shield_01_device", ":agent_no", ":troop_no")])]],
["tab_shield_round_01_nodevice", "Painted Round Shield", [("Roundshield_01_tab_nodevice",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  510 , weight(4)|hit_points(310)|body_armor(18)|spd_rtng(90)|shield_width(38),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_vc_round_shield_01_nodevice", ":agent_no", ":troop_no")])]],
["tab_shield_round_02_device", "Painted Round Shield", [("Roundshield_02_tab_device",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  510 , weight(4)|hit_points(310)|body_armor(18)|spd_rtng(90)|shield_width(38),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_vc_round_shield_02_device", ":agent_no", ":troop_no")])]],
["tab_shield_round_02_nodevice", "Painted Round Shield", [("Roundshield_02_tab_nodevice",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  510 , weight(4)|hit_points(310)|body_armor(18)|spd_rtng(90)|shield_width(38),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_vc_round_shield_02_nodevice", ":agent_no", ":troop_no")])]],
["tab_shield_round_03_device", "Painted Round Shield", [("Roundshield_03_tab_device",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  510 , weight(4)|hit_points(310)|body_armor(18)|spd_rtng(90)|shield_width(38),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_vc_round_shield_03_device", ":agent_no", ":troop_no")])]],
["tab_shield_round_03_nodevice", "Painted Round Shield", [("Roundshield_03_tab_nodevice",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  510 , weight(4)|hit_points(310)|body_armor(18)|spd_rtng(90)|shield_width(38),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_vc_round_shield_03_nodevice", ":agent_no", ":troop_no")])]],
#vikings
["tab_shield_round_04_device", "Painted Round Shield", [("Roundshield_04_tab_device",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  530 , weight(4.5)|hit_points(310)|body_armor(20)|spd_rtng(85)|shield_width(43),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_vc_round_shield_04_device", ":agent_no", ":troop_no")])]],
["tab_shield_round_04_nodevice", "Painted Round Shield", [("Roundshield_04_tab_nodevice",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  530 , weight(4.5)|hit_points(310)|body_armor(20)|spd_rtng(85)|shield_width(43),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_vc_round_shield_04_nodevice", ":agent_no", ":troop_no")])]],
#britons
["tab_shield_round_05_device", "Painted Convex Shield", [("Convexshield_05_tab_device",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  580 , weight(4)|hit_points(340)|body_armor(17)|spd_rtng(90)|shield_width(35),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_vc_round_shield_05_device", ":agent_no", ":troop_no")])], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]],
["tab_shield_round_05_nodevice", "Painted Convex Shield", [("Convexshield_05_tab_nodevice",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  580 , weight(4)|hit_points(340)|body_armor(17)|spd_rtng(90)|shield_width(35),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_vc_round_shield_05_nodevice", ":agent_no", ":troop_no")])], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]],
["tab_shield_round_06_device", "Painted Convex Shield", [("Convexshield_06_tab_device",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  580 , weight(4)|hit_points(340)|body_armor(17)|spd_rtng(90)|shield_width(35),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_vc_round_shield_06_device", ":agent_no", ":troop_no")])], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]],
["tab_shield_round_06_nodevice", "Painted Convex Shield", [("Convexshield_06_tab_nodevice",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  580 , weight(4)|hit_points(340)|body_armor(17)|spd_rtng(90)|shield_width(35),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_vc_round_shield_06_nodevice", ":agent_no", ":troop_no")])], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]],
#vikings
["tab_shield_round_07_device", "Painted Round Shield", [("Roundshield_07_tab_device",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  530 , weight(4.5)|hit_points(310)|body_armor(20)|spd_rtng(85)|shield_width(43),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_vc_round_shield_07_device", ":agent_no", ":troop_no")])]],
["tab_shield_round_07_nodevice", "Painted Round Shield", [("Roundshield_07_tab_nodevice",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  530 , weight(4.5)|hit_points(310)|body_armor(20)|spd_rtng(85)|shield_width(43),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_vc_round_shield_07_nodevice", ":agent_no", ":troop_no")])]],
#britons
["tab_shield_round_08_device", "Painted Convex Shield", [("Convexshield_08_tab_device",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  580 , weight(4)|hit_points(340)|body_armor(17)|spd_rtng(90)|shield_width(35),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_vc_round_shield_08_device", ":agent_no", ":troop_no")])], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]],
["tab_shield_round_08_nodevice", "Painted Convex Shield", [("Convexshield_08_tab_nodevice",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  580 , weight(4)|hit_points(340)|body_armor(17)|spd_rtng(90)|shield_width(35),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_vc_round_shield_08_nodevice", ":agent_no", ":troop_no")])], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]],
#vikings
["tab_shield_round_09_device", "Painted Round Shield", [("Roundshield_09_tab_device",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  530 , weight(4.5)|hit_points(310)|body_armor(20)|spd_rtng(85)|shield_width(43),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_vc_round_shield_09_device", ":agent_no", ":troop_no")])]],
["tab_shield_round_09_nodevice", "Painted Round Shield", [("Roundshield_09_tab_nodevice",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  530 , weight(4.5)|hit_points(310)|body_armor(20)|spd_rtng(85)|shield_width(43),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_vc_round_shield_09_nodevice", ":agent_no", ":troop_no")])]],
#britons
["tab_shield_round_10_device", "Painted Convex Shield", [("Convexshield_10_tab_device",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  580 , weight(4)|hit_points(340)|body_armor(17)|spd_rtng(90)|shield_width(35),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_vc_round_shield_10_device", ":agent_no", ":troop_no")])], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]],
["tab_shield_round_10_nodevice", "Painted Convex Shield", [("Convexshield_10_tab_nodevice",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  580 , weight(4)|hit_points(340)|body_armor(17)|spd_rtng(90)|shield_width(35),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_vc_round_shield_10_nodevice", ":agent_no", ":troop_no")])], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]],
["tab_shield_round_11_device", "Painted Convex Shield", [("Convexshield_11_tab_device",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  580 , weight(4)|hit_points(340)|body_armor(17)|spd_rtng(90)|shield_width(35),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_vc_round_shield_11_device", ":agent_no", ":troop_no")])], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]],
["tab_shield_round_11_nodevice", "Painted Convex Shield", [("Convexshield_11_tab_nodevice",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  580 , weight(4)|hit_points(340)|body_armor(17)|spd_rtng(90)|shield_width(35),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_vc_round_shield_11_nodevice", ":agent_no", ":troop_no")])], [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_8]],
#vkings
["tab_shield_round_12_device", "Painted Round Shield", [("Roundshield_12_tab_device",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  530 , weight(4.5)|hit_points(310)|body_armor(20)|spd_rtng(85)|shield_width(43),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_vc_round_shield_12_device", ":agent_no", ":troop_no")])]],
["tab_shield_round_12_nodevice", "Painted Round Shield", [("Roundshield_12_tab_nodevice",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  530 , weight(4.5)|hit_points(310)|body_armor(20)|spd_rtng(85)|shield_width(43),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_vc_round_shield_12_nodevice", ":agent_no", ":troop_no")])]],

##Heavy shields acaba #######
####escudos ligeros
 

 ["tab_shield_small_round_c", "Small Round Shield", [("round_small_01",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
 320 , weight(1.5)|hit_points(200)|body_armor(13)|spd_rtng(98)|shield_width(25),imodbits_shield,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops

###michael this dont work, you need to add tab small round shields.
 
##["tab_shield_small_round_c", "Painted Small Round Shield", [("round_small_03_tab_nodevice",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
## 220 , weight(1.5)|hit_points(200)|body_armor(13)|spd_rtng(98)|shield_width(25),imodbits_shield,
## [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "round_small_03_tab_nodevice", ":agent_no", ":troop_no")])]], #chief cambiado

###small round shields pictish and irish seguir
 ["small_roundsh1", "Small Round Shield", [("round_small_01",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
 320 , weight(1.5)|hit_points(200)|body_armor(13)|spd_rtng(98)|shield_width(25),imodbits_shield,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
 ["small_roundsh2", "Small Round Shield", [("round_small_02",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
 320 , weight(1.5)|hit_points(200)|body_armor(13)|spd_rtng(98)|shield_width(25),imodbits_shield,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
 ["small_roundsh3", "Small Round Shield", [("round_small_03",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
 320 , weight(1.5)|hit_points(200)|body_armor(13)|spd_rtng(98)|shield_width(25),imodbits_shield,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
 ["small_roundsh4", "Small Round Shield", [("round_small_04",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
 320 , weight(1.5)|hit_points(200)|body_armor(13)|spd_rtng(98)|shield_width(25),imodbits_shield,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
 ["small_roundsh5", "Small Round Shield", [("round_small_05",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
 320 , weight(1.5)|hit_points(200)|body_armor(13)|spd_rtng(98)|shield_width(25),imodbits_shield,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops
 ["small_roundsh6", "Small Round Shield", [("round_small_06",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
 320 , weight(1.5)|hit_points(200)|body_armor(13)|spd_rtng(98)|shield_width(25),imodbits_shield,
[], [fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_20, fac_kingdom_21]], #irish and pictish shops

#small H shields pictish only
 ["h_shield1", "H Shield", [("Hshaped_01",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
 380 , weight(2)|hit_points(240)|body_armor(14)|spd_rtng(96)|shield_width(30),imodbits_shield,
[], [fac_kingdom_20]],
 ["h_shield2", "H Shield", [("Hshaped_02",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
 380 , weight(2)|hit_points(240)|body_armor(14)|spd_rtng(96)|shield_width(30),imodbits_shield,
[], [fac_kingdom_20]],
 ["h_shield3", "H Shield", [("Hshaped_03",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
 380 , weight(2)|hit_points(240)|body_armor(14)|spd_rtng(96)|shield_width(30),imodbits_shield,
[], [fac_kingdom_20]],
 ["h_shield4", "H Shield", [("Hshaped_04",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
 380 , weight(2)|hit_points(240)|body_armor(14)|spd_rtng(96)|shield_width(30),imodbits_shield,
[], [fac_kingdom_20]],
 ["h_shield5", "H Shield", [("Hshaped_05",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
 380 , weight(2)|hit_points(240)|body_armor(14)|spd_rtng(96)|shield_width(30),imodbits_shield,
[], [fac_kingdom_20]],
 ["h_shield6", "H Shield", [("Hshaped_06",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
 380 , weight(2)|hit_points(240)|body_armor(14)|spd_rtng(96)|shield_width(30),imodbits_shield,
[], [fac_kingdom_20]],

#square shield pictish only
 ["squaresh_1", "Square Shield", [("Square_01",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
 360 , weight(2)|hit_points(220)|body_armor(15)|spd_rtng(95)|shield_width(33),imodbits_shield,
[], [fac_kingdom_20]],
 ["squaresh_2", "Square Shield", [("Square_02",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
 360 , weight(2)|hit_points(220)|body_armor(15)|spd_rtng(95)|shield_width(33),imodbits_shield,
[], [fac_kingdom_20]],
 ["squaresh_3", "Square Shield", [("Square_03",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
 360 , weight(2)|hit_points(220)|body_armor(15)|spd_rtng(95)|shield_width(33),imodbits_shield,
[], [fac_kingdom_20]],
 ["squaresh_4", "Square Shield", [("Square_04",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
 360 , weight(2)|hit_points(220)|body_armor(15)|spd_rtng(95)|shield_width(33),imodbits_shield,
[], [fac_kingdom_20]],
 ["squaresh_5", "Square Shield", [("Square_05",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
 360 , weight(2)|hit_points(220)|body_armor(15)|spd_rtng(95)|shield_width(33),imodbits_shield,
[], [fac_kingdom_20]],
 ["squaresh_6", "Square Shield", [("Square_06",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
 360 , weight(2)|hit_points(220)|body_armor(15)|spd_rtng(95)|shield_width(33),imodbits_shield,
[], [fac_kingdom_20]],

 
################chief shields acaban############################
 #RANGED
#TODO:
#jabalina basica #no used
["darts",         "Simple Javelins", [("javelin",0),("javelin_carry", ixmesh_carry)], itp_type_thrown |itp_primary|itp_secondary|itp_bonus_against_shield|itp_next_item_as_melee ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 
200, weight(2)|difficulty(1)|spd_rtng(85) | shoot_speed(28) | thrust_damage(15 ,  pierce)|max_ammo(4)|weapon_length(65)|accuracy(99),imodbits_thrown ,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19, fac_kingdom_10, fac_kingdom_11]],
["darts_melee",         "Simple Javelins", [("javelin",0)], itp_type_polearm|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry , itc_jav_melee, 
200, weight(1)|difficulty(0)|spd_rtng(90) |swing_damage(11, blunt)| thrust_damage(15,  pierce)|weapon_length(65),imodbits_polearm ], #chief cambiado

###jabalinas infanteria ligera 4 u
["javelin",         "Javelins", [("javelin",0),("javelin_carry", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_next_item_as_melee ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 
200, weight(1)|difficulty(1)|spd_rtng(90) | shoot_speed(28) | thrust_damage(16 ,  pierce)|max_ammo(4)|weapon_length(65)|accuracy(99),imodbits_thrown ], #chief cambiado max_ammo
["javelin_melee",         "Javelin", [("javelin",0)], itp_type_polearm|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry , itc_jav_melee, 
200, weight(1)|difficulty(0)|spd_rtng(90) |swing_damage(11, blunt)| thrust_damage(17,  pierce)|weapon_length(65),imodbits_polearm ], #chief cambiado
##skirmish javelin
["javelin_skirmishes",         "Skirmish Javelins", [("javelin",0),("javelin_carry", ixmesh_carry)], itp_type_thrown |itp_primary|itp_secondary|itp_bonus_against_shield|itp_next_item_as_melee ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 
250, weight(2)|difficulty(1)|spd_rtng(90) | shoot_speed(28) | thrust_damage(18 ,  pierce)|max_ammo(6)|weapon_length(65)|accuracy(99),imodbits_thrown ], #chief cambiado max_ammo
["javelin_skirmishes_melee",         "Skirmish Javelin", [("javelin",0)], itp_type_polearm|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry , itc_jav_melee, 
250, weight(2)|difficulty(0)|spd_rtng(90) |swing_damage(11, blunt)| thrust_damage(17,  pierce)|weapon_length(65),imodbits_polearm ], #chief cambiado
##skirmishes irish and pictish 6-8 u
["javelin_skirmishesel",         "Heavy Javelins", [("javelin2",0),("javelin2_carry", ixmesh_carry)], itp_type_thrown |itp_primary|itp_secondary|itp_bonus_against_shield|itp_next_item_as_melee ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 
350, weight(3)|difficulty(1)|spd_rtng(90) | shoot_speed(28) | thrust_damage(20 ,  pierce)|max_ammo(8)|weapon_length(65)|accuracy(99),imodbits_thrown ], #chief cambiado max_ammo
["javelin_skirmishesel_melee",         "Heavy Javelin", [("javelin2",0)], itp_type_polearm|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry , itc_jav_melee, 
350, weight(3)|difficulty(0)|spd_rtng(90) |swing_damage(11, blunt)| thrust_damage(17,  pierce)|weapon_length(65),imodbits_polearm ], #chief cambiado
#jabalinas para jinetes ligeros 12 u
["javelin_jinetes",         "Horsemen Javelins", [("javelin2",0),("javelin2_carry", ixmesh_carry)], itp_type_thrown |itp_primary|itp_secondary|itp_bonus_against_shield|itp_next_item_as_melee ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 
400, weight(4)|difficulty(1)|spd_rtng(90) | shoot_speed(28) | thrust_damage(18 ,  pierce)|max_ammo(12)|weapon_length(65)|accuracy(99),imodbits_thrown ], #chief cambiado max_ammo
["javelin_jinetes_melee",         "Horseman Javelin", [("javelin2",0)], itp_type_polearm|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry , itc_jav_melee, 
400, weight(4)|difficulty(0)|spd_rtng(90) |swing_damage(11, blunt)| thrust_damage(17,  pierce)|weapon_length(65),imodbits_polearm ], #chief cambiado
#lanzas lanzables para infanteria pesada
["throwing_spears",         "Throwing Spears", [("Spear_S_02",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_next_item_as_melee ,itcf_throw_javelin, 
425 , weight(2)|difficulty(2)|spd_rtng(85) | shoot_speed(18) | thrust_damage(27 ,  pierce)|max_ammo(2)|weapon_length(113)|accuracy(99),imodbits_thrown ], #cambiado chief
["throwing_spear_melee",         "Throwing Spear", [("Spear_S_02",0)],itp_type_polearm|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry , itc_jav_melee, 
425 , weight(2)|difficulty(2)|spd_rtng(85) | swing_damage(10, blunt) | thrust_damage(24 ,  pierce)|weapon_length(113),imodbits_thrown ], #cambiado chief
["throwing_spears2",         "Throwing Spears", [("Spear_S_06",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_next_item_as_melee ,itcf_throw_javelin, 
425 , weight(2)|difficulty(2)|spd_rtng(88) | shoot_speed(18) | thrust_damage(27 ,  pierce)|max_ammo(2)|weapon_length(110)|accuracy(99),imodbits_thrown ], #cambiado chief
["throwing_spear2_melee",         "Throwing Spear", [("Spear_S_06",0)],itp_type_polearm|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry , itc_jav_melee, 
425 , weight(2)|difficulty(2)|spd_rtng(88) | swing_damage(10, blunt) | thrust_damage(24 ,  pierce)|weapon_length(110),imodbits_thrown ], #cambiado chief

#TODO:
#TODO: Heavy throwing Spear
["stones",         "Stones", [("throwing_stone",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_secondary ,itcf_throw_stone,
 5 , weight(1)|difficulty(0)|spd_rtng(95) | shoot_speed(20) | thrust_damage(9 ,  blunt)|max_ammo(8)|weapon_length(8),imodbit_large_bag ], #chief cambiado

##################chief finales arcos empieza##############################################
########################################################################################### 
#item quality change difficult, so a bow with difficult 4 can be 5 depend on quality. This mean that archers with p_draw 4 couldnt use it. 
["long_bow",         "Long Bow", [("LongBow",0),("LongBow_carry",ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_secondary|itp_two_handed|itp_cant_use_on_horseback ,itcf_shoot_bow|itcf_carry_bow_back, 
630 , weight(1)|abundance(60)|difficulty(2)|spd_rtng(65) | shoot_speed(55) | thrust_damage(24 ,  cut)|accuracy(95),imodbits_bow ],
["long_bow2",         "Elite Long Bow", [("LongBow150",0),("LongBow150_carry",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_primary|itp_secondary|itp_cant_use_on_horseback|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back,
830 , weight(1.25)|abundance(20)|difficulty(3)|spd_rtng(62) | shoot_speed(58) | thrust_damage(27 ,  cut)|accuracy(95),imodbits_bow ],
["long_bow3",         "Featured Long Bow", [("LongBow200",0),("LongBow200_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_secondary|itp_cant_use_on_horseback|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back,
930 , weight(1.25)|difficulty(4)|spd_rtng(60) | shoot_speed(61) | thrust_damage(28 ,  cut)|accuracy(95),imodbits_bow ],

["hunting_crossbow", "Pictish Crossbow", [("crossbow",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_secondary|itp_cant_use_on_horseback|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
750 , weight(2.25)|abundance(40)|difficulty(0)|spd_rtng(45) | shoot_speed(66) | thrust_damage(55 ,  pierce)|max_ammo(1)|accuracy(85),imodbits_crossbow, [], [fac_kingdom_20]], #chief cambiado #crossbow is quite easy to use, you need only strengh, it isnt likw bow.

###ARCOS ESPECIALES heroes
 ["strong_bow",         "Dark Hunter", [("LongBow200",0),("LongBow200_carry", ixmesh_carry)], itp_type_bow |itp_primary|itp_secondary|itp_cant_use_on_horseback|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back,
1230 , weight(1.25)|difficulty(5)|spd_rtng(55) | shoot_speed(63) | thrust_damage(31 ,  cut)|accuracy(95),imodbits_bow ],
["war_bow",         "Eye-popping", [("LongBow200",0),("LongBow200_carry",ixmesh_carry)],itp_type_bow |itp_primary|itp_secondary|itp_cant_use_on_horseback|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back,
1230 , weight(1.25)|difficulty(5)|spd_rtng(55) | shoot_speed(63) | thrust_damage(31 ,  cut)|accuracy(95),imodbits_bow ],
 
#sling rocks chief
["sling_rock1", "Sling Rocks", [("throwing_stone",0),("throwing_stone",ixmesh_flying_ammo)],
  itp_type_bullets|itp_default_ammo|itp_merchandise, 0, 15,weight(0.5)|abundance(90)|weapon_length(3)|thrust_damage(1,blunt)|max_ammo(30),imodbit_large_bag],
["sling_lead", "Sling Lead", [("throwing_stone",0),("throwing_stone",ixmesh_flying_ammo)],
  itp_type_bullets|itp_merchandise, 0, 650,weight(0.7)|abundance(13)|weapon_length(3)|thrust_damage(10,blunt)|max_ammo(20),imodbit_large_bag],
#sling chief
["sling", "Sling", [("Sling4",0)],
 itp_type_pistol |itp_merchandise|itp_primary|itp_secondary|itp_cant_use_on_horseback ,itcf_shoot_pistol,
 50, weight(0.5)|difficulty(0)|spd_rtng(85) | shoot_speed(55) | thrust_damage(24 ,blunt)|max_ammo(1)|accuracy(90),imodbits_none, [(ti_on_weapon_attack, [(play_sound,"snd_throw_stone")])]],
["sling2", "Sling", [("Sling",0)],
 itp_type_pistol |itp_merchandise|itp_primary|itp_secondary|itp_cant_use_on_horseback ,itcf_shoot_pistol,
 50, weight(0.5)|difficulty(0)|spd_rtng(85) | shoot_speed(55) | thrust_damage(24 ,blunt)|max_ammo(1)|accuracy(90),imodbits_none, [(ti_on_weapon_attack, [(play_sound,"snd_throw_stone")])]],
["sling3", "Sling", [("Sling3",0)],
 itp_type_pistol |itp_merchandise|itp_primary|itp_secondary|itp_cant_use_on_horseback ,itcf_shoot_pistol,
 50, weight(0.5)|difficulty(0)|spd_rtng(85) | shoot_speed(55) | thrust_damage(24 ,blunt)|max_ammo(1)|accuracy(90),imodbits_none, [(ti_on_weapon_attack, [(play_sound,"snd_throw_stone")])]],
["sling_militar", "Military Sling", [("Sling2",0)],
 itp_type_pistol |itp_merchandise|itp_primary|itp_secondary|itp_cant_use_on_horseback ,itcf_shoot_pistol,
 140, weight(0.5)|abundance(10)|difficulty(0)|spd_rtng(87) | shoot_speed(57) | thrust_damage(25 ,blunt)|max_ammo(1)|accuracy(92),imodbits_none, [(ti_on_weapon_attack, [(play_sound,"snd_throw_stone")])]],

["fustibalus1", "Fustibalus", [("Staf_Sling_fustibalus_1",0)],
 itp_type_pistol |itp_merchandise|itp_primary|itp_secondary|itp_cant_use_on_horseback ,itcf_shoot_musket,
 180, weight(1)|abundance(50)|difficulty(0)|spd_rtng(80) | shoot_speed(58) | thrust_damage(27 ,blunt)|max_ammo(1)|accuracy(90),imodbits_none, [(ti_on_weapon_attack, [(play_sound,"snd_throw_stone")])]],
["fustibalus2", "Fustibalus", [("Staf_Sling_fustibalus_2",0)],
 itp_type_pistol |itp_merchandise|itp_primary|itp_secondary|itp_cant_use_on_horseback ,itcf_shoot_musket,
 180, weight(1)|abundance(50)|difficulty(0)|spd_rtng(80) | shoot_speed(58) | thrust_damage(27 ,blunt)|max_ammo(1)|accuracy(90),imodbits_none, [(ti_on_weapon_attack, [(play_sound,"snd_throw_stone")])]],
##["fustibalus3", "Military Fustibalus", [("Staf_Sling_fustibalus_4",0)],
## itp_type_pistol |itp_merchandise|itp_primary|itp_cant_use_on_horseback ,itcf_shoot_musket, 110, weight(1)|difficulty(0)|spd_rtng(70) | shoot_speed(75) | thrust_damage(23 ,blunt)|max_ammo(1)|accuracy(90),imodbits_none, [(ti_on_weapon_attack, [(play_sound,"snd_throw_stone")])]],
["fustibalus_military", "Military Fustibalus", [("Staf_Sling_fustibalus_3",0)],
 itp_type_pistol |itp_merchandise|itp_primary|itp_secondary|itp_cant_use_on_horseback ,itcf_shoot_musket,
 430, weight(1)|abundance(10)|difficulty(0)|spd_rtng(85) | shoot_speed(62) | thrust_damage(29 ,blunt)|max_ammo(1)|accuracy(90),imodbits_none, [(ti_on_weapon_attack, [(play_sound,"snd_throw_stone")])]],

##
["torch",         "Torches", [("wooden_stick",0)], itp_type_one_handed_wpn |itp_primary | itp_force_attach_left_hand , 0,
 41 , weight(5)|difficulty(0)|spd_rtng(99) | shoot_speed(20) | thrust_damage(15,blunt)|max_ammo(5)|weapon_length(53),imodbits_none,
 [(ti_on_init_item, [(set_position_delta,0,60,0),(particle_system_add_new, "psys_torch_fire"),(particle_system_add_new, "psys_torch_smoke"),(set_current_color,150*1.5, 130*1.5, 70*1.5),(add_point_light, 10, 30),]),
 ]], 

# ["torch2",         "Torch", [("club",0)], itp_type_thrown|itp_primary|itp_wooden_parry|itp_wooden_attack ,itc_scimitar, 0 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(11 , blunt) | thrust_damage(0 ,  pierce),imodbits_none,
 # [(ti_on_init_item, [(set_position_delta,0,60,0),(particle_system_add_new, "psys_torch_fire"),(particle_system_add_new, "psys_torch_smoke"),(set_current_color,150, 130, 70),(add_point_light, 10, 30),]),
 # ]],
###########################proyectiles acaba chief####################################
 ####################################################################################


 ["lyre", "Lyre", [("lyre",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_wooden_parry|itp_wooden_attack, itc_scimitar|itcf_carry_sword_back,
  218 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(71)|swing_damage(12 , blunt) | thrust_damage(0 ,  pierce),imodbits_club ], #chief cambiado
 ["lute", "Lute", [("lute",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_wooden_parry|itp_wooden_attack, itc_scimitar|itcf_carry_sword_back,
  218 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(71)|swing_damage(12 , blunt) | thrust_damage(0 ,  pierce),imodbits_club ], #chief cambiado
 ["instruments_end", "Instruments End", [("lute",0)], 0, 0, 1, 0, 0],

#bebe, hijo de player
#["baby",         "Baby", [("baby",0)], itp_always_loot|itp_type_goods, 0, 255,weight(50)|abundance(120),imodbits_none],

#chief unique
["court_dress", "Court Dress", [("court_dress",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0,
 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
#chief unique acaba

#################especiales chief#############################################
###piedra para asedio chief Siege warfare
["stones_siege",         "Siege Stones", [("siegestone",0)], itp_type_thrown |itp_unique|itp_primary ,itcf_throw_stone, 10 , weight(3)|difficulty(4)|spd_rtng(70) | shoot_speed(14) | thrust_damage(28 ,  blunt)|max_ammo(5)|weapon_length(14),imodbits_none, #chief cambiado
[
    (ti_on_missile_hit,
      [
	  (try_begin),
		#Solid Round Script
        #pos1 - Missile hit position
        #param_1 - Shooter agent
		(this_or_next|multiplayer_is_server),
		(neg|game_in_multiplayer_mode),		
		(store_trigger_param_1,":shooter"),
    (set_fixed_point_multiplier, 100),
		(copy_position, pos63, pos1),
		(particle_system_burst,"psys_piedra_dust",pos1,1),
		(try_for_agents,":agent",pos63,100),
      (neg|agent_is_ally,":agent"),
      (agent_is_active,":agent"),
      (agent_is_alive,":agent"),
      (neq,":agent",":shooter"),				   
      (agent_deliver_damage_to_agent,":shooter",":agent"),
			(play_sound,"snd_shield_broken"),
		(try_end),
		(try_end),
]),
]],
 
#Otros, cuerno####

####trofeos de batalla chief
  ["trophy_a","Battle Trophy", [("standard_dragon1",0)], itp_type_goods|itp_always_loot, 0, 210,weight(3)|abundance(90),imodbits_none],
  ["trophy_b","War Trophy", [("horn_multi",0)], itp_type_goods|itp_always_loot, 0, 410,weight(7)|abundance(90),imodbits_none],
  ["trophy_c","Epic Trophy", [("vc_gold_trophy",0)], itp_type_goods|itp_always_loot, 0, 610,weight(10)|abundance(90),imodbits_none],
##chief begin
 ["iniauhorn",         "Iniau Horn", [("horn_multi",0)], itp_type_goods, 0, 255,weight(50)|abundance(120),imodbits_none],
############3
 ##################
#################especiales chief acaba ################################

####OTROS chief ##################################
["tunic_with_green_cape", "Tunic", [("Tunic_Saxon_02B",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 80 , weight(0.5)|abundance(100)|head_armor(0)|body_armor(3)|leg_armor(1), imodbits_cloth ], #cambiado chief
["keys", "Ring of Keys", [("throwing_axe_a",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,
240, weight(5)|spd_rtng(98) | swing_damage(29,cut)|max_ammo(5)|weapon_length(53),imodbits_thrown ], 
["bride_dress", "Bride Dress", [("bride_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["bride_crown", "Crown of Flowers", [("bride_crown",0)],  itp_type_head_armor | itp_doesnt_cover_hair |itp_civilian |itp_attach_armature,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["bride_shoes", "Bride Shoes", [("bride_shoes",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 30 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
###items used in tutorial
["practice_bow_2","Long Bow", [("LongBow",0),("LongBow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 
530 , weight(1)|difficulty(0)|spd_rtng(90) | shoot_speed(50) | thrust_damage(20 ,  pierce)|accuracy(99),imodbits_bow ],
["practice_arrows_2","Arrows", [("arrow",0),("flying_arrow",ixmesh_flying_ammo),("quiver3", ixmesh_carry)], itp_type_arrows|itp_default_ammo, itcf_carry_bowcase_left,
  100,weight(2)|abundance(110)|weapon_length(95)|thrust_damage(1,pierce)|max_ammo(40),imodbits_missile],
###
#cuerno multiplayer chief
["steel_bolts",         "Siege Stones", [("siegestone",0)], itp_type_thrown |itp_primary ,itcf_throw_stone, 10 , weight(4)|difficulty(0)|spd_rtng(60) | shoot_speed(8) | thrust_damage(25 ,  blunt)|max_ammo(3)|weapon_length(14),imodbits_none, #chief cambiado
[
(ti_on_missile_hit,
  [
      (try_begin),
            #Solid Round Script
    #pos1 - Missile hit position
    #param_1 - Shooter agent
       #     (multiplayer_is_server),
            #(neg|game_in_multiplayer_mode),		
            (store_trigger_param_1,":shooter"),
    (set_fixed_point_multiplier, 100),
            (copy_position, pos63, pos1),
           ## (particle_system_burst,"psys_piedra_dust",pos1,1),#activar si se habilita
            (try_for_agents,":agent",pos63,100),
                            (neg|agent_is_ally,":agent"),
                            (agent_is_active,":agent"),
                            (agent_is_alive,":agent"),
                            (neq,":agent",":shooter"),				   
#				(agent_set_hit_points,":agent",0,1),#insta-death
                            (agent_deliver_damage_to_agent,":shooter",":agent"),
                             #(multiplayer_send_int_to_server,multiplayer_event_sound_at_player, "snd_shield_broken"),
                    (play_sound,"snd_shield_broken"),
            (try_end),
            (try_end),
]), 
 ]],



#chief unique
["heraldic_mail_with_tunic_b", "Shirt", [("Tunic_Norse_12",0)], itp_unique|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 400 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(15)|leg_armor(2), imodbits_cloth],
["heraldic_mail_with_tabard", "Shirt",[("Tunic_Norse_12",0)], itp_unique|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 400 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(15)|leg_armor(2), imodbits_cloth],




##MP Thor's Champion
["thors_helmet", "Thor's Helmet", [("Broa",0)],itp_type_head_armor|itp_fit_to_head,0,
 2000,weight(1.5)|head_armor(45),0],
["thors_armor", "Thor's Armor", [("thor_armor",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 5000,weight(15)|body_armor(60)|leg_armor(25),0],
["thors_boots", "Thor's Boots", [("Trouser38",0)],itp_type_foot_armor|itp_attach_armature,0,
 2000,weight(1)|leg_armor(25),0],
["thors_hammer","Thor's Hammer",[("thor_hammer",0)], itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield|itp_no_pick_up_from_ground, itc_scimitar|itcf_carry_axe_left_hip,
 3000,weight(1.5)|spd_rtng(90)|weapon_length(60)|swing_damage(65,blunt),0],

##MP deadly bow
["deadly_bow", "Deadly Bow", [("LongBow200",0),("LongBow200_carry",ixmesh_carry)], itp_type_bow|itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back,0,weight(1)|spd_rtng(80)|shoot_speed(50)|thrust_damage(20,pierce)|accuracy(99),0],
["deadly_arrows","Deadly Arrows", [("arrow",0),("flying_arrow",ixmesh_flying_ammo),("quiver3", ixmesh_carry)], itp_type_arrows, itcf_carry_bowcase_left,0,weight(1)|weapon_length(95)|thrust_damage(1,pierce)|max_ammo(40),0],
##MP ship data
["ship_data","{!}ship_data_array",[("invalid_item",0)],0,0,1,0,0],

##singleplayer animation stuff
["drinking_ani","{!}glove_animation",[("drinkingL",0)],itp_type_hand_armor|itp_force_show_left_hand|itp_force_show_right_hand,0,0,weight(1),0],
["eating_ani","{!}glove_animation",[("eatingL",0)],itp_type_hand_armor|itp_force_show_right_hand,0,0,weight(1),0],
["sitting_working_1_ani","{!}glove_animation",[("sitting_working_1_L",0)],itp_type_hand_armor|itp_force_show_left_hand|itp_force_show_right_hand,0,0,weight(1),0],
["sitting_working_2_ani","{!}glove_animation",[("sitting_working_2_L",0)],itp_type_hand_armor|itp_force_show_left_hand|itp_force_show_right_hand,0,0,weight(1),0],
["sitting_working_3_ani","{!}glove_animation",[("sitting_working_3_L",0)],itp_type_hand_armor|itp_force_show_left_hand|itp_force_show_right_hand,0,0,weight(1),0],
["fishing_ani","{!}glove_animation",[("fishingL",0)],itp_type_hand_armor|itp_force_show_left_hand|itp_force_show_right_hand,0,0,weight(1),0],
["sharpening_1_ani","{!}glove_animation",[("sharpening_1_L",0)],itp_type_hand_armor|itp_force_show_left_hand|itp_force_show_right_hand,0,0,weight(1),0],
["reading_ani","{!}glove_animation",[("readingL",0)],itp_type_hand_armor|itp_force_show_left_hand|itp_force_show_right_hand,0,0,weight(1),0],
["woodcutting_2_ani","{!}glove_animation",[("woodcutting_2_L",0)],itp_type_hand_armor|itp_force_show_left_hand|itp_force_show_right_hand,0,0,weight(1),0],
["brooming_ani","{!}glove_animation",[("broomingL",0)],itp_type_hand_armor|itp_force_show_left_hand|itp_force_show_right_hand,0,0,weight(1),0],
["field_working_1_ani","{!}glove_animation",[("field_working_1_L",0)],itp_type_hand_armor|itp_force_show_left_hand|itp_force_show_right_hand,0,0,weight(1),0],
["field_working_2_ani","{!}glove_animation",[("field_working_2_L",0)],itp_type_hand_armor|itp_force_show_left_hand|itp_force_show_right_hand,0,0,weight(1),0],
["grinding_ani","{!}glove_animation",[("grindingL",0)],itp_type_hand_armor|itp_force_show_left_hand|itp_force_show_right_hand,0,0,weight(1),0],
["smithing_ani","{!}glove_animation",[("smithingL",0)],itp_type_hand_armor|itp_force_show_left_hand|itp_force_show_right_hand,0,0,weight(1),0],

#native trade items for scenes
["honey","Honey", [("honey_pot",0)], 0, 0, 1, 0, imodbits_none],
["raw_leather","Hides", [("leatherwork_inventory",0)], 0, 0, 1, 0, imodbits_none],
["furs","Furs", [("fur_pack",0)], 0, 0, 1, 0, 0],
["wool_cloth","Wool Cloth", [("wool_cloth",0)], 0, 0, 1, 0, 0],
["oil","Oil", [("oil",0)],  0, 0, 1, 0, 0],
#["linen","Linen", [("linen",0)],  0, 0, 1, 0, 0],
#["wool","Wool", [("wool_sack",0)],  0, 0, 1, 0, 0],
 ["velvet","Velvet", [("velvet",0)],  0, 0, 1, 0, 0],
#["smoked_fish","Smoked Fish", [("smoked_fish",0)],  0, 0, 1, 0, 0],
#["sausages","Sausages", [("sausages",0)],  0, 0, 1, 0, 0],
#["dried_meat","Dried Meat", [("smoked_meat",0)],  0, 0, 1, 0, 0],
#["apples","Fruit", [("apple_basket",0)],  0, 0, 1, 0, 0],

 ####NEW ITEMS ADDON####
 #tools 
 ["work_axe", "Axe", [("Axt06-6",0)], itp_type_two_handed_wpn|itp_primary, itcf_overswing_twohanded|itcf_slashright_twohanded|itcf_carry_axe_back, 5, weight(1.8)|difficulty(0)|spd_rtng(65) | weapon_length(89)|swing_damage(25 , cut), 0],		#weapon_length(84) was to short
 ["work_pickaxe", "Pickaxe", [("pickaxe",0)], itp_type_two_handed_wpn|itp_primary, itcf_overswing_twohanded|itcf_carry_axe_back, 5, weight(1.8)|difficulty(0)|spd_rtng(55) | weapon_length(62)|swing_damage(25 , pierce), 0],	#weapon_length(57) was to short
 ["work_pitchfork", "Pitchfork", [("pitchfork",0)], itp_type_polearm|itp_primary, itcf_thrust_polearm, 5 ,weight(3.5)|difficulty(0)|spd_rtng(60) | weapon_length(157)| thrust_damage(25,  pierce), 0], 
 ["work_basket", "Basket", [("work_basket",0)], itp_type_one_handed_wpn|itp_primary | itp_attach_armature , itcf_carry_axe_back, 41 , weight(5)|difficulty(0)|weapon_length(53), 0],

 ["torch2", "Torch", [("torch_b",0)], itp_type_shield|itp_merchandise, 0, 10 , weight(1)|abundance(90)|hit_points(60)|spd_rtng(0)|shield_width(1), 0,
  [(ti_on_init_item, [(set_position_delta,22,37.5,-5.7),(particle_system_add_new, "psys_torch_fire_2"),(particle_system_add_new, "psys_torch_smoke"),(set_position_delta,28,39,-6.9),(set_current_color,150, 130, 70),(add_point_light, 10, 30),]),
 ]],
#animals
  ["animal_boar","Boar", [("animal_boar",0),("animal_boar_2",imodbit_cracked)],	itp_disable_agent_sounds, 0, 10,abundance(10)|hit_points(25)|body_armor(0)|difficulty(0)|horse_speed(55)|horse_maneuver(150)|horse_charge(5000)|horse_scale(78),imodbits_horse_basic],
  ["animal_pig","Pig", [("animal_pig",0),("animal_pig_2",imodbit_cracked)],		itp_disable_agent_sounds, 0, 10,abundance(10)|hit_points(25)|body_armor(0)|difficulty(0)|horse_speed(5)|horse_maneuver(5)|horse_charge(0)|horse_scale(67),imodbits_horse_basic],
  ["animal_piglet","Piglet", [("animal_pig",0),("animal_pig_2",imodbit_cracked)],itp_disable_agent_sounds, 0, 10,abundance(10)|hit_points(25)|body_armor(0)|difficulty(0)|horse_speed(10)|horse_maneuver(5)|horse_charge(0)|horse_scale(38),imodbits_horse_basic],
  ["animal_sheep"  ,"Sheep", [("animal_sheep_a_1",0),("animal_sheep_a_2",imodbit_cracked),("animal_sheep_a_3",imodbit_rusty),("animal_sheep_a_4",imodbit_bent)],itp_disable_agent_sounds, 0, 10,abundance(10)|hit_points(25)|body_armor(0)|difficulty(0)|horse_speed(5)|horse_maneuver(5)|horse_charge(0)|horse_scale(78),imodbits_horse_basic],
  ["animal_sheep_b","Sheep", [("animal_sheep_b_1",0),("animal_sheep_b_2",imodbit_cracked),("animal_sheep_b_3",imodbit_rusty),("animal_sheep_b_4",imodbit_bent)],itp_disable_agent_sounds, 0, 10,abundance(10)|hit_points(25)|body_armor(0)|difficulty(0)|horse_speed(5)|horse_maneuver(5)|horse_charge(0)|horse_scale(78),imodbits_horse_basic],
  ["animal_dog","Dog", [("animal_dog",0),("animal_dog_2",imodbit_cracked)],		itp_disable_agent_sounds, 0, 10,hit_points(25)|horse_speed(19)|horse_maneuver(70)|horse_scale(57), 0],

  ["dog_companion_horse","Dog", [("animal_dog",0)],		itp_type_horse|itp_disable_agent_sounds, 0, 10,hit_points(350)|horse_speed(30)|horse_maneuver(90)|horse_scale(62), 0],
  ["magic_broom","Strange broom", [("magic_broom",0)], itp_type_horse|itp_disable_agent_sounds, 0, 10,abundance(10)|hit_points(25)|body_armor(0)|difficulty(0)|horse_speed(1050)|horse_maneuver(50)|horse_charge(100)|horse_scale(100),imodbits_horse_basic],
  ["stones_mp",         "Stones", [("throwing_stone",0)], itp_type_thrown|itp_primary|itp_secondary ,itcf_throw_stone,
 5, weight(1)|difficulty(0)|spd_rtng(95) | shoot_speed(20)|thrust_damage(9,blunt)|max_ammo(8)|weapon_length(8),0],
  ["invisible_armor", "Kejserens nye Klaeder", [("empty",0)], itp_type_body_armor ,0,1,body_armor(25),0],
  # ["no_hands", "no hands", [("empty",0)], itp_type_hand_armor ,0,1,body_armor(5),0],
  # ["no_legs", "no legs", [("empty",0)], itp_type_foot_armor ,0,1,leg_armor(20),0],
  ["dog_bite","Bite", [("empty",0)], itp_type_polearm|itp_primary|itp_can_knock_down|itp_no_pick_up_from_ground, itc_greatlance|itcf_carry_axe_left_hip, 1, weight(1)|spd_rtng(95)|weapon_length(65)|thrust_damage(25, pierce),0],
#add-ons treasure for high king quest

###NEW ARMORs Mail Armaduras
###bear and wolf armor
["addon_mail4", "Bear Byrnie", [("Chain_Bear_01",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 15000 , weight(23)|abundance(10)|head_armor(13)|body_armor(47)|leg_armor(25)|difficulty(14) ,imodbits_mail],
["addon_mail5", "Wolf Byrnie", [("Chain_Wolf_01",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 13500 , weight(21.9)|abundance(10)|head_armor(12)|body_armor(46)|leg_armor(24)|difficulty(13) ,imodbits_mail],

["addon_mail6", "Bear Lorica", [("Chain_Bear_02",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 16500 , weight(24.2)|abundance(10)|head_armor(13)|body_armor(48)|leg_armor(26)|difficulty(14) ,imodbits_mail],
["addon_mail7", "Wolf Lorica", [("Chain_Wolf_02",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 15000 , weight(23)|abundance(10)|head_armor(12)|body_armor(47)|leg_armor(25)|difficulty(14) ,imodbits_mail],
#lamellar
["lamellar_armor2", "Scale Lorica", [("Scalemail02",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 12000 , weight(16)|abundance(10)|head_armor(0)|body_armor(46)|leg_armor(27)|difficulty(9) ,imodbits_mail],

 ####trofeos de batalla chief
  ["trophy_norse","Norse Konungr Trophy", [("standard_dragon1",0)], itp_type_goods|itp_always_loot, 0, 210,weight(3)|abundance(90),imodbits_none],
  ["trophy_cymry","Vrenhin Lloegr Trophy", [("horn_multi",0)], itp_type_goods|itp_always_loot, 0, 410,weight(7)|abundance(90),imodbits_none],
  ["trophy_irish","Ard Ruire Trophy", [("vc_gold_trophy",0)], itp_type_goods|itp_always_loot, 0, 610,weight(10)|abundance(90),imodbits_none],
  ["trophy_saxon","Brytenwalda Trophy", [("vc_gold_trophy",0)], itp_type_goods|itp_always_loot, 0, 610,weight(10)|abundance(90),imodbits_none],
 
 #bonus tunics (VC-2393):
 ["bonus_tunic_1", "Emissary Tunic", [("Tunic_Norse_01",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 5540 , weight(0.5)|abundance(8)|head_armor(0)|body_armor(18)|leg_armor(4), imodbits_none,	[], norse_fac], # +1 persuasion
 ["bonus_tunic_2", "Ealdorman Tunic", [("Tunic_Briton_01",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 6840 , weight(0.5)|abundance(8)|head_armor(0)|body_armor(18)|leg_armor(3), imodbits_none,	[], angle_fac],	# +1 leadership
 ["bonus_tunic_3", "Trader Tunic", [("Tunic_Frisian_03",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 5440 , weight(0.5)|abundance(8)|head_armor(0)|body_armor(20)|leg_armor(4), imodbits_none,	[], frisia_fac],# +1 trade
 ["bonus_dress_1", "Fine Pictish Dress", [("female_dress_picts2",0)],  itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 
 5540 , weight(0.5)|abundance(8)|head_armor(0)|body_armor(18)|leg_armor(4), imodbits_none, [], pict_fac], # +1 persuasion
 ["bonus_dress_2", "Royal Saxon Dress", [("female_dress_anglosaxon4",0)],  itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 
 6840 , weight(0.5)|abundance(8)|head_armor(0)|body_armor(18)|leg_armor(3), imodbits_none, [], saxon_fac], # +1 leadership
 ["bonus_dress_3", "Noble Norse Dress", [("female_dress_scandinavian2",0)],  itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 
 5440 , weight(0.5)|abundance(8)|head_armor(0)|body_armor(20)|leg_armor(4), imodbits_none, [], norse_fac], # +1 trade
 ["thors_javelins", "Thor's Javelins", [("cow_2",0)], itp_type_thrown |itp_primary|itp_can_knock_down|itp_crush_through ,itcf_throw_axe, 
 1, weight(4)|difficulty(1)|spd_rtng(60) | shoot_speed(12) | thrust_damage(25, blunt)|max_ammo(30)|weapon_length(32), imodbits_none, [(ti_on_weapon_attack, [(play_sound,"snd_cow_moo")])]],
 
 ["decap_head", "No head", [("decap",0)], itp_type_head_armor|itp_fit_to_head|itp_covers_head   ,0,
 180 , weight(2)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_none ],
 
 ["work_axe_mp", "Axe", [("Axt06-6",0)], itp_type_two_handed_wpn|itp_primary|itp_no_blur,itc_cut_two_handed|itc_parry_two_handed|itcf_carry_axe_back, 2000, weight(1.8)|difficulty(0)|spd_rtng(75)|weapon_length(95)|swing_damage(24,cut),0],
 ["pickaxe_mp", "Pickaxe", [("pickaxe",0)], itp_type_two_handed_wpn|itp_primary|itp_no_blur, itc_cut_two_handed|itcf_carry_axe_back, 1500, weight(1.8)|difficulty(0)|spd_rtng(65)|weapon_length(65)|swing_damage(20,pierce),0],
 ["seax_1_mp", "Old Seax", [("Seax1",0),("Seax1_Scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_blur|itp_no_parry, itc_dagger|itcf_carry_quiver_back_right|itcf_show_holster_when_drawn,
 1900 , weight(0.5)|spd_rtng(90)| weapon_length(37)|swing_damage(8, cut) | thrust_damage(17, pierce),imodbits_sword],
 ["spear_1_mp", "Old Spear", [("Spear_S_01",0)], itp_type_polearm|itp_offset_lance|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear|itcf_carry_spear,
 2500 , weight(2.3)|difficulty(6)|spd_rtng(85)| weapon_length(113)|swing_damage(15, blunt)| thrust_damage(25, pierce),imodbits_polearm],
 
 ["crossbow_mp", "Pictish Crossbow", [("crossbow",0)], itp_type_crossbow|itp_primary|itp_secondary|itp_cant_use_on_horseback|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
 750 , weight(2.25)|spd_rtng(35)|shoot_speed(66)|thrust_damage(40, pierce)|max_ammo(1)|accuracy(80),imodbits_crossbow],
 ["bolts_mp","Bolts", [("bolt",0),("flying_bolt",ixmesh_flying_ammo),("boltQuiver1", ixmesh_carry),("boltQuiver1", ixmesh_carry|imodbit_large_bag)], itp_type_bolts|itp_can_penetrate_shield, itcf_carry_bowcase_left,
 250,weight(1)|weapon_length(63)|thrust_damage(1,pierce)|max_ammo(30),imodbits_missile],
 
 ["items_end", "Items End", [("velvet",0)], 0, 0, 1, 0, 0],

]

#MOTO generate no-swing versions of weapons
#Warning: this makes additions to item table non-save compatible, as the system only reads in the "new" ones, effectively overwriting the real new ones
#It may be best to comment out until the table is set
append_noswing_items(items)
