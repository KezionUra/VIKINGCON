from header_map_icons import *
from module_constants import *
from header_operations import *
from header_triggers import *
from ID_sounds import *

####################################################################################################################
#  Each map icon record contains the following fields:
#  1) Map icon id: used for referencing map icons in other files.
#     The prefix icon_ is automatically added before each map icon id.
#  2) Map icon flags. See header_map icons.py for a list of available flags
#  3) Mesh name.
#  4) Scale. 
#  5) Sound.
#  6) Offset x position for the flag icon.
#  7) Offset y position for the flag icon.
#  8) Offset z position for the flag icon.
####################################################################################################################

banner_scale = 0.5 #chief cambia de 0.3 a 0.5
avatar_scale = 0.25 #chief cambia de 0.15 a 0.25
woman_icon_scale = 0.45
settlement_scale = 1.33
settlement_scale_reduced = 1

icon_tableau_trigger = (ti_on_init_map_icon, 
	[
      (store_trigger_param_1, ":party_no"),
      (try_begin),
        (this_or_next|eq, ":party_no", "p_main_party"),
        (party_slot_eq, ":party_no", slot_party_type, spt_kingdom_hero_party),
        (party_stack_get_troop_id, ":leader_troop", ":party_no", 0),
        (troop_slot_ge,  ":leader_troop", slot_troop_banner_scene_prop, 1),
        (cur_map_icon_set_tableau_material, "tableau_vc_icon_shield_01", ":leader_troop"),
      (else_try),
        (cur_map_icon_set_tableau_material, "tableau_vc_icon_shield_01", -1),
      (try_end), 
    ])

