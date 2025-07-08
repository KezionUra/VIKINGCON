from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_map_icons import *

pmf_is_prisoner = 0x0001

####################################################################################################################
#  Each party template record contains the following fields:
#  1) Party-template id: used for referencing party-templates in other files.
#     The prefix pt_ is automatically added before each party-template id.
#  2) Party-template name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Faction
#  6) Personality. See header_parties.py for an explanation of personality flags.
#  7) List of stacks. Each stack record is a tuple that contains the following fields:
#    7.1) Troop-id. 
#    7.2) Minimum number of troops in the stack. 
#    7.3) Maximum number of troops in the stack. 
#    7.4) Member flags(optional). Use pmf_is_prisoner to note that this member is a prisoner.
#     Note: There can be at most 6 stacks.
####################################################################################################################


party_templates = [
  ("none","none",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("rescued_prisoners","Rescued Prisoners",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("enemy","Enemy",icon_gray_knight,0,fac_undeads,merchant_personality,[]),
  ("hero_party","Hero Party",icon_lords_1,0,fac_commoners,merchant_personality,[]),
####################################################################################################################
# Party templates before this point are hard-wired into the game and should not be changed. 
####################################################################################################################
##  ("old_garrison","Old Garrison",icon_vaegir_knight,0,fac_neutral,merchant_personality,[]),
  ("village_defenders","Village Defenders",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,10,20),(trp_peasant_woman,0,8)]),

  ("cattle_herd","Cattle Herd",icon_cattle|carries_goods(10),0,fac_neutral,merchant_personality,[(trp_cattle,80,120)]),

##  ("vaegir_nobleman","Vaegir Nobleman",icon_vaegir_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_vaegir_knight,2,6),(trp_vaegir_horseman,4,12)]),
##  ("swadian_nobleman","Swadian Nobleman",icon_gray_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_swadian_knight,2,6),(trp_swadian_man_at_arms,4,12)]),

# spawned parties should have minimum for starting player and maximum set for end of game player
# party size limited at any point by script_update_party_creation_random_limits
# Ryan BEGIN
  ("looters","Thieves",icon_warriors_3|carries_goods(8),0,fac_outlaws,bandit_personality,[(trp_looter,3,180)]), #chief cambiado
# Ryan END
  ("manhunters","Young Warriors",icon_warriors_4,0,fac_manhunters,soldier_personality,[(trp_manhunter,12,120)]), #chief cambiado
##  ("peasant","Peasant",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,1,6),(trp_peasant_woman,0,7)]),

#  ("black_khergit_raiders","Black Khergit Raiders",icon_khergit_horseman_b|carries_goods(2),0,fac_black_khergits,bandit_personality,[(trp_black_khergit_guard,1,10),(trp_elite_viking,5,5)]),
  # ("steppe_bandits","Northmenn",icon_warriors_2|carries_goods(2),0,fac_mountain_bandits,raider_personality,[(trp_looter_leader2,1,3),(trp_steppe_bandit,2,118)]),
  ("steppe_bandits","Northmenn",icon_warriors_2|carries_goods(2),0,fac_mountain_bandits,raider_personality,[(trp_sea_raider_leader2,1,2),(trp_steppe_bandit,2,73),(trp_sea_raider_leader,0,2)]),  #one berserk easily worth 30 men right now
  ("taiga_bandits","Vikingarnir",icon_warriors_2|carries_goods(2),0,fac_outlaws,raider_personality,[(trp_sea_raider_leader2,1,3),(trp_elite_viking_2,1,44),(trp_taiga_bandit,1,44)]),
  ("desert_bandits","Veteran Renegades",icon_warriors_2|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_looter_leader2,0,3),(trp_forest_bandit,2,110),(trp_desert_bandit,1,48)]),
  ("forest_bandits","Robbers",icon_warriors_2|carries_goods(2),0,fac_forest_bandits,bandit_personality,[(trp_looter_leader2,0,2),(trp_forest_bandit,1,69),(trp_brigand,1,69)]),
  ("mountain_bandits","Renegades",icon_warriors_2|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_looter_leader2,0,1),(trp_bandit,1,80),(trp_mountain_bandit,1,50),(trp_sea_raider,1,20)]),
  ("sea_raiders","Masterless Fighters",icon_warriors_8|carries_goods(2),0,fac_outlaws,raider_personality,[(trp_looter_leader2,0,1),(trp_sea_raider,1,40),(trp_mountain_bandit,1,80),]),
  # ("sea_raiders2","Danish Elite Vikingarnir",icon_warriors_8|carries_goods(2),0,fac_mountain_bandits,raider_personality,[(trp_sea_raider_leader2,1,3),(trp_elite_viking,1,80),(trp_taiga_bandit,1,36)]),
  ("sea_raiders2","Danish Elite Vikingarnir",icon_warriors_8|carries_goods(2),0,fac_mountain_bandits,raider_personality,[(trp_sea_raider_leader2,1,2),(trp_looter_leader,0,2),(trp_elite_viking,1,20),(trp_taiga_bandit,1,38)]),  #one berserk easily worth 30 men right now
  ("fianna","Renegade Fianna",icon_warriors_2|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_looter_leader2,1,3),(trp_irish_bowman,2,110),(trp_irish_level0_companion,1,48)]),
