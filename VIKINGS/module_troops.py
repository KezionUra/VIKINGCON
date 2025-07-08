import random

from header_common import *
from header_items import *
from header_troops import *
from header_skills import *
from ID_factions import *
from ID_items import *
from ID_scenes import *

####################################################################################################################
#  Each troop contains the following fields:
#  1) Troop id (string): used for referencing troops in other files. The prefix trp_ is automatically added before each troop-id .
#  2) Toop name (string).
#  3) Plural troop name (string).
#  4) Troop flags (int). See header_troops.py for a list of available flags
#  5) Scene (int) (only applicable to heroes) For example: scn_reyvadin_castle|entry(1) puts troop in reyvadin castle's first entry point
#  6) Reserved (int). Put constant "reserved" or 0.
#  7) Faction (int)
#  8) Inventory (list): Must be a list of items
#  9) Attributes (int): Example usage:
#           str_6|agi_6|int_4|cha_5|level(5)
# 10) Weapon proficiencies (int): Example usage:
#           wp_one_handed(55)|wp_two_handed(90)|wp_polearm(36)|wp_archery(80)|wp_crossbow(24)|wp_throwing(45)
#     The function wp(x) will create random weapon proficiencies close to value x.
#     To make an expert archer with other weapon proficiencies close to 60 you can use something like:
#           wp_archery(160) | wp(60)
# 11) Skills (int): See header_skills.py to see a list of skills. Example:
#           knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2
# 12) Face code (int): You can obtain the face code by pressing ctrl+E in face generator screen
# 13) Face code (int)(2) (only applicable to regular troops, can be omitted for heroes):
#     The game will create random faces between Face code 1 and face code 2 for generated troops
# 14) Troop image (string): If this variable is set, the troop will use an image rather than its 3D visual during the conversations
#  town_1   Sargoth
#  town_2   Tihr
#  town_3   Veluca
#  town_4   Suno
#  town_5   Jelkala
#  town_6   Praven
#  town_7   Uxkhal
#  town_8   Reyvadin
#  town_9   Khudan
#  town_10  Tulga
#  town_11  Curaw
#  town_12  Wercheg
#  town_13  Rivacheg
#  town_14  Halmar
####################################################################################################################

# Some constant and function declarations to be used below...
# wp_one_handed () | wp_two_handed () | wp_polearm () | wp_archery () | wp_crossbow () | wp_throwing ()
def wp(x): #melee
  n = 0
  r = 10 + int(x / 10)
#  n |= wp_one_handed(x + random.randrange(r))
#  n |= wp_two_handed(x + random.randrange(r))
#  n |= wp_polearm(x + random.randrange(r))
#  n |= wp_archery(x + random.randrange(r))
#  n |= wp_crossbow(x + random.randrange(r))
#  n |= wp_throwing(x + random.randrange(r))
  n |= wp_one_handed(x)
  n |= wp_two_handed(x)
  n |= wp_polearm(x)
  n |= wp_archery(x) #
  n |= wp_crossbow(x) #
  n |= wp_throwing(x)
  n |= wp_firearm(x) #slings
  return n

def wpe(m,a,c,t):
   n = 0
   n |= wp_one_handed(m)
   n |= wp_two_handed(m)
   n |= wp_polearm(m)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n

def wpex(o,w,p,a,c,t):
   n = 0
   n |= wp_one_handed(o)
   n |= wp_two_handed(w)
   n |= wp_polearm(p)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n
   
def wp_melee(x): 
  n = 0
  r = 10 + int(x / 10)
#  n |= wp_one_handed(x + random.randrange(r))
#  n |= wp_two_handed(x + random.randrange(r))
#  n |= wp_polearm(x + random.randrange(r))
  n |= wp_one_handed(x + 20)
  n |= wp_two_handed(x)
  n |= wp_polearm(x + 10)
  return n

#Skills cambios chief
# . Riding (25)
# . Athletics (26)
# . Shield (27)
# . Weapon Master (28)
#.  Power Draw (34)
# . Power Throw (35)
# . Power Strike (36)
# . Ironflesh (37)

#lvl12
knows_common = knows_weapon_master_5|knows_ironflesh_4|knows_athletics_5|knows_power_strike_3|knows_shield_1|knows_inventory_management_2|knows_power_throw_3|knows_power_draw_3 #40+12 / 2
#lvl18
knows_warrior_basic = knows_weapon_master_6|knows_ironflesh_5|knows_athletics_5|knows_riding_2|knows_power_strike_3|knows_shield_2|knows_inventory_management_4|knows_power_throw_3|knows_power_draw_3 #40+18 / 2 +2
#lvl23
knows_warrior_basic2 = knows_weapon_master_7|knows_ironflesh_7|knows_athletics_5|knows_riding_3|knows_power_strike_5|knows_shield_2|knows_inventory_management_4|knows_power_throw_3|knows_power_draw_3  #40+24 / 2 +4
#lvl26
knows_warrior_normal = knows_weapon_master_8|knows_ironflesh_8|knows_athletics_5|knows_riding_5|knows_power_strike_5|knows_shield_2|knows_inventory_management_5|knows_power_throw_4|knows_power_draw_4 #40+26 / 2 +6
#lvl29
knows_warrior_veteran = knows_weapon_master_9|knows_ironflesh_9|knows_athletics_5|knows_riding_6|knows_power_strike_7|knows_shield_3|knows_inventory_management_5|knows_power_throw_4|knows_power_draw_4 ##40+30 / 2 +8
#lvl31
knows_warrior_elite = knows_weapon_master_10|knows_ironflesh_10|knows_athletics_5|knows_riding_7|knows_power_strike_8|knows_shield_3|knows_inventory_management_6|knows_power_throw_4|knows_power_draw_4 ###40+32 / 2 +12

knows_archer_basic = knows_weapon_master_3|knows_ironflesh_6|knows_athletics_5|knows_riding_3|knows_power_strike_2|knows_shield_2|knows_inventory_management_4|knows_power_throw_4|knows_power_draw_4 #cambiado chief
#special skirmishes pictish and irish elite
knows_archer_pictish = knows_weapon_master_5|knows_ironflesh_6|knows_athletics_6|knows_riding_4|knows_power_strike_4|knows_shield_2|knows_inventory_management_4|knows_power_throw_5|knows_power_draw_5 #cambiado chief
#special horseman pictish and irish elite
knows_horseman_pictish = knows_weapon_master_5|knows_ironflesh_6|knows_athletics_6|knows_riding_8|knows_power_strike_4|knows_shield_2|knows_inventory_management_6|knows_power_throw_6|knows_power_draw_6 #cambiado chief

knows_cleric = knows_athletics_6|knows_trade_2|knows_wound_treatment_4|knows_first_aid_4|knows_surgery_4|knows_inventory_management_4



#Attributes
def_attrib = str_16 | agi_8 | int_12 | cha_12 #basic points 55
def_attrib2 = str_18 | agi_8 | int_12 | cha_12 #+3 level med
def_attrib3 = str_20 | agi_8 | int_12 | cha_12 #+5 level max
def_attrib_multiplayer = str_16 | agi_8 | int_12 | cha_12
def_attrib_troll = str_30 | agi_30 | int_6 | cha_6 #special

knows_merchant_npc = knows_riding_2|knows_trade_9|knows_inventory_management_10|knows_persuasion_4|knows_power_strike_2|knows_shield_2|knows_weapon_master_3|knows_ironflesh_3|knows_athletics_4|knows_leadership_1|knows_wound_treatment_2|knows_first_aid_2|knows_surgery_2|knows_power_throw_2|knows_spotting_3|knows_pathfinding_4
knows_warrior_npc = knows_weapon_master_2|knows_ironflesh_2|knows_athletics_5|knows_riding_6|knows_power_strike_1|knows_shield_2|knows_inventory_management_5|knows_power_throw_1 #cambiado chief
knows_tracker_npc = knows_weapon_master_1|knows_ironflesh_9|knows_athletics_4|knows_riding_3|knows_spotting_9|knows_pathfinding_9|knows_tracking_9|knows_inventory_management_5

king_attrib = str_20|agi_19|int_18|cha_20|level(40) #cambiado chief
king_skills = knows_weapon_master_10|knows_trainer_5|knows_riding_4|knows_ironflesh_10|knows_power_strike_10|knows_athletics_10|knows_shield_3|knows_tactics_10|knows_prisoner_management_9|knows_leadership_10|knows_wound_treatment_9|knows_first_aid_8|knows_surgery_8|knows_power_throw_5|knows_power_draw_6|knows_spotting_6|knows_pathfinding_5|knows_inventory_management_4|knows_persuasion_6|knows_engineer_6|knows_sea_king_4|knows_navigation_10|knows_maintenance_8 #
lord_attrib = str_18|agi_17|int_16|cha_18|level(38) #cambiado chief
knows_lord_1 = knows_weapon_master_8|knows_trainer_4|knows_riding_4|knows_ironflesh_8|knows_power_strike_8|knows_athletics_8|knows_shield_3|knows_tactics_8|knows_prisoner_management_9|knows_leadership_8|knows_wound_treatment_7|knows_first_aid_6|knows_surgery_6|knows_power_throw_4|knows_power_draw_4|knows_spotting_4|knows_pathfinding_4|knows_inventory_management_3|knows_persuasion_4|knows_engineer_4|knows_sea_king_4|knows_maintenance_6


#These face codes are generated by the in-game face generator.
#Enable edit mode and press ctrl+E in face generator screen to obtain face codes.


reserved = 0

no_scene = 0
#BRITONS
swadian_face_younger_1 = 0x000000000a00000136db6db6db6db6db00000000001db6db0000000000000000
swadian_face_young_1   = 0x000000000d00114136db6db6db6db6db00000000001db6db0000000000000000
swadian_face_middle_1  = 0x000000000d00214136db6db6db6db6db00000000001db6db0000000000000000
swadian_face_old_1     = 0x000000000d00314136db6db6db6db6db00000000001db6db0000000000000000
swadian_face_older_1   = 0x000000000d00414136db6db6db6db6db00000000001db6db0000000000000000

swadian_face_younger_2 = 0x000000003a0053c536db6db6db6db6db00000000001db6db0000000000000000
swadian_face_young_2   = 0x000000033a0063c536db6db6db6db6db00000000001db6db0000000000000000
swadian_face_middle_2  = 0x000000087a0073c536db6db6db6db6db00000000001db6db0000000000000000
swadian_face_old_2     = 0x0000000dba0083c536db6db6db6db6db00000000001db6db0000000000000000
swadian_face_older_2   = 0x0000000efa0093c536db6db6db6db6db00000000001db6db0000000000000000
#cambias caras saxons and angles, frisian
vaegir_face_younger_1 = 0x000000000400000336db6db6db6db6db00000000001db6db0000000000000000
vaegir_face_young_1   = 0x00000003c400100336db6db6db6db6db00000000001db6db0000000000000000
vaegir_face_middle_1  = 0x00000003c400200336db6db6db6db6db00000000001db6db0000000000000000
vaegir_face_old_1     = 0x00000003c400300336db6db6db6db6db00000000001db6db0000000000000000
vaegir_face_older_1   = 0x00000003c400400336db6db6db6db6db00000000001db6db0000000000000000

vaegir_face_younger_2 = 0x00000003f500414836db6db6db6db6db00000000001db6db0000000000000000
vaegir_face_young_2   = 0x000000097500514836db6db6db6db6db00000000001db6db0000000000000000
vaegir_face_middle_2  = 0x000000097500614836db6db6db6db6db00000000001db6db0000000000000000
vaegir_face_old_2     = 0x0000000db500714836db6db6db6db6db00000000001db6db0000000000000000
vaegir_face_older_2   = 0x0000000ff500914836db6db6db6db6db00000000001db6db0000000000000000
#chief  pictos normal
khergit_face_younger_1 = 0x000000000f00114d36db6db6db6db6db00000000001db6db0000000000000000
khergit_face_young_1   = 0x00000003cf00214d36db6db6db6db6db00000000001db6db0000000000000000
khergit_face_middle_1  = 0x00000007cf00314d36db6db6db6db6db00000000001db6db0000000000000000
khergit_face_old_1     = 0x0000000c0f00414d36db6db6db6db6db00000000001db6db0000000000000000
khergit_face_older_1   = 0x0000000fcf00514d36db6db6db6db6db00000000001db6db0000000000000000

khergit_face_younger_2 = 0x000000003f00635336db6db6db6db6db00000000001db6db0000000000000000
khergit_face_young_2   = 0x00000002ff00735336db6db6db6db6db00000000001db6db0000000000000000
khergit_face_middle_2  = 0x000000067f00735336db6db6db6db6db00000000001db6db0000000000000000
khergit_face_old_2     = 0x0000000aff00735336db6db6db6db6db00000000001db6db0000000000000000
khergit_face_older_2   = 0x0000000fff00935336db6db6db6db6db00000000001db6db0000000000000000
### irish 
rhodok_face_younger_1 = 0x000000002900018d36db6db6db6db6db00000000001db6db0000000000000000
rhodok_face_young_1   = 0x000000052900118d36db6db6db6db6db00000000001db6db0000000000000000
rhodok_face_middle_1  = 0x00000009e900218d36db6db6db6db6db00000000001db6db0000000000000000
rhodok_face_old_1     = 0x0000000ca900318d36db6db6db6db6db00000000001db6db0000000000000000
rhodok_face_older_1   = 0x0000000e2900418d36db6db6db6db6db00000000001db6db0000000000000000

rhodok_face_younger_2 = 0x000000003f00528d36db6db6db6db6db00000000001db6db0000000000000000
rhodok_face_young_2   = 0x00000004ff00628d36db6db6db6db6db00000000001db6db0000000000000000
rhodok_face_middle_2  = 0x000000093f00728d36db6db6db6db6db00000000001db6db0000000000000000
rhodok_face_old_2     = 0x0000000dbf00828d36db6db6db6db6db00000000001db6db0000000000000000
rhodok_face_older_2   = 0x0000000e7f00928d36db6db6db6db6db00000000001db6db0000000000000000
### pictish painted
khergit_face_younger_3 = 0x000000001200a15136db6db6db6db6db00000000001db6db0000000000000000
khergit_face_young_3   = 0x000000049200a15136db6db6db6db6db00000000001db6db0000000000000000
khergit_face_middle_3  = 0x0000000e1200a15136db6db6db6db6db00000000001db6db0000000000000000
khergit_face_old_3     = 0x000000001200b15136db6db6db6db6db00000000001db6db0000000000000000
khergit_face_older_3   = 0x000000091200b15136db6db6db6db6db00000000001db6db0000000000000000

khergit_face_younger_4 = 0x000000003900b41336db6db6db6db6db00000000001db6db0000000000000000
khergit_face_young_4   = 0x0000000db900b41336db6db6db6db6db00000000001db6db0000000000000000
khergit_face_middle_4  = 0x000000003900c41336db6db6db6db6db00000000001db6db0000000000000000
khergit_face_old_4     = 0x00000007b900c41336db6db6db6db6db00000000001db6db0000000000000000
khergit_face_older_4   = 0x0000000f7900c41336db6db6db6db6db00000000001db6db0000000000000000

#chief vikings
nord_face_younger_1 = 0x000000000000044936db6db6db6db6db00000000001db6db0000000000000000
nord_face_young_1   = 0x000000044000144936db6db6db6db6db00000000001db6db0000000000000000
nord_face_middle_1  = 0x0000000a8000244936db6db6db6db6db00000000001db6db0000000000000000
nord_face_old_1     = 0x000000094500300136db6db6db6db6db00000000001db6db0000000000000000
nord_face_older_1   = 0x0000000f0500400136db6db6db6db6db00000000001db6db0000000000000000

nord_face_younger_2 = 0x000000002c005b5036db6db6db6db6db00000000001db6db0000000000000000
nord_face_young_2   = 0x00000005ac006b5036db6db6db6db6db00000000001db6db0000000000000000
nord_face_middle_2  = 0x0000000a6c007b5036db6db6db6db6db00000000001db6db0000000000000000
nord_face_old_2     = 0x0000000dac008b5036db6db6db6db6db00000000001db6db0000000000000000
nord_face_older_2   = 0x0000000eec009b5036db6db6db6db6db00000000001db6db0000000000000000
#global
man_face_younger_1 = 0x000000000500000136db6db6db6db6db00000000001db6db0000000000000000
man_face_young_1   = 0x000000040500100136db6db6db6db6db00000000001db6db0000000000000000
man_face_middle_1  = 0x000000094500200136db6db6db6db6db00000000001db6db0000000000000000
man_face_old_1     = 0x0000000e400400006a1a8adad4d2eae400000000001eeb240000000000000000
man_face_older_1   = 0x0000000fc00400006a1a8adad4d2eae400000000001eeb240000000000000000

man_face_younger_2 = 0x000000003f005b1136db6db6db6db6db00000000001db6db0000000000000000
man_face_young_2   = 0x00000004bf006b1136db6db6db6db6db00000000001db6db0000000000000000
man_face_middle_2  = 0x0000000a3f007b1136db6db6db6db6db00000000001db6db0000000000000000
man_face_old_2     = 0x0000000dbf008b1136db6db6db6db6db00000000001db6db0000000000000000
man_face_older_2   = 0x0000000e7f009b1136db6db6db6db6db00000000001db6db0000000000000000
#bandits 
bandit_face_younger_1 = 0x000000000500000136db6db6db6db6db00000000001db6db0000000000000000
bandit_face_young_1   = 0x000000040500100136db6db6db6db6db00000000001db6db0000000000000000
bandit_face_middle_1  = 0x000000094500200136db6db6db6db6db00000000001db6db0000000000000000
bandit_face_old_1     = 0x000000094500300136db6db6db6db6db00000000001db6db0000000000000000
bandit_face_older_1   = 0x0000000f0500400136db6db6db6db6db00000000001db6db0000000000000000

bandit_face_younger_2 = 0x000000003f005b1136db6db6db6db6db00000000001db6db0000000000000000
bandit_face_young_2   = 0x00000004bf006b1136db6db6db6db6db00000000001db6db0000000000000000
bandit_face_middle_2  = 0x0000000a3f007b1136db6db6db6db6db00000000001db6db0000000000000000
bandit_face_old_2     = 0x0000000dbf008b1136db6db6db6db6db00000000001db6db0000000000000000
bandit_face_older_2   = 0x0000000e7f009b1136db6db6db6db6db00000000001db6db0000000000000000
#chief bandidos acaba
#chief caras priest
sac_face_younger_1 = 0x000000000000601436db6db6db6db6db00000000001db6db0000000000000000
sac_face_young_1   = 0x0000000f0000601436db6db6db6db6db00000000001db6db0000000000000000
sac_face_middle_1  = 0x000000000000701436db6db6db6db6db00000000001db6db0000000000000000
sac_face_old_1     = 0x0000000e8000701436db6db6db6db6db00000000001db6db0000000000000000
sac_face_older_1   = 0x000000050000801436db6db6db6db6db00000000001db6db0000000000000000

sac_face_younger_2 = 0x000000053f00830036db6db6db6db6db00000000001db6db0000000000000000
sac_face_young_2   = 0x0000000d7f00730036db6db6db6db6db00000000001db6db0000000000000000
sac_face_middle_2  = 0x000000027f00630036db6db6db6db6db00000000001db6db0000000000000000
sac_face_old_2     = 0x000000053f00930036db6db6db6db6db00000000001db6db0000000000000000
sac_face_older_2   = 0x0000000fff00930036db6db6db6db6db00000000001db6db0000000000000000
###
#women face norse and saxons
womannorth_face_younger_1 = 0x000000000000201236a4b4b36365b26c00000000001da52b0000000000000000
womannorth_face_young_1   = 0x00000004c000201236a4b4b36365b26c00000000001da52b0000000000000000
womannorth_face_middle_1  = 0x0000000b8000201236a4b4b36365b26c00000000001da52b0000000000000000
womannorth_face_old_1     = 0x0000000e4000201236a4b4b36365b26c00000000001da52b0000000000000000
womannorth_face_older_1   = 0x0000000f4000201236a4b4b36365b26c00000000001da52b0000000000000000

womannorth_face_younger_2 = 0x000000001b00401136a4b4b36365b26c00000000001da52b0000000000000000
womannorth_face_young_2   = 0x000000059b00401136a4b4b36365b26c00000000001da52b0000000000000000
womannorth_face_middle_2  = 0x0000000b9b00401136a4b4b36365b26c00000000001da52b0000000000000000
womannorth_face_old_2     = 0x0000000d1b00401136a4b4b36365b26c00000000001da52b0000000000000000
womannorth_face_older_2   = 0x0000000e1b00401136a4b4b36365b26c00000000001da52b0000000000000000
###
#women face global
woman_face_younger_1 = 0x000000000000201236a4b4b36365b26c00000000001da52b0000000000000000
woman_face_young_1   = 0x00000004c000201236a4b4b36365b26c00000000001da52b0000000000000000
woman_face_middle_1  = 0x0000000b8000201236a4b4b36365b26c00000000001da52b0000000000000000
woman_face_old_1     = 0x0000000e4000201236a4b4b36365b26c00000000001da52b0000000000000000
woman_face_older_1   = 0x0000000f4000201236a4b4b36365b26c00000000001da52b0000000000000000

woman_face_younger_2 = 0x000000003f00401136a4b4b36365b26c00000000001da52b0000000000000000
woman_face_young_2   = 0x000000053f00401136a4b4b36365b26c00000000001da52b0000000000000000
woman_face_middle_2  = 0x00000009ff00401136a4b4b36365b26c00000000001da52b0000000000000000
woman_face_old_2     = 0x0000000d7f00401136a4b4b36365b26c00000000001da52b0000000000000000
woman_face_older_2   = 0x0000000e3f00401136a4b4b36365b26c00000000001da52b0000000000000000
### Childs girl
nina_face_younger_1 = 0x000000019f0c3014193a75b5629359b200000000001eba740000000000000000
nina_face_younger_2 = 0x000000003b00300853128aba627248dd00000000001eb91c0000000000000000
### Childs boy 
nino_face_younger_1 = 0x00000001800010025d8816e23047f66e00000000001f02000000000000000000
nino_face_younger_2   = 0x000000002f001005471e524418577c2800000000001e4ae90000000000000000

#
woman_face_1    = 0x0000000000000001000000000000000000000000001c00000000000000000000
woman_face_2    = 0x00000003bf0030067ff7fbffefff6dff00000000001f6dbf0000000000000000
swadian_woman_face_1 = 0x0000000180102006124925124928924900000000001c92890000000000000000
swadian_woman_face_2 = 0x00000001bf1000061db6d75db6b6dbad00000000001c92890000000000000000
#chief ampliado
khergit_woman_face_1 = 0x000000026d10c0011854c9ed2c79345100000000001ec9f50000000000000000
khergit_woman_face_2 = 0x000000003900c00448d5aa6c5235591400000000001ed88c0000000000000000
khergit_woman_face_3 = 0x000000097f08e0013b996ddc93cd58df00000000001eaa630000000000000000
khergit_woman_face_4 = 0x000000095c0cf0053a646ae69b31c4b200000000001eab240000000000000000
khergit_woman_face_5 = 0x0000000fed1020011854c9ed2c79345100000000001ec9f50000000000000000
khergit_woman_face_6 = 0x0000000fcc08b00152da31d4997638f600000000001cb7210000000000000000
#chief ampliado
refugee_face1 = woman_face_1
refugee_face2 = woman_face_2
girl_face1    = woman_face_1
girl_face2    = woman_face_2
mercenary_face_1 = 0x00000001a400520836db6db6db6db6db00000000001db6db0000000000000000
mercenary_face_2 = 0x0000000cff00730b6db6db6db7fbffff00000000001efffe0000000000000000
vaegir_face1  = vaegir_face_young_1
vaegir_face2  = vaegir_face_older_2
#cambiados chief bandidos
bandit_face1  = bandit_face_young_1
bandit_face2  = bandit_face_older_2
####
#
undead_face1  = 0x00000000002000000000000000000000
undead_face2  = 0x000000000020010000001fffffffffff

#NAMES:
#

tf_guarantee_all = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged
tf_guarantee_all_wo_ranged = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield

########ITEMS BEGIN
#equipament
####################
#horses
common_horse = [itm_common_horse,itm_common_horse2]  # Britons and irish, cavalry
common_pony = [itm_common_pony,itm_common_pony2]  # all factions.
wild_pony = [itm_wild_pony,itm_wild_pony2,itm_wild_horse,itm_wild_horse2]  # pictish only
########################
#Guantes (hecho elites: level 11 companion, level 12 companion, level12 landed, level13 landed, horsemen)
common_gloves = [itm_leather_gloves]  # all factions normal archers
#crown
crown_onlykings = [itm_crown1]  # all factions 
#music
common_music = [itm_lute]  # all factions 
common_music2 = [itm_lyre]  # all factions 
#Trophy
common_trophy = [itm_trophy_a]  # all factions 
war_trophy = [itm_trophy_b]  # all factions 
elite_trophy = [itm_trophy_c]  # all factions 
###special items quest
special_sword_premium1 = [itm_sword_premium2]  
special_sword_premium2 = [itm_suttonhoosword2]  
special_sword_premium3 = [itm_sword_premium1]  

########################
###shoes and boots
#common shoes
#everybody less pictish and irish
common_shoes = [itm_carbatinae_1,itm_carbatinae_4,itm_carbatinae_3,itm_carbatinae_8,itm_carbatinae_5s,itm_carbatinae_11q] #1 shoes ##low class
common_shoes2 = [itm_carbatinae_1s,itm_carbatinae_vc5,itm_carbatinae_6,itm_carbatinae_4s,itm_carbatinae_5s,itm_carbatinae_12q] #2 shoes ##low class
common_shoes3 = [itm_carbatinae_5s,itm_carbatinae_vc3,itm_carbatinae_4s,itm_carbatinae_vc6,itm_carbatinae_vc2s,itm_carbatinae_5v] #3 shoes ##low class
common_shoes4 = [itm_carbatinae_vc2,itm_carbatinae_5v,itm_carbatinae_vc1,itm_carbatinae_vc2s,itm_carbatinae_vc1v,itm_carbatinae_1v] #4 shoes ##low class

pictish_shoes = [itm_just_man_boots_medium,itm_just_man_boots_light,itm_just_man_shoes,itm_bare_foot_man] #4 shoes ##low class #totalmente descalzos #itm_bare_foot_man,
irish_shoes = [itm_just_man_boots_medium,itm_bare_foot_man]
irish_shoes2 = [itm_just_man_boots_light,itm_bare_foot_man,itm_just_man_boots_medium]

#warrior shoes
#saxons and britons
war_brit_shoes1 = [itm_carbatinae_6s,itm_carbatinae_2s,itm_carbatinae_3s,itm_carbatinae_vc4s,itm_carbatinae_2] #1 shoes warriors saxons and britons
war_brit_shoes2 = [itm_carbatinae_5,itm_carbatinae_7,itm_carbatinae_9,itm_carbatinae_2v,itm_carbatinae_3v] #2 shoes warriors saxons and britons

#shoes vikings guerreros
war_norse_shoes1 = [itm_carbatinae_14qs,itm_carbatinae_vc1v,itm_carbatinae_2s,itm_carbatinae_6v,itm_carbatinae_5] #1 shoes warriors vikings
war_norse_shoes2 = [itm_carbatinae_vc3s,itm_carbatinae_vc1s,itm_carbatinae_2s,itm_carbatinae_vc4,itm_carbatinae_13qs] #2 shoes warriors vikings
war_norse_shoes3 = [itm_carbatinae_4v,itm_carbatinae_vc2v,itm_carbatinae_14qv,itm_carbatinae_6v,itm_carbatinae_3v] #3 shoes warriors vikings

##High Class Elite units.
#everybody
elite_shoes = [itm_carbatinae_11q,itm_carbatinae_12q] #shoes quality Comun
elite_brit_boots = [itm_carbatinae_11qs,itm_carbatinae_12qs,itm_carbatinae_13qs,itm_carbatinae_14qs]#shoes warriors saxons and britons
elite_norse_boots = [itm_carbatinae_vc1s,itm_carbatinae_vc3s,itm_carbatinae_4v,itm_carbatinae_14qv]#shoes warriors vikings
elite_pict_foot = [itm_just_man_boots_dark]#shoes
elite_gael_foot = [itm_gaelshoes_1,itm_gaelshoes_2,itm_gaelshoes_3]#shoes warriors irish

#women shoes
women_shoes = [itm_womenshoes_1,itm_womenshoes_3,itm_womenshoes_4] #shoes and boots all factions
#total bare legs
women_shoes2 = [itm_womenshoes_5,itm_womenshoes_8] #shoes and boots pictish
#irish shoes
women_shoes3 = [itm_womenshoes_6,itm_womenshoes_7,itm_womenshoes_8] #shoes and boots pictish
#quality boots
women_shoes4 = [itm_womenshoes_2] #shoes and boots pictish
##################################
###TUNICS
#tunics for monks and priest
monk_tunic = [itm_robe3,itm_robe4,itm_robe5,itm_robe8]#monk robe
pagan_tunic = [itm_robe6,itm_robe7]#pagan priest robe
abbot_tunic = [itm_robe,itm_robe2]#monk robe
priest_tunic = [itm_priest1,itm_priest2]#priest robe

#childs
child_tunic = [itm_red_tourney_armor,itm_blue_tourney_armor,itm_arena_armor_yellow,itm_hoodtunic_01,itm_yellow2_cloak,itm_gaeltunic_5woman,itm_bl_tunic06] #tunics 1
child_tunic2 = [itm_btunic_4,itm_green_tourney_armor,itm_gold_tourney_armor,itm_hoodtunic_04,itm_gael_tunic_03,itm_gaeltunic_6woman,itm_btunic_13,itm_bl_tunic06] #tunics 1

##Lowest class tunic and slaves tunic 
poor_tunic = [itm_btunic_8woman,itm_ptunic_1woman,itm_ptunic_2woman,itm_ptunic_3woman] #tunics 1
poor_tunic2 = [itm_ptunic_4woman,itm_ptunic_5woman,itm_ptunic_6woman,itm_ptunic_7woman] 
###common base tunics
common_hoodtunic = [itm_hoodtunic_01,itm_hoodtunic_02,itm_hoodtunic_03,itm_hoodtunic_04] #tunics with hoods1
common_hoodtunic2 = [itm_hoodtunic_05,itm_hoodtunic_06,itm_hoodtunic_07,itm_btunic_1woman] 

frisian_tunics = [itm_btunic_3woman,itm_btunic_4woman,itm_gaeltunic_1woman,itm_gaeltunic_2woman,itm_gaeltunic_3woman] 
frisian_tunics2 = [itm_yellow_cloak,itm_btunic_5woman,itm_btunic_6woman,itm_gaeltunic_7woman,itm_gaeltunic_8woman,itm_gaeltunic_6woman,itm_gaeltunic_5woman] 
frisian_lightarmor = [itm_gaeltunic_4woman,itm_long_tunic1] 

bear_berserker = [itm_britontunic_1woman,itm_britontunic_2woman,itm_britontunic_3woman,itm_britontunic_4woman] 
wolf_berserker = [itm_britontunic_5woman,itm_britontunic_6woman,itm_britontunic_7woman,itm_britontunic_8woman] 


##Vikings
common_poor_tunic = [itm_btunic_1,itm_btunic_2,itm_btunic_3,itm_btunic_4,itm_btunic_5,itm_btunic_6,itm_btunic_7] #tunics 1
common_notunic_norse = [itm_arena_armor_blue,itm_picts_tunic_09,itm_picts_tunic_10,itm_picts_tunic_11] #tunics 1
common_tunic = [itm_btunic_8,itm_btunic_9,itm_btunic_3,itm_btunic_4] #tunics 1
common_tunic2 = [itm_btunic_13,itm_btunic_14,itm_btunic_11,itm_btunic_5] 
norse_lightarmor = [itm_btunic_15,itm_btunic_16,itm_btunic_12] 
#High class, colors elite red, purple... Vikings. Nobleman and kings
elite_tunic = [itm_btunic_14,itm_btunic_11,itm_btunic_13] #tunics 

#saxons
saxon_tunic = [itm_arena_armor_yellow,itm_hoodtunic_08,itm_bl_tunic01,itm_bl_tunic04,itm_bl_tunic05] #tunics basic poor
saxon_tunic2 = [itm_red_cloak,itm_bl_tunic06,itm_bl_tunic07,itm_bl_tunic08,itm_bl_tunic10,itm_bl_tunic11,itm_bl_tunic12] #tunics medium
saxon_lightarmor = [itm_bl_tunic02,itm_bl_tunic03,itm_bl_tunic09,itm_nobleman_outfit] #
#angles
angles_basic_tunic = [itm_arena_armor_green,itm_gael_tunic_04,itm_ptunic_1,itm_ptunic_3,itm_ptunic_4,itm_ptunic_5,itm_ptunic_6,itm_yellow2_cloak] # 
angles_richtunic = [itm_gael_tunic_03,itm_ptunic_6,itm_ptunic_7,itm_ptunic_8,itm_ptunic_10,itm_ptunic_11,itm_btunic_7woman] #
angles_lightarmor = [itm_ptunic_2,itm_ptunic_9,itm_ptunic_12,itm_btunic_2woman] #

#common, warriors and elite britons only
briton_basic_tunic = [itm_briton_tunic1,itm_briton_tunic2,itm_briton_tunic3,itm_briton_tunic4] #tunics 
briton_notunic_archers = [itm_arena_armor_white] #tunics 
briton_tunic = [itm_briton_tunic6,itm_briton_tunic9,itm_briton_tunic11,itm_briton_tunic14] # 
briton_tunic2 = [itm_picts_tunic_13,itm_briton_tunic7,itm_briton_tunic5,itm_briton_tunic10,itm_briton_tunic12,itm_briton_tunic9] #  
briton_tunic3 = [itm_briton_tunic13,itm_briton_tunic5,itm_briton_tunic4,itm_briton_tunic3,itm_leather_cloak,itm_blue_cloak] #tunics 
britons_lightarmor = [itm_picts_tunic_12,itm_briton_tunic8] #

#common, warriors and elite irish only
irish_hood = [itm_briton_tunic20,itm_briton_tunic21,itm_briton_tunic22,itm_briton_tunic23] 
irish_capatrousers = [itm_celta_capa1,itm_celta_capa2,itm_celta_capa3,itm_celta_capa4] #
irish_tunic = [itm_gael_tunic_07,itm_gael_tunic_08,itm_gael_hoodtunic_09] #tunics + cloaked tunics
irish_tunic2 = [itm_briton_tunic28,itm_gael_hoodtunic_10,itm_gael_tunic_05,itm_gael_tunic_06] #tunics + cloaked tunics
irish_tunic3 = [itm_briton_tunic24,itm_briton_tunic25,itm_briton_tunic26,itm_briton_tunic27,itm_gael_hoodtunic_11] #elite
irish_hoodtunic = [itm_gael_tunic_08,itm_gael_hoodtunic_09,itm_gael_hoodtunic_10,itm_gael_hoodtunic_11] #tunics square big cloaked tunic
irish_brattunic = [itm_brat1,itm_brat2] #naked bosy with cloaks Elite.
irish_lightarmor = [itm_gael_hoodtunic_12,itm_brat3,itm_brat4] #
#pictish
pictish_tunic = [itm_gael_tunic_01,itm_gael_tunic_02,itm_briton_tunic15,itm_briton_tunic16,itm_briton_tunic17,itm_linen_tunic] #tunics 
pictish_tunic2 = [itm_picts_hoodtunic_11,itm_picts_hoodtunic_12,itm_briton_tunic18,itm_picts_hoodtunic_13,itm_picts_hoodtunic_07] #tunics 
pictish_hoodnaked = [itm_picts_hoodtunic_03,itm_picts_hoodtunic_04,itm_picts_hoodtunic_05,itm_picts_hoodtunic_06] #naked bosy with piciths hoods.
pictish_hoodtunic = [itm_picts_hoodtunic_15,itm_picts_hoodtunic_16,itm_picts_hoodtunic_14,itm_picts_hoodtunic_17] #tunics square big cloaked tunic
pictish_painted = [itm_pictish_painted1,itm_pictish_painted2,itm_pictish_painted3,itm_pictish_painted4,itm_picts_hoodtunic_01,itm_picts_hoodtunic_02] #tunics square big cloaked tunic
pictish_lightarmor = [itm_briton_tunic19,itm_green_cloak,itm_picts_hoodtunic_18] #
##########################
#Women tunics
saxon_women = [itm_woman_saxon1,itm_woman_saxon2,itm_woman_saxon3,itm_woman_saxon4,itm_woman_saxon5,itm_woman_saxon6] #tunics common
saxon_women2 = [itm_woman_saxon7,itm_woman_saxon8,itm_woman_saxon9,itm_woman_saxon10,itm_woman_saxon11] #tunics common
saxon_richwomen = [itm_richwoman_saxon2,itm_richwoman_saxon3,itm_richwoman_saxon4,itm_richwoman_saxon6,itm_richwoman_saxon7,itm_richwoman_saxon8] #tunics rich
saxon_veryrichwomen = [itm_queenwoman_saxon] #tunics very rich

gael_women = [itm_pict_long_tunic1,itm_pict_long_tunic2,itm_pict_long_tunic3,itm_pict_long_tunic4,itm_pict_long_tunic5,itm_pict_long_tunic6] #tunics common
gael_richwomen = [itm_queenpict_long_tunic,itm_pict_long_tunic2,itm_pict_long_tunic3,itm_pict_long_tunic4,itm_pict_long_tunic5,itm_pict_long_tunic6] #tunics rich
pictish_veryrichwomen = [itm_pict_richlong_tunic1,itm_pict_richlong_tunic2,itm_pict_richlong_tunic3] #tunics very rich

norse_women = [itm_woman_norse1,itm_woman_norse2,itm_woman_norse3,itm_woman_norse4,itm_woman_norse5,itm_woman_norse6] #tunics common
norse_richwomen = [itm_richwoman_norse1,itm_richwoman_norse2,itm_richwoman_norse3,itm_richwoman_norse4] #tunics rich

#veils
commonveil_women = [itm_veil_a,itm_veil_b,itm_veil_c,itm_veil_d,itm_veil_e,itm_veil_f] #veil common
richveil_women = [itm_elite_veil_1,itm_elite_veil_2,itm_elite_veil_3,itm_elite_veil_4] #veil rich
saxonveil_women = [itm_common_veil_a,itm_common_veil_b,itm_common_veil_c,itm_common_veil_d,itm_common_veil_e,itm_common_veil_f] #veil common
richsaxonveil_women = [itm_elite_veil_5,itm_elite_veil_6,itm_elite_veil_7,itm_elite_veil_8] #veil rich
##########################
##Armor mails
commonshort_mail = [itm_mail_shirt_1,itm_mail_shirt_3,itm_mail_shirt_12,itm_mail_shirt_13]##short mail
commonlong_mail = [itm_mail_shirt_12_1,itm_mail_shirt_12_2,itm_mail_shirt_12_3,itm_mail_shirt_12_4,itm_byrnie3]##long mail
common_mail = [itm_byrnie,itm_mail_shirt_12_1,itm_mail_shirt_12_2,itm_mail_shirt_3]##long mail
pictishlong_mail = [itm_mail_shirt_6,itm_mail_shirt_7,itm_mail_shirt_11_3,itm_mail_shirt_2,itm_mail_shirt_5]##long mail
irishlong_mail = [itm_byrnie9,itm_byrnie10,itm_byrnie36,itm_byrnie37,itm_byrnie38]##long mail
britonlong_mail = [itm_byrnie4,itm_byrnie6,itm_byrnie13,itm_byrnie14]##short mail ELITE Blue steel
anglelong_mail = [itm_byrnie23,itm_byrnie24,itm_byrnie25,itm_byrnie26]##long mail 
vikingshort_mail = [itm_byrnie16,itm_byrnie17]##short mail
vikinglong_mail = [itm_byrnie18,itm_byrnie19,itm_byrnie31,itm_byrnie32]##long mail
frisianshort_mail = [itm_byrnie2,itm_mail_shirt,itm_byrnie20,itm_mail_shirt_4]##short mail
frisianlong_mail = [itm_mail_shirt_11_2,itm_byrnie35]##long mail
saxonlong_mail = [itm_mail_shirt_13_3,itm_byrnie5,itm_byrnie21,itm_byrnie22]##long mail

vikingnoble_mail = [itm_byrnie33,itm_byrnie34]##long mail
frisiannoble_mail = [itm_byrnie7,itm_byrnie8]##long mail
anglenoble_mail = [itm_byrnie28,itm_byrnie30,itm_byrnie27,itm_byrnie29]##long mail 
saxonnoble_mail = [itm_mail_shirt_13_4,itm_mail_shirt_5_2,itm_mail_shirt_13_1,itm_mail_shirt_13_2]##long mail
britonnoble_mail = [itm_mail_shirt_5_1,itm_mail_shirt_10,itm_mail_shirt_11,itm_byrnie15]##short mail ELITE Blue steel
pictishnoble_mail = [itm_mail_shirt_8,itm_mail_shirt_9]##short mail
irishnoble_mail = [itm_byrnie11,itm_byrnie12]##


lamelar_armor = [itm_lamellar_armor2,itm_lamellar_armor]##long mail
animals_mail = [itm_addon_mail4,itm_addon_mail5,itm_addon_mail6,itm_addon_mail7]##animal mail
################################
#Gambeson (light armor)
#jacket-gameson corto irish
pictish_shortgambeson = [itm_gambeson1cloak,itm_gambeson1gael,itm_gambeson2gael,itm_gambeson3gael,itm_gambeson4gael]##gael corto1
pictish_shortgambeson2 = [itm_gambeson2cloak,itm_gambeson5gael,itm_gambeson6gael,itm_gambeson7gael,itm_gambeson8gael]##gael corto1
irish_shortgambeson = [itm_gambeson12gael,itm_gambeson13gael,itm_gambeson14gael,itm_gambeson15gael,itm_gambeson16gael]##gael short + some with cloaks
irish_shortgambeson2 = [itm_gambeson6cloak,itm_gambeson5cloak,itm_gambeson9gael,itm_gambeson10gael,itm_gambeson11gael]##gael short + some with cloaks

#short gambeson
common_shortgambeson = [itm_gambeson21,itm_gambeson22,itm_gambeson23,itm_gambeson24]
saxon_shortgambeson = [itm_gambeson1,itm_gambeson2,itm_gambeson3,itm_gambeson32,itm_gambeson6]
saxon_shortgambeson2 = [itm_gambeson7,itm_gambeson9,itm_gambeson15,itm_gambeson18]
angle_shortgambeson = [itm_gambeson45,itm_gambeson17,itm_gambeson10,itm_gambeson11]
briton_shortgambeson = [itm_gambeson12,itm_gambeson16]
viking_shortgambeson = [itm_gambeson5,itm_gambeson8,itm_gambeson13,itm_gambeson14]
frisian_shortgambeson = [itm_gambeson19,itm_gambeson20,itm_gambeson3cloak,itm_gambeson4cloak]
#medium and long gambeson
common_gambeson = [itm_gambeson30,itm_gambeson31,itm_gambeson47,itm_gambeson48]
angle_gambeson = [itm_gambeson26,itm_gambeson28,itm_gambeson34,itm_gambeson39]
briton_gambeson = [itm_gambeson36,itm_gambeson37,itm_gambeson38,itm_gambeson40,itm_gambeson41,itm_gambeson42]
viking_gambeson = [itm_gambeson25,itm_gambeson27,itm_gambeson29,itm_gambeson4,itm_gambeson35,itm_gambeson43]
frisian_gambeson = [itm_gambeson33,itm_gambeson44,itm_gambeson46]
####################
# hats Gorros
common_female_hats = [itm_hood_01,itm_hood_02]
common_phrygian = [itm_phrygian1,itm_phrygian2,itm_phrygian3,itm_phrygian4,itm_phrygian5,itm_phrygian6]##Phrygian poor
common_phrygian2 = [itm_phrygian7,itm_phrygian8,itm_phrygian9,itm_phrygian10,itm_phrygian11,itm_phrygian12,itm_phrygian13]##Phrygian normal
decorated_phrygian = [itm_phrygian14,itm_phrygian15,itm_phrygian16,itm_phrygian17]##Phrygian elite
###########################
##Yelmos
###
#viking basic
viking_common_helmets_old = [itm_vikingold_helm,itm_vikingold_helm3,itm_vikingold_helm5,itm_vikingold_helm7,itm_vikingold_helm9,itm_vikingold_helm11,itm_vikingold_helm13]##old helmet, rusty
viking_common_helmets_old2 = [itm_vikingold_helm2,itm_vikingold_helm4,itm_vikingold_helm6,itm_vikingold_helm8,itm_vikingold_helm10,itm_vikingold_helm12,itm_vikingold_helm14]##old helmet, rusty
viking_common_helmets = [itm_viking_helm,itm_viking_helm3,itm_viking_helm5,itm_viking_helm7,itm_viking_helm9,itm_viking_helm11,itm_viking_helm13]##v helmet, normal
viking_common_helmets2 = [itm_viking_helm2,itm_viking_helm4,itm_viking_helm6,itm_viking_helm8,itm_viking_helm10,itm_viking_helm12,itm_viking_helm14]##v helmet, normal
#viking complete
viking_complete_helmets_old = [itm_vikingold_helm15,itm_vikingold_helm17,itm_vikingold_helm19,itm_vikingold_helm21,itm_vikingold_helm23]##old helmet, rusty
viking_complete_helmets_old2 = [itm_vikingold_helm16,itm_vikingold_helm18,itm_vikingold_helm20,itm_vikingold_helm22,itm_vikingold_helm24]##old helmet, rusty
viking_complete_helmets = [itm_viking_helm15,itm_viking_helm17,itm_viking_helm19,itm_viking_helm21,itm_viking_helm23]##old helmet, rusty
viking_complete_helmets2 = [itm_viking_helm16,itm_viking_helm18,itm_viking_helm20,itm_viking_helm22,itm_viking_helm24]##old helmet, rusty
#viking elite gjermundu
viking_elite_helmets_old = [itm_vikingold_elitehelm1,itm_vikingold_elitehelm3,itm_vikingold_elitehelm5,itm_vikingold_elitehelm7]##old helmet, rusty
viking_elite_helmets_old2 = [itm_vikingold_elitehelm2,itm_vikingold_elitehelm4,itm_vikingold_elitehelm6]##old helmet, rusty
viking_elite_helmets = [itm_viking_elitehelm1,itm_viking_elitehelm3,itm_viking_elitehelm5,itm_viking_elitehelm7]##old helmet, rusty
viking_elite_helmets2 = [itm_viking_elitehelm2,itm_viking_elitehelm4,itm_viking_elitehelm6]##old helmet, rusty
#viking noble
viking_nobleman_helmets = [itm_viking_noblehelm1,itm_viking_noblehelm2,itm_viking_noblehelm3]##old helmet, rusty
viking_highquality_helmets = [itm_vikingold_elitehelm8,itm_vikingold_elitehelm9]##
####
####
#pictish and irish coopergate
pictish_common_helmets = [itm_angle_helmet2,itm_angle_helmet5,itm_angle_helmet4]##irish and pictish
pictish_elite_helmets = [itm_angle_helmet3,itm_angle_helmet6]##irish and pictish elite
pictish_noble_helmets = [itm_angle_helmet1,itm_noble_helm_smith]##

###Britons
britons_common_old_helmets = [itm_briton_helm3,itm_briton_helm4,itm_briton_helm7,itm_briton_helm8,itm_briton_helm11,itm_briton_helm12]##britons
britons_common_old_helmets2 = [itm_briton_helm22,itm_briton_helm23,itm_briton_helm24,itm_briton_helm28,itm_briton_helm29,itm_briton_helm30]##britons
britons_elite_old_helmets = [itm_briton_helm16,itm_briton_helm17,itm_briton_helm18,itm_briton_helm38,itm_briton_helm39,itm_briton_helm40]##britons elite

britons_common_helmets = [itm_briton_helm,itm_briton_helm2,itm_briton_helm5,itm_briton_helm6,itm_briton_helm9,itm_briton_helm10,itm_briton_helm31,itm_briton_helm32]##britons
britons_common_helmets2 = [itm_briton_helm19,itm_briton_helm20,itm_briton_helm21,itm_briton_helm25,itm_briton_helm26,itm_briton_helm27]##britons
britons_elite_helmets = [itm_briton_helm13,itm_briton_helm14,itm_briton_helm15,itm_briton_helm35,itm_briton_helm36,itm_briton_helm37]##britons elite

britons_nobleman_helmets = [itm_briton_helm33,itm_briton_helm34]##britons noble

#angles, saxons
saxons_common_old_helmets = [itm_spangenhelm_3,itm_spangenhelm_4,itm_spangenhelm_7,itm_spangenhelm_8,itm_spangenhelm_11,itm_spangenhelm_12,itm_spangenhelm_33,itm_spangenhelm_34]##saxons
saxons_common_old_helmets2 = [itm_spangenhelm_22,itm_spangenhelm_23,itm_spangenhelm_24,itm_spangenhelm_28,itm_spangenhelm_29,itm_spangenhelm_30]##saxons
saxons_elite_old_helmets = [itm_spangenhelm_16,itm_spangenhelm_17,itm_spangenhelm_18,itm_spangenhelm_38]##saxons elite

saxons_common_helmets = [itm_spangenhelm_1,itm_spangenhelm_2,itm_spangenhelm_5,itm_spangenhelm_6,itm_spangenhelm_9,itm_spangenhelm_10,itm_spangenhelm_31,itm_spangenhelm_32]##saxons
saxons_common_helmets2 = [itm_spangenhelm_19,itm_spangenhelm_20,itm_spangenhelm_21,itm_spangenhelm_25,itm_spangenhelm_26,itm_spangenhelm_27]##saxons
saxons_elite_helmets = [itm_spangenhelm_13,itm_spangenhelm_14,itm_spangenhelm_15,itm_spangenhelm_35,itm_spangenhelm_36,itm_spangenhelm_37]##saxons elite

saxons_noblequality_helmets = [itm_spangenhelm_39,itm_spangenhelm_40]#
##########################
###weapons
#seax
#britons, irish and pictish
basic_knives = [itm_knife,itm_knife2] #knives
basic_knives2 = [itm_knife3,itm_knife5] #knives
basic_knives3 = [itm_knife4,itm_knife5] #knives
#vikings and saxons
basic_longseax = [itm_longseax3,itm_longseax4] #spearmen
basic_longseax2 = [itm_longseax5,itm_longseax1,itm_longseax2] #spearmen
basic_longseaxnorse = [itm_longseax6,itm_longseax7,itm_longseax8] #only norse
basic_longseaxnorse2 = [itm_longseax9,itm_longseax10] #only norse
basic_seax = [itm_seax_1,itm_seax_2] #swordmen and axemen
basic_seax2 = [itm_seax_4,itm_seax_5] #swordmen and axemen
basic_seax3 = [itm_seax_4,itm_seax_3] #swordmen and axemen
############################
#swords
#saxons and vikings
common_sword = [itm_spatha,itm_spatha_2,itm_spatha_3,itm_spatha_4,itm_spatha_5,itm_spatha_6]##normales
common_sword2 = [itm_spatha_7,itm_spatha_8,itm_sword,itm_sword_2,itm_sword_3,itm_sword_4,itm_new_sword6]##normales
common_shortswordvk = [itm_sword_5,itm_sword_6,itm_sword_7,itm_sword_8,itm_new_sword1]##vikingos
common_shortswordvk2 = [itm_new_sword3,itm_new_sword4,itm_new_sword5,itm_new_sword2]##vikingos
noble_saxonvik_sword = [itm_noble_sword,itm_noble_sword_2,itm_noble_sword_3,itm_noble_sword_4,itm_noble_sword_5,itm_noble_sword_6]##nobles, lords, reyes
#britons
common_sword5 = [itm_old_swordv,itm_old_swordv2,itm_old_swordv3,itm_old_swordv4,itm_old_swordv5,itm_old_swordv6,itm_old_swordv7]##britons
elite_britons_sword = [itm_noble_sword_7,itm_noble_sword_8,itm_noble_sword_9,itm_noble_sword_10,itm_noble_sword_11,itm_noble_sword_12,itm_noble_sword_13]
#irish and pictish
noble_gael_sword = [itm_irish_long_sword1,itm_irish_long_sword2,itm_irish_long_sword1,itm_irish_long_sword2,itm_irish_long_sword1,itm_irish_long_sword2]##nobles, lords, reyes
common_gael_sword = [itm_irish_long_sword3,itm_irish_long_sword4,itm_irish_long_sword5,itm_irish_long_sword6,itm_irish_long_sword7,itm_irish_long_sword8]##common elite
short_gael_sword = [itm_irish_short_sword1,itm_irish_short_sword2,itm_irish_short_sword3,itm_irish_short_sword1,itm_irish_short_sword2,itm_irish_short_sword3]##short sword
champion_gael_sword = [itm_championsword1,itm_championsword2,itm_championsword1,itm_championsword2]##only champion goidel, no pictish
############################
##Axes
#commons alls factions less irish and pictish
common_axes = [itm_one_handed_war_axe_b,itm_axe,itm_axe_2,itm_axe_8,itm_hand_axe,itm_one_handed_war_axe_a,itm_one_handed_war_axe_d]##mezcladas comunes
common_axes2 = [itm_hatchet,itm_one_handed_war_axe_a,itm_one_handed_war_axe_c,itm_axe_7,itm_axe_8,itm_axe_9,itm_axe_6]##mezcladas comunes
common_axes3 = [itm_hatchet,itm_axe_10,itm_one_handed_war_axe_c,itm_axe_2,itm_one_handed_war_axe_b]##mezcladas comunes
common_axes4 = [itm_hand_axe,itm_axe_10,itm_hatchet,itm_axe,itm_axe_9,itm_axe_4,itm_one_handed_war_axe_e]##mezcladas comunes
twohanded_axes = [itm_axe_3,itm_axe_4,itm_one_handed_war_axe_e,itm_one_handed_war_axe_f]##2handed
#irish and pictish
gael_axes = [itm_pictish_hatchet,itm_pictish_hatchet2,itm_pictish_hatchet4,itm_pictish_hatchet5,itm_pictish_hatchet11,itm_pictish_hatchet12]## gael pictish axes
gael_axes2 = [itm_pictish_hatchet13,itm_pictish_hatchet14,itm_pictish_hatchet15,itm_pictish_hatchet16,itm_pictish_hatchet6,itm_pictish_hatchet3]##gael pictish axes
pictish_axes = [itm_pictish_hatchet5,itm_pictish_hatchet6,itm_pictish_hatchet7,itm_pictish_hatchet8,itm_pictish_hatchet9,itm_pictish_hatchet10]##only pictish
twohanded_irishaxes = [itm_axe_3,itm_axe_4]##2handed
####################
#basic
basic_weapons = [itm_wooden_stick,itm_club_hard] #basic club
basic_weapons2 = [itm_staff,itm_quarter_staff,itm_pitch_fork,itm_battle_fork] #hasta
###################
#Spears
###saonxs and vikings
light_spears = [itm_light_spear1,itm_light_spear2,itm_light_spear3,itm_light_spear4] #short spears
war_spears = [itm_war_spear1,itm_war_spear2,itm_war_spear3,itm_heavy_spear1,itm_heavy_spear2] #medium spears
heavy_spears = [itm_long_war_spear1,itm_long_war_spear2] #long spears
#britons, irish and pictish
long_lightspears = [itm_long_light_spear1,itm_long_light_spear2] #long spears
long_warspears = [itm_long_heavy_spear1,itm_long_war_spear2] #long spears
long_heavyspears = [itm_heavy_spear3,itm_long_heavy_spear2,itm_long_war_spear1] #long spears
####################
#Throwing weapons
#alls factions hevy infantry
javelin_only = [itm_javelin]
javelin_normal = [itm_throwing_spears, itm_throwing_spears2]
javelin_skirmishes = [itm_javelin_skirmishes]
irish_skirmishes = [itm_javelin_skirmishesel]
horseman_skirmishes = [itm_javelin_jinetes]
basic_throwing = [itm_stones]
########################
###BOWS
common_archer = [itm_long_bow,itm_long_bow,itm_long_bow,itm_arrows,itm_khergit_arrows]
elite_archer = [itm_long_bow2,itm_long_bow3,itm_long_bow2,itm_long_bow3,itm_long_bow2,itm_long_bow3,itm_arrows,itm_khergit_arrows,itm_barbed_arrows,itm_bodkin_arrows]
pictish_crossbow = [itm_hunting_crossbow,itm_hunting_crossbow,itm_hunting_crossbow,itm_bolts,itm_bolts2,itm_bolts3,itm_bolts4]
slings_common = [itm_sling,itm_sling2,itm_sling3,itm_fustibalus1,itm_fustibalus2,itm_sling_rock1]
slings_elite = [itm_sling_militar,itm_fustibalus_military,itm_sling_lead]
#arrows and bolts
#################
#others
standard_normal = [itm_standard]
standard_dragon = [itm_standard_dragon]
common_horn = [itm_horn]
#####################
###Shields
#britons
britons_convexshields = [itm_shield_1,itm_shield_2,itm_shield_3,itm_shield_4,itm_shield_5,itm_shield_6,itm_shield_6_2]
britons_tabconvexshields = [itm_tab_shield_round_05_device,itm_tab_shield_round_05_nodevice,itm_tab_shield_round_06_device,itm_tab_shield_round_06_nodevice,itm_tab_shield_round_08_device,itm_tab_shield_round_08_nodevice,itm_tab_shield_round_10_device,itm_tab_shield_round_10_nodevice,itm_tab_shield_round_11_device,itm_tab_shield_round_11_nodevice]
#norse
viking_shields = [itm_viking_shield_round_01,itm_viking_shield_round_02,itm_viking_shield_round_03,itm_viking_shield_round_04,itm_viking_shield_round_05,itm_viking_shield_round_06,itm_viking_shield_round_14,itm_viking_shield_round_15]
viking_shields2 = [itm_viking_shield_round_07,itm_viking_shield_round_08,itm_viking_shield_round_09,itm_viking_shield_round_10,itm_viking_shield_round_11,itm_viking_shield_round_12,itm_viking_shield_round_13]
viking_tabshields = [itm_tab_shield_round_04_device,itm_tab_shield_round_04_nodevice,itm_tab_shield_round_07_device,itm_tab_shield_round_07_nodevice,itm_tab_shield_round_09_device,itm_tab_shield_round_09_nodevice,itm_tab_shield_round_12_device,itm_tab_shield_round_12_nodevice]                         
#saxons and angles
saxons_shields = [itm_viking_shield_round_18,itm_viking_shield_round_19,itm_viking_shield_round_20]
angles_shields = [itm_viking_shield_round_16,itm_viking_shield_round_17,itm_viking_shield_round_21]
saxons_tabshields = [itm_tab_shield_round_01_device,itm_tab_shield_round_01_nodevice,itm_tab_shield_round_02_device,itm_tab_shield_round_02_nodevice,itm_tab_shield_round_03_device,itm_tab_shield_round_03_nodevice,]
#pictish
pictish_squareshields = [itm_squaresh_1,itm_squaresh_2,itm_squaresh_3,itm_squaresh_4,itm_squaresh_5,itm_squaresh_6]
pictish_hshields = [itm_h_shield1,itm_h_shield2,itm_h_shield3,itm_h_shield4,itm_h_shield5,itm_h_shield6]
#pictish_tabroundshields = [itm_tab_shield_small_round_c]
#Irish
irish_bigshields = [itm_gael_bigroundshield_01,itm_gael_bigroundshield_02,itm_gael_bigroundshield_03,itm_gael_bigroundshield_04,itm_gael_bigroundshield_05,itm_gael_bigroundshield_06,itm_gael_bigroundshield_07]
irish_smallroundshields = [itm_small_roundsh1,itm_small_roundsh2,itm_small_roundsh3,itm_small_roundsh4,itm_small_roundsh5,itm_small_roundsh6]
#irish_tabroundshields = [itm_tab_shield_small_round_c]

###bandits and mercenaries
mercenaries_roundshields = [itm_shield_11,itm_shield_12,itm_shield_13,itm_shield_14,itm_shield_15,itm_shield_16,itm_shield_17,itm_shield_18,itm_shield_20]
frankish_roundshields = [itm_shield_21]
cantabros_roundshields = [itm_shield_19]
astures_roundshields = [itm_arena_shield_blue]
galaicos_roundshields = [itm_arena_shield_green]
norwegian_roundshields = [itm_shield_18] #whites shields
danish_roundshields = [itm_shield_19] #black shields
swedish_roundshields = [itm_shield_10] #unique shields
#berserkr shields
berserkr_shields = [itm_shield_7,itm_shield_8,itm_shield_9]


##############ITEMS FINISH

troops = [
  ["player","Player","Player",tf_hero|tf_unmoveable_in_party_window,no_scene,reserved,fac_player_faction,
   [],
   str_4|agi_4|int_4|cha_4,wp(30),0,0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["multiplayer_profile_troop_male","multiplayer_profile_troop_male","multiplayer_profile_troop_male", tf_hero|tf_guarantee_all, 0, 0,fac_commoners,
   [itm_ptunic_5, itm_carbatinae_1],
   0, 0, 0, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["multiplayer_profile_troop_female","multiplayer_profile_troop_female","multiplayer_profile_troop_female", tf_hero|tf_female|tf_guarantee_all, 0, 0,fac_commoners,
   [itm_woman_saxon1, itm_carbatinae_1],
   0, 0, 0, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["temp_troop","Temp Troop","Temp Troop",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_inventory_management_10,0],
##  ["game","Game","Game",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
##  ["unarmed_troop","Unarmed Troop","Unarmed Troops",tf_hero,no_scene,reserved,fac_commoners,[itm_arrows,itm_long_bow],def_attrib|str_14,0,knows_common|knows_power_draw_2,0],

####################################################################################################################
# Troops before this point are hardwired into the game and their order should not be changed!
####################################################################################################################
  ["find_item_cheat","find_item_cheat","find_item_cheat",tf_hero|tf_is_merchant,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_inventory_management_10,0],
  ["random_town_sequence","Random Town Sequence","Random Town Sequence",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_athletics_3|knows_power_throw_1|knows_inventory_management_10,0],
  ["tournament_participants","Tournament Participants","Tournament Participants",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_athletics_3|knows_power_throw_1|knows_inventory_management_10,0],
  ["tutorial_maceman","Maceman","Maceman",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_tutorial_club,itm_btunic_16,itm_carbatinae_1], #cambiado chief
   str_6|agi_6|level(1),wp(50),knows_common,mercenary_face_1,mercenary_face_2],
  ["tutorial_archer","Archer","Archer",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   [itm_tutorial_short_bow,itm_tutorial_arrows,itm_linen_tunic,itm_carbatinae_1], #cambiado chief
   str_6|agi_6|level(5),wp(100),knows_archer_basic,mercenary_face_1,mercenary_face_2],
  ["tutorial_swordsman","Swordsman","Swordsman",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_tutorial_sword,itm_btunic_16,itm_carbatinae_1], #cambiado chief
   str_6|agi_6|level(5),wp(80),knows_common,mercenary_face_1,mercenary_face_2],

  ["novice_fighter","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_carbatinae_1], #cambiado chief
   def_attrib|level(18),wp(140),knows_warrior_basic,man_face_middle_1, man_face_old_2],
  ["regular_fighter","Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_carbatinae_1],
   def_attrib2|level(23),wp(180),knows_warrior_basic2,man_face_middle_1, man_face_old_2],
  ["veteran_fighter","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,0,fac_commoners,
   [itm_carbatinae_1],
   def_attrib3|level(29),wp(300),knows_warrior_veteran,man_face_middle_1, man_face_old_2],
  ["champion_fighter","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_carbatinae_1],
   def_attrib3|level(31),wp(380),knows_warrior_elite,man_face_middle_1, man_face_old_2],
#cambios chief end
  ["arena_training_fighter_1","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_carbatinae_1],
   str_7|agi_6|level(15),wp(100),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_2","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_carbatinae_1],
   str_8|agi_6|level(17),wp(120),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_3","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_carbatinae_1],
   str_12|agi_12|level(23),wp(170),knows_weapon_master_5|knows_ironflesh_5|knows_athletics_6|knows_power_strike_2|knows_shield_2|knows_inventory_management_2|knows_power_throw_3|knows_riding_1,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_4","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_carbatinae_1],
   str_12|agi_12|level(23),wp(170),knows_weapon_master_5|knows_ironflesh_5|knows_athletics_6|knows_power_strike_2|knows_shield_2|knows_inventory_management_2|knows_power_throw_3|knows_riding_1,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_5","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_carbatinae_1],
   str_12|agi_12|level(23),wp(170),knows_weapon_master_5|knows_ironflesh_5|knows_athletics_6|knows_power_strike_2|knows_shield_2|knows_inventory_management_2|knows_power_throw_3|knows_riding_1,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_6","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_carbatinae_1],
   str_14|agi_14|level(27),wp(230),knows_weapon_master_7|knows_shield_3|knows_inventory_management_3|knows_power_throw_4|knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_7","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_carbatinae_1],
   str_14|agi_14|level(27),wp(230),knows_weapon_master_7|knows_shield_3|knows_inventory_management_3|knows_power_throw_4|knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_8","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_carbatinae_1],
   str_14|agi_14|level(27),wp(230),knows_weapon_master_7|knows_shield_3|knows_inventory_management_3|knows_power_throw_4|knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_9","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_carbatinae_1],
   str_18|agi_18|level(33),wp(270),knows_weapon_master_9|knows_inventory_management_4|knows_power_throw_5|knows_ironflesh_5|knows_power_strike_5|knows_athletics_5|knows_riding_3|knows_shield_4,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_10","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_carbatinae_1],
   str_18|agi_18|level(33),wp(270),knows_weapon_master_9|knows_inventory_management_4|knows_power_throw_5|knows_ironflesh_5|knows_power_strike_5|knows_athletics_5|knows_riding_3|knows_shield_4,mercenary_face_1, mercenary_face_2],
#cambios chief end
  ["cattle","Cattle","Cattle",0,no_scene,reserved,fac_neutral, [], def_attrib|level(1),wp(60),0,mercenary_face_1, mercenary_face_2],

#soldiers:
#This troop is the troop marked as soldiers_begin
  ["farmer","Farmer","Farmers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   []+basic_throwing+slings_common+common_shoes+common_phrygian+poor_tunic2+basic_weapons2,
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],
  ##chief - new troop entry
  ["cantaber_iuventus","Cantabrian Warrior","Cantabrian Raider",tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_armor,no_scene,reserved,fac_commoners,
  []+irish_skirmishes+common_shoes4+commonshort_mail+britons_common_helmets+common_sword+cantabros_roundshields,
   def_attrib3|level(31),wp(380),knows_warrior_elite,man_face_younger_1, man_face_older_2],

  ["asturias_veteran","Asturian Veteran","Asturian Veteran",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,no_scene,reserved,fac_commoners,
  []+javelin_normal+war_brit_shoes1+commonlong_mail+common_shortgambeson+britons_common_helmets+common_sword+astures_roundshields,
   def_attrib3|level(31),wp(380),knows_warrior_elite,man_face_younger_1, man_face_older_2],

  ["gallaecia_warrior","Gallaecian Comes's Guard","Gallaecian Comes's Guard",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,no_scene,reserved,fac_commoners,
  []+javelin_normal+elite_shoes+common_mail+britons_common_helmets+common_sword+galaicos_roundshields,
   def_attrib3|level(31),wp(380),knows_warrior_elite,man_face_middle_1, man_face_old_2],
###
  ["townsman","Townsman","Townsmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
  []+basic_throwing+slings_common+common_hoodtunic2+poor_tunic+basic_weapons+common_shoes,
   def_attrib|level(12),wp(110),knows_common,man_face_younger_1, man_face_older_2],
###mercenaries
  ["watchman","Watchman","Watchmen",tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners,
[]+light_spears+common_shoes2+common_hoodtunic2+mercenaries_roundshields+basic_seax,
   def_attrib|level(18),wpex(145,80,130,30,30,130)|wp_firearm(110),knows_warrior_basic,man_face_younger_1, man_face_older_2],
  ["mercenary_cavalry","Frank Horseman","Frank Horsemen",tf_mounted|tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,no_scene,reserved,fac_commoners, 
   []+long_warspears+javelin_only+common_horse+war_brit_shoes1+saxons_elite_old_helmets+frisianshort_mail+frisianlong_mail+frankish_roundshields+common_sword,
   def_attrib3|level(29),wpex(295,150,310,40,0,285)|wp_firearm(100),knows_warrior_veteran,man_face_younger_1, man_face_older_2],
  ["caravan_guard","Spearman","Spearmen",tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor,no_scene,0,fac_commoners,
[]+war_spears+common_shoes2+common_hoodtunic2+common_shortgambeson+saxons_common_old_helmets+mercenaries_roundshields+basic_seax,
   def_attrib2|level(23),wpex(180,130,190,30,0,170)|wp_firearm(130),knows_warrior_basic2,man_face_younger_1, man_face_older_2],
  ["mercenary_swordsman","Veteran","Veterans",tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,no_scene,reserved,fac_commoners,
[]+war_spears+heavy_spears+common_shoes4+commonshort_mail+common_gambeson+saxons_common_old_helmets+mercenaries_roundshields+basic_seax2,
   def_attrib2|level(26),wpex(220,150,205,50,0,180)|wp_firearm(140),knows_warrior_normal,man_face_younger_1, man_face_older_2],
#chief sailors
  ["regular_sailors","Sailor","Sailors",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   []+slings_common+common_shoes2+common_phrygian2+poor_tunic2+common_hoodtunic+basic_seax3+basic_weapons,
   def_attrib|level(18),wpex(135,80,100,30,30,145)|wp_firearm(155),knows_common|knows_pathfinding_1|knows_tracking_1|knows_navigation_6,man_face_younger_1, man_face_older_2],
#chief acaba
  ["mercenary_horseman","Aquitanian Skirmisher","Aquitanian Skirmishers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,no_scene,reserved,fac_commoners,
  []+common_pony+common_axes+common_shoes2+frisian_tunics+basic_longseax2+horseman_skirmishes,
   def_attrib2|level(26),wpex(180,150,150,50,30,240)|wp_firearm(150),knows_horseman_pictish,man_face_younger_1, man_face_older_2],
  ["mercenary_leader","Old Captain","Old Captains",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   []+javelin_normal+common_shoes4+common_horse+common_sword2+saxons_elite_old_helmets+commonlong_mail+common_gloves+mercenaries_roundshields+basic_seax2,
   def_attrib3|level(31),wp(380),knows_warrior_elite,man_face_younger_1, man_face_older_2],
  ["hired_blade","Svear Warrior","Sviar Warriors",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   []+common_axes4+javelin_normal+elite_norse_boots+common_sword2+viking_elite_helmets+viking_complete_helmets+viking_gambeson+norse_lightarmor+lamelar_armor+common_gloves+swedish_roundshields+basic_seax,
   def_attrib2|level(26),wpex(230,170,190,50,0,205)|wp_firearm(145),knows_warrior_normal,nord_face_younger_1, nord_face_older_2],
  ["mercenary_crossbowman","Finn Archer","Finnas Archers",tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   []+elite_archer+common_shoes4+frisian_tunics2+basic_seax2,
   def_attrib2|level(23),wpex(180,150,165,135,30,100)|wp_firearm(100),knows_archer_basic,nord_face_younger_1, nord_face_older_2],
#mercearies_end is your village contact for reveal assasination quest - Addon.
   ["mercenaries_end","Villager","Villagers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_commoners,
   [itm_javelin_skirmishes,itm_viking_shield_round_16,itm_axe_10,itm_leather_cloak,itm_carbatinae_vc2v,itm_carbatinae_vc1v, itm_briton_tunic26]+saxon_tunic,
  def_attrib2|level(26),wp(220),knows_warrior_normal,mercenary_face_2, nord_face_older_2],
  
  

## FACTION TROOPS ##
# Divided into two sections: available for multiplayer and not
# In general, there are levy (landed) troops. These have steady income so may have better equipment
# And then there are "professional" (companion) troops that attach only to hero parties. These may have the skill and level benefits of experience

########################VIKINGS vikingos
# I took some liberties here. Hirdmenn are the base warrior class, but then we also have their division into unproven (Drenger) and proven (Pegn) warriors. Rekkr is Old Norse, also meaning "warrior."
# Here I have Drenger and Pegn representing higher levels of the landed levy, and Hirdmenn and Rekkr representing the corresponding levels of "professional" soldiers.
# "Landmann," a captain of 40 men and a ship, would probably be a better choice than "Rekkr" at the level indicated.
  ["norse_slave","Norse Freedman (Leysingi)","Norse Freedmen (Leysingja)",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_norse,
   []+basic_throwing+basic_weapons+basic_seax3+common_poor_tunic+common_shoes+common_phrygian,
   def_attrib|level(12),wpex(100,100,100,50,20,95)|wp_firearm(95),knows_common,nord_face_younger_1, nord_face_older_2],
  ["norse_bowman","Norse Bowman (Gestr)","Norse Bowmen (Gestir)",tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_culture_norse,
   []+common_archer+common_shoes2+basic_seax2+common_poor_tunic+common_notunic_norse+common_phrygian,
   def_attrib|level(19),wpex(140,100,100,120,30,140)|wp_firearm(105),knows_archer_basic,nord_face_younger_1, nord_face_older_2],
#elite archer
  ["norse_elitearcher","Norse Warrior Archer (Heimthegi)","Norse Warriors Archers (Heimthegar)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,0,0,fac_culture_norse,
   []+elite_archer+common_axes+war_norse_shoes3+norse_lightarmor+viking_shortgambeson+basic_longseaxnorse+viking_tabshields+viking_common_helmets2+viking_elite_helmets_old+basic_seax2,
   def_attrib2|level(26),wpex(200,150,150,160,30,200)|wp_firearm(105),knows_archer_pictish,nord_face_younger_1, nord_face_older_2],
  ["norse_level0_landed","Norse Freeholder (Boandi)","Norse Freeholders (Bondar)",tf_guarantee_polearm|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_norse,
   []+light_spears+war_norse_shoes1+common_tunic+common_tunic2+viking_shields+javelin_only+viking_common_helmets_old+common_phrygian2+basic_seax,
   def_attrib|level(18),wpex(140,100,130,60,30,140)|wp_firearm(120),knows_warrior_basic,nord_face_younger_1, nord_face_older_2],
  ["norse_level1_landed","Norse Spearman (Drengr)","Norse Spearmen (Drengir)",tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor,0,0,fac_culture_norse,
   []+light_spears+war_norse_shoes1+norse_lightarmor+elite_tunic+viking_shortgambeson+viking_complete_helmets_old+viking_common_helmets+javelin_only+viking_shields2+basic_seax3,
   def_attrib2|level(23),wpex(180,150,185,80,30,160)|wp_firearm(150),knows_warrior_basic2,nord_face_younger_1, nord_face_older_2],
  ["norse_level2_landed","Norse Elite Spearman (Thegn)","Norse Elite Spearmen (Thegnar)",tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_culture_norse,
   []+war_spears+war_norse_shoes2+viking_gambeson+vikingshort_mail+viking_complete_helmets2+viking_complete_helmets+basic_longseaxnorse2+javelin_only+viking_tabshields+basic_seax2,
   def_attrib2|level(26),wpex(220,170,230,80,30,200)|wp_firearm(190),knows_warrior_normal,nord_face_younger_1, nord_face_older_2],
  ["norse_level3_landed","Norse Noble (Hersir)","Norse Nobles (Hersir)",tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_culture_norse,
   []+common_shortswordvk+heavy_spears+common_gloves+elite_norse_boots+vikingnoble_mail+vikinglong_mail+viking_elite_helmets2+viking_nobleman_helmets+javelin_only+viking_tabshields,
   def_attrib3|level(29),wpex(300,270,280,80,30,270)|wp_firearm(200),knows_warrior_veteran,nord_face_younger_1, nord_face_older_2],
  ["norse_level0_companion","Norse Companion (Hirthmathr)","Norse Companions (Hirthmathr)",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_norse, #http://www.questia.com/library/journal/1G1-158623709/pegn-and-drengr-in-the-viking-age
   []+basic_longseaxnorse2+common_axes+javelin_normal+war_norse_shoes1+norse_lightarmor+elite_tunic+viking_shortgambeson+viking_complete_helmets_old2+viking_common_helmets_old2+viking_shields,
   def_attrib2|level(23),wpex(195,150,155,80,30,175)|wp_firearm(150),knows_warrior_basic2,nord_face_younger_1, nord_face_older_2],
   ["norse_level1_companion","Norse Veteran (Rekkr)","Norse Veterans (Rekkar)",tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet,0,0,fac_culture_norse,
   []+common_shortswordvk2+basic_longseaxnorse+common_axes4+javelin_normal+war_norse_shoes2+viking_gambeson+vikingshort_mail+viking_elite_helmets_old2+viking_complete_helmets_old+javelin_normal+viking_tabshields,
   def_attrib2|level(27),wpex(235,160,170,80,30,210)|wp_firearm(190),knows_warrior_normal,nord_face_younger_1, nord_face_older_2],
  ["norse_level2_companion","Norse Bodyguard (Huskarl)","Norse Bodyguards (Huskarlar)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_culture_norse,
   []+basic_longseaxnorse+common_gloves+elite_norse_boots+animals_mail+viking_elite_helmets+viking_complete_helmets+javelin_normal+noble_saxonvik_sword+viking_tabshields,
   def_attrib3|level(31),wpex(385,220,230,80,30,310)|wp_firearm(200),knows_warrior_elite,nord_face_younger_1, nord_face_older_2],
  ["norse_standard_bearer","Standard Bearer (Merkismathr)","Standard Bearer (Merkismathr)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_culture_norse,
    []+war_norse_shoes3+animals_mail+standard_normal+common_trophy,
   def_attrib2|level(26),wpex(235,220,220,80,30,170)|wp_firearm(170),knows_warrior_normal,nord_face_younger_1, nord_face_older_2],
  ["norse_priest","Gothi","Gothar",tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_culture_norse,
    []+pagan_tunic+basic_seax2+basic_weapons+basic_throwing,
   def_attrib|level(12),wpex(105,100,70,20,20,110)|wp_firearm(110),knows_cleric,nord_face_younger_1, nord_face_older_2],
   
#########BRITONS
  ["briton_slave","Briton Serf (Aillt)","Briton Serfs (Aillts)",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_welsh,
   []+slings_common+basic_weapons2+basic_knives2+briton_basic_tunic+briton_notunic_archers+common_shoes,
   def_attrib|level(12),wpex(100,90,90,50,20,110)|wp_firearm(110),knows_common,swadian_face_younger_1, swadian_face_older_2],
  ["briton_level0_landed","Briton Freeman (Bonheddwr)","Briton Freemen (Bonheddwyr)",tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_culture_welsh,
   []+long_lightspears+common_shoes2+briton_tunic+briton_basic_tunic+britons_convexshields+javelin_only+britons_common_old_helmets+basic_knives,
   def_attrib|level(18),wpex(140,100,130,60,30,145)|wp_firearm(120),knows_warrior_basic,swadian_face_younger_1, swadian_face_older_2],
  ["briton_level1_landed","Briton Spearman (Pedyt)","Briton Spearmen (Pedytes)",tf_guarantee_polearm|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_welsh,
   []+long_lightspears+common_shoes3+britons_lightarmor+briton_shortgambeson+briton_tunic2+britons_common_old_helmets2+javelin_only+britons_convexshields+basic_knives2,
   def_attrib2|level(23),wpex(170,130,195,80,30,185)|wp_firearm(160),knows_warrior_basic2,swadian_face_younger_1, swadian_face_older_2],
  ["briton_level2_landed","Briton Elite Spearman (Gwrda)","Briton Elite Spearmen (Gwrdas)",tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_armor,0,0,fac_culture_welsh,
   []+war_brit_shoes1+briton_tunic2+briton_gambeson+britons_common_helmets+long_warspears+javelin_only+britons_tabconvexshields+basic_knives3,
   def_attrib2|level(26),wpex(210,150,240,80,30,215)|wp_firearm(190),knows_warrior_normal,swadian_face_younger_1, swadian_face_older_2],
  ["briton_level3_landed","Briton Noble (Uchelwr)","Briton Nobles (Uchelwyr)",tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_culture_welsh,
   []+long_heavyspears+common_axes4+common_gloves+elite_shoes+britonnoble_mail+britons_elite_helmets+javelin_only+britons_tabconvexshields+basic_knives2,
   def_attrib3|level(29),wpex(290,220,310,80,30,270)|wp_firearm(200),knows_warrior_veteran,swadian_face_younger_1, swadian_face_older_2],
  ["briton_level0_companion","Briton Warrior (Cadwr)","Briton Warriors (Cadwyr)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_culture_welsh,
   [itm_hatchet,itm_axe,itm_hand_axe,itm_axe_2]+common_shoes4+britons_lightarmor+briton_tunic3+briton_shortgambeson+britons_elite_old_helmets+javelin_normal+britons_convexshields+basic_knives,
   def_attrib2|level(23),wpex(190,130,155,80,30,185)|wp_firearm(160),knows_warrior_basic2,swadian_face_younger_1, swadian_face_older_2],
  ["briton_level1_companion","Briton Champion (Campiwr)","Briton Champions (Campgwr)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_culture_welsh,
   [itm_hatchet,itm_axe,itm_hand_axe,itm_axe_2]+common_sword5+javelin_normal+war_brit_shoes2+briton_gambeson+britons_common_helmets2+britons_tabconvexshields+basic_knives2,
   def_attrib2|level(26),wpex(220,150,200,80,30,205)|wp_firearm(190),knows_warrior_normal,swadian_face_younger_1, swadian_face_older_2],
  ["briton_level2_companion","Briton Bodyguard (Teulu)","Briton Bodyguard (Teulus)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_culture_welsh,
   []+elite_britons_sword+common_gloves+elite_brit_boots+britonlong_mail+britons_elite_helmets+javelin_normal+britons_tabconvexshields+basic_knives3,
   def_attrib3|level(29),wpex(295,210,270,80,30,280)|wp_firearm(200),knows_warrior_veteran,swadian_face_younger_1, swadian_face_older_2],
  ["briton_bowman","Briton Skirmisher (Cipryswr)","Briton Skirmishers (Cipryswyr)",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_welsh,
   []+javelin_skirmishes+slings_elite+common_shoes2+briton_basic_tunic+briton_notunic_archers+basic_knives2,
   def_attrib|level(18),wpex(120,80,80,90,20,130)|wp_firearm(130),knows_archer_basic,swadian_face_younger_1, swadian_face_older_2],
  ["briton_marksman","Briton Archer (Saethydd)","Briton Archers (Saethydds)",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_welsh,
   []+common_archer+war_brit_shoes1+briton_tunic2+common_axes3+britons_common_old_helmets+basic_knives,
   def_attrib2|level(23),wpex(165,100,80,120,20,180)|wp_firearm(180),knows_archer_basic,swadian_face_younger_1, swadian_face_older_2],
  ["briton_horseman","Briton Horseman (Marchoc)","Briton Horsemen (Marcach)",tf_mounted|tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_culture_welsh,
   []+long_warspears+common_pony+common_horse+war_brit_shoes2+briton_tunic3+briton_shortgambeson+britons_common_helmets+horseman_skirmishes+britons_convexshields+basic_knives,
   def_attrib2|level(26),wpex(230,80,220,50,20,225)|wp_firearm(100),knows_horseman_pictish,swadian_face_younger_1, swadian_face_older_2], #VC-3534

  ["briton_standard_bearer","Standard Bearer (Gwas Ys Tafell)","Standard Bearers (Gwas Ys Tafell)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_culture_welsh,
  []+britonnoble_mail+elite_brit_boots+britons_elite_helmets+standard_normal+standard_dragon+common_trophy,
   def_attrib2|level(26),wpex(220,180,240,50,20,190)|wp_firearm(190),knows_warrior_normal,swadian_face_younger_1, swadian_face_older_2],
  ["briton_priest","Briton Priest","Briton Priests",tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_culture_welsh,
   []+basic_weapons2+basic_throwing+monk_tunic+basic_knives3,
   def_attrib|level(12),wpex(100,100,70,20,20,120)|wp_firearm(120),knows_cleric,sac_face_younger_1, sac_face_older_2],

#################SAXONS
  ["saxon_slave","Saxon Peasant (Gebur)","Peasants (Geburas)",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_saxon,
   []+slings_common+basic_weapons+basic_seax+saxon_tunic+common_shoes,
   def_attrib|level(12),wpex(110,70,100,50,20,110)|wp_firearm(90),knows_common,vaegir_face_younger_1, vaegir_face_older_2],
  ["saxon_bowman","Saxon Bowman (Scytta)","Saxon Bowmen (Scyttena)",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_saxon,
   []+common_archer+common_shoes+saxon_tunic+basic_seax2,
   def_attrib|level(18),wpex(125,70,80,85,20,110)|wp_firearm(90),knows_archer_basic,vaegir_face_younger_1, vaegir_face_older_2],
  ["saxon_level0_landed","Saxon Freeholder (Kotsetla)","Saxon Freeholders (Kotsetlas)",tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_culture_saxon,
   []+light_spears+common_shoes2+saxon_tunic2+saxons_shields+javelin_only+saxons_common_old_helmets+common_phrygian2+basic_seax,
   def_attrib|level(18),wpex(145,100,135,50,30,125)|wp_firearm(100),knows_warrior_basic,vaegir_face_younger_1, vaegir_face_older_2],
  ["saxon_level1_landed","Saxon Spearman (Cniht)","Saxon Spearmen (Cnihtes)",tf_guarantee_polearm|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_saxon,
   []+war_spears+common_shoes3+saxon_tunic2+saxon_lightarmor+saxons_common_helmets+javelin_only+saxons_shields+decorated_phrygian+basic_seax2,
   def_attrib2|level(23),wpex(175,130,200,50,30,155)|wp_firearm(120),knows_warrior_basic2,vaegir_face_younger_1, vaegir_face_older_2],
  ["saxon_level2_landed","Saxon Warrior (Cempa)","Saxon Warriors (Cempan)",tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_armor,0,0,fac_culture_saxon,
   []+long_warspears+war_brit_shoes1+saxon_shortgambeson+saxon_shortgambeson2+saxons_common_helmets2+javelin_only+saxons_tabshields+basic_seax3,
   def_attrib2|level(27),wpex(215,150,245,50,30,185)|wp_firearm(130),knows_warrior_normal,vaegir_face_younger_1, vaegir_face_older_2],
  ["saxon_level3_landed","Saxon Noble (Thegn)","Saxon Nobles (Thegns)",tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_culture_saxon,
   []+heavy_spears+common_gloves+elite_shoes+saxonnoble_mail+saxons_elite_helmets+basic_longseax2+common_sword2+javelin_only+saxons_tabshields+basic_seax,
   def_attrib3|level(31),wpex(380,200,370,50,30,275)|wp_firearm(150),knows_warrior_elite,vaegir_face_younger_1, vaegir_face_older_2],
  ["saxon_level0_companion","Saxon Companion (Geneat)","Saxon Companions (Geneata)",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_saxon,
   [itm_one_handed_war_axe_a,itm_one_handed_war_axe_b,itm_one_handed_war_axe_c,itm_axe_9,itm_axe_8,itm_longseax1,itm_longseax2,itm_longseax3,itm_longseax4,itm_longseax10]+war_brit_shoes1+saxon_tunic2+saxon_lightarmor+saxons_common_helmets+javelin_normal+saxons_shields+decorated_phrygian+basic_seax,
   def_attrib2|level(23),wpex(185,130,155,50,30,160)|wp_firearm(120),knows_warrior_basic2,vaegir_face_younger_1, vaegir_face_older_2],
  ["saxon_level1_companion","Saxon Veteran (Gesith)","Saxon Veterans (Gesithas)",tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_armor,0,0,fac_culture_saxon,
   []+basic_longseax+javelin_normal+war_brit_shoes2+saxon_shortgambeson+saxon_shortgambeson2+common_axes4+common_sword2+saxons_common_helmets2+saxons_tabshields+basic_seax,
   def_attrib2|level(26),wpex(235,150,200,50,30,180)|wp_firearm(130),knows_warrior_normal,vaegir_face_younger_1, vaegir_face_older_2],
  ["saxon_level2_companion","Saxon Bodyguard (Gedriht)","Saxon Bodyguards (Gedrihtes)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_culture_saxon,
   []+basic_longseax2+common_gloves+elite_brit_boots+saxonlong_mail+saxons_elite_helmets+noble_saxonvik_sword+javelin_normal+saxons_tabshields,
   def_attrib3|level(29),wpex(310,210,270,50,30,260)|wp_firearm(170),knows_warrior_veteran,vaegir_face_younger_1, vaegir_face_older_2],
  ["saxon_horseman","Saxon Horseman (Ridda)","Saxon Horsemen (Riddan)",tf_mounted|tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_culture_saxon,
   []+heavy_spears+common_pony+war_brit_shoes1+saxon_tunic2+saxon_shortgambeson+saxons_elite_old_helmets+javelin_skirmishes+saxons_shields+basic_longseax,
   def_attrib2|level(26),wpex(230,150,215,50,30,200)|wp_firearm(130),knows_warrior_normal,vaegir_face_younger_1, vaegir_face_older_2],
  ["saxon_standard_bearer","Standard Bearer (Tacnberend)","Standard Bearers (Tacnberends)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_culture_saxon,
  []+saxonnoble_mail+elite_brit_boots+saxons_elite_helmets+standard_normal+standard_dragon+common_trophy,
   def_attrib2|level(26),wpex(220,195,225,50,30,170)|wp_firearm(150),knows_warrior_normal,vaegir_face_younger_1, vaegir_face_older_2],
  ["saxon_priest","Saxon Priest","Saxon Priests",tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_culture_saxon,
    []+basic_throwing+monk_tunic+basic_knives2,
   def_attrib|level(12),wpex(105,100,70,20,20,120)|wp_firearm(110),knows_cleric,sac_face_younger_1, sac_face_older_2],
   
############### ALBA
  ["scotch_peasant","Pictish Peasant (Bachlach)","Peasants (Bachlach)",tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_culture_scotch,
   []+slings_common+basic_throwing+basic_weapons2+pictish_tunic+pictish_shoes+basic_knives,
   def_attrib|level(12),wpex(100,70,70,20,40,105)|wp_firearm(105),knows_common,khergit_face_younger_1, khergit_face_older_2],
#skirmishers
  ["scotch_bowman","Pictish Skirmisher (Fuidir)","Skirmishers (Fuidirs)",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_scotch,
   []+javelin_skirmishes+slings_elite+gael_axes+pictish_shoes+pictish_tunic2+basic_knives2,
   def_attrib|level(18),wpex(135,70,80,20,40,145)|wp_firearm(120),knows_archer_basic,khergit_face_younger_1, khergit_face_older_2],
  ["scotch_level0_skirmisher","Pictish Veteran Skirmisher (Saigteoir)","Veteran Skirmishers (Saigteoir)",tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_culture_scotch, #fuidir were half-free Irish peasants
   []+pictish_crossbow+javelin_skirmishes+pictish_shoes+pictish_lightarmor+pictish_tunic2+pictish_axes+basic_knives,
   def_attrib2|level(23),wpex(165,70,80,20,165,185)|wp_firearm(150),knows_archer_basic,khergit_face_younger_3, khergit_face_older_4],
  ["scotch_level1_skirmisher","Pictish Elite Skirmisher (Cruithnen)","Elite Skirmishers (Cruithnen)",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_culture_scotch,
  []+pictish_crossbow+pictish_shoes+pictish_painted+short_gael_sword+pictish_axes+pictish_common_helmets+pictish_hshields+basic_knives2,
   def_attrib2|level(26),wpex(200,80,90,30,200,205)|wp_firearm(185),knows_archer_pictish,khergit_face_younger_3, khergit_face_older_4],
  ["scotch_horseman","Pictish Horseman (Marcach)","Light Horsemen (Marcach)",tf_mounted|tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_culture_scotch,
   []+wild_pony+long_warspears+pictish_shoes+pictish_tunic2+pictish_lightarmor+pictish_painted+horseman_skirmishes+pictish_common_helmets+pictish_hshields+basic_knives3,
   def_attrib2|level(26),wpex(205,70,140,20,40,215)|wp_firearm(120),knows_horseman_pictish,khergit_face_younger_1, khergit_face_older_2],
#spearmen
  ["scotch_level0_landed","Pictish Landowner (Bothach)","Pictish Landowners (Bothach)",tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_culture_scotch,
   []+long_lightspears+pictish_shoes+pictish_hoodnaked+pictish_hoodtunic+pictish_squareshields+javelin_skirmishes+basic_knives2,
   def_attrib|level(18),wpex(135,70,130,20,40,130)|wp_firearm(120),knows_warrior_basic,khergit_face_younger_1, khergit_face_older_2],
  ["scotch_level1_landed","Pictish Spearman (Octhigern)","Pictish Spearmen (Octhigern)",tf_guarantee_polearm|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_scotch,
   []+long_warspears+pictish_shoes+pictish_hoodtunic+pictish_lightarmor+javelin_skirmishes+pictish_squareshields+basic_knives2,
   def_attrib2|level(23),wpex(175,70,190,20,40,175)|wp_firearm(130),knows_warrior_basic2,khergit_face_younger_1, khergit_face_older_2],
  ["scotch_level2_landed","Pictish Warrior (Gaithlennach)","Pictish Warriors (Gaithlennach)",tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_armor,0,0,fac_culture_scotch,
   []+long_warspears+elite_pict_foot+pictish_shortgambeson2+pictish_common_helmets+javelin_skirmishes+britons_tabconvexshields+basic_knives,
   def_attrib2|level(26),wpex(215,70,230,20,40,185)|wp_firearm(150),knows_warrior_normal,khergit_face_younger_1, khergit_face_older_2],
#swordmen
  ["scotch_level0_companion","Pictish Axeman (Crechaire)","Pictish Axesmen (Crechaire)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_culture_scotch,
   []+pictish_axes+pictish_shoes+pictish_shortgambeson+pictish_common_helmets+javelin_skirmishes+pictish_hshields+basic_knives2,
   def_attrib2|level(23),wpex(235,70,180,20,40,195)|wp_firearm(150),knows_warrior_normal,khergit_face_younger_1, khergit_face_older_2],
  ["scotch_level1_companion","Pictish Veteran (Arsaid)","Pictish Veterans (Arsaid)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_culture_scotch,
   []+common_gael_sword+pictish_axes+pictish_shoes+pictishlong_mail+pictish_common_helmets+javelin_skirmishes+pictish_hshields+basic_knives,
   def_attrib3|level(27),wpex(295,230,230,20,40,265)|wp_firearm(160),knows_warrior_veteran,khergit_face_younger_1, khergit_face_older_2],
  ["scotch_level2_companion","Pictish Champion (Gaiscedach)","Pictish Champions (Gaisgidh)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_culture_scotch,
   []+noble_gael_sword+common_gloves+elite_pict_foot+pictishlong_mail+pictish_common_helmets+javelin_skirmishes+britons_tabconvexshields+basic_knives2,
   def_attrib3|level(31),wpex(365,320,330,20,40,295)|wp_firearm(190),knows_warrior_elite,khergit_face_younger_1, khergit_face_older_2],
#horseman elite
  ["scotch_knight","Pictish Noble (Toisech)","Pictish Nobles (Toisechs)",tf_mounted|tf_guarantee_polearm|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_horse,0,0,fac_culture_scotch,
   []+long_heavyspears+common_horse+elite_pict_foot+pictishlong_mail+pictishnoble_mail+pictish_elite_helmets+pictish_noble_helmets+horseman_skirmishes+britons_tabconvexshields+common_gael_sword,
   def_attrib3|level(29),wpex(310,70,280,20,40,270)|wp_firearm(150),knows_warrior_veteran,khergit_face_younger_1, khergit_face_older_2],

  ["scotch_standard_bearer","Standard Bearer (Samhladh)","Standard Bearer (Samhladh)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_culture_scotch,
 []+pictishlong_mail+pictishnoble_mail+pictish_shoes+pictish_elite_helmets+pictish_noble_helmets+standard_normal+common_trophy,
   def_attrib2|level(26),wpex(225,240,210,20,40,195)|wp_firearm(150),knows_warrior_normal,khergit_face_younger_1, khergit_face_older_2],
  ["scotch_musician","Pictish Hornman","Pictish Hornmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_scotch,  #TODO check if MP restricts this
 []+common_axes+pictish_painted+pictish_shoes+javelin_skirmishes+common_horn+basic_knives2,
   def_attrib|level(18),wpex(140,70,50,20,40,125)|wp_firearm(110),knows_warrior_basic,khergit_face_younger_1, khergit_face_older_2],
  ["scotch_priest","Priest","Priests",tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_culture_scotch,
  []+basic_throwing+monk_tunic+basic_knives,
   def_attrib|level(12),wpex(105,50,50,20,40,105)|wp_firearm(100),knows_cleric,sac_face_younger_1, sac_face_older_2],

################ANGLES (Saxons, but slightly wealthier but less experienced)
  ["angle_slave","Angle Peasant (Gebur)","Peasants (Geburas)",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_angle,
   []+slings_common+basic_weapons2+basic_seax2+angles_basic_tunic+common_shoes2,
   def_attrib|level(12),wpex(105,70,100,50,20,105)|wp_firearm(95),knows_common,vaegir_face_younger_1, vaegir_face_older_2],
  ["angle_bowman","Angle Bowman (Scytta)","Angle Bowmen (Scyttena)",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_angle,
   []+common_archer+common_shoes3+angles_basic_tunic+basic_seax,
   def_attrib|level(18),wpex(120,70,80,85,20,105)|wp_firearm(95),knows_archer_basic,vaegir_face_younger_1, vaegir_face_older_2],
  ["angle_level0_landed","Angle Freeholder (Kotsetla)","Angle Freeholders (Kotsetlas)",tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_culture_angle,
   []+light_spears+common_shoes3+angles_richtunic+angles_shields+javelin_only+saxons_common_old_helmets2+common_phrygian2+basic_seax2,
   def_attrib|level(18),wpex(140,100,140,50,30,120)|wp_firearm(105),knows_warrior_basic,vaegir_face_younger_1, vaegir_face_older_2],
  ["angle_level1_landed","Angle Spearman (Cniht)","Spearmen (Cnihtes)",tf_guarantee_polearm|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_angle,
   []+war_spears+war_brit_shoes1+angles_richtunic+angles_lightarmor+saxons_common_helmets+javelin_only+angles_shields+decorated_phrygian+basic_seax3,
   def_attrib2|level(23),wpex(170,130,205,50,30,150)|wp_firearm(125),knows_warrior_basic2,vaegir_face_younger_1, vaegir_face_older_2],
  ["angle_level2_landed","Angle Warrior (Cempa)","Angle Warriors (Cempan)",tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_armor,0,0,fac_culture_angle,
   []+long_warspears+war_brit_shoes2+angle_shortgambeson+angle_gambeson+saxons_common_helmets2+javelin_only+saxons_tabshields+basic_seax2,
   def_attrib2|level(26),wpex(210,150,250,50,30,180)|wp_firearm(135),knows_warrior_normal,vaegir_face_younger_1, vaegir_face_older_2],
  ["angle_level3_landed","Angle Noble (Thegn)","Angle Nobles (Thegns)",tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_culture_angle,
   []+basic_longseax+common_gloves+elite_shoes+anglenoble_mail+saxons_elite_helmets+common_sword+heavy_spears+javelin_only+saxons_tabshields+basic_seax,
   def_attrib3|level(29),wpex(320,200,340,50,30,270)|wp_firearm(155),knows_warrior_veteran,vaegir_face_younger_1, vaegir_face_older_2],
  ["angle_level0_companion","Angle Companion (Geneat)","Angle Companions (Geneata)",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_angle,
   [itm_longseax9,itm_longseax8,itm_longseax7,itm_longseax6,itm_one_handed_war_axe_d,itm_axe_7,itm_axe_6,itm_one_handed_war_axe_c,itm_hand_axe]+war_brit_shoes1+angles_richtunic+angles_lightarmor+saxons_common_helmets+javelin_normal+angles_shields+decorated_phrygian+basic_seax2,
   def_attrib2|level(23),wpex(190,130,150,50,30,155)|wp_firearm(120),knows_warrior_basic2,vaegir_face_younger_1, vaegir_face_older_2],
  ["angle_level1_companion","Angle Veteran (Gesith)","Angle Veterans(Gesithas)",tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_armor,0,0,fac_culture_angle,
  []+basic_longseax2+javelin_normal+war_brit_shoes2+angle_gambeson+angle_shortgambeson+common_axes3+common_sword2+saxons_common_helmets2+saxons_tabshields+basic_seax,
   def_attrib2|level(27),wpex(235,150,205,50,30,170)|wp_firearm(130),knows_warrior_normal,vaegir_face_younger_1, vaegir_face_older_2],
  ["angle_level2_companion","Angle Bodyguard (Gedriht)","Angle Bodyguards (Gedrihtes)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_culture_angle,
   []+common_sword+common_gloves+elite_brit_boots+anglelong_mail+saxons_elite_helmets+basic_longseax+javelin_normal+saxons_tabshields,
   def_attrib3|level(31),wpex(355,210,320,50,30,280)|wp_firearm(170),knows_warrior_elite,vaegir_face_younger_1, vaegir_face_older_2],
 ["angle_horseman","Angle Horseman (Ridda)","Angle Horsemen (Riddan)",tf_mounted|tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_culture_angle,
   []+heavy_spears+common_pony+war_brit_shoes2+angles_richtunic+angle_shortgambeson+saxons_elite_old_helmets+javelin_skirmishes+saxons_shields+basic_longseax2,
   def_attrib2|level(26),wpex(220,150,235,50,30,215)|wp_firearm(130),knows_warrior_normal,vaegir_face_younger_1, vaegir_face_older_2],
  ["angle_standard_bearer","Standard Bearer (Tacnberend)","Standard Bearers (Tacnberends)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_culture_angle,
 []+anglenoble_mail+elite_brit_boots+saxons_elite_helmets+standard_normal+common_trophy,
   def_attrib2|level(26),wpex(220,195,225,50,30,170)|wp_firearm(130),knows_warrior_normal,vaegir_face_younger_1, vaegir_face_older_2],
  ["angle_priest","Angle Priest","Angle Priests",tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_culture_angle,
   []+basic_throwing+monk_tunic+basic_knives3,
   def_attrib|level(12),wpex(100,100,70,20,20,115)|wp_firearm(105),knows_cleric,sac_face_younger_1, sac_face_older_2],

##########IRELAND
# http://www.danann.org/library/law/breh3.html
  ["irish_slave","Irish Serf (Senchleithe)","Irish Serfs (Senchleithe)",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_irish,
   []+slings_common+basic_throwing+basic_weapons2+basic_knives2+irish_capatrousers+irish_hood+irish_shoes,
   def_attrib|level(12),wpex(100,70,100,20,20,115)|wp_firearm(100),knows_common,rhodok_face_younger_1, rhodok_face_older_2],
#skirmishes
  ["irish_bowman","Irish Skirmisher (Fer Midboth)","Irish Skirmishes (Fer Midboth)",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_irish,
   []+javelin_skirmishes+slings_common+gael_axes+irish_shoes+irish_tunic+irish_hood+basic_knives,
   def_attrib|level(18),wpex(140,70,70,30,30,155)|wp_firearm(130),knows_archer_basic,rhodok_face_younger_1, rhodok_face_older_2],
  ["irish_level0_skirmisher","Irish Veteran Skirmisher (Ceithernach)","Irish Veteran Skirmishers (Ceithern)",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_irish,
   []+irish_skirmishes+slings_elite+irish_shoes2+irish_tunic+irish_lightarmor+gael_axes,
   def_attrib2|level(23),wpex(165,100,110,50,30,190)|wp_firearm(190),knows_archer_basic,rhodok_face_younger_1, rhodok_face_older_2],
  ["irish_level1_skirmisher","Irish Elite Skirmisher (Fianaige)","Irish Elite Skirmishers (Fian)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,0,0,fac_culture_irish, #?? Fianna were the king's family/companions, or roving bands of landless nobles, perhaps Fiagania are meant # http://forums.taleworlds.com/index.php?topic=78607.0
   [itm_irish_short_sword1,itm_irish_short_sword2,itm_irish_short_sword3,itm_irish_short_sword1,itm_irish_short_sword2,itm_irish_short_sword3]+irish_skirmishes+elite_gael_foot+irish_tunic2+irish_shortgambeson2+pictish_common_helmets+irish_smallroundshields+basic_knives,
   def_attrib2|level(26),wpex(205,130,160,70,30,220)|wp_firearm(220),knows_archer_pictish,rhodok_face_younger_1, rhodok_face_older_2],
  ["irish_horseman","Irish Horseman (Marcach)","Irish Horsemen (Marcach)",tf_mounted|tf_guarantee_polearm|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_culture_irish,
   []+long_warspears+common_pony+irish_shoes2+irish_tunic2+irish_shortgambeson+horseman_skirmishes+pictish_common_helmets+irish_smallroundshields+gael_axes,
   def_attrib2|level(26),wpex(210,130,205,70,30,220)|wp_firearm(170),knows_horseman_pictish,rhodok_face_younger_1, rhodok_face_older_2],
#spearmen
  ["irish_level0_landed","Irish Laborer (Bothach)","Irish Militia (Bothach)",tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_culture_irish,  #
   []+long_lightspears+irish_shoes+irish_hoodtunic+irish_tunic3+irish_bigshields+javelin_skirmishes+basic_knives,
   def_attrib|level(18),wpex(130,100,145,30,30,135)|wp_firearm(120),knows_warrior_basic,rhodok_face_younger_1, rhodok_face_older_2],
  ["irish_level1_landed","Irish Freeholder (Ocaire)","Irish Freeholders (Ocaires)",tf_guarantee_polearm|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_irish,
   [itm_long_war_spear1,itm_long_war_spear2]+irish_shoes2+irish_hoodtunic+irish_brattunic+irish_lightarmor+javelin_skirmishes+irish_bigshields+basic_knives2,
   def_attrib2|level(23),wpex(170,120,190,50,30,170)|wp_firearm(135),knows_warrior_basic2,rhodok_face_younger_1, rhodok_face_older_2],
  ["irish_level2_landed","Irish Veteran (Boaire)","Irish Veterans (Boaires)",tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_armor,0,0,fac_culture_irish,  #young freeman http://en.wikipedia.org/wiki/Early_Irish_law
   [itm_long_war_spear1,itm_long_war_spear2]+irish_shoes2+irish_brattunic+irish_lightarmor+irish_shortgambeson+pictish_common_helmets+javelin_skirmishes+britons_tabconvexshields+basic_knives3,
   def_attrib2|level(26),wpex(210,130,230,70,30,175)|wp_firearm(180),knows_warrior_normal,rhodok_face_younger_1, rhodok_face_older_2],
  ["irish_level3_landed","Irish Noble (Aire)","Irish Nobles (Airig)",tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_culture_irish,
   [itm_long_war_spear1,itm_long_war_spear2]+common_gloves+elite_gael_foot+irishlong_mail+irishnoble_mail+pictish_elite_helmets+pictish_noble_helmets+common_gael_sword+javelin_skirmishes+britons_tabconvexshields+basic_knives2,
   def_attrib3|level(29),wpex(295,190,300,70,30,260)|wp_firearm(220),knows_warrior_veteran,rhodok_face_younger_1, rhodok_face_older_2],
#swords
  ["irish_level0_companion","Irish Warrior (Cliarnach)","Irish Warriors (Cliathaire)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_culture_irish,
   [itm_pictish_hatchet13,itm_pictish_hatchet14,itm_pictish_hatchet15,itm_pictish_hatchet16,itm_pictish_hatchet6,itm_pictish_hatchet3]+irish_shoes2+irish_tunic3+irish_shortgambeson2+pictish_common_helmets+javelin_skirmishes+irish_bigshields+basic_knives,
   def_attrib2|level(23),wpex(230,130,200,70,30,215)|wp_firearm(170),knows_warrior_normal,rhodok_face_younger_1, rhodok_face_older_2],
  ["irish_level1_companion","Irish Champion (Caur)","Irish Champions (Curadmir)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_culture_irish, #no shield
   []+common_gloves+elite_gael_foot+irishlong_mail+pictish_elite_helmets+pictish_common_helmets+javelin_skirmishes+champion_gael_sword+britons_tabconvexshields+twohanded_irishaxes,
   def_attrib3|level(26),wpex(290,200,285,70,30,255)|wp_firearm(200),knows_warrior_veteran,rhodok_face_younger_1, rhodok_face_older_2],
#cavalry with long spear
  ["irish_knight","Irish Bodyguard (Riglach)","Irish Bodyguards (Riglach)",tf_mounted|tf_guarantee_polearm|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_horse,0,0,fac_culture_irish, #An Curraidh "Knights of the Red Bough" was but one order http://home.earthlink.net/~rggsibiba/html/galloglas/gallohist.html
   []+common_horse+elite_gael_foot+irishlong_mail+irish_shortgambeson+pictish_elite_helmets+pictish_common_helmets+horseman_skirmishes+long_heavyspears+britons_tabconvexshields+common_gael_sword,
   def_attrib3|level(29),wpex(295,190,305,70,30,265)|wp_firearm(220),knows_warrior_veteran,rhodok_face_younger_1, rhodok_face_older_2],
  ["irish_standard_bearer","Standard Bearer (Meirgeach)","Standard Bearers (Meirgeach)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_culture_irish,
 []+irishnoble_mail+irishlong_mail+elite_gael_foot+pictish_elite_helmets+pictish_noble_helmets+standard_normal+common_trophy,
   def_attrib2|level(26),wpex(210,195,205,50,30,210)|wp_firearm(130),knows_warrior_normal,rhodok_face_younger_1, rhodok_face_older_2],
  ["irish_priest","Godelic Priest","Godelic Priests",tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_culture_irish,
   []+basic_throwing+monk_tunic+basic_knives2,
   def_attrib|level(12),wpex(100,90,70,20,20,115)|wp_firearm(115),knows_cleric,sac_face_younger_1, sac_face_older_2],

#Everybody
  ["todos_cuerno","Hornman","Hornmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_neutral,
  []+common_hoodtunic+common_hoodtunic2+common_shoes2+basic_knives+common_axes+javelin_skirmishes+common_horn,
   def_attrib|level(18),wpex(140,70,120,30,30,145)|wp_firearm(120),knows_warrior_basic,man_face_younger_1, man_face_older_2],


## FACTION TROOPS for single player only
########################VIKINGS SP only
  ["norse_messenger","Messenger (Bodi)","Messengers (Bodar)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_culture_norse,
   []+common_horse+javelin_normal+war_norse_shoes2+viking_gambeson+basic_longseaxnorse+common_axes4+viking_complete_helmets_old,
   def_attrib2|level(26),wp(220),knows_warrior_normal,nord_face_younger_1, nord_face_older_2],
  ["norse_deserter","Norse Deserter","Norse Deserters",tf_guarantee_polearm|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   []+war_norse_shoes1+common_tunic2+viking_gambeson+viking_complete_helmets_old+basic_longseaxnorse2+light_spears+javelin_only+mercenaries_roundshields,
   def_attrib2|level(23),wp(180),knows_warrior_basic2,nord_face_younger_1, nord_face_older_2],
  ["norse_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_norse,
   []+war_norse_shoes2+viking_gambeson+viking_complete_helmets2+basic_longseaxnorse2+javelin_normal+viking_shields+war_spears,
   def_attrib3|level(29),wp(300),knows_warrior_veteran,nord_face_younger_1, nord_face_older_2],
  ["norse_castle_guard","Fort Guard","Fort Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_norse,
   []+javelin_normal+war_norse_shoes1+viking_gambeson+viking_gambeson+basic_longseaxnorse+common_axes4+viking_complete_helmets+viking_complete_helmets_old+javelin_normal+viking_shields,
   def_attrib3|level(29),wp(300),knows_warrior_veteran,nord_face_younger_1, nord_face_older_2],

#######FRISIANS SP only
  ["frisian_basic","Frisian (Husmo)","Frisians (Fresen)",tf_guarantee_polearm|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_culture_norse,
   []+slings_common+basic_weapons+basic_seax2+frisian_tunics+common_shoes+light_spears,
   def_attrib|level(15),wp(140),knows_common,vaegir_face_younger_1, vaegir_face_older_2],
  ["frisian_mid","Frisian Warrior (Wigand)","Frisian Warriors (Wiganda)",tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,0,fac_culture_norse,
   []+common_shoes4+frisian_tunics2+frisian_lightarmor+saxons_common_helmets+basic_seax+war_spears+javelin_only+angles_shields+decorated_phrygian,
   def_attrib2|level(21),wp(170),knows_warrior_basic2,vaegir_face_younger_1, vaegir_face_older_2],
    ["frisian_heavy","Frisian Veteran (Werand)","Frisian Veterans (Weranda)",tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_culture_norse,
   []+war_brit_shoes1+frisianshort_mail+frisian_gambeson+saxons_common_helmets2+basic_seax2+long_warspears+javelin_only+saxons_tabshields,
   def_attrib2|level(25),wp(210),knows_warrior_normal,vaegir_face_younger_1, vaegir_face_older_2],
     ["frisian_cav","Frisian Horseman (Riddere)","Frisian Horsemen (Riddere)",tf_mounted|tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_shield,no_scene,reserved,fac_culture_norse,
   []+common_pony+war_brit_shoes2+frisian_lightarmor+frisian_shortgambeson+saxons_common_helmets2+basic_seax3+long_warspears+javelin_only+saxons_shields,
   def_attrib2|level(25),wp(210),knows_warrior_normal,vaegir_face_younger_1, vaegir_face_older_2],
 

#########BRITONS SP only
  ["briton_messenger","Messenger","Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_culture_welsh,
    []+common_pony+common_horse+elite_shoes+briton_tunic2+briton_shortgambeson+britons_common_old_helmets2+horseman_skirmishes+basic_knives2+light_spears+britons_convexshields,
   def_attrib2|level(26),wp(220),knows_warrior_normal,swadian_face_younger_1, swadian_face_older_2],
  ["briton_deserter","Briton Deserter","Briton Deserters",tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor,0,0,fac_deserters,
   []+common_shoes3+briton_tunic+briton_gambeson+britons_elite_old_helmets+common_axes3+javelin_normal+mercenaries_roundshields,
   def_attrib2|level(23),wp(180),knows_warrior_basic2,swadian_face_younger_1, swadian_face_older_2],
  ["briton_prison_guard","Prison Guard","Prison Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_culture_welsh,
   []+javelin_normal+war_brit_shoes2+briton_tunic2+briton_gambeson+basic_knives3+common_axes2+common_sword5+britons_common_helmets2+britons_convexshields,
   def_attrib3|level(29),wp(300),knows_warrior_veteran,swadian_face_younger_1, swadian_face_older_2],
  ["briton_castle_guard","Fort Guard","Fort Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_welsh,
   []+war_brit_shoes1+briton_tunic+britons_common_helmets+basic_knives+long_warspears+javelin_normal+britons_convexshields,
   def_attrib3|level(29),wp(300),knows_warrior_veteran,swadian_face_younger_1, swadian_face_older_2],

#################SAXONS SP only
  ["saxon_messenger","Messenger (Horsweala)","Messengers (Horswealas)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_culture_saxon,
   []+common_pony+elite_shoes+saxon_tunic2+saxon_shortgambeson+saxons_elite_old_helmets+javelin_skirmishes+war_spears+saxons_shields,
   def_attrib2|level(26),wp(220),knows_warrior_normal,vaegir_face_younger_1, vaegir_face_older_2],
  ["saxon_deserter","Saxon Deserter","Saxon Deserters",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   []+common_shoes3+saxon_tunic+saxon_shortgambeson+saxons_common_helmets+basic_longseax+common_axes2+javelin_normal+mercenaries_roundshields+decorated_phrygian,
   def_attrib2|level(23),wp(180),knows_warrior_basic2,vaegir_face_younger_1, vaegir_face_older_2],
  ["saxon_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_culture_saxon,
   []+javelin_normal+war_brit_shoes2+saxon_tunic2+saxon_shortgambeson2+basic_longseax+common_axes4+common_sword2+saxons_common_helmets2+saxons_shields,
   def_attrib3|level(29),wp(300),knows_warrior_veteran,vaegir_face_younger_1, vaegir_face_older_2],
  ["saxon_castle_guard","Fort Guard","Fort Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_saxon,
   []+war_brit_shoes1+saxon_tunic2+saxon_shortgambeson+saxons_common_helmets2+basic_seax2+long_warspears+javelin_only+saxons_shields,
   def_attrib3|level(29),wp(300),knows_warrior_veteran,vaegir_face_younger_1, vaegir_face_older_2],


############### ALBA SP only
  ["scotch_messenger","Messenger","Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_culture_scotch,
   []+wild_pony+pictish_shoes+pictish_tunic2+horseman_skirmishes+long_lightspears+basic_knives2+pictish_common_helmets,
   def_attrib2|level(26),wp(220),knows_warrior_normal,khergit_face_younger_1, khergit_face_older_2],
  ["scotch_deserter","Picti Deserter","Picti Deserters",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_deserters,
   []+irish_skirmishes+pictish_shoes+pictish_shortgambeson+pictish_hoodnaked+common_gael_sword+pictish_axes+pictish_hshields+pictish_common_helmets,
   def_attrib2|level(23),wp(180),knows_warrior_basic2,khergit_face_younger_1, khergit_face_older_4],
  ["scotch_prison_guard","Prison Guard","Prison Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_culture_scotch,
   []+pictish_shoes+pictish_shortgambeson+pictish_common_helmets+common_gael_sword+long_warspears+javelin_skirmishes+pictish_squareshields,
   def_attrib3|level(29),wp(300),knows_warrior_veteran,khergit_face_younger_1, khergit_face_older_2],
  ["scotch_castle_guard","Fort Guard","Fort Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_scotch,
   []+pictish_shoes+pictish_shortgambeson+pictish_common_helmets+common_gael_sword+pictish_axes+javelin_skirmishes+pictish_hshields,
   def_attrib3|level(29),wp(300),knows_warrior_veteran,khergit_face_younger_1, khergit_face_older_2],

################ANGLES SP only
  ["angle_messenger","Messenger (Horsweala)","Messengers (Horswealas)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_culture_angle,
   []+common_pony+elite_shoes+angle_shortgambeson+saxons_elite_old_helmets+javelin_skirmishes+war_spears+saxons_shields,
   def_attrib2|level(26),wp(220),knows_warrior_normal,vaegir_face_younger_1, vaegir_face_older_2],
  ["angle_deserter","Angle Deserter","Angle Deserters",tf_guarantee_polearm|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   []+common_shoes3+angles_basic_tunic+angle_shortgambeson+saxons_common_helmets+common_axes3+common_sword2+javelin_normal+mercenaries_roundshields+decorated_phrygian,
   def_attrib2|level(23),wp(180),knows_warrior_basic2,vaegir_face_younger_1, vaegir_face_older_2],
  ["angle_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_culture_angle,
   []+war_brit_shoes2+angles_richtunic+angle_shortgambeson+saxons_common_helmets2+common_axes3+javelin_normal+angles_shields,
   def_attrib3|level(29),wp(300),knows_warrior_veteran,vaegir_face_younger_1, vaegir_face_older_2],
  ["angle_castle_guard","Fort Guard","Fort Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_angle,
  []+javelin_normal+war_brit_shoes1+angles_richtunic+angle_gambeson+basic_longseax2+common_axes3+common_sword2+saxons_common_helmets2+angles_shields,
   def_attrib3|level(29),wp(300),knows_warrior_veteran,vaegir_face_younger_1, vaegir_face_older_2],

##########IRELAND SP only
  ["irish_messenger","Messenger","Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_culture_irish,
   []+common_pony+irish_shoes2+irish_tunic2+irish_shortgambeson+horseman_skirmishes+long_lightspears+basic_knives2+pictish_common_helmets+irish_smallroundshields,
   def_attrib2|level(26),wp(220),knows_warrior_normal,rhodok_face_younger_1, rhodok_face_older_2],
  ["irish_deserter","Goidelic Deserter","Goidelic Deserters",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   []+irish_skirmishes+irish_bigshields+irish_shoes2+irish_tunic2+irish_shortgambeson+gael_axes2+pictish_common_helmets,
   def_attrib2|level(23),wp(180),knows_warrior_basic2,rhodok_face_younger_1, rhodok_face_older_2],
  ["irish_prison_guard","Prison Guard","Prison Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_culture_irish,
   []+irish_shoes2+irish_brattunic+irish_shortgambeson+pictish_common_helmets+basic_knives3+gael_axes2+javelin_skirmishes+irish_bigshields,
   def_attrib3|level(29),wp(300),knows_warrior_veteran,rhodok_face_younger_1, rhodok_face_older_2],
  ["irish_castle_guard","Fort Guard","Fort Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_irish,
   []+irish_shoes2+irish_brattunic+irish_shortgambeson2+pictish_common_helmets+gael_axes2+javelin_skirmishes+irish_bigshields,
   def_attrib3|level(29),wp(300),knows_warrior_veteran,rhodok_face_younger_1, rhodok_face_older_2],

  ###seguir 
# Ryan BEGIN  
  ["looter","Ruffian","Ruffians",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_outlaws,
   [(itm_ptunic_1woman,imod_ragged),(itm_staff,imod_cracked),itm_staff, (itm_quarter_staff,imod_bent),itm_quarter_staff, itm_battle_fork, itm_pitch_fork, (itm_pitch_fork,imod_cracked),(itm_battle_fork, imod_cracked),
(itm_ptunic_2woman,imod_tattered),(itm_ptunic_3woman, imod_ragged),(itm_ptunic_4woman, imod_tattered),(itm_ptunic_5woman, imod_ragged),(itm_ptunic_6woman,imod_tattered),(itm_ptunic_7woman, imod_ragged),(itm_ptunic_1woman, imod_tattered),(itm_ptunic_2woman, imod_ragged),(itm_ptunic_3woman,imod_tattered),(itm_ptunic_4woman, imod_ragged),
(itm_carbatinae_1,imod_ragged),(itm_bare_foot_man,imod_tattered),(itm_carbatinae_4,imod_tattered),(itm_bare_foot_man,imod_ragged),(itm_carbatinae_5s,imod_ragged),(itm_carbatinae_4s,imod_tattered)]+basic_throwing+slings_common+common_phrygian,
   def_attrib|level(12),wpex(105,100,70,20,20,115)|wp_firearm(110),knows_common,man_face_younger_1, man_face_older_2],
# Ryan END
  ["bandit","Footpad","Footpads",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_outlaws,
[(itm_one_handed_war_axe_c,imod_rusty),(itm_axe_8, imod_chipped),itm_axe_2,(itm_axe_2,imod_rusty), (itm_axe_2,imod_chipped),(itm_hand_axe,imod_chipped), 
(itm_hand_axe, imod_rusty), (itm_one_handed_war_axe_c, imod_chipped),(itm_hoodtunic_01,imod_ragged),itm_hoodtunic_02,(itm_hoodtunic_03, imod_ragged),itm_hoodtunic_04,
(itm_hoodtunic_05, imod_ragged),(itm_hoodtunic_06,imod_tattered),(itm_hoodtunic_07, imod_ragged),(itm_btunic_1woman, imod_ragged),(itm_hoodtunic_01, imod_tattered),(itm_hoodtunic_02, imod_ragged),(itm_shield_11,imod_battered),(itm_shield_11,imod_cracked),
(itm_shield_12,imod_battered),(itm_shield_12,imod_cracked),(itm_shield_13,imod_cracked),(itm_shield_14,imod_battered),
(itm_shield_14,imod_cracked),(itm_shield_15,imod_cracked), (itm_shield_15,imod_battered),(itm_shield_16,imod_battered),(itm_shield_16,imod_cracked),(itm_carbatinae_1,imod_ragged),(itm_carbatinae_4,imod_tattered),(itm_bare_foot_man,imod_tattered),
(itm_bare_foot_man,imod_ragged),(itm_carbatinae_5s,imod_ragged),(itm_carbatinae_11q,imod_tattered)]+common_phrygian+basic_seax3,
   def_attrib|level(18),wpex(140,90,70,20,20,110)|wp_firearm(100),knows_warrior_basic,man_face_younger_2, man_face_older_2],
  ["brigand","Brigand","Brigands",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor,0,0,fac_outlaws,
   [(itm_shield_11,imod_cracked),(itm_shield_12,imod_battered),(itm_shield_12,imod_cracked),(itm_shield_13,imod_cracked),(itm_shield_13,imod_cracked),(itm_shield_14,imod_battered),
(itm_shield_14,imod_cracked),(itm_shield_15,imod_cracked), (itm_shield_15,imod_battered),(itm_shield_16,imod_battered),(itm_shield_16,imod_cracked),
    (itm_hoodtunic_01,imod_crude),(itm_hoodtunic_02, imod_tattered),(itm_hoodtunic_03,imod_crude),(itm_hoodtunic_04, imod_ragged),(itm_hoodtunic_05,imod_ragged),(itm_hoodtunic_06, imod_tattered),(itm_hoodtunic_07, imod_poor),(itm_hoodtunic_01, imod_tattered),
    (itm_hand_axe,imod_chipped),(itm_axe_8,imod_rusty),(itm_hand_axe,imod_rusty),
(itm_one_handed_war_axe_d, imod_chipped),(itm_one_handed_war_axe_d,imod_rusty),(itm_one_handed_war_axe_c, imod_chipped),itm_javelin, (itm_javelin, imod_bent),(itm_javelin, imod_cracked),(itm_carbatinae_11q,imod_tattered),(itm_carbatinae_3,imod_tattered),
(itm_carbatinae_1,imod_ragged),(itm_carbatinae_10,imod_tattered),(itm_carbatinae_5s, imod_tattered),(itm_carbatinae_4, imod_ragged),(itm_briton_helm16,imod_cracked), (itm_briton_helm17,imod_crude), (itm_briton_helm18,imod_battered),
(itm_briton_helm38,imod_cracked),(itm_briton_helm39,imod_cracked),(itm_briton_helm40,imod_battered)]+slings_common+basic_knives2,
   def_attrib2|level(23),wpex(165,110,100,20,20,175)|wp_firearm(180),knows_warrior_basic2,swadian_face_younger_1, swadian_face_older_2],
  ["mountain_bandit","Robber","Robbers",tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor,0,0,fac_outlaws,
[(itm_shield_11,imod_cracked),(itm_shield_12,imod_battered),(itm_shield_12,imod_cracked),(itm_shield_13,imod_cracked),(itm_shield_13,imod_crude),(itm_shield_14,imod_battered),
(itm_shield_14,imod_cracked),(itm_shield_15,imod_cracked),(itm_shield_15,imod_battered),(itm_shield_16,imod_battered),(itm_shield_16,imod_cracked),
 (itm_gambeson21,imod_ragged),(itm_gambeson22,imod_tattered),(itm_gambeson23,imod_tattered),(itm_gambeson24,imod_ragged),(itm_gambeson21,imod_tattered),(itm_gambeson22,imod_ragged),(itm_gambeson23, imod_ragged),(itm_gambeson24,imod_crude),(itm_gambeson21,imod_crude),
 (itm_war_spear1,imod_bent),(itm_war_spear1, imod_cracked),
(itm_war_spear2,imod_cracked),(itm_war_spear2,imod_bent),(itm_heavy_spear2, imod_bent),itm_war_spear2,itm_war_spear1,(itm_spangenhelm_3,imod_battered),(itm_spangenhelm_4,imod_cracked),(itm_spangenhelm_7,imod_cracked),
(itm_spangenhelm_8,imod_battered),(itm_spangenhelm_11,imod_battered),(itm_spangenhelm_12,imod_rusty),(itm_spangenhelm_33, imod_rusty),(itm_spangenhelm_34, imod_cracked),
 (itm_hoodtunic_01,imod_crude),(itm_hoodtunic_02,imod_tattered),(itm_hoodtunic_03,imod_crude),(itm_hoodtunic_04,imod_tattered),(itm_hoodtunic_05,imod_tattered),(itm_hoodtunic_06, imod_ragged),
 (itm_carbatinae_4,imod_tattered),(itm_carbatinae_5,imod_crude),(itm_carbatinae_6,imod_tattered),(itm_carbatinae_vc1,imod_ragged),(itm_carbatinae_vc2,imod_tattered),
(itm_carbatinae_vc3, imod_crude)]+common_shoes2+common_hoodtunic2+basic_seax2,
   def_attrib2|level(23),wpex(170,110,190,20,20,155)|wp_firearm(140),knows_warrior_basic2,man_face_younger_1, man_face_older_2],
  ["forest_bandit","Bandit","Bandits",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_outlaws,
    [itm_javelin_skirmishes, (itm_javelin_skirmishes, imod_bent),(itm_carbatinae_1,imod_tattered),(itm_bare_foot_man,imod_ragged),(itm_carbatinae_3,imod_tattered),(itm_carbatinae_vc4,imod_tattered),(itm_carbatinae_vc5,imod_ragged),(itm_carbatinae_vc6, imod_tattered),
(itm_hoodtunic_05,imod_ragged),(itm_hoodtunic_06,imod_tattered),(itm_hoodtunic_07,imod_ragged),(itm_btunic_1woman, imod_ragged),
     itm_wooden_stick,itm_club_hard,(itm_wooden_stick,imod_bent),(itm_club_hard, imod_crude),(itm_club_hard, imod_cracked)]+slings_common+common_shoes2+poor_tunic2+basic_knives2,
   def_attrib|level(18),wpex(120,90,70,20,20,140)|wp_firearm(140),knows_archer_basic,swadian_face_younger_1, swadian_face_older_2],
  ["sea_raider","Reaver","Reavers",tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor,0,0,fac_outlaws,
   [(itm_javelin, imod_bent),(itm_throwing_spears, imod_bent),(itm_throwing_spears2, imod_bent),(itm_carbatinae_4s,imod_tattered),(itm_carbatinae_5s,imod_tattered),(itm_carbatinae_6s,imod_ragged),(itm_carbatinae_vc3s,imod_tattered),(itm_carbatinae_vc4s, imod_tattered),
(itm_hoodtunic_01,imod_ragged),(itm_hoodtunic_02,imod_tattered),(itm_hoodtunic_03,imod_crude),(itm_hoodtunic_04,imod_poor),(itm_hoodtunic_05,imod_ragged),(itm_hoodtunic_06,imod_tattered),
    (itm_gambeson30,imod_tattered),(itm_gambeson30,imod_crude),(itm_gambeson47,imod_ragged),(itm_gambeson48,imod_ragged),(itm_gambeson31, imod_tattered),(itm_gambeson31,imod_crude),
    (itm_shield_12,imod_battered),(itm_shield_12,imod_cracked),(itm_shield_13,imod_cracked),(itm_shield_14,imod_battered),(itm_shield_14,imod_cracked),(itm_shield_15,imod_battered),(itm_shield_16,imod_battered),(itm_shield_16,imod_cracked),(itm_shield_11,imod_cracked),(itm_one_handed_war_axe_d,imod_chipped),(itm_one_handed_war_axe_d,imod_rusty),(itm_one_handed_war_axe_a,imod_rusty),
(itm_one_handed_war_axe_c,imod_rusty),(itm_hand_axe,imod_chipped),(itm_axe_8,imod_chipped),(itm_axe_7,imod_rusty),(itm_axe_7, imod_chipped),(itm_old_swordv2,imod_chipped),(itm_old_swordv3,imod_chipped),(itm_old_swordv4,imod_rusty),(itm_briton_helm19,imod_cracked),
(itm_briton_helm20,imod_cracked),(itm_briton_helm21,imod_battered),(itm_briton_helm25,imod_cracked),(itm_briton_helm27, imod_cracked)]+common_hoodtunic2+basic_knives+britons_common_helmets2,
   def_attrib2|level(26),wpex(205,90,70,20,20,185)|wp_firearm(145),knows_warrior_normal,swadian_face_younger_1, swadian_face_older_2],
   ["desert_bandit","Highwayman","Highwaymen",tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_armor,0,0,fac_outlaws,
[(itm_mail_shirt_1,imod_battered),(itm_mail_shirt_3,imod_battered),(itm_gambeson30, imod_ragged),(itm_gambeson31, imod_ragged),(itm_gambeson47, imod_ragged),(itm_gambeson23, imod_ragged),(itm_gambeson48, imod_ragged),(itm_gambeson22, imod_tattered),]+common_shoes4+javelin_normal+saxons_common_old_helmets+mercenaries_roundshields+war_spears+heavy_spears+basic_seax,
   def_attrib2|level(26),wpex(190,120,220,20,20,150)|wp_firearm(145),knows_warrior_normal,man_face_younger_1, man_face_older_2],
  ["steppe_bandit","Northmathr Vikingr","Northmenn Vikingarnir",tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_outlaws,
   [itm_gambeson25,itm_gambeson27,(itm_gambeson27, imod_tattered),itm_gambeson29,itm_gambeson4,itm_gambeson35,itm_gambeson43,(itm_byrnie16,imod_battered),(itm_byrnie17,imod_battered),(itm_byrnie16,imod_rusty),(itm_byrnie17,imod_rusty)]+common_gloves+war_norse_shoes3+viking_gambeson+viking_elite_helmets2+viking_elite_helmets_old+basic_longseaxnorse+heavy_spears+javelin_normal+norwegian_roundshields,
   def_attrib3|level(29),wpex(295,220,290,50,0,240)|wp_firearm(225),knows_warrior_veteran,nord_face_younger_1, nord_face_older_2],
  ["taiga_bandit","Vikingr","Vikingarnir",tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor,0,0,fac_outlaws,
   [(itm_gambeson5, imod_ragged),(itm_gambeson8, imod_ragged),(itm_gambeson13, imod_ragged),(itm_gambeson14, imod_ragged),
    (itm_carbatinae_1s,imod_tattered),(itm_carbatinae_2s,imod_tattered),(itm_carbatinae_1v,imod_tattered),(itm_carbatinae_2v,imod_tattered),(itm_carbatinae_3v, imod_tattered),]+javelin_normal+common_tunic2+light_spears+basic_seax+basic_longseaxnorse2+common_axes4+viking_common_helmets_old+viking_complete_helmets_old+norwegian_roundshields+danish_roundshields,
   def_attrib2|level(23),wpex(190,110,160,50,0,165)|wp_firearm(155),knows_warrior_basic2,nord_face_younger_1, nord_face_older_2],
  ["elite_viking","Danish Elite Vikingr","Danish Elite Vikingarnir",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_outlaws,
   []+common_gloves+elite_norse_boots+vikingshort_mail+viking_gambeson+viking_gambeson+viking_elite_helmets+viking_elite_helmets_old2+basic_longseaxnorse+javelin_normal+vikinglong_mail+common_sword+danish_roundshields,
   def_attrib3|level(29),wpex(300,220,220,50,0,245)|wp_firearm(170),knows_warrior_veteran|knows_spotting_6,nord_face_younger_1, nord_face_older_2],
  ["elite_viking_2","Svear Elite Vikingr","Sviar Elite Vikingarnir",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged,0,0,fac_outlaws,
   [itm_throwing_spears2, itm_leather_gloves,
itm_carbatinae_11qs,itm_carbatinae_12qs,itm_carbatinae_14qv,#shoes
itm_lamellar_armor2,itm_lamellar_armor,itm_byrnie17,itm_byrnie16,
itm_btunic_11,itm_btunic_12,itm_btunic_13,itm_btunic_15,itm_gambeson35,itm_gambeson43,
itm_viking_helm7,itm_viking_helm4,itm_viking_helm2,itm_viking_helm8,itm_viking_helm9,##yelmos normales y rusty, 
itm_spatha_3,itm_seax_1,itm_axe_7,itm_axe,itm_axe_10,itm_long_light_spear2,
itm_shield_10],
   def_attrib3|level(29),wpex(280,150,280,50,0,245)|wp_firearm(170),knows_warrior_elite|knows_spotting_6,bandit_face1, bandit_face2],

#lideres bandidos chief
    ["sea_raider_leader2","Ship Captain","Captains",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_outlaws,
   []+common_gloves+elite_norse_boots+vikinglong_mail+viking_elite_helmets+viking_elite_helmets_old+basic_longseaxnorse+common_sword+javelin_normal+viking_shields,
   def_attrib3|level(29),wpex(280,140,220,20,0,255)|wp_firearm(170),knows_warrior_veteran|knows_spotting_6,nord_face_younger_1, nord_face_older_2],
  ["looter_leader2","Bandit Leader","Bandit Leaders",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_outlaws,
   []+common_gloves+elite_brit_boots+commonlong_mail+saxons_elite_helmets+basic_longseax+noble_saxonvik_sword+javelin_normal+mercenaries_roundshields,
   def_attrib3|level(29),wpex(275,140,210,20,0,225)|wp_firearm(170),knows_warrior_veteran,vaegir_face_younger_1, vaegir_face_older_2],
#lideres bandidos acaban
  
  ["manhunter","Young Warrior","Young Warriors",tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_manhunters,
   []+common_shoes2+common_hoodtunic+common_hoodtunic2+basic_knives2+common_axes3+javelin_normal+mercenaries_roundshields,
   def_attrib|level(18),wpex(135,90,110,30,0,130)|wp_firearm(100),knows_warrior_basic2,swadian_face_younger_1, swadian_face_older_2],

#fac_slavers
  ["slave_driver","Slave Driver","Slave Drivers",tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_slavers,
   []+light_spears+common_shoes2+poor_tunic+mercenaries_roundshields+basic_knives+javelin_only,
   def_attrib|level(18),wpex(135,90,110,30,0,130)|wp_firearm(100),knows_warrior_basic,swadian_face_younger_1, swadian_face_older_2],
  ["slave_hunter","Slave Hunter","Slave Hunters",tf_guarantee_polearm|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_ranged,0,0,fac_slavers,
   []+common_shoes3+common_hoodtunic+saxons_common_old_helmets+basic_knives3+war_spears+javelin_only+mercenaries_roundshields,
   def_attrib2|level(23),wpex(160,100,170,40,0,165)|wp_firearm(150),knows_warrior_basic2,swadian_face_younger_1, swadian_face_older_2],

  ["slave_crusher","Veteran Slave Hunter","Veteran Slave Hunters",tf_guarantee_polearm|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,0,0,fac_slavers,
   []+war_brit_shoes1+common_gambeson+saxons_common_old_helmets+basic_knives2+long_warspears+javelin_only+mercenaries_roundshields,
   def_attrib2|level(26),wpex(205,100,210,40,0,185)|wp_firearm(150),knows_warrior_normal,swadian_face_younger_1, swadian_face_older_2],
  ["slaver_chief","Slaver Chief","Slaver Chiefs",tf_mounted|tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_horse,0,0,fac_slavers,
   []+common_gloves+elite_brit_boots+commonlong_mail+common_gambeson+saxons_elite_old_helmets+basic_knives+common_axes4+long_heavyspears+javelin_only+mercenaries_roundshields,
   def_attrib3|level(29),wpex(275,120,250,40,0,195)|wp_firearm(160),knows_warrior_veteran,swadian_face_younger_1, swadian_face_older_2],


####others
  ["follower_woman","Camp Woman","Camp Women",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_commoners,
   []+basic_throwing+women_shoes+poor_tunic+common_female_hats+basic_weapons,
   def_attrib|level(12),wpex(105,70,70,40,0,110)|wp_firearm(105),knows_common,woman_face_younger_1, woman_face_older_2],
  ["hunter_woman","Camp Follower","Camp Followers",tf_female|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_commoners,
[]+slings_common+norse_women+gael_women+basic_weapons+commonveil_women,
   def_attrib|level(18),wpex(125,80,90,40,0,130)|wp_firearm(140),knows_warrior_basic,woman_face_younger_1, woman_face_older_2],
  ["fighter_woman","Soldier's Wife","Soldiers' Wives",tf_female|tf_guarantee_polearm|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
[]+saxon_women+saxon_women2+light_spears+basic_seax3+javelin_only+commonveil_women,
   def_attrib2|level(23),wpex(155,95,150,80,0,140)|wp_firearm(130),knows_warrior_basic2,woman_face_younger_1, woman_face_older_2],
  ["sword_sister","Camp Defender","Camp Defenders",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_commoners,
   []+common_archer+women_shoes+basic_weapons+common_hoodtunic+commonveil_women,
   def_attrib|level(26),wpex(170,80,110,125,0,150)|wp_firearm(150),knows_archer_basic,woman_face_younger_1, woman_face_older_2],

  ["refugee","Refugee","Refugees",tf_female|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_commoners,
   []+basic_throwing+saxon_women+norse_women+gael_women+basic_weapons,
   def_attrib|level(12),wpex(95,60,60,40,0,95)|wp_firearm(90),knows_common,woman_face_younger_1, woman_face_older_2],
  ["peasant_woman","Peasant Woman","Peasant Women",tf_female|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_commoners,
   []+basic_throwing+norse_women+gael_women+basic_weapons,
   def_attrib|level(12),wpex(95,60,60,40,0,90)|wp_firearm(90),knows_common,woman_face_younger_1, woman_face_older_2],
#para dungeon chief
  ["refugeeromanruins","Refugee","Refugees",tf_female|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_commoners,
   []+basic_throwing+frisian_tunics+basic_weapons,
   def_attrib|level(12),wp(100),knows_common,woman_face_younger_1, woman_face_older_2],
  ["peasant_womanromanruins","Peasant Woman","Peasant Women",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   []+basic_throwing+frisian_tunics+basic_weapons,
   def_attrib|level(12),wp(100),knows_common,woman_face_younger_1, woman_face_older_2],
 
  ["refugeedruid","Refugee","Refugees",tf_female|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_commoners,
   []+basic_throwing+norse_women+gael_women+saxon_women+basic_weapons,
   def_attrib|level(12),wp(100),knows_common,woman_face_younger_1, woman_face_older_2],
  ["peasant_womandruid","Peasant Woman","Peasant Women",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   []+basic_throwing+norse_women+gael_women+basic_weapons,
   def_attrib|level(12),wp(100),knows_common,woman_face_younger_1, woman_face_older_2],
  ["farmerdruid","Farmer","Farmers",tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   []+basic_throwing+slings_common+common_shoes+common_phrygian+poor_tunic+basic_weapons2,
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],
  ["manhunterdruid","Young Warrior","Young Band",tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor,0,0,fac_manhunters,
[]+common_shoes2+common_hoodtunic+mercenaries_roundshields+light_spears+basic_seax2,
   def_attrib|level(18),wp(140),knows_warrior_basic,man_face_younger_1, man_face_older_2],
  ["prisionerdruid","Prisoner","Prisoners",tf_bajo|tf_guarantee_boots,no_scene,reserved,fac_commoners,
[], def_attrib|level(5),wp(70),knows_common,man_face_middle_1, man_face_old_2],
  ["quarry_trabajador","Worker","Workers",tf_randomize_face|tf_guarantee_armor|tf_guarantee_boots,no_scene,reserved,fac_commoners,
[
itm_just_man_boots_medium,itm_just_man_boots_light,itm_just_man_shoes, #shoes
itm_phrygian1,itm_phrygian17,itm_phrygian16,itm_phrygian15,
itm_ptunic_7,itm_ptunic_8,itm_ptunic_9,itm_ptunic_10,itm_ptunic_11,itm_ptunic_12, #tunics 2
itm_knife,itm_wooden_stick],
   def_attrib|level(5),wp(70),knows_common,man_face_middle_1, man_face_old_2],
  ["quarry_capataz","Foreman","Foremen",tf_hero|tf_randomize_face|tf_is_merchant|tf_alto|tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
[
itm_just_man_boots_medium,itm_just_man_boots_light,itm_just_man_shoes, #shoes
itm_phrygian15,itm_phrygian15,itm_phrygian14,
itm_ptunic_7, #tunics 2
itm_knife],
   def_attrib|level(5),wp(70),knows_common,man_face_middle_2, man_face_old_2],
  ["saltmine_capataz","Foreman","Foremen",tf_hero|tf_randomize_face|tf_is_merchant|tf_alto|tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
[
itm_just_man_boots_medium,itm_just_man_boots_light,itm_just_man_shoes, #shoes
itm_phrygian15,itm_phrygian15,itm_phrygian14,
itm_ptunic_7, #tunics 2
itm_knife,itm_wooden_stick],
   def_attrib|level(5),wp(70),knows_common,man_face_middle_1, man_face_old_1],
  ["lumbercamp_capataz","Lumber Camp Foreman","Lumber Camp Foremen",tf_hero|tf_randomize_face|tf_is_merchant|tf_alto|tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
[
itm_just_man_boots_medium,itm_just_man_boots_light,itm_just_man_shoes, #shoes
itm_phrygian15,itm_phrygian15,itm_phrygian14,
itm_ptunic_7, #tunics 2
itm_hatchet],
   def_attrib|level(5),wp(70),knows_common,man_face_middle_1, man_face_old_1],
  ["farmstead_boss","Farmstead Reeve","Farmstead Reeves",tf_hero|tf_randomize_face|tf_is_merchant|tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
[
itm_carbatinae_12qs,itm_just_man_boots_light,itm_just_man_shoes, #shoes
itm_red_cloak,itm_blue_cloak,itm_yellow2_cloak,itm_briton_tunic25, #tunics 2
itm_seax_4],
   def_attrib|level(15),wp(180),knows_common,man_face_middle_1, man_face_old_2],
  ["bandit_lairmerchant","Bandit Leader","Bandit Leader",tf_hero|tf_randomize_face|tf_is_merchant|tf_alto|tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
[
itm_just_man_boots_medium,itm_just_man_boots_light,itm_just_man_shoes, #shoes
itm_mail_shirt,itm_byrnie,itm_byrnie12,itm_mail_shirt_6, #tunics 2
itm_longseax1],
   def_attrib|level(5),wp(70),knows_common,man_face_old_1, man_face_old_2],
["abad","Abbot","Abbot",tf_hero|tf_randomize_face|tf_is_merchant|tf_guarantee_armor, no_scene,reserved, fac_commoners,
   [itm_robe, itm_robe2],
   def_attrib|level(12),wp(100),knows_cleric,sac_face_younger_1, sac_face_older_2],
["monjes","Monk","Monks",tf_randomize_face|tf_guarantee_armor,0,0,fac_commoners,
   []+monk_tunic,
   def_attrib|level(12),wp(100),knows_cleric,sac_face_younger_1, sac_face_older_2],
###chief acaba

  ["caravan_master","Caravan Master","Caravan Masters",tf_mounted|tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_commoners,
   []+common_pony+war_brit_shoes2+common_gambeson+horseman_skirmishes+basic_knives2+light_spears+mercenaries_roundshields,
   def_attrib2|level(26),wp(220),knows_warrior_normal,man_face_middle_1, man_face_old_2],

  ["kidnapped_girl","Kidnapped Girl","Kidnapped Girls",tf_hero|tf_female|tf_randomize_face|tf_unmoveable_in_party_window,0,reserved,fac_commoners,
   []+norse_women,
   def_attrib|level(12),wp(100),knows_common,woman_face_younger_1, woman_face_older_2],

#This troop is the troop marked as soldiers_end and town_walkers_begin
#briton
 ["town_walker_1","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
    []+common_shoes2+briton_tunic2+basic_knives3+briton_tunic3+briton_tunic,
   def_attrib|level(12),wp(100),knows_common,swadian_face_younger_1, swadian_face_older_2],
 ["town_walker_2","Townswoman","Townswomen",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   []+saxon_women+commonveil_women,
   def_attrib|level(12),wp(100),knows_common,woman_face_younger_1, woman_face_older_2],
#picto e irlandes
 ["town_walker_3","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
    []+common_shoes+irish_tunic+irish_tunic2+basic_knives2+pictish_hoodnaked,
   def_attrib|level(12),wp(100),knows_common,khergit_face_younger_1, rhodok_face_older_2],
 ["town_walker_4","Townswoman","Townswomen",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   []+gael_women+commonveil_women,
   def_attrib|level(12),wp(100),knows_common,woman_face_younger_1, woman_face_older_2],
#sajon
 ["town_walker_5","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
    []+common_shoes3+saxon_tunic+saxon_tunic2+basic_knives+angles_basic_tunic+common_phrygian2+decorated_phrygian,
   def_attrib|level(12),wp(100),knows_common,vaegir_face_younger_1, vaegir_face_older_2],
 ["town_walker_6","Townswoman","Townswomen",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   []+saxon_women+saxon_women2+commonveil_women,
   def_attrib|level(12),wp(100),knows_common,woman_face_younger_1, woman_face_older_2],
#norse
 ["town_walker_7","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
    []+common_shoes3+common_tunic+common_tunic2+basic_knives2+common_phrygian+common_phrygian2,
   def_attrib|level(12),wp(100),knows_common,nord_face_younger_1, nord_face_older_2],
 ["town_walker_8","Townswoman","Townswomen",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   []+norse_women+commonveil_women,
   def_attrib|level(12),wp(100),knows_common,womannorth_face_younger_1, womannorth_face_older_2],

#ninos 
 ["nino_varon","Child","Children",tf_nino|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
    []+irish_shoes+poor_tunic+child_tunic,
   def_attrib|level(12),wp(100),knows_common,nino_face_younger_1, nino_face_younger_2],

 ["nina_chica","Child","Children",tf_nina|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   []+women_shoes2+poor_tunic2+child_tunic2,
   def_attrib|level(12),wp(100),knows_common,nina_face_younger_1, nina_face_younger_2],
###ninos end
["monk_walker","Monk","Monks",tf_guarantee_armor,0,0,fac_commoners,
   []+monk_tunic,
   def_attrib|level(12),wp(100),knows_cleric,sac_face_younger_1, sac_face_older_2],
    
#This troop is the troop marked as town_walkers_end and village_walkers_begin
#briton
 ["village_walker_1","Villager","Villagers",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
    []+common_shoes2+briton_tunic2+basic_knives+briton_tunic3+briton_tunic,
   def_attrib|level(12),wp(100),knows_common,swadian_face_younger_1, swadian_face_older_2],
   ["village_walker_2","Villager","Villagers",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   []+saxon_women+commonveil_women,
   def_attrib|level(12),wp(100),knows_common,woman_face_younger_1, woman_face_older_2],
#pict and irish
 ["village_walker_3","Villager","Villager",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
     [itm_work_basket]+common_shoes+irish_tunic+irish_tunic2+basic_knives2+pictish_hoodnaked,
   def_attrib|level(12),wp(100),knows_common,khergit_face_younger_1, khergit_face_older_2],
 ["village_walker_4","Villager","Villager",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
    []+gael_women+commonveil_women,
   def_attrib|level(12),wp(100),knows_common,woman_face_younger_1, woman_face_older_2],
#sajon
 ["village_walker_5","Villager","Villager",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
    []+common_shoes3+saxon_tunic+saxon_tunic2+basic_knives+angles_basic_tunic+common_phrygian2+decorated_phrygian,
   def_attrib|level(12),wp(100),knows_common,vaegir_face_younger_1, vaegir_face_older_2],
 ["village_walker_6","Villager","Villager",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   []+saxon_women+saxon_women2+commonveil_women,
   def_attrib|level(12),wp(100),knows_common,woman_face_younger_1, woman_face_older_2],
#norse
 ["village_walker_7","Villager","Villagers",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
    [itm_work_basket]+common_shoes3+common_tunic+common_tunic2+basic_knives2+common_phrygian+common_phrygian2,
   def_attrib|level(12),wp(100),knows_common,nord_face_younger_1, nord_face_older_2],
 ["village_walker_8","Villager","Villager",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   []+norse_women+commonveil_women,
   def_attrib|level(12),wp(100),knows_common,womannorth_face_younger_1, womannorth_face_older_2],
#specials
 ["village_walker_1a","Villager","Villagers",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
    []+common_shoes3+common_hoodtunic2+basic_knives3+common_hoodtunic+common_phrygian+common_phrygian2,
   def_attrib|level(12),wp(100),knows_common,man_face_young_1, man_face_old_2],
 ["village_walker_3a","Villager","Villager",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
    []+common_shoes2+common_hoodtunic2+basic_knives2+briton_tunic3+common_hoodtunic,
   def_attrib|level(12),wp(100),knows_common,swadian_face_younger_1, swadian_face_older_2],
 ["village_walker_5a","Villager","Villager",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
    []+common_shoes3+common_hoodtunic+basic_knives+saxon_tunic2+common_hoodtunic+angles_basic_tunic+common_phrygian2+decorated_phrygian,
   def_attrib|level(12),wp(100),knows_common,man_face_young_1, man_face_old_2],
#This troop is the troop marked as village_walkers_end and spy_walkers_begin
 ["spy_walker_1","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
    []+common_shoes3+basic_knives+common_hoodtunic2,
   def_attrib|level(12),wp(100),knows_common,swadian_face_younger_1, swadian_face_older_2],
 ["spy_walker_2","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   []+norse_women+commonveil_women,
   def_attrib|level(12),wp(100),knows_common,woman_face_younger_1, woman_face_older_2],
# Ryan END

#This troop is the troop marked as spy_walkers_end
# Zendar
  ["tournament_master","Tournament Master","Tournament Master",tf_hero, scn_zendar_center|entry(1),reserved,  fac_commoners,[itm_bl_tunic01,itm_just_man_boots_medium],def_attrib|level(2),wp(20),knows_common,man_face_younger_1, man_face_older_2],
  ["trainer","Trainer","Trainer",tf_hero, scn_zendar_center|entry(2),reserved,  fac_commoners,[itm_btunic_8,itm_just_man_boots_medium],def_attrib|level(2),wp(20),knows_common,man_face_younger_1, man_face_older_2],
  ["Constable_Hareck","Constable Hareck","Constable Hareck",tf_hero, scn_zendar_center|entry(5),reserved,  fac_commoners,[itm_gambeson1,itm_just_man_boots_medium],def_attrib|level(5),wp(20),knows_common,0x0000000d180859d15a8476bbb332313200000000001e5d1d0000000000000000],

# Ryan BEGIN
  ["Ramun_the_slave_trader","Aethelmaer, the Slaver","Aethelmaer, the Slaver",tf_bajo|tf_hero, no_scene,reserved, fac_commoners,[itm_btunic_11,itm_just_man_boots_medium],def_attrib|level(5),wp(20),knows_common,0x0000000d1a0c52833b8a4ea4ecbabb2300000000001ea4930000000000000000],

  ["guide","Ulric","Ulric",tf_hero, no_scene,0,  fac_commoners,[itm_bl_tunic01,itm_just_man_boots_medium],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_younger_1, man_face_older_2],
# Ryan END

  ["Xerina","Anchoret the Pict","Anchoret",tf_hero|tf_osa, scn_the_happy_boar|entry(5),reserved,  fac_commoners,[itm_gambeson1,itm_just_man_boots_dark],
   def_attrib3|level(29),wp(300),knows_warrior_veteran,woman_face_younger_1, woman_face_older_2],
  ["Dranton","Niall the Briton","Niall",tf_hero, scn_the_happy_boar|entry(2),reserved,  fac_commoners,[itm_gambeson2,itm_carbatinae_1],
   def_attrib3|level(29),wp(300),knows_warrior_veteran,man_face_middle_1, man_face_old_2],
  ["Kradus","Uthred the Saxon","Kradus",tf_alto|tf_hero, scn_the_happy_boar|entry(3),reserved,  fac_commoners,[itm_gambeson3,itm_carbatinae_3],
   def_attrib3|level(29),wp(300),knows_warrior_veteran,man_face_middle_1, man_face_old_2],


#Tutorial
  ["tutorial_trainer","Training Ground Master","Training Ground Master",tf_hero, 0, 0, fac_commoners,[itm_robe,itm_carbatinae_1],def_attrib|level(2),wp(20),knows_common,0x000000000008414401e28f534c8a2d09],
  ["tutorial_student_1","{!}tutorial_student_1","{!}tutorial_student_1",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_sword, itm_practice_shield, itm_gambeson2,itm_gambeson1,itm_gambeson3,itm_carbatinae_1,itm_spangenhelm_1,itm_arena_helmet_yellow],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],
  ["tutorial_student_2","{!}tutorial_student_2","{!}tutorial_student_2",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_sword, itm_practice_shield, itm_gambeson2,itm_gambeson3,itm_gambeson3,itm_carbatinae_1,itm_spangenhelm_1,itm_arena_helmet_yellow],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],
  ["tutorial_student_3","{!}tutorial_student_3","{!}tutorial_student_3",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_staff, itm_gambeson3,itm_gambeson2,itm_gambeson1,itm_carbatinae_1,itm_spangenhelm_1,itm_arena_helmet_yellow],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],
  ["tutorial_student_4","{!}tutorial_student_4","{!}tutorial_student_4",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_staff, itm_gambeson3,itm_gambeson2,itm_gambeson1,itm_carbatinae_1,itm_spangenhelm_1,itm_arena_helmet_yellow],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],

#Sargoth
  #halkard, hardawk. lord_taucard lord_caupard. lord_paugard

#Salt mine
  ["Galeas","Balin","Balin",tf_hero, 0, reserved, fac_commoners,[itm_btunic_16,itm_carbatinae_12q],def_attrib|level(5),wp(20), knows_common, 0x0000000ebe0c224a6ce565c71b4ca8da00000000001de46e0000000000000000],

#Dhorak keep

  ["farmer_from_bandit_village","Farmer","Farmers",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_linen_tunic,itm_bl_tunic01,itm_ptunic_4,itm_carbatinae_1,itm_just_man_boots_medium],
   def_attrib|level(5),wp(70),knows_common,man_face_middle_1, man_face_older_2],
###Mike and Michael this is savegame compatible? Test plz!
#lair trainer player lair = trainer_2 chief
  ["trainer_2","Harald","Trainer",tf_hero, 0,reserved,  fac_commoners,[itm_gambeson41,itm_just_man_boots_medium],def_attrib|level(40),wp(20),knows_common,0x0000000e5a04360428ec253846640b5d0000000000000ee80000000000000000],
#mainquest veteran
  ["trainer_1","Veteran","Veteran",tf_hero, scn_training_ground_ranged_melee_1|entry(6),reserved,  fac_commoners,[itm_mail_shirt_1, itm_spatha, itm_viking_shield_round_07, itm_just_man_boots_medium],def_attrib|level(2),wp(20),knows_common,0x0000000d0d1030c74ae8d661b651c6840000000000000e220000000000000000],
  ["trainer_3","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_3|entry(6),reserved,  fac_commoners,[itm_gambeson1,itm_just_man_boots_medium],def_attrib|level(2),wp(20),knows_common,0x0000000e4a0445822ca1a11ab1e9eaea0000000000000f510000000000000000],
  ["trainer_4","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_4|entry(6),reserved,  fac_commoners,[itm_btunic_16,itm_just_man_boots_medium],def_attrib|level(2),wp(20),knows_common,0x0000000e600452c32ef8e5bb92cf1c970000000000000fc20000000000000000],
  ["trainer_5","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_5|entry(6),reserved,  fac_commoners,[itm_robe,itm_just_man_boots_medium],def_attrib|level(2),wp(20),knows_common,0x0000000e77082000150049a34c42ec960000000000000e080000000000000000],

# Ransom brokers.
  ["ransom_broker_1","Ransom Broker","Slave_Trader",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
   [itm_hoodtunic_01,itm_longseax1,itm_carbatinae_1],
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],
  ["ransom_broker_2","Ransom Broker","Slave_Trader",tf_bajo|tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
  [itm_hoodtunic_02,itm_longseax1,itm_carbatinae_2],
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],
  ["ransom_broker_3","Ransom Broker","Slave_Trader",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
   [itm_hoodtunic_03,itm_longseax1,itm_carbatinae_3],
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],
  ["ransom_broker_4","Ransom Broker","Slave_Trader",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
   [itm_btunic_1woman,itm_longseax1,itm_carbatinae_4],
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],
  ["ransom_broker_5","Ransom Broker","Slave_Trader",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
   [itm_bl_tunic03,itm_longseax1,itm_carbatinae_5],
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],
  ["ransom_broker_6","Ransom Broker","Slave_Trader",tf_alto|tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
  [itm_bl_tunic05,itm_longseax1,itm_carbatinae_6],
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],
  ["ransom_broker_7","Ransom Broker","Slave_Trader",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
   [itm_briton_tunic9,itm_longseax1,itm_carbatinae_7],
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],
  ["ransom_broker_8","Ransom Broker","Slave_Trader",tf_bajo|tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
   [itm_btunic_8,itm_longseax1,itm_carbatinae_8],
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],
  ["ransom_broker_9","Ransom Broker","Slave_Trader",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
   [itm_briton_tunic7,itm_longseax1,itm_carbatinae_9],
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],
  ["ransom_broker_10","Ransom Broker","Slave_Trader",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
   [itm_btunic_7,itm_longseax1,itm_just_man_boots_medium],
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],
#followers
  ["ransom_broker_20","Ransom Broker","Slave_Trader",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
   [itm_btunic_6,itm_longseax1,itm_just_man_boots_medium],
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],

# Tavern traveler.
  ["tavern_traveler_1","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
   [itm_btunic_8,itm_phrygian14,itm_carbatinae_7],
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],
  ["tavern_traveler_2","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
   [itm_btunic_10,itm_phrygian15,itm_carbatinae_8],
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],
  ["tavern_traveler_3","Traveller","Traveller",tf_alto|tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
   [itm_briton_tunic19,itm_phrygian16,itm_carbatinae_9],
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],
  ["tavern_traveler_4","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
   [itm_briton_tunic6,itm_phrygian17,itm_carbatinae_7],
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],
  ["tavern_traveler_5","Traveller","Traveller",tf_alto|tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
   [itm_briton_tunic14,itm_phrygian15,itm_carbatinae_8],
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],
  ["tavern_traveler_6","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
   [itm_brat1,itm_phrygian16,itm_just_man_boots_medium],
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],
  ["tavern_traveler_7","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
   [itm_bl_tunic04,itm_phrygian15,itm_just_man_boots_medium],
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],
  ["tavern_traveler_8","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
   [itm_picts_tunic_13,itm_phrygian14,itm_just_man_boots_medium],
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],
  ["tavern_traveler_9","Traveller","Traveller",tf_bajo|tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
   [itm_gael_tunic_01,itm_phrygian17,itm_just_man_boots_medium],
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],
  ["tavern_traveler_10","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
   [itm_gael_tunic_02,itm_phrygian16,itm_just_man_boots_medium],
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],

# Tavern traveler.
  ["tavern_bookseller_1","Book_Merchant","Book_Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_yellow_cloak,itm_carbatinae_2,
               itm_book_tactics, itm_book_persuasion, itm_book_wound_treatment_reference, itm_book_leadership, 
               itm_book_intelligence, itm_book_training_reference, itm_book_surgery_reference],def_attrib|level(5),wp(20),knows_common,man_face_middle_1,man_face_older_2],
  ["tavern_bookseller_2","Book_Merchant","Book_Merchant",tf_bajo|tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_btunic_7woman,itm_carbatinae_2,
               itm_book_wound_treatment_reference, itm_book_leadership, itm_book_intelligence, itm_book_trade, 
               itm_book_engineering, itm_book_weapon_mastery],def_attrib|level(5),wp(20),knows_common,man_face_middle_1, man_face_older_2],

# Tavern minstrel.
  ["tavern_minstrel_1","Wandering Skald","Minstrel",tf_alto|tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,
   []+elite_tunic+elite_norse_boots+common_music,
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],
  ["tavern_minstrel_2","Wandering Bard","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,
   []+angles_richtunic+elite_brit_boots+common_music2,
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],
  ["tavern_minstrel_3","Wandering Bard","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,
   []+briton_tunic+elite_shoes+common_music,
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],
  ["tavern_minstrel_4","Wandering Bard","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,
   []+pictish_hoodtunic+elite_pict_foot+common_music2,
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],
  ["tavern_minstrel_5","Wandering Bard","Minstrel",tf_bajo|tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,
   []+irish_brattunic+elite_gael_foot+common_music,
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],

   # ["bardo_tabernaend","bardo_end","Minstrel",tf_bajo|tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_btunic_11,itm_btunic_11, itm_just_man_boots_light, itm_lute],def_attrib|level(5),wp(20),knows_common,man_face_middle_1,man_face_older_2], #Lute or Byzantine/Occitan lyra
#damas de compania en tabernas
  ["quastuosa_1","Happy Widow","quastuosa",tf_female|tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
   [itm_pict_long_tunic1],
   def_attrib|level(12),wp(100),knows_common,woman_face_younger_1, woman_face_older_2],
  ["quastuosa_2","Happy Widow","quastuosa",tf_female|tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
   [itm_woman_saxon1,itm_womenshoes_3],
   def_attrib|level(12),wp(100),knows_common,woman_face_younger_1, woman_face_older_1],
  ["quastuosa_3","Happy Widow","quastuosa",tf_female|tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
   [itm_pict_long_tunic5],
   def_attrib|level(12),wp(100),knows_common,woman_face_younger_2, woman_face_older_2],
  ["quastuosa_4","Happy Widow","quastuosa",tf_alta|tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
   [itm_gael_tunic_01,itm_womenshoes_5],
   def_attrib|level(12),wp(100),knows_common,woman_face_younger_1, woman_face_older_2],
  ["quastuosa_5","Happy Widow","quastuosa",tf_female|tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
   [itm_btunic_4woman,itm_womenshoes_6],
   def_attrib|level(12),wp(100),knows_common,woman_face_younger_2, woman_face_older_2],
  ["quastuosa_6","Happy Widow","quastuosa",tf_female|tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
   [itm_btunic_3woman,itm_womenshoes_7],
   def_attrib|level(12),wp(100),knows_common,woman_face_younger_1, woman_face_older_2],
  ["quastuosa_7","Happy Widow","quastuosa",tf_baja|tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
   [itm_woman_norse1,itm_woman_saxon1],
   def_attrib|level(12),wp(100),knows_common,woman_face_younger_1, woman_face_older_1],
  ["quastuosa_end","Happy Widow","quastuosa",tf_female|tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
   [itm_pict_long_tunic4],
   def_attrib|level(12),wp(100),knows_common,woman_face_younger_1, woman_face_older_2],
#damas de compania acaba chief
 
#cortesanos y similares Chief
  # Bardos chief
  ["bardo_1","Kingdom Skald","Skald",tf_bajo|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_1_castle|entry(10), reserved, fac_commoners,
   []+elite_tunic+elite_norse_boots+common_music,
   def_attrib|level(12),wp(100),knows_common,man_face_middle_1, man_face_older_1],
  ["bardo_2","Kingdom Skald","Skald",tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_2_castle|entry(10), reserved, fac_commoners,
   []+elite_tunic+elite_shoes+common_music2,
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],
  ["bardo_3","Kingdom Skald","Skald",tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_3_castle|entry(10), reserved, fac_commoners,
   []+elite_tunic+elite_shoes+common_music,
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],
  ["bardo_4","Kingdom Skald","Skald",tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_4_castle|entry(10), reserved, fac_commoners,
   []+elite_tunic+elite_norse_boots+common_music2,
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],
  ["bardo_5","Kingdom Bard","Owain",tf_alto|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_5_castle|entry(10), reserved, fac_commoners,
   []+angles_richtunic+elite_brit_boots+common_music,
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],
  ["bardo_6","Kingdom Bard","Bard",tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_6_castle|entry(10), reserved, fac_commoners,
   []+angles_richtunic+elite_shoes+common_music2,
   def_attrib|level(12),wp(100),knows_common,man_face_middle_2, man_face_old_2],
  ["bardo_7","Kingdom Bard","Bard",tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_7_castle|entry(10), reserved, fac_commoners,
   []+angles_richtunic+elite_brit_boots+common_music,
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],
  ["bardo_8","Kingdom Skald","Skald",tf_bajo|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_8_castle|entry(10), reserved, fac_commoners,
   []+elite_tunic+elite_norse_boots+common_music,
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],
  ["bardo_9","Kingdom Bard","Bard",tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_9_castle|entry(10), reserved, fac_commoners,
   []+briton_tunic2+elite_brit_boots+common_music2,
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],
  ["bardo_10","Kingdom Bard","Bard",tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_10_castle|entry(10), reserved, fac_commoners,
   []+briton_tunic3+elite_shoes+common_music,
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],
  ["bardo_11","Kingdom Bard","Bard",tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_11_castle|entry(10), reserved, fac_commoners,
   []+briton_tunic+elite_brit_boots+common_music,
   def_attrib|level(12),wp(100),knows_common,man_face_middle_1, man_face_older_2],
  ["bardo_12","Kingdom Bard","Bard",tf_alto|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_12_castle|entry(10), reserved, fac_commoners,
   []+briton_tunic2+elite_shoes+common_music2,
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],
  ["bardo_13","Kingdom Bard","Bard",tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_13_castle|entry(10), reserved, fac_commoners,
   []+briton_tunic3+elite_brit_boots+common_music,
   def_attrib|level(12),wp(100),knows_common,man_face_middle_2, man_face_older_2],
  ["bardo_14","Kingdom Bard","Bard",tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_14_castle|entry(10), reserved, fac_commoners,
   []+irish_brattunic+elite_gael_foot+common_music,
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_old_2],
  ["bardo_15","Kingdom Bard","Bard",tf_bajo|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_15_castle|entry(10), reserved, fac_commoners,
   []+irish_brattunic+elite_gael_foot+common_music2,
   def_attrib|level(12),wp(100),knows_common,man_face_middle_2, man_face_old_2],
  ["bardo_16","Kingdom Bard","Bard",tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_16_castle|entry(10), reserved, fac_commoners,
   []+irish_brattunic+elite_gael_foot+common_music,
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],
  ["bardo_17","Kingdom Bard","Bard",tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_17_castle|entry(10), reserved, fac_commoners,
   []+irish_brattunic+elite_gael_foot+common_music2,
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_1],
  ["bardo_18","Kingdom Bard","Bard",tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_18_castle|entry(10), reserved, fac_commoners,
   []+irish_brattunic+elite_gael_foot+common_music,
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_middle_2],
  ["bardo_19","Kingdom Bard","Bard",tf_alto|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_19_castle|entry(10), reserved, fac_commoners,
   []+irish_brattunic+elite_gael_foot+common_music,
   def_attrib|level(12),wp(100),knows_common,man_face_younger_2, man_face_older_2],
  ["bardo_20","Kingdom Bard","Bard",tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_20_castle|entry(10), reserved, fac_commoners,
   []+pictish_hoodtunic+elite_shoes+common_music2,
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],
  ["bardo_21","Kingdom Bard","Bard",tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_21_castle|entry(10), reserved, fac_commoners,
   []+irish_brattunic+elite_gael_foot+common_music,
   def_attrib|level(12),wp(100),knows_common,man_face_younger_2, man_face_older_2],

# chief sacerdotes, obispos y abades, quest especial derfel Cadarn
  ["sacerdote_1","Christian Bishop","Christian Bishop",tf_hero|tf_randomize_face|tf_guarantee_armor, 0,0, fac_christians,
   []+priest_tunic,
   def_attrib|level(12),wp(100),knows_cleric,sac_face_younger_1, sac_face_older_2],
##  ["sacerdote_1","Christian Bishop","Christian Bishop",tf_bajo|tf_hero|tf_randomize_face|tf_guarantee_armor|tf_guarantee_boots, scn_town_1_castle|entry(11), reserved, fac_kingdom_5,
##   []+priest_tunic,
##   def_attrib|level(12),wp(100),knows_cleric,sac_face_younger_1, sac_face_older_2],
  ["sacerdote_2","Bishop Ealhheard","sacerdote",tf_hero|tf_randomize_face|tf_guarantee_armor|tf_guarantee_boots, no_scene,0, fac_kingdom_5,
   []+priest_tunic,
   def_attrib|level(12),wp(100),knows_cleric,sac_face_younger_1, sac_face_older_2],
##  ["sacerdote_3","Bishop Wulfhere","sacerdote",tf_bajo|tf_randomize_face|tf_hero|tf_guarantee_armor|tf_guarantee_boots, no_scene, reserved, fac_kingdom_8,
##   []+priest_tunic,
##   def_attrib|level(12),wp(100),knows_cleric,sac_face_younger_1, sac_face_older_2],
##  ["sacerdote_4","Abbot Aidan","sacerdote",tf_hero|tf_randomize_face|tf_guarantee_armor|tf_guarantee_boots, no_scene, reserved, fac_kingdom_11,
##   []+priest_tunic,
##   def_attrib|level(12),wp(100),knows_cleric,sac_face_younger_1, sac_face_older_2],
##  ["sacerdote_5","Abbot Saxulf","sacerdote",tf_alto|tf_randomize_face|tf_hero|tf_guarantee_armor|tf_guarantee_boots, no_scene, reserved, fac_kingdom_7,
##   []+priest_tunic,
##   def_attrib|level(12),wp(100),knows_cleric,sac_face_younger_1, sac_face_older_2],
##  ["sacerdote_6","Abbot Oudeceus","sacerdote",tf_hero|tf_randomize_face|tf_guarantee_armor|tf_guarantee_boots, no_scene, reserved, fac_kingdom_13,
##   []+priest_tunic,
##   def_attrib|level(12),wp(100),knows_cleric,sac_face_younger_1, sac_face_older_2],
##  ["sacerdote_7","Abbot Eadwine","sacerdote",tf_hero|tf_randomize_face|tf_guarantee_armor|tf_guarantee_boots, no_scene, reserved, fac_kingdom_7,
##   []+priest_tunic,
##   def_attrib|level(12),wp(100),knows_cleric,sac_face_younger_1, sac_face_older_2],
##  ["sacerdote_8","Abbot Mochonna","sacerdote",tf_hero|tf_randomize_face|tf_guarantee_armor|tf_guarantee_boots, no_scene, reserved, fac_kingdom_9,
##   []+priest_tunic,
##   def_attrib|level(12),wp(100),knows_cleric,sac_face_younger_1, sac_face_older_2],
##  ["sacerdote_9","Abbot Cuminian","sacerdote",tf_bajo|tf_randomize_face|tf_hero|tf_guarantee_armor|tf_guarantee_boots, no_scene, reserved, fac_kingdom_6,
##   []+priest_tunic,
##   def_attrib|level(12),wp(100),knows_cleric,sac_face_younger_1, sac_face_older_2],
##  ["sacerdote_10","High Abbot Flaithbertach mac Muirchertaigh","sacerdote",tf_hero|tf_randomize_face|tf_guarantee_armor|tf_guarantee_boots, no_scene, reserved, fac_kingdom_20,
##   []+priest_tunic,
##   def_attrib|level(12),wp(100),knows_cleric,sac_face_younger_1, sac_face_older_2],
##  ["sacerdote_11","Bishop Hunger","sacerdote",tf_hero|tf_randomize_face|tf_guarantee_armor|tf_guarantee_boots, no_scene, reserved, fac_kingdom_5,
##   []+priest_tunic,
##   def_attrib|level(12),wp(100),knows_cleric,sac_face_younger_1, sac_face_older_2],
##  ["sacerdote_12","Bishop Kenstec","sacerdote",tf_bajo|tf_hero|tf_randomize_face|tf_guarantee_armor|tf_guarantee_boots, no_scene, reserved, fac_kingdom_12,
##   []+priest_tunic,
##   def_attrib|level(12),wp(100),knows_cleric,sac_face_younger_1, sac_face_older_2],
##  ["sacerdote_13","Abbot Aedh Dubh","sacerdote",tf_bajo|tf_hero|tf_randomize_face|tf_guarantee_armor|tf_guarantee_boots, no_scene, reserved, fac_kingdom_21,
##   []+priest_tunic,
##   def_attrib|level(12),wp(100),knows_cleric,sac_face_younger_1, sac_face_older_2],
##  ["sacerdote_14","Monk Ceallach","sacerdote",tf_hero|tf_randomize_face|tf_guarantee_armor|tf_guarantee_boots, no_scene, reserved, fac_kingdom_20,
##   []+priest_tunic,
##   def_attrib|level(12),wp(100),knows_cleric,sac_face_younger_1, sac_face_older_2],

##  ["sacerdote_15","High Abbot Flaithbertach mac Muirchertaigh","sacerdote",tf_bajo|tf_randomize_face|tf_hero|tf_guarantee_armor|tf_guarantee_boots, no_scene,0, reserved, fac_kingdom_14,
##   []+priest_tunic,
##   def_attrib|level(12),wp(100),knows_cleric,sac_face_younger_1, sac_face_older_2],
##  ["sacerdote_16","Abbot Ciaran","sacerdote",tf_hero|tf_randomize_face|tf_guarantee_armor|tf_guarantee_boots, no_scene, reserved, fac_kingdom_15,
##   []+priest_tunic,
##   def_attrib|level(12),wp(100),knows_cleric,sac_face_younger_1, sac_face_older_2],
##  ["sacerdote_17","Abbot Dunghal","sacerdote",tf_alto|tf_hero|tf_randomize_face|tf_guarantee_armor|tf_guarantee_boots, no_scene, reserved, fac_kingdom_9,
##   []+priest_tunic,
##   def_attrib|level(12),wp(100),knows_cleric,sac_face_younger_1, sac_face_older_2],
##  ["sacerdote_18","Bishop Herefrith","sacerdote",tf_hero|tf_randomize_face|tf_guarantee_armor|tf_guarantee_boots, no_scene, reserved, fac_kingdom_7,
##   []+priest_tunic,
##   def_attrib|level(12),wp(100),knows_cleric,sac_face_younger_1, sac_face_older_2],
##  ["sacerdote_19","Monk Ceallach","sacerdote",tf_alto|tf_hero|tf_randomize_face|tf_guarantee_armor|tf_guarantee_boots, no_scene, reserved, fac_kingdom_16,
##   []+priest_tunic,
##   def_attrib|level(12),wp(100),knows_cleric,sac_face_younger_1, sac_face_older_2],
##  ["sacerdote_20","Bishop Fethgno mac Nechtain","sacerdote",tf_hero|tf_randomize_face|tf_guarantee_armor|tf_guarantee_boots, no_scene, reserved, fac_kingdom_18,
##   []+priest_tunic,
##   def_attrib|level(12),wp(100),knows_cleric,sac_face_younger_1, sac_face_older_2],
##  ["sacerdote_21","Abbot Fechin","sacerdote",tf_hero|tf_randomize_face|tf_guarantee_armor|tf_guarantee_boots, no_scene, reserved, fac_kingdom_10,
##   []+priest_tunic,
##   def_attrib|level(12),wp(100),knows_cleric,sac_face_younger_1, sac_face_older_2],
##  ["sacerdote_22","Abbot Aebbe","sacerdote",tf_hero|tf_randomize_face|tf_guarantee_armor|tf_guarantee_boots, no_scene, reserved, fac_kingdom_8,
##   []+priest_tunic,
##   def_attrib|level(12),wp(100),knows_cleric,sac_face_younger_1, sac_face_older_2],
##  ["sacerdote_23","Abbot Ultan","sacerdote",tf_bajo|tf_hero|tf_randomize_face|tf_guarantee_armor|tf_guarantee_boots, no_scene, reserved, fac_kingdom_17,
##   []+priest_tunic,
##   def_attrib|level(12),wp(100),knows_cleric,sac_face_younger_1, sac_face_older_2],
##  ["sacerdote_24","Bishop Cobo mac Crundmail","sacerdote",tf_hero|tf_randomize_face|tf_guarantee_armor|tf_guarantee_boots, no_scene, reserved, fac_kingdom_19,
##   []+priest_tunic,
##   def_attrib|level(12),wp(100),knows_cleric,sac_face_younger_1, sac_face_older_2],

#sacerdotes paganos
  ["paganop_1","Gothi","Gothar",tf_guarantee_armor, 0,0, fac_pagans,
   []+pagan_tunic,
   def_attrib|level(12),wp(100),knows_cleric,nord_face_young_1, nord_face_older_2],

##  ["paganop_1","Priest Thorgil","sacerdote",tf_hero|tf_randomize_face|tf_guarantee_armor|tf_guarantee_boots, scn_town_4_castle|entry(11), reserved, fac_kingdom_1,
##   []+pagan_tunic,
##   def_attrib|level(12),wp(100),knows_cleric,nord_face_young_1, nord_face_older_2],
##  ["paganop_2","Priest Harald","sacerdote",tf_hero|tf_randomize_face|tf_guarantee_armor|tf_guarantee_boots, no_scene,0, fac_kingdom_2,
##   []+pagan_tunic,
##   def_attrib|level(12),wp(100),knows_cleric,nord_face_young_1, nord_face_older_2],
##  ["paganop_3","Priest Gudrod","sacerdote",tf_hero|tf_randomize_face|tf_guarantee_armor|tf_guarantee_boots, no_scene, reserved, fac_kingdom_3,
##   []+pagan_tunic,
##   def_attrib|level(12),wp(100),knows_cleric,nord_face_young_1, nord_face_older_2],
##  ["paganop_4","Priest Barid","sacerdote",tf_bajo|tf_hero|tf_randomize_face|tf_guarantee_armor|tf_guarantee_boots, no_scene, reserved, fac_kingdom_8,
##   []+pagan_tunic,
##   def_attrib|level(12),wp(100),knows_cleric,nord_face_young_1, nord_face_older_2],
##  ["paganop_5","Priest Olaf","sacerdote",tf_bajo|tf_hero|tf_randomize_face|tf_guarantee_armor|tf_guarantee_boots, no_scene, reserved, fac_kingdom_4,
##   []+pagan_tunic,
##   def_attrib|level(12),wp(100),knows_cleric,nord_face_young_1, nord_face_older_2],

  ["priest_end","Priest both religions end","sacerdote",tf_bajo|tf_hero|tf_randomize_face|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_kingdom_4,
   []+pagan_tunic,
   def_attrib|level(12),wp(100),knows_cleric,nord_face_young_1, nord_face_older_2],
#sacerdotes chief acaba
  
  #Especiales npcs, aparecen en sitios concretos
  ["especiales_1","Hermit Derfel Gadarn","especiales",tf_alto|tf_hero|tf_guarantee_armor|tf_guarantee_boots, scn_castle_25_interior|entry(1), reserved, fac_commoners,[itm_robe, itm_just_man_boots_light],def_attrib|level(5),wp(20),knows_common,0x0000000fcd04d2802cdc4ca6692e3c9500000000001eb90b0000000000000000],
  
#NPC system changes begin
#Companions
  ["kingdom_heroes_including_player_begin",  "kingdom_heroes_including_player_begin",  "kingdom_heroes_including_player_begin",  tf_hero, 0,reserved,  fac_kingdom_1,[],          lord_attrib,wp(220),knows_lord_1, 0x000000000010918a01f248377289467d],
#40 points for skills #45 points for attributes
  ["npc1","Caio","Caio",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[(itm_hoodtunic_06, imod_crude),(itm_carbatinae_vc5,imod_tattered),itm_knife4, (itm_darts,imod_bent)],
   str_14 | agi_16 | int_8 | cha_7|level(5),wpex(99,72,91,91,72,101)|wp_firearm(91), #caio acabado
   knows_ironflesh_4|knows_power_strike_3|knows_power_throw_6|knows_power_draw_2|knows_maintenance_4|knows_weapon_master_3|knows_athletics_6|knows_riding_1|knows_looting_1|knows_tracking_4|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_3|knows_first_aid_1|knows_engineer_3|knows_persuasion_3|knows_leadership_2|knows_trade_3|knows_shield_1,
   0x000000003f106510329d852b9c56ab1a00000000001e3b120000000000000000], #chief acabado 
  ["npc2","Egil","Egil", tf_hero|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,[itm_btunic_14,itm_carbatinae_vc2v,(itm_axe_6, imod_chipped),(itm_light_spear4, imod_bent)],
    str_17 | agi_12 | int_8 | cha_14|level(11),wpex(98,91,110,91,91,91)|wp_firearm(91),
   knows_sea_king_2|knows_navigation_2|knows_ironflesh_8|knows_power_strike_8|knows_power_throw_8|knows_power_draw_2|knows_maintenance_3|knows_weapon_master_6|knows_athletics_6|knows_riding_3|knows_trainer_3|knows_tactics_4|knows_inventory_management_1|knows_first_aid_1|knows_persuasion_6|knows_leadership_7|knows_trade_2|knows_shield_3,
   0x00000005800866d05924ede72da938d400000000001eb4f20000000000000000], #chief acabado
  ["npc3","Brunhild","Brunhild",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_woman_norse3,itm_veil_b,itm_knife2],
    str_9 | agi_10 | int_14 | cha_12|level(5),wpex(91,72,91,80,72,91)|wp_firearm(100),
   knows_ironflesh_4|knows_power_strike_3|knows_power_throw_4|knows_maintenance_7|knows_weapon_master_1|knows_athletics_5|knows_looting_5|knows_inventory_management_6|knows_wound_treatment_2|knows_first_aid_7|knows_persuasion_6|knows_leadership_1|knows_trade_6|knows_shield_1,
   0x0000000038000011270e2a9db5b2c46300000000001ec7950000000000000000], #chief mainstory, lo conoce en la playa donde va a coger el barco #moto
  ["npc4","Donnchadh","Donnchadh",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_picts_tunic_15,(itm_just_man_boots_light, imod_tattered), (itm_light_spear1,imod_bent),itm_knife5],
    str_13 | agi_13 | int_14 | cha_10|level(11),wpex(110,72,91,91,72,98)|wp_firearm(91),
   knows_sea_king_1|knows_navigation_2|knows_ironflesh_6|knows_power_strike_3|knows_power_throw_6|knows_weapon_master_6|knows_athletics_5|knows_looting_6|knows_tracking_7|knows_tactics_5|knows_pathfinding_6|knows_spotting_6|knows_inventory_management_6|knows_first_aid_1|knows_persuasion_3|knows_leadership_5|knows_trade_5|knows_shield_2,
   0x000000002200479024e48e47ac6a4972000000000006281b0000000000000000], #chief acabado
  ["npc5","Morgant","Morgant",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[(itm_briton_tunic20, imod_crude),(itm_carbatinae_vc4, imod_ragged), itm_fustibalus2,itm_sling_lead,itm_club_hard],
    str_15 | agi_18 | int_9 | cha_8|level(13),wpex(91,72,91,102,72,103)|wp_firearm(91),
   knows_navigation_2|knows_ironflesh_7|knows_power_strike_5|knows_power_throw_5|knows_power_draw_3|knows_maintenance_4|knows_weapon_master_4|knows_athletics_5|knows_riding_8|knows_looting_9|knows_tactics_2|knows_pathfinding_2|knows_inventory_management_7|knows_first_aid_1|knows_engineer_1|knows_persuasion_4|knows_leadership_2|knows_trade_6|knows_shield_2,
   0x000000001a04218816a992a9ac95a4d400000000001ea95c0000000000000000], #chief acabado
  ["npc6","Bodo","Bodo",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_hoodtunic_02,itm_carbatinae_1,itm_javelin, itm_long_light_spear2],
    str_14 | agi_11 | int_10 | cha_14|level(9),wpex(111,91,91,91,91,91)|wp_firearm(91),
   knows_ironflesh_7|knows_power_strike_7|knows_power_throw_7|knows_maintenance_3|knows_weapon_master_5|knows_athletics_5|knows_riding_4|knows_trainer_5|knows_tactics_5|knows_inventory_management_4|knows_first_aid_2|knows_persuasion_7|knows_leadership_7|knows_trade_1|knows_shield_3,
  0x00000004b40c628d45188ce8ae8e592300000000001d9c9b0000000000000000], #chief acabado
  ["npc7","Dwywei","Dwywei",tf_baja|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_ptunic_6woman,(itm_womenshoes_3, imod_ragged), itm_hunting_crossbow, itm_bolts, itm_knife],
    str_10 | agi_12 | int_12 | cha_12|level(7),wpex(91,72,91,72,95,72)|wp_firearm(91), #chief acabado
   knows_ironflesh_3|knows_power_strike_4|knows_power_throw_5|knows_power_draw_5|knows_maintenance_2|knows_weapon_master_6|knows_athletics_6|knows_riding_5|knows_looting_6|knows_tracking_3|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_5|knows_wound_treatment_4|knows_surgery_2|knows_first_aid_5|knows_persuasion_7|knows_leadership_5|knows_trade_3|knows_shield_2,
   0x000000002d00600212ae47566c71d88b00000000001e3dec0000000000000000], #moto
  ["npc8","Reginhard","Reginhard",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[(itm_phrygian15, imod_ragged), (itm_btunic_5woman,imod_tattered), (itm_carbatinae_vc1s, imod_ragged), (itm_long_light_spear2, imod_cracked),itm_seax_4, (itm_javelin, imod_bent)],
    str_11 | agi_15 | int_10 | cha_10|level(12),wpex(91,73,125,91,72,91)|wp_firearm(91), #lo conoce en la taberna en la quest principal
   knows_navigation_2|knows_ironflesh_5|knows_power_strike_5|knows_power_throw_5|knows_power_draw_3|knows_weapon_master_6|knows_athletics_6|knows_riding_2|knows_looting_7|knows_tracking_5|knows_tactics_2|knows_pathfinding_7|knows_spotting_3|knows_inventory_management_5|knows_first_aid_3|knows_persuasion_3|knows_leadership_3|knows_trade_5|knows_shield_2,
   0x0000000d6e040b037ae68dd5b4f5532c00000000001e34da0000000000000000], #chief acabado
  ["npc9","Clovis","Clovis",tf_alto|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_bl_tunic08,(itm_carbatinae_vc5, imod_tattered), (itm_heavy_spear2, imod_bent),(itm_throwing_spears2, imod_bent),(itm_phrygian10, imod_ragged)],
    str_15 | agi_12 | int_13 | cha_9|level(13),wpex(101,101,101,92,91,100)|wp_firearm(91),
   knows_sea_king_1|knows_navigation_1|knows_ironflesh_7|knows_power_strike_7|knows_power_throw_7|knows_power_draw_2|knows_maintenance_6|knows_weapon_master_6|knows_athletics_4|knows_riding_4|knows_trainer_5|knows_tactics_6|knows_inventory_management_6|knows_first_aid_3|knows_engineer_3|knows_persuasion_4|knows_leadership_5|knows_trade_3|knows_shield_3,
   0x0000000a7f0c55d4689a4da2b28ac72700000000001d26ed0000000000000000], #chief acabado
  ["npc10","Ceawlin","Ceawlin",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[(itm_bl_tunic12, imod_crude),(itm_carbatinae_vc1s, imod_tattered), itm_long_light_spear1, itm_seax_1,(itm_throwing_spears, imod_bent)],
    str_20 | agi_12 | int_6 | cha_11|level(11),wpex(106,91,103,91,91,91)|wp_firearm(91),
   knows_ironflesh_9|knows_power_strike_9|knows_power_throw_9|knows_maintenance_3|knows_weapon_master_6|knows_athletics_8|knows_riding_2|knows_looting_6|knows_trainer_1|knows_tactics_1|knows_inventory_management_4|knows_first_aid_3|knows_persuasion_1|knows_leadership_3|knows_trade_2|knows_shield_3,
   0x00000008cb0826cc195ba5c8e1d2d33200000000001ec91c0000000000000000], #chief acabado
  ["npc11","Solveig","Solveig",tf_alta|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_btunic_11, (itm_carbatinae_2v, imod_tattered), itm_war_spear2,(itm_throwing_spears, imod_cracked),(itm_axe_7, imod_chipped)], #Solveig, ayuda a player en emboscada
    str_12 | agi_8 | int_12 | cha_18|level(10),wpex(110,85,100,40,0,100)|wp_firearm(50),
   knows_sea_king_1|knows_navigation_1|knows_ironflesh_6|knows_power_strike_4|knows_power_throw_4|knows_power_draw_6|knows_maintenance_4|knows_weapon_master_4|knows_athletics_6|knows_riding_4|knows_trainer_1|knows_spotting_2|knows_inventory_management_4|knows_wound_treatment_2|knows_first_aid_4|knows_persuasion_9|knows_leadership_9|knows_trade_3|knows_shield_2,
   0x000000000010100828de9214614e4a5200000000001de0a40000000000000000], #moto
  ["npc12","Asbjorn","Asbjorn",tf_hero|tf_guarantee_armor|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_robe6, itm_staff, itm_sling3, itm_sling_rock1],
    str_14 | agi_12 | int_14 | cha_7|level(5),wpex(91,72,91,80,72,82)|wp_firearm(91),
   knows_ironflesh_6|knows_power_strike_1|knows_power_throw_5|knows_power_draw_2|knows_weapon_master_2|knows_athletics_4|knows_riding_4|knows_tactics_2|knows_inventory_management_7|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_7|knows_engineer_1|knows_persuasion_7|knows_leadership_3|knows_trade_4|knows_shield_1,
   0x00000008cb001508452311ba9d75d91900000000001d16650000000000000000], #chief acabado
  ["npc13","Helgi","Helgi",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_btunic_12,(itm_carbatinae_10, imod_tattered), itm_light_spear2,(itm_throwing_spears, imod_bent),(itm_hatchet, imod_rusty),itm_phrygian16],
    str_15 | agi_12 | int_12 | cha_12|level(13),wpex(117,72,92,72,72,72)|wp_firearm(91),
   knows_sea_king_4|knows_navigation_6|knows_ironflesh_7|knows_power_strike_7|knows_power_throw_7|knows_maintenance_4|knows_weapon_master_6|knows_athletics_4|knows_looting_2|knows_pathfinding_2|knows_inventory_management_7|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_3|knows_persuasion_6|knows_trainer_3|knows_leadership_6|knows_trade_7|knows_shield_2,
   0x00000008c00c3214189c2d8002ce330c00000000001e2b8b0000000000000000], #chief acabado
  ["npc14","Ailchu","Ailchu",tf_bajo|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_gael_tunic_02,(itm_just_man_boots_light, imod_ragged), (itm_pictish_hatchet11, imod_chipped),(itm_darts, imod_bent)],
    str_8 | agi_19 | int_10 | cha_8|level(11),wpex(95,72,114,87,72,91)|wp_firearm(91),
   knows_ironflesh_6|knows_power_strike_4|knows_power_throw_4|knows_power_draw_4|knows_maintenance_5|knows_weapon_master_9|knows_athletics_9|knows_riding_9|knows_looting_9|knows_inventory_management_4|knows_first_aid_4|knows_engineer_1|knows_persuasion_2|knows_leadership_2|knows_trade_4|knows_shield_2,
   0x000000078010120f26c432b56d6948db00000000001da59a0000000000000000], #chief acabado
  ["npc15","Agathinos","Agathinos",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_hoodtunic_04,(itm_carbatinae_vc3, imod_tattered), itm_knife3,itm_sling2, itm_sling_rock1],
    str_9 | agi_9 | int_18 | cha_8|level(6),wpex(91,72,103,78,72,91)|wp_firearm(91),
   knows_navigation_4|knows_ironflesh_5|knows_power_strike_4|knows_power_throw_3|knows_maintenance_9|knows_weapon_master_4|knows_athletics_5|knows_riding_3|knows_looting_1|knows_tactics_9|knows_inventory_management_5|knows_first_aid_1|knows_engineer_9|knows_persuasion_4|knows_leadership_4|knows_trade_4|knows_shield_1,
   0x0000000f3f0470807894959ae227335a00000000001d29240000000000000000], #chief acabado
  ["npc16","Beda","Beda",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_robe, itm_knife,itm_staff],
    str_9 | agi_9 | int_14 | cha_13|level(6),wpex(91,72,91,82,77,78)|wp_firearm(91),
   knows_ironflesh_5|knows_power_throw_4|knows_weapon_master_1|knows_athletics_4|knows_riding_2|knows_looting_4|knows_tactics_5|knows_inventory_management_5|knows_wound_treatment_7|knows_surgery_5|knows_first_aid_7|knows_engineer_4|knows_persuasion_7|knows_leadership_5|knows_trade_6|knows_shield_1,
   0x0000000ea60c6204431548ea53d2325600000000001da98a0000000000000000], #chief acabado 

#NPC system changes end
#lords and kings equipament
#                   Horse   Bodywear    Footwear_in       Footwear_out      Armor   Weapon     Shield   Headwaer

###sample_king
##[itm_common_horse,itm_brat1,itm_gaelshoes_1,itm_byrnie35,itm_leather_gloves,itm_irish_long_sword1,itm_tab_shield_round_08_nodevice,itm_crown1,itm_knife2,itm_javelin_skirmishes,itm_trophy_c],
##   king_attrib,wp(420),king_skills,rhodok_face_younger_1, rhodok_face_older_2],
###sample_lords swords
##[itm_common_pony,itm_brat1,itm_gaelshoes_1,itm_byrnie5,itm_leather_gloves,itm_irish_long_sword2,itm_tab_shield_round_06_device,itm_angle_helmet5,itm_knife2,itm_javelin_skirmishes,itm_trophy_c],
##   lord_attrib,wp(380),knows_lord_1,rhodok_face_younger_1, rhodok_face_older_2],

########################REYES                                                                                              Horse          Bodywear                Footwear_in                              Footwear_out                              Armor                                 Weapon                  Shield                  Headwaer
  ["kingdom_1_lord",  "Konungr Horik Gottfredsson",  "Horik Gottfredsson",  tf_alto|tf_hero, 0,reserved,  fac_kingdom_1,
[itm_common_pony,itm_btunic_12,itm_carbatinae_11q,itm_byrnie33,itm_leather_gloves,itm_noble_sword,itm_tab_shield_round_07_device,itm_crown1,itm_longseax10,itm_throwing_spears2,itm_trophy_c],
   king_attrib,wp(420),king_skills,0x00000006c10432053123b0a55495db1d00000000001ebc6b0000000000000000],
#  ["kingdom_1_lord",  "King Sigifrid Angantyrsson",  "Kingdom 1 Lord",  tf_hero, 0,reserved,  fac_kingdom_1,[itm_common_horse,   itm_bl_tunic03,        itm_just_man_boots_dark,     itm_carbatinae_11qs,  itm_mail_shirt_8,          itm_leather_gloves,    itm_seax_1,      itm_tab_shield_round_c,       itm_briton_helm13, itm_trophy_c],          knight_attrib_5,wp(280),knight_skills_5|knows_trainer_5, 0x0000000f45041105241acd2b5a66a86900000000001e98310000000000000000],
  #??? Sigurd Orm i Oje (Snake-in-the-Eye) Ragnarson was not mentioned as king until 873. King was possibly Erik Barn (the Child), last survivor of the royal civil war following 854 http://en.wikipedia.org/wiki/List_of_legendary_kings_of_Denmark
#sigurd is old lord yet. Horik II is mentioned until 864 in your source (3 years before 867). Sigfred is mentioned in 873 (4 years more late that VC begining). Ok, Horik II is usable.
  ["kingdom_2_lord",  "Konungr Harald Halfdanarson",  "Harald Halfdanarson",  tf_hero, 0,reserved,  fac_kingdom_2,
[itm_common_pony2,itm_btunic_14,itm_carbatinae_12q,itm_addon_mail4,itm_leather_gloves,itm_noble_sword_2,itm_tab_shield_round_09_device,itm_crown1,itm_longseax9,itm_throwing_spears2,itm_trophy_c],
   king_attrib,wp(420),king_skills,0x00000000370c29072ca271ba8b92d89100000000001d4a9d0000000000000000],
  #not king until 872 (and no kingdom until then either). From the death of his father in 860, his uncle Guthorm was regent of their petty kingdom of Vestfold
  #technically, he should be Harald Tanglehair at this time, since he had vowed not to comb his hair until he became king of Norway http://en.wikipedia.org/wiki/Harald_Fairhair
  ["kingdom_3_lord",  "Konungr Gudrod Ragnarson",  "Gudrod Ragnarson",  tf_hero, 0,reserved,  fac_kingdom_3,
[itm_common_pony,itm_btunic_16,itm_carbatinae_11q,itm_byrnie34,itm_leather_gloves,itm_noble_sword_3,itm_tab_shield_round_07_device,itm_crown1,itm_longseax8,itm_throwing_spears,itm_trophy_c],
   king_attrib,wp(420),king_skills,0x000000084d0862c34149d14a7468931c00000000001ea3120000000000000000],
  ["kingdom_4_lord",  "Konungr Hrorek Hemmingsson",  "Hrorek Hemmingsson",  tf_hero, 0,reserved,  fac_kingdom_4,
[itm_common_pony2,itm_btunic_15,itm_carbatinae_12q,itm_byrnie8,itm_leather_gloves,itm_noble_sword_4,itm_tab_shield_round_09_device,itm_crown1,itm_longseax7,itm_throwing_spears,itm_trophy_c],
   king_attrib,wp(420),king_skills,0x0000000854087807285d69d3332d68d200000000001e4cab0000000000000000],

  ["kingdom_5_lord",  "Brytenwalda Aethelred Aethelwulfing",  "Aethelred Aethelwulfing",  tf_alto|tf_hero, 0,reserved,  fac_kingdom_5,
[itm_common_pony,itm_bl_tunic07,itm_carbatinae_11qs,itm_mail_shirt_13_1,itm_leather_gloves,itm_noble_sword,itm_tab_shield_round_05_device,itm_crown1,itm_longseax5,itm_javelin,itm_trophy_c],
   king_attrib,wp(420),king_skills,0x0000000c891017842b63ca571c25998400000000001f4d4d0000000000000000],
  ["kingdom_6_lord",  "Cyning Eadmund Aethelberhting",  "Eadmund Aethelberhting",  tf_alto|tf_hero, 0,reserved,  fac_kingdom_6,
[itm_common_pony2,itm_ptunic_7,itm_carbatinae_12qs,itm_byrnie28,itm_leather_gloves,itm_noble_sword_2,itm_tab_shield_round_05_nodevice,itm_crown1,itm_longseax4,itm_javelin,itm_trophy_c],
   king_attrib,wp(420),king_skills,0x0000000bd200284836d08dbadaade76300000000001f56d80000000000000000],
  ["kingdom_7_lord",  "Cyning Brugred Beorhtwulfing",  "Brugred Beorhtwulfing",  tf_hero, 0,reserved,  fac_kingdom_7,
[itm_common_pony,itm_ptunic_6,itm_carbatinae_13qs,itm_byrnie30,itm_leather_gloves,itm_noble_sword_3,itm_tab_shield_round_06_nodevice,itm_crown1,itm_longseax3,itm_javelin,itm_trophy_c],
   king_attrib,wp(420),king_skills,0x0000000564082247435b0ee5f6a8f59c00000000001e8bd20000000000000000],

  ["kingdom_8_lord",  "Jarl Halfdan Ragnarsson",  "Halfdan Ragnarsson",  tf_hero, 0,reserved,  fac_kingdom_8,
[itm_common_pony,itm_btunic_13,itm_carbatinae_12q,itm_byrnie34,itm_leather_gloves,itm_sword_premium3,itm_tab_shield_round_07_nodevice,itm_viking_noblehelm1,itm_longseax7,itm_throwing_spears2,itm_trophy_c],
   king_attrib,wp(420),king_skills,0x00000006c60c438d46a99538b23248ae00000000001e359b0000000000000000],

  ["kingdom_9_lord",  "Ri Rhodri map Merfyn",  "Rhodri map Merfyn",  tf_alto|tf_hero, 0,reserved,  fac_kingdom_9,
[itm_common_horse,itm_briton_tunic10,itm_carbatinae_11q,itm_mail_shirt_10,itm_leather_gloves,itm_noble_sword_7,itm_tab_shield_round_08_nodevice,itm_crown1,itm_knife2,itm_javelin,itm_trophy_c],
   king_attrib,wp(420),king_skills,0x00000008aa08d1cf3a9952c8e17a32de00000000001dd71c0000000000000000],
  ["kingdom_10_lord",  "Ri Elisedd map Tewdr",  "Elisedd map Tewdr",  tf_hero, 0,reserved,  fac_kingdom_10,
 [itm_common_horse,itm_briton_tunic11,itm_carbatinae_12q,itm_mail_shirt_11,itm_leather_gloves,itm_noble_sword_8,itm_tab_shield_round_10_nodevice,itm_crown1,itm_knife3,itm_javelin,itm_trophy_c],
   king_attrib,wp(420),king_skills,0x000000089e002091186493392265c8e400000000001e96220000000000000000], #cara real rey chief
  ["kingdom_11_lord",  "Ri Arthgal map Dumnagual",  "Arthgal map Dumnagual",  tf_alto|tf_hero, 0,reserved,  fac_kingdom_11,
 [itm_common_horse,itm_briton_tunic9,itm_carbatinae_11q,itm_mail_shirt_10,itm_leather_gloves,itm_noble_sword_9,itm_tab_shield_round_11_nodevice,itm_crown1,itm_knife4,itm_javelin,itm_trophy_c],
   king_attrib,wp(420),king_skills,0x00000003fc041144245396b72cb5db6e00000000001ea9560000000000000000], #cara real rey chief
  ["kingdom_12_lord",  "Ri Dunyart map Eferferdyn",  "Dunyart map Eferferdyn",  tf_hero, 0,reserved,  fac_kingdom_12,
 [itm_common_horse,itm_briton_tunic8,itm_carbatinae_12q,itm_mail_shirt_11,itm_leather_gloves,itm_noble_sword_10,itm_tab_shield_round_08_nodevice,itm_crown1,itm_knife5,itm_javelin,itm_trophy_c],
   king_attrib,wp(420),king_skills,0x0000000fc60c544732e4923b558d38f500000000001db7260000000000000000], #cara real rey chief
  ["kingdom_13_lord",  "Ri Hywel map Rhys",  "Hywel map Rhys",  tf_hero, 0,reserved,  fac_kingdom_13,
 [itm_common_horse,itm_briton_tunic13,itm_carbatinae_11q,itm_mail_shirt_10,itm_leather_gloves,itm_noble_sword_11,itm_tab_shield_round_10_nodevice,itm_crown1,itm_knife2,itm_javelin,itm_trophy_c],
   king_attrib,wp(420),king_skills,0x00000008811003c812db8b3c9bc526dc00000000001e5b240000000000000000], #cara real rey chief

  ["kingdom_14_lord",  "Ruire Lethlobar mac Loingsig",  "Lethlobar mac Loingsig",  tf_hero, 0,reserved,  fac_kingdom_14,
[itm_common_horse,itm_brat1,itm_gaelshoes_1,itm_byrnie11,itm_leather_gloves,itm_irish_long_sword1,itm_tab_shield_round_06_nodevice,itm_crown1,itm_knife2,itm_javelin_skirmishes,itm_trophy_c],
   king_attrib,wp(420),king_skills,0x0000000e010441533699513c5b6e94f200000000001da6ac0000000000000000],
  ["kingdom_15_lord",  "Ruire Dunlaing mac Muiredaig",  "Dunlaing mac Muiredaig",  tf_hero, 0,reserved,  fac_kingdom_15,
[itm_common_horse2,itm_brat2,itm_gaelshoes_2,itm_byrnie12,itm_leather_gloves,itm_irish_long_sword2,itm_tab_shield_round_08_nodevice,itm_crown1,itm_knife,itm_javelin_skirmishes,itm_trophy_c],
   king_attrib,wp(420),king_skills,0x00000008a108704528d395c7a28f34cb00000000001d88e40000000000000000],
  ["kingdom_16_lord",  "Ruire Cenn Faelad hua Mugthigirn",  "Cenn Faelad hua Mugthigirn",  tf_hero, 0,reserved,  fac_kingdom_16,
[itm_common_horse,itm_brat3,itm_gaelshoes_3,itm_byrnie11,itm_leather_gloves,itm_irish_long_sword2,itm_tab_shield_round_11_nodevice,itm_crown1,itm_knife3,itm_javelin_skirmishes,itm_trophy_c],
   king_attrib,wp(420),king_skills,0x00000008910815864ae4f532eb4a48ce00000000001eca250000000000000000],
  ["kingdom_17_lord",  "Ruire Mugron mac Cothaid",  "Mugron mac Cothaid",  tf_hero, 0,reserved,  fac_kingdom_17,
[itm_common_horse2,itm_brat4,itm_gaelshoes_3,itm_byrnie12,itm_leather_gloves,itm_irish_long_sword1,itm_tab_shield_round_10_nodevice,itm_crown1,itm_knife4,itm_javelin_skirmishes,itm_trophy_c],
   king_attrib,wp(420),king_skills, 0x000000088a086547246d88b8d92cc55b00000000001d596a0000000000000000],
  ["kingdom_18_lord",  "Ard Ruire Aed mac Niall",  "Aed mac Niall",  tf_alto|tf_hero, 0,reserved,  fac_kingdom_18,
[itm_common_horse,itm_briton_tunic24,itm_gaelshoes_1,itm_byrnie11,itm_leather_gloves,itm_irish_long_sword2,itm_tab_shield_round_06_nodevice,itm_crown1,itm_knife2,itm_javelin_skirmishes,itm_trophy_c],
   king_attrib,wp(420),king_skills, 0x0000000fe21072801b2357ccc56a426400000000001f6b760000000000000000],
  ["kingdom_19_lord",  "Ruire Donnchad mac Eochocai",  "Donnchad mac Eochocai",  tf_hero, 0,reserved,  fac_kingdom_19,
[itm_common_horse2,itm_briton_tunic25,itm_gaelshoes_2,itm_byrnie12,itm_leather_gloves,itm_irish_long_sword1,itm_tab_shield_round_08_nodevice,itm_crown1,itm_knife5,itm_javelin_skirmishes,itm_trophy_c],
   king_attrib,wp(420),king_skills,0x000000065205920736a269baa652572900000000001dd8ae0000000000000000],
  ["kingdom_20_lord",  "Ruire Causantin mac Cinaeda",  "Causantin mac Cinaeda",  tf_hero, 0,reserved,  fac_kingdom_20,
[itm_common_horse,itm_briton_tunic26,itm_just_man_boots_dark,itm_mail_shirt_8,itm_leather_gloves,itm_irish_long_sword2,itm_tab_shield_round_11_nodevice,itm_crown1,itm_knife4,itm_javelin_skirmishes,itm_trophy_c],
   king_attrib,wp(420),king_skills,0x0000000a74116356591c8a266c92c96200000000001e3aa50000000000000000],
  ["kingdom_21_lord",  "Ruire Cerball mac Dunlainge",  "Cerball mac Dunlainge",  tf_hero, 0,reserved,  fac_kingdom_21,
[itm_common_horse2,itm_briton_tunic27,itm_gaelshoes_2,itm_byrnie12,itm_leather_gloves,itm_irish_long_sword1,itm_tab_shield_round_10_nodevice,itm_crown1,itm_knife3,itm_javelin_skirmishes,itm_trophy_c],
    king_attrib,wp(420),king_skills,0x0000000ff900b846495daa389d55e88d00000000001dc8e40000000000000000], #face moto
  
#                                                                                                              Horse                   Bodywear                Armor                               Footwear_in                 Footwear_out                        Headwear                    Weapon               Shield
  #Swadian civilian clothes: itm_btunic_11 itm_btunic_16 itm_gambeson2 itm_gambeson2 itm_nobleman_outfit itm_rich_outfit itm_btunic_10 itm_tabard
  #Older knights with higher skills moved to top
  ["knight_1_1", "Jarl Sigifrid Angantyrsson", "Sigifrid Angantyrsson", tf_bajo|tf_hero, 0, reserved,  fac_kingdom_1,
 [itm_common_pony,itm_carbatinae_11qs,itm_lamellar_armor2,itm_leather_gloves,itm_noble_sword,itm_tab_shield_round_09_device,itm_vikingold_elitehelm8,itm_longseax10,itm_throwing_spears,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_8,0x0000000f401046515cf671b5558dd89300000000001e38f30000000000000000],
  ["knight_1_2", "Jarl Bagsecg", "Bagsecg", tf_hero, 0, reserved,  fac_kingdom_1,
  [itm_common_pony2,itm_carbatinae_12qs,itm_byrnie31,itm_leather_gloves,itm_noble_sword_2,itm_tab_shield_round_02_device,itm_vikingold_elitehelm9,itm_longseax9,itm_throwing_spears2,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_8,0x00000001d904698d4624c9a8db45b7a400000000001d47190000000000000000],
  ["knight_1_3", "Jarl Halfdan Angantyrsson", "Halfdan Angantyrsson", tf_hero, 0, reserved,  fac_kingdom_1,
 [itm_common_pony,itm_carbatinae_14qv,itm_byrnie19,itm_leather_gloves,itm_heavy_spear1,itm_tab_shield_round_07_nodevice,itm_vikingold_elitehelm9,itm_longseax7,itm_throwing_spears,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_8,0x00000007a6002194125b6db6cb6db6db00000000001db6c30000000000000000],
  ["knight_1_4", "Hersir Gothormr", "Gothormr", tf_hero, 0, reserved,  fac_kingdom_1,
 [itm_carbatinae_12qs,itm_byrnie18,itm_leather_gloves,itm_axe_10,itm_tab_shield_round_12_device,itm_viking_noblehelm1,itm_longseax8,itm_throwing_spears2,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_8,0x000000029710034536db6db6db6db6db00000000001db6db0000000000000000],
#ragnar's son
  ["knight_1_5", "Jarl Sigurd Ragnarsson", "Sigurd Ragnarsson", tf_hero, 0, reserved,  fac_kingdom_1,
 [itm_common_pony,itm_carbatinae_11qs,itm_byrnie17,itm_leather_gloves,itm_premium_spear1,itm_tab_shield_round_09_device,itm_vikingold_elitehelm8,itm_longseax7,itm_throwing_spears2, itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_9,0x0000000d860c730535346de89b88caa400000000001cc7290000000000000000],
  ["knight_1_6", "Hersir Helgi Hvassi", "Helgi Hvassi", tf_alto|tf_hero, 0, reserved,  fac_kingdom_1,
 [itm_common_pony2,itm_carbatinae_12qs,itm_byrnie16,itm_leather_gloves,itm_one_handed_war_axe_f,itm_tab_shield_round_07_device,itm_viking_noblehelm2,itm_longseax9,itm_throwing_spears, itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_8,0x00000008f20c09c358d2e246d3b3365300000000001f20d40000000000000000],
#  ["knight_1_1", "Jarl Godafrid Haraldsson", "Jarl Godafrid Haraldsson", tf_hero, 0, reserved,  fac_kingdom_1, [itm_arabian_horse_a,itm_bl_tunic09,      itm_byrnie7,   itm_carbatinae_12q, itm_carbatinae_11qs,       itm_spangenhelm_13,           itm_noble_sword_8,  itm_leather_gloves,         itm_tab_shield_round_c],   knight_attrib_3,wp(240),knight_skills_3|knows_trainer_3, 0x00000007a6002194125b6db6cb6db6db00000000001db6c30000000000000000], #adorno chief

  ["knight_2_1", "Jarl Guthorm Haraldrsson", "Guthorm Haraldrsson", tf_hero, 0, reserved,  fac_kingdom_2,
 [itm_common_pony,itm_carbatinae_14qv,itm_byrnie34,itm_leather_gloves,itm_noble_sword_4,itm_tab_shield_round_12_device,itm_vikingold_elitehelm8,itm_longseax10,itm_throwing_spears2, itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_8,0x0000000e720cb7cb5d148e3b5b6a2da100000000001e14990000000000000000], #cara real
  ["knight_2_2", "Konungr Eirik", "Eirik", tf_alto|tf_hero, 0, reserved,  fac_kingdom_2,
 [itm_common_pony,itm_carbatinae_12qs,itm_byrnie33,itm_leather_gloves,itm_noble_sword_5,itm_tab_shield_round_07_nodevice,itm_vikingold_elitehelm9,itm_longseax7,itm_throwing_spears,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_8,0x0000000d800c30c3099126a49c71c8eb00000000001d859c0000000000000000], #cara real
  ["knight_2_3", "Jarl Kjotvi Hinn Audgi", "Kjotvi Hinn Audgi", tf_hero, 0, reserved,  fac_kingdom_2,
 [itm_common_pony,itm_carbatinae_12qs,itm_byrnie32,itm_leather_gloves,itm_heavy_spear2,itm_tab_shield_round_09_nodevice,itm_vikingold_elitehelm8,itm_longseax8,itm_throwing_spears,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_8,0x00000001ad0c620628ab4c688b2ddb1b0000000000113caa0000000000000000], #cara real
  ["knight_2_4", "Hersir Ketill Bjornsson", "Ketill Bjornsson", tf_alto|tf_hero, 0, reserved,  fac_kingdom_2,
 [itm_carbatinae_11qs,itm_byrnie31,itm_leather_gloves,itm_axe_10,itm_tab_shield_round_12_nodevice,itm_viking_noblehelm1,itm_long_bow2,itm_barbed_arrows,itm_longseax6,itm_throwing_spears2,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_8,0x0000000d950c470838cc0ca46c914ae600000000001ea6130000000000000000], #cara real
  ["knight_2_5", "Hersir Bjorn Ketilsson", "Bjorn Ketilsson", tf_hero, 0, reserved,  fac_kingdom_2,
 [itm_carbatinae_14qv,itm_byrnie16,itm_leather_gloves,itm_axe_4,itm_tab_shield_round_07_nodevice,itm_viking_noblehelm2,itm_longseax8,itm_throwing_spears,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_8,0x0000000da70825d0449c71b94cb1b51200000000000e38e30000000000000000], #cara real

  ["knight_3_1", "Jarl Olaf Gudrodrsson", "Olaf Gudrodrsson", tf_hero, 0, reserved,  fac_kingdom_3,
 [itm_common_pony,itm_carbatinae_11qs,itm_byrnie33,itm_leather_gloves,itm_noble_sword,itm_tab_shield_round_09_nodevice,itm_vikingold_elitehelm9,itm_throwing_spears,itm_longseax6,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_6,0x0000000d8510974858c44e56eb71409b00000000001d991c0000000000000000],
  ["knight_3_2", "Jarl Ivar Gudrodrsson", "Ivarr Gudrodrsson", tf_bajo|tf_hero, 0, reserved,  fac_kingdom_3,
 [itm_common_pony,itm_carbatinae_12qs,itm_byrnie18,itm_leather_gloves,itm_noble_sword_2,itm_tab_shield_round_12_nodevice,itm_vikingold_elitehelm9,itm_throwing_spears,itm_longseax7,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_6,0x00000006a31028104b2c0552f561c71400000000001ebd2c0000000000000000],
  ["knight_3_3", "Jarl Asl Gudrodrsson", "Asl Gudrodrsson", tf_hero, 0, reserved,  fac_kingdom_3,
 [itm_common_pony,itm_carbatinae_11qs,itm_byrnie19,itm_leather_gloves,itm_noble_sword_6,itm_tab_shield_round_07_device,itm_vikingold_elitehelm8,itm_throwing_spears,itm_longseax9,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_6,0x000000044804174336db6db6db6db6db00000000001d86db0000000000000000],
  ["knight_3_4", "Jarl Orkan", "Orkan", tf_hero, 0, reserved,  fac_kingdom_3,
 [itm_carbatinae_11qs,itm_byrnie31,itm_leather_gloves,itm_noble_sword_5,itm_tab_shield_round_09_device,itm_viking_noblehelm2,itm_throwing_spears,itm_longseax9,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_6,0x0000000f3a00048e576342c89c95b49c00000000001f549b0000000000000000],
  ["knight_3_5", "Jarl Helgi Ketilsson", "Helgi Ketilsson", tf_hero, 0, reserved,  fac_kingdom_3,
 [itm_common_pony,itm_carbatinae_14qv,itm_byrnie32,itm_leather_gloves,itm_noble_sword_2,itm_tab_shield_round_12_device,itm_viking_noblehelm3,itm_throwing_spears2,itm_longseax8,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_6,0x000000089500628838dbdad6ed2db6db00000000001e851b0000000000000000],
  ["knight_3_6", "Hersir Eystein Olafsson", "Eystein Olafsson", tf_hero, 0, reserved,  fac_kingdom_3,
 [itm_carbatinae_11qs,itm_byrnie33,itm_leather_gloves,itm_axe_10,itm_tab_shield_round_09_device,itm_viking_noblehelm1,itm_throwing_spears2,itm_longseax10,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_6,0x000000000d1061913513dab9116950cc00000000001cd5240000000000000000],
  ["knight_3_7", "Hersir Sygtrygg Ivarrsson", "Sygtrygg Ivarrsson", tf_alto|tf_hero, 0, reserved,  fac_kingdom_3,
 [itm_carbatinae_14qv,itm_byrnie34,itm_leather_gloves,itm_axe_4,itm_tab_shield_round_07_device,itm_viking_noblehelm2,itm_throwing_spears2,itm_longseax6,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_6,0x000000011100695071ac8ccfd3113b0900000000001e06150000000000000000],
  ["knight_3_8", "Hersir Thorstein Olafsson", "Thorstein Olafsson", tf_hero, 0, reserved,  fac_kingdom_3,
 [itm_common_pony,itm_carbatinae_11qs,itm_addon_mail7,itm_leather_gloves,itm_heavy_spear3,itm_tab_shield_round_12_device,itm_viking_noblehelm3,itm_throwing_spears,itm_longseax8,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_6,0x00000007c90430902612f8a45d8ebaae00000000001ea76d0000000000000000],
#  ["knight_3_9", "Hersir Sigfroth Ivarrsson", "Hersir Sigfroth Ivarrsson", tf_hero, 0, reserved,  fac_kingdom_3, [  itm_mail_shirt_5,  itm_mail_shirt_5,   itm_carbatinae_4,  itm_carbatinae_11qs,   itm_spangenhelm_17, itm_leather_gloves, itm_sword_7,  itm_tab_shield_round_c, itm_throwing_spears2],      knight_attrib_1,wp(200),knight_skills_1|knows_trainer_1, 0x0000000d030812002c92aa3c94ca18a300000000001e36b50000000000000000],

  ["knight_4_1", "Jarl Harald Hemmingsson", "Haraldr Hemmingsson", tf_hero, 0, reserved,  fac_kingdom_4,
 [itm_common_pony,itm_carbatinae_14qv,itm_byrnie34,itm_leather_gloves,itm_noble_sword_3,itm_tab_shield_round_07_nodevice,itm_spangenhelm_39,itm_throwing_spears,itm_longseax10,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_6,0x00000006e700430e4961c62a927814e400000000001f4ca40000000000000000],
  ["knight_4_2", "Jarl Gotrik Haraldsson", "Gotrik Haraldsson", tf_bajo|tf_hero, 0, reserved,  fac_kingdom_4,
 [itm_common_pony,itm_carbatinae_12qs,itm_byrnie35,itm_leather_gloves,itm_heavy_spear2,itm_tab_shield_round_09_nodevice,itm_spangenhelm_40,itm_throwing_spears2,itm_longseax7,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_6,0x00000006e0047188375c8d24d3b2d78b00000000001dac640000000000000000],
  ["knight_4_3", "Jarl Hrodulf Haraldsson", "Hrodulfr Haraldsson", tf_hero, 0, reserved,  fac_kingdom_4,
 [itm_common_pony2,itm_carbatinae_11qs,itm_mail_shirt_11_2,itm_leather_gloves,itm_axe_10,itm_tab_shield_round_12_nodevice,itm_spangenhelm_39,itm_throwing_spears,itm_longseax6,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_6,0x00000006df04570628acb945986a992a00000000001e32dc0000000000000000],

  ["knight_5_1", "Aetheling Aelfred Aethelwulfing", "Aelfred Aethelwulfing", tf_hero, 0, reserved,  fac_kingdom_5,
[itm_common_pony,itm_red_cloak,itm_carbatinae_12qs,itm_mail_shirt_13_1,itm_leather_gloves,itm_noble_sword_2,itm_tab_shield_round_01_device,itm_spangenhelm_39,itm_longseax1,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x00000004bc0063832c9cb627938d626e00000000001de9030000000000000000], #alfred
  ["knight_5_2", "Ealdorman Aethelmod", "Aethelmod", tf_hero, 0, reserved,  fac_kingdom_5,
[itm_common_pony2,itm_yellow_cloak,itm_carbatinae_11qs,itm_mail_shirt_5_2,itm_leather_gloves,itm_noble_sword_2,itm_tab_shield_round_01_nodevice,itm_spangenhelm_40,itm_longseax3,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x00000003520c24cd1adbf736b70db6db00000000001e98eb0000000000000000],
  ["knight_5_3", "Ealdorman Wulfhere", "Wulfhere", tf_bajo|tf_hero, 0, reserved,  fac_kingdom_5,
[itm_common_pony,itm_blue_cloak,itm_carbatinae_13qs,itm_mail_shirt_13_4,itm_leather_gloves,itm_noble_sword_2,itm_tab_shield_round_02_device,itm_spangenhelm_39,itm_longseax4,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x00000003400076414892b3434d95466e00000000001c12ea0000000000000000],
  ["knight_5_4", "Ealdorman Aelfstan", "Aelfstan", tf_hero, 0, reserved,  fac_kingdom_5,
[itm_common_pony2,itm_red_cloak,itm_carbatinae_14qs,itm_mail_shirt_13_2,itm_leather_gloves,itm_noble_sword,itm_tab_shield_round_02_nodevice,itm_spangenhelm_40,itm_longseax3,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x000000035b08404528f58e335cb5531c00000000001d116d0000000000000000],
  ["knight_5_5", "Ealdorman Cuthred", "Cuthred", tf_alto|tf_hero, 0, reserved,  fac_kingdom_5,
[itm_common_pony,itm_yellow2_cloak,itm_carbatinae_14qs,itm_mail_shirt_13_4,itm_leather_gloves,itm_noble_sword,itm_tab_shield_round_02_nodevice,itm_spangenhelm_39,itm_longseax5,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000c2e04318138db8d3755ce572d00000000001da6f30000000000000000],
  ["knight_5_6", "Ealdorman Bucca", "Bucca", tf_hero, 0, reserved,  fac_kingdom_5,
[itm_common_pony,itm_red_cloak,itm_carbatinae_14qs,itm_mail_shirt_13_3,itm_leather_gloves,itm_noble_sword_3,itm_tab_shield_round_02_nodevice,itm_spangenhelm_40,itm_longseax5,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000c1204330f36eed72f5b28a50b00000000001f0d540000000000000000],
  ["knight_5_7", "Ealdorman Wulfred", "Wulfred", tf_hero, 0, reserved,  fac_kingdom_5,
[itm_common_pony2,itm_green_cloak,itm_carbatinae_13qs,itm_byrnie21,itm_leather_gloves,itm_heavy_spear1,itm_tab_shield_round_02_device,itm_spangenhelm_39,itm_longseax2,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000348082783465398b9638f4adc00000000001da78b0000000000000000],
  ["knight_5_8", "Ealdorman Wigstan", "Wigstan", tf_hero, 0, reserved,  fac_kingdom_5,
[itm_common_pony,itm_green_cloak,itm_carbatinae_13qs,itm_mail_shirt_13_3,itm_leather_gloves,itm_noble_sword_3,itm_tab_shield_round_03_device,itm_spangenhelm_39,itm_longseax4,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x00000003ab000983059d48fb094c541100000000001ecf1e0000000000000000],
  ["knight_5_9", "Ealdorman Sigeberht Sigewulfing", "Sigeberht Sigewulfing", tf_hero, 0, reserved,  fac_kingdom_5,
[itm_common_pony2,itm_yellow2_cloak,itm_carbatinae_12qs,itm_byrnie21,itm_leather_gloves,itm_heavy_spear1,itm_tab_shield_round_03_device,itm_spangenhelm_36,itm_longseax3,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x000000070a046187671aab050837a39100000000001e57550000000000000000],
  ["knight_5_10", "Ealdorman Garulf", "Garulf", tf_hero, 0, reserved,  fac_kingdom_5,
[itm_common_pony,itm_blue_cloak,itm_carbatinae_12qs,itm_byrnie22,itm_leather_gloves,itm_noble_sword_4,itm_tab_shield_round_03_device,itm_spangenhelm_37,itm_longseax2,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x000000073100214b3903fb14d4a9a8ed00000000001e47150000000000000000],
  ["knight_5_11", "Dryhten Drihtwald", "Drihtwald", tf_alto|tf_hero, 0, reserved,  fac_kingdom_5,
[itm_yellow_cloak,itm_carbatinae_11qs,itm_byrnie8,itm_leather_gloves,itm_one_handed_war_axe_f,itm_tab_shield_round_01_device,itm_spangenhelm_15,itm_longseax1,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x000000012904648736db6db6db6db6db00000000001db6db0000000000000000],

  ["knight_6_1", "Ealdorman Oswald", "Oswald", tf_hero, 0, reserved,  fac_kingdom_6,
[itm_common_pony,itm_green_cloak,itm_carbatinae_12qs,itm_byrnie28,itm_leather_gloves,itm_noble_sword_5,itm_tab_shield_round_01_device,itm_spangenhelm_39,itm_longseax1,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x00000007241068c44caaea569136978400000000001e88b10000000000000000],
  ["knight_6_2", "Ealdorman Aethelred", "Aethelred", tf_hero, 0, reserved,  fac_kingdom_6,
[itm_common_pony2,itm_leather_cloak,itm_carbatinae_12qs,itm_byrnie24,itm_leather_gloves,itm_noble_sword_5,itm_tab_shield_round_02_device,itm_spangenhelm_40,itm_longseax3,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x00000007200c09045554cab54a0e9d2a00000000001e036c0000000000000000],
  ["knight_6_3", "Ealdorman Ealhhere", "Ealhhere", tf_alto|tf_hero, 0, reserved,  fac_kingdom_6,
[itm_common_pony2,itm_red_cloak,itm_carbatinae_13qs,itm_byrnie25,itm_leather_gloves,itm_heavy_spear1,itm_tab_shield_round_03_device,itm_spangenhelm_40,itm_longseax2,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000d4d0c804447138ddcd370945c00000000001f29170000000000000000],
  ["knight_6_4", "Dryhten Eanfrith", "Eanfrith", tf_hero, 0, reserved,  fac_kingdom_6,
[itm_red_cloak,itm_carbatinae_13qs,itm_mail_shirt_11_2,itm_leather_gloves,itm_one_handed_war_axe_c,itm_tab_shield_round_01_device,itm_spangenhelm_37,itm_longseax4,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x000000074c04278022db4ddbc42ab39000000000001e84280000000000000000],
  ["knight_6_5", "Dryhten Ecgwald", "Ecgwald", tf_hero, 0, reserved,  fac_kingdom_6,
[itm_leather_cloak,itm_carbatinae_14qs,itm_byrnie21,itm_leather_gloves,itm_one_handed_war_axe_c,itm_tab_shield_round_02_device,itm_spangenhelm_36,itm_longseax5,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x000000042e0822945b0d89cae672c7a400000000001d44e30000000000000000],

  ["knight_7_1", "Ealdorman Ceowulf Ceowulfing", "Ceowulf Ceowulfing", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_common_pony,itm_yellow_cloak,itm_carbatinae_14qs,itm_byrnie30,itm_leather_gloves,itm_noble_sword_6,itm_tab_shield_round_01_nodevice,itm_spangenhelm_40,itm_longseax2,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x000000094d004184375d99c16de0225300000000001d89210000000000000000],
  ["knight_7_2", "Ealdorman Hereberht", "Hereberht", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_common_pony,itm_yellow_cloak,itm_carbatinae_11qs,itm_byrnie27,itm_leather_gloves,itm_noble_sword_6,itm_tab_shield_round_02_nodevice,itm_spangenhelm_40,itm_longseax1,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000d650c87942d55939691d624ce00000000001d49130000000000000000],
  ["knight_7_3", "Ealdorman Aethelred", "Aethelred", tf_bajo|tf_hero, 0, reserved,  fac_kingdom_7,
[itm_common_pony,itm_green_cloak,itm_carbatinae_11qs,itm_byrnie28,itm_leather_gloves,itm_noble_sword_6,itm_tab_shield_round_03_nodevice,itm_spangenhelm_39,itm_longseax5,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000cdd0c9a0042a151b4db9128ea00000000001e8ce30000000000000000],
  ["knight_7_4", "Ealdorman Aethelred Mucel", "Aethelred Mucel", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_common_pony2,itm_red_cloak,itm_carbatinae_14qs,itm_byrnie29,itm_leather_gloves,itm_heavy_spear1,itm_tab_shield_round_01_nodevice,itm_spangenhelm_40,itm_longseax2,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000e5e00914644a39248616d431e00000000001e1d190000000000000000],
  ["knight_7_5", "Ealdorman Aelfgar", "Aelfgar", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_common_pony,itm_green_cloak,itm_carbatinae_14qs,itm_byrnie30,itm_leather_gloves,itm_heavy_spear1,itm_tab_shield_round_02_nodevice,itm_spangenhelm_39,itm_longseax3,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x00000006780c2007546ed67b4567aab800000000001e04510000000000000000],
  ["knight_7_6", "Ealdorman Aethulf", "Aethulf", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_common_pony2,itm_yellow2_cloak,itm_carbatinae_13qs,itm_byrnie23,itm_leather_gloves,itm_noble_sword,itm_tab_shield_round_03_nodevice,itm_spangenhelm_39,itm_longseax4,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x00000006680031c41aed37c28c4a830b00000000001e8e340000000000000000],
  ["knight_7_7", "Ealdorman Beornoth", "Beornoth", tf_alto|tf_hero, 0, reserved,  fac_kingdom_7,
[itm_common_pony,itm_yellow2_cloak,itm_carbatinae_13qs,itm_byrnie24,itm_leather_gloves,itm_noble_sword_2,itm_tab_shield_round_01_nodevice,itm_spangenhelm_37,itm_longseax5,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000db20851454d24699893d0da4900000000001e0a940000000000000000],
  ["knight_7_8", "Ealdorman Sigberth", "Sigberth", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_common_pony2,itm_blue_cloak,itm_carbatinae_12qs,itm_mail_shirt_5_2,itm_leather_gloves,itm_noble_sword_2,itm_tab_shield_round_02_nodevice,itm_spangenhelm_15,itm_longseax1,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000da410818d469ab4c2c156f30400000000001dab1b0000000000000000],
  ["knight_7_9", "Dryhten Aethelwulf Aethelreding", "Aethelwulf Aethelreding", tf_hero, 0, reserved,  fac_kingdom_7,
 [itm_blue_cloak,itm_carbatinae_12qs,itm_byrnie21,itm_leather_gloves,itm_one_handed_war_axe_f,itm_tab_shield_round_03_nodevice,itm_spangenhelm_15,itm_longseax2,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x00000001640425055cebaf01138a8ba200000000001d16e30000000000000000],

  ["knight_8_1", "Cyning Egbert", "Egbert", tf_bajo|tf_hero, 0, reserved,  fac_kingdom_8,
[itm_common_pony,itm_yellow2_cloak,itm_carbatinae_11qs,itm_byrnie24,itm_leather_gloves,itm_noble_sword_2,itm_tab_shield_round_01_device,itm_crown1,itm_longseax4,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x00000009661097054b594acc948e486100000000000cc6f30000000000000000],
  ["knight_8_2", "Jarl Rathbarth Ragnarsson", "Rathbarth Ragnarsson", tf_hero, 0, reserved,  fac_kingdom_8,
 [itm_common_pony,itm_carbatinae_12qs,itm_byrnie16,itm_leather_gloves,itm_noble_sword_4,itm_tab_shield_round_07_nodevice,itm_vikingold_elitehelm8,itm_throwing_spears,itm_longseax2,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_6,0x000000068a0c46d46b1489a5134e2cdd00000000001eb9620000000000000000],
  ["knight_8_3", "Ealdorman Ealdred", "Ealdred", tf_hero, 0, reserved,  fac_kingdom_8,
[itm_common_pony,itm_red_cloak,itm_carbatinae_12qs,itm_byrnie27,itm_leather_gloves,itm_noble_sword_3,itm_tab_shield_round_02_device,itm_spangenhelm_39,itm_longseax8,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000dca00105026d36dd8e38e2b2200000000001f38cd0000000000000000],
  ["knight_8_4", "Jarl Sidroc the Elder", "Sidroc the Elder", tf_hero, 0, reserved,  fac_kingdom_8,
 [itm_common_pony,itm_carbatinae_14qv,itm_byrnie17,itm_leather_gloves,itm_noble_sword_6,itm_tab_shield_round_09_device,itm_vikingold_elitehelm8,itm_throwing_spears2,itm_longseax7,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_6,0x00000008e8047285272ac192d70a8a6300000000001ea9100000000000000000],
  ["knight_8_5", "Ealdorman Ricsige", "Ricsige", tf_hero, 0, reserved,  fac_kingdom_8,
[itm_common_pony2,itm_green_cloak,itm_carbatinae_13qs,itm_byrnie26,itm_leather_gloves,itm_heavy_spear1,itm_tab_shield_round_03_device,itm_spangenhelm_35,itm_longseax6,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_6,0x0000000ba908594146918cd73192faeb000000000016244a0000000000000000],
  ["knight_8_6", "Ealdorman Egbert the Second", "Egbert the Second", tf_hero, 0, reserved,  fac_kingdom_8,
[itm_red_cloak,itm_carbatinae_14qs,itm_byrnie28,itm_leather_gloves,itm_one_handed_war_axe_f,itm_tab_shield_round_01_device,itm_spangenhelm_36,itm_longseax8,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1,0x0000000baf087295572e95cb5b31c0d900000000001e451d0000000000000000],
###Bjorn Ironside
  ["knight_8_7", "Jarl Bjorn Ragnarsson", "Bjorn Jarnsida", tf_alto|tf_hero, 0, reserved,  fac_kingdom_8,
 [itm_common_pony,itm_carbatinae_12qs,itm_lamellar_armor,itm_leather_gloves,itm_noble_sword_3,itm_tab_shield_round_12_device,itm_viking_noblehelm1,itm_throwing_spears2,itm_longseax9,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_6,0x00000002fb04798838acb940946ca75a00000000001f54ee0000000000000000],
#######
  ["knight_8_8", "Hersir Guthred Knutr", "Guthred Knutr", tf_hero, 0, reserved,  fac_kingdom_8,
 [itm_common_pony,itm_carbatinae_12qs,itm_byrnie19,itm_leather_gloves,itm_noble_sword_4,itm_tab_shield_round_07_device,itm_vikingold_elitehelm8,itm_throwing_spears,itm_longseax10,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_5,0x0000000771103342351aad95226cbc9b00000000001c57140000000000000000],
  ["knight_8_9", "Hersir Rognvald", "Rognvald", tf_hero, 0, reserved,  fac_kingdom_8,
 [itm_common_pony,itm_carbatinae_14qv,itm_byrnie31,itm_leather_gloves,itm_heavy_spear3,itm_tab_shield_round_07_nodevice,itm_vikingold_elitehelm9,itm_throwing_spears,itm_longseax7,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_5,0x0000000b0f1035854ab18eccad95baa200000000001ebb190000000000000000],
  ["knight_8_10", "Hersir Harald", "Harald", tf_bajo|tf_hero, 0, reserved,  fac_kingdom_8,
 [itm_common_pony,itm_carbatinae_14qv,itm_byrnie32,itm_leather_gloves,itm_heavy_spear1,itm_tab_shield_round_09_nodevice,itm_vikingold_elitehelm8,itm_throwing_spears2,itm_longseax6,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_5,0x000000074604318c36a1da269d71b8d900000000001caf740000000000000000],
  ["knight_8_11", "Hersir Sidroc the Young", "Sidroc the Young", tf_alto|tf_hero, 0, reserved,  fac_kingdom_8,
 [itm_carbatinae_12qs,itm_lamellar_armor2,itm_leather_gloves,itm_axe_4,itm_tab_shield_round_09_nodevice,itm_vikingold_elitehelm9,itm_throwing_spears,itm_longseax10,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_5,0x0000000bb50c119366d492d79488b6d800000000001d29160000000000000000],
  ["knight_8_12", "Hersir Fraena", "Fraena", tf_hero, 0, reserved,  fac_kingdom_8,
 [itm_carbatinae_14qv,itm_byrnie34,itm_leather_gloves,itm_axe_10,itm_tab_shield_round_12_nodevice,itm_vikingold_elitehelm8,itm_throwing_spears,itm_longseax9,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_5,0x00000007100c1507132d4a38e645c6d200000000001db6e40000000000000000],
###invasores, deberian ser otra faccion?
  ["knight_8_13", "Jarl Ivarr Inn Beinlaussi", "Ivarr Inn Beinlaussi", tf_hero, 0, reserved,  fac_kingdom_8,
 [itm_common_pony,itm_carbatinae_14qv,itm_byrnie33,itm_leather_gloves,itm_noble_sword_6,itm_tab_shield_round_09_device,itm_viking_noblehelm3,itm_longseax8,itm_long_bow3,itm_barbed_arrows,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_6,0x00000001ba0050052aeb58b85a0ed54100000000001caadd0000000000000000], #ivar
  ["knight_8_14", "Jarl Hubbi Ragnarsson", "Hubbi Ragnarsson",  tf_oso|tf_hero, 0, reserved,  fac_kingdom_8,
 [itm_common_pony,itm_carbatinae_11qs,itm_mail_shirt_13_3,itm_leather_gloves,itm_noble_sword_5,itm_tab_shield_round_07_device,itm_viking_noblehelm2,itm_throwing_spears2,itm_longseax6,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_5,0x0000000188080b4d4aa0523a5ba8a526000000000012e4ec0000000000000000], #hubbi
#come in 871 with summer heathen army?
  ["knight_8_15", "Konungr Bagsecg", "Bagsecg", tf_hero, 0, reserved,  fac_kingdom_8,
 [itm_common_pony,itm_carbatinae_12qs,itm_byrnie18,itm_leather_gloves,itm_noble_sword_4,itm_tab_shield_round_12_device,itm_viking_noblehelm1,itm_throwing_spears,itm_longseax7,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_5,0x00000006c7005885676b6aa84d6cb79b00000000001e39150000000000000000],

  ["knight_9_1", "Mael Anarawd map Rhodri", "Anarawd map Rhodri", tf_hero, 0, reserved,  fac_kingdom_9,
[itm_common_horse,itm_briton_tunic9,itm_carbatinae_13qs,itm_mail_shirt_10,itm_leather_gloves,itm_noble_swordv3,itm_tab_shield_round_05_device,itm_briton_helm33,itm_knife2,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x000000044900018832a696b4da8dc59300000000001d46b20000000000000000], #cara real rey chief
  ["knight_9_2", "Mael Cadell map Rhodri", "Cadell map Rhodri", tf_hero, 0, reserved,  fac_kingdom_9,
[itm_common_horse2,itm_briton_tunic10,itm_carbatinae_14qs,itm_mail_shirt_11,itm_leather_gloves,itm_noble_sword_8,itm_tab_shield_round_08_device,itm_briton_helm34,itm_knife4,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x000000003208654d27244a5b0cd242d200000000001ec34a0000000000000000], 
  ["knight_9_3", "Mael Merfyn map Rhodri", "Merfyn map Rhodri", tf_bajo|tf_hero, 0, reserved,  fac_kingdom_9,
[itm_common_pony2,itm_briton_tunic11,itm_carbatinae_14qs,itm_byrnie13,itm_leather_gloves,itm_noble_swordv6,itm_tab_shield_round_10_device,itm_briton_helm33,itm_knife4,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x000000038b0453492663827dce85569f00000000001cfaa30000000000000000], 
  ["knight_9_4", "Ri Gwgon map Meurig", "Gwgon map Meurig", tf_hero, 0, reserved,  fac_kingdom_9,
[itm_common_pony,itm_briton_tunic12,itm_carbatinae_13qs,itm_byrnie14,itm_leather_gloves,itm_noble_sword_7,itm_tab_shield_round_11_device,itm_briton_helm34,itm_knife2,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000fd60c115015636ddb5c2cd36b00000000001ed69c0000000000000000], 
  ["knight_9_5", "Guledic Gwriad map Merfyn", "Gwriad map Merfyn", tf_hero, 0, reserved,  fac_kingdom_9,
[itm_common_pony2,itm_briton_tunic13,itm_carbatinae_12qs,itm_byrnie15,itm_leather_gloves,itm_noble_swordv,itm_tab_shield_round_06_device,itm_briton_helm33,itm_knife2,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000a070c4387374bd19addd2a4ab00000000001e32cc0000000000000000], 
  ["knight_9_6", "Mael Tudwal map Rhodri", "Tudwal map Rhodri", tf_alto|tf_hero, 0, reserved,  fac_kingdom_9,
[itm_common_pony,itm_briton_tunic12,itm_carbatinae_11qs,itm_byrnie4,itm_leather_gloves,itm_long_heavy_spear2,itm_tab_shield_round_11_nodevice,itm_briton_helm34,itm_axe_3,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x000000002a0c638c3aec92a6dca634a300000000001e3aa30000000000000000], 
  ["knight_9_7", "Guledic Hyfaidd map Bleddri", "Hyfaidd map Bleddri", tf_hero, 0, reserved,  fac_kingdom_9,
[itm_common_pony2,itm_briton_tunic11,itm_carbatinae_12qs,itm_byrnie6,itm_leather_gloves,itm_noble_sword_10,itm_tab_shield_round_08_nodevice,itm_briton_helm37,itm_knife2,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x000000003f0852132925ce54eb6d962300000000001d26650000000000000000], 
  ["knight_9_8", "Tiern Ffernfael ab Meurig", "Ffernfael ab Meurig", tf_hero, 0, reserved,  fac_kingdom_9,
[itm_common_pony2,itm_briton_tunic10,itm_carbatinae_13qs,itm_mail_shirt_10,itm_leather_gloves,itm_noble_swordv5,itm_tab_shield_round_05_device,itm_briton_helm36,itm_knife3,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x000000003f041506450476599495c52c00000000001dd7a40000000000000000], 
  ["knight_9_9", "Tiern Llofan map Cilmin Broetu", "Llofan map Cilmin Broetu", tf_hero, 0, reserved,  fac_kingdom_9,
[itm_common_pony,itm_briton_tunic8,itm_carbatinae_14qs,itm_mail_shirt_11,itm_leather_gloves,itm_long_heavy_spear1,itm_tab_shield_round_08_device,itm_briton_helm35,itm_axe_4,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x000000019504115c674d29b3512ca90c00000000000da4dd0000000000000000], 
 
  ["knight_10_1", "Mael Guledic", "Guledic", tf_hero, 0, reserved,  fac_kingdom_10,
[itm_common_horse2,itm_briton_tunic7,itm_carbatinae_11qs,itm_mail_shirt_10,itm_leather_gloves,itm_noble_swordv4,itm_tab_shield_round_10_device,itm_briton_helm33,itm_knife4,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000ee00c62093452b5a9336f9a9200000000001de71c0000000000000000], 

  ["knight_11_1", "Mael Rhun map Arthgal", "Rhun map Arthgal", tf_bajo|tf_hero, 0, reserved,  fac_kingdom_11,
[itm_common_horse,itm_briton_tunic8,itm_carbatinae_11qs,itm_mail_shirt_11,itm_leather_gloves,itm_noble_swordv3,itm_tab_shield_round_11_device,itm_briton_helm33,itm_knife4,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000f710c875334db7a6b5a79bb2200000000000dd9150000000000000000], 
  ["knight_11_2", "Mael Echou map Rhun",  "Echou map Rhun", tf_hero, 0, reserved,  fac_kingdom_11,
[itm_common_horse,itm_briton_tunic9,itm_carbatinae_14qs,itm_byrnie14,itm_leather_gloves,itm_noble_swordv3,itm_tab_shield_round_11_nodevice,itm_briton_helm34,itm_knife5,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x00000001a90523d338ab7238da46a2d100000000001ce69b0000000000000000], 
  ["knight_11_3", "Guledic Dyfnwal map Rhun", "Dyfnwal map Rhun", tf_hero, 0, reserved,  fac_kingdom_11,
[itm_common_pony2,itm_briton_tunic10,itm_carbatinae_13qs,itm_byrnie13,itm_leather_gloves,itm_noble_swordv,itm_tab_shield_round_06_nodevice,itm_briton_helm34,itm_knife5,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x000000083210300424a2cd57a379536a00000000001d48930000000000000000], 
  ["knight_11_4", "Guledic Giric Map Rath","Giric map Rath", tf_hero, 0, reserved,  fac_kingdom_11,
[itm_common_pony2,itm_briton_tunic11,itm_carbatinae_12qs,itm_byrnie6,itm_leather_gloves,itm_noble_swordv6,itm_tab_shield_round_08_device,itm_briton_helm33,itm_knife,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x000000003604058b4b4d91e35c8e492300000000001e456b0000000000000000], 
  ["knight_11_5", "Mael Cynon map Cyndrwyn", "Cynon map Cyndrwyn", tf_hero, 0, reserved,  fac_kingdom_11,
[itm_common_pony2,itm_briton_tunic12,itm_carbatinae_14qs,itm_byrnie4,itm_leather_gloves,itm_noble_swordv5,itm_tab_shield_round_05_device,itm_briton_helm35,itm_knife2,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x000000002d1010032cd269b62476bee300000000001ca8630000000000000000], 
  ["knight_11_6", "Mael Gwion map Cyndrwyn","Gwion map Cyndrwyn", tf_hero, 0, reserved,  fac_kingdom_11,
[itm_common_pony,itm_briton_tunic13,itm_carbatinae_13qs,itm_mail_shirt_13_3,itm_leather_gloves,itm_long_heavy_spear1,itm_tab_shield_round_11_device,itm_briton_helm35,itm_axe_3,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x00000000380834cd291295b51b64b70b00000000001e33960000000000000000], 
  ["knight_11_7", "Mael Madoc map Cadell","Madoc map Cadell", tf_hero, 0, reserved,  fac_kingdom_11,
[itm_common_pony,itm_briton_tunic7,itm_carbatinae_12qs,itm_mail_shirt_13_3,itm_leather_gloves,itm_noble_sword_12,itm_tab_shield_round_08_device,itm_briton_helm36,itm_knife4,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000], 
  ["knight_11_8", "Mael Caradoc map Riwall", "Caradoc map Riwall", tf_alto|tf_hero, 0, reserved,  fac_kingdom_11,
[itm_common_pony2,itm_briton_tunic6,itm_carbatinae_11qs,itm_byrnie3,itm_leather_gloves,itm_noble_sword_13,itm_tab_shield_round_05_nodevice,itm_briton_helm36,itm_knife5,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x000000003c04108f4565f5c69d76389c000000000005b50b0000000000000000], 

  ["knight_12_1", "Guledic Eliud map Eferferdyn", "Eliud map Eferferdyn", tf_hero, 0, reserved,  fac_kingdom_12,
[itm_common_horse2,itm_briton_tunic6,itm_carbatinae_11qs,itm_mail_shirt_10,itm_leather_gloves,itm_noble_swordv7,itm_tab_shield_round_11_nodevice,itm_briton_helm33,itm_knife2,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000b8d00240644ac323993d5c91b00000000001f3aad0000000000000000], 
  ["knight_12_2", "Guledic Alanorus map Eliud","Alanorus map Eliud", tf_bajo|tf_hero, 0, reserved,  fac_kingdom_12,
[itm_common_pony2,itm_briton_tunic7,itm_carbatinae_12qs,itm_byrnie4,itm_leather_gloves,itm_noble_swordv,itm_tab_shield_round_06_nodevice,itm_briton_helm34,itm_knife3,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x00000000200000113ada69b723ab553a00000000001e5b6c0000000000000000], 
  ["knight_12_3", "Mael Ricatus map Dunyart",  "Ricatus map Dunyart", tf_hero, 0, reserved,  fac_kingdom_12,
[itm_common_pony,itm_briton_tunic8,itm_carbatinae_13qs,itm_mail_shirt_13_3,itm_leather_gloves,itm_long_heavy_spear2,itm_tab_shield_round_08_nodevice,itm_briton_helm13,itm_axe_4,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x000000003b0c11ce55324dd4e270bd7400000000001e37250000000000000000], 

  ["knight_13_1", "Guledic Meurig map Arthfael", "Meurig map Arthfael", tf_hero, 0, reserved,  fac_kingdom_13,
[itm_common_horse,itm_briton_tunic9,itm_carbatinae_13qs,itm_mail_shirt_11,itm_leather_gloves,itm_noble_swordv4,itm_tab_shield_round_08_device,itm_briton_helm33,itm_knife5,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000f1d10140029588596dd31c71400000000001d529a0000000000000000], 
  ["knight_13_2", "Mael Owain map Hywel","Owain map Hywel", tf_alto|tf_hero, 0, reserved,  fac_kingdom_13,
[itm_common_pony,itm_briton_tunic10,itm_carbatinae_12qs,itm_byrnie6,itm_leather_gloves,itm_noble_swordv5,itm_tab_shield_round_11_nodevice,itm_briton_helm34,itm_knife4,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000024001146390b72479d69c6dc00000000001db7970000000000000000], 
  ["knight_13_3", "Tiern Brochwael map Meurig", "Brochwael map Meurig", tf_hero, 0, reserved,  fac_kingdom_13,
[itm_common_pony,itm_briton_tunic11,itm_carbatinae_11qs,itm_mail_shirt_5_1,itm_leather_gloves,itm_long_heavy_spear1,itm_tab_shield_round_11_device,itm_briton_helm33,itm_axe_4,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000ef00055883533d603a4323ca300000000000cb7290000000000000000], 
#  ["knight_13_4", "Mael Arthfael map Hywel", "Mael Arthfael map Hywel", tf_hero, 0, reserved,  fac_kingdom_13, [itm_arabian_horse_b,      itm_byrnie15,     itm_byrnie15,                 itm_carbatinae_4,              itm_carbatinae_11qs,                      itm_spangenhelm_22,  itm_leather_gloves,     itm_one_handed_war_axe_b,   itm_tab_shield_round_c],  knight_attrib_4,wp(240),knight_skills_4|knows_trainer_4, 0x0000000c350c418438ab85b75c61b8d300000000001d21530000000000000000, khergit_face_middle_2],
#  ["knight_13_5", "Tiern Ffernfael ab Meurig",  "Tiern Ffernfael ab Meurig", tf_hero, 0, reserved,  fac_kingdom_13, [itm_byrnie21,     itm_byrnie21,                 itm_carbatinae_4,              itm_carbatinae_11qs,                      itm_spangenhelm_22,  itm_leather_gloves,     itm_sword_6,   itm_tab_shield_round_c], knight_attrib_3,wp(240),knight_skills_3|knows_trainer_3, 0x0000000c280461004929b334ad632aa200000000001e05120000000000000000, khergit_face_old_2],

  ["knight_14_1", "Mael Cathalan mac Indrechtaig", "Cathalan mac Indrechtaig", tf_hero, 0, reserved,  fac_kingdom_14,
[itm_common_horse,itm_brat1,itm_gaelshoes_1,itm_byrnie11,itm_leather_gloves,itm_irish_long_sword1,itm_tab_shield_round_08_nodevice,itm_angle_helmet1,itm_knife2,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000c1500510528f50d52d20b152300000000001d66db0000000000000000],
  ["knight_14_2", "Mael Conallan mac Duin","Conallan mac Duin", tf_hero, 0, reserved,  fac_kingdom_14,
[itm_common_horse2,itm_brat2,itm_gaelshoes_3,itm_byrnie10,itm_leather_gloves,itm_irish_long_sword1,itm_tab_shield_round_10_nodevice,itm_noble_helm_smith,itm_knife3,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000fd208a253479c8e467a4628e900000000001dc4620000000000000000],
  ["knight_14_3", "Ard Tiarna Mocheirge mac Indrechtaig","Mocheirge mac Indrechtaig", tf_bajo|tf_hero, 0, reserved,  fac_kingdom_14,
[itm_common_pony,itm_briton_tunic24,itm_gaelshoes_3,itm_byrnie11,itm_leather_gloves,itm_irish_long_sword2,itm_tab_shield_round_08_device,itm_angle_helmet1,itm_knife4,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000c0810500347ae7acd0d3ad74a00000000001e289a0000000000000000],
  ["knight_14_4", "Tiarna Ainbith mac Aedo","Ainbith mac Aedo", tf_hero, 0, reserved,  fac_kingdom_14,
[itm_briton_tunic25,itm_gaelshoes_2,itm_byrnie12,itm_leather_gloves,itm_pictish_hatchet4,itm_tab_shield_round_05_device,itm_angle_helmet1,itm_knife4,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000e0d1091413aabada93c8ac95b00000000001d42e10000000000000000],
  ["knight_14_5", "Tiarna Cummascach mac Cathalan","Cummascach mac Cathalan", tf_hero, 0, reserved,  fac_kingdom_14,
[itm_common_pony2,itm_briton_tunic26,itm_gaelshoes_1,itm_mail_shirt_12_1,itm_leather_gloves,itm_long_heavy_spear1,itm_tab_shield_round_05_nodevice,itm_pictish_hatchet3,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x00000003ff08030436e13756f42dbae400000000001e672a0000000000000000],
 
  ["knight_15_1", "Ard Tiarna Ailill mac Dunlainge", "Ailill mac Dunlainge", tf_hero, 0, reserved,  fac_kingdom_15,
[itm_common_horse,itm_brat3,itm_gaelshoes_1,itm_byrnie12,itm_leather_gloves,itm_irish_long_sword2,itm_tab_shield_round_08_nodevice,itm_angle_helmet1,itm_knife3,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000b800803d348eb68a71b6956dc00000000001d399b0000000000000000],
  ["knight_15_2", "Ard Tiarna Cairpre mac Dunlainge", "Cairpre mac Dunlainge", tf_alto|tf_hero, 0, reserved,  fac_kingdom_15,
[itm_common_pony2,itm_brat4,itm_gaelshoes_3,itm_byrnie36,itm_leather_gloves,itm_irish_long_sword1,itm_tab_shield_round_11_nodevice,itm_noble_helm_smith,itm_knife3,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x000000089b0c305312cb39b6dec5869a00000000001ed9340000000000000000],
  ["knight_15_3", "Tiarna Muiredach mac Brain", "Muiredach mac Brain", tf_hero, 0, reserved,  fac_kingdom_15,
[itm_common_pony2,itm_brat1,itm_gaelshoes_3,itm_byrnie37,itm_leather_gloves,itm_irish_long_sword2,itm_tab_shield_round_10_nodevice,itm_angle_helmet1,itm_knife3,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000ff508330546dc4a59422d450c00000000001e51340000000000000000],
  ["knight_15_4", "Tiarna Domnall mac Muirecain", "Domnall mac Muirecain", tf_hero, 0, reserved,  fac_kingdom_15,
[itm_common_pony,itm_briton_tunic24,itm_gaelshoes_3,itm_byrnie38,itm_leather_gloves,itm_long_heavy_spear2,itm_tab_shield_round_06_device,itm_angle_helmet1,itm_pictish_hatchet12,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000ef204224c288986372a6d34d400000000001de8e30000000000000000],
  ["knight_15_5", "Tiarna Cerball mac Muirecain", "Cerball mac Muirecain", tf_hero, 0, reserved,  fac_kingdom_15,
[itm_common_pony,itm_briton_tunic25,itm_gaelshoes_2,itm_mail_shirt_12_3,itm_leather_gloves,itm_long_heavy_spear1,itm_tab_shield_round_08_device,itm_pictish_hatchet11,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4, 0x0000000752004814530c44941349a8b300000000001da6dd0000000000000000],
  ["knight_15_6", "Tiarna Augaire mac Ailella", "Augaire mac Ailella", tf_hero, 0, reserved,  fac_kingdom_15,
[itm_brat1,itm_gaelshoes_2,itm_mail_shirt_12_2,itm_leather_gloves,itm_pictish_hatchet,itm_tab_shield_round_06_device,itm_knife2,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x000000001310624b391a64b6e46d98e400000000001db6f60000000000000000],

  ["knight_16_1", "Ard Tiarna Dunchad mac Dub da Bairenn", "Dunchad mac Dub da Bairenn", tf_hero, 0, reserved,  fac_kingdom_16,
[itm_common_horse2,itm_brat2,itm_gaelshoes_2,itm_byrnie11,itm_leather_gloves,itm_irish_long_sword1,itm_tab_shield_round_11_device,itm_angle_helmet1,itm_knife2,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x000000088a08d25356d64946ec722c9c000000000012692c0000000000000000],
  ["knight_16_2", "Ard Tiarna Dub Lachtnai mac Gualu", "Dub Lachtnai mac Gualu", tf_bajo|tf_hero, 0, reserved,  fac_kingdom_16,
[itm_common_horse,itm_brat3,itm_gaelshoes_2,itm_byrnie36,itm_leather_gloves,itm_irish_long_sword1,itm_tab_shield_round_10_device,itm_noble_helm_smith,itm_knife2,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000fd010005236dd4de8e456c6a600000000001da0db0000000000000000],
  ["knight_16_3", "Tiarna Foghartach mac Suibhne", "Foghartach mac Suibhne", tf_hero, 0, reserved,  fac_kingdom_16,
[itm_common_pony2,itm_briton_tunic24,itm_gaelshoes_3,itm_byrnie37,itm_leather_gloves,itm_irish_long_sword2,itm_tab_shield_round_08_device,itm_noble_helm_smith,itm_knife3,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x00000005b00011813d9b6d4a92ada53500000000001cc1180000000000000000],
  ["knight_16_4", "Tiarna Longbortan mac Finnachta", "Longbortan mac Finnachta", tf_hero, 0, reserved,  fac_kingdom_16,
[itm_common_pony,itm_briton_tunic25,itm_gaelshoes_3,itm_byrnie38,itm_leather_gloves,itm_championsword1,itm_angle_helmet6,itm_knife3,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000762007910267265247671469100000000001d55240000000000000000],
  ["knight_16_5", "Tiarna Reachtabhra macBran Finn", "Reachtabhra macBran Finn", tf_hero, 0, reserved,  fac_kingdom_16,
[itm_common_pony2,itm_briton_tunic26,itm_gaelshoes_3,itm_mail_shirt_12_3,itm_leather_gloves,itm_long_heavy_spear1,itm_tab_shield_round_06_device,itm_pictish_hatchet12,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x00000006690002873d9b6d4a92ada53500000000001cc1180000000000000000],
  ["knight_16_6", "Tiarna Colman mac Cionaith", "Colman mac Cionaith", tf_alto|tf_hero, 0, reserved,  fac_kingdom_16,
[itm_common_pony,itm_briton_tunic27,itm_gaelshoes_3,itm_mail_shirt_12_4,itm_leather_gloves,itm_long_heavy_spear2,itm_tab_shield_round_08_nodevice,itm_pictish_hatchet14,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x000000003f0063834716b1472b46479e00000000001d41720000000000000000],

  ["knight_17_1", "Mael Conchobar mac Taidg Mor", "Conchobar mac Taidg Mor", tf_hero, 0, reserved,  fac_kingdom_17,
[itm_common_horse2,itm_brat1,itm_gaelshoes_1,itm_byrnie12,itm_leather_gloves,itm_irish_long_sword1,itm_tab_shield_round_08_nodevice,itm_noble_helm_smith,itm_knife2,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000ab90872001b1a76d51bb22ce600000000001e4b6b0000000000000000],
  ["knight_17_2", "Tiarna Aedh mac Conchobar", "Aedh mac Conchobar", tf_hero, 0, reserved,  fac_kingdom_17,
[itm_common_horse,itm_brat4,itm_gaelshoes_2,itm_byrnie11,itm_leather_gloves,itm_irish_long_sword1,itm_tab_shield_round_10_nodevice,itm_angle_helmet1,itm_knife3,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x00000003ef04620736c6a8e75a7aa6dd00000000001d96e60000000000000000],
  ["knight_17_3", "Tiarna Tadg mac Conchobar", "Tadg mac Conchobar", tf_hero, 0, reserved,  fac_kingdom_17,
[itm_common_pony2,itm_briton_tunic24,itm_gaelshoes_2,itm_byrnie12,itm_leather_gloves,itm_irish_long_sword2,itm_tab_shield_round_11_nodevice,itm_angle_helmet1,itm_knife3,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000c2c0844d42914d19b2369b4ea00000000001e331b0000000000000000],
  ["knight_17_4", "Tiarna Finshnechta mac Corcrai", "Finshnechta mac Corcrai", tf_hero, 0, reserved,  fac_kingdom_17,
[itm_common_pony2,itm_briton_tunic25,itm_gaelshoes_3,itm_byrnie36,itm_leather_gloves,itm_irish_long_sword2,itm_tab_shield_round_06_device,itm_noble_helm_smith,itm_knife3,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4, 0x0000000c3a0455c443d46e4c8b91291a00000000001ca51b0000000000000000],
  ["knight_17_5", "Tiarna Dobhailen mac Gormghus", "Dobhailen mac Gormghus", tf_alto|tf_hero, 0, reserved,  fac_kingdom_17,
[itm_briton_tunic27,itm_gaelshoes_3,itm_mail_shirt_12_1,itm_leather_gloves,itm_pictish_hatchet2,itm_tab_shield_round_08_device,itm_knife2,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000bbf001198371aa526a46caf1d00000000001e4b1e0000000000000000],
  ["knight_17_6", "Tiarna Cathal mac Conchobar", "Cathal mac Conchobar", tf_hero, 0, reserved,  fac_kingdom_17,
[itm_briton_tunic28,itm_gaelshoes_3,itm_mail_shirt_12_2,itm_leather_gloves,itm_pictish_hatchet,itm_tab_shield_round_11_device,itm_knife2,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000c130461054af448eb19cd40e400000000001d488a0000000000000000],

  ["knight_18_1", "Mael Domnall mac Aeda", "Domnall mac Aeda", tf_alto|tf_hero, 0, reserved,  fac_kingdom_18,
[itm_common_horse2,itm_brat1,itm_gaelshoes_3,itm_byrnie11,itm_leather_gloves,itm_irish_long_sword1,itm_tab_shield_round_08_nodevice,itm_noble_helm_smith,itm_knife4,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x00000000151004cc472249c89488d8cc000000000011cdb50000000000000000],
  ["knight_18_2", "Mael Dabaill", "Dabaill", tf_hero, 0, reserved,  fac_kingdom_18,
[itm_common_horse2,itm_brat2,itm_gaelshoes_2,itm_byrnie38,itm_leather_gloves,itm_irish_long_sword1,itm_tab_shield_round_11_nodevice,itm_angle_helmet1,itm_knife4,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x000000016410001843231663adc8d8e200000000001d469b0000000000000000],
  ["knight_18_3", "Mael Dub mac Aeda", "Dub mac Aeda", tf_hero, 0, reserved,  fac_kingdom_18,
[itm_common_pony,itm_briton_tunic24,itm_gaelshoes_1,itm_byrnie36,itm_leather_gloves,itm_irish_long_sword2,itm_tab_shield_round_10_nodevice,itm_angle_helmet1,itm_knife2,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x00000008b40110415d22d2b89d5aa4db00000000001e6c550000000000000000],
  ["knight_18_4", "Ruire Congalach mac Finnachta", "Congalach mac Finnachta", tf_hero, 0, reserved,  fac_kingdom_18,
[itm_common_pony2,itm_briton_tunic25,itm_gaelshoes_2,itm_byrnie37,itm_leather_gloves,itm_irish_long_sword2,itm_tab_shield_round_06_device,itm_noble_helm_smith,itm_knife3,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000000003189275b523689ac38e100000000001e39660000000000000000],
  ["knight_18_5", "Tiarna Cummascach mac Muiredaig", "Cummascach mac Muiredaig", tf_alto|tf_hero, 0, reserved,  fac_kingdom_18,
[itm_common_pony,itm_briton_tunic26,itm_gaelshoes_2,itm_byrnie7,itm_leather_gloves,itm_irish_long_sword2,itm_tab_shield_round_08_device,itm_noble_helm_smith,itm_knife3,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x000000003f1003d3491b761ae62dbd1b00000000001db6eb0000000000000000],
  ["knight_18_6", "Mael Padraig mac Curarada", "Padraig mac Curarada", tf_hero, 0, reserved,  fac_kingdom_18,
[itm_briton_tunic27,itm_gaelshoes_1,itm_mail_shirt_12_4,itm_leather_gloves,itm_pictish_hatchet4,itm_tab_shield_round_10_device,itm_knife2,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x00000008221023012b23774ccd72492400000000001f6b5c0000000000000000],
  ["knight_18_7", "Tiarna Laidhgnen mac Donnagain", "Laidhgnen mac Donnagain", tf_hero, 0, reserved,  fac_kingdom_18,
[itm_common_pony,itm_briton_tunic28,itm_gaelshoes_1,itm_mail_shirt_12_3,itm_leather_gloves,itm_irish_long_sword2,itm_tab_shield_round_11_device,itm_knife2,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x000000067810000443231663add158e400000000001dc69a0000000000000000],

  ["knight_19_1", "Mael Sechnaill mac Niall", "Sechnaill mac Niall", tf_hero, 0, reserved,  fac_kingdom_19,
[itm_common_horse,itm_brat3,itm_gaelshoes_3,itm_byrnie12,itm_leather_gloves,itm_irish_long_sword1,itm_tab_shield_round_06_device,itm_noble_helm_smith,itm_knife4,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x00000001ab0c02115d318e452d726b6300000000000dc96b0000000000000000],
  ["knight_19_2", "Mael Diarmait mac Etersceili", "Diarmait mac Etersceili", tf_hero, 0, reserved,  fac_kingdom_19,
[itm_common_pony2,itm_brat1,itm_gaelshoes_3,itm_byrnie36,itm_leather_gloves,itm_irish_long_sword1,itm_tab_shield_round_08_device,itm_angle_helmet1,itm_knife,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000a4e01419316a6b1e6527950e400000000001cb6a20000000000000000],
  ["knight_19_3", "Mael Flann Sinna mac Sechnaill", "Flann Sinna mac Sechnaill", tf_bajo|tf_hero, 0, reserved,  fac_kingdom_19,
[itm_common_pony,itm_briton_tunic24,itm_gaelshoes_1,itm_byrnie37,itm_leather_gloves,itm_championsword1,itm_angle_helmet5,itm_knife,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000f630052813b6bb36de5d6eb7400000000001dd72c0000000000000000],
  ["knight_19_4", "Tiarna Flann mac Conaing", "Flann mac Conaing", tf_hero, 0, reserved,  fac_kingdom_19,
[itm_briton_tunic25,itm_gaelshoes_3,itm_byrnie38,itm_leather_gloves,itm_pictish_hatchet,itm_tab_shield_round_08_device,itm_angle_helmet1,itm_knife2,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000a560971d52123a74b2224d36100000000001f39940000000000000000],
  ["knight_19_5", "Mael Conall mac Echach", "Conall mac Echach", tf_hero, 0, reserved,  fac_kingdom_19,
[itm_common_pony,itm_briton_tunic26,itm_gaelshoes_3,itm_mail_shirt_12_2,itm_leather_gloves,itm_long_heavy_spear2,itm_tab_shield_round_11_device,itm_pictish_hatchet15,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000],

  ["knight_20_1", "Mael Domnall dasachtach mac Causantin", "Domnall dasachtach mac Causantin", tf_hero, 0, reserved,  fac_kingdom_20,
[itm_common_horse,itm_picts_hoodtunic_03,itm_just_man_boots_dark,itm_mail_shirt_9,itm_leather_gloves,itm_irish_long_sword2,itm_tab_shield_round_10_device,itm_knife2,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000a7411820f491c8a271c4ae96300000000001e39240000000000000000],
  ["knight_20_2", "Ard Tiarna Aed mac Cinaeda", "Aed mac Cinaeda", tf_alto|tf_hero, 0, reserved,  fac_kingdom_20,
[itm_common_horse,itm_briton_tunic16,itm_just_man_boots_dark,itm_mail_shirt_8,itm_leather_gloves,itm_irish_long_sword2,itm_tab_shield_round_08_device,itm_angle_helmet1,itm_knife3,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000a74117448491c8a264c4aa76300000000001e38a40000000000000000],
  ["knight_20_3", "Tiarna Causantin mac Aeda", "Causantin mac Aeda", tf_hero, 0, reserved,  fac_kingdom_20,
[itm_common_pony,itm_briton_tunic17,itm_just_man_boots_dark,itm_mail_shirt_5,itm_leather_gloves,itm_irish_long_sword2,itm_tab_shield_round_08_nodevice,itm_noble_helm_smith,itm_knife3,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x000000040b04c2c624db4537239174cb00000000001c39730000000000000000],
  ["knight_20_4", "Tiarna Domhall mac Aeda", "Domhall mac Aeda", tf_hero, 0, reserved,  fac_kingdom_20,
[itm_common_pony2,itm_briton_tunic19,itm_just_man_boots_dark,itm_mail_shirt_6,itm_leather_gloves,itm_championsword1,itm_noble_helm_smith,itm_knife4,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000bb704c34755115dc8e0acb54d00000000001d69b30000000000000000],
  ["knight_20_5", "Mael Coluim mac Domnall", "Coluim mac Domnall", tf_hero, 0, reserved,  fac_kingdom_20,
[itm_wild_pony,itm_briton_tunic18,itm_just_man_boots_dark,itm_mail_shirt_7,itm_leather_gloves,itm_long_heavy_spear1,itm_tab_shield_round_10_nodevice,itm_angle_helmet1,itm_pictish_hatchet18,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000e9411051a051176aae165d4db00000000001ddb6b0000000000000000],
  ["knight_20_6", "Domlech", "Domlech", tf_alto|tf_hero, 0, reserved,  fac_kingdom_20,
[itm_picts_hoodtunic_18,itm_just_man_boots_dark,itm_mail_shirt_8,itm_leather_gloves,itm_pictish_hatchet4,itm_tab_shield_round_08_nodevice,itm_noble_helm_smith,itm_knife2,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x00000000140c018d136e59d6eb30b6eb00000000001ea51d0000000000000000],
  ["knight_20_7", "Entifidach", "Entifidach", tf_hero, 0, reserved,  fac_kingdom_20,
[itm_picts_hoodtunic_12,itm_just_man_boots_dark,itm_mail_shirt_9,itm_leather_gloves,itm_pictish_hatchet2,itm_tab_shield_round_10_nodevice,itm_knife2,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000e7f0c5107361c8a7bd6cdbbba00000000001edade0000000000000000],
  ["knight_20_8", "Lugthreni", "Lugthreni", tf_hero, 0, reserved,  fac_kingdom_20,
[itm_wild_pony2,itm_picts_hoodtunic_11,itm_just_man_boots_dark,itm_mail_shirt_5,itm_leather_gloves,itm_long_heavy_spear1,itm_tab_shield_round_11_nodevice,itm_pictish_hatchet17,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000aff001014351a7230d2826b1500000000001d89230000000000000000],
 
  ["knight_21_1", "Mael Diarmait mac Cerbaill", "Diarmait mac Cerbaill", tf_alto|tf_hero, 0, reserved,  fac_kingdom_21,
[itm_common_horse2,itm_brat3,itm_gaelshoes_1,itm_byrnie11,itm_leather_gloves,itm_irish_long_sword1,itm_tab_shield_round_08_nodevice,itm_noble_helm_smith,itm_knife4,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000ba50073043db37523b48dda6200000000001a46d40000000000000000],
  ["knight_21_2", "Mael Cellach mac Cerbaill", "Cellach mac Cerbaill", tf_hero, 0, reserved,  fac_kingdom_21,
[itm_common_pony,itm_briton_tunic27,itm_gaelshoes_2,itm_mail_shirt_13_3,itm_leather_gloves,itm_irish_long_sword2,itm_tab_shield_round_10_nodevice,itm_angle_helmet1,itm_knife3,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x00000009440c080852e6709a65aa28b900000000001d66dc0000000000000000],
  ["knight_21_3", "Ard Tiarna Riacan mac Dunlainge", "Riacan mac Dunlainge", tf_hero, 0, reserved,  fac_kingdom_21,
 [itm_common_pony2,itm_briton_tunic28,itm_gaelshoes_3,itm_mail_shirt_3,itm_leather_gloves,itm_long_heavy_spear2,itm_tab_shield_round_11_nodevice,itm_pictish_hatchet18,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x000000002a0c884d210e50c6d36b5d6300000000001d16b30000000000000000],
#########finaliza  LORDS  
  
##########pendiente modificar
###pretendientes#### danes
  ["kingdom_1_pretender",  "Jarl Thorgil",       "Thorgil",  tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_1,
 [itm_carbatinae_14qv,itm_byrnie26,itm_leather_gloves,itm_axe_10,itm_tab_shield_round_12_nodevice,itm_viking_elitehelm3,itm_javelin,itm_longseax4,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_7,0x0000000c471033c528ad2607670e01c500000000001e0c5a0000000000000000],
#claims pre-salic descent
#irish
  ["kingdom_2_pretender",  "Ard Tiarna Dungal", "Dungal",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_18,
 [itm_common_pony2,itm_celta_capa1,itm_gaelshoes_3,itm_byrnie,itm_leather_gloves,itm_long_heavy_spear2,itm_tab_shield_round_11_nodevice,itm_knife,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x00000004340c01841d89949529a6776a00000000001c910a0000000000000000, nord_face_young_2],
#had his patrimony falsified #northumbria
  ["kingdom_3_pretender",  "Aetheling Oswine",   "Oswine",  tf_bajo|tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_8,
 [itm_common_pony,itm_carbatinae_14qv,itm_mail_shirt,itm_leather_gloves,itm_heavy_spear1,itm_tab_shield_round_09_nodevice,itm_viking_elitehelm3,itm_javelin,itm_longseax2,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000b3c084547575e30a9293736a100000000001cd5130000000000000000],
#of the family #wessex
  ["kingdom_4_pretender",  "Aetheling Ceorl",  "Ceorl",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_5,
[itm_common_pony2,itm_hoodtunic_08,itm_carbatinae_12qs,itm_gambeson1,itm_leather_gloves,itm_noble_sword_2,itm_tab_shield_round_05_nodevice,itm_spangenhelm_15,itm_longseax6,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000d0d08324648ac6add25b1267300000000000711660000000000000000],
#dispossessed and wronged #alban
  ["kingdom_5_pretender",  "Tanist Bili",       "Bili",  tf_alto|tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_20,
[itm_brat1,itm_just_man_boots_dark,itm_byrnie3,itm_leather_gloves,itm_pictish_hatchet4,itm_tab_shield_round_08_nodevice,itm_angle_helmet6,itm_knife2,itm_javelin_skirmishes,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000324092353552375c4e14ec57300000000001c3b490000000000000000],
#republican #gwynedd
  ["kingdom_6_pretender",  "Mael Elisedd ap Cyngen",       "Elisedd ap Cyngen",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_9,
[itm_common_pony,itm_briton_tunic14,itm_carbatinae_11qs,itm_byrnie14,itm_leather_gloves,itm_long_heavy_spear1,itm_tab_shield_round_11_device,itm_briton_helm33,itm_knife5,itm_javelin,itm_trophy_b],
   lord_attrib,wp(380),knows_lord_1|knows_navigation_4,0x0000000324092353552375c4e14ec57300000000001c3b490000000000000000], 


#Royal family members

  ["knight_1_1_wife","Error - knight_1_1_wife should not appear in game","knight_1_1_wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_commoners, [itm_ptunic_4 ,   itm_veil_f,    itm_carbatinae_1],     def_attrib|level(2),wp(50),knows_common, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],

  ######ladies -  mothers, daughters, sisters
#mother ragnar's son
  ["kingdom_1_lady_1","Aslaug","Oslafa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,
   [    itm_elite_veil_1, itm_richwoman_norse1,      itm_womenshoes_2],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000ff1044007289d92aacb723b440000000000124b950000000000000000], #aslaug
#Sigurd snakes wife. Angla
  ["kingdom_1_lady_2","Blaeja","Blaeja",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,
   [    itm_elite_veil_2, itm_richwoman_norse2,      itm_womenshoes_1],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
#daughter of ragnar. Hermana Sigurd?
  ["kingdom_1_lady_3","Ragnhild Ragnarsdottir","Ragnhild Ragnarsdottir",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,
   [    itm_richwoman_norse3,      itm_womenshoes_1],  def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
#other
  ["kingdom_1_lady_4","Ingun","Ingun",tf_hero|tf_baja|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,
   [   itm_elite_veil_2, itm_richwoman_norse4,      itm_womenshoes_4],  def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000e6b08200534544a5ae132bce900000000001d369f0000000000000000],

#eirik daughter
  ["kingdom_2_lady_1","Gyda Eirikdottir","Gyda",tf_hero|tf_osa|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,
   [   itm_richwoman_norse1,      itm_womenshoes_4],  def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001841010191135e9935b66371300000000001e9ad40000000000000000],
#esposa ketil
  ["kingdom_2_lady_2","Yngvild","Yngvild",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,
   [    itm_elite_veil_4, itm_richwoman_norse4,      itm_womenshoes_3],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000004530000060512213341a24ace00000000001eef430000000000000000], 
#hija ketil
  ["kingdom_2_lady_3","Thorunn Ketilsdottir","Thorunn",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,
  [   itm_richwoman_norse3,      itm_womenshoes_2],      def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000018300300b27b5a2c843cdab0b00000000001f189b0000000000000000],
#guthrom's wife
  ["kingdom_2_lady_4","Hallbera","Hallbera",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,
   [    itm_elite_veil_1, itm_richwoman_norse2,      itm_womenshoes_2],      def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],

#laithling
  ["kingdom_3_lady_1","Salbjorg","Salbjorg",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,
   [    itm_elite_veil_2, itm_richwoman_norse3,      itm_womenshoes_1],      def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000e371040103ced9d44a3fa553a000000000004abdb0000000000000000],
  ["kingdom_3_lady_2","Bera","Bera",tf_hero|tf_baja|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,
   [    itm_elite_veil_4, itm_richwoman_norse2,      itm_womenshoes_1],      def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003f008004778a23d387447fff00000000001eab110000000000000000], 
  ["kingdom_3_lady_3","Grunnhild","Grunnhild",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,
   [  itm_richwoman_norse1,      itm_womenshoes_1],      def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000900500b36686c82d2794b0a00000000001dbb160000000000000000],
  ["kingdom_3_lady_4","Asgerd","Asgerd",tf_hero|tf_alta|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,
   [   itm_richwoman_norse4,      itm_womenshoes_1],      def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000010101544537a244dfa46ee000000000006378c0000000000000000],
#Frisa
  ["kingdom_4_lady_1","Helga","Helga",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,
  [    itm_elite_veil_1, itm_richwoman_norse2,      itm_womenshoes_3],      def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000004940c401639942d59ab5924ea00000000001e435c0000000000000000],
  ["kingdom_4_lady_2","Asfrid","Asfrid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,
   [    itm_elite_veil_4, itm_richwoman_norse3,      itm_womenshoes_3],      def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x0000000f090c300a34dcb642adb0d52800000000000dd38e0000000000000000],
  ["kingdom_4_lady_3","Ingibjorg","Ingibjorg",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,
  [    itm_richwoman_norse1,      itm_womenshoes_3],      def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000060c30124ae384350a8d475e00000000000ea6590000000000000000],
  ["kingdom_4_lady_4","Sacun","Sacun",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,
   [  itm_richwoman_norse4,      itm_womenshoes_3],      def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],

#aelfred mother born 849
  ["kingdom_5_lady_1","Osburh","Osburh",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,
   [     itm_common_veil_a,itm_queenwoman_saxon, itm_womenshoes_2],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000fff002011270e72430d59b7d300000000001da4d40000000000000000],
#Cuthred wife
  ["kingdom_5_lady_2","Wulfthryth","Wulfthryth",tf_hero|tf_alta|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,
   [   itm_common_veil_b,itm_woman_saxon2,   itm_womenshoes_2],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
#aelfred wife
  ["kingdom_5_lady_3","Ealswith","Ealswith",tf_hero|tf_baja|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,
   [   itm_common_veil_f, itm_richwoman_saxon5,  itm_womenshoes_1],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000002a50410093152c5c72355e95200000000001ee7110000000000000000],
#Aethelhelm wife
  ["kingdom_5_lady_4","Aelswith","Aelswith",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,
   [     itm_common_veil_c,itm_richwoman_saxon2,   itm_womenshoes_4],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000005d304400d112b50f54b9236f400000000001f38bb0000000000000000],
#Aethelhelm daughter
  ["kingdom_5_lady_5","Aelflaed","Aelflaed",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,
   [    itm_richwoman_saxon1,  itm_womenshoes_3],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
#others
  ["kingdom_5_lady_6","Eormengyth","Eormengyth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,
   [  itm_richwoman_saxon9,  itm_womenshoes_2],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003f08501243516756f19b472400000000001eb6e20000000000000000],
  ["kingdom_5_lady_7","Aelfwynne","Aelfwynne",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,
   [  itm_richwoman_saxon3, itm_womenshoes_1], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],

#Aelthelstan sister
  ["kingdom_6_lady_1","Edith","Edith",tf_hero|tf_baja|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,
   [    itm_common_veil_e,itm_richwoman_saxon1,itm_womenshoes_2], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007a7106006285d4e9963e7274c00000000001f44d80000000000000000],
#others
  ["kingdom_6_lady_2","Edburge","Edburge",tf_hero|tf_alta|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,
   [    itm_richwoman_saxon2,  itm_womenshoes_1],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000e1104000428db749e514c891900000000001db8d40000000000000000],
  ["kingdom_6_lady_3","Adelburga","Adelburga",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,
   [    itm_richwoman_saxon5,itm_womenshoes_4], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000005cd08401255d57ab6da88551300000000001f2ba00000000000000000],
  ["kingdom_6_lady_4","Hild","Hild",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,
   [    itm_richwoman_saxon6,  itm_womenshoes_4],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a1030133723bea0dd4e970800000000001f3b230000000000000000],

#king wife
  ["kingdom_7_lady_1","Aethelswith","Aethelswith",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,
   [    itm_common_veil_d,itm_richwoman_saxon7,  itm_womenshoes_3], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000f0710000d649c8ee4e5b0d32200000000001cb0ab0000000000000000],
#Aethelred mucel wife
  ["kingdom_7_lady_2","Eadburh","Eadburh",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,
   [   itm_common_veil_d,itm_richwoman_saxon8, itm_womenshoes_1], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000032500400b28b4cd42ced0349200000000001d27370000000000000000],
#Ceowulf wife
  ["kingdom_7_lady_3","Aedgyth","Aedgyth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,
   [   itm_common_veil_a,itm_richwoman_saxon9,  itm_womenshoes_2], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000015a0830164a957239b4d13c9000000000001d951b0000000000000000],
#others
  ["kingdom_7_lady_4","Cyneswith","Cyneswith",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,
   [   itm_common_veil_b,itm_richwoman_saxon9,  itm_womenshoes_4], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001471060025b2a65d965c6591000000000001d2aec0000000000000000],
  ["kingdom_7_lady_5","Alwith","Alwith",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,
   [   itm_common_veil_c,itm_richwoman_saxon5,  itm_womenshoes_3], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000004880c0015588b4e3975b1566300000000001d28a90000000000000000],
  ["kingdom_7_lady_6","Aedelfled","Aedelfled",tf_hero|tf_baja|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,
   [   itm_common_veil_d,itm_richwoman_saxon9,  itm_womenshoes_2], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057404400645323419598c549b00000000001ea95c0000000000000000],
  ["kingdom_7_lady_7","Aepelhilde","Aepelhilde",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,
   [   itm_common_veil_e,itm_richwoman_saxon3,  itm_womenshoes_1], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002708300c38cb3b9522d9a75d00000000001e371b0000000000000000],
  ["kingdom_7_lady_8","Aepelswip","Aepelswip",tf_hero|tf_alta|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,
   [   itm_richwoman_saxon1,  itm_womenshoes_8], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000a046008584c8d95186d38a400000000001ca79a0000000000000000],
  ["kingdom_7_lady_9","Aette","Aette",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,
   [ itm_richwoman_saxon2,  itm_womenshoes_8], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000910100738bd6c98accd9a92000000000009369a0000000000000000],

#daughter of Ragnar, sister of Harald or Ivar or other.
  ["kingdom_8_lady_1","Alof Ragnarsdottir","Alof",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,
   [   itm_richwoman_norse4,      itm_womenshoes_8],  def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
#Others non historical
  ["kingdom_8_lady_2","Eanflaed","Eanflaed",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,
   [    itm_common_veil_f,itm_richwoman_saxon3,      itm_womenshoes_4],  def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000003c910000c3762a9d6de9940aa00000000001c868b0000000000000000],
  ["kingdom_8_lady_3","Freydis","Freydis",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,
  [    itm_elite_veil_2, itm_richwoman_norse3,      itm_womenshoes_3],  def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000003c50040024693ceb71571e45b00000000001c48e40000000000000000],
  ["kingdom_8_lady_4","Gudrun","Gudrun",tf_hero|tf_osa|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,
   [    itm_elite_veil_1, itm_richwoman_norse1,      itm_womenshoes_2],  def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000025204400538d47242ab7248dc00000000001e271b0000000000000000],
  ["kingdom_8_lady_5","Sigrid","Sigrid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,
  [    itm_elite_veil_4, itm_richwoman_saxon9,      itm_womenshoes_1],  def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000010004600816e371494a2ed91300000000001542a20000000000000000],
  ["kingdom_8_lady_6","Svanhild","Svanhild",tf_hero|tf_baja|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,
   [    itm_elite_veil_1, itm_richwoman_norse4,      itm_womenshoes_4],  def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000012e04100720b38ddd0c45a0da00000000000ec90d0000000000000000],
  ["kingdom_8_lady_7","Sigrunn","Sigrunn",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,
   [  itm_richwoman_norse1,      itm_womenshoes_3],  def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000003015289d6d5b9e21c6a200000000001d26f30000000000000000],
  ["kingdom_8_lady_8","Turid","Turid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,
   [    itm_richwoman_norse3,      itm_womenshoes_2],  def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001c10000c4cb56dd68da9252100000000001f27120000000000000000],
  ["kingdom_8_lady_9","Aebbe","Aebbe",tf_hero|tf_alta|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,
  [    itm_richwoman_saxon7,     itm_womenshoes_1],  def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002b0c300a3af3b5b2dd39d94b0000000000161d1e0000000000000000],

#king wife Gwynedd
  ["kingdom_9_lady_1","Angharad verch Meurig","Angharad",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9,
   [  itm_elite_veil_1,itm_richwoman_saxon2,  itm_womenshoes_4], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
#16-17 years old in 868. King Daughter
  ["kingdom_9_lady_2","Elen verch Rhodri","Elen",tf_hero|tf_alta|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9,
   [  itm_richwoman_saxon3, itm_womenshoes_3],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
#king bastard daughter
  ["kingdom_9_lady_3","Creirwy","Creirwy",tf_hero|tf_baja|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9,
   [  itm_richwoman_saxon4,   itm_womenshoes_2],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000b0c4017459cca289d6f421a00000000001e1d110000000000000000],
#kings daughter
  ["kingdom_9_lady_4","Nest verch Rhodri","Nest",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9,
   [  itm_richwoman_saxon6, itm_womenshoes_8], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
#Others non historical
  ["kingdom_9_lady_5","Lleigy","Lleigy",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9,
   [    itm_elite_veil_2,itm_richwoman_saxon9,  itm_womenshoes_1], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000369005008535472b754a9c68c00000000001b37160000000000000000],
  ["kingdom_9_lady_6","Anna","Anna",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9,
   [   itm_elite_veil_3,itm_richwoman_saxon4,   itm_womenshoes_8],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000365044008229cc8cb518f289d00000000001e395c0000000000000000],

#brycheniog
  ["kingdom_10_lady_1","Marwenna","Marwenna",tf_hero|tf_alta|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10,
   [   itm_elite_veil_4,itm_richwoman_saxon4,  itm_womenshoes_2],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000006d60c4018585d89c8e58a46e100000000001dfad60000000000000000],
  ["kingdom_10_lady_2","Gwenonwy","Gwenonwy",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10,
   [  itm_elite_veil_3,itm_richwoman_saxon3, itm_womenshoes_1], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000002e20c30184b32b2c9236a394a00000000001d469c0000000000000000],
  ["kingdom_10_lady_3","Gweneddlon","Gweneddlon",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10,
   [    itm_richwoman_saxon2,   itm_womenshoes_8], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002600100427eaaddb5ab5c35b00000000001ec51d0000000000000000],

#rhun wife Alt clut
  ["kingdom_11_lady_1","Verh Cinaed","Verh Cinaed",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11,
   [  itm_elite_veil_1,itm_richwoman_saxon8,      itm_womenshoes_4],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000413045013052554b772d74d1b00000000001f3a4c0000000000000000],
#other non historical
  ["kingdom_11_lady_2","Brifael","Brifael",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11,
   [  itm_elite_veil_4,itm_richwoman_saxon7,        itm_womenshoes_3],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000004300000124a9dafa6dca95b2500000000000e41510000000000000000],
  ["kingdom_11_lady_3","Ceindrych","Ceindrych",tf_hero|tf_baja|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11,
   [  itm_elite_veil_3,itm_richwoman_saxon6,     itm_womenshoes_2],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001da0060106b6594349a4d476a00000000001e2b9b0000000000000000],
  ["kingdom_11_lady_4","Morgawse","Morgawse",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11,
   [  itm_richwoman_saxon2,      itm_womenshoes_8],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001290c300d59658ab84551c75b00000000001db99a0000000000000000],
#corniu
  ["kingdom_12_lady_1","Meisyr","Meisyr",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12,
   [   itm_elite_veil_4,itm_richwoman_saxon4,     itm_womenshoes_3],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
  ["kingdom_12_lady_2","Heledd","Heledd",tf_hero|tf_baja|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12,
   [   itm_elite_veil_3,itm_richwoman_saxon3,     itm_womenshoes_4], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000004c400000758a16736a94a430c00000000001cc6aa0000000000000000],
  ["kingdom_12_lady_3","Ffever","Ffever",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12,
   [    itm_elite_veil_2,itm_richwoman_saxon9, itm_womenshoes_1], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001770c500a46634a398be9192d00000000001e4a840000000000000000],
  ["kingdom_12_lady_4","Medlan","Medlan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12,
   [      itm_richwoman_saxon8,    itm_womenshoes_8],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001940c3006019c925165d1129b00000000001d13240000000000000000],
#glwyswing
  ["kingdom_13_lady_1","Rhiain Ceinfrid","Ceinfrid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_13,
   [    itm_elite_veil_1,itm_richwoman_saxon2,     itm_womenshoes_1],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001c00c100b672b56b4e1ad36eb00000000001ec9210000000000000000],
  ["kingdom_13_lady_2","Meddwyl","Meddwyl",tf_hero|tf_alta|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_13,
   [  itm_elite_veil_2,itm_richwoman_saxon3,    itm_womenshoes_2], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000019b083005389591941379b8d100000000001e63150000000000000000],
  ["kingdom_13_lady_3","Gwladus","Gwladus",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_13,
   [     itm_richwoman_saxon7, itm_womenshoes_8], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000004280800134b5cb82cad592b3100000000001dd6590000000000000000],

#ulaid
  ["kingdom_14_lady_1","Muireann","Muireann",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_14,
   [   itm_elite_veil_1,itm_queenpict_long_tunic,    itm_womenshoes_7],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000e1e0800073af7da3adc476ae300000000001d28a10000000000000000],
  ["kingdom_14_lady_2","Medb","Medb",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_14,
   [   itm_elite_veil_2,itm_pict_long_tunic2,  itm_womenshoes_8], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_14_lady_3","Creide","Creide",tf_hero|tf_alta|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_14,
   [ itm_elite_veil_3,itm_pict_long_tunic3,   itm_womenshoes_6], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_14_lady_4","Derbforgaill","Derbforgaill",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_14,
   [     itm_pict_long_tunic4,  itm_womenshoes_8],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
#Laigin
  ["kingdom_15_lady_1","Mhari","Mhari",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_15,
   [  itm_elite_veil_4,itm_queenpict_long_tunic,     itm_womenshoes_6],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000084c0c30071b5f4e272b6a389600000000001da4aa0000000000000000],
  ["kingdom_15_lady_2","Mall","Mall",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_15,
   [     itm_elite_veil_4,itm_pict_long_tunic6,    itm_womenshoes_6],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008e704501728f3ae471a8e976c00000000001dcd840000000000000000],
  ["kingdom_15_lady_3","Teglaig","Teglaig",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_15,
   [     itm_elite_veil_3,itm_pict_long_tunic5, itm_womenshoes_7], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000003bf006009631b28b95cd31c6900000000001d2ea20000000000000000],
  ["kingdom_15_lady_4","Lassa","Lassa",tf_hero|tf_baja|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_15,
   [   itm_pict_long_tunic4, itm_womenshoes_8], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
#mumain
  ["kingdom_16_lady_1","Cath","Cath",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_16,
   [    itm_elite_veil_3,itm_pict_long_tunic3,   itm_womenshoes_8],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056708000818e3ad5a5175d54e00000000001e53640000000000000000],
  ["kingdom_16_lady_2","Lassair","Lassair",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_16,
   [      itm_elite_veil_2,itm_pict_long_tunic2,     itm_womenshoes_8],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055304400924eb6536dace255d00000000001c932b0000000000000000],
  ["kingdom_16_lady_3","Duinseach","Duinseach",tf_hero|tf_alta|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_16,
   [     itm_elite_veil_1,itm_pict_long_tunic2,  itm_womenshoes_7], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000002b20c101549699098d649b69600000000001f25280000000000000000],
  ["kingdom_16_lady_4","Eva","Eva",tf_hero|tf_baja|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_16,
   [     itm_elite_veil_3,itm_pict_long_tunic3, itm_womenshoes_7], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001110100c28b567432c6d48ab00000000001ea8ea0000000000000000],
  ["kingdom_16_lady_5","Doirend","Doirend",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_16,
   [     itm_elite_veil_4,itm_pict_long_tunic4,   itm_womenshoes_6],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001c08301250666e286425c2d800000000001e98830000000000000000],
  ["kingdom_16_lady_6","Delbchaem","Delbchaem",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_16,
   [     itm_elite_veil_1,itm_pict_long_tunic5,    itm_womenshoes_6],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002b0c50131356732adace48ec00000000001f492c0000000000000000],
#connactha
  ["kingdom_17_lady_1","Caelfind","Caelfind",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_17,
   [    itm_elite_veil_4,itm_queenpict_long_tunic,     itm_womenshoes_7],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000006cc0020093d256a550970369100000000001cc8ee0000000000000000],
  ["kingdom_17_lady_2","Briana","Briana",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_17,
   [     itm_elite_veil_3,itm_pict_long_tunic5,    itm_womenshoes_7],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000111005018352dd2291472d34a00000000001eb4550000000000000000],
  ["kingdom_17_lady_3","Binne","Binne",tf_hero|tf_alta|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_17,
   [    itm_elite_veil_4,itm_pict_long_tunic4, itm_womenshoes_6], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007a404400438e3af30d969991e000000000016b51d0000000000000000],
  ["kingdom_17_lady_4","Aoibheann","Aoibheann",tf_hero|tf_baja|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_17,
   [   itm_elite_veil_4,itm_pict_long_tunic3,itm_womenshoes_6], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000006ad042002386dc9bb6969351c00000000001ea9930000000000000000],
  ["kingdom_17_lady_5","Aodhnait","Aodhnait",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_17,
   [   itm_elite_veil_3,itm_pict_long_tunic2,  itm_womenshoes_8],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001fd100009629dc2468e92414d00000000001e568c0000000000000000],
  ["kingdom_17_lady_6","Almu","Almu",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_17,
   [    itm_pict_long_tunic2, itm_womenshoes_8],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003000000a37574e30b3aa350c000000000010b86b0000000000000000],
#Aileach
  ["kingdom_18_lady_1","Fedelm","Fedelm",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_18,
   [   itm_elite_veil_2,itm_pict_long_tunic2,   itm_womenshoes_6],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000004270800096875eae8db4e3c2100000000001dd69d0000000000000000],
  ["kingdom_18_lady_2","Uaisle","Uaisle",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_18,
   [      itm_elite_veil_1,itm_pict_long_tunic6,   itm_womenshoes_8],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000068e104001429880e3a38954e300000000001de36b0000000000000000],
  ["kingdom_18_lady_3","Condadil","Condadil",tf_hero|tf_alta|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_18,
   [     itm_elite_veil_3,itm_pict_long_tunic5, itm_womenshoes_7], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000023810500d3b0c6b191e8dc92200000000001dd2420000000000000000],
  ["kingdom_18_lady_4","Flannesda","Flannesda",tf_hero|tf_baja|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_18,
   [     itm_elite_veil_4,itm_pict_long_tunic4, itm_womenshoes_8], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000022d0c3001246395c8d72dc61800000000001e1b720000000000000000],
  ["kingdom_18_lady_5","Mor","Mor",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_18,
   [     itm_pict_long_tunic3,   itm_womenshoes_6],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001a04601242f579b4e199b8d300000000001e370a0000000000000000],
  ["kingdom_18_lady_6","Aine","Aine",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_18,
   [   itm_pict_long_tunic2,   itm_womenshoes_8],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002f08601022b474590b32389d000000000015a35d0000000000000000],
#Meath
#king wife, born 842, third wife
  ["kingdom_19_lady_1","Muire ingen Cinaeda","Muire",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_19,
   [    itm_elite_veil_4,itm_queenpict_long_tunic,     itm_womenshoes_8],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000003b108400436ebb5b8d97162db00000000001e87db0000000000000000],
#flann sinna daughter
  ["kingdom_19_lady_2","Gormlaith","Gormlaith",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_19,
   [     itm_pict_long_tunic5,   itm_womenshoes_6],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003508501848a67655098eb91a00000000001f82560000000000000000],
#flann sinna wife
  ["kingdom_19_lady_3","Eithne","Eithne",tf_hero|tf_alta|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_19,
   [    itm_elite_veil_1,itm_pict_long_tunic4,  itm_womenshoes_8], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000002f20c00044614c66909513ae500000000001f2ab30000000000000000],
#other non historical
  ["kingdom_19_lady_4","Lann","Lann",tf_hero|tf_baja|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_19,
   [    itm_pict_long_tunic3,itm_womenshoes_8], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a04300c2ae46da4da6abca400000000001cc6ed0000000000000000],
  ["kingdom_19_lady_5","Etain","Etain",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_19,
   [     itm_pict_long_tunic4,  itm_womenshoes_7],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a04300b194a6da33c8d477000000000001ecb0d0000000000000000],
#alban
#domnall daughter
  ["kingdom_20_lady_1","Coluim","Coluim",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_20,
   [   itm_pict_long_tunic6, itm_womenshoes_8],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000d10300c409af1d6938ce53200000000001ac7a50000000000000000],
#kings wife
  ["kingdom_20_lady_2","Sabhdh Ingen Giric","Sabhdh Ingen Giric",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_20,
   [   itm_elite_veil_1,itm_pict_long_tunic2,    itm_womenshoes_7],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000005910040054acccd970b9e349100000000001df70c0000000000000000],
#others non historical
  ["kingdom_20_lady_3","Ingen Brude","Ingen Brude",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_20,
   [ itm_elite_veil_2,itm_pict_long_tunic2, itm_womenshoes_6], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000032f10100f0b2b663d538eeb1300000000000eab0e0000000000000000],
  ["kingdom_20_lady_4","Ingen Domlech","Ingen Domlech",tf_hero|tf_alta|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_20,
   [ itm_elite_veil_3,itm_pict_long_tunic3,itm_womenshoes_6], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_20_lady_5","Ingen Gwydd","Ingen Gwydd",tf_hero|tf_baja|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_20,
   [  itm_elite_veil_4,itm_pict_long_tunic4,     itm_womenshoes_6],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000327106015471ab25b0473370900000000001ca7210000000000000000],
  ["kingdom_20_lady_6","Bridei","Bridei",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_20,
   [   itm_pict_long_tunic6,itm_womenshoes_6],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002204501842a2b1264eb0a2a400000000001f46230000000000000000],
  ["kingdom_20_lady_7","Muire","Muire",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_20,
   [ itm_pict_long_tunic5,itm_womenshoes_6], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000280c6002052478b4db77339900000000001d436d0000000000000000],
#osrige
  ["kingdom_21_lady_1","Aideen","Aideen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_21,
   [    itm_elite_veil_4,itm_queenpict_long_tunic,itm_womenshoes_8], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000044c0c1002396571a91671caa400000000001fa0930000000000000000],
  ["kingdom_21_lady_2","Ethna","Ethna",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_21,
   [   itm_pict_long_tunic4,itm_womenshoes_8], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001d04601509eb8c45225066b100000000001ddd590000000000000000],
  
#  ["kingdom_11_lord_daughter","kingdom_11_lord_daughter","kingdom_11_lord_daughter",tf_hero|tf_female,0,reserved,fac_kingdom_10,  [ itm_lady_dress_blue ,   itm_phrygian12,    itm_just_man_boots_dark], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008300701c08d34a450ce43],
#  ["kingdom_13_lord_daughter","kingdom_13_lord_daughter","kingdom_13_lord_daughter",tf_hero|tf_female,0,reserved,fac_kingdom_10,  [ itm_lady_dress_green,   itm_phrygian11,   itm_just_man_boots_dark], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008000401db10a45b41d6d8],
##  ["kingdom_1_lady_a","kingdom_1_lady_a","kingdom_1_lady_a",tf_hero|tf_female,0,reserved,fac_kingdom_1, [   itm_lady_dress_blue ,   itm_phrygian12,    itm_carbatinae_1],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008500201d8ad93708e4694],
##  ["kingdom_1_lady_b","kingdom_1_lady_b","kingdom_1_lady_b",tf_hero|tf_female,0,reserved,fac_kingdom_1, [   itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_carbatinae_1],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000004000101c3ae68e0e944ac],
##  ["kingdom_2_lady_a","Kingdom 2 Lady a","Kingdom 2 Lady a",tf_hero|tf_female,0,reserved,fac_kingdom_2, [               itm_lady_dress_green,   itm_phrygian11,   itm_carbatinae_1],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008100501d8ad93708e4694],
##  ["kingdom_2_lady_b","Kingdom 2 Lady b","Kingdom 2 Lady b",tf_hero|tf_female,0,reserved,fac_kingdom_2, [               itm_lady_dress_blue ,   itm_phrygian12,    itm_carbatinae_1],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000004000401d8ad93708e4694],
##  ["kingdom_3_lady_a","Kingdom 3 Lady a","Kingdom 3 Lady a",tf_hero|tf_female,0,reserved,fac_kingdom_3, [               itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_carbatinae_1],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000010500301d8ad93708e4694],
##
##  ["kingdom_3_lady_b","Kingdom 3 Lady b","Kingdom 3 Lady b",tf_hero|tf_female,0,reserved,fac_kingdom_3,  [                         itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_carbatinae_1], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000000100601d8b08d76d14a24],
##  ["kingdom_4_lady_a","Kingdom 4 Lady a","Kingdom 4 Lady a",tf_hero|tf_female,0,reserved,fac_kingdom_4,  [                         itm_lady_dress_green,   itm_phrygian11,   itm_carbatinae_1], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000010500601d8ad93708e4694],
##  ["kingdom_4_lady_b","Kingdom 4 Lady b","Kingdom 4 Lady b",tf_hero|tf_female,0,reserved,fac_kingdom_4,  [                         itm_lady_dress_blue ,   itm_phrygian12,    itm_carbatinae_1], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008500201d8ad93708e4694],

  ["heroes_end", "{!}heroes end", "{!}heroes end", tf_hero, 0,reserved,  fac_neutral,[itm_common_horse,itm_btunic_16,itm_carbatinae_1],def_attrib|level(2),wp(20),knows_common, 0x000000000008318101f390c515555594],
#Merchants                                                                              AT                      SILAH                   ZIRH                        BOT                         Head_wear
##  ["merchant_1", "merchant_1_F", "merchant_1_F",tf_hero|tf_female,  0,0, fac_kingdom_1,[itm_courser,            itm_fighting_axe,       itm_btunic_16,         itm_carbatinae_1,          itm_veil_f],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008200201e54c137a940c91],
##  ["merchant_2", "merchant_2", "merchant_2", tf_hero,               0,0, fac_kingdom_2,[itm_common_horse,       itm_noble_sword_2,       itm_mail_shirt_6,          itm_carbatinae_vc4s,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000000000601db6db6db6db6db],
##  ["merchant_3", "merchant_3", "merchant_3", tf_hero,               0,0, fac_kingdom_3,[itm_courser,            itm_seax_1,       itm_btunic_16,         itm_carbatinae_vc4s,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008100701db6db6db6db6db],
##  ["merchant_4", "merchant_4_F", "merchant_4_F",tf_hero|tf_female,  0,0, fac_kingdom_4,[itm_common_horse,       itm_seax_1,           itm_mail_shirt_6,          itm_carbatinae_4,                              ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000010500401e54c137a945c91],
##  ["merchant_5", "merchant_5", "merchant_5", tf_hero,               0,0, fac_kingdom_5,[itm_common_horse,       itm_sword,              itm_long_tunic1,          itm_carbatinae_1,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008038001e54c135a945c91],
##  ["merchant_6", "merchant_6", "merchant_6", tf_hero,               0,0, fac_kingdom_1,[itm_common_horse,      itm_ragnar_seax,           itm_btunic_16,         itm_carbatinae_1,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000000248e01e54c1b5a945c91],
##  ["merchant_7", "merchant_7_F", "merchant_7_F",tf_hero|tf_female,  0,0, fac_kingdom_2,[itm_hunter,            itm_noble_sword_2,       itm_gambeson1,         itm_carbatinae_4,                              ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000004200601c98ad39c97557a],
##  ["merchant_8", "merchant_8", "merchant_8", tf_hero,               0,0, fac_kingdom_3,[itm_common_horse,      itm_seax_1,       itm_mail_shirt_6,          itm_carbatinae_1,          itm_btunic_15],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000001095ce01d6aad3a497557a],
##  ["merchant_9", "merchant_9", "merchant_9", tf_hero,               0,0, fac_kingdom_4,[itm_common_horse,      itm_sword,              itm_gambeson1,         itm_carbatinae_1,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000010519601ec26ae99898697],
##  ["merchant_10","merchant_10","merchant_10",tf_hero,               0,0, fac_merchants,[itm_hunter,             itm_bastard_sword,      itm_mail_shirt_6,          itm_carbatinae_vc4s,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000884c401f6837d3294e28a],
##  ["merchant_11","merchant_11","merchant_11",tf_hero,               0,0, fac_merchants,[itm_common_horse,       itm_sword,              itm_btunic_16,         itm_carbatinae_vc4s,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000c450501e289dd2c692694],
##  ["merchant_12","merchant_12","merchant_12",tf_hero,               0,0, fac_merchants,[itm_hunter,             itm_seax_1,           itm_btunic_16,         itm_carbatinae_1,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000c660a01e5af3cb2763401],
##  ["merchant_13","merchant_13","merchant_13",tf_hero,               0,0, fac_merchants,[itm_sumpter_horse,      itm_seax_1,       itm_gambeson1,         itm_carbatinae_1,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000001001d601ec912a89e4d534],
##  ["merchant_14","merchant_14","merchant_14",tf_hero,               0,0, fac_merchants,[itm_courser,            itm_bastard_sword,      itm_mail_shirt_6,          itm_carbatinae_1,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000004335601ea2c04a8b6a394],
##  ["merchant_15","merchant_15","merchant_15",tf_hero,               0,0, fac_merchants,[itm_common_horse,       itm_sword,              itm_gambeson1,         itm_carbatinae_vc4s,            itm_phrygian17],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008358e01dbf27b6436089d],
##  ["merchant_16","merchant_16_F","merchant_16_F",tf_hero|tf_female, 0,0, fac_merchants,[itm_hunter,             itm_bastard_sword,      itm_mail_shirt_6,          itm_carbatinae_1,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000c300101db0b9921494add],
##  ["merchant_17","merchant_17","merchant_17",tf_hero,               0,0, fac_merchants,[itm_common_horse,       itm_sword,              itm_btunic_16,         itm_carbatinae_4,                              ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008740f01e945c360976a0a],
##  ["merchant_18","merchant_18","merchant_18",tf_hero,               0,0, fac_merchants,[itm_common_horse,       itm_seax_1,       itm_gambeson1,         itm_carbatinae_1,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008020c01fc2db3b4c97685],
##  ["merchant_19","merchant_19","merchant_19",tf_hero,               0,0, fac_merchants,[itm_common_horse,       itm_seax_1,           itm_btunic_16,         itm_carbatinae_vc4s,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008118301f02af91892725b],
##  ["merchant_20","merchant_20_F","merchant_20_F",tf_hero|tf_female, 0,0, fac_merchants,[itm_courser,            itm_noble_sword_2,       itm_gambeson1,         itm_carbatinae_1,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000010500401f6837d27688212],
  
#Seneschals
### High title basic quest
  ["town_1_seneschal", "Norse Chronicler", "Chronicler", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_cloak,       itm_carbatinae_11qs], def_attrib|level(2),wp(20),knows_common, 0x00000009c00427c458abd2c894ea569500000000001e392b0000000000000000],
  ["town_2_seneschal", "Briton Chronicler", "Chronicler", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_gambeson1,     itm_carbatinae_5s],   def_attrib|level(2),wp(20),knows_common, 0x000000063f00600a36eb6d64d649d95300000000001e56d90000000000000000],
  ["town_3_seneschal", "Goidelic Chronicler", "Chronicler", tf_alto|tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_bl_tunic03,       itm_carbatinae_11qs], def_attrib|level(2),wp(20),knows_common, 0x0000000fe50820102aab8cd5ad6e497300000000001e38ab0000000000000000],
  ["town_4_seneschal", "Angle Chronicler", "Chronicler", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_cloak,      itm_carbatinae_2s],     def_attrib|level(2),wp(20),knows_common, 0x0000000fd4109311387311c31c8e54db00000000001dac910000000000000000],
###
  ["town_5_seneschal", "{!}Town 5 Seneschal", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_btunic_16,     itm_carbatinae_5s],   def_attrib|level(2),wp(20),knows_common, man_face_younger_2, man_face_older_2],
  ["town_6_seneschal", "{!}Town 6 Seneschal", "{!}Town 6 Seneschal", tf_bajo|tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_gambeson41,       itm_carbatinae_1],   def_attrib|level(2),wp(20),knows_common, man_face_younger_2, man_face_older_2],
  ["town_7_seneschal", "{!}Town 7 Seneschal", "{!}Town7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_btunic_16,     itm_carbatinae_5s],   def_attrib|level(2),wp(20),knows_common, man_face_younger_2, man_face_older_2],
  ["town_8_seneschal", "{!}Town 8 Seneschal", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_gambeson41,       itm_carbatinae_1],   def_attrib|level(2),wp(20),knows_common, man_face_younger_2, man_face_older_2],
  ["town_9_seneschal", "{!}Town 9 Seneschal", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_bl_tunic02,       itm_carbatinae_11qs], def_attrib|level(2),wp(20),knows_common, man_face_younger_2, man_face_older_2],
  ["town_10_seneschal", "{!}Town 10 Seneschal", "{!}Town 10 Seneschal", tf_alto|tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_btunic_16,     itm_carbatinae_2s],     def_attrib|level(2),wp(20),knows_common, man_face_younger_2, man_face_older_2],
  ["town_11_seneschal", "{!}Town 11 Seneschal", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_gambeson41,     itm_carbatinae_1],   def_attrib|level(2),wp(20),knows_common, man_face_younger_2, man_face_older_2],
  ["town_12_seneschal", "{!}Town 12 Seneschal", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_cloak,       itm_carbatinae_11qs], def_attrib|level(2),wp(20),knows_common, man_face_younger_2, man_face_older_2],
  ["town_13_seneschal", "{!}Town 13 Seneschal", "{!}Town 13 Seneschal", tf_bajo|tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_long_tunic1,     itm_carbatinae_5s],   def_attrib|level(2),wp(20),knows_common, man_face_younger_2, man_face_older_2],
  ["town_14_seneschal", "{!}Town 14 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_long_tunic1,      itm_carbatinae_2s],     def_attrib|level(2),wp(20),knows_common, man_face_younger_2, man_face_older_2],
  ["town_15_seneschal", "{!}Town 15 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_long_tunic1,      itm_carbatinae_2s],     def_attrib|level(2),wp(20),knows_common, man_face_younger_2, man_face_older_2],
  ["town_16_seneschal", "{!}Town 16 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_gambeson41,      itm_carbatinae_2s],     def_attrib|level(2),wp(20),knows_common, man_face_younger_2, man_face_older_2],
  ["town_17_seneschal", "{!}Town 17 Seneschal", "{!}Town 14 Seneschal", tf_alto|tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_gambeson41,      itm_carbatinae_2s],     def_attrib|level(2),wp(20),knows_common, man_face_younger_2, man_face_older_2],
  ["town_18_seneschal", "{!}Town 18 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_gambeson41,      itm_carbatinae_2s],     def_attrib|level(2),wp(20),knows_common, man_face_younger_2, man_face_older_2],
  ["town_19_seneschal", "{!}Town 19 Seneschal", "{!}Town 14 Seneschal", tf_bajo|tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_gambeson41,      itm_carbatinae_2s],     def_attrib|level(2),wp(20),knows_common, man_face_younger_2, man_face_older_2],
  ["town_20_seneschal", "{!}Town 20 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_gambeson41,      itm_carbatinae_2s],     def_attrib|level(2),wp(20),knows_common, man_face_younger_2, man_face_older_2],
  ["town_21_seneschal", "{!}Town 21 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_gambeson41,      itm_carbatinae_2s],     def_attrib|level(2),wp(20),knows_common, man_face_younger_2, man_face_older_2],
  ["town_22_seneschal", "{!}Town 22 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_cloak,      itm_carbatinae_2s],     def_attrib|level(2),wp(20),knows_common, man_face_younger_2, man_face_older_2],
  ["town_23_seneschal", "{!}Town 23 Seneschal", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_bl_tunic04,       itm_carbatinae_11qs], def_attrib|level(2),wp(20),knows_common, man_face_younger_2, man_face_older_2],
  ["town_24_seneschal", "{!}Town 24 Seneschal", "{!}Town 4 Seneschal", tf_alto|tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_gambeson41,      itm_carbatinae_2s],     def_attrib|level(2),wp(20),knows_common, man_face_younger_2, man_face_older_2],
###Add-ons quest
  ["town_25_seneschal", "Mael Bresail", "{!}Mael Bresail", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_spatha, itm_small_roundsh4,     itm_byrnie8,     itm_carbatinae_5s],   def_attrib|level(2),wp(20),knows_common, man_face_younger_2, man_face_older_2],
###
  ["town_26_seneschal", "{!}Town 26 Seneschal", "{!}Town 6 Seneschal", tf_bajo|tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_gambeson41,       itm_carbatinae_1],   def_attrib|level(2),wp(20),knows_common, man_face_younger_2, man_face_older_2],
  ["town_27_seneschal", "{!}Town 27 Seneschal", "{!}Town 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_btunic_16,     itm_carbatinae_5s],   def_attrib|level(2),wp(20),knows_common, man_face_younger_2, man_face_older_2],
  ["town_28_seneschal", "{!}Town 28 Seneschal", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_gambeson41,       itm_carbatinae_1],   def_attrib|level(2),wp(20),knows_common, man_face_younger_2, man_face_older_2],
  ["town_29_seneschal", "{!}Town 29 Seneschal", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_bl_tunic05,       itm_carbatinae_11qs], def_attrib|level(2),wp(20),knows_common, man_face_younger_2, man_face_older_2],

  ["castle_1_seneschal", "Fort Reeve", "{!}Fort 1 Seneschal", tf_bajo|tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson10,itm_longseax10,itm_carbatinae_1],    def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_2_seneschal", "Fort Reeve", "{!}Fort 2 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson11,itm_longseax1,itm_carbatinae_5s],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_3_seneschal", "Fort Reeve", "{!}Fort 3 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson12, itm_longseax4,itm_carbatinae_11qs], def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_4_seneschal", "Fort Reeve", "{!}Fort 4 Seneschal", tf_alto|tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson13,itm_longseax1,itm_carbatinae_5s],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_5_seneschal", "Fort Reeve", "{!}Fort 5 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson14,itm_longseax3,itm_carbatinae_1],    def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_6_seneschal", "Fort Reeve", "{!}Fort 6 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson15,itm_longseax10,itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_7_seneschal", "Fort Reeve", "{!}Fort 7 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson16,itm_longseax6,itm_carbatinae_2s],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_8_seneschal", "Fort Reeve", "{!}Fort 8 Seneschal", tf_bajo|tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson17,itm_longseax6,itm_carbatinae_1],    def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_9_seneschal", "Fort Reeve", "{!}Fort 9 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson18,itm_longseax10,itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_10_seneschal", "Fort Reeve", "{!}Fort 10 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson19,itm_longseax1,itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_11_seneschal", "Fort Reeve", "{!}Fort 11 Seneschal", tf_alto|tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson20,itm_longseax1,itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_12_seneschal", "Fort Reeve", "{!}Fort 2 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson21,itm_longseax1,itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_13_seneschal", "Fort Reeve", "{!}Fort 3 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson22,itm_longseax3,itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_14_seneschal", "Fort Reeve", "{!}Fort 4 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson23,itm_longseax4,itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_15_seneschal", "Fort Reeve", "{!}Fort 5 Seneschal", tf_bajo|tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson24,itm_longseax2,itm_carbatinae_1],    def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_16_seneschal", "Fort Reeve", "{!}Fort 6 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson1,itm_longseax6,itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_17_seneschal", "Fort Reeve", "{!}Fort 7 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson2,itm_longseax7,itm_carbatinae_4],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_18_seneschal", "Fort Reeve", "{!}Fort 8 Seneschal", tf_alto|tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson3,itm_longseax9,itm_carbatinae_1],    def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_19_seneschal", "Fort Reeve", "{!}Fort 9 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson32,itm_longseax1,itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_20_seneschal", "Fort Reeve", "{!}Fort 20 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson5,itm_longseax1,itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_21_seneschal", "Fort Reeve", "{!}Fort 11 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson6,itm_longseax1,itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_22_seneschal", "Fort Reeve", "{!}Fort 2 Seneschal", tf_bajo|tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson7,itm_longseax1,itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_23_seneschal", "Fort Reeve", "{!}Fort 3 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson8,itm_longseax1,itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_24_seneschal", "Fort Reeve", "{!}Fort 4 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson9,itm_longseax1,itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_25_seneschal", "Fort Reeve", "{!}Fort 5 Seneschal", tf_alto|tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson10,itm_longseax1,itm_carbatinae_1],    def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_26_seneschal", "Fort Reeve", "{!}Fort 6 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson11,itm_longseax1,itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_27_seneschal", "Fort Reeve", "{!}Fort 7 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson12,itm_longseax1,itm_carbatinae_4],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_28_seneschal", "Fort Reeve", "{!}Fort 8 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson13,itm_longseax10,itm_carbatinae_1],    def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_29_seneschal", "Fort Reeve", "{!}Fort 9 Seneschal", tf_bajo|tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson14,itm_longseax8,itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_30_seneschal", "Fort Reeve", "{!}Fort 20 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson15,itm_longseax6,itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_31_seneschal", "Fort Reeve", "{!}Fort 11 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson16,itm_longseax9,itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_32_seneschal", "Fort Reeve", "{!}Fort 2 Seneschal", tf_alto|tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson17,itm_longseax1,itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_33_seneschal", "Fort Reeve", "{!}Fort 3 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson18,itm_longseax5,itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_34_seneschal", "Fort Reeve", "{!}Fort 4 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson19,itm_longseax4,itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_35_seneschal", "Fort Reeve", "{!}Fort 5 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson20,itm_longseax1,itm_carbatinae_1],    def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_36_seneschal", "Fort Reeve", "{!}Fort 6 Seneschal", tf_bajo|tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson21,itm_longseax4,itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_37_seneschal", "Fort Reeve", "{!}Fort 7 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson22,itm_longseax1,itm_carbatinae_4],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_38_seneschal", "Fort Reeve", "{!}Fort 8 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson23,itm_longseax2,itm_carbatinae_1],    def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_39_seneschal", "Fort Reeve", "{!}Fort 9 Seneschal", tf_alto|tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson24,itm_longseax1,itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_40_seneschal", "Fort Reeve", "{!}Fort 20 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson1,itm_longseax3,itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_41_seneschal", "Fort Reeve", "{!}Fort 20 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson2,itm_longseax6,itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_42_seneschal", "Fort Reeve", "{!}Fort 20 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson3,itm_longseax9,itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_43_seneschal", "Fort Reeve", "{!}Fort 20 Seneschal", tf_bajo|tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson4,itm_longseax9,itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_44_seneschal", "Fort Reeve", "{!}Fort 20 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson5,itm_longseax10,itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_45_seneschal", "Fort Reeve", "{!}Fort 20 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson6,itm_longseax2,itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_46_seneschal", "Fort Reeve", "{!}Fort 20 Seneschal", tf_alto|tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson7,itm_longseax1,itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_47_seneschal", "Fort Reeve", "{!}Fort 20 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson8,itm_longseax5,itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_48_seneschal", "Fort Reeve", "{!}Fort 20 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson9,itm_longseax1,itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_49_seneschal", "Fort Reeve", "{!}Fort 9 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson10,itm_longseax1,itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_50_seneschal", "Fort Reeve", "{!}Fort 20 Seneschal", tf_bajo|tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson11,itm_longseax1,itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_51_seneschal", "Fort Reeve", "{!}Fort 11 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson12,itm_longseax1,itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_52_seneschal", "Fort Reeve", "{!}Fort 2 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson13, itm_longseax1,itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_53_seneschal", "Fort Reeve", "{!}Fort 3 Seneschal", tf_alto|tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson14,itm_longseax1, itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_54_seneschal", "Fort Reeve", "{!}Fort 4 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson15,itm_longseax5,itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_55_seneschal", "Fort Reeve", "{!}Fort 5 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson16,itm_longseax3,itm_carbatinae_1],    def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_56_seneschal", "Fort Reeve", "{!}Fort 6 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson17,itm_longseax5,itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_57_seneschal", "Fort Reeve", "{!}Fort 7 Seneschal", tf_bajo|tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson18,itm_longseax4,itm_carbatinae_4],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_58_seneschal", "Fort Reeve", "{!}Fort 8 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson19,itm_longseax5,itm_carbatinae_1],    def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_59_seneschal", "Fort Reeve", "{!}Fort 9 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson20,itm_longseax2,itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_60_seneschal", "Fort Reeve", "{!}Fort 20 Seneschal", tf_alto|tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson21,itm_longseax1,itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_61_seneschal", "Fort Reeve", "{!}Fort 11 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson22,itm_longseax1,itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_62_seneschal", "Fort Reeve", "{!}Fort 2 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson23,itm_longseax10,itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_63_seneschal", "Fort Reeve", "{!}Fort 3 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson24,itm_longseax4,itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_64_seneschal", "Fort Reeve", "{!}Fort 4 Seneschal", tf_bajo|tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson24,itm_longseax5,itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_65_seneschal", "Fort Reeve", "{!}Fort 5 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson23,itm_longseax5,itm_carbatinae_1],    def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_66_seneschal", "Fort Reeve", "{!}Fort 6 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson22,itm_longseax1,itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_67_seneschal", "Fort Reeve", "{!}Fort 7 Seneschal", tf_alto|tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson21,itm_longseax1,itm_carbatinae_4],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_68_seneschal", "Fort Reeve", "{!}Fort 8 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson20,itm_longseax2,itm_carbatinae_1],    def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_69_seneschal", "Fort Reeve", "{!}Fort 9 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson19,itm_longseax3,itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_70_seneschal", "Fort Reeve", "{!}Fort 20 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson18,itm_longseax8,itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_71_seneschal", "Fort Reeve", "{!}Fort 11 Seneschal", tf_bajo|tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson17,itm_longseax1,itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_72_seneschal", "Fort Reeve", "{!}Fort 2 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson16,itm_longseax3,itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_73_seneschal", "Fort Reeve", "{!}Fort 3 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson15,itm_longseax4,itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_74_seneschal", "Fort Reeve", "{!}Fort 4 Seneschal", tf_alto|tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson14,itm_longseax7,itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_75_seneschal", "Fort Reeve", "{!}Fort 5 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson13,itm_longseax6,itm_carbatinae_1],    def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_76_seneschal", "Fort Reeve", "{!}Fort 6 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson12,itm_longseax10,itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_77_seneschal", "Fort Reeve", "{!}Fort 7 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson11,itm_longseax3,itm_carbatinae_4],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_78_seneschal", "Fort Reeve", "{!}Fort 8 Seneschal", tf_bajo|tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson10,itm_longseax7,itm_carbatinae_1],    def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_79_seneschal", "Fort Reeve", "{!}Fort 9 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson1,itm_longseax8,itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_80_seneschal", "Fort Reeve", "{!}Fort 20 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson2,itm_longseax9,itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_81_seneschal", "Fort Reeve", "{!}Fort 11 Seneschal", tf_alto|tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson3,itm_longseax1,itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_82_seneschal", "Fort Reeve", "{!}Fort 2 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson32,itm_longseax5,itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_83_seneschal", "Fort Reeve", "{!}Fort 3 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson5, itm_longseax7,itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_84_seneschal", "Fort Reeve", "{!}Fort 4 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson6,itm_longseax6,itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_85_seneschal", "Fort Reeve", "{!}Fort 5 Seneschal", tf_bajo|tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson7,itm_longseax1,itm_carbatinae_1],    def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_86_seneschal", "Fort Reeve", "{!}Fort 6 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson8,itm_longseax4,itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_87_seneschal", "Fort Reeve", "{!}Fort 7 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson9,itm_longseax10,itm_carbatinae_4],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_88_seneschal", "Fort Reeve", "{!}Fort 8 Seneschal", tf_alto|tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson10,itm_longseax1,itm_carbatinae_1],    def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_89_seneschal", "Fort Reeve", "{!}Fort 9 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson11,itm_longseax2,itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_90_seneschal", "Fort Reeve", "{!}Fort 20 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson12,itm_longseax4,itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],
  ["castle_91_seneschal", "Fort Reeve", "{!}Fort 11 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson13,itm_longseax3,itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, mercenary_face_1, man_face_older_2],

#Arena Masters
  ["town_1_arena_master", "Competition Master","{!}Competition Master",tf_hero|tf_randomize_face, scn_town_1_arena|entry(52),reserved,   fac_commoners,[itm_btunic_1,      itm_carbatinae_1],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_2_arena_master", "Competition Master","{!}Competition Master",tf_alto|tf_hero|tf_randomize_face, scn_town_2_arena|entry(52),reserved,   fac_commoners,[itm_btunic_2,       itm_carbatinae_1],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_3_arena_master", "Competition Master","{!}Competition Master",tf_hero|tf_randomize_face, scn_town_3_arena|entry(52),reserved,   fac_commoners,[itm_btunic_3,       itm_carbatinae_1],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_4_arena_master", "Competition Master","{!}Competition Master",tf_hero|tf_randomize_face, scn_town_4_arena|entry(52),reserved,   fac_commoners,[itm_btunic_4,      itm_carbatinae_1],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_5_arena_master", "Competition Master","{!}Competition Master",tf_bajo|tf_hero|tf_randomize_face, scn_town_5_arena|entry(52),reserved,   fac_commoners,[itm_btunic_5,       itm_carbatinae_1],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_6_arena_master", "Competition Master","{!}Competition Master",tf_hero|tf_randomize_face, scn_town_6_arena|entry(52),reserved,   fac_commoners,[itm_btunic_1,    itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_7_arena_master", "Competition Master","{!}Competition Master",tf_hero|tf_randomize_face, scn_town_7_arena|entry(52),reserved,   fac_commoners,[itm_btunic_2,    itm_carbatinae_1],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_8_arena_master", "Competition Master","{!}Competition Master",tf_hero|tf_randomize_face, scn_town_8_arena|entry(52),reserved,   fac_commoners,[itm_btunic_3,       itm_carbatinae_1],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_9_arena_master", "Competition Master","{!}Competition Master",tf_alto|tf_hero|tf_randomize_face, scn_town_9_arena|entry(52),reserved,   fac_commoners,[itm_btunic_4,    itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_10_arena_master","Competition Master","{!}Competition Master",tf_hero|tf_randomize_face, scn_town_10_arena|entry(52),reserved,  fac_commoners,[itm_btunic_5,       itm_carbatinae_1],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_11_arena_master","Competition Master","{!}Competition Master",tf_hero|tf_randomize_face, scn_town_11_arena|entry(52),reserved,  fac_commoners,[itm_btunic_1,      itm_carbatinae_1],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_12_arena_master","Competition Master","{!}Competition Master",tf_bajo|tf_hero|tf_randomize_face, scn_town_12_arena|entry(52),reserved,  fac_commoners,[itm_btunic_2,    itm_carbatinae_1],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_13_arena_master","Competition Master","{!}Competition Master",tf_hero|tf_randomize_face, scn_town_13_arena|entry(52),reserved,  fac_commoners,[itm_btunic_3,      itm_carbatinae_1],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_14_arena_master","Competition Master","{!}Competition Master",tf_hero|tf_randomize_face, scn_town_14_arena|entry(52),reserved,  fac_commoners,[itm_btunic_4,    itm_carbatinae_1],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_15_arena_master","Competition Master","{!}Competition Master",tf_hero|tf_randomize_face, scn_town_15_arena|entry(52),reserved,  fac_commoners,[itm_btunic_5,    itm_carbatinae_1],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_16_arena_master","Competition Master","{!}Competition Master",tf_alto|tf_hero|tf_randomize_face, scn_town_16_arena|entry(52),reserved,  fac_commoners,[itm_btunic_1,    itm_carbatinae_1],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_17_arena_master","Competition Master","{!}Competition Master",tf_hero|tf_randomize_face, scn_town_17_arena|entry(52),reserved,  fac_commoners,[itm_btunic_2,    itm_carbatinae_1],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_18_arena_master","Competition Master","{!}Competition Master",tf_hero|tf_randomize_face, scn_town_18_arena|entry(52),reserved,  fac_commoners,[itm_btunic_3,    itm_carbatinae_1],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_19_arena_master","Competition Master","{!}Competition Master",tf_bajo|tf_hero|tf_randomize_face, scn_town_19_arena|entry(52),reserved,  fac_commoners,[itm_btunic_4,    itm_carbatinae_1],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_20_arena_master","Competition Master","{!}Competition Master",tf_hero|tf_randomize_face, scn_town_20_arena|entry(52),reserved,  fac_commoners,[itm_btunic_5,    itm_carbatinae_1],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_21_arena_master","Competition Master","{!}Competition Master",tf_hero|tf_randomize_face, scn_town_21_arena|entry(52),reserved,  fac_commoners,[itm_btunic_1,    itm_carbatinae_1],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_22_arena_master","Competition Master","{!}Competition Master",tf_hero|tf_randomize_face, scn_town_22_arena|entry(52),reserved,  fac_commoners,[itm_btunic_2,    itm_carbatinae_1],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_23_arena_master", "Competition Master","{!}Competition Master",tf_alto|tf_hero|tf_randomize_face, scn_town_23_arena|entry(52),reserved,   fac_commoners,[itm_btunic_3,       itm_carbatinae_1],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_24_arena_master", "Competition Master","{!}Competition Master",tf_hero|tf_randomize_face, scn_town_24_arena|entry(52),reserved,   fac_commoners,[itm_btunic_4,      itm_carbatinae_1],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_25_arena_master", "Competition Master","{!}Competition Master",tf_hero|tf_randomize_face, scn_town_25_arena|entry(52),reserved,   fac_commoners,[itm_btunic_5,       itm_carbatinae_1],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_26_arena_master", "Competition Master","{!}Competition Master",tf_bajo|tf_hero|tf_randomize_face, scn_town_26_arena|entry(52),reserved,   fac_commoners,[itm_btunic_2,    itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_27_arena_master", "Competition Master","{!}Competition Master",tf_hero|tf_randomize_face, scn_town_27_arena|entry(52),reserved,   fac_commoners,[itm_btunic_4,    itm_carbatinae_1],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_28_arena_master", "Competition Master","{!}Competition Master",tf_hero|tf_randomize_face, scn_town_28_arena|entry(52),reserved,   fac_commoners,[itm_btunic_3,       itm_carbatinae_1],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_29_arena_master", "Competition Master","{!}Competition Master",tf_hero|tf_randomize_face, scn_town_29_arena|entry(52),reserved,   fac_commoners,[itm_btunic_1,    itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],


# Underground 

##  ["town_1_crook","Town 1 Crook","Town 1 Crook",tf_hero,                0,0, fac_neutral,[itm_linen_tunic,        itm_carbatinae_1       ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x000000000004428401f46e44a27144e3],
##  ["town_2_crook","Town 2 Crook","Town 2 Crook",tf_hero|tf_female,      0,0, fac_neutral,[itm_lady_dress_ruby,    itm_turret_hat_ruby     ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x000000000004300101c36db6db6db6db],
##  ["town_3_crook","Town 3 Crook","Town 3 Crook",tf_hero,                0,0, fac_neutral,[itm_bl_tunic02,      itm_carbatinae_1          ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000000000c530701f17944a25164e1],
##  ["town_4_crook","Town 4 Crook","Town 4 Crook",tf_hero,                0,0, fac_neutral,[itm_bl_tunic01,       itm_carbatinae_1          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c840501f36db6db7134db],
##  ["town_5_crook","Town 5 Crook","Town 5 Crook",tf_hero,                0,0, fac_neutral,[itm_gambeson2,       itm_carbatinae_4           ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c000601f36db6db7134db],
##  ["town_6_crook","Town 6 Crook","Town 6 Crook",tf_hero,                0,0, fac_neutral,[itm_bl_tunic01,       itm_carbatinae_1          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c10c801db6db6dd7598aa],
##  ["town_7_crook","Town 7 Crook","Town 7 Crook",tf_hero|tf_female,      0,0, fac_neutral,[itm_lady_dress_ruby,       itm_btunic_15         ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000010214101de2f64db6db58d],
##  
##  ["town_8_crook","Town 8 Crook","Town 8 Crook",tf_hero,                0,0, fac_neutral,[itm_btunic_16,     itm_carbatinae_1       ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000010318401c96db4db6db58d],
##  ["town_9_crook","Town 9 Crook","Town 9 Crook",tf_hero,                0,0, fac_neutral,[itm_linen_tunic,        itm_carbatinae_1          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008520501f16db4db6db58d],
##  ["town_10_crook","Town 10 Crook","Town 10 Crook",tf_hero,             0,0, fac_neutral,[itm_bl_tunic01,      itm_carbatinae_1         ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008600701f35144db6db8a2],
##  ["town_11_crook","Town 11 Crook","Town 11 Crook",tf_hero|tf_female,   0,0, fac_neutral,[itm_peasant_dress_b_new,        itm_wimple_with_veil    ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008408101f386c4db4dd514],
##  ["town_12_crook","Town 12 Crook","Town 12 Crook",tf_hero,             0,0, fac_neutral,[itm_bl_tunic01,      itm_carbatinae_1          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000870c501f386c4f34dbaa1],
##  ["town_13_crook","Town 13 Crook","Town 13 Crook",tf_hero,             0,0, fac_neutral,[itm_gambeson2,     itm_carbatinae_1         ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c114901f245caf34dbaa1],
##  ["town_14_crook","Town 14 Crook","Town 14 Crook",tf_hero|tf_female,   0,0, fac_neutral,[itm_itm_common_horse,      itm_turret_hat_ruby     ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000001021c001f545a49b6eb2bc],

# Armor Merchants
  #arena_masters_end = zendar_armorer

  ["town_1_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_02,           itm_carbatinae_1   ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_2_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_01,          itm_veil_f       ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_3_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_02,        itm_carbatinae_1      ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_4_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|tf_alto|  tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_03,         itm_carbatinae_1   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_5_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|tf_bajo|  tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_04,          itm_carbatinae_1     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_6_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_05,       itm_carbatinae_1     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_7_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_06,       itm_carbatinae_4       ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_8_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_07,       itm_carbatinae_1   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_9_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_08,        itm_carbatinae_1     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_10_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_07,       itm_carbatinae_1      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_11_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_06,        itm_carbatinae_1   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_12_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_05,         itm_carbatinae_1     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_13_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_04,       itm_carbatinae_1      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_14_armorer","Eadwine the Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_alto|  tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_03],def_attrib|level(5),wp(20),knows_inventory_management_10,mercenary_face_1, mercenary_face_2],
  ["town_15_armorer","Donnchadh the Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|  tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_02,        itm_carbatinae_1   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_16_armorer","Paega the Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_bajo|  tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_01,         itm_carbatinae_1     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_17_armorer","Lifris the Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|   tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_02,       itm_carbatinae_1      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_18_armorer","Fearchair the Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|  tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_03],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_19_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_04,        itm_carbatinae_1   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_20_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_05,         itm_carbatinae_1     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_21_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_alto|  tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_06,       itm_carbatinae_1      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_22_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_07],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_23_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|         tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_01,        itm_carbatinae_1      ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_24_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|tf_bajo| tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_02,         itm_carbatinae_1   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_25_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|         tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_03,          itm_carbatinae_1     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_26_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|         tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_04,       itm_carbatinae_1     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_27_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|tf_alto| tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_05,       itm_carbatinae_4       ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_28_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|tf_bajo| tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_06,       itm_carbatinae_1   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_29_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|         tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_07,        itm_carbatinae_1     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
#player lair armorer
  ["town_30_armorer","Ingleri", "{!}Armorer",  tf_hero|                            tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_08,        itm_carbatinae_1   ],def_attrib|level(26),wp(20),knows_inventory_management_10, 0x000000033f0c1281478b74ca9a6ecd5c00000000001d39120000000000000000],

# Weapon merchants

  ["town_1_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_01,      itm_carbatinae_1,itm_veil_f],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_2_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_alto|  tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_02,     itm_carbatinae_1],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_3_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_03,   itm_carbatinae_1],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_4_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_bajo|  tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_04,            itm_carbatinae_1],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_5_weaponsmith", "Atli the Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_05,   itm_carbatinae_vc4s],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_6_weaponsmith", "Harenbili the Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_06,      itm_carbatinae_1],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_7_weaponsmith", "Egil the Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|     tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_07,            itm_carbatinae_1],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_8_weaponsmith", "Godgyfu the Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|  tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_08,     itm_carbatinae_vc4s],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_9_weaponsmith", "Uormuin the Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|  tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_01,   itm_carbatinae_1],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_10_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_bajo|      tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_02,     itm_carbatinae_1],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_11_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|              tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_03,  itm_carbatinae_vc4s],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_12_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_alto|      tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_04,           itm_carbatinae_1],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_13_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|              tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_05,     itm_carbatinae_vc4s],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_14_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|              tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_06,     itm_carbatinae_vc4s],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_15_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_osa|       tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_07,  itm_carbatinae_vc4s],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_16_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|              tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_08,           itm_carbatinae_1],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_17_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|              tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_01,     itm_carbatinae_vc4s],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_18_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_bajo|      tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_02,     itm_carbatinae_vc4s],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_19_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|              tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_03,  itm_carbatinae_2],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_20_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|              tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_04,           itm_carbatinae_2],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_21_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|              tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_05,     itm_carbatinae_2],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_22_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_baja|      tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_06,     itm_carbatinae_2],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_23_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|             tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_07,   itm_carbatinae_1],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_24_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|             tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_08,            itm_carbatinae_1],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_25_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_alto|     tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_01,   itm_carbatinae_vc4s],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_26_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|             tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_02,      itm_carbatinae_1],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_27_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|             tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_03,            itm_carbatinae_1],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_28_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|             tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_04,     itm_carbatinae_vc4s],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_29_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|             tf_is_merchant, 0, 0, fac_commoners,[itm_hoodtunic_05,   itm_carbatinae_1],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
#player lair
  ["town_30_weaponsmith","Ulfberht","{!}Weaponsmith",tf_hero|tf_is_merchant, 0, 0, fac_commoners,[itm_btunic_16,  itm_carbatinae_vc4s],def_attrib|level(26),wp(20),knows_inventory_management_10, 0x0000000fec045184475aa2a4c9bc48a800000000001dca250000000000000000],
###followers
  ["town_31_weaponsmith","Weland","{!}Weaponsmith",tf_hero|tf_is_merchant, 0, 0, fac_commoners,[itm_btunic_16,  itm_carbatinae_vc4s],def_attrib|level(26),wp(20),knows_inventory_management_10, 0x0000000fec045184475aa2a4c9bc48a800000000001dca250000000000000000],

#Tavern keepers

  ["town_1_tavernkeeper", "Host","{!}Host",tf_hero|tf_randomize_face,           scn_town_1_tavern|entry(9),0,   fac_commoners,[itm_hoodtunic_01,       itm_carbatinae_vc4s],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_2_tavernkeeper", "Host","{!}Host",tf_hero|tf_randomize_face|tf_alto,   scn_town_2_tavern|entry(9),0,   fac_commoners,[itm_hoodtunic_02,       itm_carbatinae_1],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_3_tavernkeeper", "Host","{!}Host",tf_hero|tf_randomize_face|tf_female, scn_town_3_tavern|entry(9),0,   fac_commoners,[itm_woman_saxon1,        itm_carbatinae_1],def_attrib|level(2),wp(20),knows_common, woman_face_younger_1, woman_face_older_2],
  ["town_4_tavernkeeper", "Host","{!}Host",tf_hero|tf_randomize_face,           scn_town_4_tavern|entry(9),0,   fac_commoners,[itm_hoodtunic_01,       itm_carbatinae_1],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_5_tavernkeeper", "Host","{!}Host",tf_hero|tf_randomize_face,   scn_town_5_tavern|entry(9),0,   fac_commoners,[itm_leather_cloak,       itm_carbatinae_1],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_6_tavernkeeper", "Host","{!}Host",tf_hero|tf_randomize_face|tf_alta,   scn_town_6_tavern|entry(9),0,   fac_commoners,[itm_woman_saxon2,        itm_carbatinae_1],def_attrib|level(2),wp(20),knows_common, woman_face_younger_1, woman_face_older_2],
  ["town_7_tavernkeeper", "Host","{!}Host",tf_hero|tf_randomize_face|tf_female,   scn_town_7_tavern|entry(9),0,   fac_commoners,[itm_woman_saxon3,        itm_carbatinae_1,      itm_veil_f],def_attrib|level(2),wp(20),knows_common, woman_face_younger_1, woman_face_older_2],
  ["town_8_tavernkeeper", "Host","{!}Host",tf_hero|tf_randomize_face|tf_bajo,    scn_town_8_tavern|entry(9),0,   fac_commoners,[itm_leather_cloak,      itm_carbatinae_1],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_9_tavernkeeper", "Host","{!}Host",tf_hero|tf_randomize_face|tf_female,    scn_town_9_tavern|entry(9),0,   fac_commoners,[itm_woman_saxon4,        itm_carbatinae_1],def_attrib|level(2),wp(20),knows_common, woman_face_younger_1, woman_face_older_2],
  ["town_10_tavernkeeper","Host","{!}Host",tf_hero|tf_randomize_face|tf_female, scn_town_10_tavern|entry(9),0,  fac_commoners,[itm_woman_saxon5,        itm_carbatinae_1],def_attrib|level(2),wp(20),knows_common,woman_face_younger_1, woman_face_older_2],
  ["town_11_tavernkeeper","Host","{!}Host",tf_hero|tf_randomize_face|tf_female,   scn_town_11_tavern|entry(9),0,  fac_commoners,[itm_woman_saxon2,        itm_carbatinae_1],def_attrib|level(2),wp(20),knows_common, woman_face_younger_1, woman_face_older_2],
  ["town_12_tavernkeeper","Host","{!}Host",tf_hero|tf_randomize_face,           scn_town_12_tavern|entry(9),0,  fac_commoners,[itm_hoodtunic_04,       itm_carbatinae_1],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_13_tavernkeeper","Host","{!}Host",tf_hero|tf_randomize_face|tf_baja,   scn_town_13_tavern|entry(9),0,  fac_commoners,[itm_woman_saxon3,        itm_carbatinae_1,     itm_veil_f],def_attrib|level(2),wp(20),knows_common, woman_face_younger_1, woman_face_older_2],
  ["town_14_tavernkeeper","Host","{!}Host",tf_hero|tf_randomize_face,   scn_town_14_tavern|entry(9),0,  fac_commoners,[itm_hoodtunic_05,               itm_carbatinae_1],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_15_tavernkeeper","Host","{!}Host",tf_hero|tf_randomize_face|tf_female,    scn_town_15_tavern|entry(9),0,  fac_commoners,[itm_woman_saxon4,        itm_carbatinae_1],def_attrib|level(2),wp(20),knows_common,woman_face_younger_1, woman_face_older_2],
  ["town_16_tavernkeeper","Host","{!}Host",tf_hero|tf_randomize_face,           scn_town_16_tavern|entry(9),0,  fac_commoners,[itm_hoodtunic_06,       itm_carbatinae_1],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_17_tavernkeeper","Host","{!}Host",tf_hero|tf_randomize_face|tf_female, scn_town_17_tavern|entry(9),0,  fac_commoners,[itm_woman_saxon5,        itm_carbatinae_1,     itm_veil_f],def_attrib|level(2),wp(20),knows_common, woman_face_younger_1, woman_face_older_2],
  ["town_18_tavernkeeper","Host","{!}Host",tf_hero|tf_randomize_face|tf_bajo,   scn_town_18_tavern|entry(9),0,  fac_commoners,[itm_gael_tunic_01,               itm_carbatinae_1],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_19_tavernkeeper","Host","{!}Host",tf_hero|tf_randomize_face|tf_female,   scn_town_19_tavern|entry(9),0,  fac_commoners,[itm_gaeltunic_1woman,        itm_carbatinae_2],def_attrib|level(2),wp(20),knows_common,woman_face_younger_1, woman_face_older_2],
  ["town_20_tavernkeeper","Host","{!}Host",tf_hero|tf_randomize_face|tf_alto,    scn_town_20_tavern|entry(9),0,  fac_commoners,[itm_gael_tunic_03,       itm_carbatinae_2],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_21_tavernkeeper","Host","{!}Host",tf_hero|tf_randomize_face|tf_female,   scn_town_21_tavern|entry(9),0,  fac_commoners,[itm_pict_long_tunic1,        itm_carbatinae_2,     itm_veil_f],def_attrib|level(2),wp(20),knows_common, woman_face_younger_1, woman_face_older_2],
  ["town_22_tavernkeeper","Host","{!}Host",tf_hero|tf_randomize_face,           scn_town_22_tavern|entry(9),0,  fac_commoners,[itm_hoodtunic_07,               itm_carbatinae_2],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_23_tavernkeeper", "Host","{!}Host",tf_hero|tf_randomize_face|tf_baja,    scn_town_23_tavern|entry(9),0,   fac_commoners,[itm_yellow2_cloak,        itm_carbatinae_1],def_attrib|level(2),wp(20),knows_common, woman_face_younger_1, woman_face_older_2],
  ["town_24_tavernkeeper", "Host","{!}Host",tf_hero|tf_randomize_face,   scn_town_24_tavern|entry(9),0,   fac_commoners,[itm_gael_tunic_04,       itm_carbatinae_1],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_25_tavernkeeper", "Host","{!}Host",tf_hero|tf_randomize_face,           scn_town_25_tavern|entry(9),0,   fac_commoners,[itm_gael_tunic_05,       itm_carbatinae_1],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_26_tavernkeeper", "Host","{!}Host",tf_hero|tf_randomize_face|tf_female, scn_town_26_tavern|entry(9),0,   fac_commoners,[itm_woman_saxon5,        itm_carbatinae_1],def_attrib|level(2),wp(20),knows_common, woman_face_younger_1, woman_face_older_2],
  ["town_27_tavernkeeper", "Host","{!}Host",tf_hero|tf_randomize_face|tf_female,   scn_town_27_tavern|entry(9),0,   fac_commoners,[itm_yellow2_cloak,        itm_carbatinae_1,      itm_veil_f],def_attrib|level(2),wp(20),knows_common, woman_face_younger_1, woman_face_older_2],

  ["town_28_tavernkeeper", "Host","{!}Host",tf_hero|tf_randomize_face|tf_bajo,   scn_town_28_tavern|entry(9),0,   fac_commoners,[itm_gael_tunic_06,      itm_carbatinae_1],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_29_tavernkeeper", "Host","{!}Host",tf_hero|tf_randomize_face|tf_female,   scn_town_29_tavern|entry(9),0,   fac_commoners,[itm_pict_long_tunic4,        itm_carbatinae_1],def_attrib|level(2),wp(20),knows_common, woman_face_younger_1, woman_face_older_2],
#player lair
  ["town_30_tavernkeeper","Casius","{!}Host",tf_hero|tf_bajo, 0,0,  fac_commoners,[itm_hoodtunic_02,        itm_carbatinae_1],def_attrib|level(2),wp(20),knows_common, 0x0000000ff91071443a5d4e491a136b0d00000000001e99140000000000000000],

#Goods Merchants

  ["town_1_merchant", "Merchant","{!}Merchant",tf_alto  |tf_hero|tf_randomize_face|tf_is_merchant, scn_town_1_store|entry(9),0, fac_commoners,     [itm_hoodtunic_01,  itm_carbatinae_1                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_middle_2, man_face_older_2],
  ["town_2_merchant", "Merchant","{!}Merchant",tf_hero|tf_randomize_face|tf_is_merchant, scn_town_2_store|entry(9),0, fac_commoners,     [itm_hoodtunic_02, itm_carbatinae_1                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_3_merchant", "Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_3_store|entry(9),0, fac_commoners,     [itm_woman_norse1,         itm_carbatinae_1,  itm_veil_f   ],def_attrib|level(2),wp(20),knows_inventory_management_10,woman_face_younger_1, woman_face_older_2],
  ["town_4_merchant", "Merchant","{!}Merchant",tf_hero|tf_randomize_face|tf_is_merchant, scn_town_4_store|entry(9),0, fac_commoners,     [itm_hoodtunic_04, itm_carbatinae_1                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_5_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_5_store|entry(9),0, fac_commoners,     [itm_hoodtunic_05,   itm_carbatinae_1                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_middle_2, man_face_older_2],
  ["town_6_merchant", "Merchant","{!}Merchant",tf_alta  |tf_hero|tf_randomize_face|tf_is_merchant, scn_town_6_store|entry(9),0, fac_commoners,     [itm_woman_norse2,  itm_carbatinae_1                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_younger_1, woman_face_older_2],
  ["town_7_merchant", "Hogni","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_7_store|entry(9),0, fac_commoners,     [itm_hoodtunic_06,itm_carbatinae_1                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_8_merchant", "Merchant","{!}Merchant",tf_hero|tf_randomize_face|tf_is_merchant, scn_town_8_store|entry(9),0, fac_commoners,     [itm_hoodtunic_07, itm_carbatinae_1                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_9_merchant", "Merchant","{!}Merchant",tf_bajo  |tf_hero|tf_randomize_face|tf_is_merchant, scn_town_9_store|entry(9),0, fac_commoners,     [itm_hoodtunic_08, itm_carbatinae_1                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_middle_2, man_face_older_2],
  ["town_10_merchant","Merchant","{!}Merchant",tf_hero|tf_randomize_face|tf_is_merchant, scn_town_10_store|entry(9),0, fac_commoners,    [itm_hoodtunic_01,itm_carbatinae_1                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_11_merchant","Adda","{!}Merchant",tf_female|tf_hero|tf_is_merchant, scn_town_11_store|entry(9),0, fac_commoners,    [itm_woman_saxon7,         itm_carbatinae_1],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x000000062f0000123cf589c9a325666600000000001d56db0000000000000000],
  ["town_12_merchant","Merchant","{!}Merchant",tf_female  |tf_hero|tf_randomize_face|tf_is_merchant, scn_town_12_store|entry(9),0, fac_commoners,    [itm_woman_norse4,  itm_carbatinae_1 ],def_attrib|level(2),wp(20),knows_inventory_management_10,woman_face_younger_1, woman_face_older_2],
  ["town_13_merchant","Merchant","{!}Merchant",tf_alta   |tf_hero|tf_randomize_face|tf_is_merchant, scn_town_13_store|entry(9),0, fac_commoners,    [itm_woman_norse3,         itm_carbatinae_1,  itm_veil_f   ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_younger_1, woman_face_older_2],
  ["town_14_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_14_store|entry(9),0, fac_commoners,    [itm_hoodtunic_04, itm_carbatinae_1                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_15_merchant","Merchant","{!}Merchant",tf_hero|tf_randomize_face|tf_is_merchant, scn_town_15_store|entry(9),0, fac_commoners,    [itm_hoodtunic_05, itm_carbatinae_1                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_middle_2, man_face_older_2],
  ["town_16_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_16_store|entry(9),0, fac_commoners,    [itm_woman_norse1,  itm_carbatinae_1 ],def_attrib|level(2),wp(20),knows_inventory_management_10,woman_face_younger_1, woman_face_older_2],
  ["town_17_merchant","Merchant","{!}Merchant",tf_female  |tf_hero|tf_randomize_face|tf_is_merchant, scn_town_17_store|entry(9),0, fac_commoners,    [itm_woman_norse2,         itm_carbatinae_1,  itm_veil_f   ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_younger_1, woman_face_older_2],
  ["town_18_merchant","Merchant","{!}Merchant",tf_bajo  |tf_hero|tf_randomize_face|tf_is_merchant, scn_town_18_store|entry(9),0, fac_commoners,    [itm_hoodtunic_07, itm_carbatinae_1                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_19_merchant","Merchant","{!}Merchant",tf_hero|tf_randomize_face|tf_is_merchant, scn_town_19_store|entry(9),0, fac_commoners,    [itm_hoodtunic_08, itm_carbatinae_1                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_20_merchant","Merchant","{!}Merchant",tf_baja  |tf_hero|tf_randomize_face|tf_is_merchant, scn_town_20_store|entry(9),0, fac_commoners,    [itm_woman_norse3,  itm_carbatinae_2],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_21_merchant","Merchant","{!}Merchant",tf_female   |tf_hero|tf_randomize_face|tf_is_merchant, scn_town_21_store|entry(9),0, fac_commoners,    [itm_woman_norse4,         itm_carbatinae_2],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_younger_1, woman_face_older_2],
  ["town_22_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_22_store|entry(9),0, fac_commoners,    [itm_hoodtunic_02, itm_carbatinae_1                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_middle_2],
  ["town_23_merchant", "Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_23_store|entry(9),0, fac_commoners,     [itm_woman_norse6,         itm_carbatinae_1,  itm_veil_f   ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_younger_1, woman_face_older_2],
  ["town_24_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_24_store|entry(9),0, fac_commoners,     [itm_hoodtunic_04, itm_carbatinae_1                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_25_merchant", "Merchant","{!}Merchant",tf_hero|tf_randomize_face|tf_is_merchant, scn_town_25_store|entry(9),0, fac_commoners,     [itm_hoodtunic_04,   itm_carbatinae_1                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_26_merchant", "Merchant","{!}Merchant",tf_alta  |tf_hero|tf_randomize_face|tf_is_merchant, scn_town_26_store|entry(9),0, fac_commoners,     [itm_woman_norse3,  itm_carbatinae_1                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_27_merchant", "Merchant","{!}Merchant",tf_hero|tf_randomize_face|tf_is_merchant, scn_town_27_store|entry(9),0, fac_commoners,     [itm_hoodtunic_06,itm_carbatinae_1                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],

  ["town_28_merchant", "Merchant","{!}Merchant",tf_alto   |tf_hero|tf_randomize_face|tf_is_merchant, scn_town_28_store|entry(9),0, fac_commoners,     [itm_hoodtunic_07, itm_carbatinae_1                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_29_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_29_store|entry(9),0, fac_commoners,     [itm_hoodtunic_08, itm_carbatinae_1                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],

  ["salt_mine_merchant","Aeron ap Gareth","Aeron ap Gareth",                tf_hero|tf_is_merchant, scn_salt_mine|entry(1),0, fac_commoners,        [itm_hoodtunic_01, itm_carbatinae_1],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x0000000ebe0911d166ad8db91390aa09000000000011b6bc0000000000000000],

# Horse Merchants

  ["town_1_horse_merchant","Horse Merchant","{!}Town 1 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,    0, 0, fac_commoners,[itm_hoodtunic_01,           itm_carbatinae_4,      itm_phrygian15],   def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_middle_2, man_face_older_2],
  ["town_2_horse_merchant","Horse Merchant","{!}Town 2 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_hoodtunic_01,          itm_carbatinae_1,],                      def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_3_horse_merchant","Horse Merchant","{!}Town 3 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_alto,      0, 0, fac_commoners,[itm_hoodtunic_02,          itm_carbatinae_1],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_middle_2],
  ["town_4_horse_merchant","Horse Merchant","{!}Town 4 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_hoodtunic_03,       itm_carbatinae_1],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_5_horse_merchant","Horse Merchant","{!}Town 5 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,      0, 0, fac_commoners,[itm_hoodtunic_01,                itm_carbatinae_vc4s,    itm_phrygian14],   def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_6_horse_merchant","Horse Merchant","{!}Town 6 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_bajo,      0, 0, fac_commoners,[itm_hoodtunic_04,         itm_carbatinae_1],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_middle_2],
  ["town_7_horse_merchant","Horse Merchant","{!}Town 7 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,       0, 0, fac_commoners,[itm_hoodtunic_05,         itm_carbatinae_1],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_8_horse_merchant","Horse Merchant","{!}Town 8 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_hoodtunic_06,         itm_carbatinae_1],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_9_horse_merchant","Horse Merchant","{!}Town 9 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_alto,      0, 0, fac_commoners,[itm_hoodtunic_07,       itm_carbatinae_vc4s],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_10_horse_merchant","Horse Merchant","{!}Town 10 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,    0, 0, fac_commoners,[itm_hoodtunic_08,          itm_carbatinae_4,      itm_phrygian16],     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_11_horse_merchant","Horse Merchant","{!}Town 11 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_hoodtunic_01,         itm_carbatinae_1],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_12_horse_merchant","Horse Merchant","{!}Town 12 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_bajo,    0, 0, fac_commoners,[itm_hoodtunic_02,      itm_carbatinae_1],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_13_horse_merchant","Horse Merchant","{!}Town 13 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,     0, 0, fac_commoners,[itm_hoodtunic_03,        itm_carbatinae_1],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_14_horse_merchant","Horse Merchant","{!}Town 14 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,     0, 0, fac_commoners,[itm_hoodtunic_01,       itm_carbatinae_4,      itm_phrygian17],     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_15_horse_merchant","Horse Merchant","{!}Town 15 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_hoodtunic_04,         itm_carbatinae_1],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_16_horse_merchant","Horse Merchant","{!}Town 16 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_alto,    0, 0, fac_commoners,[itm_hoodtunic_05,      itm_carbatinae_1],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_17_horse_merchant","Horse Merchant","{!}Town 17 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_hoodtunic_06,        itm_carbatinae_1],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_18_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,  0, 0, fac_commoners,[itm_hoodtunic_01,       itm_carbatinae_4],     def_attrib|level(5),wp(20),knows_inventory_management_10,man_face_young_1, man_face_older_2],
  ["town_19_horse_merchant","Horse Merchant","{!}Town 15 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,    0, 0, fac_commoners,[itm_hoodtunic_07,         itm_carbatinae_2],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_20_horse_merchant","Horse Merchant","{!}Town 16 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_alto,     0, 0, fac_commoners,[itm_hoodtunic_08,      itm_carbatinae_2],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_21_horse_merchant","Horse Merchant","{!}Town 17 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_hoodtunic_01,        itm_carbatinae_2],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_middle_2],
  ["town_22_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,    0, 0, fac_commoners,[itm_hoodtunic_01,       itm_carbatinae_4],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_23_horse_merchant","Horse Merchant","{!}Town 23 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,    0, 0, fac_commoners,[itm_hoodtunic_02,          itm_carbatinae_1],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_24_horse_merchant","Horse Merchant","{!}Town 24 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_hoodtunic_03,       itm_carbatinae_1],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_25_horse_merchant","Horse Merchant","{!}Town 25 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,    0, 0, fac_commoners,[itm_hoodtunic_01,                itm_carbatinae_vc4s],   def_attrib|level(5),wp(20),knows_inventory_management_10,man_face_young_1, man_face_older_2],
  ["town_26_horse_merchant","Horse Merchant","{!}Town 26 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_bajo,    0, 0, fac_commoners,[itm_hoodtunic_04,         itm_carbatinae_1],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_27_horse_merchant","Horse Merchant","{!}Town 27 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,     0, 0, fac_commoners,[itm_hoodtunic_05,         itm_carbatinae_1],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_28_horse_merchant","Horse Merchant","{!}Town 28 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_hoodtunic_06,         itm_carbatinae_1],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_29_horse_merchant","Horse Merchant","{!}Town 29 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_alto,    0, 0, fac_commoners,[itm_hoodtunic_07,       itm_carbatinae_vc4s],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],


#Town Mayors  Guild Master  #itm_btunic_11 itm_btunic_16 itm_gambeson2 itm_gambeson2 itm_nobleman_outfit itm_rich_outfit
  ["town_1_mayor", "Mayor", "{!}Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_hoodtunic_01, itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["town_2_mayor", "Mayor", "{!}Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_hoodtunic_02,     itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_3_mayor", "Mayor", "{!}Mayor", tf_bajo|tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_hoodtunic_03,       itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_4_mayor", "Hallvard", "{!}Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_btunic_15,      itm_carbatinae_4],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_5_mayor", "Mayor", "{!}Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_btunic_16,     itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_6_mayor", "Mayor", "{!}Mayor", tf_alto|tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_ptunic_6,       itm_carbatinae_1],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_7_mayor", "Mayor", "{!}Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_ptunic_7,     itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_8_mayor", "Mayor", "{!}Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_yellow_cloak,       itm_carbatinae_1],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_9_mayor", "Mayor", "{!}Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_briton_tunic11,       itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_10_mayor", "Mayor", "{!}Mayor", tf_bajo|tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_btunic_16,     itm_carbatinae_4],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_11_mayor", "Mayor", "{!}Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_gaeltunic_8woman,     itm_carbatinae_1],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_12_mayor", "Mayor", "{!}Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_ptunic_8,       itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_13_mayor", "Mayor", "{!}Mayor", tf_alto|tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_briton_tunic12,    itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_14_mayor", "Mayor", "{!}Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_ptunic_9,      itm_carbatinae_4],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_15_mayor", "Mayor", "{!}Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_picts_hoodtunic_01,     itm_carbatinae_1],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_16_mayor", "Mayor", "{!}Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_ptunic_10,       itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_17_mayor", "Mayor", "{!}Mayor", tf_bajo|tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_briton_tunic13,    itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_18_mayor", "Mayor", "{!}Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_gael_hoodtunic_09,      itm_carbatinae_4],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_19_mayor", "Mayor", "{!}Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_gael_hoodtunic_11,     itm_carbatinae_2],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_20_mayor", "Mayor", "{!}Mayor", tf_alto|tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_gael_hoodtunic_10,       itm_carbatinae_2], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_21_mayor", "Mayor", "{!}Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_gael_hoodtunic_09,    itm_carbatinae_2],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_22_mayor", "Donngal", "{!}Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_green_cloak,      itm_carbatinae_2],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_23_mayor", "Mayor", "{!}Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_ptunic_12,       itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_24_mayor", "Mayor", "{!}Mayor", tf_bajo|tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_yellow_cloak,      itm_carbatinae_4],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_25_mayor", "Mayor", "{!}Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_yellow_cloak,     itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_26_mayor", "Mayor", "{!}Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_green_cloak,       itm_carbatinae_1],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_27_mayor", "Mayor", "{!}Mayor", tf_alto|tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_ptunic_11,     itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_28_mayor", "Mayor", "{!}Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_red_cloak,       itm_carbatinae_1],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_29_mayor", "Mayor", "{!}Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_red_cloak,       itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],


#Village stores
  ["village_1_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_bl_tunic06, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc,            man_face_old_1, man_face_older_2],
  ["village_2_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_bl_tunic12, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc,                              man_face_old_1, man_face_old_2],
  ["village_3_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_bl_tunic07, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc,                         man_face_old_1, man_face_older_2],
  ["village_4_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_bl_tunic08, itm_carbatinae_1, itm_spangenhelm_1],def_attrib|level(22),wp(180),knows_merchant_npc,        man_face_old_1, man_face_old_2],
  ["village_5_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_bl_tunic12, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc,                      man_face_older_1, man_face_older_2],
  ["village_6_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_bl_tunic09, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc,                          man_face_old_1, man_face_older_2],
  ["village_7_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_bl_tunic11, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc,                         man_face_old_1, man_face_older_2],
  ["village_8_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_bl_tunic08, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc,        man_face_old_1, man_face_older_2],
  ["village_9_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ptunic_6, itm_carbatinae_1, itm_spangenhelm_1],def_attrib|level(22),wp(180),knows_merchant_npc,         man_face_old_1, man_face_old_2],
  ["village_10_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ptunic_7, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc,                              man_face_old_1, man_face_older_2],
  ["village_11_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ptunic_8, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc,                         man_face_old_1, man_face_older_2],
  ["village_12_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ptunic_9, itm_carbatinae_vc4s, itm_spangenhelm_1],def_attrib|level(22),wp(180),knows_merchant_npc,             man_face_old_1, man_face_older_2],
  ["village_13_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ptunic_10, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc,                         man_face_old_1, man_face_older_2],
  ["village_14_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ptunic_11, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc,                              man_face_old_1, man_face_older_2],
  ["village_15_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ptunic_12, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc,            man_face_old_1, man_face_older_2],
  ["village_16_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ptunic_6, itm_carbatinae_1, itm_spangenhelm_1],def_attrib|level(22),wp(180),knows_merchant_npc, man_face_old_1, man_face_older_2],
  ["village_17_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ptunic_7, itm_carbatinae_1,itm_phrygian17],def_attrib|level(22),wp(180),knows_merchant_npc,             man_face_old_1, man_face_older_2],
  ["village_18_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ptunic_8, itm_carbatinae_1, itm_spangenhelm_1],def_attrib|level(22),wp(180),knows_merchant_npc, man_face_old_1, man_face_older_2],
  ["village_19_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ptunic_9, itm_carbatinae_1, itm_phrygian17],def_attrib|level(22),wp(180),knows_merchant_npc,            man_face_old_1, man_face_older_2],
  ["village_20_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ptunic_10, itm_carbatinae_1, itm_spangenhelm_1],def_attrib|level(22),wp(180),knows_merchant_npc, man_face_old_1, man_face_older_2],
  ["village_21_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_bl_tunic06, itm_carbatinae_vc4s, itm_spangenhelm_1],def_attrib|level(22),wp(180),knows_merchant_npc,             man_face_old_1, man_face_old_2],
  ["village_22_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_bl_tunic07, itm_carbatinae_1,itm_phrygian17],def_attrib|level(22),wp(180),knows_merchant_npc,             man_face_old_1, man_face_older_2],
  ["village_23_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_bl_tunic08, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc,            man_face_old_1, man_face_older_2],
  ["village_24_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_bl_tunic09, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc,                              man_face_old_1, man_face_old_2],
  ["village_25_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_bl_tunic10, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc,                      man_face_older_1, man_face_older_2],
  ["village_26_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_bl_tunic11, itm_carbatinae_vc4s, itm_spangenhelm_1],def_attrib|level(22),wp(180),knows_merchant_npc,             man_face_old_1, man_face_old_2],
  ["village_27_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_bl_tunic12, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc,        man_face_old_1, man_face_older_2],
  ["village_28_elder","Godiva_the_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_bl_tunic06, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc,                              man_face_old_1, man_face_older_2],
  ["village_29_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_briton_tunic10, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc,                          man_face_old_1, man_face_older_2],
  ["village_30_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_briton_tunic11, itm_carbatinae_vc4s, itm_spangenhelm_1],def_attrib|level(22),wp(180),knows_merchant_npc,             man_face_old_1, man_face_older_2],
  ["village_31_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_briton_tunic12, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc,                         man_face_old_1, man_face_old_2],
  ["village_32_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_briton_tunic13, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc,                              man_face_old_1, man_face_older_2],
  ["village_33_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_briton_tunic14, itm_carbatinae_vc4s, itm_spangenhelm_1],def_attrib|level(22),wp(180),knows_merchant_npc,             man_face_old_1, man_face_older_2],
  ["village_34_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_briton_tunic11, itm_carbatinae_1,itm_phrygian17],def_attrib|level(22),wp(180),knows_merchant_npc,             man_face_older_1, man_face_older_2],
  ["village_35_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_picts_hoodtunic_14, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc,                              man_face_old_1, man_face_older_2],
  ["village_36_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_picts_hoodtunic_15, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc,                          man_face_old_1, man_face_older_2],
  ["village_37_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_picts_hoodtunic_16, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc,                              man_face_old_1, man_face_older_2],
  ["village_38_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_picts_hoodtunic_17, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc,                          man_face_older_1, man_face_older_2],
  ["village_39_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_picts_hoodtunic_18, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc,                         man_face_old_1, man_face_older_2],
  ["village_40_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_picts_hoodtunic_14, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc,                              man_face_old_1, man_face_older_2],
  ["village_41_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_briton_tunic9, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc,                         man_face_old_1, man_face_older_2],
  ["village_42_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_briton_tunic10, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc,                              man_face_old_1, man_face_older_2],
  ["village_43_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_briton_tunic11, itm_carbatinae_vc4s, itm_spangenhelm_1],def_attrib|level(22),wp(180),knows_merchant_npc,             man_face_old_1, man_face_older_2],
  ["village_44_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_briton_tunic12, itm_carbatinae_1,itm_phrygian17],def_attrib|level(22),wp(180),knows_merchant_npc,             man_face_old_1, man_face_older_2],
  ["village_45_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_briton_tunic13, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc,                              man_face_old_1, man_face_older_2],
  ["village_46_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_briton_tunic14, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc,                          man_face_old_1, man_face_older_2],
  ["village_47_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_briton_tunic13, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc,                              man_face_old_1, man_face_older_2],
  ["village_48_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_briton_tunic12, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc,                          man_face_older_1, man_face_older_2],
  ["village_49_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_btunic_11, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc,                         man_face_old_1, man_face_older_2],
  ["village_50_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_btunic_12, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc,                              man_face_older_1, man_face_older_2],
  ["village_51_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_btunic_13, itm_carbatinae_vc4s, itm_spangenhelm_1],def_attrib|level(22),wp(180),knows_merchant_npc,             man_face_old_1, man_face_older_2],
  ["village_52_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_btunic_14, itm_carbatinae_1,itm_phrygian17],def_attrib|level(22),wp(180),knows_merchant_npc,             man_face_old_1, man_face_older_2],
  ["village_53_elder","Wigmund_the_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_btunic_11, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc,            man_face_old_1, man_face_older_2],
  ["village_54_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_btunic_15, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc,                              man_face_old_1, man_face_older_2],
  ["village_55_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_btunic_16, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc, man_face_old_1, man_face_older_2],
  ["village_56_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_btunic_16, itm_carbatinae_vc4s, itm_spangenhelm_1],def_attrib|level(22),wp(180),knows_merchant_npc, man_face_old_1, man_face_older_2],
  ["village_57_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_btunic_15, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc, man_face_old_1, man_face_older_2],
  ["village_58_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_btunic_14, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc, man_face_old_1, man_face_older_2],
  ["village_59_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_btunic_13, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc, man_face_old_1, man_face_older_2],
  ["village_60_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_btunic_12, itm_carbatinae_vc4s, itm_spangenhelm_1],def_attrib|level(22),wp(180),knows_merchant_npc, man_face_older_1, man_face_older_2],
  ["village_61_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_btunic_11, itm_carbatinae_vc4s, itm_spangenhelm_1],def_attrib|level(22),wp(180),knows_merchant_npc, man_face_old_1, man_face_older_2],
  ["village_62_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_btunic_13, itm_carbatinae_1,itm_phrygian17],def_attrib|level(22),wp(180),knows_merchant_npc, man_face_old_1, man_face_older_2],
  ["village_63_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_btunic_14, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc, man_face_old_1, man_face_older_2],
  ["village_64_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_gaeltunic_3woman, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc, man_face_old_1, man_face_older_2],
  ["village_65_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_gaeltunic_4woman, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc, man_face_old_1, man_face_older_2],
  ["village_66_elder","Pyr_the_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_gael_tunic_08, itm_carbatinae_vc4s, itm_spangenhelm_1],def_attrib|level(22),wp(180),knows_merchant_npc, man_face_older_1, man_face_older_2],
  ["village_67_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_gael_tunic_08, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc, man_face_older_1, man_face_older_2],
  ["village_68_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_gael_hoodtunic_09, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc, man_face_old_1, man_face_old_2],
  ["village_69_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_gael_hoodtunic_10, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc, man_face_old_1, man_face_older_2],
  ["village_70_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_gael_hoodtunic_11, itm_carbatinae_vc4s, itm_spangenhelm_1],def_attrib|level(22),wp(180),knows_merchant_npc, man_face_old_1, man_face_older_2],
  ["village_71_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_gael_hoodtunic_12, itm_carbatinae_vc4s, itm_spangenhelm_1],def_attrib|level(22),wp(180),knows_merchant_npc, man_face_old_1, man_face_older_2],
  ["village_72_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_gael_hoodtunic_12, itm_carbatinae_1,itm_phrygian17],def_attrib|level(22),wp(180),knows_merchant_npc, man_face_old_1, man_face_older_2],
  ["village_73_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_gael_tunic_05, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc, man_face_old_1, man_face_older_2],
  ["village_74_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_gael_tunic_06, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc, man_face_older_1, man_face_older_2],
  ["village_75_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_gael_tunic_05, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc, man_face_old_1, man_face_older_2],
  ["village_76_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_gael_tunic_06, itm_carbatinae_vc4s, itm_spangenhelm_1],def_attrib|level(22),wp(180),knows_merchant_npc, man_face_old_1, man_face_older_2],
  ["village_77_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_brat1, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc, man_face_old_1, man_face_older_2],
  ["village_78_elder","Caliacas", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_brat2, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc, man_face_old_1, man_face_older_2],
  ["village_79_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_brat3, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc, man_face_old_1, man_face_older_2],
  ["village_80_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_brat4, itm_carbatinae_vc4s, itm_spangenhelm_1],def_attrib|level(22),wp(180),knows_merchant_npc, man_face_old_1, man_face_old_2],
  ["village_81_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_brat3, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc,                         man_face_old_1, man_face_older_2],
  ["village_82_elder","Aesc_the_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_brat2, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc,                              man_face_old_1, man_face_older_2],
  ["village_83_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_brat1, itm_carbatinae_vc4s, itm_spangenhelm_1],def_attrib|level(22),wp(180),knows_merchant_npc,             man_face_old_1, man_face_older_2],
  ["village_84_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_brat4, itm_carbatinae_1,itm_phrygian17],def_attrib|level(22),wp(180),knows_merchant_npc,             man_face_old_1, man_face_older_2],
  ["village_85_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_briton_tunic24, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc,                              man_face_old_1, man_face_older_2],
  ["village_86_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_briton_tunic25, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc,                          man_face_old_1, man_face_older_2],
  ["village_87_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_briton_tunic26, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc,                              man_face_old_1, man_face_older_2],
  ["village_88_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_briton_tunic27, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc,                          man_face_old_1, man_face_old_2],
  ["village_89_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_briton_tunic28, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc,                         man_face_older_1, man_face_old_2],
  ["village_90_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_briton_tunic24, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc,                              man_face_old_1, man_face_older_2],
  ["village_91_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_briton_tunic25, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc,                         man_face_old_1, man_face_older_2],
  ["village_92_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_bl_tunic08, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc,                              man_face_old_1, man_face_older_2],
  ["village_93_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_bl_tunic10, itm_carbatinae_vc4s, itm_spangenhelm_1],def_attrib|level(22),wp(180),knows_merchant_npc,             man_face_old_1, man_face_older_2],
  ["village_94_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_bl_tunic11, itm_carbatinae_1,itm_phrygian17],def_attrib|level(22),wp(180),knows_merchant_npc,             man_face_old_1, man_face_old_2],
  ["village_95_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_bl_tunic12, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc,                              man_face_old_1, man_face_older_2],
  ["village_96_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_btunic_2woman, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc,                          man_face_old_1, man_face_older_2],
  ["village_97_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_btunic_2woman, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc,                              man_face_old_1, man_face_older_2],
  ["village_98_elder","Ingolf_the_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_btunic_1woman, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc,                          man_face_old_1, man_face_older_2],
  ["village_99_elder","Oleif_the_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_btunic_1woman, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc,                         man_face_older_1, man_face_old_2],
  ["village_100_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ptunic_6, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc,                              man_face_old_1, man_face_older_2],
  ["village_101_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ptunic_7, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc,                         man_face_old_1, man_face_older_2],
  ["village_102_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ptunic_8, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc,                              man_face_older_1, man_face_older_2],
  ["village_103_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_ptunic_9, itm_carbatinae_vc4s, itm_spangenhelm_1],def_attrib|level(22),wp(180),knows_merchant_npc,             man_face_old_1, man_face_older_2],
  ["village_104_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_hoodtunic_01, itm_carbatinae_1,itm_phrygian17],def_attrib|level(22),wp(180),knows_merchant_npc,             man_face_old_1, man_face_older_2],
  ["village_105_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_hoodtunic_02, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc,                              man_face_old_1, man_face_older_2],
  ["village_106_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_hoodtunic_03, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc,                          man_face_old_1, man_face_older_2],
  ["village_107_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_hoodtunic_04, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc,                              man_face_older_1, man_face_old_2],
  ["village_108_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_hoodtunic_05, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc,                          man_face_old_1, man_face_older_2],
  ["village_109_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_hoodtunic_06, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc,                         man_face_old_1, man_face_older_2],
  ["village_110_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_hoodtunic_07, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc,                              man_face_old_1, man_face_older_2],
  ["village_111_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_hoodtunic_01, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc,                         man_face_old_1, man_face_older_2],
  ["village_112_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_hoodtunic_02, itm_carbatinae_vc4s, itm_spangenhelm_1],def_attrib|level(22),wp(180),knows_merchant_npc,             man_face_old_1, man_face_older_2],
  ["village_113_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_hoodtunic_03, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc,                         man_face_old_1, man_face_older_2],
  ["village_114_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_hoodtunic_04, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc,                              man_face_old_1, man_face_older_2],
  ["village_115_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_hoodtunic_05, itm_carbatinae_1, itm_phrygian15],def_attrib|level(22),wp(180),knows_merchant_npc,            man_face_old_1, man_face_older_2],
  ["village_116_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_hoodtunic_06, itm_carbatinae_1, itm_spangenhelm_1],def_attrib|level(22),wp(180),knows_merchant_npc, man_face_old_1, man_face_older_2],
  ["village_117_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_hoodtunic_07, itm_carbatinae_1,itm_phrygian17],def_attrib|level(22),wp(180),knows_merchant_npc,             man_face_old_1, man_face_older_2],
  ["village_118_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_gael_tunic_08, itm_carbatinae_1, itm_spangenhelm_1],def_attrib|level(22),wp(180),knows_merchant_npc, man_face_old_1, man_face_older_2],
  ["village_119_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_gael_hoodtunic_09, itm_carbatinae_1, itm_phrygian17],def_attrib|level(22),wp(180),knows_merchant_npc,            man_face_old_1, man_face_older_2],
  ["village_120_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_btunic_4, itm_carbatinae_1, itm_spangenhelm_1],def_attrib|level(22),wp(180),knows_merchant_npc, man_face_old_1, man_face_older_2],
  ["village_121_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_btunic_4, itm_carbatinae_vc4s, itm_spangenhelm_1],def_attrib|level(22),wp(180),knows_merchant_npc,             man_face_old_1, man_face_older_2],
  ["village_122_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_btunic_4, itm_carbatinae_1,itm_phrygian17],def_attrib|level(22),wp(180),knows_merchant_npc,             man_face_old_1, man_face_older_2],
  ["village_123_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_bl_tunic01, itm_carbatinae_1, itm_phrygian15],def_attrib|level(22),wp(180),knows_merchant_npc,            man_face_old_1, man_face_older_2],
  ["village_124_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_gael_hoodtunic_10, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc,                              man_face_old_1, man_face_older_2],
  ["village_125_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_gael_hoodtunic_11, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc,                      man_face_old_1, man_face_older_2],
  ["village_126_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_gael_tunic_08, itm_carbatinae_vc4s, itm_spangenhelm_1],def_attrib|level(22),wp(180),knows_merchant_npc,             man_face_old_1, man_face_older_2],
  ["village_127_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_gael_hoodtunic_09, itm_carbatinae_vc4s, itm_phrygian15],def_attrib|level(22),wp(180),knows_merchant_npc,        man_face_old_1, man_face_older_2],
  ["village_128_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_gael_hoodtunic_10, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc,                              man_face_old_1, man_face_older_2],
  ["village_129_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_gael_hoodtunic_11, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc,                          man_face_old_1, man_face_older_2],
  ["village_130_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_gael_hoodtunic_12, itm_carbatinae_vc4s, itm_spangenhelm_1],def_attrib|level(22),wp(180),knows_merchant_npc,             man_face_old_1, man_face_older_2],
  ["village_131_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_gael_tunic_08, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc,                         man_face_old_1, man_face_older_2],
  ["village_132_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_bl_tunic06, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc,                              man_face_old_1, man_face_older_2],
  ["village_133_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_bl_tunic07, itm_carbatinae_vc4s, itm_spangenhelm_1],def_attrib|level(22),wp(180),knows_merchant_npc,             man_face_old_1, man_face_older_2],
  ["village_134_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_bl_tunic11, itm_carbatinae_1,itm_phrygian17],def_attrib|level(22),wp(180),knows_merchant_npc,             man_face_old_1, man_face_older_2],
  ["village_135_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_bl_tunic12, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc,                              man_face_old_1, man_face_older_2],
  ["village_136_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_gael_tunic_08, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc,                          man_face_old_1, man_face_older_2],
  ["village_137_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_gael_hoodtunic_09, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc,                              man_face_old_1, man_face_older_2],
  ["village_138_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_gael_hoodtunic_10, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc,                          man_face_old_1, man_face_older_2],
  ["village_139_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_gael_hoodtunic_11, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc,                         man_face_old_1, man_face_older_2],
  ["village_140_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_briton_tunic10, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc,                              man_face_old_1, man_face_older_2],
  ["village_141_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_briton_tunic11, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc,                         man_face_old_1, man_face_older_2],
  ["village_142_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_briton_tunic12, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc,                              man_face_old_1, man_face_older_2],
  ["village_143_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_briton_tunic13, itm_carbatinae_vc4s, itm_spangenhelm_1],def_attrib|level(22),wp(180),knows_merchant_npc,             man_face_old_1, man_face_older_2],
  ["village_144_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_briton_tunic24, itm_carbatinae_1,itm_phrygian17],def_attrib|level(22),wp(180),knows_merchant_npc,             man_face_old_1, man_face_older_2],
  ["village_145_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_briton_tunic25, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc,                              man_face_old_1, man_face_older_2],
  ["village_146_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_btunic_5woman, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc,                          man_face_old_1, man_face_older_2],
  ["village_147_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_btunic_6woman, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc,                              man_face_old_1, man_face_older_2],
  ["village_148_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_bl_tunic06, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc,                          man_face_old_1, man_face_older_2],
  ["village_149_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_bl_tunic07, itm_carbatinae_1],def_attrib|level(22),wp(180),knows_merchant_npc,man_face_old_1, man_face_older_2],
  ["village_150_elder","Thonkrik", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[itm_btunic_1woman, itm_phrygian15, itm_carbatinae_vc4s],def_attrib|level(22),wp(180),knows_merchant_npc, 0x0000000cd80c435056643ac4e17a535e00000000001db9110000000000000000],
##  ["village_151_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_btunic_11, itm_carbatinae_vc4s, itm_spangenhelm_1],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
##  ["village_152_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_bl_tunic01, itm_carbatinae_1,itm_phrygian17],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
##  ["village_153_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_bl_tunic01, itm_carbatinae_1, itm_phrygian15],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
##  ["village_154_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_btunic_11, itm_carbatinae_vc4s],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
##  ["village_155_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_bl_tunic01, itm_carbatinae_vc4s],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
##  ["village_156_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_btunic_11, itm_carbatinae_vc4s, itm_spangenhelm_1],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
##  ["village_157_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_bl_tunic01, itm_carbatinae_vc4s, itm_phrygian15],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
##  ["village_158_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_btunic_11, itm_carbatinae_vc4s],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
##  ["village_159_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_bl_tunic01, itm_carbatinae_1],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
##  ["village_160_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_carbatinae_vc4s, itm_spangenhelm_1],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
##  ["village_161_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_carbatinae_vc4s, itm_spangenhelm_1],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
##  ["village_162_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_bl_tunic01, itm_carbatinae_1,itm_phrygian17],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
##  ["village_163_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_bl_tunic01, itm_carbatinae_1, itm_phrygian15],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
##  ["village_164_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_carbatinae_vc4s],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
##  ["village_165_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_carbatinae_vc4s],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
###monasterios monje mercader
  ["monje_mercader","Monk merchant", "Monk merchants",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_carbatinae_vc4s],def_attrib|level(2),wp(20),knows_inventory_management_10,                              sac_face_younger_1, sac_face_older_2],

# Place extra merchants before this point
  ["merchants_end","merchants_end","merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],

# healer
  ["town_1_healer","Physician","{!}Town 1 Physician",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_robe9,],   def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_2_healer","Physician","{!}Town 2 Physician",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_robe9,],                      def_attrib|level(5),wp(20),knows_common, man_face_young_1, man_face_older_2],
  ["town_3_healer","Physician","{!}Town 3 Physician",tf_hero|tf_randomize_face|tf_is_merchant,      0, 0, fac_commoners,[itm_robe9,],                        def_attrib|level(5),wp(20),knows_common, man_face_young_1, man_face_older_2],
  ["town_4_healer","Physician","{!}Town 4 Physician",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_robe9,],                       def_attrib|level(5),wp(20),knows_common, man_face_young_1, man_face_older_2],
  ["town_5_healer","Physician","{!}Town 5 Physician",tf_hero|tf_randomize_face|tf_is_merchant|tf_alta,      0, 0, fac_commoners,[itm_robe9,],   def_attrib|level(5),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_6_healer","Physician","{!}Town 6 Physician",tf_hero|tf_randomize_face|tf_is_merchant,      0, 0, fac_commoners,[itm_robe10,],                        def_attrib|level(5),wp(20),knows_common, man_face_young_1, man_face_older_2],
  ["town_7_healer","Physician","{!}Town 7 Physician",tf_hero|tf_randomize_face|tf_is_merchant|tf_bajo,       0, 0, fac_commoners,[itm_robe9,],                     def_attrib|level(5),wp(20),knows_common, man_face_young_1, man_face_older_2],
  ["town_8_healer","Physician","{!}Town 8 Physician",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_robe9,],                        def_attrib|level(5),wp(20),knows_common, man_face_young_1, man_face_older_2],
  ["town_9_healer","Physician","{!}Town 9 Physician",tf_hero|tf_randomize_face|tf_is_merchant,      0, 0, fac_commoners,[itm_robe9,],                       def_attrib|level(5),wp(20),knows_common, man_face_young_1, man_face_older_2],
  ["town_10_healer","Physician","{!}Town 10 Physician",tf_hero|tf_randomize_face|tf_is_merchant|tf_baja,    0, 0, fac_commoners,[itm_robe9,],     def_attrib|level(5),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_11_healer","Physician","{!}Town 11 Physician",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_robe10,],                     def_attrib|level(5),wp(20),knows_common, man_face_young_1, man_face_older_2],
  ["town_12_healer","Physician","{!}Town 12 Physician",tf_hero|tf_randomize_face|tf_is_merchant,    0, 0, fac_commoners,[itm_robe10,],                        def_attrib|level(5),wp(20),knows_common, man_face_young_1, man_face_older_2],
  ["town_13_healer","Physician","{!}Town 13 Physician",tf_hero|tf_randomize_face|tf_is_merchant,     0, 0, fac_commoners,[itm_robe10,],                       def_attrib|level(5),wp(20),knows_common, man_face_young_1, man_face_older_2],
  ["town_14_healer","Physician","{!}Town 14 Physician",tf_hero|tf_randomize_face|tf_is_merchant|tf_osa,     0, 0, fac_commoners,[itm_robe10,],     def_attrib|level(5),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_15_healer","Physician","{!}Town 15 Physician",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_robe10,],                     def_attrib|level(5),wp(20),knows_common, man_face_young_1, man_face_older_2],
  ["town_16_healer","Physician","{!}Town 16 Physician",tf_hero|tf_randomize_face|tf_is_merchant,    0, 0, fac_commoners,[itm_robe9,],                        def_attrib|level(5),wp(20),knows_common, man_face_young_1, man_face_older_2],
  ["town_17_healer","Physician","{!}Town 17 Physician",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_robe9,],                       def_attrib|level(5),wp(20),knows_common, man_face_young_1, man_face_older_2],
  ["town_18_healer","Physician","{!}Town 18 Physician",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_robe9,],     def_attrib|level(5),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_19_healer","Physician","{!}Town 19 Physician",tf_hero|tf_randomize_face|tf_is_merchant,    0, 0, fac_commoners,[itm_robe9,],                     def_attrib|level(5),wp(20),knows_common, man_face_young_1, man_face_older_2],
  ["town_20_healer","Physician","{!}Town 20 Physician",tf_hero|tf_randomize_face|tf_is_merchant|tf_bajo,     0, 0, fac_commoners,[itm_robe9,],                        def_attrib|level(5),wp(20),knows_common, man_face_young_1, man_face_older_2],
  ["town_21_healer","Physician","{!}Town 21 Physician",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_robe10,],                       def_attrib|level(5),wp(20),knows_common, man_face_young_1, man_face_older_2],
  ["town_22_healer","Physician","{!}Town 22 Physician",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_robe9,],     def_attrib|level(5),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_23_healer","Physician","{!}Town 23 Physician",tf_hero|tf_randomize_face|tf_is_merchant|tf_alto,    0, 0, fac_commoners,[itm_robe9,],                        def_attrib|level(5),wp(20),knows_common, man_face_young_1, man_face_older_2],
  ["town_24_healer","Physician","{!}Town 24 Physician",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_robe9,],                       def_attrib|level(5),wp(20),knows_common, man_face_young_1, man_face_older_2],
  ["town_25_healer","Physician","{!}Town 25 Physician",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_robe9,],   def_attrib|level(5),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_26_healer","Physician","{!}Town 26 Physician",tf_hero|tf_randomize_face|tf_is_merchant|tf_bajo,    0, 0, fac_commoners,[itm_robe9,],                        def_attrib|level(5),wp(20),knows_common, man_face_young_1, man_face_older_2],
  ["town_27_healer","Physician","{!}Town 27 Physician",tf_hero|tf_randomize_face|tf_is_merchant,     0, 0, fac_commoners,[itm_robe9,],                     def_attrib|level(5),wp(20),knows_common, man_face_young_1, man_face_older_2],
  ["town_28_healer","Physician","{!}Town 28 Physician",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_robe9,],                        def_attrib|level(5),wp(20),knows_common, man_face_young_1, man_face_older_2],
  ["town_29_healer","Physician","{!}Town 29 Physician",tf_hero|tf_randomize_face|tf_is_merchant|tf_alto,    0, 0, fac_commoners,[itm_robe10,],                       def_attrib|level(5),wp(20),knows_common, man_face_young_1, man_face_older_2],
#followers
  ["town_30_healer","Physician","{!}Town 30 Physician",tf_hero|tf_randomize_face|tf_is_merchant,    0, 0, fac_commoners,[itm_robe10,],                       def_attrib|level(5),wp(20),knows_common, man_face_young_1, man_face_older_2],
  ["healer_end","healer_end","{!}healer_end", 0, 0, 0, fac_commoners, [], 0, 0, 0, 0, 0],

  # shipwright
  ["town_1_shipwright","Shipwright","{!}Town 1 Shipwright", 0, 0, 0, fac_commoners, [], 0, 0, 0, 0, 0],
  ["town_2_shipwright","Shipwright","{!}Town 2 Shipwright", 0, 0, 0, fac_commoners, [], 0, 0, 0, 0, 0],
  ["town_3_shipwright","Shipwright","{!}Town 3 Shipwright",tf_hero|tf_randomize_face|tf_is_merchant|tf_alto, 0, 0, fac_commoners,[itm_gambeson41, itm_carbatinae_1], def_attrib|level(5),wp(20),knows_common, man_face_young_1, man_face_older_2],
  ["port_chief", "Port Master", "Port Masters", tf_male|tf_hero|tf_is_merchant, 0, reserved, fac_neutral, [itm_carbatinae_2,itm_carbatinae_12qs,
itm_bl_tunic02,itm_linen_tunic,itm_bl_tunic02,itm_bl_tunic04,itm_bl_tunic04,itm_bl_tunic02], def_attrib|level(2), wp(20), knows_common,0x0000000db20430502a66765aa2daa51d00000000001fb8cc0000000000000000],
  ["town_5_shipwright","Kalle the Shipwright","{!}Town 5 Shipwright",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_btunic_13, itm_carbatinae_vc4s, itm_phrygian14], def_attrib|level(5),wp(20),knows_common, man_face_young_1, man_face_older_2],
  ["town_6_shipwright","Shipwright","{!}Town 6 Shipwright",tf_hero|tf_randomize_face|tf_is_merchant, 			  0, 0, fac_commoners,[itm_gambeson41,itm_carbatinae_1], 				def_attrib|level(5),wp(20),knows_common, man_face_young_1, man_face_older_2],
  ["town_7_shipwright","Shipwright","{!}Town 7 Shipwright",tf_hero|tf_randomize_face|tf_is_merchant|tf_oso, 0, 0, fac_commoners,[itm_bl_tunic01, itm_carbatinae_1], def_attrib|level(5),wp(20),knows_common, man_face_young_1, man_face_older_2],
  ["town_8_shipwright","Shipwright","{!}Town 8 Shipwright", 0, 0, 0, fac_commoners, [], 0, 0, 0, 0, 0],
  ["town_9_shipwright","Shipwright","{!}Town 9 Shipwright",tf_hero|tf_randomize_face|tf_is_merchant|tf_alto, 0, 0, fac_commoners,[itm_btunic_16, itm_carbatinae_vc4s], def_attrib|level(5),wp(20),knows_common, man_face_young_1, man_face_older_2],
  ["town_10_shipwright","Shipwright","{!}Town 10 Shipwright", 0, 0, 0, fac_commoners, [], 0, 0, 0, 0, 0],
  ["town_11_shipwright","Shipwright","{!}Town 11 Shipwright",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_nobleman_outfit, itm_carbatinae_1], def_attrib|level(5),wp(20),knows_common, man_face_young_1, man_face_older_2],
  ["town_12_shipwright","Shipwright","{!}Town 12 Shipwright",tf_hero|tf_randomize_face|tf_is_merchant|tf_bajo, 0, 0, fac_commoners,[itm_btunic_16, itm_carbatinae_1], def_attrib|level(5),wp(20),knows_common, man_face_young_1, man_face_older_2],
  ["town_13_shipwright","Shipwright","{!}Town 13 Shipwright",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_bl_tunic01, itm_carbatinae_1], def_attrib|level(5),wp(20),knows_common, man_face_young_1, man_face_older_2],
  ["town_14_shipwright","Shipwright","{!}Town 14 Shipwright",tf_hero|tf_randomize_face|tf_is_merchant|tf_bajo, 0, 0, fac_commoners,[itm_bl_tunic02, itm_carbatinae_4, itm_phrygian15], def_attrib|level(5),wp(20),knows_common, man_face_young_1, man_face_older_2],
  ["town_15_shipwright","Shipwright","{!}Town 15 Shipwright", 0, 0, 0, fac_commoners, [], 0, 0, 0, 0, 0],
  ["town_16_shipwright","Shipwright","{!}Town 16 Shipwright", 0, 0, 0, fac_commoners, [], 0, 0, 0, 0, 0],
  ["town_17_shipwright","Shipwright","{!}Town 17 Shipwright", 0, 0, 0, fac_commoners, [], 0, 0, 0, 0, 0],
  ["town_18_shipwright","Shipwright","{!}Town 18 Shipwright", 0, 0, 0, fac_commoners, [], 0, 0, 0, 0, 0],
  ["town_19_shipwright","Shipwright","{!}Town 19 Shipwright",tf_hero|tf_randomize_face|tf_is_merchant|tf_bajo, 0, 0, fac_commoners,[itm_gambeson41, itm_carbatinae_2], def_attrib|level(5),wp(20),knows_common, man_face_young_1, man_face_older_2],
  ["town_20_shipwright","Shipwright","{!}Town 20 Shipwright",tf_hero|tf_randomize_face|tf_is_merchant|tf_oso, 0, 0, fac_commoners,[itm_bl_tunic02, itm_carbatinae_2], def_attrib|level(5),wp(20),knows_common, man_face_young_1, man_face_older_2],
  ["town_21_shipwright","Shipwright","{!}Town 21 Shipwright", 0, 0, 0, fac_commoners, [], 0, 0, 0, 0, 0],
  ["town_22_shipwright","Shipwright","{!}Town 22 Shipwright", 0, 0, 0, fac_commoners, [], 0, 0, 0, 0, 0],
  ["town_23_shipwright","Shipwright","{!}Town 23 Shipwright", 0, 0, 0, fac_commoners, [], 0, 0, 0, 0, 0],
  ["town_24_shipwright","Shipwright","{!}Town 24 Shipwright", 0, 0, 0, fac_commoners, [], 0, 0, 0, 0, 0],
  ["town_25_shipwright","Shipwright","{!}Town 25 Shipwright",tf_hero|tf_randomize_face|tf_is_merchant|tf_bajo, 0, 0, fac_commoners,[itm_btunic_13, itm_carbatinae_vc4s, itm_phrygian14], def_attrib|level(5),wp(20),knows_common, man_face_young_1, man_face_older_2],
  ["town_26_shipwright","Shipwright","{!}Town 26 Shipwright",tf_hero|tf_randomize_face|tf_is_merchant|tf_bajo, 0, 0, fac_commoners,[itm_bl_tunic01, itm_carbatinae_1], def_attrib|level(5),wp(20),knows_common, man_face_young_1, man_face_older_2],
  ["town_27_shipwright","Shipwright","{!}Town 27 Shipwright",tf_hero|tf_randomize_face|tf_is_merchant|tf_alto, 0, 0, fac_commoners,[itm_bl_tunic01, itm_carbatinae_1], def_attrib|level(5),wp(20),knows_common, man_face_young_1, man_face_older_2],
  ["town_28_shipwright","Shipwright","{!}Town 28 Shipwright",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_nobleman_outfit, itm_carbatinae_1], def_attrib|level(5),wp(20),knows_common, man_face_young_1, man_face_older_2],
  ["town_29_shipwright","Shipwright","{!}Town 29 Shipwright",tf_hero|tf_randomize_face|tf_is_merchant|tf_alto, 0, 0, fac_commoners,[itm_btunic_16, itm_carbatinae_vc4s], def_attrib|level(5),wp(20),knows_common, man_face_young_1, man_face_older_2],
  ["shipwright_end","Boar","Boars", 0, 0, 0, fac_commoners, [], 0, 0, 0, 0, 0],	#reused in addon for hunting feature
  
  #Used for player enterprises
  ["town_1_master_craftsman", "Craftsman", "{!}Town 1 Craftsman", tf_hero|tf_is_merchant|tf_alto, 0,reserved,  fac_neutral,[     itm_bl_tunic02,       itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_2_master_craftsman", "Craftsman", "{!}Town 2 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_gambeson1,     itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, 0x0000000f010811c92d3295e46a96c72300000000001f5a980000000000000000],
  ["town_3_master_craftsman", "Craftsman", "{!}Town 3 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_bl_tunic01,       itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common, 0x000000001b083203151d2ad5648e52b400000000001b172e0000000000000000],
  ["town_4_master_craftsman", "Craftsman", "{!}Town 4 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_bl_tunic02,      itm_carbatinae_4],     def_attrib|level(2),wp(20),knows_common, 0x000000001a10114f091b2c259cd4c92300000000000228dd0000000000000000],
  ["town_5_master_craftsman", "Craftsman", "{!}Town 5 Craftsman", tf_hero|tf_is_merchant|tf_bajo, 0,reserved,  fac_neutral,[     itm_btunic_16,     itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, 0x000000000d1044c578598cd92b5256db00000000001f23340000000000000000],
  ["town_6_master_craftsman", "Craftsman", "{!}Town 6 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_bl_tunic02,       itm_carbatinae_1],   def_attrib|level(2),wp(20),knows_common, 0x000000001f046285493eaf1b048abcdb00000000001a8aad0000000000000000],
  ["town_7_master_craftsman", "Craftsman", "{!}Town 7 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_btunic_16,     itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, 0x000000002b0052c34c549225619356d400000000001cc6e60000000000000000],
  ["town_8_master_craftsman", "Craftsman", "{!}Town 8 Craftsman", tf_hero|tf_is_merchant|tf_alto, 0,reserved,  fac_neutral,[     itm_bl_tunic02,       itm_carbatinae_1],   def_attrib|level(2),wp(20),knows_common, 0x0000000fdb0c20465b6e51e8a12c82d400000000001e148c0000000000000000],
  ["town_9_master_craftsman", "Craftsman", "{!}Town 9 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_bl_tunic01,       itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common, 0x00000009f7005246071db236e296a45300000000001a8b0a0000000000000000],
  ["town_10_master_craftsman", "Craftsman", "{!}Town 10 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_btunic_16,     itm_carbatinae_4],     def_attrib|level(2),wp(20),knows_common, 0x00000009f71012c2456a921aa379321a000000000012c6d90000000000000000],
  ["town_11_master_craftsman", "Craftsman", "{!}Town 11 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_bl_tunic02,     itm_carbatinae_1],   def_attrib|level(2),wp(20),knows_common, 0x00000009f308514428db71b9ad70b72400000000001dc9140000000000000000],
  ["town_12_master_craftsman", "Craftsman", "{!}Town 12 Craftsman", tf_hero|tf_is_merchant|tf_bajo, 0,reserved,  fac_neutral,[ itm_bl_tunic01,       itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common, 0x00000009e90825863853a5b91cd71a5b00000000000598db0000000000000000],
  ["town_13_master_craftsman", "Craftsman", "{!}Town 13 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_btunic_16,     itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, 0x00000009fa0c708f274c8eb4c64e271300000000001eb69a0000000000000000],
  ["town_14_master_craftsman", "Craftsman", "{!}Town 14 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_bl_tunic02,      itm_carbatinae_4],     def_attrib|level(2),wp(20),knows_common, 0x00000007590c3206155c8b475a4e439a00000000001f489a0000000000000000],
  ["town_15_master_craftsman", "Craftsman", "{!}Town 14 Craftsman", tf_hero|tf_is_merchant|tf_alto, 0,reserved,  fac_neutral,[ itm_bl_tunic02,      itm_carbatinae_4],     def_attrib|level(2),wp(20),knows_common, 0x00000007440022d04b2c6cb7d3723d5a00000000001dc90a0000000000000000],
  ["town_16_master_craftsman", "Craftsman", "{!}Town 14 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_bl_tunic02,      itm_carbatinae_4],     def_attrib|level(2),wp(20),knows_common, 0x00000007680c3586054b8e372e4db65c00000000001db7230000000000000000],
  ["town_17_master_craftsman", "Craftsman", "{!}Town 14 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_bl_tunic02,      itm_carbatinae_4],     def_attrib|level(2),wp(20),knows_common, 0x0000000766046186591b564cec85d2e200000000001e4cea0000000000000000],
  ["town_18_master_craftsman", "Craftsman", "{!}Town 14 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_bl_tunic02,      itm_carbatinae_4],     def_attrib|level(2),wp(20),knows_common, 0x0000000e7e0075523a6aa9b6da61e8dd00000000001d96d30000000000000000],
  ["town_19_master_craftsman", "Craftsman", "{!}Town 14 Craftsman", tf_hero|tf_is_merchant|tf_bajo, 0,reserved,  fac_neutral,[ itm_bl_tunic02,      itm_carbatinae_4],     def_attrib|level(2),wp(20),knows_common, 0x000000002408314852a432e88aaa42e100000000001e284e0000000000000000],
  ["town_20_master_craftsman", "Craftsman", "{!}Town 14 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_arena_tunic_white,      itm_carbatinae_4],     def_attrib|level(2),wp(20),knows_common, 0x000000001104449136e44cbd1c9352bc000000000005e8d10000000000000000],
  ["town_21_master_craftsman", "Craftsman", "{!}Town 14 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_bl_tunic02,      itm_carbatinae_4],     def_attrib|level(2),wp(20),knows_common, 0x00000000131032d3351c6e43226ec96c000000000005b5240000000000000000],
  ["town_22_master_craftsman", "Craftsman", "{!}Town 14 Craftsman", tf_hero|tf_is_merchant|tf_alto, 0,reserved,  fac_neutral,[ itm_arena_tunic_white,      itm_carbatinae_4],     def_attrib|level(2),wp(20),knows_common, 0x00000000200c658a5723b1a3148dc455000000000015ab920000000000000000],
  ["town_23_master_craftsman", "Craftsman", "{!}Town 1 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_bl_tunic02,       itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_24_master_craftsman", "Craftsman", "{!}Town 2 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_gambeson1,     itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, 0x0000000f010811c92d3295e46a96c72300000000001f5a980000000000000000],
  ["town_25_master_craftsman", "Craftsman", "{!}Town 5 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_btunic_16,     itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, 0x000000001b083203151d2ad5648e52b400000000001b172e0000000000000000],
  ["town_26_master_craftsman", "Craftsman", "{!}Town 6 Craftsman", tf_hero|tf_is_merchant|tf_bajo, 0,reserved,  fac_neutral,[     itm_bl_tunic02,       itm_carbatinae_1],   def_attrib|level(2),wp(20),knows_common, 0x000000001a10114f091b2c259cd4c92300000000000228dd0000000000000000],
  ["town_27_master_craftsman", "Craftsman", "{!}Town 7 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_nobleman_outfit,     itm_carbatinae_vc4s],   def_attrib|level(2),wp(20),knows_common, 0x000000002b0052c34c549225619356d400000000001cc6e60000000000000000],
  ["town_28_master_craftsman", "Craftsman", "{!}Town 8 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_bl_tunic02,       itm_carbatinae_1],   def_attrib|level(2),wp(20),knows_common, 0x0000000fdb0c20465b6e51e8a12c82d400000000001e148c0000000000000000],
  ["town_29_master_craftsman", "Craftsman", "{!}Town 9 Craftsman", tf_hero|tf_is_merchant|tf_alto, 0,reserved,  fac_neutral,[     itm_bl_tunic01,       itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common, 0x00000009f7005246071db236e296a45300000000001a8b0a0000000000000000],
  
# Chests
  ["zendar_chest","{!}Zendar Chest","{!}Zendar Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,
   [],def_attrib|level(18),wp(60),knows_common, 0],
  ["tutorial_chest_1","{!}Melee Weapons Chest","{!}Melee Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_tutorial_sword, itm_tutorial_axe, itm_tutorial_spear, itm_tutorial_club, itm_tutorial_battle_axe],def_attrib|level(18),wp(60),knows_common, 0],
  ["tutorial_chest_2","{!}Ranged Weapons Chest","{!}Ranged Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_tutorial_short_bow, itm_tutorial_arrows, itm_tutorial_crossbow, itm_tutorial_bolts, itm_tutorial_throwing_daggers],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_1","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_byrnie4,itm_noble_sword_7],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_2","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_carbatinae_5s,itm_viking_shield_round_05],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_3","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_briton_helm12,itm_seax_1],def_attrib|level(18),wp(60),knows_common, 0],

  ["household_possessions","{!}household_possessions","{!}household_possessions",tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],  
###followers camp mules inventory chief
  ["household_possessions2","{!}household_possessions","{!}household_possessions",tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],  
  
### These are used as arrays in the scripts. 
  ["temp_array_a","{!}temp_array_a","{!}temp_array_a",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],
  ["temp_array_b","{!}temp_array_b","{!}temp_array_b",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],
  ["temp_array_c","{!}temp_array_c","{!}temp_array_c",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],
####chief acaba
  ["stack_selection_amounts","{!}stack_selection_amounts","{!}stack_selection_amounts",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
  ["stack_selection_ids","{!}stack_selection_ids","{!}stack_selection_ids",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

  ["notification_menu_types","{!}notification_menu_types","{!}notification_menu_types",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
  ["notification_menu_var1","{!}notification_menu_var1","{!}notification_menu_var1",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
  ["notification_menu_var2","{!}notification_menu_var2","{!}notification_menu_var2",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

  ["banner_background_color_array","{!}banner_background_color_array","{!}banner_background_color_array",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

  ["multiplayer_data","{!}multiplayer_data","{!}multiplayer_data",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

##  ["black_khergit_guard","Black Khergit Guard","Black Khergit Guard",tf_mounted|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_black_khergits,
##   [itm_arrows,itm_noble_sword_5,itm_ragnar_seax,itm_winged_mace,itm_long_heavy_spear2,itm_khergit_bow,itm_briton_helm12,itm_crown1,itm_khergit_guard_boots,itm_mail_shirt_6,itm_viking_shield_round_03,itm_steppe_horse,itm_warhorse],
##   def_attrib|level(28),wp(140),knows_riding_6|knows_ironflesh_4|knows_horse_archery_6|knows_power_draw_6,khergit_face1, khergit_face2],


# Add Extra Quest NPCs below this point  
####chief quest###
##  ["npc17","Neko","Neko", tf_oso|tf_hero|tf_unmoveable_in_party_window, scn_town_41_tavern|entry(6),reserved, fac_neko,[itm_btunic_11,itm_cantabro_shield_2,itm_carbatinae_1,itm_new_mace],def_attrib3|level(27),
##   wp(190),knows_warrior_elite,
##   0x000000019d004001570b893712c8d28d00000000001dc8990000000000000000],
##  ["npc18","Cado","Cado", tf_alto|tf_hero|tf_unmoveable_in_party_window, scn_town_17_tavern|entry(6),reserved, fac_neko,[itm_byrnie9,itm_cantabro_shield_1,itm_carbatinae_1,itm_new_sword],def_attrib3|level(29),
##   wp(260),knows_warrior_elite|knows_wound_treatment_8|knows_first_aid_8|knows_surgery_8,
##   0x000000091b0030112723494893b1a91b00000000001d291e0000000000000000], #chief idibil
##  ["hareck","Cerdic","Cerdic", tf_bajo|tf_hero,scn_town_41_tavern|entry(5),reserved,
##   fac_commoners,[itm_bl_tunic02,itm_carbatinae_1],def_attrib|level(5),wp(20),knows_common,0x0000000dc40011490a1bccf7d98db6df00000000001e16f30000000000000000],
##  ["violet","Aelfwyn","Aelfwyn",tf_hero|tf_female|tf_guarantee_boots|tf_guarantee_armor,scn_town_2_tavern|entry(6),reserved,fac_commoners,
##   [itm_lady_dress_ruby],
##   def_attrib|level(2),wp(40),knows_common,0x000000018c00b0061d64b5cb5c86468c00000000001c5add0000000000000000],
##  ["violet2","Lunete","Lunete",tf_alta|tf_hero|tf_female|tf_guarantee_boots|tf_guarantee_armor,scn_town_7_tavern|entry(6),reserved,fac_commoners,
##   [itm_lady_dress_ruby],
##   def_attrib|level(2),wp(40),knows_common,0x000000019008100166e18d570c59cc5500000000001e45330000000000000000],
##  ["violet3","Ceara","Ceara",tf_baja|tf_hero|tf_female|tf_guarantee_boots|tf_guarantee_armor,scn_town_35_tavern|entry(6),reserved,fac_commoners,
##   [itm_lady_dress_ruby],
##   def_attrib|level(2),wp(40),knows_common,0x000000018300900215b4925b4b8ed821000000000015975d0000000000000000],
##  ["pagano_19","Priest Leofdaeg","Leofdaeg",tf_hero|tf_guarantee_armor|tf_guarantee_boots, scn_town_23_castle|entry(11), reserved, fac_kingdom_9,[itm_briton_helm13, itm_bl_tunic02, itm_just_man_boots_light],def_attrib|level(5),wp(20),knows_common,0x0000000e5a0ce5d3190889284b6ed6d500000000001e68af0000000000000000],

###chief quest###
  ["local_merchant","Local Merchant","Local Merchants",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_bl_tunic02,itm_carbatinae_1,itm_knife],def_attrib|level(5),wp(40),knows_power_strike_1, man_face_middle_1, man_face_older_2],
  ["tax_rebel","Peasant Rebel","Peasant Rebels",tf_guarantee_armor,0,reserved,fac_commoners,
   []+basic_throwing+slings_common+common_shoes+common_phrygian+poor_tunic+basic_weapons2,
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],
  ["trainee_peasant","Peasant","Peasants",tf_guarantee_armor,0,reserved,fac_commoners,
  []+basic_throwing+common_tunic+basic_weapons+common_shoes2,
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],
  ["fugitive","Nervous Man","Nervous Men",tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor,0,0,fac_commoners,
 []+common_shoes2+common_hoodtunic+mercenaries_roundshields+light_spears+basic_seax,
   def_attrib|level(18),wp(140),knows_warrior_basic,man_face_younger_1, man_face_older_2],

#chief bounty termina   
  ["belligerent_drunk","Belligerent Drunk","Belligerent Drunks",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_tunic_with_green_cape,itm_hoodtunic_07,itm_btunic_13, itm_ptunic_6, itm_btunic_12, itm_carbatinae_1, itm_carbatinae_4,
    itm_carbatinae_vc4s, itm_carbatinae_vc4s, itm_phrygian13, itm_seax_5],
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],

  ["hired_assassin","Traveler","Hired Assassin",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners, #they look like belligerent drunks
   [itm_arena_tunic_white, itm_carbatinae_vc4s, itm_carbatinae_1, itm_carbatinae_4, itm_seax_1,itm_long_light_spear1,itm_hand_axe],
   def_attrib2|level(26),wp(240),knows_warrior_basic2,man_face_younger_1, man_face_older_2],

  ["fight_promoter","Rough-Looking Character","Rough-Looking Character",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_arena_tunic_blue,itm_linen_tunic,itm_bl_tunic01, itm_carbatinae_vc4s, itm_carbatinae_1, itm_carbatinae_4, itm_carbatinae_vc4s, itm_phrygian13, itm_spangenhelm_1, itm_hand_axe,itm_long_light_spear2],
   def_attrib2|level(23),wp(180),knows_warrior_basic2,man_face_younger_1, man_face_older_2],

   
   
  ["spy","Ordinary Townsman","Ordinary Townsmen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
   [itm_club_hard,itm_btunic_8,itm_carbatinae_1,itm_common_pony,itm_leather_gloves],
   def_attrib|agi_11|level(20),wp(130),knows_common,man_face_middle_1, man_face_older_2],
   
  ["spy_partner","Unremarkable Townsman","Unremarkable Townsmen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
   [itm_wooden_stick,itm_btunic_7,itm_carbatinae_1,itm_common_pony,itm_leather_gloves],
   def_attrib|agi_11|level(10),wp(130),knows_common,vaegir_face1, vaegir_face2],


	["camp_armory","Camp Armory","Camp Armory",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_inventory_management_10,0],


   ["nurse_for_lady","Nurse","Nurse",tf_female|tf_guarantee_armor,0,reserved,fac_commoners,
   [itm_woman_norse1, itm_carbatinae_vc4s],
   def_attrib|level(4),wp(60),knows_common,woman_face_1, woman_face_2],   
   ["temporary_minister","Minister","Minister",tf_guarantee_armor|tf_guarantee_boots,0,reserved,fac_commoners,
   [itm_btunic_6, itm_carbatinae_vc4s],
   def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_older_2],   
   
   
##  ["conspirator","Conspirator","Conspirators", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
##   [itm_sword,itm_btunic_16,itm_carbatinae_1,itm_hunter,itm_leather_gloves],
##   def_attrib|agi_11|level(10),wp(130),knows_common,vaegir_face1, vaegir_face2],
##  ["conspirator_leader","Conspirator","Conspirators", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
##   [itm_sword,itm_btunic_16,itm_carbatinae_1,itm_hunter,itm_leather_gloves],
##   def_attrib|agi_11|level(10),wp(130),knows_common,vaegir_face1, vaegir_face2],
##  ["peasant_rebel","Peasant Rebel","Peasant Rebels",tf_guarantee_armor,0,reserved,fac_peasant_rebels,
##   [itm_cleaver,itm_knife,itm_pitch_fork,itm_wooden_stick,itm_wooden_stick,itm_stones,itm_spangenhelm_1,itm_phrygian15,itm_phrygian15,itm_linen_tunic,itm_bl_tunic01,itm_carbatinae_1,itm_carbatinae_vc4s],
##   def_attrib|level(4),wp(60),knows_common,vaegir_face1, vaegir_face2],
##  ["noble_refugee","Noble Refugee","Noble Refugees",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_noble_refugees,
##   [itm_sword,itm_btunic_16,itm_carbatinae_1, itm_common_horse, itm_btunic_16, itm_spangenhelm_1],
##   def_attrib|level(9),wp(100),knows_common,swadian_face1, swadian_face2],
##  ["noble_refugee_woman","Noble Refugee Woman","Noble Refugee Women",tf_female|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_noble_refugees,
##   [itm_knife,itm_seax_1,itm_hunting_crossbow,itm_btunic_13,itm_robe,itm_lady_dress_ruby, itm_veil_f, itm_btunic_15, itm_carbatinae_vc4s],
##   def_attrib|level(3),wp(45),knows_common,refugee_face1,refugee_face2],


  # ["quick_battle_6_player", "{!}quick_battle_6_player", "{!}quick_battle_6_player", tf_hero, 0, reserved,  fac_player_faction, [itm_linen_tunic,itm_carbatinae_1, itm_carbatinae_11qs, itm_angle_helmet4, itm_long_war_spear1,  itm_long_bow, itm_arrows, itm_wooden_shield],    knight_attrib_1,wp(130),knight_skills_1, 0x000000000008010b01f041a9249f65fd],
   
#Multiplayer troops (they must have the base items only, nothing else)
  ["norse_multiplayer","Hirdman","Hirdmen",tf_guarantee_all,0,0,fac_culture_norse,
    [itm_carbatinae_vc1v,itm_btunic_9,itm_btunic_13,itm_wooden_stick],
    def_attrib_multiplayer|level(23),wpex(110,110,110,100,90,110),knows_warrior_basic, vaegir_face_young_1, vaegir_face_old_2],
  ["saxon_multiplayer","Geanata","Geanatas",tf_guarantee_all,0,0,fac_culture_saxon,
    [itm_carbatinae_5,itm_bl_tunic07,itm_bl_tunic11,itm_bl_tunic12,itm_wooden_stick],
    def_attrib_multiplayer|level(23),wpex(130,100,110,90,90,100),knows_warrior_basic, vaegir_face_young_1, vaegir_face_old_2],
  ["angle_multiplayer","Geanata","Geanatas",tf_guarantee_all,0,0,fac_culture_angle,
    [itm_carbatinae_11q,itm_carbatinae_12q,itm_ptunic_6,itm_ptunic_10,itm_gael_tunic_03,itm_wooden_stick],
    def_attrib_multiplayer|level(23),wpex(130,100,110,90,90,100),knows_warrior_basic, nord_face_young_1, nord_face_old_2],
  ["briton_multiplayer","Milwr","Milwyr",tf_guarantee_all,0,0,fac_culture_welsh,
    [itm_carbatinae_6s,itm_briton_tunic3,itm_briton_tunic4,itm_briton_tunic5,itm_wooden_stick],
    def_attrib_multiplayer|level(23),wpex(100,90,130,120,100,110),knows_warrior_basic,swadian_face_young_1, swadian_face_old_2],
  ["irish_multiplayer","Cliarthaire","Cliarthairi",tf_guarantee_all,0,0,fac_culture_irish,
    [itm_gaelshoes_1,itm_gaelshoes_2,itm_briton_tunic24,itm_briton_tunic25,itm_briton_tunic26,itm_briton_tunic27,itm_wooden_stick],
    def_attrib_multiplayer|level(23),wpex(90,120,110,110,110,130),knows_warrior_basic, rhodok_face_young_1, rhodok_face_old_2],
  ["scotch_multiplayer","Bruide","Bruides",tf_guarantee_all,0,0,fac_culture_scotch,
    [itm_bare_foot_man,itm_pictish_painted1,itm_pictish_painted2,itm_pictish_painted3,itm_wooden_stick],
    def_attrib_multiplayer|level(23),wpex(90,120,110,110,100,130),knows_warrior_basic, khergit_face_young_1, khergit_face_old_2],

#chief capitan
  ["norse_capitan", "Noble (Hersi)","Nobles (Hersir)", tf_mounted|tf_guarantee_all, 0, 0, fac_culture_norse,
    [itm_carbatinae_6,itm_btunic_12,itm_light_spear1,itm_knife,itm_common_pony],
    def_attrib_multiplayer|level(25),wpex(110,90,95,80,40,100),knows_warrior_normal,vaegir_face_middle_1, vaegir_face_older_2],
  ["norse_elite", "Elite Warrior (Huskarl)", "Elite Warriors (Huskarlar)", tf_guarantee_all, 0, 0, fac_culture_norse,
    [itm_carbatinae_6,itm_btunic_12,itm_light_spear1,itm_knife],
    def_attrib_multiplayer|level(29),wpex(150,110,130,100,50,140),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],

  ["saxon_capitan", "Noble (Thegn)","Nobles (Thegns)", tf_mounted|tf_guarantee_all, 0, 0, fac_culture_saxon,
    [itm_carbatinae_4s,itm_nobleman_outfit,itm_light_spear2,itm_seax_1,itm_common_pony2],
    def_attrib_multiplayer|level(25),wpex(100,70,120,70,60,110),knows_warrior_normal,vaegir_face_middle_1, vaegir_face_older_2],
  ["saxon_elite", "Bodyguard (Hearthweru)","Bodyguards (Hearthwerus)", tf_guarantee_all, 0, 0, fac_culture_saxon,
    [itm_carbatinae_4s,itm_nobleman_outfit,itm_light_spear2,itm_seax_1],
    def_attrib_multiplayer|level(29),wpex(140,90,170,90,80,150),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],

  ["angle_capitan", "Noble (Thegn)","Nobles (Thegns)", tf_mounted|tf_guarantee_all, 0, 0, fac_culture_angle,
    [itm_carbatinae_11q,itm_btunic_2woman,itm_light_spear2,itm_seax_1,itm_common_pony2],
    def_attrib_multiplayer|level(25),wpex(110,60,120,80,55,110),knows_warrior_normal,vaegir_face_middle_1, vaegir_face_older_2],
  ["angle_elite", "Bodyguard (Hearthweru)","Bodyguards (Hearthwerus)", tf_guarantee_all, 0, 0, fac_culture_angle,
    [itm_carbatinae_11q,itm_btunic_2woman,itm_light_spear2,itm_seax_1],
    def_attrib_multiplayer|level(29),wpex(150,80,170,100,70,150),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],

  ["briton_capitan", "Noble (Uchelwr)","Nobles (Uchelwyr)", tf_mounted|tf_guarantee_all, 0 ,0, fac_culture_welsh,
    [itm_carbatinae_3,itm_briton_tunic8,itm_long_light_spear1,itm_knife2,itm_common_horse],
    def_attrib_multiplayer|level(25),wpex(100,40,120,100,60,90),knows_warrior_normal,nord_face_middle_1, nord_face_older_2],
  ["briton_elite", "Champion (Campiwr)","Champions (Campgwr)", tf_guarantee_all, 0, 0, fac_culture_welsh,
    [itm_carbatinae_3,itm_briton_tunic8,itm_long_light_spear1,itm_knife2],
    def_attrib_multiplayer|level(29),wpex(140,50,170,140,80,120),knows_warrior_veteran,nord_face_middle_1, nord_face_older_2],

  ["irish_capitan", "Noble (Airig)","Nobles (Arras)", tf_mounted|tf_guarantee_all, 0, 0, fac_culture_irish,
    [itm_gaelshoes_1,itm_gaelshoes_2,itm_brat3,itm_brat4,itm_long_light_spear1,itm_knife3,itm_common_horse],
    def_attrib_multiplayer|level(25),wpex(110,40,120,60,60,130),knows_warrior_normal,rhodok_face_middle_1, rhodok_face_older_2],
  ["irish_elite", "Bodyguard (Deaisbard)","Bodyguard (Deaisbards)", tf_guarantee_all, 0, 0, fac_culture_irish,
    [itm_gaelshoes_1,itm_gaelshoes_2,itm_brat3,itm_brat4,itm_javelin_skirmishesel,itm_knife3],
    def_attrib_multiplayer|level(29),wpex(150,50,160,80,80,180),knows_warrior_veteran,rhodok_face_middle_1, rhodok_face_older_2],

  ["scotch_capitan", "Noble (Toisech)","Nobles (Toisechs)", tf_mounted|tf_guarantee_all, 0, 0, fac_culture_scotch,
    [itm_just_man_boots_medium,itm_picts_hoodtunic_13,itm_long_light_spear1,itm_knife4,itm_wild_pony],
    def_attrib_multiplayer|level(25),wpex(110,80,100,80,60,120),knows_warrior_normal,khergit_face_middle_1, khergit_face_older_2],
  ["scotch_elite", "Champion (Gaisgidh)","Champions (Gaisgidhs)", tf_guarantee_all, 0, 0, fac_culture_scotch,
    [itm_just_man_boots_medium,itm_picts_hoodtunic_13,itm_javelin_skirmishesel,itm_knife4],
    def_attrib_multiplayer|level(29),wpex(140,100,140,100,80,160),knows_warrior_veteran,khergit_face_middle_1, khergit_face_older_2],
#chief capitan acaba

  ["multiplayer_end","{!}multiplayer_end","{!}multiplayer_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],

  #replacable troop, not used
  ["nurse","Nurse","{!}nurse",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_woman_saxon8 ,    itm_carbatinae_1],     def_attrib|level(2),wp(50),knows_common, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  #erase later added to avoid errors
###fire arrow chief
##  ["global_value", "quick_battle_6_player", "quick_battle_6_player", tf_hero, 0, reserved,  fac_player_faction, [],    knight_attrib_1,wp(130),knight_skills_1, 0x000000000008010b01f041a9249f65fd],

#Player history array
  ["log_array_entry_type",            "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_bl_tunic02,itm_carbatinae_1,itm_knife],def_attrib|level(5),wp(40),knows_power_strike_1, man_face_middle_1, man_face_older_2],
  ["log_array_entry_time",            "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_bl_tunic02,itm_carbatinae_1,itm_knife],def_attrib|level(5),wp(40),knows_power_strike_1, man_face_middle_1, man_face_older_2],
  ["log_array_actor",                 "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_bl_tunic02,itm_carbatinae_1,itm_knife],def_attrib|level(5),wp(40),knows_power_strike_1, man_face_middle_1, man_face_older_2],
  ["log_array_center_object",         "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_bl_tunic02,itm_carbatinae_1,itm_knife],def_attrib|level(5),wp(40),knows_power_strike_1, man_face_middle_1, man_face_older_2],
  ["log_array_center_object_lord",    "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_bl_tunic02,itm_carbatinae_1,itm_knife],def_attrib|level(5),wp(40),knows_power_strike_1, man_face_middle_1, man_face_older_2],
  ["log_array_center_object_faction", "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_bl_tunic02,itm_carbatinae_1,itm_knife],def_attrib|level(5),wp(40),knows_power_strike_1, man_face_middle_1, man_face_older_2],
  ["log_array_troop_object",          "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_bl_tunic02,itm_carbatinae_1,itm_knife],def_attrib|level(5),wp(40),knows_power_strike_1, man_face_middle_1, man_face_older_2],
  ["log_array_troop_object_faction",  "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_bl_tunic02,itm_carbatinae_1,itm_knife],def_attrib|level(5),wp(40),knows_power_strike_1, man_face_middle_1, man_face_older_2],
  ["log_array_faction_object",        "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_bl_tunic02,itm_carbatinae_1,itm_knife],def_attrib|level(5),wp(40),knows_power_strike_1, man_face_middle_1, man_face_older_2],

  ["quick_battle_troop_1","Bodo the Cantabrian","Bodo the Cantabrian",tf_hero, 0, 0,  fac_culture_welsh,
    [itm_gambeson47,itm_carbatinae_11q,itm_shield_10,itm_javelin, itm_axe_3],
    str_10|agi_10|int_6|cha_8|level(26),wpex(109,33,132,15,32,100),
    knows_riding_1|knows_power_throw_4|knows_weapon_master_2|knows_power_strike_2|knows_ironflesh_2|knows_athletics_2|knows_shield_2|knows_trainer_2|knows_leadership_5,
    0x00000004b40c628d45188ce8ae8e592300000000001d9c9b0000000000000000],
  ["quick_battle_troop_2","Sven Bull Neck","Sven Bull Neck",tf_hero|tf_fat,0,0,fac_culture_norse,
    [itm_throwing_spears2,itm_carbatinae_5s,itm_byrnie22,itm_spangenhelm_1,itm_noble_sword_8,itm_long_heavy_spear2,itm_one_handed_war_axe_c,itm_viking_shield_round_04],
    def_attrib2|level(28),wpex(130,100,120,100,50,130),
    knows_warrior_elite,
    0x0000000fff11a10737135a153128b4db00000000001cc5140000000000000000],
  ["quick_battle_troop_3", "Cerball mac Dunlainge", "Cerball mac Dunlainge", tf_hero, 0, 0, fac_culture_irish,
    [itm_common_horse,itm_carbatinae_11qs,itm_mail_shirt_6,itm_leather_gloves,itm_noble_sword_11,itm_tab_shield_round_c,itm_briton_helm6],
    def_attrib_multiplayer|level(26),wpex(140,50,140,80,80,160),knows_warrior_elite, 
    0x0000000e0b103342779bc95727b1c8ed00000000001e295a0000000000000000],
  ["quick_battle_troop_4","Artorius","Artorius", tf_hero, 0, 0, fac_culture_welsh,
    [itm_arrows,itm_long_bow,itm_carbatinae_5s,itm_briton_helm33,itm_btunic_16,itm_leather_gloves,itm_long_war_spear2,itm_spatha_2],    
    def_attrib2|level(23),wpex(140,50,170,140,80,120),knows_weapon_master_7|knows_ironflesh_7|knows_athletics_6|knows_riding_7|knows_shield_3|knows_inventory_management_3|knows_power_strike_4|knows_power_draw_5|knows_power_throw_3,
    swadian_face_middle_1, swadian_face_older_2],
  ["quick_battle_troop_5", "Cinead","Cinead", tf_hero, 0, 0, fac_culture_scotch,
    [itm_common_pony,itm_just_man_boots_dark,itm_btunic_4,itm_spangenhelm_20,itm_javelin_jinetes,itm_long_light_spear1,itm_spatha_3],
    def_attrib_multiplayer|level(27),wpex(140,100,140,100,80,160),knows_weapon_master_7|knows_athletics_6|knows_riding_7|knows_shield_3|knows_inventory_management_3|knows_power_throw_4|knows_ironflesh_6|knows_power_strike_4,
    khergit_face_middle_1, khergit_face_older_2],
  ["quick_battle_troop_6", "Oswald","Oswald", tf_hero, 0, 0, fac_culture_saxon,
    [itm_carbatinae_5s,itm_mail_shirt_2,itm_spangenhelm_20,itm_long_light_spear1,itm_tab_shield_round_05_nodevice,itm_spatha_6,itm_throwing_spears2],
    def_attrib_multiplayer|level(29),wpex(140,90,170,90,80,150),knows_warrior_veteran,vaegir_face_middle_1, 
    vaegir_face_older_2],
  ["quick_battle_troop_7","Hildr","Hildr", tf_hero|tf_female|tf_tall,0,0,fac_culture_norse,
   [itm_arrows,itm_long_bow,itm_leather_gloves,itm_carbatinae_11qs,itm_linen_tunic,itm_long_light_spear2,itm_viking_shield_round_01],
   str_12|agi_15|int_12|cha_12|level(22),wpex(130,100,120,100,50,130),knows_warrior_veteran,
   0x000000061a0420043a83a5cb136d4ab500000000001da2ec0000000000000000],

  ["quick_battle_troops_cam","Camera","Camera", 0, 0, 0, fac_neutral, [], 0, 0, 0, 0, 0],
  ["quick_battle_troops_end","{!}quick_battle_troops_end","{!}quick_battle_troops_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],

  ["tutorial_fighter_1","Novice Warrior","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic,itm_carbatinae_1],
   def_attrib|level(1),wp(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x000000088c1073144252b1929a85569300000000000496a50000000000000000, vaegir_face_older_2],
  ["tutorial_fighter_2","Novice Warrior","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_ptunic_4,itm_carbatinae_2],
   def_attrib|level(1),wp(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x000000088b08049056ab56566135c46500000000001dda1b0000000000000000, vaegir_face_older_2],
  ["tutorial_fighter_3","Regular Warrior","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_ptunic_4,itm_carbatinae_3],
   def_attrib|level(9),wp(50),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x00000008bc00400654914a3b0d0de74d00000000001d584e0000000000000000, vaegir_face_older_2],
  ["tutorial_fighter_4","Veteran Warrior","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_ptunic_4,itm_carbatinae_4], #chief cambia for main quest
   def_attrib|level(16),wp(110),knows_athletics_1|knows_ironflesh_3|knows_power_strike_2|knows_shield_2,0x000000089910324a495175324949671800000000001cd8ab0000000000000000, vaegir_face_older_2],
  ["tutorial_archer_1","Archer","Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,
   [itm_btunic_10,itm_gambeson41,itm_carbatinae_5,itm_arena_helmet_yellow,itm_briton_helm9,itm_spangenhelm_1,itm_spangenhelm_1],
   def_attrib|str_12|level(19),wp(70)|wp_archery(90),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,vaegir_face_young_1, vaegir_face_older_2],
  ["tutorial_master_archer","Archery Trainer","Archery Trainer",tf_hero,0,0,fac_kingdom_2,
   [itm_btunic_11,itm_carbatinae_6],
   def_attrib|str_12|level(19),wp(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,0x0000000ea508540642f34d461d2d54a300000000001d5d9a0000000000000000, vaegir_face_older_2],
  ["tutorial_rider_1","Rider","{!}Vaegir Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_ptunic_4,itm_carbatinae_7,itm_common_pony2, itm_common_horse,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_riding_4|knows_shield_2|knows_ironflesh_3|knows_power_strike_2,vaegir_face_middle_1, vaegir_face_older_2],
  ["tutorial_rider_2","Horsewealas","{!}Khergit Horse Archers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_kingdom_3,
   [itm_ptunic_4,itm_ptunic_5,itm_carbatinae_8,itm_wooden_shield,itm_common_pony, itm_javelin],
   def_attrib|level(14),wp(80)|wp_archery(80),knows_riding_5|knows_power_draw_3|knows_ironflesh_1|knows_horse_archery_4|knows_power_throw_1,khergit_face_young_1, khergit_face_older_4],
  ["tutorial_master_horseman","Riding Trainer","Riding Trainer",tf_hero,0,0,fac_kingdom_2,
   [itm_btunic_16,itm_carbatinae_9],
   def_attrib|str_12|level(19),wp(70)|wp_archery(90),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,0x0000000ea0084140478a692894ba185500000000001d4af30000000000000000, vaegir_face_older_2],
   
#cambiado chief mercants   
  ["swadian_merchant", "Merchant", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_1, [itm_knife, itm_ptunic_4, itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common, 0x00000001870921d8585376b574d2d891000000000011ac240000000000000000],
  ["vaegir_merchant", "Merchant", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_2, [itm_knife, itm_long_tunic1, itm_carbatinae_vc4s], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["khergit_merchant", "Merchant", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_3, [itm_knife, itm_bl_tunic01, itm_carbatinae_1], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["nord_merchant", "Healer", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_4, [itm_robe10,], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2], #chief cambia para VC intro
  ["rhodok_merchant", "Merchant", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_5, [itm_knife, itm_btunic_8, itm_carbatinae_4], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["sarranid_merchant", "Merchant", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_6, [itm_knife, itm_btunic_9, itm_carbatinae_2], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],       
  ["startup_merchants_end","startup_merchants_end","startup_merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],
 ##grove quest old hero chief 
  ["old_hero_boargrove","Old Hero","Old Heroes",tf_alto|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged,0,0,fac_outlaws,
   []+javelin_normal+common_shoes4+common_horse+basic_seax2+common_sword2+saxons_elite_old_helmets+commonlong_mail+common_gloves+mercenaries_roundshields,
   def_attrib3|level(31),wp(380),knows_warrior_elite,man_face_younger_1, man_face_older_2],
  
###berserker
  ["sea_raider_leader","Berserkr","Berserkir",tf_alto|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_culture_norse,
   [itm_throwing_spears2,itm_throwing_spears]+common_gloves+war_norse_shoes3+bear_berserker+basic_longseaxnorse+twohanded_axes+noble_saxonvik_sword+berserkr_shields,
   str_27 | agi_15 | int_8 | cha_5|level(29),wpex(390,350,240,30,0,300)|wp_firearm(50),knows_weapon_master_9|knows_ironflesh_10|knows_athletics_8|knows_riding_2|knows_power_strike_8|knows_shield_3|knows_power_throw_6|knows_maintenance_5,nord_face_younger_1, nord_face_older_2],
#####Ulfhedinn
  ["looter_leader","Ulfhedinn","Ulfhednar",tf_alto|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_culture_norse,
  [itm_throwing_spears2,itm_throwing_spears]+war_norse_shoes2+wolf_berserker+basic_longseaxnorse2+common_axes4+noble_saxonvik_sword+berserkr_shields,
  str_25 | agi_17 | int_11 | cha_5|level(29),wpex(380,350,250,30,0,300)|wp_firearm(50),knows_weapon_master_9|knows_ironflesh_10|knows_athletics_7|knows_riding_2|knows_power_strike_9|knows_shield_3|knows_power_throw_7|knows_maintenance_5,nord_face_younger_1, nord_face_older_2],

###
###
  ["bandit_leaders_end","bandit_leaders_end","bandit_leaders_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],  

#use mainquest chief as Asturian captain in quest  
  ["relative_of_merchant", "Asturian Captain", "{!}Prominent",tf_hero|tf_guarantee_shield|tf_guarantee_ranged,0,0,fac_kingdom_2, # no use in VC, use for mainquest asturian army encounter
   [itm_javelin,itm_leather_gloves,
itm_carbatinae_6,itm_lamellar_armor,itm_spangenhelm_5,
itm_new_sword2,itm_seax_1,itm_viking_shield_round_02],
   def_attrib3|level(31),wp(380),knows_warrior_elite,man_face_younger_1, man_face_older_2],
   
  ["relative_of_merchants_end","relative_of_merchants_end","relative_of_merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],     
#####grueso chief empieza#############

####player lair staff chief
  ["sacerdote_lair","Priest Beda","priest",tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,
   [itm_priest1, itm_just_man_boots_light],def_attrib|level(5),wp(20),knows_common,0x00000009ff04e00e3ab34a3ad54956a300000000001cb2d80000000000000000],
  ["pagano_lair","Godi Olafr","priest",tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,
   [itm_robe6, itm_just_man_boots_light],def_attrib|level(5),wp(20),knows_common,0x0000000ff810e2931864a41b3432c91c00000000001da6230000000000000000],
  ["bardo_lair","Bard Siwi","bard",tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,
   [itm_bl_tunic03, itm_just_man_boots_light, itm_lute],def_attrib|level(5),wp(20),knows_common,0x0000000fec0451c0475aa2a4c9bc48a800000000001dca250000000000000000],
  ["skald_lair","Skald Bragi","bard",tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,
   [itm_bl_tunic02, itm_just_man_boots_light, itm_lute],def_attrib|level(5),wp(20),knows_common,0x000000002c045184475aa2a4c9bc48a800000000001dca250000000000000000],
  ["quastuosa_lair1","Suaibsech","quastuosa",tf_baja|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,
   [itm_gaeltunic_2woman, itm_just_man_boots_light],def_attrib|level(5),wp(20),knows_common,0x000000048000900624ddb1d75b7d653400000000001e6b1a0000000000000000],
  ["quastuosa_lair2","Tancoystl","quastuosa",tf_female|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,
   [itm_gaeltunic_1woman, itm_just_man_boots_light],def_attrib|level(5),wp(20),knows_common,0x0000000480000005450b0f48dd2568d600000000001deb740000000000000000],
  ["quastuosa_lair3","Gulla","quastuosa",tf_female|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,
   [itm_btunic_1woman, itm_just_man_boots_light],def_attrib|level(5),wp(20),knows_common,0x0000000199041002736b7b6b14cab89b00000000001a390d0000000000000000],
  ["quastuosa_lair4","Eadgyd","quastuosa",tf_alta|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,
   [itm_pict_long_tunic3, itm_just_man_boots_light],def_attrib|level(5),wp(20),knows_common,0x00000001ae10500129a5aeb52b3a186300000000001d44dc0000000000000000],
  ["lair_barber1","Aurelius","Aurelius",tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,
   [itm_robe4,itm_just_man_boots_medium],def_attrib|level(5),wp(20),knows_common,0x000000083e0040c649fc9e6f54b6dbbf00000000001d7b270000000000000000],
  ["lair_barber2","Morgan","Morgan",tf_bajo|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,
   [itm_robe5,itm_just_man_boots_medium],def_attrib|level(5),wp(20),knows_common,0x0000000dfe0040c649fc9e6f54b6dbbf00000000001d7b270000000000000000],
  ["lair_barber3","Alexander","Alexander",tf_alto|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,
   [itm_robe6,itm_just_man_boots_medium],def_attrib|level(5),wp(20),knows_common,0x0000000ffe0040c649fc9e6f54b6dbbf00000000001d7b270000000000000000],
  ["lair_barber4","Ailill","Ailill",tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,
   [itm_robe7,itm_just_man_boots_medium],def_attrib|level(5),wp(20),knows_common,0x0000000500003141355355370861008200000000001c96520000000000000000],
  ["cook_lair","Wamba","Cook",tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,
   [itm_hoodtunic_01, itm_just_man_boots_light],def_attrib|level(5),wp(20),knows_common,0x0000000a530854ce66d36db8dc66156300000000001e152a0000000000000000],
  ["lair_captain","Marcus","Lair Captains",tf_hero|tf_allways_fall_dead|tf_no_capture_alive, 0,reserved,  fac_commoners,
   [itm_mail_shirt_1, itm_carbatinae_1],str_30|agi_30|int_30|cha_30|level(40),wp(150),knows_common,0x0000000a1a00200336db6db6db6db6db00000000001db6db0000000000000000, 0x0000000a1a00200336db6db6db6db6db00000000001db6db0000000000000000],
### lair end
# followers camp
   ["mule_troop","The Frog","The Frog",tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_robe, itm_just_man_boots_light],def_attrib|level(5),wp(20),knows_common,0x0000000a530854ce66d36db8dc66156300000000001e152a0000000000000000],
 
##mainquest man of aelfred or halfdan
    ["leader_playerrf","Veteran","Veteran",tf_alto|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_outlaws,
   [itm_spatha,itm_long_light_spear1,itm_viking_shield_round_01,itm_javelin,itm_javelin,itm_byrnie,itm_carbatinae_1],
   def_attrib3|level(31),wp(380),knows_warrior_elite,man_face_younger_1, man_face_older_2],

## troops quest.
  ["mountain_bandit_leader","Wolf Heart","Wolf Heart",tf_alto|tf_guarantee_boots|tf_guarantee_armor|tf_randomize_face,0,0,fac_outlaws,
   []+javelin_normal+common_shoes4+common_horse+basic_seax2+special_sword_premium1+saxons_elite_old_helmets+frisiannoble_mail+common_gloves+mercenaries_roundshields,
   def_attrib3|level(31),wp(380),knows_warrior_elite,man_face_younger_1, man_face_older_2],
  ["last_druid","Druid","Druid",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_outlaws,
   [itm_robe7,itm_carbatinae_1], #quest
   def_attrib3|level(31),wp(380),knows_warrior_elite,0x0000000ff908935328e3b5289b572d2c00000000001e37730000000000000000],
  ["old_roman","Old Roman","Old Roman",tf_hero|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_outlaws,
   [itm_btunic_8,itm_carbatinae_1,itm_seax_1], #quest
   def_attrib|level(12),wp(100),knows_common,0x0000000f980485c536dcdb36ac4a632900000000001dc4cb0000000000000000],
  ["sea_raider_hero2","Captain Hero","Captain Hero",tf_alto|tf_randomize_face,0,0,fac_outlaws,
   []+javelin_normal+common_shoes4+common_horse+basic_seax3+common_sword2+saxons_elite_old_helmets+commonlong_mail+common_gloves+mercenaries_roundshields,
   def_attrib3|level(31),wp(380),knows_warrior_elite,man_face_younger_1, man_face_older_2],
  ["desert_bandit_hero","Bandit King","Bandits Kings",tf_alto|tf_guarantee_boots|tf_guarantee_armor|tf_randomize_face,0,0,fac_outlaws,
   []+common_gloves+elite_norse_boots+frisiannoble_mail+viking_elite_helmets+viking_elite_helmets_old2+basic_longseax+javelin_normal+special_sword_premium2+danish_roundshields,
   def_attrib3|level(31),wp(380),knows_warrior_veteran,nord_face_younger_1, nord_face_older_2],

  ["troll_bridge","Huge Man","Huge Man",tf_oso|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_outlaws,
   [itm_club_troll, itm_troll_tunic, itm_just_man_boots_medium], #quest
   def_attrib_troll|level(35),wp(400),knows_warrior_elite,0x00000000001050cc0a00fc7ffffc7fff00000000001df1ff0000000000000000],
  ["elf_riddles","Short Man","Short Man",tf_bajo|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_outlaws,
   [itm_seax_1, itm_gael_tunic_08, itm_gaelshoes_3], #quest
    def_attrib3|level(31),wp(380),knows_warrior_veteran,0x0000000e000475953c64528b6c8926dc00000000001ddd230000000000000000],

###mainquest chief asturians leaders
    ["silo_gallaecia","Comes Silo of Gallaecia","Silo of Gallaecia",tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_outlaws,
   [itm_throwing_spears,itm_arena_shield_green,itm_spatha_6,itm_seax_1,
    itm_spangenhelm_12,itm_carbatinae_11qs,itm_mail_shirt_8],
   def_attrib|level(42),wp(380),knows_warrior_elite,0x00000008de107308249488ea9a45ba91000000000005e84d0000000000000000],
  ["petrus_didaz","Dux Petrus Didaz","Dux Petro of Oveto",tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_outlaws,
   [itm_throwing_spears2,
itm_carbatinae_11q,itm_byrnie10,itm_spangenhelm_24, itm_seax_1,itm_spatha_6,itm_arena_shield_blue,],
   def_attrib|level(32),wp(220),knows_warrior_elite,0x0000000c0d104008584c2de3aa85b75100000000001f299b0000000000000000],
  ["gundinsalvo_cantabrian","Comes Gundinsalvo of Amaia","Comes Gundinsalvo of Amaia",tf_alto|tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_outlaws,
   [itm_throwing_spears,itm_sword_6,itm_seax_1, itm_briton_helm9,
     itm_leather_gloves,
itm_carbatinae_12qs,itm_byrnie11,itm_shield_10],
   def_attrib3|level(40),wp(300),knows_warrior_elite,0x0000000af90873cf45648ca75c7de65b0000000000129b540000000000000000],
#####

  #######grueso chief acaba
#Port Scenes
# ["port_chief", "Port Master", "Port Masters", tf_male|tf_hero|tf_is_merchant, 0, reserved, fac_neutral, [itm_carbatinae_2,itm_carbatinae_12qs, moved to shipwrights section
# itm_bl_tunic02,itm_linen_tunic,itm_bl_tunic02,itm_bl_tunic04,itm_bl_tunic04,itm_bl_tunic02], def_attrib|level(2), wp(20), knows_common,swadian_face_younger_1,swadian_face_middle_2],
 ["port_crew", "Old Sea Captain", "SR Captains", tf_hero, 0, reserved, fac_neutral,
  [itm_throwing_spears2,itm_throwing_spears2,
itm_carbatinae_11qs,itm_carbatinae_4,itm_byrnie11,itm_byrnie14,itm_byrnie8,
itm_spangenhelm_24,itm_spangenhelm_24,itm_briton_helm12,itm_spangenhelm_4,
 itm_seax_1,itm_one_handed_war_axe_c,itm_spatha_6,itm_sword_3,itm_viking_shield_round_12,itm_viking_shield_round_13],
   def_attrib2|level(26),wp(220),knows_warrior_normal,nord_face_younger_1, nord_face_older_2],
["port_pirate", "Slave Trader", "Slave Traders", tf_hero|tf_randomize_face, 0, reserved, fac_commoners, [itm_btunic_16,itm_carbatinae_3s], def_attrib|level(5), wp(20), knows_common,swadian_face_younger_1,swadian_face_middle_2],  

#people on sea (phaiak)
 ["fisher","Fisher","Fishers",tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_boots,no_scene,reserved,fac_commoners,
   [itm_stones, itm_bread, itm_bread, itm_smoked_fish, itm_cheese,
    itm_carbatinae_2,itm_carbatinae_3,itm_carbatinae_4,itm_carbatinae_5,
    itm_phrygian15,itm_phrygian14,itm_phrygian17,
itm_btunic_14,itm_btunic_15,itm_bl_tunic01,itm_bl_tunic02,itm_bl_tunic03,itm_bl_tunic04,
itm_seax_1,itm_wooden_stick],
   def_attrib|level(12),wp(100),knows_common,man_face_younger_1, man_face_older_2],

####Main quest pj chief. Personajes de la quest principal
####Mainquest pj chief. Personajes de la quest principal
    ["thiaderd","Thiaderd","Thiaderd",tf_alto|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_allways_fall_dead,0,0,fac_outlaws,
   [itm_spatha,itm_viking_shield_round_01,itm_javelin,itm_spangenhelm_24,itm_bl_tunic03,itm_carbatinae_11qs],
   def_attrib2|level(26),wp(220),knows_warrior_normal,0x000000049110738e58422de21c35a4b500000000001dd99c0000000000000000],
#prisoner to interrogate
    ["sea_raider_prisoner","Ship Captain","Captains",tf_guarantee_boots,0,0,fac_outlaws,
   [itm_carbatinae_4v,itm_saco_enlacabeza],
   def_attrib3|level(32),wp(260),knows_warrior_elite,0x0000000e061032c9431d8c469a6adaec00000000001d02de0000000000000000],

  ["doccinga_torturador","Torturer","Torturers",tf_hero|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_kingdom_1,
##  ["doccinga_torturador","Torturer","Torturers",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_carbatinae_2,itm_bl_tunic03, itm_wooden_stick,],
   def_attrib3|level(27),wp(200),knows_warrior_veteran, 0x00000001a400520836db6db6db6db6db00000000001db6db0000000000000000], #torturador, face done # Info: this is face key made by Asbjorn. Alberto, this is yours: 0x00000001aa08c6c747636a58d377375d00000000000e538c0000000000000000

    ["leader_svenlair","Harald","Captains",tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_outlaws,
   [itm_throwing_spears2,
itm_carbatinae_4v,
itm_byrnie22,itm_byrnie,itm_mail_shirt_1,itm_mail_shirt_4,itm_spangenhelm_1,itm_spangenhelm_2,itm_spangenhelm_5,
    itm_spangenhelm_3,itm_spangenhelm_4,itm_noble_sword_8,itm_spatha_4,itm_seax_1,itm_one_handed_war_axe_c,itm_viking_shield_round_04],
   def_attrib3|level(32),wp(380),knows_warrior_elite,0x00000001a010d2c558f3559d3265155100000000000bc51b0000000000000000],
###la del saco
  ["farmstead_prisoner","Prisoner","Prisoner",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_just_man_boots_light,
itm_woman_saxon8,itm_saco_enlacabeza],
   def_attrib|level(15),wp(60),knows_common,0x000000019b08e24857204b38e58558540000000000122d020000000000000000],
###hermano de sven
    ["sven_brother","Olvir White Hair","Olvir",tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_allways_fall_dead,0,0,fac_outlaws,
   [itm_throwing_spears2,
itm_carbatinae_14qv,
itm_byrnie23,itm_mail_shirt_4,itm_vikingold_elitehelm8,
    itm_spangenhelm_3,itm_spangenhelm_4,itm_sword_premium3,itm_seax_1,itm_viking_shield_round_04],
   def_attrib3|level(32),wp(400),knows_warrior_elite,0x0000000fc008078e2b657348d17b3ae300000000001e4b990000000000000000],
    ["atli_eiriksson","Atli Eiriksson","Atli",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_outlaws,
   [itm_throwing_spears2,
itm_carbatinae_14qv,
itm_addon_mail4,itm_spangenhelm_1,itm_spangenhelm_2,itm_spangenhelm_5,
    itm_spangenhelm_3,itm_vikingold_elitehelm9,itm_noble_sword_8,itm_spatha_4,itm_seax_1,itm_one_handed_war_axe_c,itm_viking_shield_round_04],
   def_attrib3|level(32),wp(400),knows_warrior_elite,0x0000000fff11a10737135a153128b4db00000000001cc5140000000000000000],
#Sven Bull Neck
      ["sven_bull_neck","Sven Bull Neck","Sven",tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_outlaws,
   [itm_throwing_spears2,
itm_carbatinae_14qv,
itm_byrnie20,itm_byrnie,itm_viking_noblehelm3,
    itm_sword_premium3,itm_seax_1,itm_viking_shield_round_04],
   def_attrib3|level(32),wp(400),knows_warrior_elite,0x0000000fff11a10737135a153128b4db00000000001cc5140000000000000000],

###### FAKE LORDS STORYLINE
##  ###fake bjorn storyline
##  ["knight_8_7fake", "Jarl Bjorn Ragnarsson", "Jarl Bjorn Jarnsida", tf_hero, 0, reserved,  fac_kingdom_8,
## [itm_common_pony,itm_carbatinae_12qs,itm_byrnie29,itm_leather_gloves,itm_noble_sword_3,itm_tab_shield_round_12_device,itm_viking_noblehelm1,itm_javelin,itm_longseax2,itm_trophy_b],
##   lord_attrib|level(32),wp(380),knows_lord_1,0x00000002fb04798838acb940946ca75a00000000001f54ee0000000000000000],
###################
  
  #intro barco en calma
    ["frisianship_merchant", "Captain", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_1, [itm_seax_1, itm_bl_tunic09, itm_carbatinae_12qs], def_attrib|level(2),wp(20),knows_common, 0x00000001a90921c24925cdb8e28adb5d00000000001658e20000000000000000],

  ["sailors","Woden Ric Sailor","Woden Ric Sailors",tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_boots,no_scene,reserved,fac_commoners,
   [itm_stones, itm_javelin,
itm_carbatinae_4,itm_carbatinae_5,itm_carbatinae_6,itm_carbatinae_vc1,itm_carbatinae_vc2,itm_carbatinae_vc3, #2 shoes
#    itm_phrygian15,itm_hood_02,itm_phrygian17,
itm_btunic_10,itm_btunic_9,itm_bl_tunic01,itm_bl_tunic02,itm_bl_tunic03,itm_bl_tunic04,
itm_seax_1,itm_wooden_stick],
   def_attrib|level(15),wp(110),knows_common,man_face_middle_1, man_face_old_2],
  ["mercenary_arqueros","Mercenary Archer","Mercenary Archers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   [itm_arrows,itm_long_bow,
    itm_carbatinae_2,itm_carbatinae_3,
itm_bl_tunic10,itm_btunic_4,
itm_seax_1],
   def_attrib2|level(19),wp_one_handed (60)|wp_polearm (60) |wp_archery(110),knows_archer_basic,mercenary_face_1, mercenary_face_2],

  ["bodo_falso","Bodo","Bodo",tf_hero, 0, reserved,  fac_commoners,[itm_ptunic_4,itm_carbatinae_11q,itm_javelin, itm_seax_1],
   str_10|agi_10|int_6|cha_8|level(17),wp(120),
   knows_warrior_veteran,
  0x00000004b40c628d45188ce8ae8e592300000000001d9c9b0000000000000000], #chief acabado

  ["your_tutorialwife","Mother","Mother",tf_hero|tf_female|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_commoners,
   [itm_stones,
 itm_just_man_boots_light,
itm_woman_saxon8,
    itm_knife],
   def_attrib|level(15),wp(60), knows_common, 0x0000000e160c10021ab16dd631b2b65c00000000001dd2a20000000000000000],
  ["your_motherold","Aged Mother","Aged Mother",tf_hero|tf_baja|tf_guarantee_armor|tf_guarantee_boots|tf_allways_fall_dead,0,0,fac_commoners,
   [itm_stones,
 itm_just_man_boots_light,
itm_woman_saxon8,
    itm_knife],
   def_attrib|level(15),wp(60), knows_common, 0x0000000fe308200029197a245bcd04d500000000001d42ec0000000000000000],

#granja  
    ["ulf_thefarmer", "Ulf", "{!}Prominent", tf_hero|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_kingdom_1, [itm_seax_1, itm_bl_tunic09, itm_carbatinae_12qs], def_attrib|level(2),wp(20),knows_common, 0x0000000dc40d22475863cab70225b8db00000000001e24a90000000000000000],

  ["hija_granja","Thora","Thora",tf_hero|tf_female|tf_guarantee_armor|tf_guarantee_boots,0,reserved,fac_kingdom_1,
   [itm_just_man_boots_light,
itm_woman_saxon9,
    itm_knife],
   def_attrib|level(15),wp(60), knows_common, 0x0000000011086013581e76d32d6dc8a400000000001dc7130000000000000000],

  ["orm_robagranjas","Orm Svarti","Orm Svarti",tf_hero|tf_alto|tf_guarantee_boots|tf_guarantee_armor|tf_randomize_face|tf_allways_fall_dead,0,reserved,fac_kingdom_1,
   [itm_throwing_spears,itm_shield_17,itm_noble_sword,itm_seax_1,
    itm_spangenhelm_12,itm_carbatinae_11qs,itm_orm_byrnie],
   def_attrib3|level(31),wp(380),knows_warrior_elite,nord_face_younger_1, nord_face_older_2],

# funeral
  ["pagano","Godi Olafr","Sacerdote",tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_robe7, itm_just_man_boots_light],def_attrib|level(5),wp(20),knows_common,0x0000000ff810e2931864a41b3432c91c00000000001da6230000000000000000],   
   
   ####personajes pj main quest acaba

# pseudo troops
  ["pseudo_troop_01","Gjalfrmarr","pt",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0], #economy logger (plural name)
  ["pseudo_troop_02","Eydendr","pt",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0], #player army logger (plural name)
  ["pseudo_troop_03","Gunnmas","pt",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0], #bandits logger (plural name)
  ["pseudo_troop_04","Sundvargs","pt",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
  ["pseudo_troop_05","Unnswin","pt",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
  ["pseudo_troop_06","Bengrefill","pt",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
  ["pseudo_troop_07","Elgslagar","pt",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
  ["pseudo_troop_08","Arajo","pt",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
  ["pseudo_troop_09","Byrskids","pt",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
  ["pseudo_troop_end","Second Outfit","pseudo_troop_end",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],  
  
###add-ons troops
    ["the_snake","The Snake","The Snake",tf_hero|tf_bajo|tf_guarantee_boots|tf_guarantee_armor|tf_randomize_face|tf_allways_fall_dead,0,reserved,fac_commoners,
   [itm_throwing_spears,itm_gael_bigroundshield_03,itm_championsword1,itm_seax_1,
    itm_crown1,itm_just_man_boots_light,itm_mail_shirt_12_1, itm_leather_gloves],
   def_attrib3|level(31),wp(380),knows_warrior_elite,rhodok_face_young_2, rhodok_face_old_2],

    ["campeon_1","Aed mac Ainmerech","Aed mac Ainmerech",tf_hero|tf_alto|tf_guarantee_boots|tf_guarantee_armor|tf_randomize_face|tf_allways_fall_dead,0,reserved,fac_commoners,
   [itm_throwing_spears,itm_gael_bigroundshield_02,itm_irish_long_sword3,itm_seax_1,
    itm_spangenhelm_40,itm_just_man_boots_medium,itm_byrnie36],
   def_attrib3|level(27),wp(280),knows_warrior_elite,rhodok_face_middle_1, rhodok_face_old_2],

  ["campeon_2","Olchobar mac Cinaeda","Olchobar mac Cinaeda",tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_randomize_face|tf_allways_fall_dead,0,reserved,fac_commoners,
   [itm_throwing_spears,itm_gael_bigroundshield_01,itm_irish_long_sword1,itm_seax_1,
    itm_just_man_boots_light,itm_gambeson13gael],
   def_attrib3|level(17),wp(280),knows_warrior_elite,rhodok_face_middle_1, rhodok_face_old_2],
  
  #["boar","Boar","Boar",0,no_scene,reserved,fac_neutral, [], def_attrib|level(1),wp(60),0,mercenary_face_1, mercenary_face_2],
  ["slave","Slave","Slaves",0,no_scene,reserved,fac_commoners,
   []+basic_throwing+poor_tunic2+basic_weapons,
   def_attrib|level(7),wp(70),knows_common,man_face_younger_1, man_face_older_2],
  ["morrigan_npc","Morrigan","Morrigan",tf_hero|tf_female|tf_guarantee_armor|tf_guarantee_boots|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,
   [itm_just_man_boots_light,
itm_btunic_8,
    itm_knife],
   def_attrib3|level(17),wp(280),knows_warrior_elite, 0x000000000f00300626922db55a4e475a00000000001d272d0000000000000000], 
 ["dog","Dog","Dogs",tf_hero|tf_undead|tf_guarantee_all,0,0,fac_commoners,
    [itm_dog_companion_horse, itm_dog_bite], level(10)|str_5|agi_5, wp_polearm(50),knows_ironflesh_2|knows_riding_3, 0, 0],
    ["caliacas_son","Bran mac Caliacas","Bran mac Caliacas",tf_mounted|tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_commoners,
   [itm_wild_pony,itm_knife5,itm_irish_long_sword4,itm_small_roundsh2,itm_javelin,itm_angle_helmet5,itm_celta_capa1,itm_gaelshoes_1],
   def_attrib3|level(31),wp(380),knows_warrior_elite,0x000000003f04000c16a488c6e16538ec00000000001f185c0000000000000000],
    ["maelbresail_man","Fergus mac Cormaic","Fergus mac Cormaic",tf_guarantee_boots|tf_guarantee_armor|tf_randomize_face|tf_allways_fall_dead,0,reserved,fac_commoners,
   [itm_throwing_spears,itm_championsword1,itm_seax_1,
    itm_briton_helm33,itm_just_man_boots_medium,itm_mail_shirt_12_2],
   def_attrib3|level(27),wp(280),knows_warrior_elite,rhodok_face_middle_1, rhodok_face_old_2],
  ["maelbressail_nother","Mael Bresail's Mother","Mael Bresail's Mother",tf_baja|tf_guarantee_armor|tf_guarantee_boots|tf_allways_fall_dead,0,0,fac_commoners,
   [ itm_just_man_boots_light,
itm_pict_long_tunic2,
    itm_knife],
   def_attrib|level(15),wp(60), knows_common, 0x0000000fff04000437326cd6958efb9300000000001d498c0000000000000000],

   
###MP ADDON PLAYER TROOPS
##MP RAID peasant troops
  ["mp_norse_peasant","Peasant","Peasant",tf_guarantee_all,0,0,fac_culture_norse,
   [itm_carbatinae_6,itm_btunic_9,itm_btunic_13,itm_wooden_stick],
   def_attrib|level(12),wpex(100,100,100,50,20,95)|wp_firearm(95),knows_common,nord_face_younger_1, nord_face_older_2],
  ["mp_saxon_peasant","Peasant","Peasant",tf_guarantee_all,0,0,fac_culture_saxon,
   [itm_carbatinae_4s,itm_carbatinae_5s,itm_bl_tunic11,itm_bl_tunic07,itm_bl_tunic12,itm_wooden_stick],
   def_attrib|level(12),wpex(110,70,100,50,20,110)|wp_firearm(90),knows_common,vaegir_face_younger_1, vaegir_face_older_2],
  ["mp_angle_peasant","Peasant","Peasant",tf_guarantee_all,0,0,fac_culture_angle,
   [itm_carbatinae_6,itm_carbatinae_1s,itm_carbatinae_10,itm_ptunic_10,itm_ptunic_6,itm_gael_tunic_03,itm_wooden_stick],
   def_attrib|level(12),wpex(105,70,100,50,20,105)|wp_firearm(95),knows_common,vaegir_face_younger_1, vaegir_face_older_2],
  ["mp_briton_peasant","Peasant","Peasant",tf_guarantee_all,0,0,fac_culture_welsh,
   [itm_carbatinae_1,itm_carbatinae_3,itm_carbatinae_4,itm_carbatinae_8,itm_briton_tunic4,itm_briton_tunic3,itm_briton_tunic5,itm_wooden_stick],
   def_attrib|level(12),wpex(100,90,90,50,20,110)|wp_firearm(110),knows_common,swadian_face_younger_1, swadian_face_older_2],
  ["mp_irish_peasant","Peasant","Peasant",tf_guarantee_all,0,0,fac_culture_irish,
   [itm_bare_foot_man,itm_briton_tunic25,itm_briton_tunic24,itm_briton_tunic26,itm_briton_tunic27,itm_wooden_stick],
   def_attrib|level(12),wpex(100,70,100,20,20,115)|wp_firearm(100),knows_common,rhodok_face_younger_1, rhodok_face_older_2],
  ["mp_scotch_peasant","Peasant","Peasant",tf_guarantee_all,0,0,fac_culture_scotch,
   [itm_bare_foot_man,itm_pictish_painted2,itm_pictish_painted1,itm_pictish_painted3,itm_briton_tunic17,itm_wooden_stick],
   def_attrib|level(12),wpex(100,70,70,20,40,105)|wp_firearm(105),knows_common,khergit_face_younger_1, khergit_face_older_2],

###MP classes
  ["mp_norse_infantry","Norse Infantry","_",tf_guarantee_all,0,0,fac_culture_norse,
    [itm_carbatinae_6,itm_btunic_9,itm_btunic_13,itm_wooden_stick],
    def_attrib_multiplayer|level(20),wpex(110,110,110,70,70,110)|wp_firearm(80),knows_ironflesh_4|knows_power_strike_5|knows_power_throw_4|knows_athletics_6|knows_shield_3|knows_riding_1, vaegir_face_young_1, vaegir_face_old_2],
  ["mp_norse_archer","Norse Archer","_",tf_guarantee_all,0,0,fac_culture_norse,
    [itm_carbatinae_6,itm_btunic_9,itm_btunic_13,itm_wooden_stick,itm_stones],
    def_attrib_multiplayer|level(20),wpex(80,70,80,140,130,90)|wp_firearm(100),knows_ironflesh_2|knows_power_strike_2|knows_shield_2|knows_power_draw_5|knows_athletics_4|knows_riding_1|knows_power_throw_1, vaegir_face_young_1, vaegir_face_old_2],
  ["mp_norse_cavalry","Norse Cavalry","_",tf_guarantee_all,0,0,fac_culture_norse,
    [itm_carbatinae_6,itm_btunic_13,itm_btunic_9,itm_wooden_stick,itm_staff,itm_common_pony2],
    def_attrib_multiplayer|level(20),wpex(100,100,110,80,70,110)|wp_firearm(80),knows_riding_4|knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_horse_archery_2|knows_power_throw_3|knows_athletics_3, vaegir_face_young_1, vaegir_face_old_2],

  ["mp_saxon_infantry","Saxon Infantry","_",tf_guarantee_all,0,0,fac_culture_saxon,
    [itm_carbatinae_4s,itm_bl_tunic07,itm_bl_tunic11,itm_bl_tunic12,itm_wooden_stick],
    def_attrib_multiplayer|level(20),wpex(130,100,110,60,60,100)|wp_firearm(80),knows_ironflesh_4|knows_power_strike_5|knows_power_throw_4|knows_athletics_6|knows_shield_3|knows_riding_1, vaegir_face_young_1, vaegir_face_old_2],
  ["mp_saxon_archer","Saxon Archer","_",tf_guarantee_all,0,0,fac_culture_saxon,
    [itm_carbatinae_4s,itm_carbatinae_5s,itm_bl_tunic11,itm_bl_tunic07,itm_bl_tunic12,itm_wooden_stick,itm_stones],
    def_attrib_multiplayer|level(20),wpex(90,70,80,130,130,80)|wp_firearm(100),knows_ironflesh_2|knows_power_strike_2|knows_shield_2|knows_power_draw_5|knows_athletics_4|knows_riding_1|knows_power_throw_1, vaegir_face_young_1, vaegir_face_old_2],
  ["mp_saxon_cavalry","Saxon Cavalry","_",tf_guarantee_all,0,0,fac_culture_saxon,
    [itm_carbatinae_4s,itm_bl_tunic12,itm_bl_tunic07,itm_bl_tunic11,itm_wooden_stick,itm_quarter_staff,itm_common_pony],
    def_attrib_multiplayer|level(20),wpex(110,80,110,60,60,100)|wp_firearm(80),knows_riding_4|knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_horse_archery_2|knows_power_throw_3|knows_athletics_3, vaegir_face_young_1, vaegir_face_old_2],

  ["mp_angle_infantry","Angle Infantry","_",tf_guarantee_all,0,0,fac_culture_angle,
    [itm_carbatinae_11q,itm_ptunic_6,itm_ptunic_10,itm_gael_tunic_03,itm_wooden_stick],
    def_attrib_multiplayer|level(20),wpex(130,100,110,60,60,100)|wp_firearm(80),knows_ironflesh_4|knows_power_strike_5|knows_power_throw_4|knows_athletics_6|knows_shield_3|knows_riding_1, nord_face_young_1, nord_face_old_2],
  ["mp_angle_archer","Angle Archer","_",tf_guarantee_all,0,0,fac_culture_angle,
    [itm_carbatinae_1s,itm_carbatinae_11q,itm_ptunic_10,itm_ptunic_6,itm_gael_tunic_03,itm_wooden_stick,itm_stones],
    def_attrib_multiplayer|level(20),wpex(90,70,80,130,130,80)|wp_firearm(100),knows_ironflesh_2|knows_power_strike_2|knows_shield_2|knows_power_draw_5|knows_athletics_4|knows_riding_1|knows_power_throw_1, nord_face_young_1, nord_face_old_2],
  ["mp_angle_cavalry","Angle Cavalry","_",tf_guarantee_all,0,0,fac_culture_angle,
    [itm_carbatinae_11q,itm_gael_tunic_03,itm_ptunic_6,itm_ptunic_10,itm_wooden_stick,itm_quarter_staff,itm_common_pony],
    def_attrib_multiplayer|level(20),wpex(110,80,110,60,60,100)|wp_firearm(80),knows_riding_4|knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_horse_archery_2|knows_power_throw_3|knows_athletics_3, nord_face_young_1, nord_face_old_2],
  
  ["mp_briton_infantry","Brittonic Infantry","_",tf_guarantee_all,0,0,fac_culture_welsh,
    [itm_carbatinae_3,itm_briton_tunic3,itm_briton_tunic4,itm_briton_tunic5,itm_wooden_stick],
    def_attrib_multiplayer|level(20),wpex(100,90,130,60,60,110)|wp_firearm(90),knows_ironflesh_4|knows_power_strike_5|knows_power_throw_4|knows_athletics_6|knows_shield_3|knows_riding_1,swadian_face_young_1, swadian_face_old_2],
  ["mp_briton_archer","Brittonic Archer","_",tf_guarantee_all,0,0,fac_culture_welsh,
    [itm_carbatinae_3,itm_carbatinae_4,itm_briton_tunic4,itm_briton_tunic3,itm_briton_tunic5,itm_wooden_stick,itm_sling_rock1,itm_sling3],
    def_attrib_multiplayer|level(20),wpex(90,80,80,140,130,80)|wp_firearm(120),knows_ironflesh_2|knows_power_strike_2|knows_shield_2|knows_power_draw_5|knows_athletics_4|knows_riding_1|knows_power_throw_1,swadian_face_young_1, swadian_face_old_2],
  ["mp_briton_cavalry","Brittonic Cavalry","_",tf_guarantee_all,0,0,fac_culture_welsh,
    [itm_carbatinae_3,itm_briton_tunic5,itm_briton_tunic4,itm_briton_tunic3,itm_wooden_stick,itm_quarter_staff,itm_common_pony2],
    def_attrib_multiplayer|level(20),wpex(90,80,130,60,60,110)|wp_firearm(90),knows_riding_4|knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_horse_archery_2|knows_power_throw_3|knows_athletics_3,swadian_face_young_1, swadian_face_old_2],
  
  ["mp_irish_infantry","Goidelic Infantry","_",tf_guarantee_all,0,0,fac_culture_irish,
    [itm_gaelshoes_1,itm_gaelshoes_2,itm_briton_tunic24,itm_briton_tunic25,itm_briton_tunic26,itm_briton_tunic27,itm_wooden_stick],
    def_attrib_multiplayer|level(20),wpex(90,120,110,80,80,130)|wp_firearm(80),knows_ironflesh_4|knows_power_strike_5|knows_power_throw_4|knows_athletics_6|knows_shield_3|knows_riding_1, rhodok_face_young_1, rhodok_face_old_2],
  ["mp_irish_archer","Goidelic Archer","_",tf_guarantee_all,0,0,fac_culture_irish,
    [itm_bare_foot_man,itm_briton_tunic25,itm_briton_tunic24,itm_briton_tunic26,itm_briton_tunic27,itm_wooden_stick,itm_stones],
    def_attrib_multiplayer|level(20),wpex(80,80,90,140,140,90)|wp_firearm(100),knows_ironflesh_2|knows_power_strike_2|knows_shield_2|knows_power_draw_5|knows_athletics_4|knows_riding_1|knows_power_throw_1, rhodok_face_young_1, rhodok_face_old_2],
  ["mp_irish_cavalry","Goidelic Cavalry","_",tf_guarantee_all,0,0,fac_culture_irish,
    [itm_gaelshoes_2,itm_gaelshoes_1,itm_briton_tunic26,itm_briton_tunic24,itm_briton_tunic25,itm_briton_tunic27,itm_wooden_stick,itm_quarter_staff,itm_common_pony],
    def_attrib_multiplayer|level(20),wpex(80,100,110,80,80,130)|wp_firearm(80),knows_riding_4|knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_horse_archery_2|knows_power_throw_3|knows_athletics_3, rhodok_face_young_1, rhodok_face_old_2],
  
  ["mp_scotch_infantry","Pictish Infantry","_",tf_guarantee_all,0,0,fac_culture_scotch,
    [itm_bare_foot_man,itm_pictish_painted1,itm_pictish_painted2,itm_pictish_painted3,itm_briton_tunic17,itm_wooden_stick],
    def_attrib_multiplayer|level(20),wpex(90,120,110,80,70,130)|wp_firearm(80),knows_ironflesh_4|knows_power_strike_5|knows_power_throw_4|knows_athletics_6|knows_shield_3|knows_riding_1, khergit_face_young_1, khergit_face_old_2],
  ["mp_scotch_archer","Pictish Archer","_",tf_guarantee_all,0,0,fac_culture_scotch,
    [itm_bare_foot_man,itm_pictish_painted2,itm_pictish_painted1,itm_pictish_painted3,itm_briton_tunic17,itm_wooden_stick,itm_stones],
    def_attrib_multiplayer|level(20),wpex(80,90,80,140,130,80)|wp_firearm(100),knows_ironflesh_2|knows_power_strike_2|knows_shield_2|knows_power_draw_5|knows_athletics_4|knows_riding_1|knows_power_throw_1, khergit_face_young_1, khergit_face_old_2],
  ["mp_scotch_cavalry","Pictish Cavalry","_",tf_guarantee_all,0,0,fac_culture_scotch,
    [itm_bare_foot_man,itm_pictish_painted3,itm_pictish_painted1,itm_pictish_painted2,itm_briton_tunic17,itm_wooden_stick,itm_quarter_staff,itm_wild_pony],
    def_attrib_multiplayer|level(20),wpex(80,100,110,80,70,130)|wp_firearm(80),knows_riding_4|knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_horse_archery_2|knows_power_throw_3|knows_athletics_3, khergit_face_young_1, khergit_face_old_2],

  ["mp_addon_player_troops_end","{!}addon_player_troops_end","{!}addon_player_troops_end", 0, 0, 0, 0, [], 0, 0, 0, 0, 0],
##MP raid AI
  ["norse_peasant_ai","Norse Freedman (Leysingi)","Norse Freedmen (Leysingja)",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_norse,
   []+basic_throwing+basic_weapons+poor_tunic2+common_shoes+common_phrygian,
   def_attrib|level(12),wpex(100,100,100,50,20,95)|wp_firearm(95),knows_common,nord_face_younger_1, nord_face_older_2],
  ["saxon_peasant_ai","Saxon Peasant (Gebur)","Peasants (Geburas)",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_saxon,
   []+basic_throwing+basic_weapons+poor_tunic2+common_shoes,
   def_attrib|level(12),wpex(110,70,100,50,20,110)|wp_firearm(90),knows_common,vaegir_face_younger_1, vaegir_face_older_2],
  ["angle_peasant_ai","Angle Peasant (Gebur)","Peasants (Geburas)",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_angle,
   []+basic_throwing+basic_weapons2+poor_tunic2+common_shoes3,
   def_attrib|level(12),wpex(105,70,100,50,20,105)|wp_firearm(95),knows_common,vaegir_face_younger_1, vaegir_face_older_2],
  ["briton_peasant_ai","Briton Serf (Aillt)","Briton Serfs (Aillts)",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_welsh,
   []+basic_throwing+basic_weapons2+briton_tunic+common_shoes,
   def_attrib|level(12),wpex(100,90,90,50,20,110)|wp_firearm(110),knows_common,swadian_face_younger_1, swadian_face_older_2],
  ["irish_peasant_ai","Irish Serf (Senchleithe)","Irish Serfs (Senchleithe)",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_irish,
   []+basic_throwing+basic_weapons2+irish_tunic+irish_shoes,
   def_attrib|level(12),wpex(100,70,100,20,20,115)|wp_firearm(100),knows_common,rhodok_face_younger_1, rhodok_face_older_2],
  ["scotch_peasant_ai","Pictish Peasant (Bachlach)","Peasants (Bachlach)",tf_guarantee_armor,0,0,fac_culture_scotch,
   []+basic_throwing+basic_weapons2+pictish_tunic+pictish_shoes,
   def_attrib|level(12),wpex(100,70,70,20,40,105)|wp_firearm(105),knows_common,khergit_face_younger_1, khergit_face_older_2],

###weak berserker
  ["fake_berserker","Berserkr","Berserkir",tf_alto|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_culture_norse,
   [itm_throwing_spears2,itm_throwing_spears]+war_norse_shoes3+bear_berserker+wolf_berserker+basic_longseaxnorse+twohanded_axes+common_axes4+berserkr_shields,
   str_14 | agi_10 | int_6 | cha_4|level(18),wpex(190,150,140,30,0,100)|wp_firearm(50),knows_weapon_master_4|knows_ironflesh_4|knows_athletics_4|knows_riding_2|knows_power_strike_2|knows_shield_2|knows_power_throw_3|knows_maintenance_5,nord_face_younger_1, nord_face_older_2],

   ["reuse1","{!}troops_end","{!}troops_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],
   ["reuse2","{!}troops_end","{!}troops_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],
   ["reuse3","{!}troops_end","{!}troops_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],
   ["reuse4","{!}troops_end","{!}troops_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],
   ["reuse5","{!}troops_end","{!}troops_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],
   ["reuse6","{!}troops_end","{!}troops_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],
   ["reuse7","{!}troops_end","{!}troops_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],
   ["reuse8","{!}troops_end","{!}troops_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],
   ["reuse9","{!}troops_end","{!}troops_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],
   ["reuse10","{!}troops_end","{!}troops_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],
   ["reuse11","{!}troops_end","{!}troops_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],
   ["reuse12","{!}troops_end","{!}troops_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],
   ["reuse13","{!}troops_end","{!}troops_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],
   ["reuse14","{!}troops_end","{!}troops_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],
   ["reuse15","{!}troops_end","{!}troops_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],
   ["reuse16","{!}troops_end","{!}troops_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],
   ["troops_end","{!}troops_end","{!}troops_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],
]


#Troop upgrade declarations
#common and mercenaries
upgrade2(troops,"slave","farmer","looter")	#new
upgrade2(troops,"farmer","watchman","todos_cuerno")
upgrade2(troops,"townsman","watchman","todos_cuerno")
upgrade(troops,"watchman","caravan_guard")
upgrade(troops,"caravan_guard","mercenary_swordsman")
#upgrade(troops,"mercenary_horseman","mercenary_cavalry") 
#britons
upgrade2(troops,"briton_slave","briton_level0_landed","briton_bowman")

upgrade2(troops,"briton_level0_landed","briton_level1_landed","briton_level0_companion")
upgrade2(troops,"briton_level1_landed","briton_level2_landed","briton_standard_bearer")
upgrade(troops,"briton_level2_landed","briton_level3_landed")
upgrade(troops,"briton_level0_companion","briton_level1_companion")
upgrade2(troops,"briton_bowman","briton_marksman","briton_horseman")
upgrade(troops,"briton_level1_companion","briton_level2_companion")

#upgrade(troops,"briton_horseman","briton_knight")
#saxons
upgrade2(troops,"saxon_slave","saxon_level0_landed","saxon_bowman")
upgrade2(troops,"saxon_level0_landed","saxon_level1_landed","saxon_level0_companion")

upgrade2(troops,"saxon_level1_landed","saxon_level2_landed","saxon_horseman")
upgrade(troops,"saxon_level2_landed","saxon_level3_landed")

upgrade2(troops,"saxon_level0_companion","saxon_level1_companion","saxon_standard_bearer")

upgrade(troops,"saxon_level1_companion","saxon_level2_companion")
#norse
upgrade2(troops,"norse_slave","norse_level0_landed","norse_bowman")
upgrade2(troops,"norse_level0_landed","norse_level1_landed","norse_level0_companion")
upgrade(troops,"norse_bowman","norse_elitearcher")

upgrade2(troops,"norse_level1_landed","norse_level2_landed","norse_standard_bearer")

upgrade(troops,"norse_level2_landed","norse_level3_landed")

upgrade(troops,"norse_level0_companion","norse_level1_companion")

upgrade(troops,"norse_level1_companion","norse_level2_companion")
#pictish
upgrade2(troops,"scotch_peasant","scotch_level0_landed","scotch_bowman")
upgrade2(troops,"scotch_level0_landed","scotch_level1_landed","scotch_level0_companion")
upgrade2(troops,"scotch_level1_landed","scotch_level2_landed","scotch_standard_bearer")
upgrade(troops,"scotch_level2_landed","scotch_knight")
upgrade(troops,"scotch_level0_companion","scotch_level1_companion")
upgrade(troops,"scotch_level1_companion","scotch_level2_companion")

upgrade(troops,"scotch_bowman","scotch_level0_skirmisher")
upgrade2(troops,"scotch_level0_skirmisher","scotch_level1_skirmisher","scotch_horseman")
#angles
upgrade2(troops,"angle_slave","angle_level0_landed","angle_bowman")
upgrade2(troops,"angle_level0_landed","angle_level1_landed","angle_level0_companion")
upgrade2(troops,"angle_level1_landed","angle_level2_landed","angle_horseman")
upgrade(troops,"angle_level2_landed","angle_level3_landed")
upgrade2(troops,"angle_level0_companion","angle_level1_companion","angle_standard_bearer")
upgrade(troops,"angle_level1_companion","angle_level2_companion")
#irish
upgrade2(troops,"irish_slave","irish_level0_landed","irish_bowman")
upgrade2(troops,"irish_level0_landed","irish_level1_landed","irish_level0_companion")
upgrade2(troops,"irish_level1_landed","irish_level2_landed","irish_standard_bearer")
upgrade(troops,"irish_level0_companion","irish_level1_companion")
upgrade(troops,"irish_level1_companion","irish_knight")
  
upgrade(troops,"irish_bowman","irish_level0_skirmisher")
upgrade2(troops,"irish_level0_skirmisher","irish_level1_skirmisher","irish_horseman")

upgrade(troops,"irish_level2_landed","irish_level3_landed")
#bandits
upgrade2(troops,"looter", "bandit", "forest_bandit")
upgrade2(troops,"bandit","mountain_bandit", "brigand")
upgrade(troops,"brigand","sea_raider")
upgrade(troops,"mountain_bandit","desert_bandit")

upgrade(troops,"manhunter","slave_hunter")

#slavers
upgrade(troops,"slave_driver","slave_hunter")
upgrade(troops,"slave_hunter","slave_crusher")
upgrade(troops,"slave_crusher","slaver_chief")
#chief TROOP UPGRADES BEGIN
#upgrade2(troops,"shepherd", "watchman","mercenary_crossbowman")
upgrade2(troops,"frisian_basic","frisian_mid","frisian_cav")
upgrade(troops,"frisian_mid","frisian_heavy")
#frisios chief acaba

upgrade(troops,"refugee","follower_woman")
upgrade(troops,"peasant_woman","follower_woman")
upgrade(troops,"follower_woman","hunter_woman")
upgrade(troops,"hunter_woman","fighter_woman")
upgrade(troops,"fighter_woman","sword_sister")
upgrade(troops,"fisher","regular_sailors")