map_icons = [

# player on land
  ("player",0,"player", avatar_scale, snd_footstep_grass, [icon_tableau_trigger,]),
  ("player_withtroops",0,"player_withtroops", avatar_scale, snd_footstep_grass, [icon_tableau_trigger,]),
  ("player_troops_followers",0,"player_troops_followers", avatar_scale, snd_footstep_grass, [icon_tableau_trigger,]),
  ("player_horseman",0,"player_horseman", avatar_scale, snd_gallop, [icon_tableau_trigger,]),
#moved below for savegame compatibility
##  ("player_horseman_withtroops",0,"player_horseman_withtroops", avatar_scale, snd_gallop, [icon_tableau_trigger,]),
##  ("player_horseman_followers",0,"player_horseman_followers", avatar_scale, snd_gallop, [icon_tableau_trigger,]),
  
# player on water
  ("ship",mcn_no_shadow,"ships_1", avatar_scale, snd_footstep_water, 0.0, 0.05, 0),
  ("ship_on_land",mcn_no_shadow,"ship_landed", avatar_scale, 0), #chief use this for sven doccinga invasion
  
# parties on land
  ("lords_1",0,"lords_01", avatar_scale, snd_gallop, [icon_tableau_trigger,]),
  ("lords_2",0,"lords_01", avatar_scale, snd_gallop, [icon_tableau_trigger,]),
  ("lords_3",0,"lords_03", avatar_scale, snd_gallop, [icon_tableau_trigger,]),
  ("lords_4",0,"lords_03", avatar_scale, snd_gallop, [icon_tableau_trigger,]),
  ("lords_5",0,"lords_05", avatar_scale, snd_gallop, [icon_tableau_trigger,]),
  ("lords_6",0,"lords_05", avatar_scale, snd_gallop, [icon_tableau_trigger,]),
  ("lords_7",0,"lords_07", avatar_scale, snd_gallop, [icon_tableau_trigger,]),
  ("lords_8",0,"lords_07", avatar_scale, snd_gallop, [icon_tableau_trigger,]),
  ("lords_9",0,"lords_07", avatar_scale, snd_gallop, [icon_tableau_trigger,]),
  ("lords_10",0,"lords_10", avatar_scale, snd_gallop, [icon_tableau_trigger,]),

  ("warriors_1",0,"warriors_01", avatar_scale, snd_footstep_grass, [icon_tableau_trigger,]),
  ("warriors_2",0,"warriors_01", avatar_scale, snd_footstep_grass, [icon_tableau_trigger,]),
  ("warriors_3",0,"warriors_03", avatar_scale, snd_footstep_grass, [icon_tableau_trigger,]),
  ("warriors_4",0,"warriors_03", avatar_scale, snd_footstep_grass, [icon_tableau_trigger,]),
  ("warriors_5",0,"warriors_05", avatar_scale, snd_footstep_grass, [icon_tableau_trigger,]),
  ("warriors_6",0,"warriors_05", avatar_scale, snd_footstep_grass, [icon_tableau_trigger,]),
  ("warriors_7",0,"warriors_07", avatar_scale, snd_footstep_grass, [icon_tableau_trigger,]),
  ("warriors_8",0,"warriors_07", avatar_scale, snd_footstep_grass, [icon_tableau_trigger,]),
  ("warriors_9",0,"warriors_07", avatar_scale, snd_footstep_grass, [icon_tableau_trigger,]),
  ("warriors_10",0,"warriors_10", avatar_scale, snd_footstep_grass, [icon_tableau_trigger,]),
  
  ("farmer_1",0,"farmer_01", avatar_scale, snd_footstep_grass, [icon_tableau_trigger,]),
  ("farmer_2",0,"farmer_01", avatar_scale, snd_footstep_grass, [icon_tableau_trigger,]),
  ("farmer_3",0,"farmer_03", avatar_scale, snd_footstep_grass, [icon_tableau_trigger,]),
  ("farmer_4",0,"farmer_03", avatar_scale, snd_footstep_grass, [icon_tableau_trigger,]),
  ("farmer_5",0,"farmer_05", avatar_scale, snd_footstep_grass, [icon_tableau_trigger,]),
  ("farmer_6",0,"farmer_05", avatar_scale, snd_footstep_grass, [icon_tableau_trigger,]),
  ("farmer_7",0,"farmer_07", avatar_scale, snd_footstep_grass, [icon_tableau_trigger,]),
  ("farmer_8",0,"farmer_07", avatar_scale, snd_footstep_grass, [icon_tableau_trigger,]),
  ("farmer_9",0,"farmer_07", avatar_scale, snd_footstep_grass, [icon_tableau_trigger,]),
  ("farmer_10",0,"farmer_10", avatar_scale, snd_footstep_grass, [icon_tableau_trigger,]),
  
  ("caravan_1",0,"caravan_01", avatar_scale, snd_footstep_grass, [icon_tableau_trigger,]),
  ("caravan_2",0,"caravan_01", avatar_scale, snd_footstep_grass, [icon_tableau_trigger,]),
  ("caravan_3",0,"caravan_03", avatar_scale, snd_footstep_grass, [icon_tableau_trigger,]),
  ("caravan_4",0,"caravan_03", avatar_scale, snd_footstep_grass, [icon_tableau_trigger,]),
  ("caravan_5",0,"caravan_03", avatar_scale, snd_footstep_grass, [icon_tableau_trigger,]),
  ("caravan_6",0,"caravan_06", avatar_scale, snd_footstep_grass, [icon_tableau_trigger,]),

# parties on water
  ("ships_1",0,"ships_1", avatar_scale, snd_footstep_water),
  ("ships_2",0,"ships_1", avatar_scale, snd_footstep_water),
  ("ships_3",0,"ships_3", avatar_scale, snd_footstep_water),
  ("ships_4",0,"ships_3", avatar_scale, snd_footstep_water),
  ("ships_5",0,"ships_5", avatar_scale, snd_footstep_water),
  ("ships_6",0,"ships_5", avatar_scale, snd_footstep_water),
  ("ships_7",0,"ships_7", avatar_scale, snd_footstep_water),
  
  ("merchants_1",0,"merchants_1", avatar_scale, snd_footstep_water),
  ("merchants_2",0,"merchants_1", avatar_scale, snd_footstep_water),
  ("merchants_3",0,"merchants_3", avatar_scale, snd_footstep_water),
  ("merchants_4",0,"merchants_3", avatar_scale, snd_footstep_water),
  ("merchants_5",0,"merchants_5", avatar_scale, snd_footstep_water),
  ("merchants_6",0,"merchants_5", avatar_scale, snd_footstep_water),
  ("merchants_7",0,"merchants_7", avatar_scale, snd_footstep_water),

# settlement icons
  ("town_port",mcn_no_shadow,"map_tradeport", 			settlement_scale_reduced, 0), #ciudad con puerto chief Adorno
  ("town_walled",mcn_no_shadow,"wall_town_icon", 		settlement_scale, 0), #con muro dentro hall y casas
  ("fort1",mcn_no_shadow,"map_vikingcastle", 			settlement_scale_reduced, 0), #cambiado para capitales chief Adorno  
  ("fort2",mcn_no_shadow,"hillfort_icon", 				settlement_scale,0), #dos murallas fuerte en colina Adorno    
  ("monastery",mcn_no_shadow,"monastery", 				settlement_scale,0), #icono monastery chief, para lugares de culto y ruinas
  ("village_a",mcn_no_shadow,"town_icon2", 				settlement_scale,0), #sin muro solo hall y casas Adorno
  
  ("town_port_burnt",mcn_no_shadow,"map_tradeport_burned", 	settlement_scale_reduced,0),  
  ("town_walled_burnt",mcn_no_shadow,"wall_town_icon_burned", settlement_scale,0),
  ("fort1_burnt",mcn_no_shadow,"map_vikingcastle_burned", 	settlement_scale_reduced, 0),  
  ("fort2_burnt",mcn_no_shadow,"hillfort_icon_burned", 		settlement_scale,0),  
  ("monastery_burnt",mcn_no_shadow,"monastery_burned", 		settlement_scale,0),  
  ("village_burnt_a",mcn_no_shadow,"town_icon2_burned", 	settlement_scale, 0),  

# could be deleted begin
  ("town_port_snow",mcn_no_shadow,"town_icon2", 	settlement_scale_reduced,0),  
  ("town_walled_snow",mcn_no_shadow,"town_icon2", 		settlement_scale, 0),   
  ("fort1_snow",mcn_no_shadow,"town_icon2", 		settlement_scale_reduced, 0),
  ("fort2_snow",mcn_no_shadow,"town_icon2", 		settlement_scale,0),  
  ("monastery_snow",mcn_no_shadow,"town_icon2", 				settlement_scale,0),  
  ("village_snow_a",mcn_no_shadow,"town_icon2",		settlement_scale,0), 
  
  ("player_horseman_withtroops",0,"player_horseman_withtroops", avatar_scale, snd_gallop, [icon_tableau_trigger,]),
  ("player_horseman_followers",0,"player_horseman_followers", avatar_scale, snd_gallop, [icon_tableau_trigger,]),
##  ("town_port_snow_burnt",mcn_no_shadow,"town_icon2", 	settlement_scale_reduced,0),
##  ("town_walled_snow_burnt",mcn_no_shadow,"town_icon2", 	settlement_scale,0),  
  ("boar",0,"icon_boar", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),
##  ("fort1_snow_burnt",mcn_no_shadow,"town_icon2", 		settlement_scale_reduced, 0),
  ("fort2_snow_burnt",mcn_no_shadow,"town_icon2", 			settlement_scale,0),
  ("monastery_snow_burnt",mcn_no_shadow,"town_icon2", 		settlement_scale,0),
  ("village_snow_burnt_a",mcn_no_shadow,"town_icon2", 	settlement_scale, 0),
# could be deleted end

  ("village_deserted_a",mcn_no_shadow,"town_icon2_burned", settlement_scale, 0), #para animales en agua chief
  ("village_snow_deserted_a",mcn_no_shadow,"town_icon2_burned", settlement_scale,0),

# story icons
  ("snotingaham_siege", mcn_no_shadow, "snotingaham_siege", settlement_scale, 0), #mainquest siege icon
  ("snotingaham_siege_camps", mcn_no_shadow, "snotingaham_siege_camps", settlement_scale, 0), #siege camp icon
  
# camp icons
  ("camp",mcn_no_shadow,"playerrefuge", settlement_scale, 0), #chief do more big
  ("camp_basic",0,"quarry_icon", settlement_scale, 0), #quarry
  ("camp_fortified",0,"playerrefuge_upgrade", settlement_scale, 0),
  ("camp_refuge",0,"camp_fortified", settlement_scale,0), #Refuge
  ("siege_camp_ports", mcn_no_shadow, "map_tradeport_siegecamps", settlement_scale, 0),
  ("siege_camp_town", mcn_no_shadow, "wall_town_icon_siegecamps", settlement_scale, 0),
  ("siege_camp_fort", mcn_no_shadow, "map_vikingcastle_siegecamps", settlement_scale, 0),
  #("siege_camp", mcn_no_shadow, "siege_camp", 1.35, 0), #siege camp icon  
  
# special places
  ("sacred_forest",mcn_no_shadow,"sacred_forest", settlement_scale,0), #icono sacred forest chief, para templos paganos
  ("cave",mcn_no_shadow,"cave", settlement_scale,0), #
  ("bridge_b",mcn_no_shadow,"troll_bridge", 1.27,0), #troll bridge
  ("farmstead_sp",0,"farmstead", settlement_scale, 0), #farmstead
  ("woodcutter_sp",0,"woodcutter", settlement_scale, 0), #farmstead
  
# technical icons
  ("landing_point", mcn_no_shadow, "empty", 0, 0),
  ("chimney_smoke", mcn_no_shadow, "empty", 1,0,
	[
   (ti_on_init_map_icon,
	[ (store_trigger_param_1, ":icon_id"),
	  (party_clear_particle_systems, ":icon_id"),
	  (party_add_particle_system, ":icon_id", "psys_icon_chimney_smoke"),]),]),
   	
# native icons
  ("gray_knight",0,"lords_01", avatar_scale, snd_gallop, 0.15, 0.173, 0),
  ("vaegir_knight",0,"lords_01", avatar_scale, snd_gallop, 0.15, 0.173, 0),
  ("flagbearer_a",0,"lords_01", avatar_scale, snd_gallop, 0.15, 0.173, 0), #mesh not used, mesh was flagbearer_a
  ("flagbearer_b",0,"lords_01", avatar_scale, snd_gallop, 0.15, 0.173, 0), #mesh not used, mesh was flagbearer_b
  ("peasant",0,"farmer_01", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0), #mesh YES used, mesh was peasant_a
  ("khergit",0,"lords_01", avatar_scale,snd_gallop, 0.15, 0.173, 0), #mesh not used, mesh was khergit_horseman
  ("khergit_horseman_b",0,"lords_01", avatar_scale,snd_gallop, 0.15, 0.173, 0), #mesh not used, mesh was khergit_horseman_b
  ("axeman",0,"lords_01", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0), #not used, mesh was bandit_a
  ("woman",0,"farmer_01", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0), #mesh YES used, mesh was woman_a
  ("woman_b",0,"lords_01", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0), #mesh not used, mesh was woman_b
  ("bandit_lair",mcn_no_shadow,"camp_2", 0.45, 0), #mesh not used, mesh was map_bandit_lair
  ("mule",0,"caravan_03", 0.2,snd_footstep_grass, 0.15, 0.173, 0), #mesh no used, mesh was icon_mule
  ("cattle",0,"icon_cow", avatar_scale, snd_footstep_grass, 0.15, 0.173, 0), #mesh YES used, mesh was icon_cow
  ("training_ground",mcn_no_shadow,"camp_2", 1,0), #mesh YES used, mesh was camp_2

# bridge icons
  ("bridge_a",mcn_no_shadow,"bridge", 1,0),
  ("bridge_snow_a",mcn_no_shadow,"bridge", 1,0),
  ("ferry",mcn_no_shadow,"ferrystation", 1,0),

# map text icons
  ("map_txt_laithlind", 0, "map_txt_1", 1.0, 0, 0, 0, 0),
  ("map_txt_alban", 0, "map_txt_2", 1.0, 0, 0, 0, 0),
  ("map_txt_altclut", 0, "map_txt_3", 1.0, 0, 0, 0, 0),
  ("map_txt_norphymbra_1", 0, "map_txt_4", 1.0, 0, 0, 0, 0),
  ("map_txt_norphymbra_2", 0, "map_txt_5", 1.0, 0, 0, 0, 0),
  ("map_txt_gwynedd_1", 0, "map_txt_6", 1.0, 0, 0, 0, 0),
  ("map_txt_gwynedd_2", 0, "map_txt_7", 1.0, 0, 0, 0, 0),
  ("map_txt_corniu_1", 0, "map_txt_8", 1.0, 0, 0, 0, 0),
  ("map_txt_corniu_2", 0, "map_txt_9", 1.0, 0, 0, 0, 0),
  ("map_txt_wessex", 0, "map_txt_10", 1.0, 0, 0, 0, 0),
  ("map_txt_eastengla", 0, "map_txt_11", 1.0, 0, 0, 0, 0),
  ("map_txt_mearce", 0, "map_txt_12", 1.0, 0, 0, 0, 0),

  ("map_txt_aileach", 0, "map_txt_13", 1.0, 0, 0, 0, 0),
  ("map_txt_connachta", 0, "map_txt_14", 1.0, 0, 0, 0, 0),
  ("map_txt_meath", 0, "map_txt_15", 1.0, 0, 0, 0, 0),
  ("map_txt_laigin", 0, "map_txt_16", 1.0, 0, 0, 0, 0),
  ("map_txt_mumain", 0, "map_txt_17", 1.0, 0, 0, 0, 0),

  ("map_txt_noregr", 0, "map_txt_18", 1.0, 0, 0, 0, 0),
  ("map_txt_danmork", 0, "map_txt_19", 1.0, 0, 0, 0, 0),
  ("map_txt_frisa", 0, "map_txt_20", 1.0, 0, 0, 0, 0),

# banners
  ("map_flag_extra01", 0, "map_flag_extra01", banner_scale, 0),
  ("map_flag_extra02", 0, "map_flag_extra02", banner_scale, 0),
  ("map_flag_extra03", 0, "map_flag_extra03", banner_scale, 0),
  ("map_flag_extra04", 0, "map_flag_extra04", banner_scale, 0),
  ("map_flag_extra05", 0, "map_flag_extra05", banner_scale, 0),
  ("map_flag_extra06", 0, "map_flag_extra06", banner_scale, 0),
  ("map_flag_extra07", 0, "map_flag_extra07", banner_scale, 0),
  ("map_flag_extra08", 0, "map_flag_extra08", banner_scale, 0),
  ("map_flag_extra09", 0, "map_flag_extra09", banner_scale, 0),
  ("map_flag_extra10", 0, "map_flag_extra10", banner_scale, 0),
  ("map_flag_extra11", 0, "map_flag_extra11", banner_scale, 0),
  ("map_flag_extra12", 0, "map_flag_extra12", banner_scale, 0),
  ("map_flag_extra13", 0, "map_flag_extra13", banner_scale, 0),
  ("map_flag_extra14", 0, "map_flag_extra14", banner_scale, 0),
  ("map_flag_extra15", 0, "map_flag_extra15", banner_scale, 0),
  ("map_flag_extra16", 0, "map_flag_extra16", banner_scale, 0),
  ("map_flag_extra17", 0, "map_flag_extra17", banner_scale, 0),
  ("map_flag_extra18", 0, "map_flag_extra18", banner_scale, 0),
  ("map_flag_extra19", 0, "map_flag_extra19", banner_scale, 0),
  ("map_flag_extra20", 0, "map_flag_extra20", banner_scale, 0),
  ("map_flag_extra21", 0, "map_flag_extra21", banner_scale, 0),
  ("map_flag_extra201", 0, "map_flag_extra201", banner_scale, 0),
  ("map_flag_extra202", 0, "map_flag_extra202", banner_scale, 0),
  ("map_flag_extra203", 0, "map_flag_extra203", banner_scale, 0),
  ("map_flag_extra204", 0, "map_flag_extra204", banner_scale, 0),
  ("map_flag_extra205", 0, "map_flag_extra205", banner_scale, 0),
  ("map_flag_extra206", 0, "map_flag_extra206", banner_scale, 0),
  # ("map_flag_extra207", 0, "map_flag_extra207", banner_scale, 0), reserve for default
  ("map_flag_extra208", 0, "map_flag_extra208", banner_scale, 0),
  ("map_flag_extra209", 0, "map_flag_extra209", banner_scale, 0),
  ("map_flag_extra210", 0, "map_flag_extra210", banner_scale, 0),
  ("map_flag_extra211", 0, "map_flag_extra211", banner_scale, 0),
  # ("map_flag_extra212", 0, "map_flag_extra212", banner_scale, 0),
  # ("map_flag_extra213", 0, "map_flag_extra213", banner_scale, 0),
  # ("map_flag_extra214", 0, "map_flag_extra214", banner_scale, 0),
  # ("map_flag_extra215", 0, "map_flag_extra215", banner_scale, 0),
  # ("map_flag_extra216", 0, "map_flag_extra216", banner_scale, 0),
  # ("map_flag_extra217", 0, "map_flag_extra217", banner_scale, 0),
  # ("map_flag_extra218", 0, "map_flag_extra218", banner_scale, 0),
  # ("map_flag_extra219", 0, "map_flag_extra219", banner_scale, 0),
  # ("map_flag_extra220", 0, "map_flag_extra220", banner_scale, 0),
  # ("map_flag_extra221", 0, "map_flag_extra221", banner_scale, 0),
  ("map_flag_anglosaxon01", 0, "map_flag_anglosaxon01", banner_scale, 0),
  ("map_flag_anglosaxon02", 0, "map_flag_anglosaxon02", banner_scale, 0),
  ("map_flag_anglosaxon03", 0, "map_flag_anglosaxon03", banner_scale, 0),
  ("map_flag_anglosaxon04", 0, "map_flag_anglosaxon04", banner_scale, 0),
  ("map_flag_anglosaxon05", 0, "map_flag_anglosaxon05", banner_scale, 0),
  ("map_flag_anglosaxon06", 0, "map_flag_anglosaxon06", banner_scale, 0),
  ("map_flag_anglosaxon07", 0, "map_flag_anglosaxon07", banner_scale, 0),
  ("map_flag_anglosaxon08", 0, "map_flag_anglosaxon08", banner_scale, 0),
  ("map_flag_anglosaxon09", 0, "map_flag_anglosaxon09", banner_scale, 0),
  ("map_flag_anglosaxon10", 0, "map_flag_anglosaxon10", banner_scale, 0),
  ("map_flag_anglosaxon11", 0, "map_flag_anglosaxon11", banner_scale, 0),
  ("map_flag_anglosaxon12", 0, "map_flag_anglosaxon12", banner_scale, 0),
  ("map_flag_anglosaxon13", 0, "map_flag_anglosaxon13", banner_scale, 0),
  ("map_flag_anglosaxon14", 0, "map_flag_anglosaxon14", banner_scale, 0),
  ("map_flag_anglosaxon15", 0, "map_flag_anglosaxon15", banner_scale, 0),
  ("map_flag_anglosaxon16", 0, "map_flag_anglosaxon16", banner_scale, 0),
  ("map_flag_anglosaxon17", 0, "map_flag_anglosaxon17", banner_scale, 0),
  ("map_flag_anglosaxon18", 0, "map_flag_anglosaxon18", banner_scale, 0),
  ("map_flag_anglosaxon19", 0, "map_flag_anglosaxon19", banner_scale, 0),
  ("map_flag_anglosaxon20", 0, "map_flag_anglosaxon20", banner_scale, 0),
  ("map_flag_anglosaxon21", 0, "map_flag_anglosaxon21", banner_scale, 0),
  ("map_flag_anglosaxon201", 0, "map_flag_anglosaxon201", banner_scale, 0),
  ("map_flag_anglosaxon202", 0, "map_flag_anglosaxon202", banner_scale, 0),
  ("map_flag_anglosaxon203", 0, "map_flag_anglosaxon203", banner_scale, 0),
  ("map_flag_anglosaxon204", 0, "map_flag_anglosaxon204", banner_scale, 0),
  # ("map_flag_anglosaxon205", 0, "map_flag_anglosaxon205", banner_scale, 0),
  # ("map_flag_anglosaxon206", 0, "map_flag_anglosaxon206", banner_scale, 0),
  # ("map_flag_anglosaxon207", 0, "map_flag_anglosaxon207", banner_scale, 0),
  # ("map_flag_anglosaxon208", 0, "map_flag_anglosaxon208", banner_scale, 0),
  # ("map_flag_anglosaxon209", 0, "map_flag_anglosaxon209", banner_scale, 0),
  # ("map_flag_anglosaxon210", 0, "map_flag_anglosaxon210", banner_scale, 0),
  # ("map_flag_anglosaxon211", 0, "map_flag_anglosaxon211", banner_scale, 0),
  # ("map_flag_anglosaxon212", 0, "map_flag_anglosaxon212", banner_scale, 0),
  # ("map_flag_anglosaxon213", 0, "map_flag_anglosaxon213", banner_scale, 0),
  # ("map_flag_anglosaxon214", 0, "map_flag_anglosaxon214", banner_scale, 0),
  # ("map_flag_anglosaxon215", 0, "map_flag_anglosaxon215", banner_scale, 0),
  # ("map_flag_anglosaxon216", 0, "map_flag_anglosaxon216", banner_scale, 0),
  # ("map_flag_anglosaxon217", 0, "map_flag_anglosaxon217", banner_scale, 0),
  # ("map_flag_anglosaxon218", 0, "map_flag_anglosaxon218", banner_scale, 0),
  # ("map_flag_anglosaxon219", 0, "map_flag_anglosaxon219", banner_scale, 0),
  # ("map_flag_anglosaxon220", 0, "map_flag_anglosaxon220", banner_scale, 0),
  # ("map_flag_anglosaxon221", 0, "map_flag_anglosaxon221", banner_scale, 0),
  ("map_flag_briton01", 0, "map_flag_briton01", banner_scale, 0),
  ("map_flag_briton02", 0, "map_flag_briton02", banner_scale, 0),
  ("map_flag_briton03", 0, "map_flag_briton03", banner_scale, 0),
  ("map_flag_briton04", 0, "map_flag_briton04", banner_scale, 0),
  ("map_flag_briton05", 0, "map_flag_briton05", banner_scale, 0),
  ("map_flag_briton06", 0, "map_flag_briton06", banner_scale, 0),
  ("map_flag_briton07", 0, "map_flag_briton07", banner_scale, 0),
  ("map_flag_briton08", 0, "map_flag_briton08", banner_scale, 0),
  ("map_flag_briton09", 0, "map_flag_briton09", banner_scale, 0),
  ("map_flag_briton10", 0, "map_flag_briton10", banner_scale, 0),
  ("map_flag_briton11", 0, "map_flag_briton11", banner_scale, 0),
  ("map_flag_briton12", 0, "map_flag_briton12", banner_scale, 0),
  ("map_flag_briton13", 0, "map_flag_briton13", banner_scale, 0),
  ("map_flag_briton14", 0, "map_flag_briton14", banner_scale, 0),
  ("map_flag_briton15", 0, "map_flag_briton15", banner_scale, 0),
  ("map_flag_briton16", 0, "map_flag_briton16", banner_scale, 0),
  ("map_flag_briton17", 0, "map_flag_briton17", banner_scale, 0),
  ("map_flag_briton18", 0, "map_flag_briton18", banner_scale, 0),
  ("map_flag_briton19", 0, "map_flag_briton19", banner_scale, 0),
  ("map_flag_briton20", 0, "map_flag_briton20", banner_scale, 0),
  ("map_flag_briton21", 0, "map_flag_briton21", banner_scale, 0),
  ("map_flag_briton201", 0, "map_flag_briton201", banner_scale, 0),
  ("map_flag_briton202", 0, "map_flag_briton202", banner_scale, 0),
  ("map_flag_briton203", 0, "map_flag_briton203", banner_scale, 0),
  ("map_flag_briton204", 0, "map_flag_briton204", banner_scale, 0),
  ("map_flag_briton205", 0, "map_flag_briton205", banner_scale, 0),
  ("map_flag_briton206", 0, "map_flag_briton206", banner_scale, 0),
  ("map_flag_briton207", 0, "map_flag_briton207", banner_scale, 0),
  ("map_flag_briton208", 0, "map_flag_briton208", banner_scale, 0),
  ("map_flag_briton209", 0, "map_flag_briton209", banner_scale, 0),
  ("map_flag_briton210", 0, "map_flag_briton210", banner_scale, 0),
  ("map_flag_briton211", 0, "map_flag_briton211", banner_scale, 0),
  ("map_flag_briton212", 0, "map_flag_briton212", banner_scale, 0),
  ("map_flag_briton213", 0, "map_flag_briton213", banner_scale, 0),
  ("map_flag_briton214", 0, "map_flag_briton214", banner_scale, 0),
  ("map_flag_briton215", 0, "map_flag_briton215", banner_scale, 0),
  ("map_flag_briton216", 0, "map_flag_briton216", banner_scale, 0),
  ("map_flag_briton217", 0, "map_flag_briton217", banner_scale, 0),
  ("map_flag_briton218", 0, "map_flag_briton218", banner_scale, 0),
  ("map_flag_briton219", 0, "map_flag_briton219", banner_scale, 0),
  ("map_flag_briton220", 0, "map_flag_briton220", banner_scale, 0),
  ("map_flag_briton221", 0, "map_flag_briton221", banner_scale, 0),
  ("map_flag_irish01", 0, "map_flag_irish01", banner_scale, 0),
  ("map_flag_irish02", 0, "map_flag_irish02", banner_scale, 0),
  ("map_flag_irish03", 0, "map_flag_irish03", banner_scale, 0),
  ("map_flag_irish04", 0, "map_flag_irish04", banner_scale, 0),
  ("map_flag_irish05", 0, "map_flag_irish05", banner_scale, 0),
  ("map_flag_irish06", 0, "map_flag_irish06", banner_scale, 0),
  ("map_flag_irish07", 0, "map_flag_irish07", banner_scale, 0),
  ("map_flag_irish08", 0, "map_flag_irish08", banner_scale, 0),
  ("map_flag_irish09", 0, "map_flag_irish09", banner_scale, 0),
  ("map_flag_irish10", 0, "map_flag_irish10", banner_scale, 0),
  ("map_flag_irish11", 0, "map_flag_irish11", banner_scale, 0),
  ("map_flag_irish12", 0, "map_flag_irish12", banner_scale, 0),
  ("map_flag_irish13", 0, "map_flag_irish13", banner_scale, 0),
  ("map_flag_irish14", 0, "map_flag_irish14", banner_scale, 0),
  ("map_flag_irish15", 0, "map_flag_irish15", banner_scale, 0),
  ("map_flag_irish16", 0, "map_flag_irish16", banner_scale, 0),
  ("map_flag_irish17", 0, "map_flag_irish17", banner_scale, 0),
  ("map_flag_irish18", 0, "map_flag_irish18", banner_scale, 0),
  ("map_flag_irish19", 0, "map_flag_irish19", banner_scale, 0),
  ("map_flag_irish20", 0, "map_flag_irish20", banner_scale, 0),
  ("map_flag_irish21", 0, "map_flag_irish21", banner_scale, 0),
  ("map_flag_irish201", 0, "map_flag_irish201", banner_scale, 0),
  ("map_flag_irish202", 0, "map_flag_irish202", banner_scale, 0),
  ("map_flag_irish203", 0, "map_flag_irish203", banner_scale, 0),
  ("map_flag_irish204", 0, "map_flag_irish204", banner_scale, 0),
  ("map_flag_irish205", 0, "map_flag_irish205", banner_scale, 0),
  ("map_flag_irish206", 0, "map_flag_irish206", banner_scale, 0),
  ("map_flag_irish207", 0, "map_flag_irish207", banner_scale, 0),
  ("map_flag_irish208", 0, "map_flag_irish208", banner_scale, 0),
  ("map_flag_irish209", 0, "map_flag_irish209", banner_scale, 0),
  ("map_flag_irish210", 0, "map_flag_irish210", banner_scale, 0),
  ("map_flag_irish211", 0, "map_flag_irish211", banner_scale, 0),
  ("map_flag_irish212", 0, "map_flag_irish212", banner_scale, 0),
  ("map_flag_irish213", 0, "map_flag_irish213", banner_scale, 0),
  # ("map_flag_irish214", 0, "map_flag_irish214", banner_scale, 0),
  # ("map_flag_irish215", 0, "map_flag_irish215", banner_scale, 0),
  # ("map_flag_irish216", 0, "map_flag_irish216", banner_scale, 0),
  # ("map_flag_irish217", 0, "map_flag_irish217", banner_scale, 0),
  # ("map_flag_irish218", 0, "map_flag_irish218", banner_scale, 0),
  # ("map_flag_irish219", 0, "map_flag_irish219", banner_scale, 0),
  # ("map_flag_irish220", 0, "map_flag_irish220", banner_scale, 0),
  # ("map_flag_irish221", 0, "map_flag_irish221", banner_scale, 0),
  ("map_flag_pict01", 0, "map_flag_pict01", banner_scale, 0),
  ("map_flag_pict02", 0, "map_flag_pict02", banner_scale, 0),
  ("map_flag_pict03", 0, "map_flag_pict03", banner_scale, 0),
  ("map_flag_pict04", 0, "map_flag_pict04", banner_scale, 0),
  ("map_flag_pict05", 0, "map_flag_pict05", banner_scale, 0),
  ("map_flag_pict06", 0, "map_flag_pict06", banner_scale, 0),
  ("map_flag_pict07", 0, "map_flag_pict07", banner_scale, 0),
  ("map_flag_pict08", 0, "map_flag_pict08", banner_scale, 0),
  # ("map_flag_pict09", 0, "map_flag_pict09", banner_scale, 0),
  # ("map_flag_pict10", 0, "map_flag_pict10", banner_scale, 0),
  # ("map_flag_pict11", 0, "map_flag_pict11", banner_scale, 0),
  # ("map_flag_pict12", 0, "map_flag_pict12", banner_scale, 0),
  # ("map_flag_pict13", 0, "map_flag_pict13", banner_scale, 0),
  # ("map_flag_pict14", 0, "map_flag_pict14", banner_scale, 0),
  # ("map_flag_pict15", 0, "map_flag_pict15", banner_scale, 0),
  # ("map_flag_pict16", 0, "map_flag_pict16", banner_scale, 0),
  # ("map_flag_pict17", 0, "map_flag_pict17", banner_scale, 0),
  # ("map_flag_pict18", 0, "map_flag_pict18", banner_scale, 0),
  # ("map_flag_pict19", 0, "map_flag_pict19", banner_scale, 0),
  # ("map_flag_pict20", 0, "map_flag_pict20", banner_scale, 0),
  # ("map_flag_pict21", 0, "map_flag_pict21", banner_scale, 0),
  ("map_flag_viking01", 0, "map_flag_viking01", banner_scale, 0),
  ("map_flag_viking02", 0, "map_flag_viking02", banner_scale, 0),
  ("map_flag_viking03", 0, "map_flag_viking03", banner_scale, 0),
  ("map_flag_viking04", 0, "map_flag_viking04", banner_scale, 0),
  ("map_flag_viking05", 0, "map_flag_viking05", banner_scale, 0),
  ("map_flag_viking06", 0, "map_flag_viking06", banner_scale, 0),
  ("map_flag_viking07", 0, "map_flag_viking07", banner_scale, 0),
  ("map_flag_viking08", 0, "map_flag_viking08", banner_scale, 0),
  ("map_flag_viking09", 0, "map_flag_viking09", banner_scale, 0),
  ("map_flag_viking10", 0, "map_flag_viking10", banner_scale, 0),
  ("map_flag_viking11", 0, "map_flag_viking11", banner_scale, 0),
  ("map_flag_viking12", 0, "map_flag_viking12", banner_scale, 0),
  ("map_flag_viking13", 0, "map_flag_viking13", banner_scale, 0),
  ("map_flag_viking14", 0, "map_flag_viking14", banner_scale, 0),
  ("map_flag_viking15", 0, "map_flag_viking15", banner_scale, 0),
  ("map_flag_viking16", 0, "map_flag_viking16", banner_scale, 0),
  ("map_flag_viking17", 0, "map_flag_viking17", banner_scale, 0),
  ("map_flag_viking18", 0, "map_flag_viking18", banner_scale, 0),
  ("map_flag_viking19", 0, "map_flag_viking19", banner_scale, 0),
  ("map_flag_viking20", 0, "map_flag_viking20", banner_scale, 0),
  ("map_flag_viking21", 0, "map_flag_viking21", banner_scale, 0),
  ("map_flag_viking201", 0, "map_flag_viking201", banner_scale, 0),
  ("map_flag_viking202", 0, "map_flag_viking202", banner_scale, 0),
  ("map_flag_viking203", 0, "map_flag_viking203", banner_scale, 0),
  ("map_flag_viking204", 0, "map_flag_viking204", banner_scale, 0),
  ("map_flag_viking205", 0, "map_flag_viking205", banner_scale, 0),
  ("map_flag_viking206", 0, "map_flag_viking206", banner_scale, 0),
  ("map_flag_viking207", 0, "map_flag_viking207", banner_scale, 0),
  ("map_flag_viking208", 0, "map_flag_viking208", banner_scale, 0),
  ("map_flag_viking209", 0, "map_flag_viking209", banner_scale, 0),
  ("map_flag_viking210", 0, "map_flag_viking210", banner_scale, 0),
  ("map_flag_viking211", 0, "map_flag_viking211", banner_scale, 0),
  ("map_flag_viking212", 0, "map_flag_viking212", banner_scale, 0),
  ("map_flag_viking213", 0, "map_flag_viking213", banner_scale, 0),
  ("map_flag_viking214", 0, "map_flag_viking214", banner_scale, 0),
  ("map_flag_viking215", 0, "map_flag_viking215", banner_scale, 0),
  ("map_flag_viking216", 0, "map_flag_viking216", banner_scale, 0),
  # ("map_flag_viking217", 0, "map_flag_viking217", banner_scale, 0),
  # ("map_flag_viking218", 0, "map_flag_viking218", banner_scale, 0),
  # ("map_flag_viking219", 0, "map_flag_viking219", banner_scale, 0),
  # ("map_flag_viking220", 0, "map_flag_viking220", banner_scale, 0),
  # ("map_flag_viking221", 0, "map_flag_viking221", banner_scale, 0),
  ("map_flag_kingdom_a", 0, "map_flag_kingdom_a", banner_scale, 0),
  ("map_flag_kingdom_b", 0, "map_flag_kingdom_b", banner_scale, 0),
  ("map_flag_kingdom_c", 0, "map_flag_kingdom_c", banner_scale, 0),
  ("map_flag_kingdom_d", 0, "map_flag_kingdom_d", banner_scale, 0),
  ("map_flag_kingdom_e", 0, "map_flag_kingdom_e", banner_scale, 0),
  ("map_flag_kingdom_f", 0, "map_flag_kingdom_f", banner_scale, 0),
  ("map_flag_kingdom_g", 0, "map_flag_kingdom_g", banner_scale, 0),
  ("map_flag_kingdom_h", 0, "map_flag_kingdom_h", banner_scale, 0),
  ("map_flag_kingdom_i", 0, "map_flag_kingdom_i", banner_scale, 0),
  ("map_flag_kingdom_j", 0, "map_flag_kingdom_j", banner_scale, 0),
  ("map_flag_kingdom_k", 0, "map_flag_kingdom_k", banner_scale, 0),
  ("map_flag_kingdom_l", 0, "map_flag_kingdom_l", banner_scale, 0),
  ("map_flag_kingdom_ll", 0, "map_flag_kingdom_ll", banner_scale, 0),
  ("map_flag_kingdom_m", 0, "map_flag_kingdom_m", banner_scale, 0),
  ("map_flag_kingdom_n", 0, "map_flag_kingdom_n", banner_scale, 0),
  ("map_flag_kingdom_o", 0, "map_flag_kingdom_o", banner_scale, 0),
  ("map_flag_kingdom_p", 0, "map_flag_kingdom_p", banner_scale, 0),
  ("map_flag_kingdom_q", 0, "map_flag_kingdom_q", banner_scale, 0),
  ("map_flag_kingdom_r", 0, "map_flag_kingdom_r", banner_scale, 0),
  ("map_flag_kingdom_s", 0, "map_flag_kingdom_s", banner_scale, 0),
  ("map_flag_kingdom_t", 0, "map_flag_kingdom_t", banner_scale, 0),
  ("map_flag_default", 0, "map_flag_extra207", banner_scale, 0),
]