#2 new bandits for Frisia and Denmark
  ("frank_looters_1","Thieving Franks",icon_warriors_3|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_mountain_bandit,2,150)]),
  ("frank_looters_2","Raiding Franks",icon_warriors_3|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_brigand,2,100),(trp_forest_bandit,1,50)]),
  #deserters signifies end of laired spawned party types 
  ("deserters","Masterless Men",icon_warriors_2|carries_goods(3),0,fac_deserters,bandit_personality,[]),
  
  ("merchant_caravan","Merchant Caravan",icon_caravan_2|carries_goods(40)|pf_auto_remove_in_town|pf_quest_party,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,5,25)]),
  ("troublesome_bandits","Troublesome Bandits",icon_warriors_2|carries_goods(9)|pf_quest_party,0,fac_outlaws,bandit_personality,[(trp_bandit,14,55)]),
  ("bandits_awaiting_ransom","Bandits Awaiting Ransom",icon_warriors_2|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_bandit,24,58),(trp_kidnapped_girl,1,1,pmf_is_prisoner)]),
  ("kidnapped_girl","Kidnapped Girl",icon_woman|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_kidnapped_girl,1,1)]),

  ("village_farmers","Village Farmers",icon_peasant|pf_civilian,0,fac_innocents,merchant_personality,[(trp_farmer,5,20),(trp_peasant_woman,3,16)]),
###nuevo template chief de neko y relic quest

  ("spy_partners", "Unremarkable Travellers", icon_gray_knight|carries_goods(10)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy_partner,1,1),(trp_caravan_guard,5,11)]),
  ("runaway_serfs","Runaway Serfs",icon_peasant|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_farmer,6,7), (trp_peasant_woman,3,3)]),
  ("spy", "Ordinary Townsman", icon_gray_knight|carries_goods(4)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy,1,1)]),
  ("sacrificed_messenger", "Sacrificed Messenger", icon_gray_knight|carries_goods(3)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[]),
##  ("conspirator", "Conspirators", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator,3,4)]),
##  ("conspirator_leader", "Conspirator Leader", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator_leader,1,1)]),
##  ("peasant_rebels", "Peasant Rebels", icon_peasant,0,fac_peasant_rebels,bandit_personality,[(trp_peasant_rebel,33,97)]),
##  ("noble_refugees", "Noble Refugees", icon_gray_knight|carries_goods(12)|pf_quest_party,0,fac_noble_refugees,merchant_personality,[(trp_noble_refugee,3,5),(trp_noble_refugee_woman,5,7)]),

#  ("forager_party","Foraging Party",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("scout_party","Scouts",icon_gray_knight|carries_goods(1)|pf_show_faction,0,fac_commoners,bandit_personality,[]),

#  ("war_party", "War Party",icon_gray_knight|carries_goods(3),0,fac_commoners,soldier_personality,[]),
  ("messenger_party","Messenger",icon_gray_knight|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("raider_party","Raiders",icon_gray_knight|carries_goods(16)|pf_quest_party,0,fac_outlaws,bandit_personality,[]),
  ("raider_captives","Raider Captives",0,0,fac_commoners,0,[(trp_peasant_woman,6,30,pmf_is_prisoner)]),
  ("kingdom_caravan_party","Trader",icon_mule|carries_goods(45)|pf_show_faction,0,fac_commoners,merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,12,40)]),
  ("prisoner_train_party","Prisoner Train",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("default_prisoners","Default Prisoners",0,0,fac_commoners,0,[(trp_bandit,5,10,pmf_is_prisoner)]),

  ("routed_warriors","Routed Enemies",icon_warriors_1|pf_auto_remove_in_town,0,fac_commoners,soldier_personality,[]),


###caza
##  ("deer_herd","Deer Herd",icon_cattle|carries_goods(10),0,fac_wild_animals,merchant_personality,[(trp_deer,16,40)]),
##  ("boar_herd","Boar Herd",icon_cattle|carries_goods(10),0,fac_wild_animals,merchant_personality,[(trp_boar,3,12)]),
##  ("wolf_herd","Wolf Pack",icon_cattle|carries_goods(10),0,fac_wild_animals,merchant_personality,[(trp_wolf,4,18)]),
##  ("coat_herd","Goat Herd",icon_cattle|carries_goods(10),0,fac_wild_animals,merchant_personality,[(trp_coat,4,28)]),
##  ("coatb_herd","Goat Herd",icon_cattle|carries_goods(10),0,fac_wild_animals,merchant_personality,[(trp_coat_b,4,28)]),
##  ("wilddonkey_herd","Wild Donkey Herd",icon_cattle|carries_goods(10),0,fac_wild_animals,merchant_personality,[(trp_wilddonkey,6,18)]),


# Caravans
  ("center_reinforcements","Reinforcements",icon_warriors_6|carries_goods(16),0,fac_commoners,soldier_personality,[(trp_townsman,5,30),(trp_watchman,4,20)]),
  
  ("kingdom_hero_party","War Party",icon_flagbearer_a|pf_show_faction|pf_default_behavior,0,fac_commoners,soldier_personality,[]),
  
# Reinforcements
  # each faction includes three party templates. One is less-modernised, one is med-modernised and one is high-modernised
  # less-modernised templates are generally includes 7-14 troops in total, VC 20-30
  # med-modernised templates are generally includes 5-10 troops in total, VC 10-20
  # high-modernised templates are generally includes 3-5 troops in total VC 8-16
  # VC: since higher levels are called only half as often as the one before, we use this to control troop types. Centers don't pull from *_c, so these have hero's companions

  ("norse_reinforcements_a", "{!}norse_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_norse_level0_landed,7,10),(trp_norse_level1_landed,2,8),(trp_norse_bowman,3,7),(trp_norse_slave,3,8)]),
  ("norse_reinforcements_b", "{!}norse_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_norse_level1_landed,5,8),(trp_norse_level2_landed,2,4),(trp_norse_elitearcher,1,4),(trp_norse_priest,0,2)]),
  ("norse_reinforcements_c", "{!}norse_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_sea_raider_leader,0,2),(trp_norse_level0_companion,4,8),(trp_norse_level1_companion,1,3),(trp_norse_level2_companion,1,3),(trp_norse_standard_bearer,0,2),(trp_todos_cuerno,0,2)]),

  ("saxon_reinforcements_a", "{!}saxon_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_saxon_level0_landed,6,11),(trp_saxon_level1_landed,4,9),(trp_saxon_bowman,1,3),(trp_saxon_slave,3,12)]),
  ("saxon_reinforcements_b", "{!}saxon_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_saxon_level1_landed,5,9),(trp_saxon_level2_landed,2,4),(trp_saxon_level3_landed,0,3),(trp_saxon_priest,0,2),(trp_saxon_level0_landed,1,4)]),
  ("saxon_reinforcements_c", "{!}saxon_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_saxon_level0_companion,2,9),(trp_saxon_level1_companion,2,4),(trp_saxon_level2_companion,1,3),(trp_saxon_standard_bearer,0,2),(trp_saxon_horseman,1,3),(trp_todos_cuerno,0,2)]),
  
  ("angle_reinforcements_a", "{!}angle_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_angle_level0_landed,7,10),(trp_angle_level1_landed,4,9),(trp_angle_bowman,1,3),(trp_angle_slave,3,12)]),
  ("angle_reinforcements_b", "{!}angle_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_angle_level1_landed,6,9),(trp_angle_level2_landed,2,4),(trp_angle_level3_landed,0,3),(trp_angle_priest,0,2),(trp_angle_level0_landed,1,5)]),
  ("angle_reinforcements_c", "{!}angle_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_angle_level0_companion,2,8),(trp_angle_level1_companion,2,4),(trp_angle_level2_companion,0,3),(trp_angle_standard_bearer,0,2),(trp_angle_horseman,1,3),(trp_todos_cuerno,0,2)]),
  
  ("welsh_reinforcements_a", "{!}welsh_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_briton_level0_landed,6,10),(trp_briton_level1_landed,3,9),(trp_briton_slave,3,10),(trp_briton_bowman,1,6),(trp_briton_marksman,1,4),]),
  ("welsh_reinforcements_b", "{!}welsh_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_briton_level1_landed,2,9),(trp_briton_level2_landed,2,4),(trp_briton_level3_landed,0,3),(trp_briton_priest,0,2),(trp_briton_level0_landed,1,4)]),
  ("welsh_reinforcements_c", "{!}welsh_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_briton_level0_companion,2,8),(trp_briton_level1_companion,2,4),(trp_briton_level2_companion,0,3),(trp_briton_standard_bearer,0,2),(trp_briton_horseman,1,3),(trp_todos_cuerno,0,2)]),

  ("scotch_reinforcements_a", "{!}scotch_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_scotch_level0_landed,3,15),(trp_scotch_peasant,2,13),(trp_scotch_bowman,2,6),(trp_scotch_level0_skirmisher,3,9)]),
  ("scotch_reinforcements_b", "{!}scotch_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_scotch_level1_landed,2,4),(trp_scotch_level2_landed,1,3),(trp_scotch_level1_skirmisher,3,5),(trp_scotch_horseman,2,6),(trp_scotch_priest,0,2)]),
  ("scotch_reinforcements_c", "{!}scotch_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_scotch_level0_companion,1,4),(trp_scotch_level1_companion,1,4),(trp_scotch_level2_companion,0,3),(trp_scotch_knight,1,3),(trp_scotch_standard_bearer,0,2),(trp_scotch_musician,0,2)]),

  ("irish_reinforcements_a", "{!}irish_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_irish_level0_landed,5,15),(trp_irish_slave,5,9),(trp_irish_bowman,4,7),(trp_irish_level0_skirmisher,3,6)]),
  ("irish_reinforcements_b", "{!}irish_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_irish_level1_landed,2,7),(trp_irish_level2_landed,2,4),(trp_irish_level3_landed,0,3),(trp_irish_horseman,3,4),(trp_irish_priest,0,2)]),
  ("irish_reinforcements_c", "{!}irish_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_irish_level0_companion,1,4),(trp_irish_level1_companion,1,4),(trp_irish_level1_skirmisher,1,4),(trp_irish_knight,1,3),(trp_irish_standard_bearer,0,2),(trp_todos_cuerno,0,2)]),

  #special treatment Frisa
  ("kingdom_4_reinforcements_a", "{!}kingdom_4_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_norse_level0_landed,4,9),(trp_frisian_mid,3,11),(trp_norse_bowman,2,6),(trp_frisian_basic,3,11)]), #some basic troops are frisians
  ("kingdom_4_reinforcements_b", "{!}kingdom_4_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_norse_level1_landed,3,10),(trp_norse_level2_landed,1,5),(trp_norse_level3_landed,0,3),(trp_norse_priest,0,2),(trp_norse_level0_landed,1,3)]),#some basic troops are frisians
  ("kingdom_4_reinforcements_c", "{!}kingdom_4_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_norse_level0_companion,2,8),(trp_norse_level1_companion,2,3),(trp_norse_level2_companion,1,2),(trp_norse_standard_bearer,0,2),(trp_frisian_cav,1,4),(trp_todos_cuerno,0,2)]), 
  #special treatment Northanhymbre
  ("kingdom_8_reinforcements_a", "{!}kingdom_8_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_angle_level0_landed,7,10),(trp_norse_level1_landed,4,10),(trp_norse_bowman,3,7),(trp_angle_slave,2,7)]), #some basic troops are angles
  ("kingdom_8_reinforcements_b", "{!}kingdom_8_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_norse_level1_landed,4,10),(trp_norse_level2_landed,1,4),(trp_norse_level3_landed,0,3),(trp_norse_priest,0,2),(trp_angle_level0_landed,1,4)]),#some basic troops are angles
  ("kingdom_8_reinforcements_c", "{!}kingdom_8_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_norse_level0_companion,3,8),(trp_norse_level1_companion,1,3),(trp_norse_level2_companion,0,2),(trp_norse_standard_bearer,0,2),(trp_angle_horseman,2,4),(trp_todos_cuerno,0,2)]), 
  #special treatment Osrige
  ("kingdom_21_reinforcements_a", "{!}kingdom_21_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_irish_level0_landed,5,14),(trp_irish_slave,2,12),(trp_irish_bowman,2,6),(trp_irish_level0_skirmisher,3,7)]),
  ("kingdom_21_reinforcements_b", "{!}kingdom_21_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_irish_level1_landed,2,7),(trp_irish_level2_landed,2,5),(trp_steppe_bandit,1,6),(trp_irish_horseman,2,4),(trp_irish_priest,0,2),(trp_irish_level3_landed,0,2)]),
  ("kingdom_21_reinforcements_c", "{!}kingdom_21_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_irish_level0_companion,1,5),(trp_irish_level1_companion,1,5),(trp_elite_viking,0,6),(trp_irish_knight,1,3),(trp_irish_standard_bearer,0,2),(trp_todos_cuerno,0,2)]), #Cerball often hired Viking mercenaries from Waterford


  ("steppe_bandit_lair" ,"a Northmenn longphort",icon_ship_on_land|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_mountain_bandits,bandit_personality,[(trp_steppe_bandit,15,50)]),#chief cambiado icono
  ("taiga_bandit_lair","a Vikingarnir longphort",icon_ship_on_land|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_mountain_bandits,bandit_personality,[(trp_taiga_bandit,15,58)]),#chief cambiado icono
  ("desert_bandit_lair" ,"a veteran renegades' camp",icon_camp|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_outlaws,bandit_personality,[(trp_desert_bandit,7,50),(trp_forest_bandit,15,90)]),#chief cambiado icono
  ("forest_bandit_lair" ,"a robbers' den",icon_cave|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_outlaws,bandit_personality,[(trp_forest_bandit,12,90),(trp_brigand,12,90)]),#chief cambiado icono
  ("mountain_bandit_lair" ,"a renegades' camp",icon_camp|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_outlaws,bandit_personality,[(trp_mountain_bandit,15,96),(trp_sea_raider,6,30),(trp_bandit,4,20)]),#chief cambiado icono
  ("sea_raider_lair","a fighters camp",icon_camp|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_outlaws,bandit_personality,[(trp_sea_raider,15,75),(trp_taiga_bandit,8,90)]), #chief cambiado icono
  ("sea_raider_lair2","a Danish longphort",icon_ship_on_land|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_mountain_bandits,bandit_personality,[(trp_elite_viking,15,30),(trp_taiga_bandit,6,28)]), #chief cambiado icono
  ("looter_lair","the kidnappers' hideout",icon_cave|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_outlaws,bandit_personality,[(trp_looter,15,180)]),#chief cambiado icono
  
  ("bandit_lair_templates_end","{!}bandit_lair_templates_end",icon_warriors_2|carries_goods(2)|pf_is_static,0,fac_outlaws,bandit_personality,[(trp_sea_raider,15,50)]),

  ("leaded_looters","Band of Robbers",icon_warriors_2|carries_goods(8)|pf_quest_party,0,fac_outlaws,bandit_personality,[(trp_looter_leader2,1,2),(trp_looter,3,4)]),

#chief sacerdotes party religion
    ("sacerdotes_party","Christian Clergy",icon_peasant|carries_goods(2),0,fac_christians,merchant_personality,[(trp_scotch_priest,3,9), (trp_peasant_woman,4,15)]),
    ("paganos_party","Pagan Priests",icon_peasant|carries_goods(2),0,fac_pagans,merchant_personality,[(trp_norse_priest,3,9), (trp_farmer,4,15)]),

  # Script de refuerzos y reclutas a ciudades chief
  #("reinforcements","Reinforcements",icon_warriors_2|pf_show_faction,0,fac_commoners,soldier_personality,[]),
  # standard ships carried 30 men, 1-5 ships here
  ("sea_raiders_ships" ,"Frankish Raiders",			icon_ship|pf_is_ship|carries_goods(2),0,fac_outlaws,raider_personality,[(trp_sea_raider_leader2, 1, 4), (trp_sea_raider, 14, 59), (trp_regular_sailors, 14, 59)]),
  ("sea_raiders_ships2","Danish Vikingr",	icon_ship|pf_is_ship|carries_goods(2),0,fac_mountain_bandits,raider_personality,[(trp_elite_viking, 7, 20),(trp_taiga_bandit, 14, 40),(trp_sea_raider_leader,0,2),(trp_regular_sailors, 10, 29)]),  #one berserk easily worth 30 men right now
  ("sea_raiders_ships3","Vikingr",			icon_ship|pf_is_ship|carries_goods(2),0,fac_mountain_bandits,raider_personality,[(trp_sea_raider_leader,0,2), (trp_taiga_bandit, 14, 44),(trp_regular_sailors, 14, 44)]),  #one berserk easily worth 30 men right now
  ("sea_raiders_ships4","Norwegian Vikingr",icon_ship|pf_is_ship|carries_goods(2),0,fac_mountain_bandits,raider_personality,[(trp_steppe_bandit, 14, 44), (trp_sea_raider_leader,0,2),(trp_regular_sailors, 14, 44)]),  #one berserk easily worth 30 men right now
  ("sea_raiders_ships5","Swedish Vikingr",	icon_ship|pf_is_ship|carries_goods(2),0,fac_mountain_bandits,raider_personality,[(trp_sea_raider_leader2, 1, 4),(trp_elite_viking_2, 9, 29),(trp_taiga_bandit, 9, 29),(trp_regular_sailors, 9, 29)]),
  ("sea_raiders_ships6","Raiders",			icon_ship|pf_is_ship|carries_goods(2),0,fac_outlaws,raider_personality,[(trp_sea_raider_leader2, 1, 4), (trp_brigand, 10, 48), (trp_forest_bandit, 5, 24),(trp_regular_sailors, 10, 48)]),
  # Phaiak begin chief
  ("chimney_smoke","Smoke",icon_chimney_smoke|pf_is_static|pf_always_visible|pf_no_label|pf_hide_defenders,0, 0, 0,[]),
  ("epic_fleet","Epic Viking Fleet",icon_ship|pf_is_ship|carries_goods(2),0,fac_outlaws,raider_personality,[(trp_elite_viking,200,300)]),
  ("port","port",icon_landing_point|pf_is_static|pf_always_visible|pf_show_faction|pf_label_large|pf_hide_defenders,0, 0, 0,[]),
  ("ferry_port","port",icon_landing_point|pf_no_label|pf_is_static|pf_hide_defenders,0, 0, 0,[]),
  ("landet_ships","your ships",icon_ship_on_land|pf_is_static|pf_always_visible|pf_hide_defenders|pf_is_ship|pf_label_large,0, fac_player_supporters_faction, 0,[]),
  ("fisher_ship","Fisher",icon_merchants_1|carries_goods(2)|pf_is_ship|pf_civilian,0,fac_innocents,merchant_personality,[(trp_fisher,3,10)]),
  ("traveller_ship","Traveller",icon_merchants_1|carries_goods(4)|pf_is_ship|pf_auto_remove_in_town|pf_civilian,0,fac_commoners,merchant_personality,[(trp_regular_sailors,6,90)]),
  ("slave_trader_ship","Slave Trader",icon_merchants_1|carries_goods(3)|pf_is_ship|pf_auto_remove_in_town|pf_civilian,0,fac_manhunters,merchant_personality,[(trp_slaver_chief,1,2), (trp_slave_crusher,0,12), (trp_slave_hunter,0,24), (trp_slave_driver,4,48),]),
  ("sea_king_danish","Sea King",icon_ship|carries_goods(3)|pf_is_ship,0,fac_commoners,soldier_personality,[(trp_norse_level3_landed, 1,2),(trp_norse_level2_companion, 0,5),(trp_norse_level1_companion, 4,18),(trp_norse_level0_companion, 9,38),(trp_norse_elitearcher, 4,18),(trp_norse_bowman, 9,38),]),
  ("sea_king_norweg","Sea King",icon_ship|carries_goods(3)|pf_is_ship,0,fac_commoners,soldier_personality,[(trp_norse_level3_landed, 1,2),(trp_norse_level2_companion, 0,5),(trp_norse_level1_companion, 4,18),(trp_norse_level0_companion, 9,38),(trp_norse_elitearcher, 4,18),(trp_norse_bowman, 9,38),]),
  ("walrus_hunter","Walrus Hunter",icon_merchants_1|carries_goods(2)|pf_is_ship|pf_civilian,0,fac_innocents,merchant_personality,[(trp_fisher,3,5), (trp_norse_level1_landed,0,10)]),
  ("viking_raider","Viking Raider",icon_ship|carries_goods(3)|pf_is_ship,0,fac_commoners,raider_personality,[(trp_elite_viking,25,90)]),	#deprecated
  # Phaiak end
#otras chief
#  ("scouts","Pictish Scouts",icon_gray_knight|carries_goods(1)|pf_show_faction,0,fac_kingdom_20,bandit_personality,[(trp_scotch_bowman,10,20),(trp_pict_woman,1,1)]),
#  ("watchtower_scouts","Scouts",icon_gray_knight|carries_goods(1)|pf_show_faction,0,fac_kingdom_20,bandit_personality,[(trp_mercenary_horseman,5,7)]),
#  ("iniau","Iniau Scouts",icon_vaegir_knight|carries_goods(1),0,fac_neko,bandit_personality,[(trp_iniau,1,1),(trp_swadian_sergeant,43,65)]),
#chief followers seguidores
("ambushers","Ambushers",icon_warriors_2|carries_goods(2),0,fac_forest_bandits,aggressiveness_15 | courage_15,[(trp_forest_bandit,5,160)]),

	("ship"	,"Ship",icon_ship|pf_is_ship|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders|pf_show_faction,0,fac_commoners,merchant_personality,[(trp_mercenary_leader,1,1)]),

#mainquest chief
   # ("thiaderd_lair","Thiaderd's Hideout",icon_camp|carries_goods(8)|pf_is_static|pf_always_visible|pf_label_large|pf_hide_defenders|pf_quest_party,0,fac_dark_knights,aggressiveness_15 | courage_15,[(trp_thiaderd,1,1),(trp_bandit,12,16)]),#chief cambiado icono
    ("sven_doccinga_ca","Sven's Raiders",carries_goods(8)|pf_always_visible|pf_hide_defenders,0,fac_dark_knights,aggressiveness_15 | courage_15,[(trp_norse_level0_landed,1,1),(trp_sea_raider_leader2,2,2),(trp_elite_viking,9,10),(trp_taiga_bandit,57,58),]),
    ("sven_lair_deffense","Sven's Hideout",icon_camp_refuge|carries_goods(2)|pf_always_visible|pf_is_static|pf_hide_defenders,0,fac_dark_knights,aggressiveness_15 | courage_15,[(trp_leader_svenlair,1,1),(trp_elite_viking,1,1),(trp_taiga_bandit,19,21),]),
    ("kennemer_revenge","Raiders",icon_warriors_8|carries_goods(2),0,fac_dark_knights,aggressiveness_15 | courage_15,[(trp_elite_viking,1,2),(trp_looter,24,26),(trp_bandit,9,11),(trp_taiga_bandit,4,6),]),
    ("sigurd_farm_men","Sigurd's Men",carries_goods(8)|pf_always_visible|pf_hide_defenders,0,fac_dark_knights,aggressiveness_15 | courage_15,[(trp_sven_brother,1,1),(trp_farmstead_prisoner,1,1),(trp_elite_viking,2,4),(trp_taiga_bandit,24,26),]),
   # ("doccinga_deffend","Doccinga Defenders",icon_camp|carries_goods(8)|pf_always_visible|pf_hide_defenders|pf_quest_party,0,fac_manhunters,soldier_personality,[(trp_village_150_elder,1,1),(trp_farmer,55,60),(trp_norse_level0_companion,18,20),(trp_norse_standard_bearer,1,2),(trp_norse_level1_landed,8,12),(trp_norse_level2_companion,1,1)]),
    ("wessex_foragers","West Seaxe Foragers",icon_warriors_2|carries_goods(2),0,fac_neutral,aggressiveness_12| courage_15,[(trp_saxon_bowman,14,25),(trp_saxon_slave,40,55)]),
    ("wessex_patrol","West Seaxe Patrol",icon_warriors_2|carries_goods(2),0,fac_kingdom_5,bandit_personality,[(trp_saxon_level2_companion,1,2),(trp_saxon_level0_companion,14,16),(trp_saxon_bowman,20,22),(trp_saxon_level0_landed,24,26)]),
 # ("looters","Thieves",icon_warriors_3|carries_goods(8),0,fac_outlaws,bandit_personality,[(trp_looter,3,30)]), #chief cambiado
  ##  ("followers","Camp Followers",icon_mule|carries_goods(25)|pf_show_faction,0,fac_commoners,merchant_personality,[(trp_caravan_master,1,3),(trp_caravan_guard,4,6),(trp_farmer,3,14),(trp_follower_woman,15,60),(trp_fighter_woman,12,40)]),
##  ("followersplayer","Camp Followers",icon_mule|carries_goods(25)|pf_show_faction,0,fac_commoners,merchant_personality,[(trp_caravan_master,1,3),(trp_caravan_guard,4,6),(trp_farmer,3,14),(trp_follower_woman,15,60),(trp_fighter_woman,12,40)]),
# Foragers SoT chief
###anglos
##  ("bernician_foragers","Acerweras",icon_gray_knight|carries_goods(5),0,fac_kingdom_4,merchant_personality,[(trp_nord_footman,5,10),(trp_nord_huntsman,2,4),(trp_nord_warrior,2,4)]),
###jutos
##  ("rheged_foragers","Foragers",icon_vaegir_knight|carries_goods(5),0,fac_kingdom_1,merchant_personality,[(trp_norse_level0_landed,5,10),(trp_norse_bowman,2,4),(trp_norse_level1_landed,2,4)]),
###britons
##  ("gododdin_foragers","Foragers",icon_vaegir_knight|carries_goods(5),0,fac_kingdom_3,merchant_personality,[(trp_swadian_militia,3,7),(trp_swadian_footman,3,5),(trp_swadian_skirmisher,2,6)]),
###sajones
##  ("dalriadan_foragers","Foragers",icon_vaegir_knight|carries_goods(5),0,fac_kingdom_2,merchant_personality,[(trp_vaegir_footman,5,10),(trp_vaegir_skirmisher,2,4),(trp_vaegir_infantry,2,4)]),
###irish
##  ("alcluyd_foragers","Foragers",icon_vaegir_knight|carries_goods(5),0,fac_kingdom_7,merchant_personality,[(trp_rhodok_spearman,5,10),(trp_rhodok_crossbowman,2,4),(trp_rhodok_veteran_spearman,2,4)]),
###pictos
##  ("pictish_foragers","Pictish Foragers",icon_vaegir_knight|carries_goods(5),0,fac_kingdom_5,merchant_personality,[(trp_khergit_skirmisher,6,12),(trp_picti_each,3,5),(trp_pict_woman,1,3)]),

###########################################
### party templates added after release ###
###########################################

# new bandits for Frisia and Denmark
  ("norway_looters","Thieves",icon_warriors_3|carries_goods(2)|pf_auto_remove_in_town,0,fac_outlaws,bandit_personality,[(trp_looter,3,180)]),	#deprecated
  ("jetty_port","port",icon_landing_point|pf_no_label|pf_is_static|pf_hide_defenders,0, 0, 0,[]),
  #addon:
  ("boar_herd","Boar Herd",icon_boar,0,fac_neutral,merchant_personality,[(trp_shipwright_end,1,5)]),
   # Adventurers
  ("adv_party","War Party",icon_warriors_1,0,fac_adventurers,soldier_personality,[]),
  ("slave_hideout" ,"Hideout",icon_camp|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[]),	#VC-1883
  ("village_elder", "Levy", icon_peasant,0,fac_commoners,aggressiveness_0|courage_12,[]),

]
