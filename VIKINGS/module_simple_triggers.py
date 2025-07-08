from header_common import *
from header_operations import *
from header_parties import *
from header_items import *
from header_skills import *
from header_triggers import *
from header_troops import *
from header_music import *
from header_terrain_types import *	#added motomataru chief

from module_constants import *

####################################################################################################################
# Simple triggers are the alternative to old style triggers. They do not preserve state, and thus simpler to maintain.
#
#  Each simple trigger contains the following fields:
# 1) Check interval: How frequently this trigger will be checked
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference.
####################################################################################################################



simple_triggers = [
  
  # This trigger is deprecated. Use "script_game_event_party_encounter" in module_scripts.py instead
  (ti_on_party_encounter,
    [
  ]),
  
  
  # This trigger is deprecated. Use "script_game_event_simulate_battle" in module_scripts.py instead
  (ti_simulate_battle,
    [
  ]),
  
  
  (1,
    [
      (try_begin),
        (eq, "$training_ground_position_changed", 0),
        (assign, "$training_ground_position_changed", 1),
        (set_fixed_point_multiplier, 100),
        (position_set_x, pos0, 7050),
        (position_set_y, pos0, 7200),
        (party_set_position, "p_training_ground_3", pos0),
      (try_end),
      
      (gt,"$auto_besiege_town",0),
      (gt,"$g_player_besiege_town", 0),
      (ge, "$g_siege_method", 1),
      (store_current_hours, ":cur_hours"),
      (eq, "$g_siege_force_wait", 0),
      (ge, ":cur_hours", "$g_siege_method_finish_hours"),
      (neg|is_currently_night),
      (rest_for_hours, 0, 0, 0), #stop resting
  ]),
  
  
  (0,
    [
      (eq,"$g_player_is_captive",1),
      (eq, "$travel_town", 0),	#Player isn't travelling
      (gt, "$capturer_party", 0),
      (party_is_active, "$capturer_party"),
      (party_relocate_near_party, "p_main_party", "$capturer_party", 0),
  ]),
  
  
  #Auto-menu
  (0,
    [
      (try_begin),
        (gt, "$g_last_rest_center", 0),
        (party_get_battle_opponent, ":besieger_party", "$g_last_rest_center"),
        (gt, ":besieger_party", 0),
        (store_faction_of_party, ":encountered_faction", "$g_last_rest_center"),
        (store_relation, ":faction_relation", ":encountered_faction", "fac_player_faction"),
        (store_faction_of_party, ":besieger_party_faction", ":besieger_party"),
        (store_relation, ":besieger_party_relation", ":besieger_party_faction", "fac_player_faction"),
        (ge, ":faction_relation", 0),
        (lt, ":besieger_party_relation", 0),
        (start_encounter, "$g_last_rest_center"),
        (rest_for_hours, 0, 0, 0), #stop resting
      (else_try),
        (store_current_hours, ":cur_hours"),
        (assign, ":check", 0),
        (try_begin),
          (neq, "$g_check_autos_at_hour", 0),
          (ge, ":cur_hours", "$g_check_autos_at_hour"),
          (assign, ":check", 1),
          (assign, "$g_check_autos_at_hour", 0),
        (try_end),
        (this_or_next|eq, ":check", 1),
        (map_free),
        (try_begin),
          (ge,"$auto_menu",1),
          (jump_to_menu,"$auto_menu"),
          (assign,"$auto_menu",-1),
        (else_try),
          (ge,"$auto_enter_town",1),
          (start_encounter, "$auto_enter_town"),
        (else_try),
          (ge,"$auto_besiege_town",1),
          (start_encounter, "$auto_besiege_town"),
        (else_try),
          (ge,"$g_camp_mode", 1),
          (assign, "$g_camp_mode", 0),
          (assign, "$g_infinite_camping", 0),
          #motomataru chief fix camping on water	# We dont need this anymore..
          # (assign, "$g_player_icon_state", pis_normal),
          #(party_get_current_terrain,":terrain","p_main_party"),
          (try_begin),
            # (neq, ":terrain", 0),	#not rt_water
            # (neq, ":terrain", 7),	#not rt_river used as water terrain
            # (neq, ":terrain", 8),	#not rt_bridge used as water terrain
            (party_slot_eq, "p_main_party", slot_party_on_water, 0),
            (assign, "$g_player_icon_state", pis_normal),
          (else_try),
            (assign, "$g_player_icon_state", pis_ship),
          (try_end),
          #end motomataru fix camping on water
          
          (rest_for_hours, 0, 0, 0), #stop camping
          
          (display_message, "@Breaking camp..."),
        (try_end),
      (try_end),
  ]),
  
  ###anadido Siege warfare, if player take far place, then break siege
  (0.2,
    [
      (eq, "$g_empieza_asedio", 1),
      #(gt,"$auto_besiege_town",0),
      
      (ge,"$g_player_besiege_town", 0),
      # (ge, "$g_siege_method", 1),
      (str_clear, s10),
      
      (store_distance_to_party_from_party, ":distance", "$g_player_besiege_town", "p_main_party"),
      (try_begin),
        (ge, ":distance", 2),
        (str_store_party_name_link, s10, "$g_player_besiege_town"),
        (display_message, "str_your_men_break_off_the_siege_of_s10_to_follow_you"),
        (call_script, "script_lift_siege", "$g_player_besiege_town", 0),
        (assign, "$g_player_besiege_town", -1),
      (else_try),
        (ge, ":distance", 1),
        (str_store_party_name_link, s10, "$g_player_besiege_town"),
        (display_message, "str_if_you_get_too_far_from_s10_your_siege_will_end"),
      (else_try),
      (try_end),
  ]),
  ###acaba sieges menu chief
  
  #Notification menus
  (0,
    [
      (troop_slot_ge, "trp_notification_menu_types", 0, 1),
      (troop_get_slot, ":menu_type", "trp_notification_menu_types", 0),
      (troop_get_slot, "$g_notification_menu_var1", "trp_notification_menu_var1", 0),
      (troop_get_slot, "$g_notification_menu_var2", "trp_notification_menu_var2", 0),
      (jump_to_menu, ":menu_type"),
      (assign, ":end_cond", 2),
      (try_for_range, ":cur_slot", 1, ":end_cond"),
        (try_begin),
          (troop_slot_ge, "trp_notification_menu_types", ":cur_slot", 1),
          (val_add, ":end_cond", 1),
        (try_end),
        (store_sub, ":cur_slot_minus_one", ":cur_slot", 1),
        (troop_get_slot, ":local_temp", "trp_notification_menu_types", ":cur_slot"),
        (troop_set_slot, "trp_notification_menu_types", ":cur_slot_minus_one", ":local_temp"),
        (troop_get_slot, ":local_temp", "trp_notification_menu_var1", ":cur_slot"),
        (troop_set_slot, "trp_notification_menu_var1", ":cur_slot_minus_one", ":local_temp"),
        (troop_get_slot, ":local_temp", "trp_notification_menu_var2", ":cur_slot"),
        (troop_set_slot, "trp_notification_menu_var2", ":cur_slot_minus_one", ":local_temp"),
      (try_end),
  ]),
  
  #Music, #bandit_lair too
  (1,
    [
      (map_free),
      (call_script, "script_music_set_situation_with_culture", mtf_sit_travel),
      (try_begin), #bandit merchant reset money
        (troop_get_slot,":val","trp_bandit_lairmerchant",slot_troop_days_on_mission),
        (neq,":val",0),#0 = can ask to sing about player
        (val_sub,":val",1),
        (val_max,":val",0),#to clear negative values (errors)
        (troop_set_slot,"trp_bandit_lairmerchant",slot_troop_days_on_mission,":val"),
      (try_end),
  ]),
  
  (0,
    [
      #escort caravan quest auto dialog trigger
      (try_begin),
        (eq, "$caravan_escort_state", 1),
        (party_is_active, "$caravan_escort_party_id"),
        
        (store_distance_to_party_from_party, ":caravan_distance_to_destination","$caravan_escort_destination_town","$caravan_escort_party_id"),
        (lt, ":caravan_distance_to_destination", 2),
        
        (store_distance_to_party_from_party, ":caravan_distance_to_player","p_main_party","$caravan_escort_party_id"),
        (lt, ":caravan_distance_to_player", 5),
        
        (assign, "$talk_context", tc_party_encounter),
        (assign, "$g_encountered_party", "$caravan_escort_party_id"),
        (party_stack_get_troop_id, ":caravan_leader", "$caravan_escort_party_id", 0),
        (party_stack_get_troop_dna, ":caravan_leader_dna", "$caravan_escort_party_id", 0),
        
        (start_map_conversation, ":caravan_leader", ":caravan_leader_dna"),
      (try_end),
      
      (try_begin),
        (gt, "$g_reset_mission_participation", 1),
        
        (try_for_range, ":troop", active_npcs_begin, kingdom_ladies_end),
          (troop_set_slot, ":troop", slot_troop_mission_participation, 0),
        (try_end),
      (try_end),
  ]),
  
  (24,
    [
      #updating refugees in monasteries
      (try_for_range,":center","p_monasterio1","p_yourlair"),
        (party_get_slot,":val",":center",slot_center_volunteer_troop_type),
        (neq,":val",0),#0 = can recruit
        (val_sub,":val",1),
        (val_max,":val",0),#to clear negative values (errors)
        (party_set_slot,":center",slot_center_volunteer_troop_type,":val"),
      (try_end),
      #updating workers in farmsteads
      (try_for_range,":center","p_farmsteadsp1","p_hadrian_wall1"),
        (party_get_slot,":val",":center",slot_center_volunteer_troop_type),
        (neq,":val",0),#0 = can recruit
        (val_sub,":val",1),
        (val_max,":val",0),#to clear negative values (errors)
        (party_set_slot,":center",slot_center_volunteer_troop_type,":val"),
      (try_end),
      #updating berserkers in hof
      (try_for_range,":center","p_paganholysites1","p_oldpagan_hut"),
        (party_get_slot,":val",":center",slot_center_volunteer_troop_type),
        (neq,":val",0),#0 = can recruit
        (val_sub,":val",1),
        (val_max,":val",0),#to clear negative values (errors)
        (party_set_slot,":center",slot_center_volunteer_troop_type,":val"),
      (try_end),
      #updating minstrel player poem cooldowns
      (try_for_range,":troop",bardo_begin, bardo_end),
        (troop_get_slot,":val",":troop",slot_troop_days_on_mission),
        (neq,":val",0),#0 = can ask to sing about player
        (val_sub,":val",1),
        (val_max,":val",0),#to clear negative values (errors)
        (troop_set_slot,":troop",slot_troop_days_on_mission,":val"),
        (try_begin),
          (eq, ":val", 0),
          (try_begin),
            (troop_slot_eq, ":troop", slot_troop_current_mission, npc_mission_improve_relations),
            (troop_get_slot, ":mission_object", ":troop", slot_troop_mission_object),
            (is_between, ":mission_object", kingdom_ladies_begin, kingdom_ladies_end),
            (troop_get_slot, ":lady_reputation", ":mission_object", slot_lord_reputation_type),
            (call_script, "script_troop_get_player_relation",  ":mission_object"),
            (assign, ":relation", reg0),
            #				(troop_get_slot, ":relation", ":mission_object", slot_troop_player_relation),
            (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
            (val_div, ":player_renown", 6),
            (val_sub, ":player_renown", 40),
            (call_script, "script_troop_get_romantic_chemistry_with_troop", ":mission_object", "trp_player"),
            (assign, ":chemistry", reg0),
            (try_begin),
              (eq, ":lady_reputation", lrep_ambitious),
              (val_div, ":chemistry", 2),
              (val_mul, ":player_renown", 2),
            (else_try),
              (eq, ":lady_reputation", lrep_otherworldly),
              (val_mul, ":chemistry", 2),
              (val_div, ":player_renown", 2),
            (else_try),
              (eq, ":lady_reputation", lrep_adventurous),
              (val_mul, ":chemistry", 3),
              (val_div, ":chemistry", 2),
              (val_div, ":player_renown", 2),
            (else_try),
              (eq, ":lady_reputation", lrep_moralist),
              (val_div, ":chemistry", 2),
              (val_div, ":player_renown", 2),
            (try_end),
            (store_add, ":modifier", ":chemistry", ":player_renown"),
            (val_add, ":modifier", ":relation"),
            (store_random_in_range, ":rand", 1,4),
            (try_begin),
              (lt, ":modifier", 0),
              (val_mul, ":rand", -1),
              (str_store_troop_name, s33, ":mission_object"),
              (display_message, "@The poem the bard had written for {s33} didn't seem to work very well."),
              (call_script, "script_change_player_relation_with_troop", ":mission_object", ":rand"),
              (tutorial_box, "@The poem the bard had written for {s33} didn't seem to work very well.", "@Poem for a lady"),
            (else_try),
              (gt, ":modifier", 0),
              (str_store_troop_name, s33, ":mission_object"),
              (display_message, "@{s33} seemed to like the poem the bard had written for her."),
              (call_script, "script_change_player_relation_with_troop", ":mission_object", ":rand"),
              (tutorial_box, "@{s33} seemed to like the poem the bard had written for her.", "@Poem for a lady"),
            (try_end),
          (else_try),
            (troop_slot_eq, ":troop", slot_troop_current_mission, npc_mission_seek_recognition),
            (store_random_in_range, ":rand", 2,6),
            (display_message, "@The bard's poem about you seems to be spreading through the land."),
            (tutorial_box, "@The bard's poem about you seems to be spreading through the land.", "@Fame spreads"),
            (call_script, "script_change_troop_renown", "trp_player", ":rand"),
          (try_end),
          (troop_set_slot, ":troop", slot_troop_current_mission, -1),
        (try_end),
      (try_end),
      (try_for_range,":troop","trp_bardo_lair","trp_quastuosa_lair1"),
        (troop_get_slot,":val",":troop",slot_troop_days_on_mission),
        (neq,":val",0),#0 = can ask to sing about player
        (val_sub,":val",1),
        (val_max,":val",0),#to clear negative values (errors)
        (troop_set_slot,":troop",slot_troop_days_on_mission,":val"),
        (try_begin),
          (eq, ":val", 0),
          (try_begin),
            (this_or_next|eq, ":troop", "trp_bardo_lair"),
            (eq, ":troop", "trp_skald_lair"),
            (troop_slot_eq, ":troop", slot_troop_current_mission, npc_mission_seek_recognition),
            (store_random_in_range, ":rand", 2,6),
            (display_message, "@The bard's poem about you seems to be spreading through the land."),
            (tutorial_box, "@The bard's poem about you seems to be spreading through the land.", "@Fame spreads"),
            (call_script, "script_change_troop_renown", "trp_player", ":rand"),
          (try_end),
        (try_end),
      (try_end),
      # Wife wives
      (try_for_range,":troop","trp_knight_1_1_wife", "trp_heroes_end"),
        (troop_slot_eq, ":troop", slot_troop_spouse, "trp_player"),
        (troop_get_slot,":val",":troop",slot_troop_days_on_mission),
        (neq,":val",0),#0
        (val_sub,":val",1),
        (val_max,":val",0),#to clear negative values (errors)
        (troop_set_slot,":troop",slot_troop_days_on_mission,":val"),
      (try_end),
      # Happy widows
      (try_for_range,":troop",quastuosa_begin, quastuosa_end),
        (troop_get_slot,":val",":troop",slot_troop_days_on_mission),
        (neq,":val",0),#0 = can ask to sing about player
        (val_sub,":val",1),
        (val_max,":val",0),#to clear negative values (errors)
        (troop_set_slot,":troop",slot_troop_days_on_mission,":val"),
      (try_end),
      #Sacerdotes
      (try_for_range, ":troop",sacerdote_begin, sacerdote_end),
        (troop_get_slot,":val",":troop",slot_troop_days_on_mission),
        (neq,":val",0),#0 = can ask to sing about player
        (val_sub,":val",1),
        (val_max,":val",0),#to clear negative values (errors)
        (troop_set_slot,":troop",slot_troop_days_on_mission,":val"),
      (try_end),
      # pagan priets
      (try_for_range, ":troop",pagano_begin, pagano_end),
        (troop_get_slot,":val",":troop",slot_troop_days_on_mission),
        (neq,":val",0),#0 = can ask to sing about player
        (val_sub,":val",1),
        (val_max,":val",0),#to clear negative values (errors)
        (troop_set_slot,":troop",slot_troop_days_on_mission,":val"),
      (try_end),
      #Lair priests
      (try_begin),
        (troop_get_slot,":val","trp_pagano_lair",slot_troop_days_on_mission),
        (neq,":val",0),#0 = can ask to sing about player
        (val_sub,":val",1),
        (val_max,":val",0),#to clear negative values (errors)
        (troop_set_slot,"trp_pagano_lair",slot_troop_days_on_mission,":val"),
      (try_end),
      # Lair whores
      (try_for_range, ":troop","trp_quastuosa_lair1", "trp_lair_barber1"),
        (troop_get_slot,":val",":troop",slot_troop_days_on_mission),
        (neq,":val",0),#0 = can ask to sing about player
        (val_sub,":val",1),
        (val_max,":val",0),#to clear negative values (errors)
        (troop_set_slot,":troop",slot_troop_days_on_mission,":val"),
      (try_end),
      (try_begin),
        (troop_get_slot,":val","trp_sacerdote_lair",slot_troop_days_on_mission),
        (neq,":val",0),#0 = can ask to sing about player
        (val_sub,":val",1),
        (val_max,":val",0),#to clear negative values (errors)
        (troop_set_slot,"trp_sacerdote_lair",slot_troop_days_on_mission,":val"),
      (try_end),
      (try_begin),
        (troop_get_slot,":val","trp_saxon_priest",slot_troop_days_on_mission),
        (neq,":val",0),#0 = can ask to sing about player
        (val_sub,":val",1),
        (val_max,":val",0),#to clear negative values (errors)
        (troop_set_slot,"trp_saxon_priest",slot_troop_days_on_mission,":val"),
      (try_end),
      (try_begin),
        (troop_get_slot,":val","trp_briton_priest",slot_troop_days_on_mission),
        (neq,":val",0),#0 = can ask to sing about player
        (val_sub,":val",1),
        (val_max,":val",0),#to clear negative values (errors)
        (troop_set_slot,"trp_briton_priest",slot_troop_days_on_mission,":val"),
      (try_end),
      (try_begin),
        (troop_get_slot,":val","trp_angle_priest",slot_troop_days_on_mission),
        (neq,":val",0),#0 = can ask to sing about player
        (val_sub,":val",1),
        (val_max,":val",0),#to clear negative values (errors)
        (troop_set_slot,":troop",slot_troop_days_on_mission,":val"),
      (try_end),
      (try_begin),
        (troop_get_slot,":val","trp_irish_priest",slot_troop_days_on_mission),
        (neq,":val",0),#0 = can ask to sing about player
        (val_sub,":val",1),
        (val_max,":val",0),#to clear negative values (errors)
        (troop_set_slot,"trp_irish_priest",slot_troop_days_on_mission,":val"),
      (try_end),
      (try_begin),
        (troop_get_slot,":val","trp_scotch_priest",slot_troop_days_on_mission),
        (neq,":val",0),#0 = can ask to sing about player
        (val_sub,":val",1),
        (val_max,":val",0),#to clear negative values (errors)
        (troop_set_slot,"trp_scotch_priest",slot_troop_days_on_mission,":val"),
      (try_end),
      (try_begin),
        (troop_get_slot,":val","trp_norse_priest",slot_troop_days_on_mission),
        (neq,":val",0),#0 = can ask to sing about player
        (val_sub,":val",1),
        (val_max,":val",0),#to clear negative values (errors)
        (troop_set_slot,"trp_norse_priest",slot_troop_days_on_mission,":val"),
      (try_end),
      (try_begin),
        (troop_get_slot,":val","trp_follower_woman",slot_troop_days_on_mission),
        (neq,":val",0),#0 = can ask to sing about player
        (val_sub,":val",1),
        (val_max,":val",0),#to clear negative values (errors)
        (troop_set_slot,"trp_follower_woman",slot_troop_days_on_mission,":val"),
      (try_end),
      ##	(try_begin), #bandit merchant
      ##		(troop_get_slot,":val","trp_bandit_lairmerchant",slot_troop_days_on_mission),
      ##		(neq,":val",0),#0 = can ask to sing about player
      ##		(val_sub,":val",1),
      ##		(val_max,":val",0),#to clear negative values (errors)
      ##		(troop_set_slot,"trp_bandit_lairmerchant",slot_troop_days_on_mission,":val"),
      ##	(try_end),
      # Lair priests
      # travelers
      (try_for_range,":troop",tavern_travelers_begin, tavern_travelers_end),
        (troop_get_slot,":val",":troop",slot_troop_days_on_mission),
        (neq,":val",0),
        (val_sub,":val",1),
        (val_max,":val",0),
        #		(assign, reg44, ":val"),
        #		(display_message, "@Days remaining {reg44}"),
        (troop_set_slot,":troop",slot_troop_days_on_mission,":val"),
        (try_begin),
          (eq, ":val", 0),
          #			(troop_get_slot, ":mission", ":troop", slot_troop_current_mission),
          #			(assign, reg43, ":mission"),
          #			(display_message,"@Mission is {reg43}"),
          (try_begin),
            (troop_slot_eq, ":troop", slot_troop_current_mission, npc_mission_improve_relations),
            (troop_get_slot, ":mission_object", ":troop", slot_troop_mission_object),
            (str_store_troop_name, s32, ":mission_object"),
            #			(display_message, "@Mission object is {s32}"),
            (troop_get_slot, ":target", ":troop", slot_troop_mission_target),
            (gt, ":mission_object", 0),
            (try_begin),
              (gt, ":target", 0),
              (call_script, "script_troop_get_relation_with_troop", ":mission_object", ":target"),
              (str_store_troop_name, s31, ":target"),
              #					(display_message, "@Rels are {reg0}"),
              (assign, ":rels", reg0),
              (val_add, ":rels", 100),
              (try_begin),
                (le, ":rels", 1),
                (assign, ":rels", 3),
              (try_end),
              #					(display_message, "@testing rels - target is {s31}"),
              (store_random_in_range, ":random", 0,":rels"),
              (try_begin),
                (lt, ":random", 35),
                (store_random_in_range, ":change", -8,-3),
                (call_script, "script_troop_change_relation_with_troop", ":mission_object", ":target", ":change"),
                (store_random_in_range, ":mess", 0,4),
                (try_begin),
                  (eq, ":mess", 0),
                  (str_store_string, s33, "@People say that {s31} found a buried Viking hoard on {s32}'s property. The lords came to blows over its ownership."),
                (else_try),
                  (eq, ":mess", 1),
                  (str_store_string, s33, "@People say that {s31} or his servants are stealing cattle from {s32}'s property. That made {s32} furious."),
                (else_try),
                  (eq, ":mess", 2),
                  (str_store_string, s33, "@People say that {s31} served one of {s32}'s bodyguards a horn of poisoned mead. {s32} is infuriated."),
                (else_try),
                  (str_store_string, s33, "@People say that {s31} tried to bribe some of {s32}'s bodyguards to get access to the household, but {s32} found out."),
                (try_end),
              (else_try),
                (str_store_string, s33, "@People say that a rumor spread by an unknown traveller failed to incite enmity between {s31} and {s32}."),
              (try_end),
              (display_message, "@{s33}"),
              (tutorial_box, "@{s33}", "@Rumors"),
              (store_random_in_range, ":rand", 0, 100),
              (try_begin),
                (is_between, ":rand", 20, 40),
                (call_script, "script_troop_change_relation_with_troop", ":mission_object", "trp_player", -2),
                (call_script, "script_troop_change_relation_with_troop", ":target", "trp_player", -2),
                (display_message, "@{playername} is believed to be behind the recent derogatory rumors involving {s32} and {s31}."),
              (try_end),
            (else_try),
              (le, ":target", 0),
              (store_random_in_range, ":random", 0,100),
              (try_begin),
                (is_between, ":random", 30, 60),
                (troop_get_slot, ":renown", ":mission_object", slot_troop_renown),
                (store_faction_of_troop, ":faction",  ":mission_object"),
                (store_div, ":upper_limit", ":renown", 40),
                (val_mul, ":upper_limit", -1),
                (store_random_in_range, ":change", ":upper_limit",-1),
                (val_add, ":renown", ":change"),
                (try_begin),
                  (faction_slot_eq, ":faction", slot_faction_leader, ":mission_object"),
                  (val_max, ":renown", 600),
                (else_try),
                  (val_max, ":renown", 400),
                (try_end),
                (troop_set_slot, ":mission_object", slot_troop_renown, ":renown"),
                (troop_get_slot, ":controversy",  ":mission_object", slot_troop_controversy),
                (val_add, ":controversy", 2),
                (troop_set_slot, ":mission_object", slot_troop_controversy, ":controversy"),
                (store_random_in_range, ":mess", 0,4),
                (try_begin),
                  (eq, ":mess", 0),
                  (str_store_string, s33, "@A recent rumor alleges that {s32} hides behind his bodyguards in battles."),
                (else_try),
                  (eq, ":mess", 1),
                  (str_store_string, s33, "@A recent rumor alleges that {s32} is practicing some kind of perverted rituals in his mead hall."),
                (else_try),
                  (eq, ":mess", 2),
                  (str_store_string, s33, "@A recent rumor alleges that {s32} is very fond of his new mare, if you know what I mean."),
                (else_try),
                  (str_store_string, s33, "@A recent rumor alleges that {s32} would rather wield a drinking horn than a sword."),
                (try_end),
              (else_try),
                (str_store_string, s33, "@People say that a rumor spread by an unknown traveller about {s32} failed to damage his reputation."),
              (try_end),
              (display_message, "@{s33}"),
              (tutorial_box, "@{s33}", "@Rumors"),
              (store_random_in_range, ":rand", 0, 100),
              (try_begin),
                (is_between, ":rand", 15, 35),
                (call_script, "script_troop_change_relation_with_troop", ":mission_object", "trp_player", -2),
                (display_message, "@{playername} is believed to be behind the recent rumors about {s32}'s indiscretions."),
              (try_end),
            (try_end),
            #			(try_end),
          (else_try),
            (troop_slot_eq, ":troop", slot_troop_current_mission, npc_mission_test_waters),
            (troop_get_slot, ":mission_object", ":troop", slot_troop_mission_object),
            (gt, ":mission_object", 0),
            (str_store_troop_name, s32, ":mission_object"),
            (store_troop_faction, ":faction_no", ":mission_object"),
            (faction_get_slot, ":king", ":faction_no", slot_faction_leader),
            (call_script, "script_troop_get_relation_with_troop", ":mission_object", ":king"),
            (str_store_troop_name, s31, ":king"),
            (assign, ":rels", reg0),
            (val_add, ":rels", 100),
            (try_begin),
              (le, ":rels", 1),
              (assign, ":rels", 3),
            (try_end),
            (store_random_in_range, ":random", 0,":rels"),
            (try_begin),
              (lt, ":random", 32),
              (store_random_in_range, ":change", -9,-2),
              (call_script, "script_troop_change_relation_with_troop", ":mission_object", ":king", ":change"),
              (str_store_string, s33, "@A recent rumor spread by an unknown traveller alleges that {s32} is intriguing against {s31}."),
            (else_try),
              (str_store_string, s33, "@People say that a rumor spread by an unknown traveller about {s32} being a disloyal vassal failed to incite enmity between {s32} and {s31}."),
            (try_end),
            (display_message, "@{s33}"),
            (tutorial_box, "@{s33}", "@Rumors"),
            (store_random_in_range, ":rand", 0, 100),
            (try_begin),
              (is_between, ":rand", 25, 45),
              (call_script, "script_troop_change_relation_with_troop", ":mission_object", "trp_player", -2),
              (call_script, "script_troop_change_relation_with_troop", ":king", "trp_player", -2),
              (display_message, "@{playername} is believed to be behind the recent rumors about {s32}'s disloyalty."),
            (try_end),
          (try_end),
          (troop_set_slot, ":troop", slot_troop_current_mission, -1),
          (troop_set_slot, ":troop", slot_troop_mission_object, -1),
          (troop_set_slot, ":troop", slot_troop_mission_target, -1),
        (try_end),
      (try_end),
      # Kingdom ladies
      (try_for_range,":troop",kingdom_ladies_begin, kingdom_ladies_end),
        (troop_get_slot,":val",":troop",slot_troop_days_on_mission),
        (neq,":val",0),
        (val_sub,":val",1),
        (val_max,":val",0),
        #		(assign, reg44, ":val"),
        #		(display_message, "@Days remaining {reg44}"),
        (troop_set_slot,":troop",slot_troop_days_on_mission,":val"),
        (try_begin),
          (eq, ":val", 0),
          #			(troop_get_slot, ":mission", ":troop", slot_troop_current_mission),
          #			(assign, reg43, ":mission"),
          #			(display_message,"@Mission is {reg43}"),
          (try_begin),
            (troop_slot_eq, ":troop", slot_troop_current_mission, npc_mission_improve_relations),
            (troop_get_slot, ":mission_object", ":troop", slot_troop_mission_object),
            (str_store_troop_name, s32, ":mission_object"),
            #				(display_message, "@Mission object is {s32}"),
            (troop_get_slot, ":target", ":troop", slot_troop_mission_target),
            (str_store_troop_name, s31, ":target"),
            (troop_get_slot, ":amount", ":troop", slot_troop_mission_amount),
            (gt, ":mission_object", 0),
            (try_begin),
              (eq, ":amount", 120),
              (store_random_in_range, ":random", 0,100),
              (try_begin),
                (is_between, ":random", 25, 55),
                (store_random_in_range, ":change", -6,-3),
                (call_script, "script_troop_change_relation_with_troop", ":mission_object", ":target", ":change"),
                (str_store_string, s33, "@It seems that {s31} has found recent stories about {s32}'s infidelity plausible."),
              (else_try),
                (str_store_string, s33, "@It appears {s31} has dismissed recent stories about {s32}'s infidelity as nothing but his enemies' gossip."),
              (try_end),
              (display_message, "@{s33}"),
              (tutorial_box, "@{s33}", "@Rumors"),
            (else_try),
              (eq, ":amount", 200),
              (store_random_in_range, ":random", 0,100),
              (try_begin),
                (is_between, ":random", 35, 70),
                (store_random_in_range, ":change", -9,-5),
                (call_script, "script_troop_change_relation_with_troop", ":mission_object", ":target", ":change"),
                (str_store_string, s33, "@It seems that {s31} has found recent stories about {s32}'s disloyalty quite plausible."),
              (else_try),
                (str_store_string, s33, "@It appears that {s31} has dismissed recent stories about {s32}'s disloyalty as nothing but his enemies' gossip."),
              (try_end),
              (display_message, "@{s33}"),
              (tutorial_box, "@{s33}", "@Rumors"),
            (else_try),
              (eq, ":amount", 1500),
              (store_random_in_range, ":random", 0,100),
              (try_begin),
                (lt, ":random", 45),
                (store_random_in_range, ":change", -25,-15),
                (call_script, "script_troop_change_relation_with_troop", ":mission_object", ":target", ":change"),
                (str_store_string, s33, "@It seems that {s31} was not amused after {s32} was found to be involved in a cattle-thieving scheme."),
              (else_try),
                (str_store_string, s33, "@It appears {s32} had managed to avoid being linked to a recent murder, and his relations with {s31} didn't suffer."),
              (try_end),
              (display_message, "@{s33}"),
              (tutorial_box, "@{s33}", "@Rumors"),
            (try_end),
          (try_end),
          (troop_set_slot, ":troop", slot_troop_current_mission, -1),
          (troop_set_slot, ":troop", slot_troop_mission_object, -1),
          (troop_set_slot, ":troop", slot_troop_mission_target, -1),
          (troop_set_slot, ":troop", slot_troop_mission_amount, -1),
        (try_end),
      (try_end),
  ]),
  
  #STrig 10
  (.04, #Locate kingdom ladies
    [
      #change location for ONE ladies
      (store_random_in_range, ":troop_id", kingdom_ladies_begin, kingdom_ladies_end),
      (neg|troop_slot_ge, ":troop_id", slot_troop_prisoner_of_party, 0),
      (call_script, "script_get_kingdom_lady_social_determinants", ":troop_id"),
      (assign, ":location", reg1),
      (troop_set_slot, ":troop_id", slot_troop_cur_center, ":location"),
      # (try_end),
  ]),
  
  
  (2, #Error check for multiple parties on the map
    [
      (eq, "$cheat_mode", 1),
      (assign, ":debug_menu_noted", 0),
      (try_for_parties, ":party_no"),
        (gt, ":party_no", "p_spawn_points_end"),
        
        (party_get_num_companion_stacks, reg4, ":party_no"),
        (gt, reg4, 0),
        
        (party_stack_get_troop_id, ":commander", ":party_no", 0),
        (is_between, ":commander", active_npcs_begin, active_npcs_end),
        
        (troop_get_slot, ":commander_party", ":commander", slot_troop_leaded_party),
        (neq, ":party_no", ":commander_party"),
        
        (assign, reg4, ":party_no"),
        (assign, reg5, ":commander_party"),
        (str_store_troop_name, s3, ":commander"),
        (party_get_template_id, reg6, ":party_no"),
        (display_message, "str_s3_commander_of_party_reg4_which_is_not_his_troop_leaded_party_reg5"),
        (assign, ":debug_menu_noted", 1),
      (try_end),
          
      (eq, ":debug_menu_noted", 1),
      (str_store_string, s65, "str_party_with_commander_mismatch__check_log_for_details_"),
      (call_script, "script_add_notification_menu", "mnu_debug_alert_from_s65", 0, 0),
    ]),
    
    
    (24, #Kingdom ladies send messages
      [
        (try_begin),
          (neg|check_quest_active, "qst_visit_lady"),
          (neg|troop_slot_ge, "trp_player", slot_troop_prisoner_of_party, 1),
          (neg|troop_slot_ge, "trp_player", slot_troop_spouse, active_npcs_begin),
          
          (assign, ":lady_not_visited_longest_time", -1),
          (assign, ":longest_time_without_visit", 120), #five days
          (try_for_range, ":troop_id", kingdom_ladies_begin, kingdom_ladies_end),
            (troop_set_slot, ":troop_id", slot_troop_refused, 0),
            #set up message for ladies the player is courting
            (troop_slot_ge, ":troop_id", slot_troop_met, 2),
            (neg|troop_slot_eq, ":troop_id", slot_troop_met, 4),
            (troop_slot_eq, ":troop_id", slot_lady_no_messages, 0),
            (troop_get_slot, ":location", ":troop_id", slot_troop_cur_center),
            (is_between, ":location", walled_centers_begin, walled_centers_end),
            (call_script, "script_troop_get_relation_with_troop", "trp_player", ":troop_id"),
            (gt, reg0, 1),
            (store_current_hours, ":hours_since_last_visit"),
            (troop_get_slot, ":last_visit_hour", ":troop_id", slot_troop_last_talk_time),
            (val_sub, ":hours_since_last_visit", ":last_visit_hour"),
            (gt, ":hours_since_last_visit", ":longest_time_without_visit"),
            (assign, ":longest_time_without_visit", ":hours_since_last_visit"),
            (assign, ":lady_not_visited_longest_time", ":troop_id"),
            (assign, ":visit_lady_location", ":location"),
          (try_end),
          (try_begin),
            (gt, ":lady_not_visited_longest_time", 0),
            (call_script, "script_add_notification_menu", "mnu_notification_lady_requests_visit", ":lady_not_visited_longest_time", ":visit_lady_location"),
          (try_end),
          
        (try_end),
    ]),
    
    
    #Player raiding a village
    # This trigger will check if player's raid has been completed and will lead control to village menu.
    (1,
      [
        (ge,"$g_player_raiding_village",1),
        (try_begin),
          (neq, "$g_player_is_captive", 0),
          #(rest_for_hours, 0, 0, 0), #stop resting - abort
          (assign,"$g_player_raiding_village",0),
        (else_try),
          (map_free), #we have been attacked during raid
          (assign,"$g_player_raiding_village",0),
        (else_try),
          # (this_or_next|party_slot_eq, "$g_player_raiding_village", slot_village_state, svs_deserted),
          (party_slot_eq, "$g_player_raiding_village", slot_village_state, svs_looted),
          (start_encounter, "$g_player_raiding_village"),
          (rest_for_hours, 0),
          (assign,"$g_player_raiding_village",0),
          (assign,"$g_player_raid_complete",1),
        (else_try),
          (party_slot_eq, "$g_player_raiding_village", slot_village_state, svs_being_raided),
          (rest_for_hours, 3, 5, 1), #rest while attackable
        (else_try),
          (rest_for_hours, 0, 0, 0), #stop resting - abort
          (assign,"$g_player_raiding_village",0),
          (assign,"$g_player_raid_complete",0),
        (try_end),
    ]),
    
    # Oath fulfilled -- ie, mercenary contract expired?
    (24,
      [
        (le, "$auto_menu", 0),
        (gt, "$players_kingdom", 0),
        (neq, "$players_kingdom", "fac_player_supporters_faction"),
        (eq, "$player_has_homage", 0),
        
        (troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
        
        #A player bound to a kingdom by marriage will not have the contract expire. This should no longer be the case, as I've counted wives as having homage, but is in here as a fallback
        (assign, ":player_has_marriage_in_faction", 0),
        (try_begin),
          (is_between, ":player_spouse", active_npcs_begin, active_npcs_end),
          (store_faction_of_troop, ":spouse_faction", ":player_spouse"),
          (eq, ":spouse_faction", "$players_kingdom"),
          (assign, ":player_has_marriage_in_faction", 1),
        (try_end),
        (eq, ":player_has_marriage_in_faction", 0),
        
        (store_current_day, ":cur_day"),
        (gt, ":cur_day", "$mercenary_service_next_renew_day"),
        (jump_to_menu, "mnu_oath_fulfilled"),
    ]),
    
    # Reducing luck by 1 in every 180 hours
    (180,
      [
        (val_sub, "$g_player_luck", 1),
        (val_max, "$g_player_luck", 0),
    ]),
    
    #courtship reset
    (72,
      [
        (assign, "$lady_flirtation_location", 0),
    ]),
    
    #reset time to spare
    (4,
      [
        (assign, "$g_time_to_spare", 1),
        
        (try_begin),
          (troop_slot_ge, "trp_player", slot_troop_spouse, active_npcs_begin),
          (assign, "$g_player_banner_granted", 1),
        (try_end),
        
    ]),
    
    
    # Banner selection menu
    (24,
      [
        (eq, "$g_player_banner_granted", 1),
        (troop_slot_eq, "trp_player", slot_troop_banner_scene_prop, 0),
        (le,"$auto_menu",0),
        #normal_banner_begin
        (start_presentation, "prsnt_banner_selection"),
        #custom_banner_begin
        #    (start_presentation, "prsnt_custom_banner"),
    ]),
    
    # Party Morale: Move morale towards target value.
    (24,
      [
        (call_script, "script_get_player_party_morale_values"),
        (assign, ":target_morale", reg0),
        (party_get_morale, ":cur_morale", "p_main_party"),
        (store_sub, ":dif", ":target_morale", ":cur_morale"),
        (store_div, ":dif_to_add", ":dif", 5),
        (store_mul, ":dif_to_add_correction", ":dif_to_add", 5),
        (try_begin),#finding ceiling of the value
          (neq, ":dif_to_add_correction", ":dif"),
          (try_begin),
            (gt, ":dif", 0),
            (val_add, ":dif_to_add", 1),
          (else_try),
            (val_sub, ":dif_to_add", 1),
          (try_end),
        (try_end),
        (val_add, ":cur_morale", ":dif_to_add"),
        (party_set_morale, "p_main_party", ":cur_morale"),
    ]),
    
    #STrig 20
    #Weekly trigger no loops
    (24 * 7,
      [
        #Pay day.
        # (assign, "$g_presentation_lines_to_display_begin", 0),
        # (assign, "$g_presentation_lines_to_display_end", 15),
        (assign, "$g_apply_budget_report_to_gold", 1),
        (try_begin),
          (eq, "$g_infinite_camping", 0),
          (start_presentation, "prsnt_budget_report"),
        (try_end),
        
        #winter = morale and renown penalty
        (try_begin),
          (this_or_next|eq, "$g_cur_month", 12),
          (this_or_next|eq, "$g_cur_month", 1),
          (eq, "$g_cur_month", 2),
          
          (display_message, "@Winter is the worst time for war. It's cold, it rains too much and food is scarce. In winter, men would rather shelter by the fire than campaign. Watch your morale and your food stores."),
          (call_script, "script_change_player_party_morale", -5),
        (try_end),
        #invierno penalty chief
    ]),
    
    #walled centers weekly ON AVERAGE
    (1.4,
      [
        #Party AI: pruning some of the prisoners in each center (once a week)
        (store_random_in_range, ":center_no", walled_centers_begin, walled_centers_end),
        (neg|party_slot_eq, ":center_no", slot_town_lord, "trp_player"), #center does not belong to player.
        (party_get_num_prisoner_stacks, ":num_prisoner_stacks",":center_no"),
        (try_for_range_backwards, ":stack_no", 0, ":num_prisoner_stacks"),
          (party_prisoner_stack_get_troop_id, ":stack_troop",":center_no",":stack_no"),
          (neg|troop_is_hero, ":stack_troop"),
          (party_prisoner_stack_get_size, ":stack_size",":center_no",":stack_no"),
          (gt, ":stack_size", 0),
          (store_random_in_range, ":rand_no", 10, 60),#changed from 0..40
          (val_mul, ":stack_size", ":rand_no"),
          (val_div, ":stack_size", 100),
          (try_begin),
            (eq, ":stack_size", 0),
            (val_add, ":stack_size", 1),
          (try_end),
          (party_get_slot, ":cur_wealth", ":center_no", slot_town_wealth),
          (store_mul,":prisoner_sell",":stack_size",20), #20 peningas per prisoner
          (val_add,":cur_wealth",":prisoner_sell"),
          (party_set_slot, ":center_no", slot_town_wealth, ":cur_wealth"),
          (party_remove_prisoners, ":center_no", ":stack_troop", ":stack_size"),
        (try_end),
        # Add AI option
        (options_get_campaign_ai, ":reduce_campaign_ai"), #moto chief
        (assign, ":modifier", 1),
        (try_begin),
          (eq, ":reduce_campaign_ai", 0), #hard
          (assign, ":modifier", 3),
        (else_try),
          (eq, ":reduce_campaign_ai", 1), #moderate
          (assign, ":modifier", 2),
        (else_try),
          (eq, ":reduce_campaign_ai", 2), #easy
          (assign, ":modifier", 1),
        (try_end),
        (val_mul, ":modifier", 480),#1440 max
        (party_get_slot, ":cur_wealth", ":center_no", slot_town_wealth),
        (party_get_slot, ":prosperity", ":center_no", slot_town_prosperity),
        (assign, ":no_works", 1),
        (try_begin),
          (this_or_next|party_slot_ge, ":center_no", slot_center_blockaded, 2),    #center blockaded (by player) OR
          (party_slot_ge, ":center_no", slot_center_is_besieged_by, 1), #center besieged by someone else
          (assign, ":no_works", 0),
        (try_end),
        (try_begin),
          (eq, ":no_works", 1),
          (le, ":prosperity", 72),
          (store_mul, ":added_wealth", ":prosperity", ":prosperity"), #5144 max
        (else_try),
          (eq, ":no_works", 1),
          (store_mul, ":added_wealth", ":prosperity", 73), #7300 max
        (else_try),
          (eq, ":no_works", 0),
          (store_div, ":adj_prosperity",":prosperity", 2),
          (store_mul, ":added_wealth", ":adj_prosperity", ":adj_prosperity"),
        (try_end),
        (try_begin),
          (party_slot_ge, ":center_no", slot_town_lord, 1), #center belongs to someone.
          (val_add, ":added_wealth", ":modifier"), #8740 max
          (try_begin),
            (party_slot_eq, ":center_no", slot_party_type, spt_town),#13110 max
            (val_mul, ":added_wealth", 3),
            (val_div, ":added_wealth", 2),
          (try_end),
        (else_try),
          (party_slot_eq, ":center_no", slot_town_lord, -1),
          ##JuJu70 added for non-owned centers
          (val_div, ":added_wealth", 3),
          (val_add, ":added_wealth", ":modifier"), #wealth
          (try_begin),
            (party_slot_eq, ":center_no", slot_party_type, spt_town),
            (val_mul, ":added_wealth", 3),
            (val_div, ":added_wealth", 2),
          (try_end),
        (try_end),
        (val_add, ":cur_wealth", ":added_wealth"),
        (party_set_slot, ":center_no", slot_town_wealth, ":cur_wealth"),
        (call_script, "script_calculate_weekly_party_wage", ":center_no"),
        (assign, ":wage", reg0),
        (val_sub, ":cur_wealth", ":wage"),
        (val_max, ":cur_wealth", 0),
        (party_set_slot, ":center_no", slot_town_wealth, ":cur_wealth"),
        (assign, ":no_works", 1),
        (try_begin),
          (this_or_next|party_slot_ge, ":center_no", slot_center_blockaded, 2),    #center blockaded (by player) OR
          (party_slot_ge, ":center_no", slot_center_is_besieged_by, 1), #center besieged by someone else
          (assign, ":no_works", 0),
        (try_end),
        (eq, ":no_works", 1),
        
        #siege warfare
        (party_slot_eq, ":center_no", slot_center_is_besieged_by, -1), #center not under siege
        (party_get_slot, ":food_stores", ":center_no", slot_party_food_store),
        (call_script, "script_center_get_food_store_limit", ":center_no"),
        (val_min, ":food_stores", reg0),
        (party_set_slot, ":center_no", slot_party_food_store, ":food_stores"),
        (store_faction_of_party, ":center_faction", ":center_no"),
        (try_begin),
          (this_or_next|eq, ":center_faction", "fac_player_supporters_faction"),
          (eq, ":center_faction", "$players_kingdom"),
          (assign, ":reinforcement_cost", reinforcement_cost_moderate),
          (assign, ":num_hiring_rounds", 1),
        (else_try),
          (options_get_campaign_ai, ":reduce_campaign_ai"), #moto chief
          (assign, ":reinforcement_cost", reinforcement_cost_moderate),
          (try_begin),
            (eq, ":reduce_campaign_ai", 0), #hard (1x or 2x reinforcing)
            (assign, ":reinforcement_cost", reinforcement_cost_hard),
            (store_random_in_range, ":num_hiring_rounds", 0, 2),
            (val_add, ":num_hiring_rounds", 1),
          (else_try),
            (eq, ":reduce_campaign_ai", 1), #moderate (1x reinforcing)
            (assign, ":reinforcement_cost", reinforcement_cost_moderate),
            (assign, ":num_hiring_rounds", 1),
          (else_try),
            (eq, ":reduce_campaign_ai", 2), #easy (none or 1x reinforcing)
            (assign, ":reinforcement_cost", reinforcement_cost_easy),
            (store_random_in_range, ":num_hiring_rounds", 0, 2),
          (try_end),
        (try_end),
        #Adjustment for party size
        (store_party_size_wo_prisoners, ":gar_size", ":center_no"),
        (try_begin),
          (is_between, ":center_no", castles_begin, castles_end),
          (val_div, ":gar_size", 150),
        (else_try),
          (val_div, ":gar_size", 200),
        (try_end),
        (val_add, ":gar_size", 1),
        (val_mul, ":reinforcement_cost", ":gar_size"),
        #End adjustment
        #Reduce garrisons when they're too big
        (party_get_num_companions,":companions", ":center_no"),
        (assign, ":limit", 0),
        (try_begin),
          (is_between, ":center_no", castles_begin, castles_end),
          (assign, ":base", 150),
        (else_try),
          (is_between, ":center_no", towns_begin, towns_end),
          (assign, ":base", 250),
        (try_end),
        (store_character_level, ":level", "trp_player"),
        (try_begin),
          (le, ":level", 12),
        (else_try),
          (val_mul, ":base", ":level"),
          (val_div, ":base", 12),
        (try_end),
        (try_begin),
          (is_between, ":center_no", castles_begin, castles_end),
          (store_mul, ":limit", ":prosperity", 6),
          (val_max, ":limit", ":base"),
        (else_try),
          (is_between, ":center_no", towns_begin, towns_end),
          (store_mul, ":limit", ":prosperity", 8),
          (val_max, ":limit", ":base"),
        (try_end),
        (val_add, ":limit", 50),
        (try_begin),
          (neg|party_slot_ge, ":center_no", slot_center_blockaded, 2),    #center blockaded (by player) OR
          (neg|party_slot_ge, ":center_no", slot_center_is_besieged_by, 1), #center besieged by someone else
          (gt, ":companions", ":limit"),
          (store_sub, ":diff", ":companions", ":limit"),
          (assign, reg44, ":diff"),
          #			(str_store_party_name, s34, ":center_no"),
          #			(display_message, "@{s34} has {reg44} too many troops"),
          (try_begin),
            (le, ":diff", 10),
            (store_random_in_range, ":p_leave", 5, 13),
            (assign, ":num_troops", ":p_leave"),
            (try_for_range, ":unused", 0, ":num_troops"),
              (call_script, "script_cf_party_remove_random_regular_troop", ":center_no"),
            (try_end),
          (else_try),
            (store_random_in_range, ":p_leave", 10, ":diff"),
            (assign, ":num_troops", ":p_leave"),
            (try_for_range, ":unused", 0, ":num_troops"),
              (call_script, "script_cf_party_remove_random_regular_troop", ":center_no"),
            (try_end),
          (try_end),
        (try_end),
        (try_for_range, ":unused", 0, ":num_hiring_rounds"),
          (party_get_slot, ":cur_wealth", ":center_no", slot_town_wealth),
          (assign, ":hiring_budget", ":cur_wealth"),
          #		 (str_store_party_name, s35, ":center_no"),
          (val_div, ":hiring_budget", 2),
          #		 (assign, reg34, ":cur_wealth"),
          #		 (assign, reg31, ":reinforcement_cost"),
          (gt, ":hiring_budget", ":reinforcement_cost"),
          #		 (display_message, "@{s35} wealth is {reg34} and it is being reinforced - reinforcement cost is {reg31}"),
          (call_script, "script_cf_reinforce_party", ":center_no"),
          (val_sub, ":cur_wealth", ":reinforcement_cost"),
          (party_set_slot, ":center_no", slot_town_wealth, ":cur_wealth"),
        (try_end),
    ]),
    #Adding net incomes to centers (once a week)
    #If non-player center, adding income to wealth
    #(24*7,
    #[
    #   (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
    # (neg|party_slot_eq, ":center_no", slot_town_lord, "trp_player"), #center does not belong to player.
    # (try_begin),
    # (party_slot_ge, ":center_no", slot_town_lord, 1), #center belongs to someone.
    # (party_get_slot, ":cur_wealth", ":center_no", slot_town_wealth),
    # (party_get_slot, ":prosperity", ":center_no", slot_town_prosperity),
    # (store_mul, ":added_wealth", ":prosperity", 30), #prosperity is the key chief
    # (val_add, ":added_wealth", 1400), #wealth
    # (try_begin),
    # (party_slot_eq, ":center_no", slot_party_type, spt_town),
    # (val_mul, ":added_wealth", 3),
    # (val_div, ":added_wealth", 2),
    # (try_end),
    # (else_try),
    ##JuJu70 added for non-owned centers
    #	   (party_get_slot, ":cur_wealth", ":center_no", slot_town_wealth),
    # (party_get_slot, ":prosperity", ":center_no", slot_town_prosperity),
    # (store_mul, ":added_wealth", ":prosperity", 10), #prosperity is the key chief
    # (val_add, ":added_wealth", 700), #wealth
    # (try_begin),
    # (party_slot_eq, ":center_no", slot_party_type, spt_town),
    # (val_mul, ":added_wealth", 3),
    # (val_div, ":added_wealth", 2),
    # (try_end),
    # (try_end),
    # (val_add, ":cur_wealth", ":added_wealth"),
    #    (call_script, "script_calculate_weekly_party_wage", ":center_no"),
    #     (val_sub, ":cur_wealth", reg0),
    #    (val_max, ":cur_wealth", 0),
    #    (party_set_slot, ":center_no", slot_town_wealth, ":cur_wealth"),
    #  (try_end),
    #    ]),
    
    # JuJu70 (#22)
    # NPCs turn adventurers if quit or rejected
    (1.8,
      [
        (neq, "$campaign_type", camp_storyline),
        (store_random_in_range, ":troop_no", companions_begin, companions_end),
        (troop_slot_eq, ":troop_no", slot_troop_occupation, 0),
        #no some companions, total out = 8
        (neg|is_between, ":troop_no", "trp_npc15", "trp_kingdom_1_lord"), #no beda or aghatinos #no leaders
        (neq, ":troop_no", "trp_npc12"), #no Asbjorn
        (neq, ":troop_no", "trp_npc3"), #no brunhild, no leader.
        (neq, ":troop_no", "trp_npc7"), #no dwywei, I forgot about romance.
        (neq, ":troop_no", "trp_npc11"), #no solveig, women problem become lords
        (neg|main_party_has_troop, ":troop_no"),  #prevent cloning
        #
        (call_script, "script_troop_get_relation_with_troop", "trp_player", ":troop_no"),
        (le, reg0, 30), #vc-3258
        
        (store_faction_of_troop, ":faction", ":troop_no"),
        (neg|is_between, ":faction", kingdoms_begin, kingdoms_end),
        (assign, ":start_chance", 0),
        (assign, ":cont", 0),
        (assign, ":test", 0),
        (try_begin),
          (neq, "$game_started_with_content_update", 1),
          (try_begin),
            (eq, "$g_sgfix", 0),
            (store_current_hours, "$g_current_hours"),
            (assign, "$g_sgfix", "$g_current_hours"),
            (assign, ":cont", 1),
          (else_try),
            (store_current_hours, "$g_current_hours"),
            (store_sub, ":test","$g_current_hours","$g_sgfix"),
            (lt, ":test", 85),
            (assign, ":cont", 1),
          (try_end),
        (try_end),
        (eq, ":cont", 0),
        (try_begin),
          (this_or_next|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_retirement),
          (troop_slot_eq, ":troop_no", slot_troop_turned_down_twice, 1),
          (try_begin),
            (eq, ":troop_no", "trp_npc1"), #Caio
            (assign, ":start_chance", 1),
          (else_try),
            (eq, ":troop_no", "trp_npc2"), #Egil
            (assign, ":start_chance", 30),
          (else_try),
            (eq, ":troop_no", "trp_npc4"), #Donnchadh
            (assign, ":start_chance", 15),
          (else_try),
            (eq, ":troop_no", "trp_npc5"), #Morgant
            (assign, ":start_chance", 20),
          (else_try),
            (eq, ":troop_no", "trp_npc6"), #Bodo
            (assign, ":start_chance", 6),
          (else_try),
            (eq, ":troop_no", "trp_npc8"), #Reginhard
            (assign, ":start_chance", 3),
          (else_try),
            (eq, ":troop_no", "trp_npc9"), #Clovis
            (assign, ":start_chance", 15),
          (else_try),
            (eq, ":troop_no", "trp_npc10"), #Ceawlin
            (assign, ":start_chance", 25),
            ##			(else_try),
            ##                           (eq, ":troop_no", "trp_npc11"), #Solveig
            ##			   (assign, ":start_chance", 10),
          (else_try),
            (eq, ":troop_no", "trp_npc13"), #Helgi
            (assign, ":start_chance", 30),
          (else_try),
            (eq, ":troop_no", "trp_npc14"), #Ailchu
            (assign, ":start_chance", 15),
          (else_try),
            (assign, ":start_chance", 25),
          (try_end),
        (else_try),
          (troop_slot_eq, ":troop_no",slot_troop_playerparty_history, pp_history_quit),
          (try_begin),
            (eq, ":troop_no", "trp_npc1"), #Caio
            (assign, ":start_chance", 3),
          (else_try),
            (eq, ":troop_no", "trp_npc2"), #Egil
            (assign, ":start_chance", 50),
          (else_try),
            (eq, ":troop_no", "trp_npc4"), #Donnchadh
            (assign, ":start_chance", 25),
          (else_try),
            (eq, ":troop_no", "trp_npc5"), #Morgant
            (assign, ":start_chance", 30),
          (else_try),
            (eq, ":troop_no", "trp_npc6"), #Bodo
            (assign, ":start_chance", 10),
          (else_try),
            (eq, ":troop_no", "trp_npc8"), #Reginhard
            (assign, ":start_chance", 5),
          (else_try),
            (eq, ":troop_no", "trp_npc9"), #Clovis
            (assign, ":start_chance", 25),
          (else_try),
            (eq, ":troop_no", "trp_npc10"), #Ceawlin
            (assign, ":start_chance", 35),
            ##			(else_try),
            ##                           (eq, ":troop_no", "trp_npc11"), #Solveig
            ##			   (assign, ":start_chance", 15),
          (else_try),
            (eq, ":troop_no", "trp_npc13"), #Helgi
            (assign, ":start_chance", 50),
          (else_try),
            (eq, ":troop_no", "trp_npc14"), #Ailchu
            (assign, ":start_chance", 20),
          (else_try),
            (assign, ":start_chance", 50),
          (try_end),
          #(assign, ":start_chance", 50),
        (else_try),
          (troop_slot_eq, ":troop_no",slot_troop_playerparty_history, pp_history_dismissed),
          (try_begin),
            (eq, ":troop_no", "trp_npc1"), #Caio
            (assign, ":start_chance", 2),
          (else_try),
            (eq, ":troop_no", "trp_npc2"), #Egil
            (assign, ":start_chance", 40),
          (else_try),
            (eq, ":troop_no", "trp_npc4"), #Donnchadh
            (assign, ":start_chance", 20),
          (else_try),
            (eq, ":troop_no", "trp_npc5"), #Morgant
            (assign, ":start_chance", 25),
          (else_try),
            (eq, ":troop_no", "trp_npc6"), #Bodo
            (assign, ":start_chance", 8),
          (else_try),
            (eq, ":troop_no", "trp_npc8"), #Reginhard
            (assign, ":start_chance", 4),
          (else_try),
            (eq, ":troop_no", "trp_npc9"), #Clovis
            (assign, ":start_chance", 20),
          (else_try),
            (eq, ":troop_no", "trp_npc10"), #Ceawlin
            (assign, ":start_chance", 30),
            ##			(else_try),
            ##                           (eq, ":troop_no", "trp_npc11"), #Solveig
            ##			   (assign, ":start_chance", 12),
          (else_try),
            (eq, ":troop_no", "trp_npc13"), #Helgi
            (assign, ":start_chance", 40),
          (else_try),
            (eq, ":troop_no", "trp_npc14"), #Ailchu
            (assign, ":start_chance", 18),
          (else_try),
            (assign, ":start_chance", 35),
          (try_end),
          #(assign, ":start_chance", 35),
        (try_end),
        (store_random_in_range, ":random", 0, 120),
        (lt, ":random", ":start_chance"),
        (troop_get_slot, ":center", ":troop_no", slot_troop_home),
        (str_store_party_name, s39, ":center"),
        (set_spawn_radius, 15),
        (spawn_around_party,":center","pt_adv_party"),
        (assign, ":party_no", reg(0)),
        (party_set_slot, ":party_no", slot_party_type, spt_kingdom_hero_party),
        (troop_set_slot, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
        (troop_set_slot, ":troop_no", slot_troop_prisoner_of_party, -1),
        (party_set_faction, ":party_no", "fac_adventurers"),
        (troop_set_faction, ":troop_no", "fac_adventurers"),
        (troop_set_slot, ":troop_no", slot_troop_leaded_party, ":party_no"),
        (party_add_leader, ":party_no", ":troop_no"),
        (store_random_in_range,":random_gold",1500,5000),
        (troop_get_slot, ":wealth", ":troop_no", slot_troop_wealth),
        (val_add, ":wealth", ":random_gold"),
        (troop_set_slot, ":troop_no", slot_troop_wealth, ":wealth"),
        (troop_get_slot, ":renown", ":troop_no", slot_troop_renown),
        (val_add, ":renown", 90),
        (troop_set_slot, ":troop_no", slot_troop_renown, ":renown"),
        (party_set_ai_behavior, ":party_no", ai_bhvr_hold),
        (str_store_troop_name, s40, ":troop_no"),
        (party_set_name, ":party_no", s40),
        (display_message, "@{s40} decided to become an adventurer near {s39}",color_hero_news),
        (troop_set_slot, ":troop_no", slot_troop_turned_down_twice, 0),
        (troop_set_slot, ":troop_no", slot_troop_playerparty_history, 0),
        (try_begin),
          (store_skill_level, ":spotting", "skl_spotting", ":troop_no"),
          (store_sub, ":corr",":spotting", 4),
          (lt, ":corr",0),
          (val_mul, ":corr", -1),
          (troop_raise_skill, ":troop_no",skl_spotting,":corr"),
        (try_end),
        (try_begin),
          (store_skill_level, ":path", "skl_pathfinding", ":troop_no"),
          (store_sub, ":corr",":path", 5),
          (lt, ":corr",0),
          (val_mul, ":corr", -1),
          (troop_raise_skill, ":troop_no",skl_pathfinding,":corr"),
        (try_end),
        (try_begin),
          (store_skill_level, ":lead", "skl_leadership", ":troop_no"),
          (store_sub, ":corr",":lead", 5),
          (lt, ":corr",0),
          (val_mul, ":corr", -1),
          (troop_raise_skill, ":troop_no",skl_leadership,":corr"),
        (try_end),
        (try_begin),
          (store_skill_level, ":train", "skl_trainer", ":troop_no"),
          (store_sub, ":corr",":train", 2),
          (lt, ":corr",0),
          (val_mul, ":corr", -1),
          (troop_raise_skill, ":troop_no",skl_trainer,":corr"),
        (try_end),
        
        #	(try_end),
    ]),
    #Hiring men with hero wealths (once a day)
    # JuJu70 probabilistic?
    (0.14,
      [
        (store_random_in_range, ":troop_no", active_npcs_begin, active_npcs_end),
        (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
        (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
        (ge, ":party_no", 1),
        (party_is_active, ":party_no"),
        
        (store_random_in_range, ":rand", 0, 100),
        (try_begin),
          (lt, ":rand", 7),
          (call_script, "script_assign_troop_love_interests", ":troop_no"),
        (try_end),
        
        (party_get_attached_to, ":cur_attached_party", ":party_no"),
        (is_between, ":cur_attached_party", centers_begin, centers_end),
        #siege warfare chief cambia
        
        (assign, ":no_works", 1),
        (try_begin),
          (this_or_next|party_slot_ge, ":cur_attached_party", slot_center_blockaded, 2),    #center blockaded (by player) OR
          (party_slot_ge, ":cur_attached_party", slot_center_is_besieged_by, 1), #center besieged by someone else
          (assign, ":no_works", 0),
        (try_end),
        (eq, ":no_works", 1),
        #siege warfare
        
        (party_slot_eq, ":cur_attached_party", slot_center_is_besieged_by, -1), #center not under siege
        
        (store_faction_of_party, ":party_faction", ":party_no"),
        (try_begin),
          (this_or_next|eq, ":party_faction", "fac_player_supporters_faction"),
          (eq, ":party_faction", "$players_kingdom"),
          (assign, ":num_hiring_rounds", 1),
          (store_random_in_range, ":random_value", 0, 2),
          (val_add, ":num_hiring_rounds", ":random_value"),
        (else_try),
          (options_get_campaign_ai, ":reduce_campaign_ai"), #moto chief
          (try_begin),
            (eq, ":reduce_campaign_ai", 0), #hard (2x reinforcing)
            (assign, ":num_hiring_rounds", 2),
          (else_try),
            (eq, ":reduce_campaign_ai", 1), #medium (1x or 2x reinforcing)
            (assign, ":num_hiring_rounds", 1),
            (store_random_in_range, ":random_value", 0, 2),
            (val_add, ":num_hiring_rounds", ":random_value"),
          (else_try),
            (eq, ":reduce_campaign_ai", 2), #easy (1x reinforcing)
            (assign, ":num_hiring_rounds", 1),
          (try_end),
        (try_end),
        
        (try_begin),
          (faction_slot_eq,  ":party_faction", slot_faction_marshal, ":troop_no"),
          (val_add, ":num_hiring_rounds", 1),
        (try_end),
        
        (try_for_range, ":unused", 0, ":num_hiring_rounds"),
          (call_script, "script_hire_men_to_kingdom_hero_party", ":troop_no"), #Hiring men with current wealth
        (try_end),
        #    (try_end),
    ]),
    
    #walled center daily ON AVERAGE
    (0.20, [
        (store_random_in_range, ":center_no", walled_centers_begin, walled_centers_end),
        (call_script, "script_process_sieges", ":center_no"),
    ]),
    
    #center every three days ON AVERAGE
    (0.27, [
        (store_random_in_range, ":center_no", centers_begin, centers_end),
        #(neg|is_between, ":center_no", castles_begin, castles_end),
        
        (call_script, "script_get_center_ideal_prosperity", ":center_no"),
        (assign, ":ideal_prosperity", reg0),
        (party_get_slot, ":prosperity", ":center_no", slot_town_prosperity),
        (store_random_in_range, ":random", 0, 10),
        (try_begin),
          (eq, ":random", 0), #with 10% probability it will gain +10%/-10% prosperity even it has higher prosperity than its ideal prosperity.
          (try_begin),
            (store_random_in_range, ":random", 0, 2),
            (store_div, ":ten_percent", ":prosperity", 10),
            (try_begin),
              (eq, ":random", 0),
              (neg|is_between, ":center_no", castles_begin, castles_end), #castles always gain positive prosperity from surprise income to balance their prosperity.
              (val_mul, ":ten_percent", -1),
              (call_script, "script_change_center_prosperity", ":center_no", ":ten_percent"),
              (val_add, "$newglob_total_prosperity_from_convergence", ":ten_percent"),
            (else_try),
              (call_script, "script_change_center_prosperity", ":center_no", ":ten_percent"),
              (val_add, "$newglob_total_prosperity_from_convergence", ":ten_percent"),
            (try_end),
          (try_end),
        (else_try),
          (gt, ":prosperity", ":ideal_prosperity"),
          (call_script, "script_change_center_prosperity", ":center_no", -1),
          (val_add, "$newglob_total_prosperity_from_convergence", -1),
        (else_try),
          (lt, ":prosperity", ":ideal_prosperity"),
          (call_script, "script_change_center_prosperity", ":center_no", 1),
          (val_add, "$newglob_total_prosperity_from_convergence", 1),
        (try_end),
        (try_begin),
          (is_between, ":center_no", walled_centers_begin, walled_centers_end),
          (party_get_slot, ":food_stores", ":center_no", slot_party_food_store),
          (call_script, "script_center_get_food_store_limit", ":center_no"),
          (val_min, ":food_stores", reg0),
          (party_set_slot, ":center_no", slot_party_food_store, ":food_stores"),
        (try_end),
    ]),
    
    #Converging center prosperity to ideal prosperity once in every 15 days
    #(24*15,
    #[]),
    
    #Checking if the troops are resting at a half payment point
    (6,
      [(store_current_day, ":cur_day"),
        (try_begin),
          (neq, ":cur_day", "$g_last_half_payment_check_day"),
          (assign, "$g_last_half_payment_check_day", ":cur_day"),
          (try_begin),
            (eq, "$g_half_payment_checkpoint", 1),
            (val_add, "$g_cur_week_half_daily_wage_payments", 1), #half payment for yesterday
          (try_end),
          (assign, "$g_half_payment_checkpoint", 1),
        (try_end),
        (assign, ":resting_at_manor_or_walled_center", 0),
        (try_begin),
          (neg|map_free),
          (ge, "$g_last_rest_center", 0),
          (this_or_next|party_slot_eq, "$g_last_rest_center", slot_center_has_manor, 1),
          (is_between, "$g_last_rest_center", walled_centers_begin, walled_centers_end),
          (assign, ":resting_at_manor_or_walled_center", 1),
        (try_end),
        (eq, ":resting_at_manor_or_walled_center", 0),
        (assign, "$g_half_payment_checkpoint", 0),
    ]),
    
    #diplomatic indices
    (24,
      [
        (call_script, "script_find_neighbors"),	#MOTO chief
        (call_script, "script_randomly_start_war_peace_new", 1),
        
        #dumping
        (try_begin),
          (eq, "$cheat_mode", 4), #change back to 4
          (try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
            (store_faction_of_troop, ":active_npc_faction", ":active_npc"),
            (neg|faction_slot_eq, ":active_npc_faction", slot_faction_ai_state, sfai_default),
            (neg|faction_slot_eq, ":active_npc_faction", slot_faction_ai_state, sfai_feast),
            (neg|faction_slot_eq, ":active_npc_faction", slot_faction_ai_state, sfai_gathering_army),
            
            (troop_get_slot, ":active_npc_party", ":active_npc", slot_troop_leaded_party),
            (party_is_active, ":active_npc_party"),
            
            (val_add, "$total_vassal_days_on_campaign", 1),
            
            (party_slot_eq, ":active_npc_party", slot_party_ai_state, spai_accompanying_army),
            (val_add, "$total_vassal_days_responding_to_campaign", 1),
          (try_end),
        (try_end),
    ]),
    
    (1,	#MOTO recycle trigger (to 1 from 24) from 24-hour trigger above
      [
        (store_random_in_range, ":faction_1", kingdoms_begin, kingdoms_end),
        (try_begin),
          (faction_slot_eq, ":faction_1", slot_faction_state, sfs_active),
          (try_for_range, ":faction_2", kingdoms_begin, kingdoms_end),
            (neq, ":faction_1", ":faction_2"),
            (faction_slot_eq, ":faction_2", slot_faction_state, sfs_active),
            
            #remove provocations
            (store_add, ":slot_truce_days", ":faction_2", slot_faction_truce_days_with_factions_begin),
            (val_sub, ":slot_truce_days", kingdoms_begin),
            (faction_get_slot, ":truce_days", ":faction_1", ":slot_truce_days"),
            (try_begin),
              (ge, ":truce_days", 1),
              (try_begin),
                (eq, ":truce_days", 1),
                (call_script, "script_update_faction_notes", ":faction_1"),
                (lt, ":faction_1", ":faction_2"),
                #(call_script, "script_add_notification_menu", "mnu_notification_truce_expired", ":faction_1", ":faction_2"),
              (else_try),
                (eq, ":truce_days", truce_time + 1),#replaced 61
                (call_script, "script_update_faction_notes", ":faction_1"),
                (lt, ":faction_1", ":faction_2"),
                #(call_script, "script_add_notification_menu", "mnu_notification_alliance_expired", ":faction_1", ":faction_2"), #chief puesto off
              (try_end),
              (val_sub, ":truce_days", 1),
              (faction_set_slot, ":faction_1", ":slot_truce_days", ":truce_days"),
            (try_end),
            
            (store_add, ":slot_provocation_days", ":faction_2", slot_faction_provocation_days_with_factions_begin),
            (val_sub, ":slot_provocation_days", kingdoms_begin),
            (faction_get_slot, ":provocation_days", ":faction_1", ":slot_provocation_days"),
            (try_begin),
              (ge, ":provocation_days", 1),
              (try_begin),#factions already at war
                (store_relation, ":relation", ":faction_1", ":faction_2"),
                (lt, ":relation", 0),
                (faction_set_slot, ":faction_1", ":slot_provocation_days", 0),
              (else_try), #Provocation expires
                (eq, ":provocation_days", 1),
                (call_script, "script_add_notification_menu", "mnu_notification_casus_belli_expired", ":faction_1", ":faction_2"),
                (faction_set_slot, ":faction_1", ":slot_provocation_days", 0),
              (else_try),
                (val_sub, ":provocation_days", 1),
                (faction_set_slot, ":faction_1", ":slot_provocation_days", ":provocation_days"),
              (try_end),
            (try_end),
            
            (try_begin), #at war
              (store_relation, ":relation", ":faction_1", ":faction_2"),
              (lt, ":relation", 0),
              (store_add, ":slot_war_damage", ":faction_2", slot_faction_war_damage_inflicted_on_factions_begin),
              (val_sub, ":slot_war_damage", kingdoms_begin),
              (faction_get_slot, ":war_damage", ":faction_1", ":slot_war_damage"),
              (val_add, ":war_damage", 1),
              (faction_set_slot, ":faction_1", ":slot_war_damage", ":war_damage"),
            (try_end),
            
          (try_end),
          (call_script, "script_update_faction_notes", ":faction_1"),
        (try_end),
        
        (store_time_of_day, ":oclock"),
        (store_current_day, ":day_mod"),
        (val_mod, ":day_mod", 8),	#eighth the rate of incidents moto chief
        
        (store_sub, ":num_villages", villages_end, villages_begin),
        (val_div, ":num_villages", 23),
        (store_mul, ":start_village", ":oclock", ":num_villages"),
        (val_add, ":start_village", villages_begin),
        (store_add, ":end_village", ":start_village", ":num_villages"),
        (val_min, ":end_village", villages_end),
        
        #MOTO ramp up border incidents
        (try_for_range, ":acting_village", ":start_village", ":end_village"),
          (store_mod, reg0, ":acting_village", 8),	#eighth the rate of incidents moto chief
          (eq, reg0, ":day_mod"),
          # (try_begin),
          # (store_random_in_range, ":acting_village", villages_begin, villages_end),
          #MOTO ramp up border incidents end
          (store_random_in_range, ":target_village", villages_begin, villages_end),
          (store_faction_of_party, ":acting_faction", ":acting_village"),
          (store_faction_of_party, ":target_faction", ":target_village"), #target faction receives the provocation
          (neq, ":acting_village", ":target_village"),
          (neq, ":acting_faction", ":target_faction"),
          
          (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", ":target_faction", ":acting_faction"),
          (eq, reg0, 0),
          
          (try_begin),
            (party_slot_eq, ":acting_village", slot_center_original_faction, ":target_faction"),
            
            (call_script, "script_add_notification_menu", "mnu_notification_border_incident", ":acting_village", -1),
          (else_try),
            (party_slot_eq, ":acting_village", slot_center_ex_faction, ":target_faction"),
            
            (call_script, "script_add_notification_menu", "mnu_notification_border_incident", ":acting_village", -1),
            
          (else_try),
            (set_fixed_point_multiplier, 1),
            (store_distance_to_party_from_party, ":distance", ":acting_village", ":target_village"),
            (lt, ":distance", 25),
            
            (call_script, "script_add_notification_menu", "mnu_notification_border_incident", ":acting_village", ":target_village"),
          (try_end),
        (try_end),
    ]),
    
    # Give some xp to hero parties every 48 hours ON AVERAGE
    (.27,
      [
        (store_random_in_range, ":troop_no", active_npcs_begin, active_npcs_end),
        (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
        (troop_set_slot, ":troop_no",slot_troop_sell_prisoner, 0),
        (troop_set_slot, ":troop_no", slot_troop_refused, 0),
        (troop_get_slot, ":hero_party", ":troop_no", slot_troop_leaded_party),
        (gt, ":hero_party", centers_end),
        (party_is_active, ":hero_party"),
        
        (store_skill_level, ":trainer_level", skl_trainer, ":troop_no"),
        #        (val_add, ":trainer_level", 5), #average trainer level is 3 for npc lords, worst : 0, best : 6
        (store_mul, ":xp_gain", ":trainer_level", 1000), #xp gain in two days of period for each lord, average : 8000.
        
        (assign, ":max_accepted_random_value", 30),
        (try_begin),
          (store_troop_faction, ":cur_troop_faction", ":troop_no"),
          (neq, ":cur_troop_faction", "$players_kingdom"),
          
          (options_get_campaign_ai, ":reduce_campaign_ai"), #moto chief
          (try_begin),
            (eq, ":reduce_campaign_ai", 0), #hard (1.5x)
            (assign, ":max_accepted_random_value", 35),
            (val_mul, ":xp_gain", 3),
            (val_div, ":xp_gain", 2),
          (else_try),
            (eq, ":reduce_campaign_ai", 2), #easy (0.5x)
            (assign, ":max_accepted_random_value", 25),
            (val_div, ":xp_gain", 2),
          (try_end),
        (try_end),
        
        (store_random_in_range, ":rand", 0, 100),
        (le, ":rand", ":max_accepted_random_value"),
        
        (party_upgrade_with_xp, ":hero_party", ":xp_gain"),
        # (try_end),
        
    ]),
    
    #STrig 30
    # Give some xp to garrisons every 48 hours ON AVERAGE
    (.41,
      [
        (store_random_in_range, ":center_no", walled_centers_begin, walled_centers_end),
        (party_get_slot, ":center_lord", ":center_no", slot_town_lord),
        (neq, ":center_lord", "trp_player"),
        
        (assign, ":xp_gain", 3000), #xp gain in two days of period for each center, average : 3000.
        
        (assign, ":max_accepted_random_value", 30),
        (try_begin),
          (assign, ":cur_center_lord_faction", -1),
          (try_begin),
            (ge, ":center_lord", 0),
            (store_troop_faction, ":cur_center_lord_faction", ":center_lord"),
          (try_end),
          (neq, ":cur_center_lord_faction", "$players_kingdom"),
          
          (options_get_campaign_ai, ":reduce_campaign_ai"), #moto chief
          (try_begin),
            (eq, ":reduce_campaign_ai", 0), #hard (1.5x)
            (assign, ":max_accepted_random_value", 35),
            (val_mul, ":xp_gain", 3),
            (val_div, ":xp_gain", 2),
          (else_try),
            (eq, ":reduce_campaign_ai", 2), #easy (0.5x)
            (assign, ":max_accepted_random_value", 25),
            (val_div, ":xp_gain", 2),
          (try_end),
        (try_end),
        
        (store_random_in_range, ":rand", 0, 100),
        (le, ":rand", ":max_accepted_random_value"),
        (store_random_in_range, ":rand", 0, 100),
        (try_begin),
          (lt, ":rand", 70),
          (party_upgrade_with_xp, ":center_no", ":xp_gain",0),
        (else_try),
          (party_upgrade_with_xp, ":center_no", ":xp_gain",1),
        (try_end),
        
        # (try_end),
    ]),
    
    # Process sieges MOVED to daily walled center
    
    # Process village raids
    (2,
      [
        (call_script, "script_process_village_raids"),
    ]),
    
    
    # Duplicates recalculate AI, now that it is 6 hours
    #   (24,
    #   [
    # (call_script, "script_init_ai_calculation"),
    # #(call_script, "script_decide_kingdom_party_ais"),
    # (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
    # (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
    # (call_script, "script_calculate_troop_ai", ":troop_no"),
    # (try_end),
    #     ]),
    
    # JuJu70
    # AI Invite adventurers to become lords
    (24,
      [(try_for_range, ":troop_no", companions_begin, companions_end),
          (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
          (troop_slot_ge, ":troop_no", slot_troop_leaded_party, 1),
          (troop_get_slot, ":hero_party",":troop_no", slot_troop_leaded_party),
          (party_is_active, ":hero_party"),
          (store_faction_of_party, ":hero_faction", ":hero_party"),
          (eq, ":hero_faction", "fac_adventurers"),
          #		(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
          (party_slot_eq, ":hero_party", slot_party_type, spt_kingdom_hero_party),
          (troop_get_type, ":type", ":troop_no"),
          (val_mod, ":type", 2),    #gender fix chief
          (store_random_in_range, ":kingdom_no", npc_kingdoms_begin, npc_kingdoms_end),
          (faction_slot_eq, ":kingdom_no", slot_faction_state, sfs_active), #VC-3911 duh
          (faction_get_slot, ":kingdom_lord", ":kingdom_no", slot_faction_leader),
          (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":kingdom_lord"),
          (assign, ":lord_relation", reg0),
          (assign, ":party_size", 0),
          (try_begin),
            (ge, ":hero_party", 0),
            (store_party_size_wo_prisoners, ":party_size", ":hero_party"),
          (try_end),
          (try_begin),
            (troop_get_slot, ":renown", ":troop_no", slot_troop_renown),
            (ge, ":renown", 250),
            (ge, ":lord_relation", 0),
            (ge, ":party_size", 70),#70
            (store_random_in_range, ":rand", 0, 100),
            (lt, ":rand", 50),
            (call_script, "script_get_poorest_village_of_faction", ":kingdom_no"),
            (assign, ":village", reg0),
            (try_begin),
              (ge, ":village", 0),
              (call_script, "script_change_troop_faction", ":troop_no", ":kingdom_no"),
              (call_script, "script_give_center_to_lord", ":village",  ":troop_no", 0),
              (call_script, "script_change_troop_renown", ":troop_no", 150),
              (call_script, "script_troop_change_relation_with_troop", ":troop_no", ":kingdom_lord", 7),
            (else_try),
              (call_script, "script_change_troop_faction", ":troop_no", ":kingdom_no"),
              (call_script, "script_change_troop_renown", ":troop_no", 80),
              (call_script, "script_troop_change_relation_with_troop", ":troop_no", ":kingdom_lord", 4),
            (try_end),
            (call_script, "script_equip_new_noble", ":troop_no"),
            (party_set_faction, ":hero_party", ":kingdom_no"),
            (troop_set_note_available, ":troop_no", 1),
            (troop_set_slot, ":troop_no", slot_troop_occupation,slto_kingdom_hero),
            (troop_get_slot, ":faction", ":troop_no", slot_troop_original_faction),
            (try_begin),
              (eq, ":faction", 0),
              (troop_set_slot, ":troop_no", slot_troop_original_faction, ":kingdom_no"),
            (try_end),
            (assign, ":end_cond", banner_scene_props_end),
            (try_for_range, reg0, banner_scene_props_begin, ":end_cond"),
              (assign, ":end_loop", active_npcs_end),
              (try_for_range, ":kingdom_hero", active_npcs_including_player_begin, ":end_loop"),
                (try_begin),
                  (eq, ":kingdom_hero", "trp_kingdom_heroes_including_player_begin"),
                  (assign, ":kingdom_hero", "trp_player"),
                (try_end),
                (troop_slot_eq, ":kingdom_hero", slot_troop_banner_scene_prop, reg0),
                (assign, ":cur_banner_prop", reg0),
                (assign, ":end_loop", ":kingdom_hero"),
              (try_end),
              (eq, ":end_loop", active_npcs_end), #no one has this banner?
              (troop_set_slot, ":troop_no", slot_troop_banner_scene_prop, ":cur_banner_prop"),
              (troop_get_slot, ":cur_party", ":troop_no", slot_troop_leaded_party),
              (gt, ":cur_party", 0),
              (store_sub, ":cur_banner_icon", ":cur_banner_prop", banner_scene_props_begin),
              (val_add, ":cur_banner_icon", banner_map_icons_begin),
              (party_set_banner_icon, ":cur_party", ":cur_banner_icon"),
              (assign, ":end_cond", 0), #break
            (try_end),
          (try_end),
        (try_end),
    ]),
    
    # Hold regular marshal elections for players_kingdom
    (24, #Disabled in favor of new system MOTO reenable as new system is missing (see 1158 prsnt_marshal_selection and mnu_marshal_selection_candidate_ask) TODO: TEST, add trigger for dissatisfaction as for NPC factions
      [
        (val_add, "$g_election_date", 1),
        (ge, "$g_election_date", 90), #elections holds once in every 90 days.
        (is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
        (neq, "$players_kingdom", "fac_player_supporters_faction"),
        (store_current_day, ":cur_day"),
        (lt, "$mercenary_service_next_renew_day", ":cur_day"),
        (assign, "$g_presentation_input", -1),
        (assign, "$g_presentation_marshal_selection_1_vote", 0),
        (assign, "$g_presentation_marshal_selection_2_vote", 0),
        
        (assign, "$g_presentation_marshal_selection_max_renown_1", -10000),
        (assign, "$g_presentation_marshal_selection_max_renown_2", -10000),
        (assign, "$g_presentation_marshal_selection_max_renown_3", -10000),
        (assign, "$g_presentation_marshal_selection_max_renown_1_troop", -10000),
        (assign, "$g_presentation_marshal_selection_max_renown_2_troop", -10000),
        (assign, "$g_presentation_marshal_selection_max_renown_3_troop", -10000),
        (assign, ":num_men", 0),
        (try_for_range, ":loop_var", "trp_kingdom_heroes_including_player_begin", active_npcs_end),
          (assign, ":cur_troop", ":loop_var"),
          (assign, ":continue", 0),
          (try_begin),
            (eq, ":loop_var", "trp_kingdom_heroes_including_player_begin"),
            (assign, ":cur_troop", "trp_player"),
            (try_begin),
              (eq, "$g_player_is_captive", 0),
              (eq, "$player_has_homage", 1), #mercenary player cannot be candidate
              (assign, ":continue", 1),
            (try_end),
          (else_try),
            (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
            (store_troop_faction, ":cur_troop_faction", ":cur_troop"),
            (eq, "$players_kingdom", ":cur_troop_faction"),
            #(troop_slot_eq, ":cur_troop", slot_troop_is_prisoner, 0),
            (neg|troop_slot_ge, ":cur_troop", slot_troop_prisoner_of_party, 0),
            (troop_slot_ge, ":cur_troop", slot_troop_leaded_party, 1),
            (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
            (neg|faction_slot_eq, ":cur_troop_faction", slot_faction_leader, ":cur_troop"),
            (troop_get_slot, ":cur_party", ":cur_troop", slot_troop_leaded_party),
            (gt, ":cur_party", 0),
            (party_is_active, ":cur_party"),
            (call_script, "script_party_count_fit_for_battle", ":cur_party"),
            (assign, ":party_fit_for_battle", reg0),
            (call_script, "script_party_get_ideal_size", ":cur_party"),
            (assign, ":ideal_size", reg0),
            (store_mul, ":relative_strength", ":party_fit_for_battle", 100),
            (val_div, ":relative_strength", ":ideal_size"),
            (ge, ":relative_strength", 25),
            (assign, ":continue", 1),
          (try_end),
          (eq, ":continue", 1),
          (val_add, ":num_men", 1),
          (troop_get_slot, ":renown", ":cur_troop", slot_troop_renown),
          (try_begin),
            (gt, ":renown", "$g_presentation_marshal_selection_max_renown_1"),
            (assign, "$g_presentation_marshal_selection_max_renown_3", "$g_presentation_marshal_selection_max_renown_2"),
            (assign, "$g_presentation_marshal_selection_max_renown_2", "$g_presentation_marshal_selection_max_renown_1"),
            (assign, "$g_presentation_marshal_selection_max_renown_1", ":renown"),
            (assign, "$g_presentation_marshal_selection_max_renown_3_troop", "$g_presentation_marshal_selection_max_renown_2_troop"),
            (assign, "$g_presentation_marshal_selection_max_renown_2_troop", "$g_presentation_marshal_selection_max_renown_1_troop"),
            (assign, "$g_presentation_marshal_selection_max_renown_1_troop", ":cur_troop"),
          (else_try),
            (gt, ":renown", "$g_presentation_marshal_selection_max_renown_2"),
            (assign, "$g_presentation_marshal_selection_max_renown_3", "$g_presentation_marshal_selection_max_renown_2"),
            (assign, "$g_presentation_marshal_selection_max_renown_2", ":renown"),
            (assign, "$g_presentation_marshal_selection_max_renown_3_troop", "$g_presentation_marshal_selection_max_renown_2_troop"),
            (assign, "$g_presentation_marshal_selection_max_renown_2_troop", ":cur_troop"),
          (else_try),
            (gt, ":renown", "$g_presentation_marshal_selection_max_renown_3"),
            (assign, "$g_presentation_marshal_selection_max_renown_3", ":renown"),
            (assign, "$g_presentation_marshal_selection_max_renown_3_troop", ":cur_troop"),
          (try_end),
        (try_end),
        (ge, "$g_presentation_marshal_selection_max_renown_1_troop", 0),
        (ge, "$g_presentation_marshal_selection_max_renown_2_troop", 0),
        (ge, "$g_presentation_marshal_selection_max_renown_3_troop", 0),
        (gt, ":num_men", 2), #at least 1 voter
        (assign, "$g_election_date", 0),
        (assign, "$g_presentation_marshal_selection_ended", 0),
        (try_begin),
          (neq, "$g_presentation_marshal_selection_max_renown_1_troop", "trp_player"),
          (neq, "$g_presentation_marshal_selection_max_renown_2_troop", "trp_player"),
          (start_presentation, "prsnt_marshal_selection"),
        (else_try),
          (jump_to_menu, "mnu_marshal_selection_candidate_ask"),
        (try_end),
    ]),#
    
    # JuJu70 - probabilistic
    (0.14,
      [
        (store_random_in_range, ":kingdom_hero", active_npcs_begin, active_npcs_end),
        (troop_get_slot, ":impatience", ":kingdom_hero", slot_troop_intrigue_impatience),
        (val_sub, ":impatience", 5),
        (val_max, ":impatience", 0),
        (troop_set_slot, ":kingdom_hero", slot_troop_intrigue_impatience, ":impatience"),
        (store_random_in_range, ":controversy_deduction", 0, 3),
        (val_min, ":controversy_deduction", 2),
        (troop_get_slot, ":controversy", ":kingdom_hero", slot_troop_controversy),
        (ge, ":controversy", 1),
        (val_sub, ":controversy", ":controversy_deduction"),
        (val_max, ":controversy", 0),
        (troop_set_slot, ":kingdom_hero", slot_troop_controversy, ":controversy"),
    ]),
    #	(assign, ":controversy_deduction", 1),
    #This reduces controversy by one each round
    # (try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
    # (troop_get_slot, ":controversy", ":active_npc", slot_troop_controversy),
    # (ge, ":controversy", 1),
    # (val_sub, ":controversy", ":controversy_deduction"),
    # (val_max, ":controversy", 0),
    # (troop_set_slot, ":active_npc", slot_troop_controversy, ":controversy"),
    # (try_end),
    (24,
      [
        (troop_get_slot, ":controversy", "trp_player", slot_troop_controversy),
        (store_random_in_range, ":controversy_deduction", 0, 3),
        (val_sub, ":controversy", ":controversy_deduction"),
        (val_max, ":controversy", 0),
        (troop_set_slot, "trp_player", slot_troop_controversy, ":controversy"),
        (assign,"$g_player_prisoner_released", 0),
        # JuJu70 piggybacking - disappearing items
        (store_party_size_wo_prisoners, ":main_party_size", "p_main_party"),
        (gt, ":main_party_size", 70),
        (troop_get_inventory_capacity, ":inv_size", "trp_player"),
        (store_skill_level, ":bonus", "skl_inventory_management", "trp_player"),
        (val_add, ":bonus", 100),
        (try_for_range, ":i_slot", 0, ":inv_size"),
          (troop_get_inventory_slot, ":item_id", "trp_player", ":i_slot"),
          (ge, ":item_id", 0),
          (try_begin),
            (this_or_next|eq, ":item_id", "itm_jewelry"),
            (this_or_next|eq, ":item_id", "itm_amber"),
            (this_or_next|eq, ":item_id", "itm_ivory"),
            (this_or_next|eq, ":item_id", "itm_silver"),
            (this_or_next|eq, ":item_id", "itm_soapstone"),
            (this_or_next|eq, ":item_id", "itm_vc_furs"),
            (this_or_next|eq, ":item_id", "itm_wine"),
            (this_or_next|eq, ":item_id", "itm_mead"),
            (eq, ":item_id", "itm_ale"),
            (store_random_in_range, ":rand", 0,":bonus"),
            (lt, ":rand", 4),
            (troop_remove_item, "trp_player", ":item_id"),
            (try_begin),
              (this_or_next|eq, ":item_id", "itm_wine"),
              (this_or_next|eq, ":item_id", "itm_mead"),
              (eq, ":item_id", "itm_ale"),
              (str_store_string, s22, "@It seems your soldiers had a good time and helped themselves to some of the drinks in your inventory."),
              (call_script, "script_change_player_party_morale", 2),
            (else_try),
              (str_store_item_name, s33, ":item_id"),
              (str_store_string, s22, "@It seems someone went through your inventory and stole some of your {s33}."),
            (try_end),
            (display_message, "@{s22}",color_bad_news),
          (try_end),
        (try_end),
    ]),
    
    #POLITICAL TRIGGERS
    #POLITICAL TRIGGER #1`
    (4, #increased from 12 #moto chief cambia
      [
        (call_script, "script_cf_random_political_event"),
        
        #Added Nov 2010 begins - do this twice
        #(call_script, "script_cf_random_political_event"),
        #Added Nov 2010 ends
        
        #This generates quarrels and occasional reconciliations and interventions
    ]),
    
    #Individual lord political calculations MOVED to weekly active NPCs trigger below
    
    #active NPCs hourly ON AVERAGE
    (.017, [ #was script_process_kingdom_parties_ai
        (try_for_range, ":unused", 0, 5),  #must do this more often than the frame rate (which seems to be one game minute)
          (store_random_in_range, ":troop_no", active_npcs_begin, active_npcs_end),
          (troop_get_slot, reg1, ":troop_no", 0),
          (val_add, reg1, 1),
          (troop_set_slot, ":troop_no", 0, reg1),
          (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
          (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
          (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
          (gt, ":party_no", 0),
          (call_script, "script_process_hero_ai", ":troop_no"),
        (try_end),
    ]),
    
    #TEMPORARILY DISABLED, AS READINESS IS NOW A PRODUCT OF NPC_DECISION_CHECKLIST
    # Changing readiness to join army
    #   (10,
    #   [
    #     (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
    #		(eq, 1, 0),
    #	    (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
    #        (assign, ":modifier", 1),
    #        (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
    #        (try_begin),
    #          (gt, ":party_no", 0),
    #          (party_get_slot, ":commander_party", ":party_no", slot_party_commander_party),
    #          (ge, ":commander_party", 0),
    #          (store_faction_of_party, ":faction_no", ":party_no"),
    #          (faction_get_slot, ":faction_marshal", ":faction_no", slot_faction_marshal),
    #          (ge, ":faction_marshal", 0),
    #          (troop_get_slot, ":marshal_party", ":faction_marshal", slot_troop_leaded_party),
    #          (eq, ":commander_party", ":marshal_party"),
    #          (assign, ":modifier", -1),
    #        (try_end),
    #        (troop_get_slot, ":readiness", ":troop_no", slot_troop_readiness_to_join_army),
    #        (val_add, ":readiness", ":modifier"),
    #        (val_clamp, ":readiness", 0, 100),
    #        (troop_set_slot, ":troop_no", slot_troop_readiness_to_join_army, ":readiness"),
    #        (assign, ":modifier", 1),
    #        (try_begin),
    #          (gt, ":party_no", 0),
    #          (store_troop_faction, ":troop_faction", ":troop_no"),
    #          (eq, ":troop_faction", "fac_player_supporters_faction"),
    #          (neg|troop_slot_eq, ":troop_no", slot_troop_player_order_state, spai_undefined),
    #          (party_get_slot, ":party_ai_state", ":party_no", slot_party_ai_state),
    #          (party_get_slot, ":party_ai_object", ":party_no", slot_party_ai_object),
    #          #Check if party is following player orders
    #          (try_begin),
    #            (troop_slot_eq, ":troop_no", slot_troop_player_order_state, ":party_ai_state"),
    #            (troop_slot_eq, ":troop_no", slot_troop_player_order_object, ":party_ai_object"),
    #            (assign, ":modifier", -1),
    #          (else_try),
    #            #Leaving following player orders if the current party order is not the same.
    #            (troop_set_slot, ":troop_no", slot_troop_player_order_state, spai_undefined),
    #            (troop_set_slot, ":troop_no", slot_troop_player_order_object, -1),
    #          (try_end),
    #        (try_end),
    #        (troop_get_slot, ":readiness", ":troop_no", slot_troop_readiness_to_follow_orders),
    #        (val_add, ":readiness", ":modifier"),
    #        (val_clamp, ":readiness", 0, 100),
    #        (troop_set_slot, ":troop_no", slot_troop_readiness_to_follow_orders, ":readiness"),
    #        (try_begin),
    #          (lt, ":readiness", 10),
    #          (troop_set_slot, ":troop_no", slot_troop_player_order_state, spai_undefined),
    #          (troop_set_slot, ":troop_no", slot_troop_player_order_object, -1),
    #        (try_end),
    #      (try_end),
    #     ]),
    
    # Process vassal ai
    ##   (2,
    ##   [
    ##     #(call_script, "script_process_kingdom_parties_ai"), #moved to above stochastic trigger
    ##   ]),
    
    # Process alarms - perhaps break this down into several groups, with a modula
    # (1, #this now calls 1/3 of all centers each time, thus hopefully lightening the CPU load
    (.022, #now calling two centers in this period (still all centers in 3 hours)
      [
        (call_script, "script_process_alarms"),
        (call_script, "script_process_alarms"),
        
        # (call_script, "script_allow_vassals_to_join_indoor_battle"), #functionality now in script_process_hero_ai
    ]),
    
    # Process siege ai tri-hourly ON AVERAGE
    (.025,
      [
        (store_current_hours, ":cur_hours"),
        (store_random_in_range, ":center_no", walled_centers_begin, walled_centers_end),
        (party_get_slot, ":besieger_party", ":center_no", slot_center_is_besieged_by),
        (gt, ":besieger_party", 0),
        (party_is_active, ":besieger_party"),
        (store_faction_of_party, ":besieger_faction", ":besieger_party"),
        (party_slot_ge, ":center_no", slot_center_is_besieged_by, 1),
        (party_get_slot, ":siege_begin_hours", ":center_no", slot_center_siege_begin_hours),
        (store_sub, ":siege_begin_hours", ":cur_hours", ":siege_begin_hours"),
        (assign, ":launch_attack", 0),
        (assign, ":call_attack_back", 0),
        (assign, ":attacker_strength", 0),
        (assign, ":marshal_attacking", 0),
        (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
          (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
          (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
          (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
          (gt, ":party_no", 0),
          (party_is_active, ":party_no"),
          
          (store_troop_faction, ":troop_faction_no", ":troop_no"),
          (eq, ":troop_faction_no", ":besieger_faction"),
          (assign, ":continue", 0),
          (try_begin),
            (party_slot_eq, ":party_no", slot_party_ai_state, spai_besieging_center),
            (party_slot_eq, ":party_no", slot_party_ai_object, ":center_no"),
            (assign, ":continue", 1),
          (else_try),
            (party_slot_eq, ":party_no", slot_party_ai_state, spai_accompanying_army),
            (party_get_slot, ":commander_party", ":party_no", slot_party_ai_object),
            (gt, ":commander_party", 0),
            (party_is_active, ":commander_party"),
            (party_slot_eq, ":commander_party", slot_party_ai_state, spai_besieging_center),
            (party_slot_eq, ":commander_party", slot_party_ai_object, ":center_no"),
            (assign, ":continue", 1),
          (try_end),
          (eq, ":continue", 1),
          (party_get_battle_opponent, ":opponent", ":party_no"),
          (this_or_next|lt, ":opponent", 0),
          (eq, ":opponent", ":center_no"),
          (try_begin),
            (faction_slot_eq, ":besieger_faction", slot_faction_marshal, ":troop_no"),
            (assign, ":marshal_attacking", 1),
          (try_end),
          (call_script, "script_party_calculate_regular_strength", ":party_no"),
          (val_add, ":attacker_strength", reg0),
        (try_end),
        (try_begin),
          (gt, ":attacker_strength", 0),
          (party_collect_attachments_to_party, ":center_no", "p_collective_enemy"),
          (call_script, "script_party_calculate_regular_strength", "p_collective_enemy"),
          (assign, ":defender_strength", reg0),
          (try_begin),
            (eq, "$auto_enter_town", ":center_no"),
            (eq, "$g_player_is_captive", 0),
            (call_script, "script_party_calculate_regular_strength", "p_main_party"),
            (val_add, ":defender_strength", reg0),
            (val_mul, ":attacker_strength", 2), #double the power of attackers if the player is in the campaign
          (try_end),
          (party_get_slot, ":siege_hardness", ":center_no", slot_center_siege_hardness),
          (val_add, ":siege_hardness", 100),
          (val_mul, ":defender_strength", ":siege_hardness"),
          (val_div, ":defender_strength", 100),
          (val_max, ":defender_strength", 1),
          (try_begin),
            (eq, ":marshal_attacking", 1),
            (eq, ":besieger_faction", "$players_kingdom"),
            (check_quest_active, "qst_follow_army"),
            (val_mul, ":attacker_strength", 2), #double the power of attackers if the player is in the campaign
          (try_end),
          (store_mul, ":strength_ratio", ":attacker_strength", 100),
          (val_div, ":strength_ratio", ":defender_strength"),
          (store_sub, ":random_up_limit", ":strength_ratio", 250), #was 300 (1.126)
          
          (try_begin),
            (gt, ":random_up_limit", -100), #never attack if the strength ratio is less than 150%
            (store_div, ":siege_begin_hours_effect", ":siege_begin_hours", 2), #was 3 (1.126)
            (val_add, ":random_up_limit", ":siege_begin_hours_effect"),
          (try_end),
          
          (val_div, ":random_up_limit", 5),
          (val_max, ":random_up_limit", 0),
          (store_sub, ":random_down_limit", 175, ":strength_ratio"), #was 200 (1.126)
          (val_max, ":random_down_limit", 0),
          (try_begin),
            (store_random_in_range, ":rand", 0, 100),
            (lt, ":rand", ":random_up_limit"),
            (gt, ":siege_begin_hours", 24),#initial preparation
            (assign, ":launch_attack", 1),
          (else_try),
            (store_random_in_range, ":rand", 0, 100),
            (lt, ":rand", ":random_down_limit"),
            (assign, ":call_attack_back", 1),
          (try_end),
        (else_try),
          (assign, ":call_attack_back", 1),
        (try_end),
        
        #Assault the fortress
        (try_begin),
          (eq, ":launch_attack", 1),
          (call_script, "script_begin_assault_on_center", ":center_no"),
        (else_try),
          (eq, ":call_attack_back", 1),
          (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
            (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
            (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
            (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
            (gt, ":party_no", 0),
            (party_is_active, ":party_no"),
            
            (party_slot_eq, ":party_no", slot_party_ai_state, spai_besieging_center),
            (party_slot_eq, ":party_no", slot_party_ai_object, ":center_no"),
            (party_slot_eq, ":party_no", slot_party_ai_substate, 1),
            (call_script, "script_party_set_ai_state", ":party_no", spai_undefined, -1),
            (call_script, "script_party_set_ai_state", ":party_no", spai_besieging_center, ":center_no"),
            #resetting siege begin time if at least 1 party retreats
            (party_set_slot, ":center_no", slot_center_siege_begin_hours, ":cur_hours"),
          (try_end),
        (try_end),
        # (try_end),
    ]),
    
    #STrig 40
    # Decide faction ais
    (6.6, #it was 23
      [
        (assign, "$g_recalculate_ais", 1),
    ]),
    
    # Decide faction ai flag check
    #When above trigger calls
    #When a lord changes factions
    #When a center changes factions
    #When a center is captured
    #When a marshal is defeated
    #More...
    (.11, [
        # (try_begin),
        # (ge, "$cheat_mode", 1),
        
        # (try_for_range, ":king", "trp_kingdom_1_lord", "trp_knight_1_1"),
        # (store_add, ":proper_faction", ":king", "fac_kingdom_1"),
        # (val_sub, ":proper_faction", "trp_kingdom_1_lord"),
        # (store_faction_of_troop, ":actual_faction", ":king"),
        
        # (neq, ":proper_faction", ":actual_faction"),
        # (neq, ":actual_faction", "fac_commoners"),
        # (ge, "$cheat_mode", 2),
        # (neq, ":king", "trp_kingdom_2_lord"),
        
        # (str_store_troop_name, s4, ":king"),
        # (str_store_faction_name, s5, ":actual_faction"),
        # (str_store_faction_name, s6, ":proper_faction"),
        # (str_store_string, s65, "@{!}DEBUG - {s4} is in {s5}, should be in {s6}, disabling political cheat mode"),
        #			(display_message, "@{s65}"),
        # (rest_for_hours, 0, 0, 0),
        
        #(assign, "$cheat_mode", 1),
        # (jump_to_menu, "mnu_debug_alert_from_s65"),
        # (try_end),
        # (try_end),
        
        (eq, "$g_recalculate_ais", 1),
        (assign, "$g_recalculate_ais", 0),
        (call_script, "script_init_ai_calculation"),
        
        (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
          (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
          #(neg|faction_slot_eq, ":faction_no",  slot_faction_marshal, "trp_player"),
          (call_script, "script_decide_faction_ai", ":faction_no"),
        (try_end),
        
        (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
          (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
          (call_script, "script_calculate_troop_ai", ":troop_no"),
        (try_end),
    ]),
    
    # Kingdoms daily ON AVERAGE
    (1.2, [
        (store_random_in_range, ":faction_no", kingdoms_begin, kingdoms_end),
        (try_begin),
          (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
          (call_script, "script_faction_recalculate_strength", ":faction_no"),
          
          (try_begin),
            (ge, ":faction_no", npc_kingdoms_begin),
            (faction_get_slot, ":faction_morale", ":faction_no",  slot_faction_morale_of_player_troops),
            
            (store_sub, ":divisor", 140, "$player_right_to_rule"),
            (val_div, ":divisor", 14),
            (val_max, ":divisor", 1),
            
            (store_div, ":faction_morale_div_10", ":faction_morale", ":divisor"), #10 is the base, down to 2 for 100 rtr
            (val_sub, ":faction_morale", ":faction_morale_div_10"),
            
            (faction_set_slot, ":faction_no",  slot_faction_morale_of_player_troops, ":faction_morale"),
          (try_end),
        (try_end),
    ]),
    
    # Reset hero quest status every 36 hours ON AVERAGE
    (.13,
      [
        (store_random_in_range, ":troop_no", heroes_begin, heroes_end),
        (troop_set_slot, ":troop_no", slot_troop_does_not_give_quest, 0),
        # (try_end),
        
        (store_random_in_range, reg0, 0, 2),
        (try_begin),
          (eq, reg0, 0),	#about half as many elders as heroes
          (store_random_in_range, ":troop_no", village_elders_begin, village_elders_end),
          (troop_set_slot, ":troop_no", slot_troop_does_not_give_quest, 0),
          
          #piggyback VC-3848 free elders held prisoner
          (troop_get_slot, ":held_by", ":troop_no", slot_troop_prisoner_of_party),
          (try_begin),
            (gt, ":held_by", "p_routed_enemies"),
            (party_remove_prisoners, ":held_by", ":troop_no", 1),
            (troop_set_slot, ":troop_no", slot_troop_prisoner_of_party, -1),
            
            (str_store_troop_name, s1, ":troop_no"),
            (store_sub, ":offset", ":troop_no", village_elders_begin),
            (store_add, ":village", ":offset", villages_begin),
            (str_store_party_name, s2, ":village"),
            (display_log_message, "@{s1} of {s2} has been released from captivity."),
          (try_end),
        (try_end),
    ]),
    # Moved to 24*5 trigger
    # Companions improving relations with castles/towns effects
    (24,
      [(try_for_range, ":troop", companions_begin, companions_end),
          (troop_slot_eq, ":troop", slot_troop_occupation, slto_player_companion),
          (neg|troop_slot_ge, ":troop", slot_troop_prisoner_of_party, 0),
          (troop_slot_eq, ":troop", slot_troop_current_mission, npc_mission_improve_relations),
          (troop_slot_ge, ":troop", slot_troop_days_on_mission, 1),
          (troop_get_slot, ":mission_object", ":troop", slot_troop_mission_object),
          (party_get_slot, ":center_relation", ":mission_object", slot_center_player_relation),
          (store_skill_level, ":persuasion", "skl_persuasion", ":troop"),
          (store_attribute_level, ":charisma", ":troop", ca_charisma),
          (store_attribute_level, ":intel", ":troop", ca_intelligence),
          (val_sub, ":persuasion", 4),
          (val_sub, ":charisma", 12),
          (val_sub, ":intel", 12),
          (val_div, ":intel", 3),
          (val_div, ":charisma", 2),
          (try_begin),
            (le, ":persuasion", 0),
            (assign, ":persuasion", 1),
          (else_try),
            (le, ":charisma", 0),
            (assign, ":charisma", 1),
          (else_try),
            (le, ":intel", 0),
            (assign, ":intel", 1),
          (try_end),
          (lt, ":center_relation", 0),
          (store_add, ":limit", 100, ":center_relation"),
          (try_begin),
            (gt, ":limit", 40),
            (assign, ":limit", 40),
          (try_end),
          (val_add, ":limit", ":persuasion"),
          (val_add, ":limit", ":charisma"),
          (val_add, ":limit", ":intel"),
          (str_store_troop_name, s33, ":troop"),
          (str_store_party_name, s34, ":mission_object"),
          (store_random_in_range, ":random", 0, ":limit"),
          (try_begin),
            (gt, ":random", 19),
            (call_script, "script_change_player_relation_with_center", ":mission_object", 1),
          (else_try),
            (try_begin),
              (gt, ":limit", 18),
              (le, ":random", 18),
              (store_div, ":half_limit", ":limit", 2),
              (store_random_in_range,":rand", 0, ":limit"),
              (try_begin),
                (le,":rand", ":half_limit"),
                (party_add_prisoners, ":mission_object", ":troop", 1),
                (troop_set_slot, ":troop", slot_troop_prisoner_of_party, ":mission_object"),
                (display_message, "@{s33} was beaten up and thrown into dungeon by an angry crowd in {s34}.", color_terrible_news),
              (else_try),
                (gt,":rand", ":half_limit"),
                (display_message, "@{s33}'s attempts to influence people of {s34} have failed.", color_bad_news),
              (try_end),
            (else_try),
              (le, ":limit", 18),
              (troop_set_slot, ":troop", slot_troop_days_on_mission, 0),
              (display_message, "@The people of {s34} hate you so much that the guards did not allow {s33} to enter.", color_bad_news),
            (try_end),
          (try_end),
        (try_end),
    ]),
    
    #Refreshing village defenders bi-daily ON AVERAGE
    #Clearing slot_village_player_can_not_steal_cattle flags
    (.32,
      [
        (store_random_in_range, ":village_no", villages_begin, villages_end),
        (call_script, "script_refresh_village_defenders", ":village_no"),
        (party_set_slot, ":village_no", slot_village_player_can_not_steal_cattle, 0),
        # (try_end),
    ]),
    
    #villages weekly ON AVERAGE
    (1.2, [
        (store_random_in_range, ":village_no", villages_begin, villages_end),
        
        # Refresh merchant inventories
        (call_script, "script_refresh_village_merchant_inventory", ":village_no"),
        
        # Refresh number of cattle in villages
        (party_get_slot, ":num_cattle", ":village_no", slot_center_head_cattle),
        (party_get_slot, ":num_sheep", ":village_no", slot_center_head_sheep),
        (party_get_slot, ":num_acres", ":village_no", slot_center_acres_pasture),
        (val_max, ":num_acres", 1),
        (store_mul, ":grazing_capacity", ":num_cattle", 400),
        (store_mul, ":sheep_addition", ":num_sheep", 200),
        (val_add, ":grazing_capacity", ":sheep_addition"),
        (val_div, ":grazing_capacity", ":num_acres"),
        
        (store_random_in_range, ":random_no", 0, 100),
        (try_begin), #Disaster
          (le, ":random_no", 5),#5% chance of epidemic - should happen once every two years It was more common in Dark Ages
          (val_min, ":num_cattle", 10),
          (val_min, ":num_sheep", 15),
          (party_get_slot, reg4, ":village_no", slot_center_head_cattle),
          (party_get_slot, reg5, ":village_no", slot_center_head_sheep),
          (val_sub, reg4, ":num_cattle"),
          (val_sub, reg5, ":num_sheep"),
          (try_begin),
            (lt, reg4, 0),
            (assign, reg4, 0),
          (try_end),
          (try_begin),
            (lt, reg5, 0),
            (assign, reg5, 0),
          (try_end),
          (try_begin),
            (gt, reg4, 0),
            (eq, reg5, 0),
            (party_slot_eq, ":village_no", slot_town_lord, "trp_player"),
            (str_store_party_name_link, s4, ":village_no"),
            (display_log_message, "@A livestock epidemic has killed {reg4} cattle in {s4}."),
          (else_try),
            (eq, reg4, 0),
            (gt, reg5, 0),
            (party_slot_eq, ":village_no", slot_town_lord, "trp_player"),
            (str_store_party_name_link, s4, ":village_no"),
            (display_log_message, "@A livestock epidemic has killed {reg5} sheep in {s4}."),
          (else_try),
            (gt, reg4, 0),
            (gt, reg5, 0),
            (party_slot_eq, ":village_no", slot_town_lord, "trp_player"),
            (str_store_party_name_link, s4, ":village_no"),
            (display_log_message, "@A livestock epidemic has killed {reg4} cattle and {reg5} sheep in {s4}."),
          (try_end),
        (else_try), #Overgrazing
          (gt, ":grazing_capacity", 100),
          
          (val_mul, ":num_sheep", 90), #10% decrease at number of cattles
          (val_div, ":num_sheep", 100),
          
          (val_mul, ":num_cattle", 90), #10% decrease at number of sheeps
          (val_div, ":num_cattle", 100),
          
        (else_try), #superb grazing
          (lt, ":grazing_capacity", 30),
          
          (val_mul, ":num_cattle", 120), #20% increase at number of cattles
          (val_div, ":num_cattle", 100),
          (val_add, ":num_cattle", 1),
          
          (val_mul, ":num_sheep", 120), #20% increase at number of sheeps
          (val_div, ":num_sheep", 100),
          (val_add, ":num_sheep", 1),
          
        (else_try), #very good grazing
          (lt, ":grazing_capacity", 60),
          
          (val_mul, ":num_cattle", 110), #10% increase at number of cattles
          (val_div, ":num_cattle", 100),
          (val_add, ":num_cattle", 1),
          
          (val_mul, ":num_sheep", 110), #10% increase at number of sheeps
          (val_div, ":num_sheep", 100),
          (val_add, ":num_sheep", 1),
          
        (else_try), #good grazing
          (lt, ":grazing_capacity", 100),
          (lt, ":random_no", 50),
          
          (val_mul, ":num_cattle", 105), #5% increase at number of cattles
          (val_div, ":num_cattle", 100),
          (try_begin), #if very low number of cattles and there is good grazing then increase number of cattles also by one
            (le, ":num_cattle", 20),
            (val_add, ":num_cattle", 1),
          (try_end),
          
          (val_mul, ":num_sheep", 105), #5% increase at number of sheeps
          (val_div, ":num_sheep", 100),
          (try_begin), #if very low number of sheeps and there is good grazing then increase number of sheeps also by one
            (le, ":num_sheep", 20),
            (val_add, ":num_sheep", 1),
          (try_end),
        (try_end),
        
        (party_set_slot, ":village_no", slot_center_head_cattle, ":num_cattle"),
        (party_set_slot, ":village_no", slot_center_head_sheep, ":num_sheep"),
    ]),
    
    #Accumulate taxes MOVED to centers weekly trigger
    #  (24,
    #   [
    #    ]),
    
    # JuJu70  (47)
    # Recruiting in villages for adventurers hourly on average
    (0.03,
      [
        (store_random_in_range, ":troop_no", companions_begin, kings_end),   #VC-3907 include leaders of defeated factions
          (store_faction_of_troop, ":hero_faction", ":troop_no"),
          (eq, ":hero_faction", "fac_adventurers"),
          (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
          (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
          (troop_get_slot, ":hero_party",":troop_no", slot_troop_leaded_party),
          (ge, ":hero_party", 1),
          (party_slot_eq, ":hero_party", slot_party_type, spt_kingdom_hero_party),
          (party_is_active, ":hero_party"),
          #		(store_faction_of_party, ":hero_faction", ":hero_party"),
          
          #things we don't want to interrupt to recruit
          (get_party_ai_behavior, ":ai_bhvr", ":hero_party"),
          #		(party_get_slot, ":ai_behavior", ":hero_party", slot_party_ai_state),
          #		(assign, reg33, ":ai_bhvr"),
          #		(assign, reg35, ":ai_behavior"),
          #		(display_message, "@Behavior {reg33} and ai state is {reg35}"),
          (neq, ":ai_bhvr", ai_bhvr_travel_to_party),
          (neg|party_slot_eq, ":hero_party", slot_party_ai_state, spai_trading_with_town),
          (neg|faction_slot_eq, ":hero_faction", slot_faction_marshal, ":troop_no"),
          
          (call_script, "script_party_get_ideal_size", ":hero_party"),
          (assign, ":ideal_size", reg0),
          (store_party_size_wo_prisoners, ":party_size", ":hero_party"),
          #		(store_mul, ":party_strength_as_percentage_of_ideal", ":party_size", 100),
          #		(val_div, ":party_strength_as_percentage_of_ideal", ":ideal_size"),
          (store_mul, ":adj_ideal", ":ideal_size", 130),
          (val_div, ":adj_ideal", 100),
          (val_min, ":ideal_size", 100),
          (try_begin),
            (this_or_next|lt, ":party_size", ":adj_ideal"),
            (lt, ":party_size", ":ideal_size"),
            (assign, ":minimum_distance", 200),
            (assign, ":closest_village", -1),
            (try_for_range, ":village_no", villages_begin, villages_end),
              (store_distance_to_party_from_party, ":dist", ":hero_party",":village_no"),
              (lt, ":dist", ":minimum_distance"),
              (try_begin),
                (store_faction_of_party, ":village_faction", ":village_no"),
                (assign, ":faction_relation", 100),
                (try_begin),
                  (neq, ":village_faction", ":hero_faction"),    # faction relation will be checked only if the village doesn't belong to the hero's current faction
                  (store_relation, ":faction_relation", ":hero_faction", ":village_faction"),
                (try_end),
                (ge, ":faction_relation", 0),
                (party_get_slot, ":volunteers_in_village", ":village_no", slot_center_npc_volunteer_troop_amount),
                (gt, ":volunteers_in_village", 0),
                (neg|party_slot_eq, ":village_no", slot_village_state, svs_looted),
                (neg|party_slot_eq, ":village_no", slot_village_state, svs_being_raided),
                (neg|party_slot_ge, ":village_no", slot_village_infested_by_bandits, 1),
                (assign, ":minimum_distance", ":dist"),
                (assign, ":closest_village", ":village_no"),
              (try_end),
            (try_end),
            
            (gt, ":closest_village", -1),
            (party_get_slot, ":volunteers_in_target", ":closest_village", slot_center_npc_volunteer_troop_amount),
            (party_set_ai_object, ":hero_party", ":closest_village"),
            (party_get_position, pos1, ":closest_village"),
            (map_get_random_position_around_position, pos2, pos1, 2),
            (party_set_ai_target_position, ":hero_party", pos2),
            (party_set_slot, ":hero_party", slot_party_ai_object, ":closest_village"),
            (party_set_slot, ":hero_party", slot_party_ai_state, spai_patrolling_around_center),
            
            (store_distance_to_party_from_party, ":distance_from_target", ":hero_party", ":closest_village"),
            (try_begin),
              (gt, ":distance_from_target", 2),
              (party_set_ai_behavior, ":hero_party", ai_bhvr_travel_to_point),
              
            (else_try),
              (party_get_slot, ":target_volunteer_type", ":closest_village", slot_center_npc_volunteer_troop_type),
              (store_sub, ":needed", ":ideal_size", ":party_size"),
              (try_begin),
                (gt, ":needed", 0),
                (assign, ":still_needed", ":needed"),
              (else_try),
                (le, ":needed", 0),
                (store_sub, ":still_needed", ":adj_ideal", ":party_size"),
              (try_end),
              
              (gt, ":volunteers_in_target", ":still_needed"),
              (gt, ":still_needed", 0),
              (store_sub, ":new_target_volunteer_amount", ":volunteers_in_target", ":still_needed"),
              (party_set_slot, ":closest_village", slot_center_npc_volunteer_troop_amount, ":new_target_volunteer_amount"),
              (party_add_members, ":hero_party", ":target_volunteer_type", ":still_needed"),
              (party_set_ai_behavior, ":hero_party", ai_bhvr_hold),
              
            (else_try),
              #set behavior for when no more recruits
              (party_set_ai_behavior, ":hero_party", ai_bhvr_patrol_location),
              (party_set_ai_patrol_radius, ":hero_party", 35),
              (party_set_aggressiveness, ":hero_party", 10),
              (party_set_courage, ":hero_party", 11),
              (party_set_ai_initiative, ":hero_party", 100),
              (party_set_helpfulness, ":hero_party", 110),
              
              #get last recruits (if any)
              (le, ":volunteers_in_target", ":still_needed"),
              (gt, ":volunteers_in_target", 0),
              (party_set_slot, ":closest_village", slot_center_npc_volunteer_troop_amount, -1),
              (party_add_members, ":hero_party", ":target_volunteer_type", ":volunteers_in_target"),
            (try_end),
          
          #no need or ability to recruit
          (else_try),
            #things we don't want to interrupt
            (neq, ":ai_bhvr", ai_bhvr_attack_party),
            (neq, ":ai_bhvr", ai_bhvr_travel_to_ship),
            (neq, ":ai_bhvr", ai_bhvr_escort_party),
            
            (neg|party_slot_eq, ":hero_party", slot_party_ai_state, spai_raiding_around_center),
            (neg|party_slot_eq, ":hero_party", slot_party_ai_state, spai_besieging_center),
            (neg|party_slot_eq, ":hero_party", slot_party_ai_state, spai_engaging_army),
            (neg|party_slot_eq, ":hero_party", slot_party_ai_state, spai_holding_center),
            (neg|party_slot_eq, ":hero_party", slot_party_ai_state, spai_accompanying_army),
            (neg|party_slot_eq, ":hero_party", slot_party_ai_state, spai_screening_army),
            
            (party_slot_eq, ":hero_party", slot_party_on_water, 0),
            
            (party_get_slot, ":target", ":hero_party", slot_party_ai_object),
            (try_begin),
              (is_between, ":target", walled_centers_begin, walled_centers_end),
              
              (store_faction_of_party, ":town_faction", ":target"),
              (assign, ":faction_relation", 100),
              (try_begin),
                (neq, ":town_faction", ":hero_faction"),
                (store_relation, ":faction_relation", ":hero_faction", ":town_faction"),
              (try_end),
              (ge, ":faction_relation", 0),
              
              (store_distance_to_party_from_party, ":dist", ":hero_party",":target"),
              (try_begin),
                (le, ":dist", 50),  #at destination?
                (party_set_ai_object, ":hero_party", ":target"),
                (party_set_ai_behavior, ":hero_party", ai_bhvr_patrol_party),
                (party_set_slot, ":hero_party", slot_party_ai_object, ":target"),
                (party_set_slot, ":hero_party", slot_party_ai_state, spai_patrolling_around_center),
                (party_set_ai_patrol_radius, ":hero_party", 55),
                
                (party_set_aggressiveness, ":hero_party", 10),
                (party_set_courage, ":hero_party", 11),
                (party_set_ai_initiative, ":hero_party", 100),
                (party_set_helpfulness, ":hero_party", 110),
              (try_end),
              
            #set a destination
            (else_try),
              (assign, ":minimum_distance", 150),
              (assign, ":closest_town", -1),
              (try_for_range, ":town_no", walled_centers_begin, walled_centers_end),
                (store_distance_to_party_from_party, ":dist", ":hero_party",":town_no"),
                (lt, ":dist", ":minimum_distance"),
                (try_begin),
                  (store_faction_of_party, ":town_faction", ":town_no"),
                  (assign, ":faction_relation", 100),
                  (try_begin),
                    (neq, ":town_faction", ":hero_faction"),
                    (store_relation, ":faction_relation", ":hero_faction", ":town_faction"),
                  (try_end),
                  (ge, ":faction_relation", 0),
                  (assign, ":minimum_distance", ":dist"),
                  (assign, ":closest_town", ":town_no"),
                (try_end),
              (try_end),
              
              (try_begin),
                (le, ":closest_town", 0),
                (troop_get_slot, ":closest_town", ":troop_no", slot_troop_home),
              (try_end),
              
              (party_set_ai_object, ":hero_party", ":closest_town"),
              (party_get_position, pos1, ":closest_town"),
              (map_get_random_position_around_position, pos2, pos1, 10),
              (party_set_ai_behavior, ":hero_party", ai_bhvr_travel_to_point),
              (party_set_ai_target_position, ":hero_party", pos2),
              (party_set_slot, ":hero_party", slot_party_ai_object, ":closest_town"),
              (party_set_slot, ":hero_party", slot_party_ai_state, spai_patrolling_around_center),
              (party_set_ai_patrol_radius, ":hero_party", 35),
              (party_set_aggressiveness, ":hero_party", 10),
              (party_set_courage, ":hero_party", 11),
              (party_set_ai_initiative, ":hero_party", 100),
              (party_set_helpfulness, ":hero_party", 110),
            (try_end),
          (try_end),
    ]),
    
    # Offer player to join faction
    # Only if the player is male -- female characters will be told that they should seek out a faction through NPCs, possibly
    (32,
      [
        (eq, "$players_kingdom", 0),
        (le, "$g_invite_faction", 0),
        (eq, "$g_player_is_captive", 0),
        (neq, "$campaign_type", camp_storyline),# not in storyline
        (troop_get_type, ":type", "trp_player"),
        (val_mod, ":type", 2),
        (try_begin),
          (eq, ":type", 1),
          (eq, "$npc_with_sisterly_advice", 0),
          (try_for_range, ":npc", companions_begin, companions_end),
            (main_party_has_troop, ":npc"),
            (troop_get_type, ":npc_type", ":npc"),
            (val_mod, ":npc_type", 2),
            (eq, ":npc_type", 1),
            (troop_slot_ge, "trp_player", slot_troop_renown, 150),
            (troop_slot_ge, ":npc", slot_troop_woman_to_woman_string, 1),
            (assign, "$npc_with_sisterly_advice", ":npc"),
          (try_end),
        (else_try),
          (store_random_in_range, ":kingdom_no", npc_kingdoms_begin, npc_kingdoms_end),
          (assign, ":min_distance", 999999),
          (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
            (store_faction_of_party, ":center_faction", ":center_no"),
            (eq, ":center_faction", ":kingdom_no"),
            (store_distance_to_party_from_party, ":cur_distance", "p_main_party", ":center_no"),
            (val_min, ":min_distance", ":cur_distance"),
          (try_end),
          (lt, ":min_distance", 30),
          (store_relation, ":kingdom_relation", ":kingdom_no", "fac_player_faction"),
          (faction_get_slot, ":kingdom_lord", ":kingdom_no", slot_faction_leader),
          (call_script, "script_troop_get_player_relation", ":kingdom_lord"),
          (assign, ":lord_relation", reg0),
          #(troop_get_slot, ":lord_relation", ":kingdom_lord", slot_troop_player_relation),
          (call_script, "script_get_number_of_hero_centers", "trp_player"),
          (assign, ":num_centers_owned", reg0),
          (eq, "$g_infinite_camping", 0),
          
          (assign, ":player_party_size", 0),
          (try_begin),
            (ge, "p_main_party", 0),
            (store_party_size_wo_prisoners, ":player_party_size", "p_main_party"),
          (try_end),
          
          (try_begin),
            (eq, ":num_centers_owned", 0),
            (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
            (ge, ":player_renown", 160),
            (ge, ":kingdom_relation", 0),
            (ge, ":lord_relation", 0),
            (ge, ":player_party_size", 45),
            (store_random_in_range, ":rand", 0, 100),
            (lt, ":rand", 50),
            (call_script, "script_get_poorest_village_of_faction", ":kingdom_no"),
            (assign, "$g_invite_offered_center", reg0),
            (ge, "$g_invite_offered_center", 0),
            (assign, "$g_invite_faction", ":kingdom_no"),
            (jump_to_menu, "mnu_invite_player_to_faction"),
          (else_try),
            (gt, ":num_centers_owned", 0),
            (neq, "$players_oath_renounced_against_kingdom", ":kingdom_no"),
            (ge, ":kingdom_relation", -40),
            (ge, ":lord_relation", -20),
            (ge, ":player_party_size", 30),
            (store_random_in_range, ":rand", 0, 100),
            (lt, ":rand", 20),
            (assign, "$g_invite_faction", ":kingdom_no"),
            (assign, "$g_invite_offered_center", -1),
            (jump_to_menu, "mnu_invite_player_to_faction_without_center"),
          (try_end),
        (try_end),
    ]),
    
    #active NPCs weekly ON AVERAGE
    (1.1, [
        (store_random_in_range, ":troop_no", "trp_kingdom_heroes_including_player_begin", active_npcs_end),
        
        (try_begin),
          (eq, ":troop_no", "trp_kingdom_heroes_including_player_begin"),
          (assign, ":troop_no", "trp_player"),
          (assign, ":faction", "$players_kingdom"),
          
        (else_try),
          (store_faction_of_troop, ":faction", ":troop_no"),
          (neq, ":faction", "fac_outlaws"),
          #recalculate lord random decision seeds
          (store_random_in_range, ":random", 0, 9999),
          (troop_set_slot, ":troop_no", slot_troop_temp_decision_seed, ":random"),
          
          #npcs will only change their minds on issues at least 24 hours after speaking to the player
          #(store_current_hours, ":hours"),
          #(try_begin),
          #  (eq, 1, 0), #disabled
          #  (try_for_range, ":npc", active_npcs_begin, active_npcs_end),
          #    (troop_get_slot, ":last_talk", ":npc", slot_troop_last_talk_time),
          #    (val_sub, ":hours", ":last_talk"),
          #    (ge, ":hours", 24),
          #    (store_random_in_range, ":random", 0, 9999),
          #    (troop_set_slot, ":npc", slot_troop_temp_decision_seed, ":random"),
          #  (try_end),
          #(try_end),
          
          #Increasing debts to heroes by 1% (once a week)
          (troop_get_slot, ":cur_debt", ":troop_no", slot_troop_player_debt),#Increasing debt
          (val_mul, ":cur_debt", 101),
          (val_div, ":cur_debt", 100),
          (troop_set_slot, ":troop_no", slot_troop_player_debt, ":cur_debt"),
          
          (troop_get_slot, ":religion",":troop_no", slot_troop_religion),
          (troop_get_slot, ":controversy", ":troop_no", slot_troop_controversy),
          
          # Clearing conversion fails
          (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
          (try_begin),
            (troop_slot_eq, ":troop_no", slot_troop_conv, 1),
            (troop_set_slot, ":troop_no", slot_troop_conv, 0),
          
          # Player's converts
          (else_try),
            (troop_slot_eq, ":troop_no", slot_troop_conv, 2),
            (try_begin),
              (eq, ":religion", 1),
              (troop_set_slot, ":troop_no", slot_troop_religion, 2),
            (else_try),
              (troop_set_slot, ":troop_no", slot_troop_religion, 1),
            (try_end),
            (val_add, ":controversy", 5),
            (troop_set_slot, ":troop_no", slot_troop_controversy, ":controversy"),
            (troop_set_slot, ":troop_no", slot_troop_conv, 0),
          
          # Random conversion
          (else_try),
            (assign, ":chance", 1),
            
            #lord will convert to religion favored by faction/lords 3x faster, so on average only 1/3 faction will be a different religion
            #faction religion
            (try_begin),
              (eq, ":religion", 1),
              (faction_slot_eq, ":faction", slot_faction_religion, cb3_pagan),
              (val_add, ":chance", 1),
            (else_try),
              (eq, ":religion", 2),
              (faction_slot_eq, ":faction", slot_faction_religion, cb3_christian),
              (val_add, ":chance", 1),
            (try_end),
            
            #don't convert to the "wrong" religion if already in too much trouble
            (this_or_next|gt, ":chance", 1),
            (lt, ":controversy", 40),
            
            #lords' religion
            (assign, ":rel_comp", 0),
            (try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
              (troop_slot_eq, ":active_npc", slot_troop_occupation, slto_kingdom_hero),
              (store_faction_of_troop, ":npc_faction", ":active_npc"),
              (eq, ":npc_faction", ":faction"),
              (neq, ":active_npc", ":troop_no"),
              (troop_get_slot, ":religion1",":active_npc", slot_troop_religion),
              (try_begin),
                (eq, ":religion1", ":religion"),
                (val_add, ":rel_comp", -1),
              (else_try),
                (val_add, ":rel_comp", 1),
              (try_end),
            (try_end),
            #		(assign, reg33, ":rel_comp"),
            #		(display_message, "@{reg33} more lords with a different religion"),
            (try_begin),
              (gt, ":rel_comp", 0),
              (val_add, ":chance", 1),
            (try_end),
            
            #lord personalities
            (try_begin),
              (this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_cunning),
              (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_debauched),
              (val_add, ":chance", 2),
            (else_try),
              (this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_roguish),
              (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_quarrelsome),
              (val_add, ":chance", 1),
            (try_end),
            #		(assign, reg32, ":chance"),
            #		(str_store_troop_name, s31, ":troop_no"),
            #		(display_message, "@{s31} has a {reg32} chance of conversion"),
            
            (store_random_in_range, ":conv", 0, 150), #lord will convert on average n = log(.5)/log(1.00 - 1/150) = 103 weeks = 2 years
            #		(assign, reg33, ":conv"),
            #		(display_message, "@Random is {reg33}"),
            (lt, ":conv", ":chance"),
            (try_begin),
              (eq, ":religion", 1),
              (troop_set_slot, ":troop_no", slot_troop_religion, 2),
            (else_try),
              (troop_set_slot, ":troop_no", slot_troop_religion, 1),
            (try_end),
            (val_add, ":controversy", 5),
            (troop_set_slot, ":troop_no", slot_troop_controversy, ":controversy"),
          (try_end),
          # End conversion
          
          #Adding net incomes to heroes (once a week)
          (call_script, "script_calculate_hero_weekly_net_income_and_add_to_wealth", ":troop_no"),#Adding net income
        (try_end), #not player
        
        #Individual lord political calculations
        #Check for lords without fiefs, auto-defections, etc
        (troop_get_slot, ":prisoner_of_party", ":troop_no", slot_troop_prisoner_of_party),  #VC-3705 weird things happen when imprisoned lords defect or are indicted
        (lt,":prisoner_of_party", 0),
        
        (neq, ":faction", "fac_outlaws"),   #VC-3909 unwanted escaped prisoners that can't spawn a party

        (try_begin),
          (eq, "$cheat_mode", 1),
          (str_store_troop_name, s1, ":troop_no"),
          (display_message, "@{!}DEBUG -- Doing political calculations for {s1}"),
        (try_end),
        
        (assign, ":fief_found", -1),
        (assign, ":num_centers", 0),
        
        (try_for_range, ":center", centers_begin, centers_end),
          (try_begin),
            (party_slot_eq, ":center", slot_town_lord, ":troop_no"),
            (assign, ":fief_found", ":center"),
          (try_end),
          
          (is_between,":center", walled_centers_begin, walled_centers_end),
          (store_faction_of_party, ":faction_of_center", ":center"),
          (eq, ":faction_of_center", ":faction"),
          (val_add, ":num_centers", 1),
        (try_end),
        
        #Penalty for no fief
        (faction_get_slot, ":faction_leader", ":faction", slot_faction_leader),
        (try_begin),
          (eq, ":fief_found", -1),
          (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
          (neq, ":troop_no", "trp_player"),
          (neq, ":troop_no", ":faction_leader"),
          (gt, ":faction_leader", -1),
          (neq, ":faction", "fac_adventurers"),
          (neq, ":faction", "fac_commoners"),
          
          (troop_get_slot, ":troop_reputation", ":troop_no", slot_lord_reputation_type),
          (try_begin),
            (this_or_next|eq, ":troop_reputation", lrep_quarrelsome),
            (this_or_next|eq, ":troop_reputation", lrep_selfrighteous),
            (this_or_next|eq, ":troop_reputation", lrep_cunning),
            (eq, ":troop_reputation", lrep_debauched),
            (try_begin),
              (eq, ":faction", "fac_player_supporters_faction"),
              (str_store_troop_name, s1, ":troop_no"),
              (display_message, "@You receive a message from {s1} demanding lands to support them in a style that befits them."),
            (try_end),
            (call_script, "script_troop_change_relation_with_troop", ":troop_no", ":faction_leader", -4),  #three months for neutral lord to start considering defection (see below)
            (val_add, "$total_no_fief_changes", -4),
            
          (else_try),
            (try_begin),
              (eq, ":faction", "fac_player_supporters_faction"),
              (str_store_troop_name, s1, ":troop_no"),
              (display_message, "@You receive a message from {s1} reminding you of your obligations to provide for your vassals."),
            (try_end),
            (call_script, "script_troop_change_relation_with_troop", ":troop_no", ":faction_leader", -2),  #six months for neutral lord to start considering defection (see below)
            (val_add, "$total_no_fief_changes", -2),
          (try_end),
        (try_end),
        
        #Auto-indictment or defection
        (try_begin),
          (neq, "$campaign_type", camp_storyline), #disable both auto-defection and auto-indictment completely in storyline mode, only let for sandbox mode chief.
          
          (try_begin),
            (eq, ":faction_leader", "trp_player"),
            (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_inactive), #waiting on player to accept them into faction?
            (assign, ":cont", 1),
          (else_try),
            (assign, ":cont", 0),
          (try_end),

          (this_or_next|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
          (this_or_next|eq, ":cont", 1),
          (eq, ":troop_no", "trp_player"),
          
          (neq, ":troop_no", ":faction_leader"),
          (neg|is_between, ":troop_no", kings_begin, kings_end),
          (neg|is_between, ":troop_no", pretenders_begin, pretenders_end),
          
          #VC-3915 use this process for lords of defeated factions
          (assign, ":seek_new_faction", 0),
          
          (try_begin),
            (eq, ":faction", "fac_adventurers"),
            
            (try_begin),
              (is_between, ":troop_no", lords_begin, lords_end),  #NPC adventurers have "AI Invite adventurers to become lords"
              (assign, ":seek_new_faction", recruit_adv),
            (try_end),
            
          #VC-3915 original case lords of active factions
          (else_try),
            (neq, ":faction", "fac_commoners"),
            (faction_slot_eq, ":faction", slot_faction_state, sfs_active),
            
            (assign, "$g_talk_troop", -1),  #see comments in script_calculate_troop_political_factors_for_liege
            (call_script, "script_calculate_troop_political_factors_for_liege", ":troop_no", ":faction_leader"),    #VC-3909 tie directly to reported unhappiness
            (assign, ":happiness", reg3),
            
            # pointless now that no longer auto defect for centerless factions; all it does is ensure player has advantage
            # #we are counting num_centers to allow defection although there is high relation between faction leader and troop.
            # #but this rule should not applied for player's faction and player_supporters_faction so thats why here 1 is added to num_centers in that case.
            # (try_begin),
              # (this_or_next|eq, ":faction", "$players_kingdom"),
              # (eq, ":faction", "fac_player_supporters_faction"),
              # (val_add, ":num_centers", 1),
            # (try_end),
            
            (neq, ":troop_no", "trp_player"),  #VC-3955 don't assign motive to player
            
            (try_begin),
              (eq, ":num_centers", 0), #if there is no walled centers that faction has defection happens 100%.
              (assign, ":seek_new_faction", no_income),
              
            (else_try),
              (le, ":happiness", defection_trigger),
              (call_script, "script_cf_troop_can_intrigue", ":troop_no", 0), #Should include battle, prisoner, in a castle with others
              (store_random_in_range, ":cont", 0, 2),
              (eq, ":cont", 0),
              (assign, ":seek_new_faction", court_intrigue),
              
            (else_try),
              (le, ":happiness", defection_trigger),
              (eq, ":faction_leader", "trp_player"),
              (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_inactive), #waiting on player to accept them into faction?
              (assign, ":seek_new_faction", court_intrigue),
            (try_end),
          (try_end),
            
          #do a defection
          (try_begin),
            # (this_or_next|eq, ":num_centers", 0), #Thanks Caba`drin & Osviux #VC-3915 handled by ":seek_new_faction" now
            (neq, ":seek_new_faction", 0),
            # (neq, ":troop_no", "trp_player"), VC-3955 caught above
            
            (assign, "$g_give_advantage_to_original_faction", 0),
            # (try_begin),  VC-3918 why use a global to pass an argument to the next function down? never mind that it counts walled centers AGAIN, so is completely unnecessary
              # (neq, ":num_centers", 0),
              # (assign, "$g_give_advantage_to_original_faction", 1),
            # (try_end),
            
            (call_script, "script_lord_find_alternative_faction", ":troop_no", 0),
            (assign, ":new_faction", reg0),
            
            (try_begin),  #case nowhere to go
              (neg|is_between, ":new_faction", kingdoms_begin, kingdoms_end),
              
              #cases hero can't remain a lord
              (try_begin),
                (this_or_next|eq, ":seek_new_faction", no_income),
                (eq, ":seek_new_faction", recruit_adv), #lords of defeated factions now out of prison
                (troop_set_slot, ":troop_no", slot_troop_change_to_faction, "fac_outlaws"),
                
                (try_begin),
                  (eq, "$cheat_mode", 1),
                  (str_store_troop_name, s1, ":troop_no"),
                  (display_message, "@{!}DEBUG -- Remove {s1} to fac_outlaws"),
                (try_end),
              (try_end),

            (else_try),
              (neq, ":new_faction", ":faction"),  #new kingdom found
              
              (assign, ":cont", 1),
              (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
              
              (try_begin),
                (gt, ":party_no", -1),
                (party_get_attached_to, ":attached_to",":party_no"),
                (gt, ":attached_to", -1),
                (assign, ":cont", 0),
              (try_end),
              
              (try_begin),
                (eq, ":cont", 1),
                
                (str_store_troop_name_link, s1, ":troop_no"),
                (str_store_faction_name_link, s2, ":new_faction"),
                (str_store_faction_name_link, s3, ":faction"),
                (call_script, "script_change_troop_faction", ":troop_no", ":new_faction"),
                
                (troop_get_type, reg4, ":troop_no"),
                (val_mod, reg4, 2),
                (str_store_string, s4, "str_lord_defects_ordinary"),
                (display_log_message, "@{!}{s4}"),
                
                (try_begin),
                  (ge, "$cheat_mode", 1),
                  (this_or_next|eq, ":new_faction", "$players_kingdom"),
                  (eq, ":faction", "$players_kingdom"),
                  (call_script, "script_add_notification_menu", "mnu_notification_lord_defects", ":troop_no", ":faction"),
                (try_end),
              (try_end),
            (try_end),
          (try_end),    #defection
          
          #do an indictment
          (try_begin),
            (neq, ":faction", "fac_adventurers"),
            (neq, ":faction", "fac_commoners"),
            (faction_slot_eq, ":faction", slot_faction_state, sfs_active),
            
            (neq, ":faction_leader", "trp_player"),
            (neg|is_between, ":faction_leader", pretenders_begin, pretenders_end),  #VC-3834
            
            (le, ":happiness", defection_trigger),  #faction leader purges whomever is left
            
            (try_begin),
              (eq, ":seek_new_faction", 0),
              (assign, ":cont", 1),
            (else_try),
              (eq, ":seek_new_faction", court_intrigue),
              (store_faction_of_troop, ":new_faction", ":troop_no"),
              (eq, ":new_faction", ":faction"),  #new kingdom wasn't found
              (assign, ":cont", 1),
            # (else_try),   VC-3955 included first case
              # (eq, ":troop_no", "trp_player"),
              # (assign, ":cont", 1),
            (else_try),
              (assign, ":cont", 0),
            (try_end),
            
            (eq, ":cont", 1),
            (call_script, "script_indict_lord_for_treason", ":troop_no", ":faction"),
          (try_end),
        (try_end),  #auto-indict/defect
        
        #Take a stand on an issue
        (try_begin),
          (faction_slot_eq, ":faction", slot_faction_state, sfs_active),
          (neq, ":troop_no", "trp_player"),
          #     (store_faction_of_troop, ":faction", ":troop_no"),
          (faction_slot_ge, ":faction", slot_faction_political_issue, 1),
          #This bit of complication is needed for savegame compatibility -- if zero is in the slot, they'll choose anyway
          (neg|troop_slot_ge, ":troop_no", slot_troop_stance_on_faction_issue, 1),
          (this_or_next|troop_slot_eq, ":troop_no", slot_troop_stance_on_faction_issue, -1),
          (neq, "$players_kingdom", ":faction"),
          (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
          (call_script, "script_npc_decision_checklist_take_stand_on_issue", ":troop_no"),
          (troop_set_slot, ":troop_no", slot_troop_stance_on_faction_issue, reg0),
        (try_end),
        # Fixing rels with spouses
        (try_begin),
          (troop_get_slot, ":spouse", ":troop_no", slot_troop_spouse),
          (ge, ":spouse", 0),
          (call_script, "script_troop_get_relation_with_troop", ":spouse", ":troop_no"),
          (lt, reg0, 0),
          (call_script, "script_troop_change_relation_with_troop",  ":spouse", ":troop_no", 1),
        (try_end),
        # End fixing
        (try_for_range, ":active_npc", active_npcs_including_player_begin, active_npcs_end),
          (try_begin),
            (eq, ":active_npc", "trp_kingdom_heroes_including_player_begin"),
            (assign, ":active_npc", "trp_player"),
          (try_end),
          
          (neq, ":troop_no", ":active_npc"),
          (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":active_npc"),
          (assign, ":relation", reg0),
          
          # Reduce relations between lords based on religion
          # JuJu70
          (set_show_messages, 0),
          (try_begin),
            (gt, ":relation", -7),
            #       (neq, ":troop_no", "trp_player"), prevents player to lose relations with anyone if player is Christian
            (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
            (troop_slot_eq, ":troop_no", slot_troop_religion, 1),#only christian lords
            (troop_slot_eq, ":active_npc", slot_troop_occupation, slto_kingdom_hero),
            (troop_slot_eq, ":active_npc", slot_troop_religion, 2),#only pagan lords
            (store_add, ":chance_of_convergence", ":relation", 6),
            (store_random_in_range, ":random", -2, 106),
            (lt,":random", ":chance_of_convergence"),
            (call_script, "script_troop_change_relation_with_troop", ":troop_no", ":active_npc", -1),
            # JuJu70
            
            #convergence
          (else_try),
            (lt, ":relation", 0),
            (neq, ":troop_no", "trp_player"),
            (neq, ":active_npc", "trp_player"),
            (store_sub, ":chance_of_convergence", 0, ":relation"),
            (store_random_in_range, ":random", 0, 125),
            (lt, ":random", ":chance_of_convergence"),
            (call_script, "script_troop_change_relation_with_troop", ":troop_no", ":active_npc", 1),
            (val_add, "$total_relation_changes_through_convergence", 1),
            
          (else_try),
            (gt, ":relation", 0),
            (neq, ":troop_no", "trp_player"),
            (neq, ":active_npc", "trp_player"),
            (assign, ":chance_of_convergence", ":relation"),
            (store_random_in_range, ":random", 0, 100),
            (lt, ":random", ":chance_of_convergence"),
            (call_script, "script_troop_change_relation_with_troop", ":troop_no", ":active_npc", -1),
            (val_add, "$total_relation_changes_through_convergence", -1),
          (else_try),
            (troop_get_slot, ":rob", ":troop_no", slot_troop_robbed),
            (gt, ":rob", 0),
            (val_mul, ":rob", -1),
            (eq, ":active_npc", "trp_player"),
            (call_script, "script_troop_change_relation_with_troop", ":troop_no", ":active_npc",":rob"),
          (try_end),
          (set_show_messages, 1),
        (try_end),
    ]),
    
    # During rebellion, removing troops from player faction randomly because of low relation points
    # Deprecated -- should be part of regular political events
    
    
    # Reset kingdom lady current centers
    ##   (28,
    ##   [
    ##       (try_for_range, ":troop_no", heroes_begin, heroes_end),
    ##         (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_lady),
    ##
    ##         # Find the active quest ladies
    ##         (assign, ":not_ok", 0),
    ##         (try_for_range, ":quest_no", lord_quests_begin, lord_quests_end),
    ##           (eq, ":not_ok", 0),
    ##           (check_quest_active, ":quest_no"),
    ##           (quest_slot_eq, ":quest_no", slot_quest_object_troop, ":troop_no"),
    ##           (assign, ":not_ok", 1),
    ##         (try_end),
    ##         (eq, ":not_ok", 0),
    ##
    ##         (troop_get_slot, ":troop_center", ":troop_no", slot_troop_cur_center),
    ##         (assign, ":is_under_siege", 0),
    ##         (try_begin),
    ##           (is_between, ":troop_center", walled_centers_begin, walled_centers_end),
    ##           (party_get_battle_opponent, ":besieger_party", ":troop_center"),
    ##           (gt, ":besieger_party", 0),
    ##           (assign, ":is_under_siege", 1),
    ##         (try_end),
    ##
    ##         (eq, ":is_under_siege", 0),# Omit ladies in centers under siege
    ##
    ##         (try_begin),
    ##           (store_random_in_range, ":random_num",0, 100),
    ##           (lt, ":random_num", 20),
    ##           (store_troop_faction, ":cur_faction", ":troop_no"),
    ##           (call_script, "script_cf_select_random_town_with_faction", ":cur_faction"),#Can fail
    ##           (troop_set_slot, ":troop_no", slot_troop_cur_center, reg0),
    ##         (try_end),
    ##
    ##         (store_random_in_range, ":random_num",0, 100),
    ##         (lt, ":random_num", 50),
    ##         (troop_get_slot, ":lord_no", ":troop_no", slot_troop_father),
    ##         (try_begin),
    ##           (eq, ":lord_no", 0),
    ##           (troop_get_slot, ":lord_no", ":troop_no", slot_troop_spouse),
    ##         (try_end),
    ##         (gt, ":lord_no", 0),
    ##         (troop_get_slot, ":cur_party", ":lord_no", slot_troop_leaded_party),
    ##         (gt, ":cur_party", 0),
    ##         (party_get_attached_to, ":cur_center", ":cur_party"),
    ##         (gt, ":cur_center", 0),
    ##
    ##         (troop_set_slot, ":troop_no", slot_troop_cur_center, ":cur_center"),
    ##       (try_end),
    ##    ]),
    
    
    #STrig 50
    # Attach Lord Parties to the town they are in
    (0.1,
      [
        (try_for_range, ":troop_no", heroes_begin, heroes_end),
          (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
          (troop_get_slot, ":troop_party_no", ":troop_no", slot_troop_leaded_party),
          (ge, ":troop_party_no", 1),
          (party_is_active, ":troop_party_no"),
          
          (party_get_attached_to, ":cur_attached_town", ":troop_party_no"),
          (lt, ":cur_attached_town", 1),
          (party_get_cur_town, ":destination", ":troop_party_no"),
          (is_between, ":destination", centers_begin, centers_end),
          (call_script, "script_get_relation_between_parties", ":destination", ":troop_party_no"),
          (try_begin),
            (ge, reg0, 0),
            (party_attach_to_party, ":troop_party_no", ":destination"),
          (else_try),
            (party_set_ai_behavior, ":troop_party_no", ai_bhvr_hold),
          (try_end),
          
          (try_begin),
            (this_or_next|party_slot_eq, ":destination", slot_party_type, spt_town),
            (party_slot_eq, ":destination", slot_party_type, spt_castle),
            (store_faction_of_party, ":troop_faction_no", ":troop_party_no"),
            (store_faction_of_party, ":destination_faction_no", ":destination"),
            (eq, ":troop_faction_no", ":destination_faction_no"),
            (party_get_num_prisoner_stacks, ":num_stacks", ":troop_party_no"),
            (gt, ":num_stacks", 0),
            (assign, "$g_move_heroes", 1),
            (call_script, "script_party_prisoners_add_party_prisoners", ":destination", ":troop_party_no"),#Moving prisoners to the center
            (assign, "$g_move_heroes", 1),
            (call_script, "script_party_remove_all_prisoners", ":troop_party_no"),
          (try_end),
        (try_end),
        
        (try_for_parties, ":bandit_camp"),
          (gt, ":bandit_camp", "p_spawn_points_end"),
          #Can't have party is active here, because it will fail for inactive parties
          (party_get_template_id, ":template", ":bandit_camp"),
          # (is_between, ":template", "pt_steppe_bandit_lair", "pt_bandit_lair_templates_end"), ##CC fix - Caba Fix chief
          (this_or_next|eq, ":template", "pt_slave_hideout"),	#for VC-1883
          (is_between, ":template", "pt_steppe_bandit_lair", "pt_looter_lair"),  #only instances of pt_looter_lair in VC are invalid
          
          (store_distance_to_party_from_party, ":distance", "p_main_party", ":bandit_camp"),
          (lt, ":distance", 6),
          (party_set_flags, ":bandit_camp", pf_disabled, 0),
          (party_set_flags, ":bandit_camp", pf_always_visible, 1),
          
          #VC-1883 Removing old hideouts:
          (try_begin),
            (eq, ":template", "pt_slave_hideout"),
            (this_or_next|neg|check_quest_active, "qst_blank_quest_7"),
            (neg|quest_slot_eq, "qst_blank_quest_7", slot_quest_target_party, ":bandit_camp"),
            (remove_party, ":bandit_camp"),
          (try_end),
          
        (try_end),
    ]),
    
    # Check escape chances of hero prisoners. MOTO chief call more frequently with less chances.
    
    (10,
      [
        (assign, ":troop_no", "trp_player"),
        (store_skill_level, ":skill", "skl_prisoner_management", ":troop_no"),
        (assign, ":ratio_chance", 20),
        (val_sub, ":ratio_chance", ":skill"),
        
        (try_begin), #not on water
          (party_slot_eq, "p_main_party", slot_party_on_water, 0), #player on land.
          (call_script, "script_randomly_make_prisoner_heroes_escape_from_party", "p_main_party", ":ratio_chance"),
        (try_end),
        
        (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
          ##         (party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
          (assign, ":chance", 8),
          (try_begin),
            (party_slot_eq, ":center_no", slot_center_has_prisoner_tower, 1),
            (assign, ":chance", 2),
          (try_end),
          (call_script, "script_randomly_make_prisoner_heroes_escape_from_party", ":center_no", ":chance"),
        (try_end),
    ]),
    
    # Asking the ownership of captured centers to the player
    #  (3,
    #   [
    #    (assign, "$g_center_taken_by_player_faction", -1),
    #    (try_for_range, ":center_no", centers_begin, centers_end),
    #      (eq, "$g_center_taken_by_player_faction", -1),
    #      (store_faction_of_party, ":center_faction", ":center_no"),
    #      (eq, ":center_faction", "fac_player_supporters_faction"),
    #      (this_or_next|party_slot_eq, ":center_no", slot_town_lord, stl_reserved_for_player),
    #      (this_or_next|party_slot_eq, ":center_no", slot_town_lord, stl_unassigned),
    #      (party_slot_eq, ":center_no", slot_town_lord, stl_rejected_by_player),
    #      (assign, "$g_center_taken_by_player_faction", ":center_no"),
    #    (try_end),
    #    (faction_get_slot, ":leader", "fac_player_supporters_faction", slot_faction_leader),
    
    #	(try_begin),
    #		(ge, "$g_center_taken_by_player_faction", 0),
    
    #		(eq, "$cheat_mode", 1),
    #		(str_store_party_name, s14, "$g_center_taken_by_player_faction"),
    #		(display_message, "@{!}{s14} should be assigned to lord"),
    #	(try_end),
    
    #    ]),
    
    
    # Respawn hero party after kingdom hero is released from captivity. every 48 hours ON AVERAGE (52)
    (.27,
      [
        (store_random_in_range, ":troop_no", active_npcs_begin, active_npcs_end),
        (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
        
        # (str_store_troop_name, s1, ":troop_no"),
        
        (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
        
        (store_troop_faction, ":cur_faction", ":troop_no"),

        #case defeated factions
        (try_begin),
          (is_between, ":cur_faction", kingdoms_begin, kingdoms_end),
          (neg|faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
          (try_begin),
            (is_between, ":troop_no", kings_begin, kings_end),
            (troop_set_slot, ":troop_no", slot_troop_change_to_faction, "fac_adventurers"), #keep kings around in case faction is restored
          (else_try),
            (call_script, "script_lord_find_alternative_faction", ":troop_no", 1),
            (gt, reg0, -1),
            (troop_set_slot, ":troop_no", slot_troop_change_to_faction, reg0),
          (else_try), #VC-3908 case for when no other factions exist
            (troop_set_slot, ":troop_no", slot_troop_change_to_faction, "fac_outlaws"),
          (try_end),
          
          (assign, ":cur_faction", "fac_outlaws"),  #flag to not spawn a party yet
        (try_end),
        
        (troop_slot_eq, ":troop_no", slot_troop_change_to_faction, 0),  #not in midst of changing faction?
        (neq, ":cur_faction", "fac_outlaws"),
        (neg|troop_slot_ge, ":troop_no", slot_troop_leaded_party, 1),  #no hero party?
        
        (try_begin),
          (this_or_next|eq, ":cur_faction", "fac_adventurers"),
          (eq, ":cur_faction", "fac_commoners"),    #VC-3908 retain deprecated system to keep save games valid
          (troop_get_slot, ":center", ":troop_no", slot_troop_home),
          (set_spawn_radius, 15),
          (spawn_around_party,":center","pt_adv_party"),
          (assign, ":party_no", reg(0)),
          (party_set_faction, ":party_no", "fac_adventurers"),
          (troop_set_faction, ":troop_no", "fac_adventurers"),
          (troop_set_slot, ":troop_no", slot_troop_leaded_party, ":party_no"),
          (party_set_slot, ":party_no", slot_party_type, spt_kingdom_hero_party),
          (troop_set_slot, ":troop_no", slot_troop_prisoner_of_party, -1),
          (party_add_leader, ":party_no", ":troop_no"),
          (party_set_ai_behavior, ":party_no", ai_bhvr_hold),
          (str_store_troop_name, s40, ":troop_no"),
          (troop_set_health, ":troop_no", 100),
          (party_set_name, ":party_no", s40),
          (troop_equip_items, ":troop_no"),
          #			(display_message, "@{s1} respawned", color_hero_news),
          
        (else_try),
          (try_begin),
            (eq, "$cheat_mode", 2),
            (str_store_troop_name, s4, ":troop_no"),
            (display_message, "str_debug__attempting_to_spawn_s4"),
          (try_end),
          
          (call_script, "script_cf_select_random_walled_center_with_faction_and_owner_priority_no_siege", ":cur_faction", ":troop_no"),#Can fail
          (assign, ":center_no", reg0),
          
          (try_begin),
            (eq, "$cheat_mode", 2),
            (str_store_party_name, s7, ":center_no"),
            (str_store_troop_name, s0, ":troop_no"),
            (display_message, "str_debug__s0_is_spawning_around_party__s7"),
          (try_end),
          
          (call_script, "script_create_kingdom_hero_party", ":troop_no", ":center_no"),
          
          # Reequip lords after robbery
          (try_begin),
            (assign, ":melee", 0),
            (assign, ":spear", 0),
            (assign, ":thrown", 0),
            (assign, ":shield", 0),
            (assign, ":body", 0),
            (assign, ":head", 0),
            (try_for_range, ":slot", ek_item_0,num_equipment_kinds),
              (troop_get_inventory_slot, ":slot_item", ":troop_no", ":slot"),
              (gt, ":slot_item", 0),
              (item_get_type, ":item_type", ":slot_item"),
              (try_begin),
                (eq, ":item_type", itp_type_polearm),
                (val_add, ":spear", 1),
              (else_try),
                (eq, ":item_type", itp_type_thrown),
                (val_add, ":thrown", 1),
              (else_try),
                (this_or_next|eq, ":item_type", itp_type_one_handed_wpn),
                (eq, ":item_type", itp_type_two_handed_wpn),
                #					(neg|is_between, ":slot_item", "itm_knife", "itm_longseax1"),
                (neg|is_between, ":slot_item", "itm_knife", "itm_ragnar_seax"),
                (val_add, ":melee", 1),
              (else_try),
                (eq, ":item_type",itp_type_head_armor),
                (neq, ":slot_item", "itm_crown1"),
                (val_add, ":head", 1),
              (else_try),
                (eq, ":item_type", itp_type_body_armor),
                (item_get_body_armor, ":armor", ":slot_item"),
                (ge, ":armor", 25),
                (val_add, ":body", 1),
              (else_try),
                (eq, ":item_type", itp_type_shield),
                (val_add, ":shield", 1),
              (try_end),
            (try_end),
            (try_begin),
              (eq, ":body", 0),
              (store_random_in_range, ":equip", "itm_byrnie", "itm_orm_byrnie"),
              (troop_add_item, ":troop_no", ":equip"),
            (try_end),
            (try_begin),
              (eq, ":head", 0),
              (troop_get_slot, ":religion",":troop_no", slot_troop_religion),
              (try_begin),
                (eq, ":religion", 1),
                (store_random_in_range, ":equip", "itm_spangenhelm_5", "itm_vikingold_helm"),
              (else_try),
                (store_random_in_range, ":equip", "itm_vikingold_helm3", "itm_angle_helmet1"),
              (try_end),
              (troop_add_item, ":troop_no", ":equip"),
            (try_end),
            (try_begin),
              (eq, ":melee",0),
              (try_begin),
                (is_between, ":cur_faction", "fac_kingdom_14", "fac_kingdoms_end"),
                (store_random_in_range, ":equip", "itm_irish_long_sword1", "itm_widow_maker"),
              (else_try),
                (is_between, ":cur_faction", "fac_kingdom_9", "fac_kingdom_14"),
                (store_random_in_range, ":equip", "itm_noble_sword_7", "itm_irish_long_sword1"),
              (else_try),
                (store_random_in_range, ":equip", "itm_noble_sword", "itm_old_swordv"),
              (try_end),
              (troop_add_item, ":troop_no", ":equip"),
            (try_end),
            (try_begin),
              (eq, ":thrown", 0),
              (try_begin),
                (is_between, ":cur_faction", "fac_kingdom_14", "fac_kingdoms_end"),
                (assign, ":equip", "itm_javelin_skirmishesel"),
              (else_try),
                (is_between, ":cur_faction", "fac_kingdom_9", "fac_kingdom_14"),
                (assign, ":equip", "itm_javelin_skirmishes",),
              (else_try),
                (assign, ":equip", "itm_throwing_spears"),
              (try_end),
              (troop_add_item, ":troop_no", ":equip"),
            (try_end),
            (try_begin),
              (eq, ":shield", 0),
              (store_random_in_range, ":rand", 0,15),
              (try_begin),
                (lt, ":rand", 3),
                (assign, ":equip","itm_tab_shield_round_02_device"),
              (else_try),
                (lt, ":rand", 6),
                (assign, ":equip","itm_tab_shield_round_03_device"),
              (else_try),
                (lt, ":rand", 9),
                (assign, ":equip","itm_tab_shield_round_04_device"),
              (else_try),
                (lt, ":rand", 12),
                (assign, ":equip","itm_tab_shield_round_05_device"),
              (else_try),
                (assign, ":equip","itm_tab_shield_round_06_device"),
              (try_end),
              (troop_add_item, ":troop_no", ":equip"),
            (try_end),
            (try_begin),
              (eq, ":spear",0),
              (store_random_in_range, ":equip","itm_heavy_spear3","itm_new_mace"),
              (troop_add_item, ":troop_no", ":equip"),
            (try_end),
            (troop_equip_items, ":troop_no"),
          (try_end),
          #End reequipment
          
          (try_begin),
            (eq, "$g_there_is_no_avaliable_centers", 0),
            (party_attach_to_party, "$pout_party", ":center_no"),
          (try_end),
          
          #new
          #(troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
          #(call_script, "script_npc_decision_checklist_party_ai", ":troop_no"), #This handles AI for both marshal and other parties
          #(call_script, "script_party_set_ai_state", ":party_no", reg0, reg1),
          #new end
          
          (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
          (call_script, "script_party_set_ai_state", ":party_no", spai_holding_center, ":center_no"),
        (try_end),
    ]),
    
    # Spawn merchant caravan parties
    ##  (3,
    ##   [
    ##       (try_for_range, ":troop_no", merchants_begin, merchants_end),
    ##         (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_merchant),
    ##         (troop_slot_eq, ":troop_no", slot_troop_is_prisoner, 0),
    ##         (neg|troop_slot_ge, ":troop_no", slot_troop_leaded_party, 1),
    ##
    ##         (call_script, "script_cf_create_merchant_party", ":troop_no"),
    ##       (try_end),
    ##    ]),
    
    # Spawn village farmer parties
    # A bit more probabilistic JuJu70
    (0.48, #chief pone 48 horas a spawn de campesinos en vez de 24 MOTO lengthen to 72 after removing 60% randomization
      [(try_begin),
          (store_random_in_range, ":village_no", villages_begin, villages_end),
          (party_slot_eq, ":village_no", slot_village_state, svs_normal),
          (party_get_slot, ":farmer_party", ":village_no", slot_village_farmer_party),
          (this_or_next|eq, ":farmer_party", 0),
          (neg|party_is_active, ":farmer_party"),
          # (store_random_in_range, ":random_no", 0, 100), obviously don't still need randomization
          # (lt, ":random_no", 60),
          (call_script, "script_create_village_farmer_party", ":village_no"),
          (party_set_slot, ":village_no", slot_village_farmer_party, reg0),
        (try_end),
        # Christian priests
        (try_begin),
          (store_random_in_range, ":monastery", "p_monasterio1", "p_yourlair"),
          (store_random_in_range, ":monastery1", "p_monasterio1", "p_yourlair"),
          (neq, ":monastery", ":monastery1"),
          (party_slot_eq, ":monastery", slot_party_looted_left_days, 0),
          (party_slot_eq, ":monastery1", slot_party_looted_left_days, 0),
          (store_random_in_range, ":random_no", 0, 100),
          (lt, ":random_no", 9),
          (set_spawn_radius, 0),
          (spawn_around_party, ":monastery", "pt_sacerdotes_party"),
          (assign, ":new_party", reg0),
          (party_set_slot, ":new_party", slot_party_ai_object, ":monastery1"),
          (party_set_ai_behavior, ":new_party", ai_bhvr_travel_to_party),
          (party_set_ai_object, ":new_party", ":monastery1"),
          (party_set_flags, ":new_party", pf_default_behavior, 0),
          #		(str_store_party_name, s33, ":monastery"),
          #		(str_store_party_name, s34, ":monastery1"),
          #		(display_message, "@Spawned priests traveling from {s33} to {s34}"),
          #         (str_store_party_name, s1, ":village_no"),
          #         (display_message, "@Village farmers created at {s1}."),
        (try_end),
        (try_for_parties, ":party_no"),
          (party_get_template_id, ":party_template", ":party_no"),
          (eq, ":party_template", "pt_sacerdotes_party"),
          (get_party_ai_object,":target",":party_no"),
          (is_between, ":target", "p_monasterio1", "p_yourlair"),
          #		(str_store_party_name, s33, ":target"),
          (party_is_in_town, ":party_no", ":target"),
          (remove_party, ":party_no"),
          #		(display_message, "@Removing party in {s33}"),
        (try_end),
    ]),
    
    
    (72,
      [# Cows in inventory give food items
        (try_begin),
          (assign, ":cont", 0),
          (assign, ":cont1", 0),
          (assign, ":space", 0),
          (store_free_inventory_capacity, ":space", "trp_player"),
          (gt, ":space", 0),
          (store_item_kind_count, ":cont", "itm_cow1"),
          (store_item_kind_count, ":cont1", "itm_cow2"),
          (val_add, ":cont", ":cont1"),
          (ge, ":cont", 1),
          (store_random_in_range, ":rand", 0, 100),
          (lt, ":rand", 50),
          (troop_add_item,"trp_player","itm_butter"),
          (display_message, "@Your men made some delicious butter from cow's milk.", color_good_news),
        (try_end),
        # Updating trade good prices according to the productions
        (call_script, "script_update_trade_good_prices"),
        # Updating player odds
        (try_for_range, ":cur_center", centers_begin, centers_end),
          (party_get_slot, ":player_odds", ":cur_center", slot_town_player_odds),
          (try_begin),
            (gt, ":player_odds", 1000),
            (val_mul, ":player_odds", 95),
            (val_div, ":player_odds", 100),
            (val_max, ":player_odds", 1000),
          (else_try),
            (lt, ":player_odds", 1000),
            (val_mul, ":player_odds", 105),
            (val_div, ":player_odds", 100),
            (val_min, ":player_odds", 1000),
          (try_end),
          (party_set_slot, ":cur_center", slot_town_player_odds, ":player_odds"),
        (try_end),
        #Farmstead cattle
        (store_random_in_range, ":farm", "p_farmsteadsp1", "p_hadrian_wall1"),
        (party_get_slot, ":num_cattle", ":farm", slot_center_head_cattle),
        (party_get_slot, ":num_pcattle", ":farm", slot_center_player_cattle),
        (store_add, ":total_cattle", ":num_cattle",":num_pcattle"),
        (store_random_in_range, ":random_no", 0, 100),
        (assign, ":minimum_distance", 100),
        (assign, ":closest_town", -1),
        (try_for_range, ":town_no", centers_begin, centers_end),
          (store_distance_to_party_from_party, ":dist", ":farm",":town_no"),
          (lt, ":dist", ":minimum_distance"),
          (assign, ":minimum_distance", ":dist"),
          (assign, ":closest_town", ":town_no"),
        (try_end),
        (str_store_party_name_link, s4, ":closest_town"),
        (try_begin), #Disaster
          (le, ":random_no", 5),#5% chance of epidemic - should happen once every two years It was more common in Dark Ages
          (val_min, ":num_cattle", 10),
          (val_min, ":num_pcattle", 15),
          (party_get_slot, reg4, ":farm", slot_center_head_cattle),
          (party_get_slot, reg5, ":farm", slot_center_player_cattle),
          (val_sub, reg4, ":num_cattle"),
          (val_sub, reg5, ":num_pcattle"),
          (try_begin),
            (eq, reg4, 0),
            (eq, reg5, 0),
          (else_try),
            (eq, reg4, 0),
            (gt, reg5, 0),
            (display_log_message, "@A livestock epidemic has killed {reg5} of your cattle at a farmstead near {s4}."),
          (else_try),
            (gt, reg4, 0),
            (eq, reg5, 0),
          (else_try),
            (display_log_message, "@A livestock epidemic has killed {reg4} cattle and {reg5} of your cattle at a farmstead near {s4}."),
          (try_end),
        (else_try), #Overgrazing
          (gt, ":total_cattle", 500),
          (val_mul, ":num_cattle", 90), #10% decrease at number of cattles
          (val_div, ":num_cattle", 100),
          (try_begin),
            (gt, ":num_pcattle",30),
            (val_mul, ":num_pcattle", 90), #10% decrease at number of sheeps
            (val_div, ":num_pcattle", 100),
          (try_end),
        (else_try), #superb grazing
          (lt, ":total_cattle", 200),
          (val_mul, ":num_cattle", 120), #20% increase at number of cattles
          (val_div, ":num_cattle", 100),
          (val_add, ":num_cattle", 1),
          (try_begin),
            (gt, ":num_pcattle", 30),
            (val_mul, ":num_pcattle", 120), #20% increase at number of sheeps
            (val_div, ":num_pcattle", 100),
          (try_end),
        (else_try), #very good grazing
          (lt, ":total_cattle", 300),
          (val_mul, ":num_cattle", 110), #10% increase at number of cattles
          (val_div, ":num_cattle", 100),
          (val_add, ":num_cattle", 1),
          (try_begin),
            (gt, ":num_pcattle", 30),
            (val_mul, ":num_pcattle", 110), #10% increase at number of sheeps
            (val_div, ":num_pcattle", 100),
          (try_end),
        (else_try), #good grazing
          (lt, ":total_cattle", 400),
          (lt, ":random_no", 50),
          (val_mul, ":num_cattle", 105), #5% increase at number of cattles
          (val_div, ":num_cattle", 100),
          (try_begin),
            (gt, ":num_pcattle", 30),
            (val_mul, ":num_pcattle", 105), #5% increase at number of cattles
            (val_div, ":num_pcattle", 100),
          (try_end),
        (try_end),
        
        (party_set_slot, ":farm", slot_center_head_cattle, ":num_cattle"),
        (party_set_slot, ":farm", slot_center_player_cattle, ":num_pcattle"),
    ]),
    
    
    #Troop AI: Merchants thinking
    (8,
      [
        (try_for_parties, ":party_no"),
          (party_slot_eq, ":party_no", slot_party_type, spt_kingdom_caravan),
          (party_is_in_any_town, ":party_no"),
          
          (store_faction_of_party, ":merchant_faction", ":party_no"),
          (faction_get_slot, ":num_towns", ":merchant_faction", slot_faction_num_towns),
          (try_begin),
            (le, ":num_towns", 0),
            (remove_party, ":party_no"),
          (else_try),
            (party_get_cur_town, ":cur_center", ":party_no"),
            
            (store_random_in_range, ":random_no", 0, 100),
            
            (try_begin),
              (party_slot_eq, ":cur_center", slot_town_lord, "trp_player"),
              
              (options_get_campaign_ai, ":reduce_campaign_ai"), #moto chief
              (try_begin),
                (eq, ":reduce_campaign_ai", 0), #hard (less money from tariffs)
                (assign, ":tariff_succeed_limit", 35),
              (else_try),
                (eq, ":reduce_campaign_ai", 1), #medium (normal money from tariffs)
                (assign, ":tariff_succeed_limit", 45),
              (else_try),
                (eq, ":reduce_campaign_ai", 2), #easy (more money from tariffs)
                (assign, ":tariff_succeed_limit", 60),
              (try_end),
            (else_try),
              (assign, ":tariff_succeed_limit", 45),
            (try_end),
            
            (lt, ":random_no", ":tariff_succeed_limit"),
            
            (assign, ":can_leave", 1),
            (try_begin),
              (is_between, ":cur_center", walled_centers_begin, walled_centers_end),
              (neg|party_slot_eq, ":cur_center", slot_center_is_besieged_by, -1),
              (assign, ":can_leave", 0),
            (try_end),
            (eq, ":can_leave", 1),
            
            (assign, ":do_trade", 0),
            (try_begin),
              (party_get_slot, ":cur_ai_state", ":party_no", slot_party_ai_state),
              (eq, ":cur_ai_state", spai_trading_with_town),
              (party_get_slot, ":cur_ai_object", ":party_no", slot_party_ai_object),
              (eq, ":cur_center", ":cur_ai_object"),
              (assign, ":do_trade", 1),
            (try_end),
            
            (assign, ":target_center", -1),
            
            (try_begin), #Make sure escorted caravan continues to its original destination.
              (eq, "$caravan_escort_party_id", ":party_no"),
              (neg|party_is_in_town, ":party_no", "$caravan_escort_destination_town"),
              (assign, ":target_center", "$caravan_escort_destination_town"),
            (else_try),
              (call_script, "script_cf_select_most_profitable_town_at_peace_with_faction_in_trade_route", ":cur_center", ":merchant_faction"),
              (assign, ":target_center", reg0),
            (try_end),
            (is_between, ":target_center", towns_begin, towns_end),
            (neg|party_is_in_town, ":party_no", ":target_center"),
            
            (try_begin),
              (eq, ":do_trade", 1),
              (str_store_party_name, s7, ":cur_center"),
              (call_script, "script_do_merchant_town_trade", ":party_no", ":cur_center"),
            (try_end),
            (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
            (party_set_ai_object, ":party_no", ":target_center"),
            (party_set_flags, ":party_no", pf_default_behavior, 0),
            (party_set_slot, ":party_no", slot_party_ai_state, spai_trading_with_town),
            (party_set_slot, ":party_no", slot_party_ai_object, ":target_center"),
          (try_end),
        (try_end),
    ]),
    
    #Troop AI: Village farmers thinking
    # (8,	#MOTO chief randomize activity; change from 8-hour to random 1-hour #idibil back to 8. Moto if it is each hour Towns have always max food, no?
    (.05,	#check every village's farmer party every 5.5 hours ON AVERAGE (twice during working hours)
      # (5.5,	#check every village's farmer party every 5.5 hours ON AVERAGE (twice during working hours) for ICM testing
      [
        #MOTO farmers start out early in day
        (store_time_of_day, ":oclock"),
        (is_between, ":oclock", 4, 17),
        #MOTO farmers start out early in day end
        
        (store_random_in_range, ":home_center", villages_begin, villages_end),
        # (try_for_range, ":home_center", villages_begin, villages_end),	#for testing
        (party_get_slot, ":party_no", ":home_center", slot_village_farmer_party),
        (gt, ":party_no", 0),
        (party_is_active, ":party_no"),
        (party_is_in_any_town, ":party_no"),
        (party_get_cur_town, ":cur_center", ":party_no"),
        (assign, ":can_leave", 1),
        (try_begin),
          (is_between, ":cur_center", walled_centers_begin, walled_centers_end),
          #siege warfare chief cambia #no villagers in siege
          (this_or_next|party_slot_ge, ":cur_center", slot_center_blockaded, 2),    #center blockaded (by player) OR
          (party_slot_ge, ":cur_center", slot_center_is_besieged_by, 1), #center besieged by someone else
          #siege warfare
          (neg|party_slot_eq, ":cur_center", slot_center_is_besieged_by, -1),
          (assign, ":can_leave", 0),
        (try_end),
        (eq, ":can_leave", 1),
        
        (try_begin),
          (neg|party_slot_eq, ":cur_center", slot_party_type, spt_castle),	#gets overwritten by script_calculate_castle_prosperities_by_using_its_villages
          (try_begin),
            (party_slot_eq, ":cur_center", slot_party_type, spt_town),
            (assign, ":chance", 35),	#going for average 50
          (else_try),
            (assign, ":chance", 100),	#going for average 45; villages get beat up a lot
          (try_end),
          (store_random_in_range, ":rand", 0, 100),
          (lt, ":rand", ":chance"), #was 35
          (call_script, "script_change_center_prosperity", ":cur_center", 1),
          (val_add, "$newglob_total_prosperity_from_village_trade", 1),
        (try_end),
        
        (try_begin),
          (eq, ":cur_center", ":home_center"),
          
          #Peasants trade in their home center
          (call_script, "script_do_party_center_trade", ":party_no", ":home_center", 3), #this needs to be the same as the center
          (store_faction_of_party, ":center_faction", ":cur_center"),
          (party_set_faction, ":party_no", ":center_faction"),
          (party_get_slot, ":market_town", ":home_center", slot_village_market_town),
          (party_set_slot, ":party_no", slot_party_ai_object, ":market_town"),
          (party_set_slot, ":party_no", slot_party_ai_state, spai_trading_with_town),
          (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
          (party_set_ai_object, ":party_no", ":market_town"),
          
          (party_get_slot, reg1, ":market_town", slot_town_farmer_visit_starts),
          (val_add, reg1, 1),
          (party_set_slot, ":market_town", slot_town_farmer_visit_starts, reg1),
          
        (else_try),
          (try_begin),
            (party_get_slot, ":cur_ai_object", ":party_no", slot_party_ai_object),
            (eq, ":cur_center", ":cur_ai_object"),
            (call_script, "script_do_party_center_trade", ":party_no", ":cur_ai_object", 3), #raised from 10
            (assign, ":total_change", reg0),
            #This is roughly 50% of what a caravan would pay
            
            #Adding tariffs to the town
            (party_get_slot, ":accumulated_tariffs", ":cur_ai_object", slot_center_accumulated_tariffs),
            (party_get_slot, ":prosperity", ":cur_ai_object", slot_town_prosperity),
            
            (assign, ":tariffs_generated", ":total_change"),
            (val_mul, ":tariffs_generated", ":prosperity"),
            (val_div, ":tariffs_generated", 100),
            (val_div, ":tariffs_generated", 20), #10 for caravans, 20 for villages
            (val_add, ":accumulated_tariffs", ":tariffs_generated"),
            
            #			(try_begin), #no tariffs for infested villages
            #				(party_slot_ge, ":cur_ai_object", slot_village_infested_by_bandits, 1),
            #				(assign,":accumulated_tariffs", 0),
            #			(try_end),
            
            (try_begin),
              (ge, "$cheat_mode", 3),
              (assign, reg4, ":tariffs_generated"),
              (str_store_party_name, s4, ":cur_ai_object"),
              (assign, reg5, ":accumulated_tariffs"),
              (display_message, "@{!}New tariffs at {s4} = {reg4}, total = {reg5}"),
            (try_end),
            
            (party_set_slot, ":cur_ai_object", slot_center_accumulated_tariffs, ":accumulated_tariffs"),
            
            #Increasing food stocks of the town
            (party_get_slot, ":town_food_store", ":cur_ai_object", slot_party_food_store),
            (call_script, "script_center_get_food_store_limit", ":cur_ai_object"),
            (assign, ":food_store_limit", reg0),
            
            (party_get_slot, reg1, ":cur_ai_object", slot_town_farmer_visits),
            (val_add, reg1, 1),
            (party_set_slot, ":cur_ai_object", slot_town_farmer_visits, reg1),
            
            (party_get_slot, reg1, ":home_center", slot_town_prosperity),
            # (val_mul, reg1, 4),
            # (val_div, reg1, 5),
            (val_add, reg1, 267),	#267-367
            (val_add, ":town_food_store", reg1),  #2 farmer visit per 3 days, 2 villages per town, x4/3 by experience
            (val_min, ":town_food_store", ":food_store_limit"),
            (party_set_slot, ":cur_ai_object", slot_party_food_store, ":town_food_store"),
            
            # #Adding 1 to village prosperity DO THIS for other centers as well (below)
            # (try_begin),
            # (store_random_in_range, ":rand", 0, 100),
            # (lt, ":rand", 10), #was 35
            # (call_script, "script_change_center_prosperity", ":home_center", 1),
            # (val_add, "$newglob_total_prosperity_from_village_trade", 1),
            # (try_end),
          (try_end),
          
          #Moving farmers to their home village
          (party_set_slot, ":party_no", slot_party_ai_object, ":home_center"),
          (party_set_slot, ":party_no", slot_party_ai_state, spai_trading_with_town),
          (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
          (party_set_ai_object, ":party_no", ":home_center"),
          # (try_end),	#for testing
        (try_end),
    ]),
    
    #Increase castle food stores
    # JuJu70 - probabilistic
    # (0.26, #siege warfare
    # (24, #done above
    #  [
    # (store_random_in_range, ":center_no", castles_begin, castles_end),
    # (assign, ":no_works", 1),
    # (try_begin),
    # (this_or_next|party_slot_ge, ":center_no", slot_center_blockaded, 2),    #center blockaded (by player) OR
    # (party_slot_ge, ":center_no", slot_center_is_besieged_by, 1), #center besieged by someone else
    # (assign, ":no_works", 0),
    # (try_end),
    # (eq, ":no_works", 1), #no foods in sieges
    # (party_slot_eq, ":center_no", slot_center_is_besieged_by, -1), #castle is not under siege
    # (party_get_slot, ":center_food_store", ":center_no", slot_party_food_store),
    
    # (try_for_range, ":village_no", villages_begin, villages_end),
    # (party_slot_eq, ":village_no", slot_village_state, svs_normal),
    # (party_get_slot, ":bound_center", ":village_no", slot_village_bound_center),# ":center_no"??
    # (eq, ":bound_center", ":center_no"),
    # (party_get_slot, reg1, ":village_no", slot_town_prosperity),
    # # (val_add, ":center_food_store", 100),
    # (val_add, reg1, 30),
    # (try_end),
    # (val_add, ":center_food_store", reg1), #0-100 accord prosperity + 30
    # (call_script, "script_center_get_food_store_limit", ":center_no"),
    # (assign, ":food_store_limit", reg0),
    # (val_min, ":center_food_store", ":food_store_limit"),
    # (party_set_slot, ":center_no", slot_party_food_store, ":center_food_store"),
    # #       (try_end),
    #   ]),
    
    # JuJu70
    # Adventurers check and attend feasts every six days
    (4,
      [
        (store_random_in_range, ":troop_no", companions_begin, kings_end),   #VC-3907 include leaders of defeated factions
          (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
          (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
          (gt, ":party_no", 0),
          (store_troop_faction, ":faction", ":troop_no"),
          (eq, ":faction", "fac_adventurers"),
          (neg|party_slot_eq, ":party_no", slot_party_ai_state, spai_besieging_center),
          (neg|party_slot_eq, ":party_no", slot_party_ai_state, spai_engaging_army),
          (try_begin),
            (assign, ":minimum_distance", 500),
            (try_for_range,":faction_no", kingdoms_begin, kingdoms_end),
              (faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_feast),
              (faction_get_slot, ":center_to_visit", ":faction_no", slot_faction_ai_object),
              (is_between, ":center_to_visit", walled_centers_begin, walled_centers_end),
              (gt, ":center_to_visit", 0),
              (party_get_slot, ":town_lord", ":center_to_visit", slot_town_lord),
              (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":town_lord"),
              (ge, reg0, 0),
              (party_get_position, pos1, ":party_no"),
              (party_get_position, pos2, ":center_to_visit"),
              (store_distance_to_party_from_party, ":dist", ":party_no", ":center_to_visit"),
              (try_begin),
                (lt, ":dist", ":minimum_distance"),
                (assign, ":minimum_distance", ":dist"),
                (assign, ":closest_town", ":center_to_visit"),
              (try_end),
            (try_end),
            #			(str_clear, s44),
            #			(str_clear, s41),
            #			(str_store_party_name, s44, ":closest_town"),
            #			(str_store_party_name, s41, ":party_no"),
            #			(display_message, "@{s41} found a feast at {s44}"),
            (gt, ":closest_town", 0),
            (is_between, ":closest_town", walled_centers_begin, walled_centers_end),
            (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
            (party_set_ai_object, ":party_no", ":closest_town"),
            (party_set_slot, ":party_no", slot_party_ai_object, ":closest_town"),
            (party_set_slot, ":party_no", slot_party_ai_state, spai_retreating_to_center),
            (try_begin),
              (eq, ":troop_no", "$g_talk_troop"),
              (str_store_string, s14, "str_i_wish_to_attend_the_feast_there"),
              (str_store_string, s16, "str_there_is_a_feast_which_i_wish_to_attend"),
            (try_end),
          (try_end),
    ]),
    
    #cache party strengths (to avoid re-calculating)
    ##  (2,
    ##   [
    ##       (try_for_range, ":cur_troop", heroes_begin, heroes_end),
    ##         (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
    ##         (troop_get_slot, ":cur_party", ":cur_troop", slot_troop_leaded_party),
    ##         (ge, ":cur_party", 0),
    ##         (call_script, "script_party_calculate_strength", ":cur_party", 0), #will update slot_party_cached_strength
    ##       (try_end),
    ##    ]),
    ##
    ##  (6,
    ##   [
    ##       (try_for_range, ":cur_center", walled_centers_begin, walled_centers_end),
    ##         (call_script, "script_party_calculate_strength", ":cur_center", 0), #will update slot_party_cached_strength
    ##       (try_end),
    ##    ]),
    
    ##  (1,
    ##   [
    ##       (try_for_range, ":cur_center", walled_centers_begin, walled_centers_end),
    ##         (store_random_in_range, ":rand", 0, 100),
    ##         (lt, ":rand", 10),
    ##         (store_faction_of_party, ":center_faction", ":cur_center"),
    ##         (assign, ":friend_strength", 0),
    ##         (try_for_range, ":cur_troop", heroes_begin, heroes_end),
    ##           (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
    ##           (troop_get_slot, ":cur_troop_party", ":cur_troop", slot_troop_leaded_party),
    ##           (gt, ":cur_troop_party", 0),
    ##           (store_distance_to_party_from_party, ":distance", ":cur_troop_party", ":cur_center"),
    ##           (lt, ":distance", 10),
    ##           (store_troop_faction, ":army_faction", ":cur_troop"),
    ##           (store_relation, ":rel", ":army_faction", ":center_faction"),
    ##           (try_begin),
    ##             (gt, ":rel", 10),
    ##             (party_get_slot, ":str", ":cur_troop_party", slot_party_cached_strength),
    ##             (val_add, ":friend_strength", ":str"),
    ##           (try_end),
    ##         (try_end),
    ##         (party_set_slot, ":cur_center", slot_party_nearby_friend_strength, ":friend_strength"),
    ##       (try_end),
    ##    ]),
    
    # Make heroes running away from someone retreat to friendly centers
    (0.5,
      [
        (try_for_range, ":cur_troop", heroes_begin, heroes_end),
          (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
          (troop_get_slot, ":cur_party", ":cur_troop", slot_troop_leaded_party),
          (gt, ":cur_party", 0),
          (try_begin),
            (party_is_active, ":cur_party"),
            (try_begin),
              (get_party_ai_current_behavior, ":ai_bhvr", ":cur_party"),
              (eq, ":ai_bhvr", ai_bhvr_avoid_party),
              
              #Certain lord personalities will not abandon a battlefield to flee to a fortress
              (assign, ":continue", 1),
              (try_begin),
                (this_or_next|troop_slot_eq, ":cur_troop", slot_lord_reputation_type, lrep_upstanding),
                (troop_slot_eq, ":cur_troop", slot_lord_reputation_type, lrep_martial),
                (get_party_ai_current_object, ":ai_object", ":cur_party"),
                (party_is_active, ":ai_object"),
                (party_get_battle_opponent, ":battle_opponent", ":ai_object"),
                (party_is_active, ":battle_opponent"),
                (assign, ":continue", 0),
              (try_end),
              (try_begin),
                (troop_slot_eq, ":cur_troop", slot_troop_current_mission, npc_mission_improve_relations),
                (assign, ":continue", 0),
              (try_end),
              (eq, ":continue", 1),
              
              (store_faction_of_party, ":party_faction", ":cur_party"),
              (party_get_slot, ":commander_party", ":cur_party", slot_party_commander_party),
              (faction_get_slot, ":faction_marshal", ":party_faction", slot_faction_marshal),
              (neq, ":faction_marshal", ":cur_troop"),
              (assign, ":continue", 1),
              (try_begin),
                (ge, ":faction_marshal", 0),
                (troop_get_slot, ":faction_marshal_party", ":faction_marshal", slot_troop_leaded_party),
                (party_is_active, ":faction_marshal_party", 0),
                (eq, ":commander_party", ":faction_marshal_party"),
                (assign, ":continue", 0),
              (try_end),
              (eq, ":continue", 1),
              (assign, ":done", 0),
              (try_for_range, ":cur_center", walled_centers_begin, walled_centers_end),
                (eq, ":done", 0),
                (party_slot_eq, ":cur_center", slot_center_is_besieged_by, -1),
                (store_faction_of_party, ":center_faction", ":cur_center"),
                (store_relation, ":cur_relation", ":center_faction", ":party_faction"),
                (gt, ":cur_relation", 0),
                (store_distance_to_party_from_party, ":cur_distance", ":cur_party", ":cur_center"),
                (lt, ":cur_distance", 20),
                (party_get_position, pos1, ":cur_party"),
                (party_get_position, pos2, ":cur_center"),
                (neg|position_is_behind_position, pos2, pos1),
                (call_script, "script_party_set_ai_state", ":cur_party", spai_retreating_to_center, ":cur_center"),
                (assign, ":done", 1),
              (try_end),
            (try_end),
          (else_try),
            (troop_set_slot, ":cur_troop", slot_troop_leaded_party, -1),
          (try_end),
        (try_end),
    ]),
    
    # Centers give alarm if the player is around
    (0.5,
      [
        (store_current_hours, ":cur_hours"),
        (store_mod, ":cur_hours_mod", ":cur_hours", 11),
        (store_sub, ":hour_limit", ":cur_hours", 5),
        (party_get_num_companions, ":num_men", "p_main_party"),
        (party_get_num_prisoners, ":num_prisoners", "p_main_party"),
        (val_add, ":num_men", ":num_prisoners"),
        (convert_to_fixed_point, ":num_men"),
        (store_sqrt, ":num_men_effect", ":num_men"),
        (convert_from_fixed_point, ":num_men_effect"),
        (try_begin),
          (eq, ":cur_hours_mod", 0),
          #Reduce alarm by 2 in every 11 hours.
          (try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
            (faction_get_slot, ":player_alarm", ":cur_faction", slot_faction_player_alarm),
            (val_sub, ":player_alarm", 1),
            (val_max, ":player_alarm", 0),
            (faction_set_slot, ":cur_faction", slot_faction_player_alarm, ":player_alarm"),
          (try_end),
        (try_end),
        (eq, "$g_player_is_captive", 0),
        (try_for_range, ":cur_center", centers_begin, centers_end),
          (store_faction_of_party, ":cur_faction", ":cur_center"),
          (store_relation, ":reln", ":cur_faction", "fac_player_faction"),
          (lt, ":reln", 0),
          (store_distance_to_party_from_party, ":dist", "p_main_party", ":cur_center"),
          (lt, ":dist", 5),
          (store_mul, ":dist_sqr", ":dist", ":dist"),
          (store_sub, ":dist_effect", 20, ":dist_sqr"),
          (store_sub, ":reln_effect", 20, ":reln"),
          (store_mul, ":total_effect", ":dist_effect", ":reln_effect"),
          (val_mul, ":total_effect", ":num_men_effect"),
          (store_div, ":spot_chance", ":total_effect", 10),
          (store_random_in_range, ":random_spot", 0, 1000),
          (lt, ":random_spot", ":spot_chance"),
          (faction_get_slot, ":player_alarm", ":cur_faction", slot_faction_player_alarm),
          (val_add, ":player_alarm", 1),
          (val_min, ":player_alarm", 100),
          (faction_set_slot, ":cur_faction", slot_faction_player_alarm, ":player_alarm"),
          (try_begin),
            (neg|party_slot_ge, ":cur_center", slot_center_last_player_alarm_hour, ":hour_limit"),
            (str_store_party_name_link, s1, ":cur_center"),
            (display_message, "@Your party is spotted by {s1}."),
            (party_set_slot, ":cur_center", slot_center_last_player_alarm_hour, ":cur_hours"),
          (try_end),
        (try_end),
    ]),
    
    #STrig 60
    # Consuming food at every 24 hours
    # Modified by JuJu70 to include prisoners
    (12, #chief change 12 hours. In ancient and dark ages, men did two meals each day
      [
        (eq, "$g_player_is_captive", 0),
        (store_party_size, reg25, "p_main_party"),
        #   (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
        #   (assign, ":num_men", 0),
        #    (try_for_range, ":i_stack", 0, ":num_stacks"),
        #     (party_stack_get_size, ":stack_size","p_main_party",":i_stack"),
        #      (val_add, ":num_men", ":stack_size"),
        #   (try_end),
        #(val_div, ":num_men", 1), #chief change of 3 to 1. 1 men = 1 food unit eaten
        (assign, ":num_men", reg25),
        
        (val_div, ":num_men", 3), #1 piece of food let eat 3 men
        (try_begin),
          (eq, ":num_men", 0),
          (val_add, ":num_men", 1),
        (try_end),
        
        (try_begin),
          (assign, ":number_of_foods_player_has", 0),
          (try_for_range, ":cur_edible", food_begin, food_end),
            (call_script, "script_cf_player_has_item_without_modifier", ":cur_edible", imod_rotten),
            (val_add, ":number_of_foods_player_has", 1),
          (try_end),
          (try_begin),
            (ge, ":number_of_foods_player_has", 6),
            (unlock_achievement, ACHIEVEMENT_ABUNDANT_FEAST),
          (try_end),
        (try_end),
        
        (assign, ":consumption_amount", ":num_men"),
        (assign, ":no_food_displayed", 0),
        (try_for_range, ":unused", 0, ":consumption_amount"),
          (assign, ":available_food", 0),
          (try_for_range, ":cur_food", food_begin, food_end),
            (item_set_slot, ":cur_food", slot_item_is_checked, 0),
            (call_script, "script_cf_player_has_item_without_modifier", ":cur_food", imod_rotten),
            (val_add, ":available_food", 1),
          (try_end),
          (try_begin),
            (gt, ":available_food", 0),
            (store_random_in_range, ":selected_food", 0, ":available_food"),
            (call_script, "script_consume_food", ":selected_food"),
          (else_try),
            (eq, ":no_food_displayed", 0),
            (display_message, "@Your men have nothing to eat!", 0xFF0000), #moto chief
            (call_script, "script_change_player_party_morale", -8), #extreme. Men dont like to have hungry, -16 each day = 4 days without food starting desertions.
            ###player lose hit points as he has hungry
            # (get_player_agent_no, ":player_agent"),  No agents in map
            # (store_agent_hit_points, ":hit_points", ":player_agent"),
            # (try_begin),
            # (ge, ":hit_points", 30),
            # (agent_set_hit_points, ":player_agent", 20),
            # (display_message, "@Lack of food makes you feel weak, and your health suffers!", 0xFF0000),
            # (try_end),
            ####
            
            (assign, ":no_food_displayed", 1),
            #NPC companion changes begin
            (try_begin),
              (call_script, "script_party_count_fit_regulars", "p_main_party"),
              (gt, reg0, 0),
              (call_script, "script_objectionable_action", tmt_egalitarian, "str_men_hungry"),
            (try_end),
            #NPC companion changes end
          (try_end),
        (try_end),
    ]),
    
    
    # Setting item modifiers for food
    (24,
      [
        (troop_get_inventory_capacity, ":inv_size", "trp_player"),
        (try_for_range, ":i_slot", 0, ":inv_size"),
          (troop_get_inventory_slot, ":item_id", "trp_player", ":i_slot"),
          (this_or_next|eq, ":item_id", "itm_cattle_meat"),
          (this_or_next|eq, ":item_id", "itm_chicken"),
          (eq, ":item_id", "itm_pork"),
          
          (troop_get_inventory_slot_modifier, ":modifier", "trp_player", ":i_slot"),
          (try_begin),
            (ge, ":modifier", imod_fresh),
            (lt, ":modifier", imod_rotten),
            (val_add, ":modifier", 1),
            (troop_set_inventory_slot_modifier, "trp_player", ":i_slot", ":modifier"),
          (else_try),
            (lt, ":modifier", imod_fresh),
            (troop_set_inventory_slot_modifier, "trp_player", ":i_slot", imod_fresh),
          (try_end),
        (try_end),
    ]),
    
    ##  # Assigning lords to centers with no leaders
    ##  (72,
    ##   [
    ##   #(call_script, "script_assign_lords_to_empty_centers"),
    ##    ]),
    
    # Updating player icon in every frame
    (0,
      [  (troop_get_inventory_slot, ":cur_horse", "trp_player", 8), #horse slot
        (assign, ":new_icon", -1),
        (try_begin),
          (eq, "$g_player_icon_state", pis_normal),
          # (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
          # (assign, ":num_men", 0),
          # (try_for_range, ":i_stack", 0, ":num_stacks"),
          # (party_stack_get_size, ":stack_size","p_main_party",":i_stack"),
          # (val_add, ":num_men", ":stack_size"),
          # (try_end),
          # (party_get_num_companions, ":num_men", "p_main_party"),
          # (assign, ":party_size", ":num_men"),
          (store_party_size_wo_prisoners, ":party_size", "p_main_party"),
          (try_begin),
            (ge, ":cur_horse", 0),
            (try_begin),
              (eq,"$followers_on",1),
              (gt, ":party_size", 290),
              (assign, ":new_icon", "icon_player_horseman_followers"),
            (else_try),
              (gt, ":party_size", 100),
              (assign, ":new_icon", "icon_player_horseman_withtroops"),
            (else_try),
              (assign, ":new_icon", "icon_player_horseman"),
            (try_end),
          (else_try),
            (eq,"$followers_on",1),
            (gt, ":party_size", 290),
            (assign, ":new_icon", "icon_player_troops_followers"),
          (else_try),
            (ge, ":party_size", 100), #
            (assign, ":new_icon", "icon_player_withtroops"),
          (else_try),
            (assign, ":new_icon", "icon_player"),
          (try_end),
          
          # (try_begin),
          # (eq,"$followers_on",1), #on followers camp icon system chief
          # (ge, ":num_men", 290), #
          # (assign, ":new_icon", "icon_player_troops_followers"),
          
          # (else_try),
          # (ge, ":cur_horse", 0),
          # (assign, ":new_icon", "icon_player_horseman"),
          
          ##      (else_try), #chief para items, 1 item determina icono de player. Iconos
          ##	    (try_begin),
          ##		   (troop_has_item_equipped, "trp_player", "itm_robe"),
          ##           (assign, ":new_icon", "icon_monje"),
          ##		(else_try),
          ##           (troop_has_item_equipped, "trp_player", "itm_mail"),
          ##           (assign, ":new_icon", "icon_warrior"),
          
          
          
          #############
        (else_try),
          (eq, "$g_player_icon_state", pis_camping),
          #motomataru chief fix camping on water chief
          # (assign, ":new_icon", "icon_camp_basic"), #chief cambiado
          # (party_get_current_terrain,":terrain","p_main_party"),
          (try_begin),
            # (neq, ":terrain", 0),	#not rt_water
            # (neq, ":terrain", 7),	#not rt_bridge used as water terrain
            # (neq, ":terrain", 8),	#not rt_bridge used as water terrain
            (party_slot_eq, "p_main_party", slot_party_on_water, 0),
            (try_begin),
              (eq, "$fortified_camp", 1),
              (assign, ":new_icon", "icon_camp_fortified"), #fortified camps
            (else_try),
              (assign, ":new_icon", "icon_camp"),
            (try_end),
          (else_try),
            (assign, ":new_icon", "icon_ship_on_land"),
          (try_end),
          #end motomataru fix camping on water
        (else_try),
          (eq, "$g_player_icon_state", pis_ship),
          (try_begin),
            (party_slot_ge, "p_main_party", slot_party_7_ship_type, 1),
            (assign, ":new_icon", "icon_ships_7"),
          (else_try),
            (party_slot_ge, "p_main_party", slot_party_5_ship_type, 1),
            (assign, ":new_icon", "icon_ships_5"),
          (else_try),
            (party_slot_ge, "p_main_party", slot_party_3_ship_type, 1),
            (assign, ":new_icon", "icon_ships_3"),
          (else_try),
            (assign, ":new_icon", "icon_ships_1"),
          (end_try),
        (try_end),
        (neq, ":new_icon", "$g_player_party_icon"),
        (assign, "$g_player_party_icon", ":new_icon"),
        (party_set_icon, "p_main_party", ":new_icon"),
    ]),
    
    #Update how good a target player is for bandits
    (2,
      [
        (store_troop_gold, ":total_value", "trp_player"),
        (store_div, ":bandit_attraction", ":total_value", (10000/100)), #10000 gold = excellent_target
        
        (troop_get_inventory_capacity, ":inv_size", "trp_player"),
        (try_for_range, ":i_slot", 0, ":inv_size"),
          (troop_get_inventory_slot, ":item_id", "trp_player", ":i_slot"),
          (ge, ":item_id", 0),
          (try_begin),
            (is_between, ":item_id", trade_goods_begin, trade_goods_end),
            (store_item_value, ":item_value", ":item_id"),
            (val_add, ":total_value", ":item_value"),
          (try_end),
        (try_end),
        (val_clamp, ":bandit_attraction", 0, 100),
        (party_set_bandit_attraction, "p_main_party", ":bandit_attraction"),
    ]),
    
    
    #This is a backup script to activate the player faction if it doesn't happen automatically, for whatever reason
    (3,
      [
        (neq, "$campaign_type", camp_storyline),
        (try_for_range, ":center", walled_centers_begin, walled_centers_end),
          (faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_inactive),
          (store_faction_of_party, ":center_faction", ":center"),
          (eq, ":center_faction", "fac_player_supporters_faction"),
          (call_script, "script_activate_player_faction", "trp_player"),
        (try_end),
    ]),
    
    # Checking escape chances of prisoners that joined the party recently.
    (6,
      [(gt, "$g_prisoner_recruit_troop_id", 0),
        (gt, "$g_prisoner_recruit_size", 0),
        (gt, "$g_prisoner_recruit_last_time", 0),
        (is_currently_night),
        (try_begin),
          (neq, "$fortified_camp", 1), #no when fortified ok
          (store_skill_level, ":leadership", "skl_leadership", "trp_player"),
          (val_mul, ":leadership", 5),
          (store_sub, ":chance", 66, ":leadership"),
          (gt, ":chance", 0),
          (party_get_morale,":cur_morale","p_main_party"),#JuJu70
          (assign, ":num_escaped", 0),
          (try_for_range, ":unused", 0, "$g_prisoner_recruit_size"),
            (store_random_in_range, ":random_no", 0, ":cur_morale"), # JuJu70 adjustment to make it more prevalent for lower morale party
            (lt, ":random_no", ":chance"),
            (val_add, ":num_escaped", 1),
          (try_end),
          (party_remove_members, "p_main_party", "$g_prisoner_recruit_troop_id", ":num_escaped"),
          (assign, ":num_escaped", reg0),
          (gt, ":num_escaped", 0),
          (try_begin),
            (gt, ":num_escaped", 1),
            (assign, reg2, 1),
          (else_try),
            (assign, reg2, 0),
          (try_end),
          (assign, reg1, ":num_escaped"),
          (str_store_troop_name_by_count, s1, "$g_prisoner_recruit_troop_id", ":num_escaped"),
          (display_log_message, "@{reg1} {s1} {reg2?have:has} escaped from your party during the night.", color_bad_news), #moto chief
        (try_end),
        (assign, "$g_prisoner_recruit_troop_id", 0),
        (assign, "$g_prisoner_recruit_size", 0),
    ]),
    
    # Offering ransom fees for player's prisoner heroes
    (24,
      [(neq, "$g_ransom_offer_rejected", 1),
        (call_script, "script_offer_ransom_amount_to_player_for_prisoners_in_party", "p_main_party"),
        (eq, reg0, 0),#no prisoners offered
        (assign, ":end_cond", walled_centers_end),
        (try_for_range, ":center_no", walled_centers_begin, ":end_cond"),
          (party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
          (call_script, "script_offer_ransom_amount_to_player_for_prisoners_in_party", ":center_no"),
          (eq, reg0, 1),#a prisoner is offered
          (assign, ":end_cond", 0),#break
        (try_end),
    ]),
    
    # Exchanging hero prisoners between factions and clearing old ransom offers
    # JuJu70 probabilistic
    (0.61,
      [(assign, "$g_ransom_offer_rejected", 0),
        (store_random_in_range, ":center_no", walled_centers_begin, walled_centers_end),
        (party_get_slot, ":town_lord", ":center_no", slot_town_lord),
        (gt, ":town_lord", 0),
        (party_get_num_prisoner_stacks, ":num_stacks", ":center_no"),
        (try_for_range_backwards, ":i_stack", 0, ":num_stacks"),
          (party_prisoner_stack_get_troop_id, ":stack_troop", ":center_no", ":i_stack"),
          (troop_is_hero, ":stack_troop"),
          (troop_slot_eq, ":stack_troop", slot_troop_occupation, slto_kingdom_hero),
          (store_random_in_range, ":random_no", 0, 100),
          (try_begin),
            (le, ":random_no", 10),
            (call_script, "script_calculate_ransom_amount_for_troop", ":stack_troop"),
            (assign, ":ransom_amount", reg0),
            (troop_get_slot, ":wealth", ":town_lord", slot_troop_wealth),
            (val_add, ":wealth", ":ransom_amount"),
            (troop_set_slot, ":town_lord", slot_troop_wealth, ":wealth"),
            
            (party_remove_prisoners, ":center_no", ":stack_troop", 1),
            (call_script, "script_remove_troop_from_prison", ":stack_troop"),
            
            (store_troop_faction, ":troop_faction", ":stack_troop"),
            (str_store_troop_name, s1, ":stack_troop"),
            (str_store_faction_name, s3, ":troop_faction"),
            (faction_get_color, ":faction_color", ":troop_faction"),
            (display_log_message, "@{s1} of the {s3} has been released from captivity.", ":faction_color"),
          (try_end),
        (try_end),
    ]),
    
    # Adding mercenary troops to the towns tri-daily ON AVERAGE
    (8,
      [
        (store_random_in_range, ":switch", 0, 9),
        
        (try_begin),
          (eq, ":switch", 0),
          (call_script, "script_update_mercenary_units_of_towns"),
          #NPC changes begin
          # removes   (call_script, "script_update_companion_candidates_in_taverns"),
          #NPC changes end
        (else_try),
          (eq, ":switch", 1),
          (call_script, "script_update_ransom_brokers"),
        (else_try),
          (eq, ":switch", 2),
          (call_script, "script_update_tavern_travellers"),
        (else_try),
          (eq, ":switch", 3),
          (call_script, "script_update_tavern_minstrels"),
        (else_try),
          (eq, ":switch", 4),
          (call_script, "script_update_booksellers"),
        (else_try),
          (eq, ":switch", 5),
          (call_script, "script_update_companion_candidates_in_taverns"),
        (else_try),
          (call_script, "script_update_other_taverngoers"), #happens once a day ON AVERAGE
        (try_end),
    ]),
    
    #villages tri-daily ON AVERAGE
    (0.48,
      [
        (store_random_in_range, ":village_no", villages_begin, villages_end),
        (call_script, "script_update_villages_infested_by_bandits", ":village_no"),
        (call_script, "script_update_volunteer_troops_in_village", ":village_no"),
        (call_script, "script_update_npc_volunteer_troops_in_village", ":village_no"),
        # (try_end),
    ]),
    
    #STrig 70
    # Setting random walker types
    # JuJu70 probabilistic
    (0.13,
      [(store_random_in_range, ":center_no", centers_begin, centers_end),
        ##      (this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_town), #chief pone off para castle walkers
        ##      (             party_slot_eq, ":center_no", slot_party_type, spt_village),
        (call_script, "script_center_remove_walker_type_from_walkers", ":center_no", walkert_needs_money),
        (call_script, "script_center_remove_walker_type_from_walkers", ":center_no", walkert_needs_money_helped),
        (store_random_in_range, ":rand", 0, 100),
        (try_begin),
          (lt, ":rand", 70),
          (neg|party_slot_ge, ":center_no", slot_town_prosperity, 60),
          (call_script, "script_cf_center_get_free_walker", ":center_no"),
          (call_script, "script_center_set_walker_to_type", ":center_no", reg0, walkert_needs_money),
        (try_end),
        #    (try_end),
    ]),
    
    # Checking center upgrades half day ON AVERAGE
    (.045,
      [(store_random_in_range, ":center_no", centers_begin, centers_end),
        (party_get_slot, ":cur_improvement", ":center_no", slot_center_current_improvement),
        (gt, ":cur_improvement", 0),
        (party_get_slot, ":cur_improvement_end_time", ":center_no", slot_center_improvement_end_hour),
        (store_current_hours, ":cur_hours"),
        (ge, ":cur_hours", ":cur_improvement_end_time"),
        (party_set_slot, ":center_no", ":cur_improvement", 1),
        (party_set_slot, ":center_no", slot_center_current_improvement, 0),
        (call_script, "script_get_improvement_details", ":cur_improvement"),
        (try_begin),
          (party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
          (str_store_party_name, s4, ":center_no"),
          (display_log_message, "str_the_s0_in_s4_has_been_completed", color_quest_and_faction_news), #moto chief
        (try_end),
        # (try_begin),  duplicates script_get_center_ideal_prosperity
        # (is_between, ":center_no", villages_begin, villages_end),
        # (eq, ":cur_improvement", slot_center_has_fish_pond),
        # (store_random_in_range, ":rand", 0,10), #add prosperity to 0-10
        # (call_script, "script_change_center_prosperity", ":center_no", ":rand"),
        # (try_end),
        #(try_end),
    ]),
    
    # Adding bandits to towns and villages
    #daily on average
    (.089, [
        (store_random_in_range, ":center_no", centers_begin, centers_end),
        (this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_town),
        (party_slot_eq, ":center_no", slot_party_type, spt_village),
        (party_get_slot, ":has_bandits", ":center_no", slot_center_has_bandits),
        (try_begin),
          (le, ":has_bandits", 0),
          (assign, ":continue", 0),
          (try_begin),
            (check_quest_active, "qst_deal_with_night_bandits"),
            (quest_slot_eq, "qst_deal_with_night_bandits", slot_quest_target_center, ":center_no"),
            (neg|check_quest_succeeded, "qst_deal_with_night_bandits"),
            (assign, ":continue", 1),
          (else_try),
            (store_random_in_range, ":random_no", 0, 100),
            (lt, ":random_no", 3),
            (assign, ":continue", 1),
          (try_end),
          (try_begin),
            (eq, ":continue", 1),
            (store_random_in_range, ":random_no", 0, 3),
            (try_begin),
              (eq, ":random_no", 0),
              (assign, ":bandit_troop", "trp_bandit"),
            (else_try),
              (eq, ":random_no", 1),
              (assign, ":bandit_troop", "trp_mountain_bandit"),
            (else_try),
              (assign, ":bandit_troop", "trp_forest_bandit"),
            (try_end),
            (party_set_slot, ":center_no", slot_center_has_bandits, ":bandit_troop"),
            (try_begin),
              (eq, "$cheat_mode", 1),
              (str_store_party_name, s1, ":center_no"),
              (display_message, "@{!}{s1} is infested by bandits at night."),
            (try_end),
          (try_end),
        (else_try),
          (gt, ":has_bandits", 1),
          (try_begin),
            (assign, ":random_chance", 40),
            (try_begin),
              (party_slot_eq, ":center_no", slot_party_type, spt_town),
              (assign, ":random_chance", 20),
            (try_end),
            (assign, ":go", 0),
            (try_begin),
              (check_quest_active, "qst_deal_with_night_bandits"),
              (quest_get_slot, ":quest_target_center", "qst_deal_with_night_bandits", slot_quest_target_center),
              (eq, ":quest_target_center", ":center_no"),
              (assign, ":go", 1),
            (try_end),
            (eq, ":go", 0),
            (store_random_in_range, ":random_no", 0, 100),
            (lt, ":random_no", ":random_chance"),
            (party_set_slot, ":center_no", slot_center_has_bandits, 0),
            (try_begin),
              (eq, "$cheat_mode", 1),
              (str_store_party_name, s1, ":center_no"),
              (display_message, "@{s1} is no longer infested by bandits at night."),
            (try_end),
          (try_end),
        (else_try),
          (eq, ":has_bandits", 1),
          (store_random_in_range, ":rand", 0,100),
          (lt, ":rand", 10),
          (party_set_slot, ":center_no", slot_center_has_bandits, 0),
        (try_end),
        (try_begin),
          (party_slot_eq,":center_no", slot_party_levy_on, 1),
          (party_get_slot, ":village_elder", ":center_no",slot_town_elder),
          (troop_get_slot, ":cur_party", ":village_elder", slot_troop_leaded_party),
          (try_begin),
            (gt, ":cur_party", 0),
            (party_slot_eq, ":cur_party", slot_party_type, spt_levy),
            (party_is_active, ":cur_party"),
          (else_try),
            (try_for_range, ":slot", ek_item_0, ek_head),
              (troop_get_inventory_slot, ":weapon", ":village_elder", ":slot"),
              (gt, ":weapon", 0),
              (troop_inventory_slot_set_item_amount, ":village_elder", ":slot", 0),
            (try_end),
            (troop_get_inventory_slot, ":slot_coat", ":village_elder", ek_body),
            (try_begin),
              (gt, ":slot_coat", 0),
              (item_get_body_armor, ":ba", ":slot_coat"),
              (gt, ":ba", 25),
              (troop_remove_item, ":village_elder", ":slot_coat"),
              (troop_equip_items, ":village_elder"),
            (try_end),
            (troop_get_inventory_slot, ":slot_coat", ":village_elder", ek_body),
            (try_begin),
              (le, ":slot_coat", 0),
              (party_get_slot, ":center_culture", ":center_no", slot_center_culture),
              (try_begin),
                (this_or_next|eq,":center_culture","fac_culture_saxon"),
                (eq,":center_culture","fac_culture_angle"),
                (store_random_in_range, ":new", "itm_bl_tunic06", "itm_yellow_cloak"),
              (else_try),
                (eq, ":center_culture", "fac_culture_welsh"),
                (store_random_in_range, ":new", "itm_briton_tunic9", "itm_briton_tunic15"),
              (else_try),
                (eq, ":center_culture", "fac_culture_norse"),
                (store_random_in_range, ":new", "itm_btunic_3", "itm_btunic_12"),
              (else_try),
                (eq, ":center_culture", "fac_culture_scotch"),
                (store_random_in_range, ":new", "itm_briton_tunic15", "itm_briton_tunic19"),
              (else_try),
                (eq, ":center_culture", "fac_culture_irish"),
                (store_random_in_range, ":new", "itm_briton_tunic20", "itm_celta_capa3"),
              (try_end),
              (troop_add_item, ":village_elder", ":new"),
              (troop_equip_items, ":village_elder"),
            (try_end),
            (troop_get_inventory_slot, ":slot_head", ":village_elder", ek_head),
            (try_begin),
              (gt, ":slot_head", 0),
              (item_get_head_armor, ":ha", ":slot_head"),
              (gt, ":ha", 20),
              (troop_remove_item, ":village_elder", ":slot_head"),
            (try_end),
            (party_set_slot, ":center_no", slot_party_levy_on, 0),
            #			(str_store_party_name, s33, ":center_no"),
            #			(display_message, "@Village elder is available in {s33}"),
          (try_end),
        (try_end),
    ]),
    
    # Adding tournaments to towns
    (24,
      [(assign, ":num_active_tournaments", 0),
        (try_for_range, ":center_no", towns_begin, towns_end),
          (party_get_slot, ":has_tournament", ":center_no", slot_town_has_tournament),
          (try_begin),
            (eq, ":has_tournament", 1),#tournament ended, simulate
            (call_script, "script_fill_tournament_participants_troop", ":center_no", 0),
            (call_script, "script_sort_tournament_participant_troops"),#may not be needed
            (call_script, "script_get_num_tournament_participants"),
            (store_sub, ":needed_to_remove_randomly", reg0, 1),
            (call_script, "script_remove_tournament_participants_randomly", ":needed_to_remove_randomly"),
            (call_script, "script_sort_tournament_participant_troops"),
            (troop_get_slot, ":winner_troop", "trp_tournament_participants", 0),
            (try_begin),
              (is_between, ":winner_troop", active_npcs_begin, active_npcs_end),
              (str_store_troop_name_link, s1, ":winner_troop"),
              (str_store_party_name_link, s2, ":center_no"),
              (display_message, "@{s1} has won the tournament at {s2}.", color_hero_news), #moto chief
              (call_script, "script_change_troop_renown", ":winner_troop", 20),
            (try_end),
          (try_end),
          (val_sub, ":has_tournament", 1),
          (val_max, ":has_tournament", 0),
          (party_set_slot, ":center_no", slot_town_has_tournament, ":has_tournament"),
          (try_begin),
            (gt, ":has_tournament", 0),
            (val_add, ":num_active_tournaments", 1),
          (try_end),
        (try_end),
        
        (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
          (faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_feast),
          
          (faction_get_slot, ":faction_object", ":faction_no", slot_faction_ai_object),
          (is_between, ":faction_object", towns_begin, towns_end),
          
          (party_slot_ge, ":faction_object", slot_town_has_tournament, 1),
          #continue holding tournaments during the feast
          (party_set_slot, ":faction_object", slot_town_has_tournament, 2),
        (try_end),
        
        (try_begin),
          (lt, ":num_active_tournaments", 3),
          (store_random_in_range, ":random_no", 0, 100),
          #Add new tournaments with a 30% chance if there are less than 3 tournaments going on
          (lt, ":random_no", 30),
          (store_random_in_range, ":random_town", towns_begin, towns_end),
          (store_random_in_range, ":random_days", 12, 15),
          (party_set_slot, ":random_town", slot_town_has_tournament, ":random_days"),
          (try_begin),
            (eq, "$cheat_mode", 1),
            (str_store_party_name, s1, ":random_town"),
            (display_message, "@{!}{s1} is holding a tournament."),
          (try_end),
        (try_end),
    ]),
    
    (3,
      [
        (assign, "$g_player_tournament_placement", 0),
    ]),
    
    
    #(0.1,
    
    #	[
    #	(try_begin),
    #		(troop_slot_ge, "trp_player", slot_troop_spouse, active_npcs_begin),
    #		(troop_get_slot, ":spouse", "trp_player", slot_troop_spouse),
    #		(store_faction_of_troop, ":spouse_faction", ":spouse"),
    #		(neq, ":spouse_faction", "$players_kingdom"),
    #		(display_message, "@{!}ERROR! Player and spouse are separate factions"),
    #	(try_end),
    #	]
    #),
    
    # Asking to give center to player
    ##  (8,
    ##   [
    ###    (assign, ":done", 0),
    ###    (try_for_range, ":center_no", centers_begin, centers_end),
    ###      (eq, ":done", 0),
    ###      (party_slot_eq, ":center_no", slot_town_lord, stl_reserved_for_player),
    ###      (assign, "$g_center_to_give_to_player", ":center_no"),
    ## #     (try_begin),
    ##  #      (eq, "$g_center_to_give_to_player", "$g_castle_requested_by_player"),
    ##   #     (assign, "$g_castle_requested_by_player", 0),
    ##	#	(try_begin),
    ##	#		(eq, "$g_castle_requested_for_troop", "trp_player"),
    ##	#		(jump_to_menu, "mnu_requested_castle_granted_to_player"),
    ##	#	(else_try),
    ##	#		(jump_to_menu, "mnu_requested_castle_granted_to_player_husband"),
    ##	#	(try_end),
    ##    #  (else_try),
    ##    #    (jump_to_menu, "mnu_give_center_to_player"),
    ##    # (try_end),
    ##    #  (assign, ":done", 1),
    ##    #(else_try),
    ##    #  (eq, ":center_no", "$g_castle_requested_by_player"),
    ##    #  (party_slot_ge, ":center_no", slot_town_lord, active_npcs_begin),
    ##    #  (assign, "$g_castle_requested_by_player", 0),
    ##    #  (store_faction_of_party, ":faction", ":center_no"),
    ##    #  (eq, ":faction", "$players_kingdom"),
    ##    #  (assign, "$g_center_to_give_to_player", ":center_no"),
    ##	#  (try_begin),
    ###		(eq, "$player_has_homage", 1),
    ###		(jump_to_menu, "mnu_requested_castle_granted_to_another"),
    ###	  (else_try),
    ###		(jump_to_menu, "mnu_requested_castle_granted_to_another_female"),
    ###	  (try_end),
    ## #     (assign, ":done", 1),
    ##  #  (try_end),
    ##    ]),
    
    # Taking denars from player while resting in not owned centers
    (1,
      [(neg|map_free),
        (is_currently_night),
        #    (ge, "$g_last_rest_center", 0),
        (is_between, "$g_last_rest_center", centers_begin, centers_end),
        (neg|party_slot_eq, "$g_last_rest_center", slot_town_lord, "trp_player"),
        (store_faction_of_party, ":last_rest_center_faction", "$g_last_rest_center"),
        (neq, ":last_rest_center_faction", "fac_player_supporters_faction"),
        (store_current_hours, ":cur_hours"),
        (ge, ":cur_hours", "$g_last_rest_payment_until"),
        (store_add, "$g_last_rest_payment_until", ":cur_hours", 24),
        (store_troop_gold, ":gold", "trp_player"),
        (party_get_num_companions, ":num_men", "p_main_party"),
        (store_div, ":total_cost", ":num_men", 4),
        (val_add, ":total_cost", 1),
        (try_begin),
          (ge, ":gold", ":total_cost"),
          (display_message, "@You pay for accommodation."),
          (troop_remove_gold, "trp_player", ":total_cost"),
        (else_try),
          (gt, ":gold", 0),
          (troop_remove_gold, "trp_player", ":gold"),
        (try_end),
    ]),
    
    # Spawn some bandits.
    (35,  #for spawn points of 15 parties, all will be spawned in three weeks.
      [
        (call_script, "script_update_party_creation_random_limits"),
        (call_script, "script_spawn_bandits"),
    ]),
    
    # Spawn lairs every two weeks ON AVERAGE
    (24*14/20, [	#laired_spawn_points_end - laired_spawn_points_begin = 20
        (store_random_in_range, ":bandit_spawn_point", laired_spawn_points_begin, laired_spawn_points_end),
        (call_script, "script_spawn_lairs", ":bandit_spawn_point"),
    ]),
    
    # Check if a faction is defeated every day
    (24,
      [
        (assign, ":num_active_factions", 0),
        (try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
          (faction_set_slot, ":cur_kingdom", slot_faction_number_of_parties, 0),
        (try_end),
        (try_for_parties, ":cur_party"),
          (store_faction_of_party, ":party_faction", ":cur_party"),
          (is_between, ":party_faction", kingdoms_begin, kingdoms_end),
          (this_or_next|is_between, ":cur_party", centers_begin, centers_end),
          (party_slot_eq, ":cur_party", slot_party_type, spt_kingdom_hero_party),
          (faction_get_slot, ":kingdom_num_parties", ":party_faction", slot_faction_number_of_parties),
          (val_add, ":kingdom_num_parties", 1),
          (faction_set_slot, ":party_faction", slot_faction_number_of_parties, ":kingdom_num_parties"),
        (try_end),
        (try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
          #(try_begin),
          #(eq, "$cheat_mode", 1),
          #(str_store_faction_name, s1, ":cur_kingdom"),
          #(faction_get_slot, reg1, ":cur_kingdom", slot_faction_number_of_parties),
          #(display_message, "@{!}Number of parties belonging to {s1}: {reg1}"),
          #(try_end),
          (faction_slot_eq, ":cur_kingdom", slot_faction_state, sfs_active),
          (val_add, ":num_active_factions", 1),
          (faction_slot_eq, ":cur_kingdom", slot_faction_number_of_parties, 0),
          (assign, ":faction_removed", 0),
          (try_begin),
            (eq, ":cur_kingdom", "fac_player_supporters_faction"),
            (try_begin),
              (le, "$supported_pretender", 0),
              (call_script, "script_deactivate_player_faction", 1),
              (assign, ":faction_removed", 1),
            (try_end),
          (else_try),
            (neq, "$players_kingdom", ":cur_kingdom"),
            (faction_set_slot, ":cur_kingdom", slot_faction_state, sfs_defeated),
            (try_for_parties, ":cur_party"),
              (store_faction_of_party, ":party_faction", ":cur_party"),
              (eq, ":party_faction", ":cur_kingdom"),
              (party_get_slot, ":home_center", ":cur_party", slot_party_home_center),
              (is_between, ":home_center", centers_begin, centers_end),
              (store_faction_of_party, ":home_center_faction", ":home_center"),
              (party_set_faction, ":cur_party", ":home_center_faction"),
            (try_end),
            (assign, ":kingdom_pretender", -1),
            (try_for_range, ":cur_pretender", pretenders_begin, pretenders_end),
              (troop_slot_eq, ":cur_pretender", slot_troop_original_faction, ":cur_kingdom"),
              (assign, ":kingdom_pretender", ":cur_pretender"),
            (try_end),
            (try_begin),
              (is_between, ":kingdom_pretender", pretenders_begin, pretenders_end),
              (neq, ":kingdom_pretender", "$supported_pretender"),
              (troop_set_slot, ":kingdom_pretender", slot_troop_cur_center, 0), #remove pretender from the world
            (try_end),
            (assign, ":faction_removed", 1),
            (try_begin),
              (eq, "$players_oath_renounced_against_kingdom", ":cur_kingdom"),
              (assign, "$players_oath_renounced_against_kingdom", 0),
              (assign, "$players_oath_renounced_given_center", 0),
              (assign, "$players_oath_renounced_begin_time", 0),
              (call_script, "script_add_notification_menu", "mnu_notification_oath_renounced_faction_defeated", ":cur_kingdom", 0),
            (try_end),
            #This menu must be at the end because faction banner will change after this menu if the player's supported pretender's original faction is cur_kingdom
            (call_script, "script_add_notification_menu", "mnu_notification_faction_defeated", ":cur_kingdom", 0),
            
            (try_for_range, ":quest", 0, "qst_quests_end"),
              (neq, ":quest", "qst_rebel_against_kingdom"),
              (check_quest_active, ":quest"),
              
              (this_or_next|quest_slot_eq, ":quest", slot_quest_target_faction, ":cur_kingdom"),
              (quest_slot_eq, ":quest", slot_quest_object_faction, ":cur_kingdom"),
              
              (neg|check_quest_succeeded, ":quest"),
              (call_script, "script_abort_quest", ":quest", 0),
            (try_end),
          (try_end),
          (try_begin),
            (eq, ":faction_removed", 1),
            (val_sub, ":num_active_factions", 1),
            #(call_script, "script_store_average_center_value_per_faction"),
          (try_end),
          (try_for_range, ":cur_kingdom_2", kingdoms_begin, kingdoms_end),
            (call_script, "script_update_faction_notes", ":cur_kingdom_2"),
          (try_end),
        (try_end),
        (try_begin),
          (eq, ":num_active_factions", 1),
          (eq, "$g_one_faction_left_notification_shown", 0),
          (assign, "$g_one_faction_left_notification_shown", 1),
          (try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
            (faction_slot_eq, ":cur_kingdom", slot_faction_state, sfs_active),
            (call_script, "script_add_notification_menu", "mnu_notification_one_faction_left", ":cur_kingdom", 0),
          (try_end),
        (try_end),
    ]),
    #79
    (3, #check to see if player's court has been captured
      [(try_begin),
          (faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_active),
          (try_begin), #The old court has been lost
            (is_between, "$g_player_court", centers_begin, centers_end),
            (store_faction_of_party, ":court_faction", "$g_player_court"),
            (neq, ":court_faction", "fac_player_supporters_faction"),
            (call_script, "script_add_notification_menu", "mnu_notification_court_lost", 0, 0),
            
          (else_try),	#At least one new court has been found since last call of trigger
            (lt, "$g_player_court", centers_begin),
            #Will by definition not active until a center is taken by the player faction
            #Player minister must have been appointed at some point
            (this_or_next|faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
            (gt, "$g_player_minister", 0),
            
            (assign, ":center_found", 0),
            (try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
              (eq, ":center_found", 0),
              (store_faction_of_party, ":court_faction", ":walled_center"),
              (eq, ":court_faction", "fac_player_supporters_faction"),
              (assign, ":center_found", ":walled_center"),
            (try_end),
            (try_begin),
              (ge, ":center_found", 1),
              (call_script, "script_add_notification_menu", "mnu_notification_court_lost", 0, 0),
            (else_try),
              (call_script, "script_deactivate_player_faction", 1),
            (try_end),
          (try_end),
        (try_end),
        
        #Piggybacking on trigger:
        (call_script, "script_map_sea_ai_3"),
        
        (try_begin),
          (troop_get_slot, ":betrothed", "trp_player", slot_troop_betrothed),
          (gt, ":betrothed", 0),
          (neg|check_quest_active, "qst_wed_betrothed"),
          (neg|check_quest_active, "qst_wed_betrothed_female"),
          (str_store_troop_name, s5, ":betrothed"),
          (display_message, "str_s5_sends_word_that_your_betrothal_is_ended"),
          (troop_set_slot, "trp_player", slot_troop_betrothed, -1),
          (troop_set_slot, ":betrothed", slot_troop_betrothed, -1),
        (try_end),
    ]),
    
    #STrig 80
    # Reduce renown slightly by 0.5% every week
    (7 * 24, [
      (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
      (store_div, ":renown_decrease", ":player_renown", 200),
      (val_sub, ":player_renown", ":renown_decrease"),
      (troop_set_slot, "trp_player", slot_troop_renown, ":player_renown"),
    ]),
    
    # Read books if player is resting.
    (1, [(neg|map_free),
        (gt, "$g_player_reading_book", 0),
        (player_has_item, "$g_player_reading_book"),
        (store_attribute_level, ":int", "trp_player", ca_intelligence),
        (item_get_slot, ":int_req", "$g_player_reading_book", slot_item_intelligence_requirement),
        (le, ":int_req", ":int"),
        (item_get_slot, ":book_reading_progress", "$g_player_reading_book", slot_item_book_reading_progress),
        (item_get_slot, ":book_read", "$g_player_reading_book", slot_item_book_read),
        (eq, ":book_read", 0),
        (val_add, ":book_reading_progress", 7),
        (item_set_slot, "$g_player_reading_book", slot_item_book_reading_progress, ":book_reading_progress"),
        (ge, ":book_reading_progress", 1000),
        (item_set_slot, "$g_player_reading_book", slot_item_book_read, 1),
        (str_store_item_name, s1, "$g_player_reading_book"),
        (str_clear, s2),
        (try_begin),
          (eq, "$g_player_reading_book", "itm_book_tactics"),
          (troop_raise_skill, "trp_player", "skl_tactics", 1),
          (str_store_string, s2, "@ Your tactics skill has increased by 1."),
        (else_try),
          (eq, "$g_player_reading_book", "itm_book_persuasion"),
          (troop_raise_skill, "trp_player", "skl_persuasion", 1),
          (str_store_string, s2, "@ Your persuasion skill has increased by 1."),
        (else_try),
          (eq, "$g_player_reading_book", "itm_book_leadership"),
          (troop_raise_skill, "trp_player", "skl_leadership", 1),
          (str_store_string, s2, "@ Your leadership skill has increased by 1."),
        (else_try),
          (eq, "$g_player_reading_book", "itm_book_intelligence"),
          (troop_raise_attribute, "trp_player", ca_intelligence, 1),
          (str_store_string, s2, "@ Your intelligence has increased by 1."),
        (else_try),
          (eq, "$g_player_reading_book", "itm_book_trade"),
          (troop_raise_skill, "trp_player", "skl_trade", 1),
          (str_store_string, s2, "@ Your trade skill has increased by 1."),
        (else_try),
          (eq, "$g_player_reading_book", "itm_book_weapon_mastery"),
          (troop_raise_skill, "trp_player", "skl_weapon_master", 1),
          (str_store_string, s2, "@ Your weapon master skill has increased by 1."),
        (else_try),
          (eq, "$g_player_reading_book", "itm_book_engineering"),
          (troop_raise_skill, "trp_player", "skl_engineer", 1),
          (str_store_string, s2, "@ Your engineer skill has increased by 1."),
        (try_end),
        
        (unlock_achievement, ACHIEVEMENT_BOOK_WORM),
        
        (try_begin),
          (eq, "$g_infinite_camping", 0),
          (dialog_box, "@You have finished reading {s1}.{s2}", "@Book Read"),
        (try_end),
        
        (assign, "$g_player_reading_book", 0),
    ]),
    
    # Removing cattle herds if they are way out of range
    (12, [(party_slot_eq, "p_main_party", slot_party_on_water, 0),	#VC-2184
        (try_for_parties, ":cur_party"),
          (party_slot_eq, ":cur_party", slot_party_type, spt_cattle_herd),
          (store_distance_to_party_from_party, ":dist",":cur_party", "p_main_party"),
          (try_begin),
            (gt, ":dist", 30),
            (remove_party, ":cur_party"),
            (try_begin),
              #Fail quest if the party is the quest party
              (check_quest_active, "qst_move_cattle_herd"),
              (neg|check_quest_concluded, "qst_move_cattle_herd"),
              (quest_slot_eq, "qst_move_cattle_herd", slot_quest_target_party, ":cur_party"),
              (call_script, "script_fail_quest", "qst_move_cattle_herd"),
            (end_try),
          (else_try),
            (gt, ":dist", 10),
            (party_set_slot, ":cur_party", slot_cattle_driven_by_player, 0),
            (party_set_ai_behavior, ":cur_party", ai_bhvr_hold),
          (try_end),
        (try_end),
    ]),
    
    
    #####!!!!!
    
    # Village upgrade triggers
    
    # School chief cambia a 7x24
    # Too deterministic -JuJu70- make a bit random
    # JuJu70 -- People destroying churches
    (1.12,
      [  (store_random_in_range, ":cur_village", villages_begin, villages_end),
        (try_begin),
          (party_slot_eq, ":cur_village", slot_town_lord, "trp_player"),
          (party_slot_eq, ":cur_village", slot_center_has_school, 1),
          (party_get_slot, ":cur_relation", ":cur_village", slot_center_player_relation),
          (lt, ":cur_relation", 70), # school shouldn't improve relation all the way to the max, not even 70 TBH
          (store_random_in_range, ":rand", 0, 150),
          (lt, ":rand", 55),
          (val_add, ":cur_relation", 1),
          (party_set_slot, ":cur_village", slot_center_player_relation, ":cur_relation"),
        (try_end),
        # religious unhapiness
        (store_random_in_range, ":center", centers_begin, centers_end),
        (assign, ":destroy", 0),
        (try_begin),
          (party_slot_eq, ":center", slot_center_religion, 1),
          (this_or_next|party_slot_eq, ":center", slot_center_has_temple1, 1),
          (party_slot_eq, ":center", slot_center_has_monastery1, 1),
          (party_get_slot, ":faith", ":center", slot_center_faithratio),
          
          (try_begin),
            (neg|party_slot_eq, ":center", slot_town_lord, "trp_player"),
            (lt, ":faith", 30),
            (store_random_in_range, ":rand", 0, 40),
            (lt, ":rand", 4),
            (assign, ":destroy", 1),
          (else_try),
            (party_slot_eq, ":center", slot_town_lord, "trp_player"),
            (party_get_slot, ":center_relation", ":center", slot_center_player_relation),
            (lt, ":faith", 55),
            (try_begin),
              (lt, ":center_relation", 15),
              (store_random_in_range, ":rand", 0, 40),
              (lt, ":rand", 4),
              (assign, ":destroy", 1),
            (else_try),
              (is_between, ":center_relation", 15, 50),
              (store_random_in_range, ":rand", 0, 40),
              (lt, ":rand", 2),
              (assign, ":destroy", 1),
            (else_try),
              (store_random_in_range, ":rand", 0, 40),
              (lt, ":rand", 1),
              (assign, ":destroy", 1),
            (try_end),
          (try_end),
        (else_try),
          (party_slot_eq, ":center", slot_center_religion, 2),
          (this_or_next|party_slot_eq, ":center", slot_center_has_temple3, 1),
          (party_slot_eq, ":center", slot_center_has_monastery3, 1),
          (party_get_slot, ":faith", ":center", slot_center_faithratio),
          (store_sub, ":p_faith", 100, ":faith"),
          (try_begin),
            (neg|party_slot_eq, ":center", slot_town_lord, "trp_player"),
            (lt, ":p_faith", 30),
            (store_random_in_range, ":rand", 0, 40),
            (lt, ":rand", 4),
            (assign, ":destroy", 1),
          (else_try),
            (party_slot_eq, ":center", slot_town_lord, "trp_player"),
            (party_get_slot, ":center_relation", ":center", slot_center_player_relation),
            (lt, ":p_faith", 55),
            (try_begin),
              (lt, ":center_relation", 15),
              (store_random_in_range, ":rand", 0, 40),
              (lt, ":rand", 4),
              (assign, ":destroy", 1),
            (else_try),
              (is_between, ":center_relation", 15, 50),
              (store_random_in_range, ":rand", 0, 40),
              (lt, ":rand", 2),
              (assign, ":destroy", 1),
            (else_try),
              (store_random_in_range, ":rand", 0, 40),
              (lt, ":rand", 1),
              (assign, ":destroy", 1),
            (try_end),
          (try_end),
        (try_end),
        (eq, ":destroy", 1),
        (try_begin),
          (party_slot_eq, ":center", slot_center_has_temple1, 1),
          (party_set_slot, ":center", slot_center_has_temple1, 0),
          (str_store_string, s25, "@Christian monastery"),
        (else_try),
          (party_slot_eq, ":center", slot_center_has_monastery1, 1),
          (party_set_slot, ":center", slot_center_has_monastery1, 0),
          (str_store_string, s25, "@Christian church"),
        (else_try),
          (party_slot_eq, ":center", slot_center_has_monastery3, 1),
          (party_set_slot, ":center", slot_center_has_monastery3, 0),
          (str_store_string, s25, "@shrine to Norse gods"),
        (else_try),
          (party_slot_eq, ":center", slot_center_has_temple3, 1),
          (party_set_slot, ":center", slot_center_has_temple3, 0),
          (str_store_string, s25, "@temple to Odin"),
        (try_end),
        (store_random_in_range, ":rand", -3,0),
        (try_begin),
          (party_slot_eq, ":center", slot_center_religion, 1),
          (val_add, ":faith", ":rand"),
          (val_clamp, ":faith", 0, 101),
          (party_set_slot, ":center", slot_center_faithratio, ":faith"),
        (else_try),
          (party_slot_eq, ":center", slot_center_religion, 2),
          (val_add, ":p_faith", ":rand"),
          (store_sub, ":faith", 100, ":p_faith"),
          (val_clamp, ":faith", 0, 101),
          (party_set_slot, ":center", slot_center_faithratio, ":faith"),
        (try_end),
        (try_begin),
          (party_slot_eq, ":center", slot_town_lord, "trp_player"),
          (str_store_party_name, s24, ":center"),
          (display_message, "@People of {s24} are unhappy with your religious intolerance, and destroyed {s25}.", color_bad_news),
          (call_script, "script_change_player_relation_with_center", ":center", -3),
        (try_end),
    ]),
    
    # Quest triggers:
    
    # Remaining days text update
    (24, [(try_for_range, ":cur_quest", all_quests_begin, all_quests_end),
          (try_begin),
            (check_quest_active, ":cur_quest"),
            (try_begin),
              (neg|check_quest_concluded, ":cur_quest"),
              (quest_slot_ge, ":cur_quest", slot_quest_expiration_days, 1),
              (quest_get_slot, ":exp_days", ":cur_quest", slot_quest_expiration_days),
              (val_sub, ":exp_days", 1),
              (try_begin),
                (eq, ":exp_days", 0),
                (call_script, "script_abort_quest", ":cur_quest", 2),
              (else_try),
                (quest_set_slot, ":cur_quest", slot_quest_expiration_days, ":exp_days"),
                (assign, reg0, ":exp_days"),
                (add_quest_note_from_sreg, ":cur_quest", 7, "@You have {reg0} days to finish this quest.", 0),
              (try_end),
            (try_end),
          (else_try),
            (quest_slot_ge, ":cur_quest", slot_quest_dont_give_again_remaining_days, 1),
            (quest_get_slot, ":value", ":cur_quest", slot_quest_dont_give_again_remaining_days),
            (val_sub, ":value", 1),
            (quest_set_slot, ":cur_quest", slot_quest_dont_give_again_remaining_days, ":value"),
          (try_end),
        (try_end),
    ]),
    
    # Report to army quest
    (2,
      [
        (eq, "$g_infinite_camping", 0),
        (is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
        (eq, "$g_player_is_captive", 0),
        
        (try_begin),
          (check_quest_active, "qst_report_to_army"),
          (faction_slot_eq, "$players_kingdom", slot_faction_marshal, -1),
          (call_script, "script_abort_quest", "qst_report_to_army", 0),
        (try_end),
        
        (faction_get_slot, ":faction_object", "$players_kingdom", slot_faction_ai_object),
        
        (neg|faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_default),
        (neg|faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_feast),
        
        (assign, ":continue", 1),
        (try_begin),
          (this_or_next|faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_attacking_enemies_around_center),
          (this_or_next|faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_attacking_center),
          (faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_raiding_village),
          (neg|is_between, ":faction_object", walled_centers_begin, walled_centers_end),
          (assign, ":continue", 0),
        (try_end),
        (eq, ":continue", 1),
        
        (assign, ":kingdom_is_at_war", 0),
        (try_for_range, ":faction", kingdoms_begin, kingdoms_end),
          (neq, ":faction", "$players_kingdom"),
          (store_relation, ":relation", ":faction", "$players_kingdom"),
          (lt, ":relation", 0),
          (assign, ":kingdom_is_at_war", 1),
        (try_end),
        (eq, ":kingdom_is_at_war", 1),
        
        (neg|check_quest_active, "qst_report_to_army"),
        (neg|check_quest_active, "qst_follow_army"),
        
        (neg|quest_slot_ge, "qst_report_to_army", slot_quest_dont_give_again_remaining_days, 1),
        (faction_get_slot, ":faction_marshal", "$players_kingdom", slot_faction_marshal),
        (gt, ":faction_marshal", 0),
        (troop_get_slot, ":faction_marshal_party", ":faction_marshal", slot_troop_leaded_party),
        (gt, ":faction_marshal_party", 0),
        (party_is_active, ":faction_marshal_party"),
        
        (store_distance_to_party_from_party, ":distance_to_marshal", ":faction_marshal_party", "p_main_party"),
        (le, ":distance_to_marshal", 96),
        
        (assign, ":has_no_quests", 1),
        (try_for_range, ":cur_quest", lord_quests_begin, lord_quests_end),
          (check_quest_active, ":cur_quest"),
          (quest_slot_eq, ":cur_quest", slot_quest_giver_troop, ":faction_marshal"),
          (assign, ":has_no_quests", 0),
        (try_end),
        (eq, ":has_no_quests", 1),
        
        (try_for_range, ":cur_quest", lord_quests_begin_2, lord_quests_end_2),
          (check_quest_active, ":cur_quest"),
          (quest_slot_eq, ":cur_quest", slot_quest_giver_troop, ":faction_marshal"),
          (assign, ":has_no_quests", 0),
        (try_end),
        (eq, ":has_no_quests", 1),
        
        (try_for_range, ":cur_quest", army_quests_begin, army_quests_end),
          (check_quest_active, ":cur_quest"),
          (assign, ":has_no_quests", 0),
        (try_end),
        (eq, ":has_no_quests", 1),
        
        (store_character_level, ":level", "trp_player"),
        (ge, ":level", 8),
        (assign, ":cur_target_amount", 2),
        (try_for_range, ":cur_center", centers_begin, centers_end),
          (party_slot_eq, ":cur_center", slot_town_lord, "trp_player"),
          (try_begin),
            (party_slot_eq, ":cur_center", slot_party_type, spt_town),
            (val_add, ":cur_target_amount", 3),
          (else_try),
            (party_slot_eq, ":cur_center", slot_party_type, spt_castle),
            (val_add, ":cur_target_amount", 1),
          (else_try),
            (val_add, ":cur_target_amount", 1),
          (try_end),
        (try_end),
        
        (val_mul, ":cur_target_amount", 4),
        (val_min, ":cur_target_amount", 60),
        (quest_set_slot, "qst_report_to_army", slot_quest_giver_troop, ":faction_marshal"),
        (quest_set_slot, "qst_report_to_army", slot_quest_target_troop, ":faction_marshal"),
        (quest_set_slot, "qst_report_to_army", slot_quest_target_amount, ":cur_target_amount"),
        (quest_set_slot, "qst_report_to_army", slot_quest_expiration_days, 4),
        (quest_set_slot, "qst_report_to_army", slot_quest_dont_give_again_period, 22),
        (jump_to_menu, "mnu_kingdom_army_quest_report_to_army"),
    ]),
    
    
    # Army quest initializer
    (3,
      [
        (assign, "$g_random_army_quest", -1),
        (check_quest_active, "qst_follow_army", 1),
        (is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
        #Rebellion changes begin
        #     (neg|is_between, "$players_kingdom", rebel_factions_begin, rebel_factions_end),
        #Rebellion changes end
        (neg|faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_default),
        (faction_get_slot, ":faction_marshal", "$players_kingdom", slot_faction_marshal),
        (neq, ":faction_marshal", "trp_player"),
        (gt, ":faction_marshal", 0),
        (troop_get_slot, ":faction_marshal_party", ":faction_marshal", slot_troop_leaded_party),
        (gt, ":faction_marshal_party", 0),
        (party_is_active, ":faction_marshal_party"),
        (store_distance_to_party_from_party, ":dist", ":faction_marshal_party", "p_main_party"),
        (try_begin),
          (lt, ":dist", 15),
          (assign, "$g_player_follow_army_warnings", 0),
          (store_current_hours, ":cur_hours"),
          (faction_get_slot, ":last_offensive_time", "$players_kingdom", slot_faction_last_offensive_concluded),
          (store_sub, ":passed_time", ":cur_hours", ":last_offensive_time"),
          
          (assign, ":result", -1),
          (try_begin),
            (store_random_in_range, ":random_no", 0, 100),
            (lt, ":random_no", 30),
            (troop_slot_eq, ":faction_marshal", slot_troop_does_not_give_quest, 0),
            (try_for_range, ":unused", 0, 20), #Repeat trial twenty times
              (eq, ":result", -1),
              (store_random_in_range, ":quest_no", army_quests_begin, army_quests_end),
              (neg|quest_slot_ge, ":quest_no", slot_quest_dont_give_again_remaining_days, 1),
              (try_begin),
                (eq, ":quest_no", "qst_deliver_cattle_to_army"),
                # (eq, 1, 0), #disables temporarily
                (try_begin),
                  (faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_attacking_center),
                  (gt, ":passed_time", 120),#5 days
                  (store_random_in_range, ":quest_target_amount", 5, 10),
                  (assign, ":result","qst_deliver_cattle_to_army"),
                  (quest_set_slot, ":result", slot_quest_target_amount, ":quest_target_amount"),
                  (quest_set_slot, ":result", slot_quest_expiration_days, 10),
                  (quest_set_slot, ":result", slot_quest_dont_give_again_period, 30),
                (try_end),
              (else_try),
                (eq, ":quest_no", "qst_join_siege_with_army"),
                (val_add, ":quest_no", 1),
                (eq, 1, 0),
                # (try_begin),
                  # (faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_attacking_center),
                  # (faction_get_slot, ":ai_object", "$players_kingdom", slot_faction_ai_object),
                  # (is_between, ":ai_object", walled_centers_begin, walled_centers_end),
                  # (party_get_battle_opponent, ":besieged_center", ":faction_marshal_party"),
                  # (eq, ":besieged_center", ":ai_object"),
                  # #army is assaulting the center
                  # (assign, ":result", ":quest_no"),
                  # (quest_set_slot, ":result", slot_quest_target_center, ":ai_object"),
                  # (quest_set_slot, ":result", slot_quest_expiration_days, 2),
                  # (quest_set_slot, ":result", slot_quest_dont_give_again_period, 15),
                # (try_end),
              (else_try),
                (eq, ":quest_no", "qst_scout_waypoints"),
                (try_begin),
                  (assign, ":end_cond", 100),
                  (assign, "$qst_scout_waypoints_wp_1", -1),
                  (assign, "$qst_scout_waypoints_wp_2", -1),
                  (assign, "$qst_scout_waypoints_wp_3", -1),
                  (assign, ":continue", 0),
                  (try_for_range, ":unused", 0, ":end_cond"),
                    (try_begin),
                      (lt, "$qst_scout_waypoints_wp_1", 0),
                      (call_script, "script_cf_get_random_enemy_center_within_range", ":faction_marshal_party", 50),
                      (assign, "$qst_scout_waypoints_wp_1", reg0),
                    (try_end),
                    (try_begin),
                      (lt, "$qst_scout_waypoints_wp_2", 0),
                      (call_script, "script_cf_get_random_enemy_center_within_range", ":faction_marshal_party", 50),
                      (neq, "$qst_scout_waypoints_wp_1", reg0),
                      (assign, "$qst_scout_waypoints_wp_2", reg0),
                    (try_end),
                    (try_begin),
                      (lt, "$qst_scout_waypoints_wp_3", 0),
                      (call_script, "script_cf_get_random_enemy_center_within_range", ":faction_marshal_party", 50),
                      (neq, "$qst_scout_waypoints_wp_1", reg0),
                      (neq, "$qst_scout_waypoints_wp_2", reg0),
                      (assign, "$qst_scout_waypoints_wp_3", reg0),
                    (try_end),
                    (neq, "$qst_scout_waypoints_wp_1", "$qst_scout_waypoints_wp_2"),
                    (neq, "$qst_scout_waypoints_wp_1", "$qst_scout_waypoints_wp_2"),
                    (neq, "$qst_scout_waypoints_wp_2", "$qst_scout_waypoints_wp_3"),
                    (ge, "$qst_scout_waypoints_wp_1", 0),
                    (ge, "$qst_scout_waypoints_wp_2", 0),
                    (ge, "$qst_scout_waypoints_wp_3", 0),
                    (assign, ":end_cond", 0),
                    (assign, ":continue", 1),
                  (try_end),
                  (eq, ":continue", 1),
                  (assign, "$qst_scout_waypoints_wp_1_visited", 0),
                  (assign, "$qst_scout_waypoints_wp_2_visited", 0),
                  (assign, "$qst_scout_waypoints_wp_3_visited", 0),
                  (assign, ":result", "qst_scout_waypoints"),
                  (quest_set_slot, ":result", slot_quest_expiration_days, 7),
                  (quest_set_slot, ":result", slot_quest_dont_give_again_period, 25),
                (try_end),
              (try_end),
            (try_end),
            
            (try_begin),
              (neq, ":result", -1),
              (quest_set_slot, ":result", slot_quest_current_state, 0),
              (quest_set_slot, ":result", slot_quest_giver_troop, ":faction_marshal"),
              (try_begin),
                (eq, ":result", "qst_join_siege_with_army"),
                (jump_to_menu, "mnu_kingdom_army_quest_join_siege_order"),
              (else_try),
                (assign, "$g_random_army_quest", ":result"),
                (quest_set_slot, "$g_random_army_quest", slot_quest_giver_troop, ":faction_marshal"),
                (jump_to_menu, "mnu_kingdom_army_quest_messenger"),
              (try_end),
            (try_end),
          (try_end),
        (else_try),
          (val_add, "$g_player_follow_army_warnings", 1),
          (try_begin),
            (lt, "$g_player_follow_army_warnings", 15),
            (try_begin),
              (store_mod, ":follow_mod", "$g_player_follow_army_warnings", 3),
              (eq, ":follow_mod", 0),
              (str_store_troop_name_link, s1, ":faction_marshal"),
              (try_begin),
                (lt, "$g_player_follow_army_warnings", 8),
                #             (display_message, "str_marshal_warning"),
              (else_try),
                (display_message, "str_marshal_warning"),
              (try_end),
            (try_end),
          (else_try),
            (jump_to_menu, "mnu_kingdom_army_follow_failed"),
          (try_end),
        (try_end),
    ]),
    
    # Move cattle herd
    (0.5, [(check_quest_active,"qst_move_cattle_herd"),
        (party_slot_eq, "p_main_party", slot_party_on_water, 0),	#VC-2184
        (neg|check_quest_concluded,"qst_move_cattle_herd"),
        (quest_get_slot, ":target_party", "qst_move_cattle_herd", slot_quest_target_party),
        (quest_get_slot, ":target_center", "qst_move_cattle_herd", slot_quest_target_center),
        (store_distance_to_party_from_party, ":dist",":target_party", ":target_center"),
        (lt, ":dist", 3),
        (remove_party, ":target_party"),
        (call_script, "script_succeed_quest", "qst_move_cattle_herd"),
    ]),
    
    (2, [
        (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
          (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
          (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
          (ge, ":party_no", 1),
          (party_is_active, ":party_no"),
          (party_slot_eq, ":party_no", slot_party_following_player, 1),
          (store_current_hours, ":cur_time"),
          (neg|party_slot_ge, ":party_no", slot_party_follow_player_until_time, ":cur_time"),
          (party_set_slot, ":party_no", slot_party_commander_party, -1),
          (party_set_slot, ":party_no", slot_party_following_player, 0),
          (assign,  ":dont_follow_period", 200),
          (store_add, ":dont_follow_time", ":cur_time", ":dont_follow_period"),
          (party_set_slot, ":party_no", slot_party_dont_follow_player_until_time,  ":dont_follow_time"),
        (try_end),
    ]),
    
    # Deliver cattle and deliver cattle to army
    (0.5,
      [
        (try_begin),
          (check_quest_active,"qst_deliver_cattle"),
          (neg|check_quest_succeeded, "qst_deliver_cattle"),
          (quest_get_slot, ":target_center", "qst_deliver_cattle", slot_quest_target_center),
          (quest_get_slot, ":target_amount", "qst_deliver_cattle", slot_quest_target_amount),
          (quest_get_slot, ":cur_amount", "qst_deliver_cattle", slot_quest_current_state),
          (store_sub, ":left_amount", ":target_amount", ":cur_amount"),
          (call_script, "script_remove_cattles_if_herd_is_close_to_party", ":target_center", ":left_amount"),
          (val_add, ":cur_amount", reg0),
          (quest_set_slot, "qst_deliver_cattle", slot_quest_current_state, ":cur_amount"),
          (le, ":target_amount", ":cur_amount"),
          (call_script, "script_succeed_quest", "qst_deliver_cattle"),
        (try_end),
        (try_begin),
          (check_quest_active, "qst_deliver_cattle_to_army"),
          (neg|check_quest_succeeded, "qst_deliver_cattle_to_army"),
          (quest_get_slot, ":giver_troop", "qst_deliver_cattle_to_army", slot_quest_giver_troop),
          (troop_get_slot, ":target_party", ":giver_troop", slot_troop_leaded_party),
          (try_begin),
            (gt, ":target_party", 0),
            (quest_get_slot, ":target_amount", "qst_deliver_cattle_to_army", slot_quest_target_amount),
            (quest_get_slot, ":cur_amount", "qst_deliver_cattle_to_army", slot_quest_current_state),
            (store_sub, ":left_amount", ":target_amount", ":cur_amount"),
            (call_script, "script_remove_cattles_if_herd_is_close_to_party", ":target_party", ":left_amount"),
            (val_add, ":cur_amount", reg0),
            (quest_set_slot, "qst_deliver_cattle_to_army", slot_quest_current_state, ":cur_amount"),
            (try_begin),
              (le, ":target_amount", ":cur_amount"),
              (call_script, "script_succeed_quest", "qst_deliver_cattle_to_army"),
            (try_end),
          (else_try),
            (call_script, "script_abort_quest", "qst_deliver_cattle_to_army", 0),
          (try_end),
        (try_end),
        (try_begin),
          (check_quest_active, "qst_learn_where_merchant_brother_is"), #storyline quest
          (neg|check_quest_succeeded, "qst_learn_where_merchant_brother_is"),
          #phaiak begin
          (try_begin),
            (check_quest_active, "qst_aescesdun"),
            (quest_slot_eq,"qst_aescesdun",slot_quest_current_state, 2),
            (eq, "$player_side", 2), #danish
            (assign, ":target_party", "p_readingum"),
          (else_try),
            (check_quest_active, "qst_aescesdun"),
            (quest_slot_eq,"qst_aescesdun",slot_quest_current_state, 2),
            (eq, "$player_side", 1), #West Seaxe
            (assign, ":target_party", "p_aescesdun"),
          (end_try),
          #phaiak end
          (try_begin),
            (gt, ":target_party", 0),
            (quest_get_slot, ":target_amount", "qst_learn_where_merchant_brother_is", slot_quest_target_amount),
            (quest_get_slot, ":cur_amount", "qst_learn_where_merchant_brother_is", slot_quest_current_state),
            (store_sub, ":left_amount", ":target_amount", ":cur_amount"),
            (call_script, "script_remove_cattles_if_herd_is_close_to_party", ":target_party", ":left_amount"),
            (val_add, ":cur_amount", reg0),
            (quest_set_slot, "qst_learn_where_merchant_brother_is", slot_quest_current_state, ":cur_amount"),
            (try_begin),
              (le, ":target_amount", ":cur_amount"),
              (call_script, "script_succeed_quest", "qst_learn_where_merchant_brother_is"),
            (try_end),
          (else_try),
            (call_script, "script_abort_quest", "qst_learn_where_merchant_brother_is", 0),
          (try_end),
        (try_end),
    ]),
    
    #STrig 90
    # Train peasants against bandits
    (1,
      [
        (neg|map_free),
        (check_quest_active, "qst_train_peasants_against_bandits"),
        (neg|check_quest_concluded, "qst_train_peasants_against_bandits"),
        (eq, "$qst_train_peasants_against_bandits_currently_training", 1),
        (val_add, "$qst_train_peasants_against_bandits_num_hours_trained", 1),
        (call_script, "script_get_max_skill_of_player_party", "skl_trainer"),
        (assign, ":trainer_skill", reg0),
        (store_sub, ":needed_hours", 20, ":trainer_skill"),
        (val_mul, ":needed_hours", 3),
        (val_div, ":needed_hours", 5),
        (ge, "$qst_train_peasants_against_bandits_num_hours_trained", ":needed_hours"),
        (assign, "$qst_train_peasants_against_bandits_num_hours_trained", 0),
        (rest_for_hours, 0, 0, 0), #stop resting
        (jump_to_menu, "mnu_train_peasants_against_bandits_ready"),
    ]),
    
    # Scout waypoints
    (1,
      [
        (check_quest_active,"qst_scout_waypoints"),
        (neg|check_quest_succeeded, "qst_scout_waypoints"),
        (try_begin),
          (eq, "$qst_scout_waypoints_wp_1_visited", 0),
          (store_distance_to_party_from_party, ":distance", "$qst_scout_waypoints_wp_1", "p_main_party"),
          (le, ":distance", 3),
          (assign, "$qst_scout_waypoints_wp_1_visited", 1),
          (str_store_party_name_link, s1, "$qst_scout_waypoints_wp_1"),
          (display_message, "@{s1} is scouted."),
        (try_end),
        (try_begin),
          (eq, "$qst_scout_waypoints_wp_2_visited", 0),
          (store_distance_to_party_from_party, ":distance", "$qst_scout_waypoints_wp_2", "p_main_party"),
          (le, ":distance", 3),
          (assign, "$qst_scout_waypoints_wp_2_visited", 1),
          (str_store_party_name_link, s1, "$qst_scout_waypoints_wp_2"),
          (display_message, "@{s1} is scouted."),
        (try_end),
        (try_begin),
          (eq, "$qst_scout_waypoints_wp_3_visited", 0),
          (store_distance_to_party_from_party, ":distance", "$qst_scout_waypoints_wp_3", "p_main_party"),
          (le, ":distance", 3),
          (assign, "$qst_scout_waypoints_wp_3_visited", 1),
          (str_store_party_name_link, s1, "$qst_scout_waypoints_wp_3"),
          (display_message, "@{s1} is scouted."),
        (try_end),
        (eq, "$qst_scout_waypoints_wp_1_visited", 1),
        (eq, "$qst_scout_waypoints_wp_2_visited", 1),
        (eq, "$qst_scout_waypoints_wp_3_visited", 1),
        (call_script, "script_succeed_quest", "qst_scout_waypoints"),
    ]),
    
    # Kill local merchant
    
    (3, [(neg|map_free),
        (check_quest_active, "qst_kill_local_merchant"),
        (quest_slot_eq, "qst_kill_local_merchant", slot_quest_current_state, 0),
        (quest_set_slot, "qst_kill_local_merchant", slot_quest_current_state, 1),
        (rest_for_hours, 0, 0, 0), #stop resting
        (assign, "$auto_enter_town", "$qst_kill_local_merchant_center"),
        (assign, "$quest_auto_menu", "mnu_kill_local_merchant_begin"),
    ]),
    
    # Collect taxes
    (1, [(neg|map_free),
        (check_quest_active, "qst_collect_taxes"),
        (eq, "$g_player_is_captive", 0),
        (eq, "$qst_collect_taxes_currently_collecting", 1),
        (quest_get_slot, ":quest_current_state", "qst_collect_taxes", slot_quest_current_state),
        (this_or_next|eq, ":quest_current_state", 1),
        (this_or_next|eq, ":quest_current_state", 2),
        (eq, ":quest_current_state", 3),
        (quest_get_slot, ":left_hours", "qst_collect_taxes", slot_quest_target_amount),
        (val_sub, ":left_hours", 1),
        (quest_set_slot, "qst_collect_taxes", slot_quest_target_amount, ":left_hours"),
        (store_skill_level, ":persuasion", "skl_persuasion", "trp_player"),
        (store_attribute_level, ":strength", "trp_player", ca_strength),
        (store_skill_level, ":power_strike", "skl_power_strike", "trp_player"),
        #      (call_script, "script_get_max_skill_of_player_party", "skl_trade"),
        (val_div, ":strength", 2),
        (val_sub, ":persuasion", 5),
        (store_add, ":mod", ":strength", ":persuasion"),
        (val_add, ":mod", ":power_strike"),
        (try_begin),
          (lt, ":left_hours", 0),
          (assign, ":quest_current_state", 4),
          (quest_set_slot, "qst_collect_taxes", slot_quest_current_state, 4),
          (rest_for_hours, 0, 0, 0), #stop resting
          (jump_to_menu, "mnu_collect_taxes_complete"),
        (else_try),
          #Continue collecting taxes
          (assign, ":max_collected_tax", "$qst_collect_taxes_hourly_income"),
          (party_get_slot, ":prosperity", "$g_encountered_party", slot_town_prosperity),
          (store_add, ":multiplier", 30, ":prosperity"),
          (val_mul, ":max_collected_tax", ":multiplier"),
          (val_div, ":max_collected_tax", 80),#Prosperity of 50 gives the default values
          
          (try_begin),
            (eq, "$qst_collect_taxes_halve_taxes", 1),
            (val_div, ":max_collected_tax", 2),
          (try_end),
          (val_max, ":max_collected_tax", 2),
          (store_random_in_range, ":collected_tax", 1, ":max_collected_tax"),
          (quest_get_slot, ":cur_collected", "qst_collect_taxes", slot_quest_gold_reward),
          (val_add, ":cur_collected", ":collected_tax"),
          (quest_set_slot, "qst_collect_taxes", slot_quest_gold_reward, ":cur_collected"),
          (call_script, "script_troop_add_gold", "trp_player", ":collected_tax"),
        (try_end),
        (try_begin),
          (eq, ":quest_current_state", 1),
          (assign, "$temp", 0),
          (assign, "$temp2", 0),
          (val_sub, "$qst_collect_taxes_menu_counter", 1),
          (le, "$qst_collect_taxes_menu_counter", 0),
          (quest_set_slot, "qst_collect_taxes", slot_quest_current_state, 2),
          (jump_to_menu, "mnu_collect_taxes_revolt_warning"),
        (else_try), #Chance of revolt against player
          (eq, ":quest_current_state", 2),
          (val_sub, "$qst_collect_taxes_unrest_counter", 1),
          (try_begin),
            (le, "$qst_collect_taxes_unrest_counter", 0),
            (eq, "$qst_collect_taxes_halve_taxes", 0),
            (quest_set_slot, "qst_collect_taxes", slot_quest_current_state, 3),
          (try_end),
          
          (store_div, ":unrest_chance", 10000, "$qst_collect_taxes_total_hours"),
          (val_add, ":unrest_chance",30),
          (val_sub, ":unrest_chance", ":mod"),
          (store_random_in_range, ":unrest_roll", "$temp", 2000),
          (val_add, "$temp",":mod"),
          (try_begin),
            (lt, ":unrest_roll", ":unrest_chance"),
            (jump_to_menu, "mnu_collect_taxes_revolt"),
            (val_add, "$temp2", 1),
          (try_end),
        (try_end),
    ]),
    
    #persuade_lords_to_make_peace begin
    (72, [(gt, "$g_force_peace_faction_1", 0),
        (gt, "$g_force_peace_faction_2", 0),
        (try_begin),
          (store_relation, ":relation", "$g_force_peace_faction_1", "$g_force_peace_faction_2"),
          (lt, ":relation", 0),
          (call_script, "script_diplomacy_start_peace_between_kingdoms", "$g_force_peace_faction_1", "$g_force_peace_faction_2", 1),
        (try_end),
        (assign, "$g_force_peace_faction_1", 0),
        (assign, "$g_force_peace_faction_2", 0),
    ]),
    
    #NPC changes begin
    #Resolve one issue each hour
    (1, [
        (try_begin),
          (eq, "$g_infinite_camping", 0),
          (str_store_string, s51, "str_no_trigger_noted"),
          (try_begin),
            (gt, "$npc_to_rejoin_party", 0),
            (try_begin),
              (neg|main_party_has_troop, "$npc_to_rejoin_party"),
              (neq, "$g_player_is_captive", 1),
              (str_store_string, s51, "str_triggered_by_npc_to_rejoin_party"),
              (assign, "$npc_map_talk_context", slot_troop_days_on_mission),
              (start_map_conversation, "$npc_to_rejoin_party", -1),
            (else_try),
              (troop_set_slot, "$npc_to_rejoin_party", slot_troop_current_mission, npc_mission_rejoin_when_possible),
              (assign, "$npc_to_rejoin_party", 0),
            (try_end),
            # Here do NPC that is quitting
          (else_try),
            (gt, "$npc_is_quitting", 0),
            (try_begin),
              (main_party_has_troop, "$npc_is_quitting"),
              (neq, "$g_player_is_captive", 1),
              (str_store_string, s51, "str_triggered_by_npc_is_quitting"),
              (start_map_conversation, "$npc_is_quitting", -1),
            (else_try),
              (assign, "$npc_is_quitting", 0),
            (try_end),
            #NPC with grievance
          (else_try), #### Grievance
            (gt, "$npc_with_grievance", 0),
            (eq, "$disable_npc_complaints", 0),
            (try_begin),
              (main_party_has_troop, "$npc_with_grievance"),
              (neq, "$g_player_is_captive", 1),
              (str_store_string, s51, "str_triggered_by_npc_has_grievance"),
              (assign, "$npc_map_talk_context", slot_troop_morality_state),
              (start_map_conversation, "$npc_with_grievance", -1),
            (else_try),
              (assign, "$npc_with_grievance", 0),
            (try_end),
          (else_try),
            (gt, "$npc_with_personality_clash", 0),
            (eq, "$disable_npc_complaints", 0),
            (troop_get_slot, ":object", "$npc_with_personality_clash", slot_troop_personalityclash_object),
            (try_begin),
              (main_party_has_troop, "$npc_with_personality_clash"),
              (main_party_has_troop, ":object"),
              (neq, "$g_player_is_captive", 1),
              
              (assign, "$npc_map_talk_context", slot_troop_personalityclash_state),
              (str_store_string, s51, "str_triggered_by_npc_has_personality_clash"),
              (start_map_conversation, "$npc_with_personality_clash", -1),
            (else_try),
              (assign, "$npc_with_personality_clash", 0),
            (try_end),
          (else_try), #### Political issue
            (assign, "$npc_with_political_grievance", 0), #dialogs all wrong; disable
            (gt, "$npc_with_political_grievance", 0),
            (eq, "$disable_npc_complaints", 0),
            (try_begin),
              (main_party_has_troop, "$npc_with_political_grievance"),
              (neq, "$g_player_is_captive", 1),
              
              (str_store_string, s51, "str_triggered_by_npc_has_political_grievance"),
              (assign, "$npc_map_talk_context", slot_troop_kingsupport_objection_state),
              (start_map_conversation, "$npc_with_political_grievance", -1),
            (else_try),
              (assign, "$npc_with_political_grievance", 0),
            (try_end),
          (else_try),
            (eq, "$disable_sisterly_advice", 0),
            (gt, "$npc_with_sisterly_advice", 0),
            (try_begin),
              (main_party_has_troop, "$npc_with_sisterly_advice"),
              (neq, "$g_player_is_captive", 1),
              
              (assign, "$npc_map_talk_context", slot_troop_woman_to_woman_string), #was npc_with_sisterly advice
              (start_map_conversation, "$npc_with_sisterly_advice", -1),
            (else_try),
              (assign, "$npc_with_sisterly_advice", 0),
            (try_end),
          (else_try), #check for regional background
            (eq, "$disable_local_histories", 0),
            (try_for_range, ":npc", companions_begin, companions_end),
              (main_party_has_troop, ":npc"),
              (troop_slot_eq, ":npc", slot_troop_home_speech_delivered, 0),
              (troop_get_slot, ":home", ":npc", slot_troop_home),
              (gt, ":home", 0),
              (store_distance_to_party_from_party, ":distance", ":home", "p_main_party"),
              (lt, ":distance", 7),
              (assign, "$npc_map_talk_context", slot_troop_home),
              
              (str_store_string, s51, "str_triggered_by_local_histories"),
              
              (start_map_conversation, ":npc", -1),
            (try_end),
          (try_end),
        (try_end),
        
        #add pretender to party if not active
        (try_begin),
          (check_quest_active, "qst_rebel_against_kingdom"),
          (is_between, "$supported_pretender", pretenders_begin, pretenders_end),
          (neg|main_party_has_troop, "$supported_pretender"),
          (neg|troop_slot_eq, "$supported_pretender", slot_troop_occupation, slto_kingdom_hero),
          (party_add_members, "p_main_party", "$supported_pretender", 1),
        (try_end),
        
        #make player marshal of rebel faction
        (try_begin),
          (check_quest_active, "qst_rebel_against_kingdom"),
          (is_between, "$supported_pretender", pretenders_begin, pretenders_end),
          (main_party_has_troop, "$supported_pretender"),
          (neg|faction_slot_eq, "fac_player_supporters_faction", slot_faction_marshal, "trp_player"),
          (call_script, "script_appoint_faction_marshal", "fac_player_supporters_faction", "trp_player"),
        (try_end),
    ]),
    #NPC changes end
    
    (25, [
        (assign, ":last_lord", active_npcs_end),
        (try_for_range, ":troop_no", active_npcs_begin, ":last_lord"),
          (troop_slot_ge, ":troop_no", slot_troop_change_to_faction, 1),
          (store_troop_faction, ":faction_no", ":troop_no"),
          (troop_get_slot, ":new_faction_no", ":troop_no", slot_troop_change_to_faction),
          (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
          (assign, ":continue", 0),
          (try_begin),
            (le, ":party_no", 0),
            #(troop_slot_eq, ":troop_no", slot_troop_is_prisoner, 0),
            (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
            (assign, ":continue", 1),
          (else_try),
            (gt, ":party_no", 0),
            
            #checking if the party is outside the centers
            (party_get_attached_to, ":cur_center_no", ":party_no"),
            (try_begin),
              (lt, ":cur_center_no", 0),
              (party_get_cur_town, ":cur_center_no", ":party_no"),
            (try_end),
            (this_or_next|neg|is_between, ":cur_center_no", centers_begin, centers_end),
            (party_slot_eq, ":cur_center_no", slot_town_lord, ":troop_no"),
            
            #checking if the party is away from his original faction parties
            (assign, ":end_cond", active_npcs_end),
            (try_for_range, ":enemy_troop_no", active_npcs_begin, ":end_cond"),
              (troop_slot_eq, ":enemy_troop_no", slot_troop_occupation, slto_kingdom_hero),
              ## bugfix - must not include himself moto chief
              (neq, ":enemy_troop_no", ":troop_no"),
              ## bugfix
              (troop_get_slot, ":enemy_party_no", ":enemy_troop_no", slot_troop_leaded_party),
              (party_is_active, ":enemy_party_no"),
              (store_faction_of_party, ":enemy_faction_no", ":enemy_party_no"),
              (eq, ":enemy_faction_no", ":faction_no"),
              (store_distance_to_party_from_party, ":dist", ":party_no", ":enemy_party_no"),
              (lt, ":dist", 4),
              (assign, ":end_cond", 0),
            (try_end),
            (neq, ":end_cond", 0),
            (assign, ":continue", 1),
          (try_end),
          (eq, ":continue", 1),
          
          (try_begin),
            (ge, "$cheat_mode", 1),
            (str_store_troop_name, s4, ":troop_no"),
            (display_message, "@{!}DEBUG - {s4} faction changed from slot_troop_change_to_faction"),
          (try_end),
          
          (call_script, "script_change_troop_faction", ":troop_no", ":new_faction_no"),
          (troop_set_slot, ":troop_no", slot_troop_change_to_faction, 0),
          (assign, "$g_recalculate_ais", 1),
          
          (assign, ":faction_under_attack", 0),
          (try_for_range, ":cur_center_no", walled_centers_begin, walled_centers_end),
            (store_faction_of_party, ":center_faction", ":cur_center_no"),
            (eq, ":center_faction", ":new_faction_no"),
            (party_slot_ge, ":center_faction", slot_center_is_besieged_by, 0),
            (assign, ":faction_under_attack", 1),
          (try_end),
          (try_begin),
            (eq, ":faction_under_attack", 0), #existence of faction not threatened?
            (assign, ":last_lord", ":troop_no"),  #wait to bring in rest of lords (break loop)
          (try_end),
          
          (try_begin),
            (is_between, ":new_faction_no", kingdoms_begin, kingdoms_end),
            (str_store_troop_name_link, s1, ":troop_no"),
            (str_store_faction_name_link, s2, ":faction_no"),
            (str_store_faction_name_link, s3, ":new_faction_no"),
            (try_begin),
              (eq, ":faction_no", "$players_kingdom"),
              (call_script, "script_add_notification_menu", "mnu_notification_troop_left_players_faction", ":troop_no", ":new_faction_no"),
              (display_message, "@{s1} has switched from the {s2} to the {s3}."),
            (else_try),
              (eq, ":new_faction_no", "$players_kingdom"),
              (call_script, "script_add_notification_menu", "mnu_notification_troop_joined_players_faction", ":troop_no", ":faction_no"),
              (display_message, "@{s1} has switched from the {s2} to the {s3}."),
            (try_end),
          (try_end),
        (try_end),
    ]),
    
    
    (1,
      [
        (eq, "$cheat_mode", 1),
        (try_for_range, ":center_no", centers_begin, centers_end),
          (party_get_battle_opponent, ":besieger_party", ":center_no"),
          (try_begin),
            (gt, ":besieger_party", 0),
            (str_store_party_name, s2, ":center_no"),
            (str_store_party_name, s3, ":besieger_party"),
            (display_message, "@{!}DEBUG : {s2} is besieged by {s3}"),
          (try_end),
        (try_end),
    ]),
    
    (1,
      [
        (store_current_day, ":cur_day"),
        (gt, ":cur_day", "$g_last_report_control_day"),
        (store_time_of_day, ":cur_hour"),
        (ge, ":cur_hour", 18),
        
        (store_random_in_range, ":rand_no", 0, 4),
        (this_or_next|ge, ":cur_hour", 22),
        (eq, ":rand_no", 0),
        
        (assign, "$g_last_report_control_day", ":cur_day"),
        
        (store_troop_gold, ":gold", "trp_player"),
        
        (try_begin),
          (lt, ":gold", 0),
          (store_sub, ":gold_difference", 0, ":gold"),
          (troop_add_gold, "trp_player", ":gold_difference"),
        (try_end),
        
        (party_get_morale, ":troop_morale", "p_main_party"),
        
        #(assign, ":swadian_soldiers_are_upset_message_showed", 0),
        #(assign, ":vaegir_soldiers_are_upset_message_showed", 0),
        #(assign, ":khergit_soldiers_are_upset_message_showed", 0),
        #(assign, ":nord_soldiers_are_upset_message_showed", 0),
        #(assign, ":rhodok_soldiers_are_upset_message_showed", 0),
        
        #Reset number of votes
        (try_for_range, ":soldier", soldiers_begin, soldiers_end),
          (troop_set_slot, ":soldier", slot_troop_temp_slot, 0),
        (try_end),
        
        (try_begin),
          (str_store_string, s1, "str_party_morale_is_low"),
          (str_clear, s2),
          (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
          (assign, ":num_deserters_total", 0),
          (try_for_range_backwards, ":i_stack", 0, ":num_stacks"),
            (party_stack_get_troop_id, ":stack_troop", "p_main_party", ":i_stack"),
            (neg|troop_is_hero, ":stack_troop"),
            (party_stack_get_size, ":stack_size", "p_main_party", ":i_stack"),
            (store_troop_faction, ":faction_no", ":stack_troop"),
            (try_begin),
              (is_between, ":faction_no", npc_kingdoms_begin, npc_kingdoms_end),
              (faction_get_slot, ":troop_morale_addition", ":faction_no",  slot_faction_morale_of_player_troops),
              (val_div, ":troop_morale_addition", 100),
              (val_add, ":troop_morale", ":troop_morale_addition"),
            (try_end),
            (lt, ":troop_morale", 32),
            (store_sub, ":desert_prob", 36, ":troop_morale"),
            (val_div, ":desert_prob", 4),
            (assign, ":num_deserters_from_that_troop", 0),
            (try_for_range, ":unused", 0, ":stack_size"),
              (store_random_in_range, ":rand_no", 0, 100),
              (lt, ":rand_no", ":desert_prob"),
              (val_add, ":num_deserters_from_that_troop", 1),
              #p.remove_members_from_stack(i_stack,cur_deserters, &main_party_instances);
              (party_slot_eq, "p_main_party", slot_party_on_water, 0),		#quick fix: no deserters on water (phaiak) #Maybe adding chance for mutiny later
              (remove_member_from_party, ":stack_troop", "p_main_party"),
            (try_end),
            (try_begin),
              (ge, ":num_deserters_from_that_troop", 1),
              (str_store_troop_name, s2, ":stack_troop"),
              (assign, reg0, ":num_deserters_from_that_troop"),
              (try_begin),
                (ge, ":num_deserters_total", 1),
                (str_store_string, s1, "str_s1_reg0_s2"),
              (else_try),
                (str_store_string, s3, s1),
                (str_store_string, s1, "str_s3_reg0_s2"),
              (try_end),
              (val_add, ":num_deserters_total", ":num_deserters_from_that_troop"),
              (troop_set_slot, ":stack_troop", slot_troop_temp_slot, ":num_deserters_from_that_troop"),
            (try_end),
          (try_end),
          
          (try_begin),
            (ge, ":num_deserters_total", 1),
            (try_begin),
              (ge, ":num_deserters_total", 2),
              (str_store_string, s2, "str_have_deserted_the_party"),
            (else_try),
              (str_store_string, s2, "str_has_deserted_the_party"),
            (try_end),
            (str_store_string, s1, "str_s1_s2"),
            (eq, "$g_infinite_camping", 0),
            # new changes for VC-1605:
            (try_begin),
              (party_slot_eq, "p_main_party", slot_party_on_water, 0),
              (tutorial_box, s1, "str_weekly_report"),
            (else_try),
              (party_slot_eq, "p_main_party", slot_party_on_water, 1),
              (jump_to_menu, "mnu_mutiny_start"),
            (try_end),
          (try_end),
        (try_end),
    ]),
    # reserved for future use. For backward compatibility, we need to use these triggers instead of creating new ones.
    
    (.27,	#castles 24 hours ON AVERAGE
      [
        (store_random_in_range, ":cur_castle", castles_begin, castles_end),
        (neg|party_slot_ge, ":cur_castle", slot_center_blockaded, 2),    #center not blockaded (by player) AND
        (neg|party_slot_ge, ":cur_castle", slot_center_is_besieged_by, 1), #center not besieged by someone else
        (call_script, "script_calculate_castle_prosperities_by_using_its_villages", ":cur_castle", 0),
        (party_get_slot, ":food_stores", ":cur_castle", slot_party_food_store),
        (call_script, "script_center_get_food_store_limit", ":cur_castle"),
        (val_min, ":food_stores", reg0),
        (party_set_slot, ":cur_castle", slot_party_food_store, ":food_stores"),
    ]),
    
    #STrig 100
    (1,			#Trigger no 100 if I counted correct
      [
        (try_begin),
          (eq, "$g_player_is_captive", 1),
          (neg|party_is_active, "$capturer_party"),
          (eq, "$travel_town", 0),	# phaiak fixing VC-1237
          (rest_for_hours, 0, 0, 0),
        (try_end),
        
        ##moto chief begin
        #seems to be a native bug
        (is_between, "$next_center_will_be_fired", villages_begin, villages_end),
        ##moto end
        (assign, ":village_no", "$next_center_will_be_fired"),
        (party_get_slot, ":is_there_already_fire", ":village_no", slot_village_smoke_added),
        (eq, ":is_there_already_fire", 0),
        
        
        (try_begin),
          (party_get_slot, ":bound_center", ":village_no", slot_village_bound_center),
          (party_get_slot, ":last_nearby_fire_time", ":bound_center", slot_town_last_nearby_fire_time),
          (store_current_hours, ":cur_hours"),
          
          (try_begin),
            (eq, "$cheat_mode", 1),
            (is_between, ":village_no", centers_begin, centers_end),
            (is_between, ":bound_center", centers_begin, centers_end),
            (str_store_party_name, s4, ":village_no"),
            (str_store_party_name, s5, ":bound_center"),
            (store_current_hours, reg3),
            (party_get_slot, reg4, ":bound_center", slot_town_last_nearby_fire_time),
            (display_message, "@{!}DEBUG - Checking fire at {s4} for {s5} - current time {reg3}, last nearby fire {reg4}"),
          (try_end),
          
          
          (eq, ":cur_hours", ":last_nearby_fire_time"),
          (party_add_particle_system, ":village_no", "psys_map_village_fire"),
          (party_add_particle_system, ":village_no", "psys_map_village_fire_smoke"),
        (else_try),
          (store_add, ":last_nearby_fire_finish_time", ":last_nearby_fire_time", fire_duration),
          (eq, ":last_nearby_fire_finish_time", ":cur_hours"),
          (party_clear_particle_systems, ":village_no"),
        (try_end),
        
        
    ]),
    
    (24,
      [
        (val_sub, "$g_dont_give_fief_to_player_days", 1),
        (val_max, "$g_dont_give_fief_to_player_days", -1),
        (val_sub, "$g_dont_give_marshalship_to_player_days", 1),
        (val_max, "$g_dont_give_marshalship_to_player_days", -1),
        
        
        #this to correct linen production at villages of durquba
        (party_set_slot, "p_village_93", slot_center_linen_looms, 0), #mazigh
        (party_set_slot, "p_village_94", slot_center_linen_looms, 0), #sekhtem
        (party_set_slot, "p_village_95", slot_center_linen_looms, 0), #qalyut
        (party_set_slot, "p_village_96", slot_center_linen_looms, 0), #tilimsal
        (party_set_slot, "p_village_97", slot_center_linen_looms, 0), #shibal zumr
        (party_set_slot, "p_village_102", slot_center_linen_looms, 0), #tamnuh
        (party_set_slot, "p_village_109", slot_center_linen_looms, 0), #habba
        
        (party_set_slot, "p_village_67", slot_center_fishing_fleet, 0), #Tebandra
        #  (party_set_slot, "p_village_5", slot_center_fishing_fleet, 15), #Kulum
        
        
        #The following scripts are to end quests which should have cancelled, but did not because of a bug
        (try_begin),
          (check_quest_active, "qst_formal_marriage_proposal"),
          (check_quest_failed, "qst_formal_marriage_proposal"),
          (call_script, "script_end_quest", "qst_formal_marriage_proposal"),
        (try_end),
        
        (try_begin),
          (check_quest_active, "qst_lend_companion"),
          (quest_get_slot, ":giver_troop", "qst_lend_companion", slot_quest_giver_troop),
          (store_faction_of_troop, ":giver_troop_faction", ":giver_troop"),
          (store_relation, ":faction_relation", ":giver_troop_faction", "$players_kingdom"),
          (this_or_next|lt, ":faction_relation", 0),
          (neg|is_between, ":giver_troop_faction", kingdoms_begin, kingdoms_end),
          (call_script, "script_abort_quest", "qst_lend_companion", 0),
        (try_end),
        
        
        
        (try_begin),
          (is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
          (neq, "$players_kingdom", "fac_player_supporters_faction"),
          (faction_slot_eq, "$players_kingdom", slot_faction_marshal, "trp_player"),
          (val_add, "$g_player_days_as_marshal", 1),
        (else_try),
          (assign, "$g_player_days_as_marshal", 0),
        (try_end),
        
        (try_for_range, ":town", towns_begin, towns_end),
          (party_get_slot, ":days_to_completion", ":town", slot_center_player_enterprise_days_until_complete),
          (ge, ":days_to_completion", 1),
          (val_sub, ":days_to_completion", 1),
          (party_set_slot, ":town", slot_center_player_enterprise_days_until_complete, ":days_to_completion"),
        (try_end),
    ]),
    (24,
      [
        # Setting food bonuses in every 6 hours again and again because of a bug (we could not find its reason) which decreases especially slot_item_food_bonus slots of items to 0.
        #Staples
        (item_set_slot, "itm_bread", slot_item_food_bonus, 8), #brought up from 4
        (item_set_slot, "itm_grain", slot_item_food_bonus, 2), #new - can be boiled as porridge
        
        #Fat sources - preserved
        (item_set_slot, "itm_smoked_fish", slot_item_food_bonus, 4),
        (item_set_slot, "itm_dried_meat", slot_item_food_bonus, 5),
        (item_set_slot, "itm_cheese", slot_item_food_bonus, 5),
        (item_set_slot, "itm_sausages", slot_item_food_bonus, 5),
        (item_set_slot, "itm_butter", slot_item_food_bonus, 4), #brought down from 8
        
        #Fat sources - perishable
        (item_set_slot, "itm_chicken", slot_item_food_bonus, 8), #brought up from 7
        (item_set_slot, "itm_cattle_meat", slot_item_food_bonus, 7), #brought down from 7
        (item_set_slot, "itm_pork", slot_item_food_bonus, 6), #brought down from 6
        
        #Produce
        #(item_set_slot, "itm_raw_olives", slot_item_food_bonus, 1),
        (item_set_slot, "itm_cabbages", slot_item_food_bonus, 2),
        (item_set_slot, "itm_barley", slot_item_food_bonus, 3),
        (item_set_slot, "itm_apples", slot_item_food_bonus, 4), #brought down from 5
        
        #Sweet items
        #(item_set_slot, "itm_soapstone", slot_item_food_bonus, 4), #brought down from 8
        (item_set_slot, "itm_vc_honey", slot_item_food_bonus, 6), #brought down from 12
        
        (item_set_slot, "itm_wine", slot_item_food_bonus, 5),
        (item_set_slot, "itm_ale", slot_item_food_bonus, 4),
    ]),
    #SEA BATTLES chief
    #SEA BATTLES chief
    #(.2, [    #trigger rewritten by motomataru
    # (party_get_current_terrain, ":terrain", "p_main_party"),
    # (store_party_size_wo_prisoners, ":party_size", "p_main_party"),
    
    # #player icon state and other considerations...
    # (try_begin),
    # (neq, ":terrain", rt_water),
    # (neq, ":terrain", rt_river),
    # (neq, ":terrain", rt_bridge),    #not rt_bridge used as water terrain
    # (try_begin),
    # (neq, "$sea_clock", 0),
    # (assign, "$g_player_icon_state", pis_normal),
    # (try_begin),
    # (gt, ":party_size", 1),
    # (display_message, "@Back on solid ground, out of reach of swells and sea monsters, your men seem more relaxed."),
    # (call_script, "script_change_player_party_morale", "$sea_morale_penalty"),
    # (else_try),
    # (set_show_messages, 0),
    # (call_script, "script_change_player_party_morale", "$sea_morale_penalty"),
    # (set_show_messages, 1),
    # (try_end),
    # (assign, "$sea_morale_penalty", 0),
    # (assign, "$ship_rented", 0),
    # (assign, "$sea_clock", 0),
    # (try_end),
    
    # (else_try),    #water terrain
    # (neq, "$g_player_is_captive", 1),
    # (store_troop_gold, ":money", "trp_player"),
    # (try_begin),
    # (eq, "$g_player_icon_state", pis_normal),
    # (assign, "$g_player_icon_state", pis_ship),
    # (gt, ":money", 9),
    # (display_message, "@You hire a nearby boat for the trip."),
    # (assign, "$ship_rented", 1),
    # (try_end),
    
    # (try_begin),
    # (eq, "$sea_clock", 0),
    # (gt, ":party_size", 1),
    # (display_message, "@Your men are uneasy about crossing the ocean and start losing heart."),
    # (try_end),
    
    # (store_mod, ":sea_tick", "$sea_clock", 5),
    # (try_begin),
    # (eq, ":sea_tick", 0),    #once per second...
    # (try_begin),
    # (gt, ":party_size", 1),
    # (call_script, "script_change_player_party_morale", -1),
    # (val_add, "$sea_morale_penalty", 1),
    # (try_end),
    
    # #ship rental
    # (eq, "$ship_rented", 1),
    # (try_begin),
    # (store_party_size, ":rental_rate",      "p_main_party"),
    # (ge, ":money", ":rental_rate"),
    # (troop_remove_gold, "trp_player", ":rental_rate"),
    # ##               (gt, ":money", 59),
    # ##               (troop_remove_gold, "trp_player", 60),
    # (call_script, "script_change_player_party_morale", -1),
    # (else_try),
    # (try_begin),
    # (eq, "$sea_clock", 0),
    # (display_message, "@Lacking money, you commandeer a nearby boat."),
    # (else_try),
    # (display_message, "@Running out of money, you force the boat to continue your voyage."),
    # (try_end),
    # (call_script, "script_change_player_honor", -2),
    # (call_script, "script_change_player_party_morale", -2),
    # (assign, "$ship_rented", 0),
    # (try_end),
    # (try_end),
    
    # (val_add, "$sea_clock", 1),
    # (try_end),
    
    #other party icons
    # (try_for_parties, ":cur_party"),
    # (neq, ":cur_party", "p_main_party"),
    # (party_get_template_id, ":cur_template", ":cur_party"),
    # (party_get_icon, ":cur_icon", ":cur_party"),
    # (party_get_current_terrain, ":terrain", ":cur_party"),
    # (try_begin),
    # (this_or_next|eq, ":terrain", rt_water),
    # (this_or_next|eq, ":terrain", rt_river),
    # (eq, ":terrain", rt_bridge),	#rt_bridge used as water terrain
    # (try_begin),
    # (neq, ":cur_icon", "icon_ship"),
    # (neq, ":cur_icon", "icon_castle_snow_a"),
    # (party_set_slot, ":cur_party", slot_party_save_icon, ":cur_icon"),
    # (try_begin),
    # ##					(neq, ":cur_template", "pt_deer_herd"),
    # ##					(neq, ":cur_template", "pt_boar_herd"),
    # ##					(neq, ":cur_template", "pt_wolf_herd"),
    # ##					(neq, ":cur_template", "pt_coat_herd"),
    # ##					(neq, ":cur_template", "pt_coatb_herd"),
    # ##					(neq, ":cur_template", "pt_wilddonkey_herd"),
    # (party_set_icon, ":cur_party", "icon_ship"),
    # (else_try),	#exception for wild animals
    # (party_set_icon, ":cur_party", "icon_castle_snow_a"),	#???
    # (try_end),
    
    # (this_or_next|eq, ":cur_template", "pt_sea_raiders_ships"),	#in case ships had "leaked" onto land
    # (this_or_next|eq, ":cur_template", "pt_sea_raiders_ships2"),
    # (eq, ":cur_template", "pt_sea_raiders_ships3"),
    # (party_set_flags, ":cur_party", pf_is_ship, 1),
    # (try_end),
    
    # #not water terrain
    # (else_try),
    # (neq, ":cur_template", "pt_sea_raiders_ships"),	#hope these guys get in the water! Problem is they spawn on land...
    # (neq, ":cur_template", "pt_sea_raiders_ships2"),
    # (neq, ":cur_template", "pt_sea_raiders_ships3"),
    
    # (this_or_next|eq, ":cur_icon", "icon_castle_snow_a"),	#exception for wild animals
    # (eq, ":cur_icon", "icon_ship"),
    # (try_begin),
    # ##				(eq, ":cur_template", "pt_sea_traders"),
    # ##				(party_set_icon, ":cur_party", "icon_gray_knight"),
    # ##				(party_set_flags, ":cur_party", pf_is_ship, 0),
    # ##			(else_try),
    # (party_get_slot, ":new_icon", ":cur_party", slot_party_save_icon),
    # (party_set_icon, ":cur_party", ":new_icon"),
    # (try_end),
    
    # (try_end),
    # (try_end),	#try_for_parties
    
    
    # (try_for_parties, ":party_no"),
    # (party_get_current_terrain, ":terrain", ":party_no"),
    # (call_script, "script_party_count_members_with_full_health", ":party_no"),
    # (assign, ":party_size", reg0),
    # (try_begin),
    ##lord parties iconos per size
    # (party_slot_eq, ":party_no", slot_party_type, spt_kingdom_hero_party),
    # (try_begin),
    ##on land
    # (neq, ":terrain", rt_water),
    # (neq, ":terrain", rt_river),
    # (neq, ":terrain", rt_bridge),    #not rt_bridge used as water terrain
    # (try_begin),
    # (ge, ":party_size", 300),
    # (party_set_icon, ":party_no", "icon_lords_10"),
    # (else_try),
    # (ge, ":party_size", 260),
    # (party_set_icon, ":party_no", "icon_lords_9"),
    # (else_try),
    # (ge, ":party_size", 210),
    # (party_set_icon, ":party_no", "icon_lords_8"),
    # (else_try),
    # (ge, ":party_size", 180),
    # (party_set_icon, ":party_no", "icon_lords_7"),
    # (else_try),
    # (ge, ":party_size", 150),
    # (party_set_icon, ":party_no", "icon_lords_6"),
    # (else_try),
    # (ge, ":party_size", 120),
    # (party_set_icon, ":party_no", "icon_lords_5"),
    # (else_try),
    # (ge, ":party_size", 90),
    # (party_set_icon, ":party_no", "icon_lords_4"),
    # (else_try),
    # (ge, ":party_size", 60),
    # (party_set_icon, ":party_no", "icon_lords_3"),
    # (else_try),
    # (ge, ":party_size", 30),
    # (party_set_icon, ":party_no", "icon_lords_2"),
    # (else_try),
    # (party_set_icon, ":party_no", "icon_lords_1"),
    # (try_end),
    # (else_try),
    ##on water
    # (try_begin),
    # (ge, ":party_size", 300),
    # (party_set_icon, ":party_no", "icon_ships_7"),
    # (else_try),
    # (ge, ":party_size", 250),
    # (party_set_icon, ":party_no", "icon_ships_6"),
    # (else_try),
    # (ge, ":party_size", 200),
    # (party_set_icon, ":party_no", "icon_ships_5"),
    # (else_try),
    # (ge, ":party_size", 150),
    # (party_set_icon, ":party_no", "icon_ships_4"),
    # (else_try),
    # (ge, ":party_size", 100),
    # (party_set_icon, ":party_no", "icon_ships_3"),
    # (else_try),
    # (ge, ":party_size", 50),
    # (party_set_icon, ":party_no", "icon_ships_2"),
    # (else_try),
    # (party_set_icon, ":party_no", "icon_ships_1"),
    # (try_end),
    # (try_end),
    # (else_try),
    ##bandit parties iconos per size
    # (store_faction_of_party, ":party_faction", ":party_no"),
    # (this_or_next|eq, ":party_faction", "fac_outlaws"),
    # (this_or_next|eq, ":party_faction", "fac_manhunters"),
    # (this_or_next|eq, ":party_faction", "fac_mountain_bandits"),
    # (this_or_next|eq, ":party_faction", "fac_forest_bandits"),
    # (eq, ":party_faction", "fac_deserters"),
    # (try_begin),
    ##on land
    # (neq, ":terrain", rt_water),
    # (neq, ":terrain", rt_river),
    # (neq, ":terrain", rt_bridge),    #not rt_bridge used as water terrain
    # (neq, ":party_no", "pt_sea_raiders_ships"),
    # (neq, ":party_no", "pt_sea_raiders_ships2"),
    # (neq, ":party_no", "pt_sea_raiders_ships3"),
    # (try_begin),
    # (ge, ":party_size", 135),
    # (party_set_icon, ":party_no", "icon_warriors_10"),
    # (else_try),
    # (ge, ":party_size", 120),
    # (party_set_icon, ":party_no", "icon_warriors_9"),
    # (else_try),
    # (ge, ":party_size", 105),
    # (party_set_icon, ":party_no", "icon_warriors_8"),
    # (else_try),
    # (ge, ":party_size", 90),
    # (party_set_icon, ":party_no", "icon_warriors_7"),
    # (else_try),
    # (ge, ":party_size", 75),
    # (party_set_icon, ":party_no", "icon_warriors_6"),
    # (else_try),
    # (ge, ":party_size", 60),
    # (party_set_icon, ":party_no", "icon_warriors_5"),
    # (else_try),
    # (ge, ":party_size", 45),
    # (party_set_icon, ":party_no", "icon_warriors_4"),
    # (else_try),
    # (ge, ":party_size", 30),
    # (party_set_icon, ":party_no", "icon_warriors_3"),
    # (else_try),
    # (ge, ":party_size", 15),
    # (party_set_icon, ":party_no", "icon_warriors_2"),
    # (else_try),
    # (party_set_icon, ":party_no", "icon_warriors_1"),
    # (try_end),
    # (else_try),
    ##on water
    # (try_begin),
    # (ge, ":party_size", 300),
    # (party_set_icon, ":party_no", "icon_ships_7"),
    # (else_try),
    # (ge, ":party_size", 250),
    # (party_set_icon, ":party_no", "icon_ships_6"),
    # (else_try),
    # (ge, ":party_size", 200),
    # (party_set_icon, ":party_no", "icon_ships_5"),
    # (else_try),
    # (ge, ":party_size", 150),
    # (party_set_icon, ":party_no", "icon_ships_4"),
    # (else_try),
    # (ge, ":party_size", 100),
    # (party_set_icon, ":party_no", "icon_ships_3"),
    # (else_try),
    # (ge, ":party_size", 50),
    # (party_set_icon, ":party_no", "icon_ships_2"),
    # (else_try),
    # (party_set_icon, ":party_no", "icon_ships_1"),
    # (try_end),
    # (try_end),
    # (try_end),
    # (try_end),
    
    
    #(is_between, ":party_no", "pt_looters", "pt_center_reinforcements"),
    #bandits parties por tamano acaba chief
    # ]),
    #### SEA BATTLES END chief#### SEA BATTLES END chief
    
    #centers weekly ON AVERAGE
    # reworked by JuJu70
    (0.62,
      [
        ###religion chief##############
        #to add faith to christians centers by building#edificios religiosos generan prosperidad
        (store_random_in_range, ":center_no", centers_begin, centers_end),
        (party_slot_eq, ":center_no", slot_party_looted_left_days, 0),
        (party_slot_eq, ":center_no", slot_village_state, svs_normal),
        
        (party_get_slot, ":prosperity", ":center_no", slot_town_prosperity),
        (store_faction_of_party, ":faction", ":center_no"),
        (troop_get_slot, ":religion","trp_player", slot_troop_religion),
        (party_get_slot, ":faith", ":center_no", slot_center_faithratio),
        
        #effects of religious improvements
        (try_begin),
          (this_or_next|party_slot_eq, ":center_no", slot_center_has_monastery1, 1),
          (party_slot_eq, ":center_no", slot_center_has_temple1, 1),
          (try_begin),
            (lt, ":prosperity", 100),
            (val_add, ":prosperity", 1),
          (try_end),
          
          (store_random_in_range, ":random", 0,5),  #has double the effect of lord's religion, randomized
          (val_add, ":faith", ":random"),
          (val_clamp, ":faith", 0, 101),
          (try_begin),
            (faction_slot_eq, ":faction", slot_faction_leader, "trp_player"),
            (eq, ":religion", 1),
            (val_add, "$faith_conversion", ":random"), #control conversions for minister
          (else_try),
            (faction_slot_eq, ":faction", slot_faction_leader, "trp_player"),
            (eq, ":religion", 2),
            (val_sub, "$faith_conversion", ":random"), #control conversions for minister
          (try_end),
          
        (else_try),
          (this_or_next|party_slot_eq, ":center_no", slot_center_has_monastery3, 1),
          (party_slot_eq, ":center_no", slot_center_has_temple3, 1),
          (try_begin),
            (lt, ":prosperity", 100),
            (val_add, ":prosperity", 1),
          (try_end),
          
          (store_random_in_range, ":random", 0,5),  #has double the effect of lord's religion, randomized
          (val_sub, ":faith", ":random"),
          (val_clamp, ":faith", 0, 101),
          (try_begin),
            (faction_slot_eq, ":faction", slot_faction_leader, "trp_player"),
            (eq, ":religion", 2),
            (val_add, "$faith_conversion", ":random"), #control conversions for minister
          (else_try),
            (faction_slot_eq, ":faction", slot_faction_leader, "trp_player"),
            (eq, ":religion", 1),
            (val_sub, "$faith_conversion", ":random"), #control conversions for minister
          (try_end),
        (try_end),
        
        #merchant guild
        (try_begin),
          (party_slot_eq, ":center_no", slot_center_has_guild, 1),
          (store_random_in_range, ":random", 0,4),
          (val_add, ":prosperity", ":random"),
          (val_clamp, ":prosperity", 0, 101),
          (gt, ":random", 0),
          (str_store_party_name_link, s1, ":center_no"),
          (display_message, "@The merchants' rest hall in {s1} adds to its prosperity."),
        (try_end),
        
        #regular religion adjustment
        (party_get_slot, ":local_lord", ":center_no", slot_town_lord),
        (try_begin),
          (gt, ":local_lord", -1),
          (troop_slot_eq, ":local_lord", slot_troop_religion, 1),
          (lt, ":faith", 100),
          (val_add, ":faith", 1),
          (try_begin),
            (faction_slot_eq, ":faction", slot_faction_leader, "trp_player"),
            (eq, ":religion", 1),
            (val_add, "$faith_conversion", ":random"), #control conversions for minister
          (else_try),
            (faction_slot_eq, ":faction", slot_faction_leader, "trp_player"),
            (eq, ":religion", 2),
            (val_sub, "$faith_conversion", ":random"), #control conversions for minister
          (try_end),
          
        (else_try),
          (gt, ":local_lord", -1),
          (troop_slot_eq, ":local_lord", slot_troop_religion, 2),
          (gt, ":faith", 0),
          (val_sub, ":faith", 1),
          (try_begin),
            (faction_slot_eq, ":faction", slot_faction_leader, "trp_player"),
            (eq, ":religion", 2),
            (val_add, "$faith_conversion", ":random"), #control conversions for minister
          (else_try),
            (faction_slot_eq, ":faction", slot_faction_leader, "trp_player"),
            (eq, ":religion", 1),
            (val_sub, "$faith_conversion", ":random"), #control conversions for minister
          (try_end),
        (try_end),
        
        # JuJu70
        # Nearby religious center affects religion
        (assign, ":min_distance", 20),
        (assign, ":closest_monastery", -1),
        
        (try_for_range, ":monastery", "p_monasterio1", "p_yourlair"),
          (party_slot_eq, ":monastery", slot_party_looted_left_days, 0),
          (store_distance_to_party_from_party, ":cur_distance", ":center_no", ":monastery"),
          (lt, ":cur_distance", ":min_distance"),
          (assign, ":min_distance", ":cur_distance"),
          (assign, ":closest_monastery", ":monastery"),
        (try_end),
        
        (try_for_range, ":monastery", "p_paganholysites1", "p_oldpagan_hut"),
          (party_slot_eq, ":monastery", slot_party_looted_left_days, 0),
          (store_distance_to_party_from_party, ":cur_distance", ":center_no", ":monastery"),
          (lt, ":cur_distance", ":min_distance"),
          (assign, ":min_distance", ":cur_distance"),
          (assign, ":closest_monastery", ":monastery"),
        (try_end),
        
        (try_begin),
          (is_between, ":closest_monastery", "p_monasterio1", "p_yourlair"),
          (lt, ":faith", 100),
          (val_add, ":faith", 1),
          (try_begin),
            (faction_slot_eq, ":faction", slot_faction_leader, "trp_player"),
            (try_begin),
              (eq, ":religion", 1),
              (val_add, "$faith_conversion", 1), #control conversions for minister
            (else_try),
              (eq, ":religion", 2),
              (val_sub, "$faith_conversion", 1), #control conversions for minister
            (try_end),
            (str_store_party_name, s33, ":closest_monastery"),
            (str_store_party_name, s34, ":center_no"),
            (display_message, "@Christian monastery at {s33} improves Christian faith in {s34}."),
          (try_end),
        
        (else_try),
          (is_between, ":closest_monastery", "p_paganholysites1", "p_oldpagan_hut"),
          (gt, ":faith", 0),
          (val_sub, ":faith", 1),
          (try_begin),
            (faction_slot_eq, ":faction", slot_faction_leader, "trp_player"),
            (try_begin),
              (eq, ":religion", 2),
              (val_add, "$faith_conversion", 1), #control conversions for minister
            (else_try),
              (eq, ":religion", 1),
              (val_sub, "$faith_conversion", 1), #control conversions for minister
            (try_end),
            (str_store_party_name, s33, ":closest_monastery"),
            (str_store_party_name, s34, ":center_no"),
            (display_message, "@Pagan hof at {s33} reduces Christian faith in {s34}."),
          (try_end),
        (try_end),
        
        #update faith and prosperity
        (party_set_slot, ":center_no", slot_town_prosperity, ":prosperity"),
        (party_set_slot, ":center_no", slot_center_faithratio, ":faith"),

        #player center
        (try_begin),
          (eq, ":local_lord", "trp_player"),
          (party_get_slot, ":cur_relation", ":center_no", slot_center_player_relation),
          #Change relation for faith Religion
          (try_begin),
            (eq, "$g_player_faith", 1),
            (try_begin),
              (party_slot_eq, ":center_no", slot_center_religion, 1),#christian
              (party_get_slot, ":faith", ":center_no", slot_center_faithratio),
              (try_begin),
                (gt, ":faith", 55),
                (store_random_in_range, ":rand", 0,2),
                (val_add, ":cur_relation", ":rand"),
              (else_try),
                (lt, ":faith", 30),
                (store_random_in_range, ":rand", -2,0),
                (val_add, ":cur_relation", ":rand"),
              (try_end),
            (else_try),
              (party_slot_eq, ":center_no", slot_center_religion, 2),#pagan
              (party_get_slot, ":faith", ":center_no", slot_center_faithratio),
              (store_sub, ":p_faith", 100, ":faith"),
              (try_begin),
                (gt, ":p_faith", 40),
                (store_random_in_range, ":rand", -2,1),
                (val_add, ":cur_relation", ":rand"),
              (else_try),
                (lt, ":p_faith", 20),
                (store_random_in_range, ":rand", 0,2),
                (val_add, ":cur_relation", ":rand"),
              (try_end),
            (try_end),
          (else_try),
            (eq, "$g_player_faith", 2),
            (try_begin),
              (party_slot_eq, ":center_no", slot_center_religion, 2),
              (party_get_slot, ":faith", ":center_no", slot_center_faithratio),
              (store_sub,":p_faith", 100, ":faith"),
              (try_begin),
                (gt, ":p_faith", 55),
                (store_random_in_range, ":rand", 0,2),
                (val_add, ":cur_relation", ":rand"),
              (else_try),
                (lt, ":p_faith", 30),
                (store_random_in_range, ":rand", -2,0),
                (val_add, ":cur_relation", ":rand"),
              (try_end),
            (else_try),
              (party_slot_eq, ":center_no", slot_center_religion, 1),#christian
              (party_get_slot, ":faith", ":center_no", slot_center_faithratio),
              (try_begin),
                (gt, ":faith", 40),
                (store_random_in_range, ":rand", -2,1),
                (val_add, ":cur_relation", ":rand"),
              (else_try),
                (lt, ":faith", 20),
                (store_random_in_range, ":rand", 0,2),
                (val_add, ":cur_relation", ":rand"),
              (try_end),
            (try_end),
          (try_end),
          
          ###kingdom taxes system faction screen
          # (try_begin),
          # (faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_inactive),
          # (neq,"$tax_rate", 0),
          # (assign, "$tax_rate", 0),
          # (try_end),
          (try_begin),
            (party_slot_eq, ":center_no", slot_center_tax_rate, 2),#high
            #			(eq, "$tax_rate", 2), #High
            (val_add, ":cur_relation", -5),
          (else_try),
            #			(eq, "$tax_rate", 1), #Low
            (party_slot_eq, ":center_no", slot_center_tax_rate, 1),#low
            (lt, ":cur_relation", 60),
            (val_add, ":cur_relation", 1),
          (else_try),
            #(val_add, ":cur_relation", -1), #this can do game too hard.
          (try_end),
          #brewery
          (try_begin),
            (party_slot_eq, ":center_no", slot_center_has_brewery, 1),
            (lt, ":cur_relation", 5),
            (store_random_in_range, ":rel_boost", 0,100),
            (lt, ":rel_boost", 30),
            (store_random_in_range, ":rand", 1,3),
            (val_add, ":cur_relation", ":rand"),
          (try_end),
          
          (party_set_slot, ":center_no", slot_center_player_relation, ":cur_relation"),
          
          #SCRIPTORIUM
          (try_begin),
            (party_slot_eq, ":center_no", slot_center_has_university, 1),
            (str_store_party_name_link, s1, ":center_no"),
            (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
            (le, ":player_renown", 1500),
            (store_random_in_range, ":rand", 0, 100),#JuJu70
            (le, ":rand", 50),#JuJu70
            (store_random_in_range, ":renown_change", 1, 3), # 1, 2 or 3
            (troop_get_slot, ":old_renown", "trp_player", slot_troop_renown),
            (store_add, ":new_renown", ":old_renown", ":renown_change"),
            (troop_set_slot, "trp_player", slot_troop_renown, ":new_renown"),
            (display_message, "@The scriptorium in {s1} adds to your renown."),
            #(call_script, "script_change_troop_renown", "trp_player", 4), #MOTO this should probably be a one-shot addition; from 6 to 3
          (try_end),
        (try_end),	#player center
        
        # Switching village designation from 1->2 or 2->1
        (party_get_slot, ":faith", ":center_no", slot_center_faithratio),
        (party_get_slot,":religion1",":center_no",slot_center_religion),
        (try_begin),
          (eq, ":religion1", 2),
          (gt, ":faith", 80),
          (store_random_in_range, ":rand", 0, 100),
          (gt, ":rand", 66),
          (party_set_slot,":center_no",slot_center_religion, 1),
        (else_try),
          (eq, ":religion1", 1),
          (lt, ":faith", 20),
          (store_random_in_range, ":rand", 0, 100),
          (lt, ":rand", 33),
          (party_set_slot,":center_no",slot_center_religion, 2),
        (try_end),
        # JuJu70
        # Piggybacking
        (try_begin),
          (party_slot_eq, ":center_no", slot_center_enslaved, 1),
          (party_set_slot, ":center_no", slot_center_enslaved, 0),
        (try_end),
        
        ##	(party_get_slot, ":accumulated_rents", ":center_no", slot_center_accumulated_rents),
        ##	(assign, ":cur_rents", 0),
        ##	  #Collect taxes for another week
        ##    (try_begin),
        ##		(party_slot_ge, ":center_no", slot_town_lord, 0), #unassigned centers do not accumulate rents
        ##		(try_begin),
        ##			(party_slot_eq, ":center_no", slot_party_type, spt_village),
        ##			(try_begin),
        ##				(party_slot_eq, ":center_no", slot_village_state, svs_normal),
        ##				(assign, ":cur_rents", 2400),
        ##			(try_end),
        ##		(else_try),
        ##			(neg|party_slot_ge, ":center_no", slot_party_looted_left_days, 1),
        ##			(party_slot_eq, ":center_no", slot_party_type, spt_castle),
        ##			(assign, ":cur_rents", 3200),
        ##		(else_try),
        ##			(neg|party_slot_ge, ":center_no", slot_party_looted_left_days, 1),
        ##			(party_slot_eq, ":center_no", slot_party_type, spt_town),
        ##			(assign, ":cur_rents", 4800),
        ##		(try_end),
        ##
        ##		(party_get_slot, ":prosperity", ":center_no", slot_town_prosperity), #prosperty changes between 0..100
        ##		(store_add, ":multiplier", 20, ":prosperity"), #multiplier changes between 20..120
        ##		(val_mul, ":cur_rents", ":multiplier"),
        ##		(val_div, ":cur_rents", 120),#Prosperity of 100 gives the default values
        ###TAXES relgion chief cambia. Religion de player affect to Taxes player gets in center.
        ##		(try_begin),
        ##			(party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
        ##			(party_get_slot, ":faith", ":center_no", slot_center_faithratio),
        ##			(store_sub, ":p_faith", 100, ":faith"),
        ##			(try_begin),
        ##				(eq, "$g_player_faith", 1),
        ##				(val_div, ":p_faith", 2),
        ##				(val_add, ":faith", ":p_faith"),
        ##				(val_mul, ":cur_rents", ":faith"),
        ##				(val_div, ":cur_rents", 100),
        ##			(else_try),
        ##				(eq, "$g_player_faith", 2), #es pagano
        ##				(val_div, ":faith", 2),
        ##				(val_add, ":p_faith", ":faith"),
        ##				(val_mul, ":cur_rents", ":p_faith"),
        ##				(val_div, ":cur_rents", 100),
        ##			(try_end),
        ##		(try_end),
        ##	(try_end),
        ###TAXES end
        ##
        ###chief empieza rentas con black smith
        ##	(try_begin), #castles maintenance is expensive  -- castle = small town
        ##		(party_slot_eq, ":center_no", slot_party_type, spt_castle),
        ##		(party_slot_eq, ":center_no", slot_center_has_blacksmith, 1),
        ##		(val_add, ":cur_rents", 300),
        ##	(try_end),
        ##	(try_begin),
        ##		(party_slot_eq, ":center_no", slot_town_port, 1),
        ##		(party_slot_eq, ":center_no", slot_center_has_slavemarket, 1),
        ##		(val_add, ":cur_rents", 800),
        ##	(try_end),
        ##	(try_begin),
        ##		(party_slot_eq, ":center_no", slot_center_has_brewery, 1),
        ##		(val_add, ":cur_rents", 200),
        ##	(try_end),
        ##	(try_begin), #advoid negatives valours
        ##		(lt, ":cur_rents", 0),
        ##		(assign, ":cur_rents", 0),
        ##	(try_end),
        ###rentas acaba
        ##    (try_begin),
        ##        (party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
        ##        (options_get_campaign_ai, ":reduce_campaign_ai"), #moto chief
        ##        (try_begin),
        ##			(eq, ":reduce_campaign_ai", 0), #hard (less money from rents)
        ##			(val_mul, ":cur_rents", 3),
        ##			(val_div, ":cur_rents", 4),
        ##        (else_try),
        ##			(eq, ":reduce_campaign_ai", 1), #medium (normal money from rents)
        ##              #same
        ##        (else_try),
        ##			(eq, ":reduce_campaign_ai", 2), #easy (more money from rents)
        ##			(val_mul, ":cur_rents", 4),
        ##			(val_div, ":cur_rents", 3),
        ##        (try_end),
        ##           ###kingdom taxes system faction screen
        ##        (try_begin),
        ###			(eq, "$tax_rate", 2), #High
        ##			(party_slot_eq, ":center_no", slot_center_tax_rate, 2),#high
        ##			(val_mul, ":cur_rents", 4),
        ##			(val_div, ":cur_rents", 3),
        ##        (else_try),
        ###			(eq, "$tax_rate", 1), #Low
        ##			(party_slot_eq, ":center_no", slot_center_tax_rate, 1),#low
        ##			(val_mul, ":cur_rents", 3),
        ##			(val_div, ":cur_rents", 4),
        ##        (try_end),
        ##    (try_end),
        ##
        ##    (val_add, ":accumulated_rents", ":cur_rents"), #cur rents changes between 23..1000
        ##    (party_set_slot, ":center_no", slot_center_accumulated_rents, ":accumulated_rents"),
        ##
        ##	(try_begin),
        ##		(is_between, ":center_no", villages_begin, villages_end),
        ##		(party_get_slot, ":bound_castle", ":center_no", slot_village_bound_center),
        ##		(party_slot_ge, ":bound_castle", slot_town_lord, 0), #unassigned centers do not accumulate rents
        ##		(is_between, ":bound_castle", castles_begin, castles_end),
        ##		(party_get_slot, ":accumulated_rents", ":bound_castle", slot_center_accumulated_rents), #castle's accumulated rents
        ##		(val_add, ":accumulated_rents", ":cur_rents"), #add village's rent to castle rents
        ##		(party_set_slot, ":bound_castle", slot_center_accumulated_rents, ":accumulated_rents"),
        ##	(try_end),
    ]),
    
    #non-player factions weekly ON AVERAGE
    (8, [
        (store_random_in_range, ":faction_no", "fac_kingdom_1", kingdoms_end), #Excluding player kingdom
        
        #PLayer relation with priest affect kingdoms relation
        # No effect if player's kingdom is at truce
        (assign, ":continue", 0),
        (try_begin),
          (gt, "$players_kingdom", 0),
          (faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),
          (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", "$players_kingdom", ":faction_no"),
          (assign, ":diplomatic_status", reg0),
          (assign, ":duration_of_status", reg1),
          (eq, ":diplomatic_status", 1),#truce
          (is_between, ":duration_of_status", 1, truce_time + 1), #still at truce
          (assign, ":continue", 1),
        (try_end),
        (store_relation, ":faction_relation", ":faction_no", "fac_player_faction"),
        (try_begin),
          (eq, ":continue", 0),
          (faction_slot_eq, ":faction_no", slot_faction_religion, cb3_christian),
          (store_relation, ":player_relation", "fac_christians", "fac_player_faction"),
          (try_begin),
            (gt, ":player_relation", 80),
            (lt, ":faction_relation", 50),
            (store_random_in_range, ":rand", 0, 10),
            (lt,":rand", 5),
            (call_script, "script_change_player_relation_with_faction", ":faction_no", 1), #la q designemos
            (str_store_faction_name, s1, ":faction_no"),
            (display_message, "@Due to the good word Christian clergymen spread about you, your relationship with the {s1} improves."),
          (else_try),
            (lt, ":player_relation", -50),
            (gt, ":faction_relation", -75),
            (store_random_in_range, ":rand", 0, 10),
            (lt,":rand", 5),
            (call_script, "script_change_player_relation_with_faction", ":faction_no", -1), #la q designemos
            (str_store_faction_name, s1, ":faction_no"),
            (display_message, "@Due to the bad word Christian clergymen spread about you, your relationship with the {s1} declines."),
            (try_begin),
              (store_relation, ":player_relation", ":faction_no", "fac_player_faction"),
              (eq, ":player_relation", -1),
              (tutorial_box, "@{s1} has become hostile to you due to your mistreatment of Christian subjects.", "@Faction became hostile"),
            (try_end),
          (try_end),
        (try_end),
        (try_begin),
          (eq, ":continue", 0),
          (faction_slot_eq, ":faction_no", slot_faction_religion, cb3_pagan),
          (store_relation, ":player_relation", "fac_pagans", "fac_player_faction"),
          (try_begin),
            (gt, ":player_relation", 80),
            (lt, ":faction_relation", 50),
            (store_random_in_range, ":rand", 0, 10),
            (lt,":rand", 5),
            (call_script, "script_change_player_relation_with_faction", ":faction_no", 1), #la q designemos
            (str_store_faction_name, s1, ":faction_no"),
            (display_message, "@Due to the good word influential pagans spread about you, your relationship with the {s1} improves."),
          (else_try),
            (lt, ":player_relation", -50),
            (gt, ":faction_relation", -75),
            (store_random_in_range, ":rand", 0, 10),
            (lt,":rand", 5),
            (call_script, "script_change_player_relation_with_faction", ":faction_no", -1), #la q designemos
            (str_store_faction_name, s1, ":faction_no"),
            (display_message, "@Due to the bad word influential pagans spread about you, your relationship with the {s1} declines."),
            (try_begin),
              (store_relation, ":player_relation", ":faction_no", "fac_player_faction"),
              (eq, ":player_relation", -1),
              (tutorial_box, "@{s1} has become hostile to you due to your mistreatment of Pagan subjects.", "@Faction became hostile"),
            (try_end),
          (try_end),
        (try_end),
    ]),
    
    (24, [
    ]),
    
    #random 90 hour ON AVERAGE
    (90,
      [
        (try_for_range, ":center", "p_quarry1", "p_hadrian_wall1"),
          (party_set_slot, ":center", slot_center_inventory, 0),
        (try_end),
        (try_for_range, ":center", "p_monasterio1", "p_yourlair"),
          (party_set_slot, ":center", slot_center_inventory, 0),
        (try_end),
        (assign, "$banquete_refuge", 0), #let do feast in refuge, player lair chief
        (assign, "$g_rezar_monasterio", 0),
        (assign, "$premio_minister", 0), #premio a ministro
        (assign, "$lord_event_possible", 0), #town event possible each 90 hours random events town
        (assign, "$rumors_inquired", 0), #rumors
        (assign, "$first_time variable", 0), #no conversation repit in 90 hours
        (assign, "$g_empieza_discurso", 0), #no conversation repit in 90 hours
        (assign, "$g_empieza_campeon", 0), #no conversation repit in 90 hours
    ]),
    
    # Masterless men AI (107)
    # JuJu70
    (1,
      [(try_for_parties, ":party_no"),
          (store_faction_of_party, ":faction", ":party_no"),
          (eq, ":faction", "fac_deserters"),
          #		(party_slot_eq, ":party_no", slot_party_on_water, 0),	#water travel AI works different and will be done in another trigger
          (assign, ":closest_village", -1),	#phaiak try fix
          (get_party_ai_behavior, ":ai_bhvr", ":party_no"),
          (party_get_slot, ":ai_behavior", ":party_no", slot_party_ai_state),
          (try_begin),
            (this_or_next|eq, ":ai_bhvr", ai_bhvr_travel_to_party),
            (eq, ":ai_bhvr", ai_bhvr_travel_to_point),
            (neq, ":ai_behavior", 0),
            (get_party_ai_object,":p_target",":party_no"),
            (gt, ":p_target", 0),
            (try_begin),
              (party_slot_eq, ":p_target", slot_party_type, spt_village),
              (store_distance_to_party_from_party, ":distance_from_target", ":party_no", ":p_target"),
              (try_begin),
                (lt, ":distance_from_target", 2),
                (party_set_slot, ":party_no", slot_party_ai_state ,spai_raiding_around_center),
                (party_set_ai_object, ":party_no", ":p_target"),
                (try_begin),
                  (party_slot_eq, ":p_target", slot_village_state, svs_normal),
                  (call_script, "script_village_set_state", ":p_target", svs_being_raided),	#possible cause for VC-2085 but p_target = spt_village so it should be ok...
                  (party_set_slot, ":p_target", slot_village_raided_by, ":party_no"),
                  (try_begin),
                    (store_faction_of_party, ":village_faction", ":p_target"),
                    (this_or_next|party_slot_eq, ":p_target", slot_town_lord, "trp_player"),
                    (eq, ":village_faction", "fac_player_supporters_faction"),
                    (store_distance_to_party_from_party, ":dist", "p_main_party", ":p_target"),
                    (this_or_next|lt, ":dist", 30),
                    (party_slot_eq, ":p_target", slot_center_has_messenger_post, 1),
                    (call_script, "script_add_notification_menu", "mnu_notification_village_raid_started", ":p_target", ":faction"),
                  (try_end),
                (else_try),
                  (party_slot_eq, ":p_target", slot_village_state, svs_being_raided),
                (else_try),
                  (party_set_slot, ":party_no", slot_party_ai_substate, 0),
                  (party_get_position, pos0,  ":party_no"),
                  (party_set_ai_behavior, ":party_no", ai_bhvr_patrol_location),
                  (party_set_ai_patrol_radius, ":party_no", 30),
                  (party_set_ai_target_position, ":party_no", pos0),
                  (party_set_slot, ":party_no", slot_party_ai_state, spai_patrolling_around_center),
                (try_end),
              (else_try),
                (party_get_position, pos1, ":p_target"),
                (map_get_random_position_around_position, pos2, pos1, 1),
                (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_point),
                (party_set_ai_target_position, ":party_no", pos2),
                (party_set_ai_object, ":party_no", ":p_target"),
                (party_set_slot, ":party_no", slot_party_ai_object, ":p_target"),
                (party_set_slot, ":party_no", slot_party_ai_state, spai_patrolling_around_center),
              (try_end),
            (else_try),
              (party_slot_eq, ":p_target", slot_party_type, spt_kingdom_hero_party),
              (neq, ":p_target", "p_main_party"),
              (store_distance_to_party_from_party, ":distance_from_target", ":party_no", ":p_target"),
              (try_begin),
                (lt, ":distance_from_target", 2),
                (party_set_slot, ":party_no", slot_party_ai_state ,spai_engaging_army),
                (party_set_ai_object, ":party_no", ":p_target"),
                (party_set_ai_behavior, ":party_no", ai_bhvr_attack_party),
              (else_try),
                (party_get_position, pos1, ":p_target"),
                (map_get_random_position_around_position, pos2, pos1, 1),
                (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_point),
                (party_set_ai_target_position, ":party_no", pos2),
                (party_set_ai_object, ":party_no", ":p_target"),
                (party_set_slot, ":party_no", slot_party_ai_object, ":p_target"),
                (party_set_slot, ":party_no", slot_party_ai_state, spai_engaging_army),
              (try_end),
            (else_try),
              (party_get_position, pos0,  ":party_no"),
              (party_set_ai_behavior, ":party_no", ai_bhvr_patrol_location),
              (party_set_ai_patrol_radius, ":party_no", 30),
              (party_set_ai_target_position, ":party_no", pos0),
              (party_set_slot, ":party_no", slot_party_ai_state, spai_patrolling_around_center),
            (try_end),
          (else_try),
            (party_get_current_terrain, ":cur_terrain", ":party_no"),
            (this_or_next|eq,":cur_terrain",rt_water),
            (this_or_next|eq,":cur_terrain",rt_bridge),
            (eq,":cur_terrain",rt_river),
            (assign, ":minimum_distance", 200),
            (assign, ":closest_village", -1),
            (try_for_range, ":town_no", towns_begin, towns_end),
              (party_slot_eq, ":town_no", slot_town_port, 1),
              (store_distance_to_party_from_party, ":dist", ":party_no",":town_no"),
              (lt, ":dist", ":minimum_distance"),
              (assign, ":minimum_distance", ":dist"),
              (assign, ":closest_village", ":town_no"),
            (try_end),
            (gt, ":closest_village", 0),
            (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
            (party_set_ai_target_position, ":party_no", ":closest_village"),
            (party_set_ai_object, ":party_no", ":closest_village"),
          (else_try),
            (store_party_size_wo_prisoners,":size", ":party_no"),
            (try_begin),
              (ge, ":size", 50),
              (store_random_in_range, ":rand", 0, 1000),
              (try_begin),
                (lt, ":rand", 50),
                (assign, ":minimum_distance", 40),
                (assign, ":closest_village", -1),
                (try_for_range, ":village_no", villages_begin, villages_end),
                  (store_distance_to_party_from_party, ":dist", ":party_no",":village_no"),
                  (lt, ":dist", ":minimum_distance"),
                  (neg|party_slot_eq, ":village_no", slot_village_state, svs_looted),
                  (neg|party_slot_eq, ":village_no", slot_village_state, svs_being_raided),
                  (neg|party_slot_ge, ":village_no", slot_village_infested_by_bandits, 1),
                  (assign, ":minimum_distance", ":dist"),
                  (assign, ":closest_village", ":village_no"),
                (try_end),
              (try_end),
              (gt, ":closest_village", 0),
              (party_get_position, pos1, ":closest_village"),
              (map_get_random_position_around_position, pos2, pos1, 1),
              (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_point),
              (party_set_ai_target_position, ":party_no", pos2),
              (party_set_ai_object, ":party_no", ":closest_village"),
              (party_set_slot, ":party_no", slot_party_ai_object, ":closest_village"),
            (else_try),
              (party_get_position, pos0,  ":party_no"),
              (party_set_ai_behavior, ":party_no", ai_bhvr_patrol_location),
              (party_set_ai_patrol_radius, ":party_no", 30),
              (party_set_ai_target_position, ":party_no", pos0),
              (party_set_slot, ":party_no", slot_party_ai_state, spai_patrolling_around_center),
            (try_end),
          (try_end),
        (try_end),
    ]),
    #para saqueo monasterios religion y otros
    (168,
      [
        (troop_set_slot, "trp_abad", slot_troop_does_not_give_quest, 0),
        #Racket + garrison warning
        (try_for_range, ":center_no", centers_begin, centers_end),
          (try_begin),
            (is_between, ":center_no", walled_centers_begin, walled_centers_end),
            (party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
            (neg|faction_slot_eq,  "$players_kingdom", slot_faction_marshal, "trp_player"),
            (assign, ":at_war", 0),
            (try_for_range, ":faction_at_war", kingdoms_begin, kingdoms_end),
              (store_relation, ":relation", "$players_kingdom", ":faction_at_war"),
              (lt, ":relation", 0),
              (val_add, ":at_war", 1),
            (try_end),
            (gt, ":at_war", 0),
            (party_get_slot, ":center_max_garrison", ":center_no", slot_town_prosperity),
            (val_mul, ":center_max_garrison", 8),
            (val_add, ":center_max_garrison", 100),	#100..900, average 500
            (val_max, ":center_max_garrison", 250),
            (store_party_size_wo_prisoners, ":center_strength", ":center_no"),
            (store_sub, ":surplus_troops", ":center_strength", ":center_max_garrison"),
            (gt, ":surplus_troops", 25),
            (str_store_party_name, s13, ":center_no"),
            (display_message,"@{s13} has too many troops garrisoned in and may be picked by marshal to levy soldiers.", color_hero_news),
          (try_end),
          (party_get_slot, ":racket", ":center_no", slot_center_racket),
          (ge, ":racket", 1),
          (val_sub, ":racket", 1),
          (party_set_slot, ":center_no", slot_center_racket, ":racket"),
        (try_end),
        #Lords reset
        (try_for_range, ":npc", active_npcs_begin, active_npcs_end),
          (troop_slot_eq, ":npc", slot_troop_temp, 1),
          (troop_set_slot, ":npc", slot_troop_temp, 0),
        (try_end),
    ]),
    
    # JuJu70
    #Adventures doing stuff in walled centers every two hours on average
    (0.05,
      [
        (store_random_in_range, ":cur_troop", companions_begin, kings_end),   #VC-3907 include leaders of defeated factions
          (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
          (troop_get_slot, ":cur_party", ":cur_troop", slot_troop_leaded_party),
          (gt, ":cur_party", 0),
          (store_faction_of_party, ":faction", ":cur_party"),
          (eq, ":faction", "fac_adventurers"),
          (try_begin),
            (party_is_active, ":cur_party"),
            (party_get_attached_to, ":attached_to_party", ":cur_party"),
            (assign, ":party_is_in_town", 0),
            (try_begin),
              (is_between, ":attached_to_party", walled_centers_begin, walled_centers_end),
              (assign, ":party_is_in_town", ":attached_to_party"),
            (try_end),
          (try_end),
          (gt, ":party_is_in_town", 0),
          (store_faction_of_party, ":center_faction", ":party_is_in_town"),
          (assign,":continue", 1),
          (try_begin),
            (faction_slot_eq, ":center_faction", slot_faction_ai_state, sfai_feast),
            (faction_get_slot, ":feast_center", ":center_faction", slot_faction_ai_object),
            (eq,":party_is_in_town", ":feast_center"),
            (party_set_slot, ":cur_party", slot_party_ai_state, spai_holding_center),
            (party_set_slot, ":cur_party", slot_party_ai_object, ":party_is_in_town"),
            (party_set_ai_behavior, ":cur_party", ai_bhvr_in_town),
            (assign, ":continue", 0),
          (try_end),
          (try_begin),
            (is_between, ":party_is_in_town", towns_begin, towns_end),
            (party_get_num_prisoners , ":prisoners_count", ":cur_party"),
            (gt, ":prisoners_count", 0),
            (call_script, "script_sell_prisoners", ":cur_troop"),
          (try_end),
          # (try_begin),
          # (is_between, ":party_is_in_town", towns_begin, towns_end),
          # (call_script, "script_party_get_ideal_size", ":cur_party"),
          # (assign, ":ideal_size", reg0),
          # (store_party_size_wo_prisoners, ":party_size", ":cur_party"),
          # (store_mul, ":party_strength_as_percentage_of_ideal", ":party_size", 100),
          # (val_div, ":party_strength_as_percentage_of_ideal", ":ideal_size"),
          # (this_or_next|lt, ":party_strength_as_percentage_of_ideal", 75),
          # (le, ":party_size", 70),
          # (party_get_slot, ":volunteers_in_target", ":party_is_in_town", slot_center_npc_volunteer_troop_amount),
          # (assign, reg22, ":volunteers_in_target"),
          # (try_begin),
          # (gt, reg22, 0),
          # (assign, ":continue", 0),
          # (try_end),
          # (party_get_slot, ":target_volunteer_type", ":party_is_in_town", slot_center_npc_volunteer_troop_type),
          # (store_sub, ":needed", ":ideal_size", ":party_size"),
          # (try_begin),
          # (gt, ":volunteers_in_target", ":needed"),
          # (store_sub, ":surplus", ":volunteers_in_target", ":needed"),
          # (assign, ":amount_to_recruit", ":needed"),
          # (party_set_slot, ":party_is_in_town", slot_center_npc_volunteer_troop_amount, ":surplus"),
          # (party_add_members, ":cur_party", ":target_volunteer_type", ":amount_to_recruit"),
          # (else_try),
          # (le, ":volunteers_in_target", ":needed"),
          # (gt, ":volunteers_in_target", 0),
          # (party_set_slot, ":party_is_in_town", slot_center_npc_volunteer_troop_amount, -1),
          # (party_add_members, ":cur_party", ":target_volunteer_type", ":volunteers_in_target"),
          # (try_end),
          # (try_end),
          (eq, ":continue", 1),
          (party_detach, ":cur_party"),
          (party_get_position, pos1, ":party_is_in_town"),
          (party_set_ai_target_position, ":cur_party", pos1),
          (party_set_ai_behavior, ":cur_party", ai_bhvr_patrol_location),
          (party_set_slot, ":cur_party", slot_party_ai_state, spai_patrolling_around_center),
          (party_set_ai_patrol_radius, ":cur_party", 35),
          (party_set_aggressiveness, ":cur_party", 11),
          (party_set_courage, ":cur_party", 10),
          (party_set_ai_initiative, ":cur_party", 100),
          (party_set_helpfulness, ":cur_party", 110),
        # (try_end),
    ]),
    #STrig 110
    (3,
      [(neq, "$campaign_type", camp_sandbox),(neq, "$campaign_type", camp_lordc),(neq, "$campaign_type", camp_kingc),
        (try_begin),
          (eq, "$beda_story_1", 1),# beda story chief
          (start_presentation, "prsnt_beda_story_1"),
          (assign, "$beda_story_1", 0), #
        (try_end),
        
        (try_begin),
          (eq, "$beda_story_1", 2),# beda story chief
          (start_presentation, "prsnt_beda_story_2"),
          (assign, "$beda_story_1", 0), #
        (try_end),
        
        ##     (try_begin), #no necesary, prst called since menu
        ##                     (eq, "$beda_story_1", 3),# beda story chief
        ##         (start_presentation, "prsnt_beda_story_3"),
        ##                                     (assign, "$beda_story_1", 0), #
        ##    (try_end),
        
        ##     (try_begin),
        ##                     (eq, "$sacerdote_mosqueado", 1),#le ha echado, no quiere saber nada
        ##                                     (assign, "$sacerdote_mosqueado", 0), #le ha echado, priest out recupera, religion chief
        ##    (try_end),
    ]),
    
    #mainquest chief tigger
    (1, #llama a conversacion dialogo con un npc en party en un momento dado
      [  (map_free), #en mapa
        (party_get_num_companions, ":party_size", "p_main_party"),
        (options_get_campaign_ai, ":ai"),
        (val_sub, ":ai", 2),
        (try_begin),
          (neq, "$last_ai_setting", ":ai"),
          (assign, "$last_ai_setting", ":ai"),
          (call_script, "script_update_party_creation_random_limits"),
          
          (assign, reg1, "$spawn_party_max_size"),
          (val_mul, reg1, 15),  #for some reason, parties spawn about 50% larger than limit
          (val_div, reg1, 10),
          (val_add, reg1, 5), #for some reason, parties can spawn size six when limit is 1
          (val_min, reg1, max_spawn_party_size),
          
          (try_begin),
            (eq, ":ai", -2),
            (lt, ":party_size", max_spawn_party_size/2), #some spawn parties cap at this size
            (str_store_string, s1, "@most"),
            (dialog_box, "str_game_difficulty_warning_desc", "str_game_difficulty_warning"),
          (else_try),
            (eq, ":ai", -1),
            (lt, ":party_size", max_spawn_party_size/2), #some spawn parties cap at this size
            (str_store_string, s1, "@half"),
            (dialog_box, "str_game_difficulty_warning_desc", "str_game_difficulty_warning"),
          (else_try),
            (lt, ":party_size", reg1),
            (str_store_string, s1, "@some"),
            (dialog_box, "str_game_difficulty_warning_desc", "str_game_difficulty_warning"),
          (else_try),
            (lt, ":party_size", max_spawn_party_size),
            (str_store_string, s1, "@few"),
            (dialog_box, "str_game_difficulty_warning_desc", "str_game_difficulty_warning"),
          (try_end),
        (try_end),
        
        (party_get_current_terrain,":terrain","p_main_party"),
        (neq,":terrain",0),
        (neq,":terrain",7),
        (neq,":terrain",8),
        (try_begin),
          (quest_slot_eq,"qst_kennemer_mission_2",slot_quest_current_state, 5),
          (main_party_has_troop,"trp_npc8"), #reginhard
          (assign, "$npc_map_talk_context", slot_troop_mainquest_dialog),
          (start_map_conversation, "trp_npc8", -1),
        (else_try),
          (quest_slot_eq,"qst_kennemer_mission_3",slot_quest_current_state, 1),
          (main_party_has_troop,"trp_npc8"),
          (assign, "$npc_map_talk_context", slot_troop_mainquest_dialog),
          (start_map_conversation, "trp_npc8", -1),
        (else_try),
          (quest_slot_eq,"qst_revenge_sigurd",slot_quest_current_state, 1),
          (main_party_has_troop,"trp_npc8"),
          (assign, "$npc_map_talk_context", slot_troop_mainquest_dialog),
          (start_map_conversation, "trp_npc8", -1),
        (else_try),
          (quest_slot_eq,"qst_danmork_protection",slot_quest_current_state, 1),
          (check_quest_active,"qst_revenge_exchange"),
          #(quest_slot_eq,"qst_revenge_exchange",slot_quest_current_state, 1),
          (main_party_has_troop,"trp_npc2"), #Egil
          (assign, "$npc_map_talk_context", slot_troop_mainquest_dialog),
          (start_map_conversation, "trp_npc2", -1),
        (try_end),
      ]
    ),
    
    #Reset Extortion fees JuJu70
    (24*30,
      [
        (try_for_range, ":center", special_places_begin, special_places_end),
          (party_set_slot, ":center", slot_center_fee_paid, 0),
        (try_end),
    ]),
    
    
    
    #MOTO bad -- these may update immediately if the player happens to start right before
    #requires a timer
    (24, #player lair chief
      [
        (party_get_slot, ":last_time", "p_yourlair", slot_lair_time_to_improve),
        (store_current_hours, ":cur_hours"),
        (store_add, ":ok_time", ":last_time", 160), #between 60 and 160 hours
        (gt, ":cur_hours", ":ok_time"),
        (party_slot_eq, "p_yourlair", slot_lair_improve, 1),
        (party_set_slot, "p_yourlair", slot_lair_improve, 2), #first stage finished
    ]),
    #(24, #player lair chief
    (24, #player lair chief
      [
        (party_get_slot, ":last_time", "p_yourlair", slot_lair_time_to_improve),
        (store_current_hours, ":cur_hours"),
        (store_add, ":ok_time", ":last_time", 300),
        (gt, ":cur_hours", ":ok_time"),
        (party_slot_eq, "p_yourlair", slot_lair_improve, 3),
        (party_set_slot, "p_yourlair", slot_lair_improve, 4), #second stage finished
    ]),
    ###
    
    (0.1, #chief mainquest doccinga coastal assault
      [(neq, "$campaign_type", camp_sandbox),(neq, "$campaign_type", camp_lordc),(neq, "$campaign_type", camp_kingc),
        (map_free), #en mapa
        (quest_slot_eq,"qst_kennemer_mission_3",slot_quest_current_state, 2),
        (jump_to_menu,"mnu_doccinga_messenger"),
        
    ]),
    
    #Accumulate taxes
    (24 * 7, #back to native times and similar system with VC changes. Way too player complains about new system
      [
        (try_for_range, ":center_no", centers_begin, centers_end),
          ##	(party_get_slot, ":accumulated_rents", ":center_no", slot_center_accumulated_rents),
          ##	(assign, ":cur_rents", 0),
          #Collect taxes for another week
          (try_begin),
            (party_slot_ge, ":center_no", slot_town_lord, 0), #unassigned centers do not accumulate rents
            (party_get_slot, ":accumulated_rents", ":center_no", slot_center_accumulated_rents),
            (assign, ":cur_rents", 0),
            (try_begin),
              (party_slot_eq, ":center_no", slot_party_type, spt_village),
              (try_begin),
                (party_slot_eq, ":center_no", slot_village_state, svs_normal),
                (assign, ":cur_rents", 1700),
              (try_end),
            (else_try),
              (neg|party_slot_ge, ":center_no", slot_party_looted_left_days, 1),
              (party_slot_eq, ":center_no", slot_party_type, spt_castle),
              (assign, ":cur_rents", 2200),
            (else_try),
              (neg|party_slot_ge, ":center_no", slot_party_looted_left_days, 1),
              (party_slot_eq, ":center_no", slot_party_type, spt_town),
              (assign, ":cur_rents", 3600),
            (try_end),
            
            (party_get_slot, ":prosperity", ":center_no", slot_town_prosperity), #prosperty changes between 0..100
            (store_add, ":multiplier", 20, ":prosperity"), #multiplier changes between 20..120
            (val_mul, ":cur_rents", ":multiplier"),
            (val_div, ":cur_rents", 120),#Prosperity of 100 gives the default values
            #TAXES relgion chief cambia. Religion de player affect to Taxes player gets in center.
            (try_begin),
              (party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
              (party_get_slot, ":faith", ":center_no", slot_center_faithratio),
              (store_sub, ":p_faith", 100, ":faith"),
              (try_begin),
                (eq, "$g_player_faith", 1),
                (val_div, ":p_faith", 2),
                (val_add, ":faith", ":p_faith"),
                (val_mul, ":cur_rents", ":faith"),
                (val_div, ":cur_rents", 100),
              (else_try),
                (eq, "$g_player_faith", 2), #es pagano
                (val_div, ":faith", 2),
                (val_add, ":p_faith", ":faith"),
                (val_mul, ":cur_rents", ":p_faith"),
                (val_div, ":cur_rents", 100),
              (try_end),
            (try_end),
            #(try_end),
            #TAXES end
            
            #chief empieza rentas con black smith
            (try_begin), #castles maintenance is expensive  -- castle = small town
              (party_slot_eq, ":center_no", slot_party_type, spt_castle),
              (party_slot_eq, ":center_no", slot_center_has_blacksmith, 1),
              (val_add, ":cur_rents", 300),
            (try_end),
            (try_begin),
              (party_slot_eq, ":center_no", slot_town_port, 1),
              (party_slot_eq, ":center_no", slot_center_has_slavemarket, 1),
              (val_add, ":cur_rents", 800),
            (try_end),
            (try_begin),
              (party_slot_eq, ":center_no", slot_center_has_brewery, 1),
              (val_add, ":cur_rents", 200),
            (try_end),
            (try_begin), #advoid negatives valours
              (lt, ":cur_rents", 0),
              (assign, ":cur_rents", 0),
            (try_end),
            #rentas acaba
            (try_begin),
              (party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
              (options_get_campaign_ai, ":reduce_campaign_ai"), #moto chief
              (try_begin),
                (eq, ":reduce_campaign_ai", 0), #hard (less money from rents)
                (val_mul, ":cur_rents", 3),
                (val_div, ":cur_rents", 4),
              (else_try),
                (eq, ":reduce_campaign_ai", 1), #medium (normal money from rents)
                #same
              (else_try),
                (eq, ":reduce_campaign_ai", 2), #easy (more money from rents)
                (val_mul, ":cur_rents", 4),
                (val_div, ":cur_rents", 3),
              (try_end),
              ###kingdom taxes system faction screen
              (try_begin),
                #			(eq, "$tax_rate", 2), #High
                (party_slot_eq, ":center_no", slot_center_tax_rate, 2),#high
                (val_mul, ":cur_rents", 4),
                (val_div, ":cur_rents", 3),
              (else_try),
                #			(eq, "$tax_rate", 1), #Low
                (party_slot_eq, ":center_no", slot_center_tax_rate, 1),#low
                (val_mul, ":cur_rents", 3),
                (val_div, ":cur_rents", 4),
              (try_end),
            (try_end),
            
            (val_add, ":accumulated_rents", ":cur_rents"), #cur rents changes between 23..1000
            (party_set_slot, ":center_no", slot_center_accumulated_rents, ":accumulated_rents"),
          (try_end),
          
          (try_begin),
            (is_between, ":center_no", villages_begin, villages_end),
            (party_get_slot, ":bound_castle", ":center_no", slot_village_bound_center),
            (party_slot_ge, ":bound_castle", slot_town_lord, 0), #unassigned centers do not accumulate rents
            (is_between, ":bound_castle", castles_begin, castles_end),
            (party_get_slot, ":accumulated_rents", ":bound_castle", slot_center_accumulated_rents), #castle's accumulated rents
            (val_add, ":accumulated_rents", ":cur_rents"), #add village's rent to castle rents
            (party_set_slot, ":bound_castle", slot_center_accumulated_rents, ":accumulated_rents"),
          (try_end),
        (try_end),
      ]
    ),
    
    (24,
      [
      ]
    ),
    
    # Check escape hero prisoners in lairs. No lords in player lair chief
    (12, #before was 4
      [
        (try_begin),
          (party_is_active, "p_troop_camp_1"),
          (call_script, "script_randomly_make_prisoner_heroes_escape_from_party", "p_troop_camp_1", 990),
        (end_try),
        (try_begin),
          (party_is_active, "p_troop_camp_2"),
          (call_script, "script_randomly_make_prisoner_heroes_escape_from_party", "p_troop_camp_2", 990),
        (end_try),
        
        (assign, "$g_campaign_death", 0), #recovery to normal status player death. chief
        ###too troops in lair = desertions
        (try_begin),
          (party_is_active, "p_yourlair"),
          (call_script, "script_randomly_make_prisoner_heroes_escape_from_party", "p_yourlair", 990),
          (party_get_num_companions,":companions", "p_yourlair"),
          (call_script,"script_game_get_lair_garrison_limit","p_yourlair"),
          (assign, ":limit", reg0),
          (try_begin),
            (gt, ":companions", ":limit"),
            (store_random_in_range, ":p_leave", 2, 6),
            (assign, ":num_troops", ":p_leave"),
            (try_for_range, ":unused", 0, ":num_troops"),
              (call_script, "script_cf_party_remove_random_regular_troop", "p_yourlair"),
            (try_end),
            (tutorial_box, "@There are too many men in your Refuge. Some of them became unhappy and deserted!", "@Refuge Garrison"),
            (display_message,"@There are too many men in your Refuge. Some of them became unhappy and deserted!",0xFFFF0000),
          (try_end),
        (try_end),
    ]),
    
    (24, #emboscada ambush, jarl of kennemer revenge chief
      [(neq, "$campaign_type", camp_sandbox),(neq, "$campaign_type", camp_lordc),(neq, "$campaign_type", camp_kingc),
        (map_free), #en mapa
        (eq, "$kennemer_revenge", 1), #enabled
        # (eq, "$g_player_icon_state", pis_camping),
        (party_get_current_terrain,":terrain","p_main_party"),
        (neq,":terrain",0),
        (neq,":terrain",7),
        (neq,":terrain",8),
        
        (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
        (assign, ":num_men", 0),
        (try_for_range, ":i_stack", 0, ":num_stacks"),
          (party_stack_get_size, ":stack_size","p_main_party",":i_stack"),
          (val_add, ":num_men", ":stack_size"),
        (try_end),
        (try_begin),
          (gt, ":num_men", 30), #player has 30 or more men
          (quest_slot_eq,"qst_kennemer_jarl_missions",slot_quest_current_state, 1), #Jarl enemigo
          (set_spawn_radius, 0),
          (spawn_around_party,"p_main_party","pt_kennemer_revenge"),
          (party_set_ai_behavior, "pt_kennemer_revenge", ai_bhvr_attack_party),
          (party_set_ai_object,"pt_kennemer_revenge","p_main_party"),
          (quest_set_slot,"qst_kennemer_jarl_missions",slot_quest_current_state, 3), #
          (assign, "$kennemer_revenge", 0), #disable
        (try_end),
        (try_begin),
          (gt, ":num_men", 30), #player has 30 or more men
          (quest_slot_eq,"qst_kennemer_jarl_missions",slot_quest_current_state, 2), #Jarl enemigo
          (quest_set_slot,"qst_kennemer_jarl_missions",slot_quest_current_state, 3), #Jarl enemigo
          (assign, "$kennemer_revenge", 0), #disable
        (try_end),
    ]),
    #STrig 120
    (12, #emboscada ambush, jarl of kennemer revenge chief
      [(neq, "$campaign_type", camp_sandbox),(neq, "$campaign_type", camp_lordc),(neq, "$campaign_type", camp_kingc),
        (map_free), #en mapa
        (check_quest_active,"qst_kennemer_jarl_missions"),
        (party_get_current_terrain,":terrain","p_main_party"),
        (neq,":terrain",0),
        (neq,":terrain",7),
        (neq,":terrain",8),
        (try_begin),
          (eq, "$kennemer_revenge", 2), #enabled
          # (eq, "$g_player_icon_state", pis_camping),
          (jump_to_menu,"mnu_ambush_kennemer"),
          (assign, "$kennemer_revenge", 0), #disable
        (try_end),
    ]),
    # training player
    # Moved from 36 trigger
    (24 * 5, [
      (try_begin),
        (eq, "$hire_trainer1", hire_trainer1),
        (eq, "$g_trainerlair_training_center", "p_yourlair"),
        (party_is_active, "p_yourlair"),
        
        (call_script, "script_cf_process_training_fail", "p_yourlair", "$g_trainerlair_training_type"),
        (str_store_party_name, s1, "p_yourlair"),
        (display_message, "@You receive word that the trainer at {s1} has completed his task."),
        (assign, "$g_trainerlair_training_center", -1),
        (assign, "$g_trainerlair_training_type", 0),
      (try_end),
      
      (try_begin),
        (faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_active),
        (faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
        
        (neq, "$g_trainerlair_training_center2", -1),
        (store_faction_of_party, ":faction", "$g_trainerlair_training_center2"),
        (eq, ":faction",  "fac_player_supporters_faction"),
        
        (call_script, "script_cf_process_training_fail", "$g_trainerlair_training_center2", "$g_trainerlair_training_type2"),
        (str_store_party_name, s1, "$g_trainerlair_training_center2"),
        (display_message, "@You receive word that the trainer at {s1} has completed his task."),
        (assign, "$g_trainerlair_training_center2", -1),
        (assign, "$g_trainerlair_training_type2", 0),
      (try_end),
    ]),

    (24 * 5, [
      (try_for_parties, ":party"),
        (party_slot_eq, ":party", slot_party_bribed, 1),
        (party_set_slot, ":party", slot_party_bribed, 0),
      (try_end),
    ]),
    ###
    (24, #put off to avoid savegames problem.
      [
    ]),
    
    # EACH HOUR TRIGGER FOR STORY QUESTS
    (1,
      [(neq, "$campaign_type", camp_sandbox),(neq, "$campaign_type", camp_lordc),(neq, "$campaign_type", camp_kingc),
        (map_free), #en mapa
        (party_get_current_terrain,":terrain","p_main_party"),
        (neq,":terrain",0),
        (neq,":terrain",7),
        (neq,":terrain",8),
        (try_begin),
          (check_quest_active,"qst_sven_lair"),
          (quest_slot_eq,"qst_sven_lair",slot_quest_current_state, 5), #despues de lair
          (main_party_has_troop,"trp_npc3"), #brunhild
          (jump_to_menu,"mnu_conversacion_companions1"),
          (assign, "$kennemer_revenge", 2), #active jarl of kennemer revenge / ambush join Solveig
        (try_end),
        (try_begin),
          (check_quest_active,"qst_danmork_protection"),
          (neg|main_party_has_troop,"trp_npc2"), #egil
          (jump_to_menu,"mnu_egil_conversacion"),
        (try_end),
        (try_begin),
          (check_quest_active,"qst_bodo_letter"),
          (quest_get_slot,":stage","qst_bodo_letter",slot_quest_current_state),
          (ge, ":stage", 4),
          #(quest_slot_eq,"qst_bodo_letter",slot_quest_current_state, 4),
          (neg|main_party_has_troop,"trp_npc15"), #aghatinos
          (jump_to_menu,"mnu_aghatinos_conversacion"),
        (try_end),
        (try_begin),
          (check_quest_active,"qst_the_holmgang"),
          (quest_slot_eq,"qst_the_holmgang",slot_quest_current_state, 33),
          (jump_to_menu,"mnu_the_holmgang3"),
        (try_end),
        (try_begin),
          (check_quest_active,"qst_the_holmgang"),
          (quest_slot_eq,"qst_the_holmgang",slot_quest_current_state, 3),
          #(neg|main_party_has_troop,"trp_npc3"), #Brunhild
          (jump_to_menu,"mnu_conversacion_companions2"),
        (try_end),
        (try_begin),
          (check_quest_active,"qst_kennemer_jarl_missions"),
          (quest_slot_eq,"qst_kennemer_jarl_missions",slot_quest_current_state, 8),
          (neg|main_party_has_troop,"trp_npc11"), #solveig
          (jump_to_menu, "mnu_ambush_kennemer"),
        (try_end),
        ##	  (try_begin),
        ##                (check_quest_active,"qst_aescesdun"),
        ##                (quest_slot_eq,"qst_aescesdun",slot_quest_current_state, 19), #conversation where Sven bull neck is
        ##                (quest_set_slot,"qst_aescesdun",slot_quest_current_state, 20),
        ##		(jump_to_menu,"mnu_svenbn_hunting"),
        ##            (try_end),
    ]),
    
    (48, #quest the Thing
      [(neq, "$campaign_type", camp_sandbox),(neq, "$campaign_type", camp_lordc),(neq, "$campaign_type", camp_kingc),
        (map_free), #en mapa
        (party_get_current_terrain,":terrain","p_main_party"),
        (neq,":terrain",0),
        (neq,":terrain",7),
        (neq,":terrain",8),
        (check_quest_active,"qst_the_thing"),
        (quest_slot_eq,"qst_the_thing",slot_quest_current_state, 1),
        (jump_to_menu,"mnu_thething_messenger"),
    ]),
    
    (8, #quest the holmgang
      [(neq, "$campaign_type", camp_sandbox),(neq, "$campaign_type", camp_lordc),(neq, "$campaign_type", camp_kingc),
        (map_free),
        (party_get_current_terrain,":terrain","p_main_party"),
        (neq,":terrain",0),
        (neq,":terrain",7),
        (neq,":terrain",8),
        
        (try_begin),
          (check_quest_active,"qst_the_holmgang"),
          (quest_get_slot,":stage","qst_the_holmgang",slot_quest_current_state),
          (this_or_next|eq,":stage",1),
          (eq,":stage",2),
          (jump_to_menu,"mnu_the_holmgang"),
        (try_end),
        (try_begin),
          (quest_slot_eq,"qst_sven_traitor",slot_quest_current_state, 4), #despues de nothingaham
          (main_party_has_troop,"trp_npc6"), #bodo
          (jump_to_menu,"mnu_conversacion_companionsbodo_choice"),
        (try_end),
        (try_begin),
          (check_quest_active,"qst_revenge_sigurd"),
          (try_begin),
            (quest_slot_eq,"qst_revenge_sigurd",slot_quest_current_state, 2),
            (jump_to_menu,"mnu_doccinga_messenger2"),
          (try_end),
          (try_begin),
            (check_quest_active,"qst_kennemer_jarl_missions"),
            (quest_slot_eq,"qst_revenge_sigurd",slot_quest_current_state, 3),
            (quest_get_slot, ":quest_current_state", "qst_kennemer_jarl_missions", slot_quest_current_state),
            (ge, ":quest_current_state", 1),
            (call_script, "script_change_player_relation_with_faction", "fac_kingdom_4", -50),
            (assign, "$kennemer_revenge", 1), #enable party attack
            (jump_to_menu,"mnu_frisa_proscrito"),
          (try_end),
        (try_end),
    ]),
    
    
    (24,
      [
    ]),
    
    # THIS IS ONLY A TEST TO HIDE SPECIAL LORDS AND BRING THEM BACK
    (1,
      [(neq, "$campaign_type", camp_sandbox),(neq, "$campaign_type", camp_lordc),(neq, "$campaign_type", camp_kingc),
        (map_free),
        (neq, "$g_lord_hide", 2),
        (neq, "$g_lord_hide", -2),
        (try_begin),
          (eq, "$g_lord_hide", 1),
          (assign, "$g_lord_hide", 2),
          (set_fixed_point_multiplier, 100),
          (position_set_x, pos1, -40862),
          (position_set_y, pos1, 20281),
          (position_set_x, pos2, -40854),
          (position_set_y, pos2, 19350),
          (try_for_parties, ":party_no"),
            (call_script, "script_cf_is_hide_party", ":party_no"),
            (try_begin),
              (party_stack_get_troop_id, ":party_leader", ":party_no", 0),
              (this_or_next|eq, ":party_leader", "trp_kingdom_5_lord"),
              (is_between, ":party_leader", "trp_knight_5_1", "trp_knight_5_6"),
              (party_set_position, ":party_no", pos1),
            (else_try),
              (party_set_position, ":party_no", pos2),
            (end_try),
          (try_end),
          (ge, "$cheat_mode", 1),
          (display_message, "@TEST: I moved Lords to St Helena."),
        (else_try),
          (eq, "$g_lord_hide", -1),
          (assign, "$g_lord_hide", -2),
          (try_for_parties, ":party_no"),
            (call_script, "script_cf_is_hide_party", ":party_no"),
            (party_relocate_near_party, ":party_no", "p_castle_9", 2),
          (try_end),
          (ge, "$cheat_mode", 1),
          (display_message, "@TEST: I bring Lords back."),
        (try_end),
    ]),
    
    
    ##  (1, #no accesible place for lords while Nothingam siege mainquest
    ##   [
    ##			(eq, 0, 1),	#disable for testing
    ##              (this_or_next|check_quest_active,"qst_sven_traitor"),
    ##              (check_quest_active,"qst_the_fleet"),
    ##
    ###		(call_script, "script_change_troop_faction", ":troop_no", "fac_outlaws"),
    ##
    ##    ###disable lords
    ##          (try_for_parties, ":party_no"),
    ##            (party_slot_eq, ":party_no", slot_party_type, spt_kingdom_hero_party),
    ##              (party_is_active, ":party_no"),
    ##		(party_stack_get_troop_id, ":party_leader", ":party_no", 0),
    ##		(troop_is_hero, ":party_leader"),
    ##
    ####       (party_get_num_attached_parties, ":num_attached_parties", ":party_no"),
    ####      (try_for_range_backwards, ":attached_party_rank", 0, ":num_attached_parties"),
    ####        (party_get_attached_party_with_rank, ":attached_party", ":root_party", ":attached_party_rank"),
    ####        (party_detach, ":attached_party"),
    ####      (try_end),
    ##              ##                 (party_get_attached_to, ":attached_to_party", ":party_no"),
    ####                 (assign, ":party_is_in_town", 0),
    ####                  (try_begin),
    ####                    (is_between, ":attached_to_party", centers_begin, centers_end),
    ####                     (assign, ":party_is_in_town", ":attached_to_party"),
    ####                  (try_end),
    ##               #vikings lords
    ##             (try_begin), #lord move inaccesible map part
    ##		(is_between, ":party_leader", "trp_knight_8_13", "trp_knight_8_15"),
    ##	        (party_relocate_near_party, ":party_no", "p_dhorak_keep", 2),
    ####              (gt, ":party_is_in_town", 0),
    ####              (party_detach, ":party_no"),
    ##             (try_end),
    ##
    ##             (try_begin), #lord move inaccesible map part
    ##		(eq, ":party_leader", "trp_knight_8_7"),
    ##	        (party_relocate_near_party, ":party_no", "p_dhorak_keep", 2),
    ##             (try_end),
    ##
    ##             (try_begin), #lord move inaccesible map part
    ##		(eq, ":party_leader", "trp_kingdom_8_lord"),
    ##	        (party_relocate_near_party, ":party_no", "p_dhorak_keep", 2),
    ##             (try_end),
    ###saxons y mercians lords
    ##             (try_begin), #lord move inaccesible map part
    ##		(is_between, ":party_leader", "trp_knight_5_1", "trp_knight_5_3"),
    ##	        (party_relocate_near_party, ":party_no", "p_four_ways_inn", 2),
    ##             (try_end),
    ##
    ##             (try_begin), #lord move inaccesible map part
    ##		(eq, ":party_leader", "trp_kingdom_7_lord"),
    ##	        (party_relocate_near_party, ":party_no", "p_four_ways_inn", 2),
    ##             (try_end),
    ##
    ##             (try_begin), #lord move inaccesible map part
    ##		(eq, ":party_leader", "trp_kingdom_5_lord"),
    ##	        (party_relocate_near_party, ":party_no", "p_four_ways_inn", 2),
    ##             (try_end),
    ##          (try_end),
    ##       ]),
    
    ###war and peace enter kingdoms in mainquest
    ##  (48,
    ##   [
    ##              (this_or_next|check_quest_active,"qst_sven_traitor"),
    ##              (check_quest_active,"qst_the_fleet"),
    ##
    ##			    (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", "fac_kingdom_5", "fac_kingdom_8"),
    ##             # -1 faction_1 has a casus belli against faction_2. 1, faction_1 has a truce with faction_2, -2, the two factions are at war
    ##	        (assign, ":war_peace_truce_status", reg0),
    ##		(neq, ":war_peace_truce_status", -2),
    ##
    ###mierce and wessex vs Northanhymbre
    ##   (call_script, "script_diplomacy_start_war_between_kingdoms", "fac_kingdom_5", "fac_kingdom_8", logent_faction_declares_war_to_respond_to_provocation),	#MOTO chief pass log entries
    ##   (call_script, "script_diplomacy_start_war_between_kingdoms", "fac_kingdom_7", "fac_kingdom_8", logent_faction_declares_war_to_respond_to_provocation),	#MOTO chief pass log entries
    ##       ]),
    ###
    ##  (10000, #lords back
    ##   [
    ##
    ##              (check_quest_active,"qst_sven_traitor"),
    ##              (quest_slot_eq,"qst_sven_traitor",slot_quest_current_state, 4),
    ##
    #####wessex, mierce peace with Ragnar's son
    ####             (try_begin), #lord move inaccesible map part
    ####		(call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", "fac_kingdom_5", "fac_kingdom_8"),
    ####             # -1 faction_1 has a casus belli against faction_2. 1, faction_1 has a truce with faction_2, -2, the two factions are at war
    ####	        (assign, ":war_peace_truce_status", reg0),
    ####		(eq, ":war_peace_truce_status", -2),
    ####                 (call_script, "script_diplomacy_start_peace_between_kingdoms", "fac_kingdom_5", "fac_kingdom_8", 1),
    ####                 (call_script, "script_diplomacy_start_peace_between_kingdoms", "fac_kingdom_7", "fac_kingdom_8", 1),
    ####             (try_end),
    ##
    ##    ###back lords
    ##          (try_for_parties, ":party_no"),
    ##            (party_slot_eq, ":party_no", slot_party_type, spt_kingdom_hero_party),
    ##              (party_is_active, ":party_no"),
    ##		(party_stack_get_troop_id, ":party_leader", ":party_no", 0),
    ##		(troop_is_hero, ":party_leader"),
    ###vikings lords
    ####	        (party_relocate_near_party, "p_four_ways_inn", "p_castle_9", 4),
    ####	        (party_relocate_near_party, "p_dhorak_keep", "p_castle_9", 4),
    ##             (try_begin), #lord move inaccesible map part
    ##		(is_between, ":party_leader", "trp_knight_8_13", "trp_knight_8_15"),
    ##	        (party_relocate_near_party, ":party_no", "p_castle_9", 2),
    ##             (try_end),
    ##
    ##             (try_begin), #lord move inaccesible map part
    ##		(eq, ":party_leader", "trp_knight_8_7"),
    ##	        (party_relocate_near_party, ":party_no", "p_castle_9", 2),
    ##             (try_end),
    ##
    ##             (try_begin), #lord move inaccesible map part
    ##		(eq, ":party_leader", "trp_kingdom_8_lord"),
    ##	        (party_relocate_near_party, ":party_no", "p_castle_9", 2),
    ##             (try_end),
    ###saxons y mercians lords
    ##             (try_begin), #lord move inaccesible map part
    ##		(is_between, ":party_leader", "trp_knight_5_1", "trp_knight_5_3"),
    ##	        (party_relocate_near_party, ":party_no", "p_castle_9", 2),
    ##             (try_end),
    ##
    ##             (try_begin), #lord move inaccesible map part
    ##		(eq, ":party_leader", "trp_kingdom_7_lord"),
    ##	        (party_relocate_near_party, ":party_no", "p_castle_9", 2),
    ##             (try_end),
    ##
    ##             (try_begin), #lord move inaccesible map part
    ##		(eq, ":party_leader", "trp_kingdom_5_lord"),
    ##	        (party_relocate_near_party, ":party_no", "p_castle_9", 2),
    ##             (try_end),
    ##          (try_end),
    ##       ]),
    
    ###skills begin
    ###chief asigna lvl de skill segun numero de tropas, para prisioneros
    ## modified by JuJu70
    (2 , #chief
      [(map_free),
        #     (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
        #    (assign, ":num_men", 0),
        #    (try_for_range, ":i_stack", 0, ":num_stacks"),
        #     (party_stack_get_size, ":stack_size","p_main_party",":i_stack"),
        #     (val_add, ":num_men", ":stack_size"),
        #   (try_end),
        (store_party_size_wo_prisoners, ":num_men", "p_main_party"),
        (try_begin),
          (lt, ":num_men", 50),
          (call_script, "script_player_set_skill_level", "skl_prisoner_management", 1),
        (else_try),
          (is_between, ":num_men", 50, 100),
          (call_script, "script_player_set_skill_level", "skl_prisoner_management", 2),
        (else_try),
          (is_between, ":num_men", 100, 150),
          (call_script, "script_player_set_skill_level", "skl_prisoner_management", 3),
        (else_try),
          (is_between, ":num_men", 150, 200),
          (call_script, "script_player_set_skill_level", "skl_prisoner_management", 4),
        (else_try),
          (is_between, ":num_men", 200, 275),
          (call_script, "script_player_set_skill_level", "skl_prisoner_management", 5),
        (else_try),
          (is_between, ":num_men", 275, 350),
          (call_script, "script_player_set_skill_level", "skl_prisoner_management", 6),
        (else_try),
          (is_between, ":num_men", 350, 425),
          (call_script, "script_player_set_skill_level", "skl_prisoner_management", 7),
        (else_try),
          (is_between, ":num_men", 425, 500),
          (call_script, "script_player_set_skill_level", "skl_prisoner_management", 8),
        (else_try),
          (is_between, ":num_men", 500, 575),
          (call_script, "script_player_set_skill_level", "skl_prisoner_management", 9),
        (else_try),
          (call_script, "script_player_set_skill_level", "skl_prisoner_management", 10),
        (try_end),
    ]),
    ###
    #STrig 130
    ###chief asigna shield skill to weapon master and control force camp to max 4.
    (12 , #chief
      [(map_free),
        (store_skill_level, ":weapon_master", "skl_weapon_master", "trp_player"),
        # (store_skill_level, ":training_skill", "skl_fake_training", "trp_player"),
        #shield
        (try_begin),
          (gt, ":weapon_master", 0),
          (le, ":weapon_master", 3),
          (call_script, "script_player_set_skill_level", "skl_shield", 1),
        (else_try),
          (le, ":weapon_master", 6),
          (call_script, "script_player_set_skill_level", "skl_shield", 2),
        (else_try),
          (le, ":weapon_master", 9),
          (call_script, "script_player_set_skill_level", "skl_shield", 3),
        (else_try),
          (ge, ":weapon_master", 10),
          (call_script, "script_player_set_skill_level", "skl_shield", 4),
        (else_try),
          (call_script, "script_player_set_skill_level", "skl_shield", 0),
        (try_end),
        ###training
        ##      (try_begin),
        ##       (gt, ":training_skill", 0),
        ##       (le, ":training_skill", 2),
        ##                (call_script, "script_player_set_skill_level", "skl_trainer", 1),
        ##      (else_try),
        ##       (le, ":training_skill", 4),
        ##                (call_script, "script_player_set_skill_level", "skl_trainer", 2),
        ##      (else_try),
        ##       (le, ":training_skill", 6),
        ##                (call_script, "script_player_set_skill_level", "skl_trainer", 3),
        ##      (else_try),
        ##       (le, ":training_skill", 8),
        ##                (call_script, "script_player_set_skill_level", "skl_trainer", 4),
        ##      (else_try),
        ##       (ge, ":training_skill", 9),
        ##                (call_script, "script_player_set_skill_level", "skl_trainer", 5),
        ##      (else_try),
        ##                (call_script, "script_player_set_skill_level", "skl_trainer", 0),
        ##      (try_end),
        
        (try_for_range, ":troop_no", companions_begin, companions_end),
          (store_skill_level, ":weapon_masterc", "skl_weapon_master", ":troop_no"),
          #  (store_skill_level, ":training_skillc", "skl_fake_training", ":troop_no"),
          #shield
          (try_begin),
            (le, ":weapon_masterc", 0),
            (store_skill_level, ":troop_sklevel", "skl_shield", ":troop_no"),
            (assign, ":new_skill", 0),
            (val_sub, ":new_skill", ":troop_sklevel"),
            (troop_raise_skill, ":troop_no","skl_shield",":new_skill"),
          (else_try),
            (le, ":weapon_masterc", 3),
            (store_skill_level, ":troop_sklevel", "skl_shield", ":troop_no"),
            (assign, ":new_skill", 1),
            (val_sub, ":new_skill", ":troop_sklevel"),
            (troop_raise_skill, ":troop_no","skl_shield",":new_skill"),
          (else_try),
            (le, ":weapon_masterc", 6),
            (store_skill_level, ":troop_sklevel", "skl_shield", ":troop_no"),
            (assign, ":new_skill", 2),
            (val_sub, ":new_skill", ":troop_sklevel"),
            (troop_raise_skill, ":troop_no","skl_shield",":new_skill"),
          (else_try),
            (le, ":weapon_masterc", 9),
            (store_skill_level, ":troop_sklevel", "skl_shield", ":troop_no"),
            (assign, ":new_skill", 3),
            (val_sub, ":new_skill", ":troop_sklevel"),
            (troop_raise_skill, ":troop_no","skl_shield",":new_skill"),
          (else_try),
            #    (ge, ":weapon_masterc", 10),
            (store_skill_level, ":troop_sklevel", "skl_shield", ":troop_no"),
            (assign, ":new_skill", 4),
            (val_sub, ":new_skill", ":troop_sklevel"),
            (troop_raise_skill, ":troop_no","skl_shield",":new_skill"),
          (try_end),
          ##    #training
          ##      (try_begin),
          ##         (le, ":training_skillc", 0),
          ##           (store_skill_level, ":troop_sklevel", "skl_trainer", ":troop_no"),
          ##           (assign, ":new_skill", 0),
          ##           (val_sub, ":new_skill", ":troop_sklevel"),
          ##           (troop_raise_skill, ":troop_no","skl_trainer",":new_skill"),
          ##       (else_try),
          ##          (le, ":training_skillc", 2),
          ##           (store_skill_level, ":troop_sklevel", "skl_trainer", ":troop_no"),
          ##           (assign, ":new_skill", 1),
          ##           (val_sub, ":new_skill", ":troop_sklevel"),
          ##           (troop_raise_skill, ":troop_no","skl_trainer",":new_skill"),
          ##      (else_try),
          ##          (le, ":training_skillc", 4),
          ##           (store_skill_level, ":troop_sklevel", "skl_trainer", ":troop_no"),
          ##           (assign, ":new_skill", 2),
          ##           (val_sub, ":new_skill", ":troop_sklevel"),
          ##           (troop_raise_skill, ":troop_no","skl_trainer",":new_skill"),
          ##      (else_try),
          ##          (le, ":training_skillc", 6),
          ##           (store_skill_level, ":troop_sklevel", "skl_trainer", ":troop_no"),
          ##           (assign, ":new_skill", 3),
          ##           (val_sub, ":new_skill", ":troop_sklevel"),
          ##           (troop_raise_skill, ":troop_no","skl_trainer",":new_skill"),
          ##      (else_try),
          ##          (le, ":training_skillc", 8),
          ##           (store_skill_level, ":troop_sklevel", "skl_trainer", ":troop_no"),
          ##           (assign, ":new_skill", 4),
          ##           (val_sub, ":new_skill", ":troop_sklevel"),
          ##           (troop_raise_skill, ":troop_no","skl_trainer",":new_skill"),
          ##      (else_try),
          ##          #(ge, ":training_skillc", 9),
          ##           (store_skill_level, ":troop_sklevel", "skl_trainer", ":troop_no"),
          ##           (assign, ":new_skill", 5),
          ##           (val_sub, ":new_skill", ":troop_sklevel"),
          ##           (troop_raise_skill, ":troop_no","skl_trainer",":new_skill"),
          ##      (try_end),
        (try_end),
        
    ]),
    ######skills end
    
    # Phaiak begin
    # trait system
    (33.3,
      [(map_free),
        (try_begin),
          (eq, "$player_trait", 0),
          (store_current_day, ":day"),
          (gt, ":day", 20),
          (store_character_level, ":level", "trp_player"),
          (ge, ":level", 13),
          (jump_to_menu, "mnu_player_trait"),
        (end_try),
        
        # Piggybacking:
        (call_script, "script_remove_sea_parties_on_land"),
        (call_script, "script_map_sea_ai_1"),
        
        (assign, "$g_recruit_attempt", 0),
    ]),
    
    
    # VC auto travel system + NEW: AI landing in general
    (0.7,
      [
        (set_fixed_point_multiplier, 100),
        
        (try_begin),
          (neq, "$travel_town", 0),
          (eq, "$g_player_is_captive", 1),
          (party_get_slot, ":target_port", "$travel_town", slot_party_port_party),
          #(party_get_position, pos2, "$travel_town"),
          (party_get_position, pos2, ":target_port"),
          (party_get_position, pos1, "p_transporter"),
          (get_distance_between_positions, ":distance", pos1, pos2),
          (le, ":distance", 150),
          (party_get_position, pos3, "$travel_town"),
          (party_set_position, "p_main_party", pos3),
          (set_camera_follow_party, "p_main_party"),
          (rest_for_hours, 0, 0, 0),
          (assign, "$g_player_is_captive", 0),
          #(party_set_flags, "p_transporter", pf_is_ship, 0),
          (disable_party, "p_transporter"),
          #(change_screen_return),
          (try_begin),
            (is_between, "$travel_town", towns_begin, towns_end),
            (store_faction_of_party, ":faction","$travel_town"),
            (store_relation, ":relation", ":faction", "fac_player_faction"),
            (ge, ":relation", 0),	#VC-2270
            (assign, "$auto_enter_town", "$travel_town"),
          (end_try),
          (assign, "$travel_town", 0),
          
          #(store_current_hours, "$g_check_autos_at_hour"),	#new 02.01.14
        (end_try),
        
        # Piggybacking:
        (call_script, "script_map_sea_ai_2"),
        
    ]),
    
    # VC wound system
    (23.8,
      [
        #piggy you know:
        (assign, "$hunted_today", 0),
        
        (try_begin),
          (gt, "$wounded_today", 0),
          (assign, "$wounded_today", 0),
          (this_or_next|quest_slot_ge, slot_quest_int_penalty_fluid_points, 1),
          (this_or_next|quest_slot_ge, slot_quest_cha_penalty_fluid_points, 1),
          (this_or_next|quest_slot_ge, slot_quest_str_penalty_fluid_points, 1),
          (				quest_slot_ge, slot_quest_agi_penalty_fluid_points, 1),
          (tutorial_box, "@Physicians in larger towns can treat the wounds for a price, after which they will heal within a few days. Any negative effects will then be removed.", "@You are wounded"),
        (end_try),
        
        (party_get_skill_level, ":chance", "p_main_party", "skl_wound_treatment"),
        (val_mul, ":chance", 5),
        
        (assign, ":num_last_day", 0),
        (assign, ":num_perma", 0),
        (assign, ":num_cured", 0),
        
        (try_for_range, ":curr_slot", slot_quest_int_penalty_left_days, slot_quest_end_penalty_left_days),
          (quest_get_slot, ":left_days", "qst_vc_wounds", ":curr_slot"),
          (neq, ":left_days", 0),
          (store_add, ":fluid_points_slot", ":curr_slot", 10),
          (quest_get_slot, ":fluid_points", "qst_vc_wounds", ":fluid_points_slot"),
          (store_add, ":perma_points_slot", ":curr_slot", 20),
          (quest_get_slot, ":perma_points", "qst_vc_wounds", ":perma_points_slot"),
          (try_begin),
            (gt, ":left_days", 0),
            # 1. SUFFERING
            (store_random_in_range, ":rand", 1, 101),
            (gt, ":rand", ":chance"),	#wound treat skill can make suffering-time longer
            (val_sub, ":left_days", 1),
            (quest_set_slot, "qst_vc_wounds", ":curr_slot", ":left_days"),
            (try_begin),
              (eq, ":left_days", 1),	#last day
              (val_add, ":num_last_day", ":fluid_points"),
            (else_try),
              (eq, ":left_days", 0),	#perma day
              (val_add, ":num_perma", ":fluid_points"),
              (quest_set_slot, "qst_vc_wounds", ":fluid_points_slot", 0),
              (val_add, ":perma_points", ":fluid_points"),
              (quest_set_slot, "qst_vc_wounds", ":perma_points_slot", ":perma_points"),
            (end_try),
          (else_try),
            (lt, ":left_days", 0),
            # 2. CURING
            (val_add, ":left_days", 1),
            (try_begin),
              (lt, ":left_days", 0),
              (store_random_in_range, ":rand", 1, 101),
              (le, ":rand", ":chance"),	#wound treat skill can make curing-time shorter
              (val_add, ":left_days", 1),
            (try_end),
            (quest_set_slot, "qst_vc_wounds", ":curr_slot", ":left_days"),
            (eq, ":left_days", 0),	#cured
            (val_add, ":num_cured", ":fluid_points"),
            (try_begin),
              (eq, ":fluid_points_slot", slot_quest_int_penalty_fluid_points),
              (troop_raise_attribute, "trp_player", ca_intelligence, ":fluid_points"),
            (else_try),
              (eq, ":fluid_points_slot", slot_quest_cha_penalty_fluid_points),
              (troop_raise_attribute, "trp_player", ca_charisma, ":fluid_points"),
            (else_try),
              (eq, ":fluid_points_slot", slot_quest_str_penalty_fluid_points),
              (troop_raise_attribute, "trp_player", ca_strength, ":fluid_points"),
            (else_try),
              (eq, ":fluid_points_slot", slot_quest_agi_penalty_fluid_points),
              (troop_raise_attribute, "trp_player", ca_agility, ":fluid_points"),
            (end_try),
            (quest_set_slot, "qst_vc_wounds", ":fluid_points_slot", 0),
          (end_try),
        (end_try),
        #(assign, "$wound_system_explained", 0),
        
        #Info message
        (str_clear, s1),
        (try_begin),
          (gt, ":num_last_day", 0),
          (assign, reg7, ":num_last_day"),
          (assign, reg8, reg7),
          (val_min, reg8, 2),
          (val_sub, reg8, 1),	#so it is 0 or 1
          (str_store_string, s1, "@{s1}You have only one day left to take care of {reg7} of your injuries. Visit a physician in a larger town to do so.^^"),
        (end_try),
        (try_begin),
          (gt, ":num_perma", 0),
          (assign, reg7, ":num_perma"),
          (assign, reg8, reg7),
          (val_min, reg8, 2),
          (val_sub, reg8, 1),	#so it is 0 or 1
          (str_store_string, s1, "@{s1}{reg7} of your injuries {reg8?have:has} become permanent because {reg8?they haven't been:it wasn't} tended.^^"),
        (end_try),
        (try_begin),
          (gt, ":num_cured", 0),
          (assign, reg7, ":num_cured"),
          (assign, reg8, reg7),
          (val_min, reg8, 2),
          (val_sub, reg8, 1),	#so it is 0 or 1
          (str_store_string, s1, "@{s1}{reg7} of your wounds {reg8?are:is} cured, and your related abilities aren't limited any more."),
        (end_try),
        (try_begin),
          (neg|str_is_empty, s1),
          (tutorial_box, "@{s1}", "@Wound Report"),
        (end_try),
        
    ]),
    
    # VC shipyard system
    (23.9,
      [
        (try_for_range, ":curr_town", towns_begin, towns_end),
          (party_slot_eq, ":curr_town", slot_town_port, 1),
          (party_get_slot, ":left_days", ":curr_town", slot_party_shipyard_ship_time),
          (gt, ":left_days", 0),
          (val_sub, ":left_days", 1),
          (party_set_slot, ":curr_town", slot_party_shipyard_ship_time, ":left_days"),
          (eq, ":left_days", 0),
          (str_store_party_name, s0, ":curr_town"),
          (tutorial_box, "@A ship has been built for you in {s0}.", "@Ship finished"),
        (try_end),
        
        #piggybacking for VC-804
        (store_add, ":raiders_end", "pt_sea_raiders_ships6", 1),
        (assign, ":troop", "trp_farmer"),
        (try_begin),
          (eq, "$game_started_with_content_update", 1),
          (assign, ":troop", "trp_slave"),
        (end_try),
        (try_for_parties, ":party"),
          (party_get_template_id, ":template_id", ":party"),
          (is_between, ":template_id", "pt_sea_raiders_ships", ":raiders_end"),
          (party_count_companions_of_type, ":num_of_farmers", ":party", ":troop"),
          (ge, ":num_of_farmers", 4),#VC-2892 (avoid ghost ship)
          (party_remove_members, ":party", ":troop", ":num_of_farmers"),
          (val_div, ":num_of_farmers", 4),#VC-2893
          (party_add_members, ":party", "trp_taiga_bandit", ":num_of_farmers"),
        (end_try),
        
    ]),
    
    # VC pillage cool down for towns, forts and monasteries
    (23.7,
      [
        #towns, forts
        (try_for_range, ":curr_center", walled_centers_begin, walled_centers_end),
          (party_get_slot, ":left_days", ":curr_center", slot_party_looted_left_days),
          (gt, ":left_days", 0),
          (val_sub, ":left_days", 1),
          (party_set_slot, ":curr_center", slot_party_looted_left_days, ":left_days"),
          (eq, ":left_days", 0),
          (call_script, "script_change_party_icon_loot_state", ":curr_center", 0),
          (eq, "$cheat_mode", 1),
          (str_store_party_name, s0, ":curr_center"),
          (display_message, "@{s0} has recovered from being raided."),
        (try_end),
        
        #monasteries
        (try_for_range, ":curr_center", "p_monasterio1", "p_yourlair"),
          (party_get_slot, ":left_days", ":curr_center", slot_party_looted_left_days),
          (gt, ":left_days", 0),
          (val_sub, ":left_days", 1),
          (party_set_slot, ":curr_center", slot_party_looted_left_days, ":left_days"),
          (eq, ":left_days", 0),
          (call_script, "script_change_party_icon_loot_state", ":curr_center", 0),
          (try_begin),
            (party_slot_ge, ":curr_center", slot_village_smoke_added, 1),
            (party_set_slot, ":curr_center", slot_village_smoke_added, 0),
            (party_clear_particle_systems, ":curr_center"),
          (end_try),
          (eq, "$cheat_mode", 1),
          (str_store_party_name, s0, ":curr_center"),
          (display_message, "@{s0} has recovered from being raided."),
        (try_end),
        
        #pagan holy sites
        (try_for_range, ":curr_center", "p_paganholysites1", "p_oldpagan_hut"),
          (party_get_slot, ":left_days", ":curr_center", slot_party_looted_left_days),
          (gt, ":left_days", 0),
          (val_sub, ":left_days", 1),
          (party_set_slot, ":curr_center", slot_party_looted_left_days, ":left_days"),
          (eq, ":left_days", 0),
          (call_script, "script_change_party_icon_loot_state", ":curr_center", 0),
          (try_begin),
            (party_slot_ge, ":curr_center", slot_village_smoke_added, 1),
            (party_set_slot, ":curr_center", slot_village_smoke_added, 0),
            (party_clear_particle_systems, ":curr_center"),
          (end_try),
          (eq, "$cheat_mode", 1),
          (str_store_party_name, s0, ":curr_center"),
          (display_message, "@{s0} has recovered from being raided."),
        (try_end),
    ]),
    
    #Apply damage to ships
    (2.1,
      [
        (eq, "$g_player_is_captive", 0),
        (party_slot_eq, "p_main_party", slot_party_on_water, 1),
        
        #piggybacking for VC-1657
        (try_begin),
          (le, "$ship_management_explained", 0),
          (party_slot_ge, "p_main_party", slot_party_2_ship_type, 1),
          (assign, "$ship_management_explained", 1),
          (tutorial_box, "@By now, you have more than one ship. In a sea battle you can give a 'stand ground' or 'charge' command to your ships by giving it to class number nine, like you give commands to a troop class in a field battle. The first troops in your army list will be together with you on the flagship. The other troops will be in the following ships. You can change your flagship in a port and while camping on the sea. If you are next to a coast you can also split your fleet while camping on the sea or search for the closest landing point with a right click on your party.", "@Ship management"),
        (try_end),
        #end
        
        #piggybacking for VC-1298
        (party_get_num_companions, ":num_men_on_ship", "p_main_party"), #added to make sure your men dont complain if you have no men - produno
        (try_begin),
          (ge, ":num_men_on_ship", 2),
          (store_random_in_range, ":rand", 1, 8),
          (eq, ":rand", 1),
          (store_time_of_day, reg12),
          (try_begin),
            (neg|is_between, reg12, 5, 21),
            (display_message, "@Your troops are angry, because they hate to spend the night on sea.", color_bad_news),
            (call_script, "script_change_player_party_morale", -1),
          (else_try),
            (party_get_skill_level, ":navigation_skill", "p_main_party", "skl_navigation"),
            (store_random_in_range, ":rand", 1, 11),
            (ge, ":rand", ":navigation_skill"),
            (display_message, "@Your troops feel uneasy about crossing the sea.", color_bad_news),
            (call_script, "script_change_player_party_morale", -1),
          (try_end),
        (try_end),
        # piggybacking for VC-1298 ends
        
        (try_for_range, ":current_ship_type_slot", slot_party_1_ship_type, slot_party_8_ship_type),
          (party_slot_ge, "p_main_party", ":current_ship_type_slot", 1),
          #getting slots
          (store_add, ":current_ship_name_slot", ":current_ship_type_slot", 10),
          (store_add, ":current_ship_cond_slot", ":current_ship_type_slot", 20),
          (store_add, ":current_ship_prop_slot", ":current_ship_type_slot", 30),
          
          (party_get_slot, ":current_ship_condition", "p_main_party", ":current_ship_cond_slot"),
          (gt, ":current_ship_condition", 0),
          (try_begin),
            (gt, "$beaufort", 6),
            (store_sub, ":chance_in_percent", "$beaufort", 6),
            (val_mul, ":chance_in_percent", ":chance_in_percent"),
            (val_mul, ":chance_in_percent", 2), # 72, 50, 32, 18, 8, 2
          (else_try),
            (assign, ":chance_in_percent", 1),
          (end_try),
          (store_mul, ":chance_in_per_mille", ":chance_in_percent", 10),
          
          # Change chance depending on wood type
          (party_get_slot, ":current_ship_prop", "p_main_party", ":current_ship_prop_slot"),
          (call_script, "script_decode_value", ":current_ship_prop"),
          (assign, ":ship_wood", reg1),
          (try_begin),
            (eq, ":ship_wood", 1),
            (val_mul, ":chance_in_per_mille", 70),
            (val_div, ":chance_in_per_mille", 100),
          (else_try),
            (eq, ":ship_wood", 2),
            (val_mul, ":chance_in_per_mille", 85),
            (val_div, ":chance_in_per_mille", 100),
          (end_try),
          
          (store_random_in_range, ":rand", 1, 1001),
          (try_begin),
            (le, ":rand", ":chance_in_per_mille"),
            # damage
            # (assign, ":damage", "$beaufort", 2),
            # (val_max, ":damage", 1),
            (val_sub, ":current_ship_condition", ":ship_wood"),	#Damage= 3 or 2 or 1(depending on wood quality)
            # ship name
            (party_get_slot, ":current_ship_name", "p_main_party", ":current_ship_name_slot"),
            (try_begin),
              (is_between, ":current_ship_name", "trp_pseudo_troop_01", "trp_pseudo_troop_end"),
              (str_store_troop_name, s1, ":current_ship_name"),
            (else_try),
              (str_store_string, s1, ":current_ship_name"),
            (end_try),
            # type_name
            (party_get_slot, ":current_ship_type", "p_main_party", ":current_ship_type_slot"),
            (call_script,  "script_get_ship_properties", ":current_ship_type"),
            (str_store_string, s7, reg7),
            #
            (try_begin),
              (gt, ":current_ship_condition", 0),
              (party_set_slot, "p_main_party", ":current_ship_cond_slot", ":current_ship_condition"),
              (try_begin),
                #VC-3642: last ship does not get destroyed, so we have to stop showing damage messages
                (assign, ":block", 0),
                (eq, ":current_ship_type_slot", slot_party_1_ship_type),#current ship is first ship
                (party_slot_eq, "p_main_party", slot_party_2_ship_type, 0),#there is no second ship
                (le, ":current_ship_condition", 3),#last ship is on low condition
                (assign, ":block", 1),# don't show message
              (end_try),
              (eq, ":block", 0),
              (display_message, "@Severe weather has damaged the {s1} ({s7})."),
            (else_try),
              #don't destroy last ship (for the moment)
              (eq, ":current_ship_type_slot", slot_party_1_ship_type),
              (party_slot_eq, "p_main_party", slot_party_2_ship_type, 0),
              # (party_set_slot, "p_main_party", ":current_ship_cond_slot", 1), #outcommented. This would show damage massages without really damaging the ship.
              # (display_message, "@Severe weather has damaged the {s1} ({s7})."),
            (else_try),
              (party_set_slot, "p_main_party", ":current_ship_cond_slot", 0),
              (party_set_slot, "p_main_party", ":current_ship_type_slot", 0),
              (display_message, "@Severe weather has destroyed the {s1} ({s7}).", color_bad_news),
              # Now we fill the gap in the entries
              (store_add, ":correction_begin", ":current_ship_type_slot", 1),
              (try_for_range, ":current_ship_type_slot_c", ":correction_begin", slot_party_8_ship_type),
                (party_get_slot, ":ship_type", "p_main_party", ":current_ship_type_slot_c"),
                (neq, ":ship_type", 0),
                (store_add, ":current_ship_name_slot_c", ":current_ship_type_slot_c", 10),
                (store_add, ":current_ship_qual_slot_c", ":current_ship_type_slot_c", 20),
                (store_add, ":current_ship_prop_slot_c", ":current_ship_type_slot_c", 30),
                (party_get_slot, ":ship_name", "p_main_party", ":current_ship_name_slot_c"),
                (party_get_slot, ":ship_qual", "p_main_party", ":current_ship_qual_slot_c"),
                (party_get_slot, ":ship_prop", "p_main_party", ":current_ship_prop_slot_c"),
                
                (store_sub, ":current_ship_type_slot_c_minus_one", ":current_ship_type_slot_c", 1),
                (store_sub, ":current_ship_name_slot_c_minus_one", ":current_ship_name_slot_c", 1),
                (store_sub, ":current_ship_qual_slot_c_minus_one", ":current_ship_qual_slot_c", 1),
                (store_sub, ":current_ship_prop_slot_c_minus_one", ":current_ship_prop_slot_c", 1),
                
                (party_set_slot, "p_main_party", ":current_ship_type_slot_c_minus_one", ":ship_type"),
                (party_set_slot, "p_main_party", ":current_ship_name_slot_c_minus_one", ":ship_name"),
                (party_set_slot, "p_main_party", ":current_ship_qual_slot_c_minus_one", ":ship_qual"),
                (party_set_slot, "p_main_party", ":current_ship_prop_slot_c_minus_one", ":ship_prop"),
                
                (party_set_slot, "p_main_party", ":current_ship_type_slot_c", 0),
                (party_set_slot, "p_main_party", ":current_ship_name_slot_c", 0),
                (party_set_slot, "p_main_party", ":current_ship_qual_slot_c", 0),
                (party_set_slot, "p_main_party", ":current_ship_prop_slot_c", 0),
                
              (end_try),
              #
              (try_begin),
                (call_script, "script_cf_crew_fit_in_ships", "p_main_party"),
              (else_try),
                #(gt, reg3, 0),
                (try_for_range, reg1, 1, reg3),
                  #remove random troop
                  (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
                  (store_random_in_range, ":random_stack", 1, ":num_stacks"),
                  (party_stack_get_troop_id, ":random_stack_troop", "p_main_party", ":random_stack"),
                  (neg|troop_is_hero, ":random_stack_troop"),
                  (party_remove_members, "p_main_party", ":random_stack_troop", 1),
                (end_try),
              (end_try),
            (end_try),
          (end_try),
        (end_try),
    ]),
    
    # season shader reset (fix for VC-463)
    (ti_on_switch_to_map,
      [
        (set_fixed_point_multiplier, 1),
        (set_shader_param_float, "@vSeason", "$shader_season"),
        (stop_all_sounds, 0), #VC-2127
    ]),
    
    (240.1,		# SEASONS (Check all 10 days)
      [
        (store_current_hours, ":hours"),
        (call_script, "script_game_get_date_text", 0, ":hours"),
        
        (try_begin),
          (ge, "$cheat_mode", 1),
        (else_try),
          (is_between, "$g_cur_month", 3, 6), # spring
          (neq, "$shader_season", shader_spring),
          (assign, "$shader_season", shader_spring),
          (jump_to_menu, "mnu_season_change"),
        (else_try),
          (is_between, "$g_cur_month", 6, 9), # summer
          (neq, "$shader_season", shader_summer),
          (assign, "$shader_season", shader_summer),
          (jump_to_menu, "mnu_season_change"),
        (else_try),
          (is_between, "$g_cur_month", 9, 12), # autumn
          (neq, "$shader_season", shader_autumn),
          (assign, "$shader_season", shader_autumn),
          (jump_to_menu, "mnu_season_change"),
        (else_try),
          (this_or_next|eq, "$g_cur_month", 12), # winter
          (is_between, "$g_cur_month", 1, 3), # winter
          (neq, "$shader_season", shader_winter),
          (assign, "$shader_season", shader_winter),
          (jump_to_menu, "mnu_season_change"),
        (end_try),
        
    ]),
    
    (2,		## SIMULATING WEATHER IN NORTH-SEA ACCORDING TO SEASON
      [
        (store_random_in_range, ":random", 1, 6),
        (this_or_next|eq, ":random", 1),
        (this_or_next|eq, "$beaufort", 0),
        (gt, "$beaufort", 10),
        
        (store_random_in_range, ":chance", 1, 101),
        (try_begin),
          (is_between, "$g_cur_month", 3, 6), # spring
          (try_begin),
            (le, ":chance", 3),
            (assign, "$beaufort", 0),
          (else_try),
            (le, ":chance", 35),
            (store_random_in_range, "$beaufort", 1, 4),
          (else_try),
            (le, ":chance", 65),
            (assign, "$beaufort", 4),
          (else_try),
            (le, ":chance", 95),
            (store_random_in_range, "$beaufort", 5, 7),
          (else_try),
            (le, ":chance", 97),
            (assign, "$beaufort", 7),
          (else_try),
            (le, ":chance", 100),
            (store_random_in_range, "$beaufort", 8, 13),
          (end_try),
        (else_try),
          (is_between, "$g_cur_month", 6, 9), # summer
          (try_begin),
            (le, ":chance", 4),
            (assign, "$beaufort", 0),
          (else_try),
            (le, ":chance", 50),
            (store_random_in_range, "$beaufort", 1, 4),
          (else_try),
            (le, ":chance", 72),
            (assign, "$beaufort", 4),
          (else_try),
            (le, ":chance", 95),
            (store_random_in_range, "$beaufort", 5, 7),
          (else_try),
            (le, ":chance", 98),
            (assign, "$beaufort", 7),
          (else_try),
            #(le, ":chance", 100),
            (store_random_in_range, "$beaufort", 8, 13),
          (end_try),
        (else_try),
          (is_between, "$g_cur_month", 9, 12), # autum
          (try_begin),
            (le, ":chance", 1),
            (assign, "$beaufort", 0),
          (else_try),
            (le, ":chance", 20),
            (store_random_in_range, "$beaufort", 1, 4),
          (else_try),
            (le, ":chance", 40),
            (assign, "$beaufort", 4),
          (else_try),
            (le, ":chance", 80),
            (store_random_in_range, "$beaufort", 5, 7),
          (else_try),
            (le, ":chance", 90),
            (assign, "$beaufort", 7),
          (else_try),
            #(le, ":chance", 100),
            (store_random_in_range, "$beaufort", 8, 13),
          (end_try),
        (else_try),
          #(is_between, "$g_cur_month", 12, 3), # winter
          (try_begin),
            (le, ":chance", 1),
            (assign, "$beaufort", 0),
          (else_try),
            (le, ":chance", 15),
            (store_random_in_range, "$beaufort", 1, 4),
          (else_try),
            (le, ":chance", 30),
            (assign, "$beaufort", 4),
          (else_try),
            (le, ":chance", 70),
            (store_random_in_range, "$beaufort", 5, 7),
          (else_try),
            (le, ":chance", 85),
            (assign, "$beaufort", 7),
          (else_try),
            #(le, ":chance", 100),
            (store_random_in_range, "$beaufort", 8, 12),
          (end_try),
        (end_try),
        
        # shader
        (store_sub, reg0, "$beaufort", 1),
        (val_max, reg0, 0),
        (store_div, ":shader_wind_strenght", reg0, 3),  #yields 0-3
        (set_fixed_point_multiplier,1),
        (set_shader_param_float, "@vWindStrength", ":shader_wind_strenght"),
        
        # message
        (try_begin),
          (party_slot_eq, "p_main_party", slot_party_on_water, 1),
          (try_begin),
            (le, "$beaufort", 0),
            (display_message, "@The weather changed to: 'Calm'"),
          (else_try),
            (le, "$beaufort", 3),
            (display_message, "@The weather changed to: 'Light breeze'"),
          (else_try),
            (le, "$beaufort", 4),
            (display_message, "@The weather changed to: 'Moderate breeze'"),
          (else_try),
            (le, "$beaufort", 6),
            (display_message, "@The weather changed to: 'Strong breeze'"),
          (else_try),
            (le, "$beaufort", 7),
            (display_message, "@The weather changed to: 'High wind'"),
          (else_try),
            (le, "$beaufort", 9),
            (display_message, "@The weather changed to: 'Gale'", color_bad_news),
          (else_try),
            (display_message, "@The weather changed to: 'Storm'", color_bad_news),
          (end_try),
          
          # (try_begin),
          # (lt, "$beaufort", 1),
          # (display_message, "@There is no wind."),
          # (else_try),
          # (lt, ":shader_wind_strenght", 1),
          # (display_message, "@The weather is breezy."),
          # (else_try),
          # (lt, ":shader_wind_strenght", 2),
          # (display_message, "@The wind has become a stiff breeze."),
          # (else_try),
          # (lt, ":shader_wind_strenght", 3),
          # (display_message, "@The wind has become a gale."),
          # (else_try),
          # (display_message, "@A storm has started."),
          # (try_end),
        (try_end),
    ]),
    # Phaiak end
    
    # (0.1,#the fleet chief mainquest
    # [
    # # Phaiak has outcommented following 3 lines:
    # # (check_quest_active,"qst_the_fleet"),
    # # (quest_slot_eq,"qst_the_fleet",slot_quest_current_state, 4),
    # # (jump_to_menu, "mnu_partida_ribe_fleet"),
    # ]),
    
    #STrig 140
    (24,
      [
    ]),
    (3, #quest back Frankia
      [(neq, "$campaign_type", camp_sandbox),(neq, "$campaign_type", camp_lordc),(neq, "$campaign_type", camp_kingc),
        (map_free), #en mapa
        (party_get_current_terrain,":terrain","p_main_party"),
        (neq,":terrain",0),
        (neq,":terrain",7),
        (neq,":terrain",8),
        
        ##quest the douar_an_enez contacto madre
        (try_begin),
          (check_quest_active,"qst_douar_an_enez"),
          (quest_get_slot,":stage","qst_douar_an_enez",slot_quest_current_state),
          (eq,":stage",1),
          (jump_to_menu,"mnu_messeger_mothernews"),
        (try_end),
        
        #quest back Frankia
        (try_begin),
          (check_quest_active,"qst_douar_an_enez"),
          (check_quest_succeeded, "qst_douar_an_enez"),
          (jump_to_menu,"mnu_backfrom_frankia"),
        (try_end),
        
        (try_begin),
          (eq, "$player_side", 1), #wessex
          (main_party_has_troop,"trp_npc2"), #egil
          (check_quest_active,"qst_the_alliance"),
          (quest_slot_eq,"qst_the_alliance",slot_quest_current_state, 1), #egil ataca!
          (jump_to_menu,"mnu_egil_rebelion"),
        (try_end),
        (try_begin),
          (eq,"$g_campaign_death",1),
          (assign,"$g_campaign_death",0),
        (try_end),
    ]),
    #mainquest chief controlar castillo
    (24, [ (neq, "$campaign_type", camp_sandbox),(neq, "$campaign_type", camp_lordc),(neq, "$campaign_type", camp_kingc),
        (check_quest_active, "qst_welsh_and_pictish"),
        (quest_get_slot, ":quest_current_state", "qst_welsh_and_pictish", slot_quest_current_state),
        ##       (this_or_next|eq, ":quest_current_state", 1),
        ##       (this_or_next|eq, ":quest_current_state", 2),
        (eq, ":quest_current_state", 1),
        
        #  (quest_get_slot, ":target_center", "qst_welsh_and_pictish", slot_quest_target_center),
        (try_begin),
          (eq, "$player_side", 2), #danish
          (store_faction_of_party, ":center_faction", "p_castle_37"),
        (else_try),
          (eq, "$player_side", 1), #wessex
          (store_faction_of_party, ":center_faction", "p_castle_41"),
        (try_end),
        (try_begin),
          #  (this_or_next|party_slot_eq,":target_center",slot_town_lord, "trp_player"),
          # (this_or_next|eq, ":center_faction", "fac_player_supporters_faction"),
          (eq, ":center_faction", "$players_kingdom"),
          (quest_get_slot, ":left_days", "qst_welsh_and_pictish", slot_quest_target_amount),
          (val_sub, ":left_days", 1),
          (quest_set_slot, "qst_welsh_and_pictish", slot_quest_target_amount, ":left_days"),
          
          (try_begin),
            (lt, ":left_days", 0),
            (assign, ":quest_current_state", 4),
            (quest_set_slot, "qst_welsh_and_pictish", slot_quest_current_state, 4),
            (rest_for_hours, 0, 0, 0), #stop resting
            (jump_to_menu, "mnu_welsh_and_pictish_complete"),
          (try_end),
        (try_end),
    ]),
    
    ##  (6, [ ###war and peace player's support faction and place kingdom faction mainquest
    ##       (check_quest_active, "qst_welsh_and_pictish"),
    ##       (quest_get_slot, ":quest_current_state", "qst_welsh_and_pictish", slot_quest_current_state),
    ##
    ##   (try_begin), #first war
    ##       (eq, ":quest_current_state", 1),
    ##
    ##       (try_begin),
    ##         (eq, "$player_side", 2), #danish
    ##                (store_faction_of_party, ":old_faction", "p_castle_37"),
    ##		(call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", ":old_faction", "fac_kingdom_8"),
    ##             # -1 faction_1 has a casus belli against faction_2. 1, faction_1 has a truce with faction_2, -2, the two factions are at war
    ##	        (assign, ":war_peace_truce_status", reg0),
    ##		(neq, ":war_peace_truce_status", -2),
    ##             #war!
    ##		(neq, ":old_faction", "fac_kingdom_8"),
    ##                (call_script, "script_diplomacy_start_war_between_kingdoms", ":old_faction", "fac_kingdom_8", 1),
    ##	(else_try),
    ##         (eq, "$player_side", 1), #wessex
    ##                (store_faction_of_party, ":old_faction", "p_castle_41"),
    ##		(call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", ":old_faction", "fac_kingdom_5"),
    ##             # -1 faction_1 has a casus belli against faction_2. 1, faction_1 has a truce with faction_2, -2, the two factions are at war
    ##	        (assign, ":war_peace_truce_status", reg0),
    ##		(neq, ":war_peace_truce_status", -2),
    ##             #war!
    ##		(neq, ":old_faction", "fac_kingdom_5"),
    ##                (call_script, "script_diplomacy_start_war_between_kingdoms", ":old_faction", "fac_kingdom_5", 1),
    ##       (try_end),
    ##     (try_end),
    ##
    ####   (try_begin), #Then peace when player get his mission up ###No no, no peace, they are angry, player mission is to weak them, but they have right to try recovery its castle
    ####       (eq, ":quest_current_state", 4),
    ####
    ####       (try_begin),
    ####         (eq, "$player_side", 2), #danish
    ####		(call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", ":cur_kingdom", ":cur_kingdom_2"),
    ####             # -1 faction_1 has a casus belli against faction_2. 1, faction_1 has a truce with faction_2, -2, the two factions are at war
    ####	        (assign, ":war_peace_truce_status", reg0),
    ####		(eq, ":war_peace_truce_status", -2),
    ####             #war!
    ####                (store_faction_of_party, ":old_faction", "p_castle_37"),
    ####		(neq, ":old_faction", "fac_kingdom_8"),
    ####                (call_script, "script_diplomacy_start_peace_between_kingdoms", ":old_faction", "fac_kingdom_8", 1),
    ####	(else_try),
    ####         (eq, "$player_side", 1), #wessex
    ####		(call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", ":cur_kingdom", ":cur_kingdom_2"),
    ####             # -1 faction_1 has a casus belli against faction_2. 1, faction_1 has a truce with faction_2, -2, the two factions are at war
    ####	        (assign, ":war_peace_truce_status", reg0),
    ####		(eq, ":war_peace_truce_status", -2),
    ####             #war!
    ####                (store_faction_of_party, ":old_faction", "p_castle_41"),
    ####		(neq, ":old_faction", "fac_kingdom_5"),
    ####                (call_script, "script_diplomacy_start_peace_between_kingdoms", ":old_faction", "fac_kingdom_5", 1),
    ####       (try_end),
    ####     (try_end),
    ##       ]),
    
    #JuJu70 - no need to scan all centers
    #towns weekly ON AVERAGE
    # Added increase in prosperity for slavemarkets
    (5.8, #recruit sailors chief to old captain in port
      [
        (store_random_in_range, ":center_no", towns_begin, towns_end),
        (try_begin),
          (party_slot_eq,":center_no",slot_town_port, 1),
          (party_slot_eq, ":center_no", slot_center_sailors_troop_amount, -1),
          (party_set_slot, ":center_no", slot_center_sailors_troop_amount, 1),
        (try_end),
        (try_begin),
          (party_slot_eq, ":center_no", slot_center_has_slavemarket, 1),
          (party_slot_eq, ":center_no", slot_center_is_besieged_by, -1), #center not under siege
          (call_script, "script_change_center_prosperity", ":center_no", 2),
          (try_begin),
            (party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
            (call_script, "script_change_player_honor", -1),
            (str_store_party_name, s33, ":center_no"),
            (display_message, "@The operation of the slave market in {s33} reduces your reputation.", color_bad_news),
          (try_end),
        (try_end),
    ]),
    ######followers camp chief
    ###chief esposas ddan moral cada 72 horas Followers camp
    (72,
      [ (map_free), #en mapa
        (eq,"$followers_on",1), #on
        
        (party_get_num_companion_stacks, ":num", "p_main_party"),
        (try_for_range, ":stack_no", 0, ":num"),
          (party_stack_get_troop_id, ":party_troop", "p_main_party", ":stack_no"),
          (is_between,":party_troop","trp_follower_woman","trp_peasant_womandruid"),
          (assign, ":num", 0), #loop breaker
          (party_stack_get_size, ":size", "p_main_party", ":stack_no"),
          (party_stack_get_num_wounded, ":wounded", "p_main_party", ":stack_no"),
          (val_sub, ":size", ":wounded"),
          (try_begin),
            (ge, ":size", 100),
            (assign, ":size", 100),
          (try_end),
          (val_div, ":size", 10),
          (call_script, "script_change_player_party_morale", ":size"),
        (try_end),
    ]),
    ####chief esposas moral acaba
    ###followers camp se activa.
    (48,
      [ (map_free), #en mapa
        (eq,"$followers_on",0), #off
        (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
        (assign, ":num_men", 0),
        (try_for_range, ":i_stack", 0, ":num_stacks"),
          (party_stack_get_size, ":stack_size","p_main_party",":i_stack"),
          (val_add, ":num_men", ":stack_size"),
        (try_end),
        (try_begin),
          (ge, ":num_men", 300), #300 men or more need.
          (jump_to_menu, "mnu_followers_camp_begin"),
        (try_end),
    ]),
    
    (6, #player have 6 hours for recovery their men or followers will run away
      [ (map_free), #en mapa
        (eq,"$followers_on",1), #on
        (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
        (assign, ":num_men", 0),
        (try_for_range, ":i_stack", 0, ":num_stacks"),
          (party_stack_get_size, ":stack_size","p_main_party",":i_stack"),
          (val_add, ":num_men", ":stack_size"),
        (try_end),
        (try_begin),
          (le, ":num_men", 290), #player has less than 290 men. Followers leave
          (jump_to_menu, "mnu_followers_camp_leave"),
        (try_end),
    ]),
    
    (24 * 14,
      [ (map_free), #en mapa
        (eq,"$followers_on",2), #player don't want followers initially. Get to take it 2 weeks later.
        (assign,"$followers_on",0), #off
    ]),
    
    
    ##  (24, [ ###war in East Engla ragnars sons advance over this kingdom
    ##              (this_or_next|check_quest_active,"qst_douar_an_enez"),
    ##              (check_quest_active, "qst_welsh_and_pictish"),
    ##
    ##		  (faction_slot_eq, "fac_kingdom_6", slot_faction_state, sfs_active),
    ##
    ##		(call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", "fac_kingdom_6", "fac_kingdom_8"),
    ##             # -1 faction_1 has a casus belli against faction_2. 1, faction_1 has a truce with faction_2, -2, the two factions are at war
    ##	        (assign, ":war_peace_truce_status", reg0),
    ##		(neq, ":war_peace_truce_status", -2),
    ##             #danish invasion!!!
    ##                (call_script, "script_diplomacy_start_war_between_kingdoms", "fac_kingdom_6", "fac_kingdom_8", 1),
    ##       ]),
    
    ##  (4, [ ###war in East Engla ragnars sons advance over this kingdom
    ##              (check_quest_active,"qst_douar_an_enez"),
    ##       (quest_get_slot, ":quest_current_state", "qst_douar_an_enez", slot_quest_current_state),
    ##       (ge, ":quest_current_state", 10),
    ##
    ##
    ##            (try_begin),
    ##		(call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", "fac_kingdom_5", "fac_kingdom_8"),
    ##             # -1 faction_1 has a casus belli against faction_2. 1, faction_1 has a truce with faction_2, -2, the two factions are at war
    ##	        (assign, ":war_peace_truce_status", reg0),
    ##		(neq, ":war_peace_truce_status", -2),
    ##             #wessex war!!!
    ##                (call_script, "script_diplomacy_start_war_between_kingdoms", "fac_kingdom_5", "fac_kingdom_8", 1),
    ##            (try_end),
    ##           (try_begin),
    ##		(call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", "fac_kingdom_7", "fac_kingdom_8"),
    ##             # -1 faction_1 has a casus belli against faction_2. 1, faction_1 has a truce with faction_2, -2, the two factions are at war
    ##	        (assign, ":war_peace_truce_status", reg0),
    ##		(neq, ":war_peace_truce_status", -2),
    ##             #Mierce war!!!
    ##                (call_script, "script_diplomacy_start_war_between_kingdoms", "fac_kingdom_7", "fac_kingdom_8", 1),
    ##            (try_end),
    ##            ###Danelaw
    ##      (try_for_range, ":center", "p_castle_17", "p_castle_21"),
    ##                (store_faction_of_party, ":old_faction", ":center"),
    ##		(neq, ":old_faction", "fac_kingdom_8"),
    ##                (call_script, "script_give_center_to_faction", ":center", "fac_kingdom_8"),
    ##      (try_end),
    ##           (try_begin),
    ##                (store_faction_of_party, ":old_faction", "p_town_12"),
    ##		(neq, ":old_faction", "fac_kingdom_8"),
    ##                (call_script, "script_give_center_to_faction", "p_town_12", "fac_kingdom_8"),
    ##           (try_end),
    ##
    #####moving vikings to lundenwic for wessex invasion
    ##
    ##          (try_for_parties, ":party_no"),
    ##             (le, ":quest_current_state", 15), #only before player get mission when he arriaves land.
    ##            (party_slot_eq, ":party_no", slot_party_type, spt_kingdom_hero_party),
    ##              (party_is_active, ":party_no"),
    ##		(party_stack_get_troop_id, ":party_leader", ":party_no", 0),
    ##		(troop_is_hero, ":party_leader"),
    ###vikings lords
    ##             (try_begin),
    ##		(is_between, ":party_leader", "trp_knight_8_8", "trp_knight_8_15"),
    ##	        (party_relocate_near_party, ":party_no", "p_town_12", 4),
    ##             (try_end),
    ##             (try_begin),
    ##		(eq, ":party_leader", "trp_knight_8_4"),
    ##	        (party_relocate_near_party, ":party_no", "p_town_12", 4),
    ##             (try_end),
    ##             (try_begin),
    ##		(eq, ":party_leader", "trp_kingdom_8_lord"),
    ##	        (party_relocate_near_party, ":party_no", "p_town_12", 4),
    ##             (try_end),
    ##         (try_end),
    ##
    #####village looted for vikings
    ##      (try_for_range, ":center", villages_begin, villages_end),
    ##		(this_or_next|is_between, ":center", "p_village_13", "p_village_15"),
    ##		(this_or_next|is_between, ":center", "p_village_112", "p_village_114"),
    ##		(this_or_next|is_between, ":center", "p_village_120", "p_village_122"),
    ##		(this_or_next|eq, ":center", "p_village_21"),
    ##		(eq, ":center", "p_village_24"),
    ##                      (call_script, "script_village_set_state",  ":center", svs_looted),
    ##      (try_end),
    ##      ]),
    
    (24, #autosave each 48 hours chief. Cause lag.
      [
        ## (eq, "$autosave_on", 1),
        ##       (map_free), #en mapa
        ##		(neq, "$g_player_is_captive", 1),	# captive or auto port travel
        ##        (auto_save), ###autosavegame
        (eq, "$g_spouse_embarazada", 1), #random time to new oportunity to childs
        (assign, "$g_spouse_embarazada", 0),
    ]),
    
    (24, #quest back Frankia
      [
    ]),
    #STrig 150
    (24,
      [
    ]),
    #####siege warfare simple tiggers ################
    #para saqueo and last druid
    (24 * 5,
      [
        (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
          (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
          (troop_slot_eq, ":troop_no", slot_troop_current_mission, npc_mission_improve_relations),
          (troop_get_slot,":val",":troop_no",slot_troop_days_on_mission),
          (le,":val",0),
          #		(str_store_troop_name, s22, ":troop_no"),
          #		(display_message, "@{s22} reset"),
          (troop_set_slot,":troop_no",slot_troop_current_mission, 0),
        (try_end),
        
    ]),
    #traicion interna and infiltration
    (96,
      [(eq, "$g_empieza_asedio", 1),
        
        (try_begin),
          (eq, "$g_traicion_interna", 1),
          (assign, "$g_traicion_interna", 2),
        (try_end),
        (try_begin),
          (eq, "$g_infiltracion_interna", 1),
          (assign, "$g_infiltracion_interna", 2),
        (try_end),
    ]),
    #pillage and burn nearby farms
    (48,
      [
        (eq, "$g_campos_cercanos", 1),
        (assign, "$g_campos_cercanos", 2),
    ]),
    
    #########
    #restaurar faccion chief
    (30*24*5/(10*12), #MOTO randomize (see below). Idea faction revolt every month on average in end game
                    #takes about 10 attempts to revolt, about 15 average Charisma, which is 7+10 = 17. 22-17 chance of revolt out of 22-10 chances
      [
        (store_skill_level, ":skill", "skl_leadership", "trp_player"),
        (val_min, ":skill", 10),
        (store_attribute_level, ":charisma", "trp_player", ca_charisma),
        (val_div, ":charisma", 2),
        (val_min, ":charisma", 10),
        (store_add, ":testval", ":skill", ":charisma"),
        (store_random_in_range, ":rand", 10, 22), #player starting charisma 9
        
        (try_begin),
          (lt, ":testval", ":rand"),  #player loses control
          
          (store_random_in_range, ":original_faction", npc_kingdoms_begin, npc_kingdoms_end),
          (try_begin),
            (eq, "$cheat_mode", 1),
            # (try_for_range, ":faction_no", npc_kingdoms_begin, npc_kingdoms_end),
              # (neg|faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
              # (assign, ":original_faction", ":faction_no"),
            # (try_end),
            
            (store_current_day, reg1),
            (str_store_faction_name,s1,":original_faction"),
            (display_message, "@DEBUG rebellion: checking faction {s1} on day {reg1}"),
          (try_end),
          (neg|faction_slot_eq, ":original_faction", slot_faction_state, sfs_active),
          
          (store_sub, ":original_king", ":original_faction", npc_kingdoms_begin),
          (val_add, ":original_king", kings_begin),
          (neg|troop_slot_ge, ":original_king", slot_troop_prisoner_of_party, 0),
          (assign, ":rand", 0), #test condition: no lords to lead revolt
          (assign, ":message_level", 1),  #level of revolt development
          (assign, ":warn_player", 0),
          (assign, ":end_lord", lords_end),
          (try_for_range, ":cur_troop", active_npcs_begin, ":end_lord"),  #NPCs, kings, lords
            (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
            (troop_slot_eq, ":cur_troop", slot_troop_original_faction, ":original_faction"),
            
            (store_troop_faction, ":faction_no", ":cur_troop"),
            (is_between,  ":faction_no", kingdoms_begin, kingdoms_end), #exclude defeated kings, who are in fac_commoners, and adventurers
            (neq, ":faction_no", ":original_faction"),
            
            (assign, ":num_walled_centers", 0),
            (try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
              (party_slot_eq, ":walled_center", slot_town_lord, ":cur_troop"),
              (val_add, ":num_walled_centers", 1),
            (try_end),
            (store_random_in_range, ":rand", 1, 4), #1-3
            (try_begin),
              (gt, ":num_walled_centers", 0), ## has a walled center, so he has support behind for rebellion.
              (store_random_in_range, reg0, -1, 4), #-1 to 3
              (val_add, reg0, ":num_walled_centers"), #0-4+
              (val_add, ":rand", reg0), #1-7+
            (try_end),
            
            (try_begin),
              (lt, ":rand", 7),
              (try_begin),
                (lt, ":message_level", ":rand"),
                (assign, ":message_level", ":rand"),
              (try_end),
              
            (else_try),
              (faction_get_slot, ":current_leader", ":faction_no", slot_faction_leader), #his current king
              (call_script, "script_troop_get_relation_with_troop", ":current_leader", ":cur_troop"),
              (assign, ":relation_with_currentking", reg0),
              
              (try_begin),
                (gt, ":relation_with_currentking", 10),
                (set_show_messages, 0), #use other message after lord loop
                (call_script, "script_troop_change_relation_with_troop", ":current_leader", ":cur_troop", -30),
                (set_show_messages, 1),
                
                (try_begin),
                  (eq, ":current_leader", "trp_player"),
                  (assign, ":warn_player", 1),
                (else_try),
                  (neq, ":warn_player", 1),
                  (assign, ":warn_player", -1),
                (try_end),
                
              #restoration
              (else_try),
                #transfer leader if needed
                (try_begin),
                  (store_troop_faction, ":faction_no_2", ":original_king"),
                  (neq, ":faction_no_2", ":original_faction"),
                  (call_script, "script_change_troop_faction", ":original_king", ":original_faction"),
                  (faction_set_slot, ":original_faction", slot_faction_leader, ":original_king"),
                (try_end),
                
                (call_script, "script_change_troop_faction", ":cur_troop", ":original_faction"),
                
                #set up other lords for transfer
                (try_for_range, ":cur_troop_2", active_npcs_begin, lords_end),
                  (troop_slot_eq, ":cur_troop_2", slot_troop_occupation, slto_kingdom_hero),
                  (troop_slot_eq, ":cur_troop_2", slot_troop_original_faction, ":original_faction"),
                  (neq, ":cur_troop_2", ":cur_troop"),
                  (neq, ":cur_troop_2", ":original_king"),
                  
                  (store_troop_faction, ":faction_no_2", ":cur_troop_2"),
                  (neq, ":faction_no_2", ":original_faction"),
                  
                  (try_begin),
                    (neg|is_between,  ":faction_no", kingdoms_begin, kingdoms_end), #adventurers etc.
                    (troop_set_slot, ":cur_troop_2", slot_troop_change_to_faction, ":original_faction"),

                  (else_try),
                    #bribe
                    (store_random_in_range,":random_gold",1000,3000),
                    (troop_get_slot, ":wealth", ":cur_troop_2", slot_troop_wealth),
                    (val_add, ":wealth", ":random_gold"),
                    (troop_set_slot, ":cur_troop_2", slot_troop_wealth, ":wealth"),
                    
                    #construct normal distribution
                    (store_random_in_range, ":testval", -45, 45),
                    (store_random_in_range, reg0, -45, 45),
                    (val_add, ":testval", reg0),  #-90 to 90
                    (try_begin),
                      (lt, ":testval", 0),
                      (val_mul, ":testval", -1),  #0 to 90
                    (try_end),
                    (val_div, ":random_gold", 100), #10-29
                    (val_add, ":testval", ":random_gold"),  #relation to overcome with bribe is at least 10, because otherwise they would have started this revolt (see above)
                    
                    (faction_get_slot, ":current_leader_2", ":faction_no_2", slot_faction_leader), #his current king
                    (call_script, "script_troop_get_relation_with_troop", ":current_leader_2", ":cur_troop_2"),
                    (le, reg0, ":testval"),
                    
                    (troop_set_slot, ":cur_troop_2", slot_troop_change_to_faction, ":original_faction"),
                  (try_end),
                (try_end),  #transfer lords
                
                (call_script, "script_add_notification_menu", "mnu_notification_kingdom_reborn", ":cur_troop", ":faction_no"),
                (try_begin),
                  (eq, "$cheat_mode", 1),
                  (store_current_day, reg1),
                  (str_store_faction_name,s1,":original_faction"),
                  (display_message, "@DEBUG rebellion: faction {s1} reborn on day {reg1}"),
                (try_end),
                (assign, ":end_lord", ":cur_troop"),
              (try_end),  #restoration
            (try_end),  #plotting restoration
          (try_end),  #outer troop loop
          
          (try_begin),
            (gt, ":rand", 0), #some plotting happened BUT
            (neq, ":end_lord", lords_end),  #no rebellion
            
            (str_store_troop_name_link, s14, ":original_king"),
            (try_begin),
              (eq, ":warn_player", 1),
              (display_message, "@(Possible Rebellion) Rumors say that {s14} recruits from your kingdom despite your leadership.", 0xFF0000),
            (else_try),
              (eq, ":warn_player", -1),
              (display_message, "@(Possible Rebellion) Rumors say that {s14} will surely attempt to restore his kingdom.", 0xFF0000),
            (else_try),
              (eq, ":message_level", 1),
              (display_message, "@(Possible Rebellion) Rumors say that {s14} is still alive.", 0xFF0000),
            (else_try),
              (eq, ":message_level", 2),
              (display_message, "@(Possible Rebellion) Rumors say that {s14} is stockpiling weapons and is seeking support among the Franks.", 0xFF0000),
            (else_try),
              (eq, ":message_level", 3),
              (display_message, "@(Possible Rebellion) Rumors say that {s14} meets in secret with his faithful.", 0xFF0000),
            (else_try),
              (eq, ":message_level", 4),
              (display_message, "@(Possible Rebellion) Rumors say that people favor the restoration of {s14}.", 0xFF0000),
            (else_try),
              (eq, ":message_level", 5),
              (display_message, "@(Possible Rebellion) Rumors say that {s14} is gathering an army to regain his throne.", 0xFF0000),
            (else_try),
              (eq, ":message_level", 6),
              (display_message, "@(Possible Rebellion) Rumors say that {s14} is stockpiling weapons.", 0xFF0000),
            (try_end),
          (try_end),
        (try_end),  #player loses control
    ]),
    ## restoration end chief
    ###random events siege
    #raciones y enfermedades
    
    (60,
      [
        (eq, "$g_empieza_asedio", 1),
        (neq, "$g_siege_saneamiento", 2),
        (neq, "$g_player_is_captive", 1),
        (neg|troop_slot_ge, "trp_player", slot_troop_prisoner_of_party, 0),
        (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
        (assign, ":num_men", 0),
        (try_for_range, ":i_stack", 0, ":num_stacks"),
          (party_stack_get_size, ":stack_size","p_main_party",":i_stack"),
          (val_add, ":num_men", ":stack_size"),
        (try_end),
        (gt, ":num_men", 30),
        (store_random_in_range, ":rand", 0, 6),
        (try_begin),
          (eq, ":rand", 0),
          (jump_to_menu,"mnu_event_siege_01"),
        (else_try),
          (eq, ":rand", 1),
          (jump_to_menu,"mnu_event_siege_02"),
        (else_try),
          (eq, ":rand", 2),
          (jump_to_menu,"mnu_event_siege_03"),
        (else_try),
          (display_message,"@ "),
        (try_end),
    ]),
    
    #eventos de guerrilla e infiltracion normales y rutina
    (24,
      [
        (eq, "$g_empieza_asedio", 1),
        (neq, "$g_player_is_captive", 1),
        (neg|troop_slot_ge, "trp_player", slot_troop_prisoner_of_party, 0),
        (call_script, "script_party_count_fit_for_battle", "p_main_party"),
        (gt, reg0, 40),
        (store_random_in_range, ":rand", 0, 38),
        (try_begin),
          (eq, ":rand", 0),
          (jump_to_menu,"mnu_event_siege_04"),
        (else_try),
          (eq, ":rand", 1),
          (jump_to_menu,"mnu_event_siege_05"),
        (else_try),
          (eq, ":rand", 2),
          (neg|party_slot_eq,"$g_encountered_party",slot_center_blockaded,2), #con block is no.
          (jump_to_menu,"mnu_event_siege_06"),
        (else_try),
          (eq, ":rand", 3),
          (jump_to_menu,"mnu_event_siege_07"),
        (else_try),
          (eq, ":rand", 4),
          (jump_to_menu,"mnu_event_siege_08"),
        (else_try),
          (eq, ":rand", 5),
          (jump_to_menu,"mnu_event_siege_09"),
        (else_try),
          (eq, ":rand", 6),
          (jump_to_menu,"mnu_event_siege_10"),
        (else_try),
          (eq, ":rand", 7),
          (jump_to_menu,"mnu_event_siege_12"),
        (else_try),
          (eq, ":rand", 8),
          (neg|party_slot_eq,"$g_encountered_party",slot_center_blockaded,2), #con block is no.
          (jump_to_menu,"mnu_event_siege_13"),
        (else_try),
          (eq, ":rand", 9),
          (neg|party_slot_eq,"$g_encountered_party",slot_center_blockaded,2), #con block is no.
          (jump_to_menu,"mnu_event_siege_14"),
        (else_try),
          (eq, ":rand", 10),
          (neg|party_slot_eq,"$g_encountered_party",slot_center_blockaded,2), #con block is no.
          (gt, "$g_campos_cercanos", 0),  #player chose to raid villages
          (jump_to_menu,"mnu_event_siege_15"),
        (else_try),
          (eq, ":rand", 11),
          (neg|party_slot_eq,"$g_encountered_party",slot_center_blockaded,2), #con block is no.
          (jump_to_menu,"mnu_event_siege_16"),
        (else_try),
          (eq, ":rand", 12),
          (neg|party_slot_eq,"$g_encountered_party",slot_center_blockaded,2), #con block is no.
          (jump_to_menu,"mnu_event_siege_17"),
        (else_try),
          (eq, ":rand", 13),
          (jump_to_menu,"mnu_event_siege_18"),
        (else_try),
          (eq, ":rand", 14),
          (jump_to_menu,"mnu_event_siege_22"),
        (else_try),
          (eq, ":rand", 15),
          (jump_to_menu,"mnu_event_siege_24"),
        (else_try),
          (eq, ":rand", 16),
          (jump_to_menu,"mnu_event_siege_25"),
        (else_try),
          (eq, ":rand", 17),
          (jump_to_menu,"mnu_event_siege_26"),
        (else_try),
          (display_message,"@ "),
        (try_end),
    ]),
    
    
    #invierno
    (24,
      [
        (ge, "$g_empieza_asedio", 1),
        (neq, "$g_player_is_captive", 1),
        (this_or_next|eq, "$g_cur_month", 12),
        (this_or_next|eq, "$g_cur_month", 1),
        (eq, "$g_cur_month", 2),
        (neg|troop_slot_ge, "trp_player", slot_troop_prisoner_of_party, 0),
        (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
        (assign, ":num_men", 0),
        (try_for_range, ":i_stack", 0, ":num_stacks"),
          (party_stack_get_size, ":stack_size","p_main_party",":i_stack"),
          (val_add, ":num_men", ":stack_size"),
        (try_end),
        (gt, ":num_men", 30),
        (store_random_in_range, ":rand", 0, 6),
        (try_begin),
          (eq, ":rand", 0),
          (jump_to_menu,"mnu_event_siege_11"),
        (else_try),
          (display_message,"@ "),
        (try_end),
    ]),
    #salidas, asaltos y respuestas
    #atacando defensores circunvallation and equipamiento de asalto
    (24,
      [
        (eq, "$g_empieza_asedio", 1),
        (neq, "$g_player_is_captive", 1),
        (neg|troop_slot_ge, "trp_player", slot_troop_prisoner_of_party, 0),
        (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
        (assign, ":num_men", 0),
        (try_for_range, ":i_stack", 0, ":num_stacks"),
          (party_stack_get_size, ":stack_size","p_main_party",":i_stack"),
          (val_add, ":num_men", ":stack_size"),
        (try_end),
        (gt, ":num_men", 50),
        (store_random_in_range, ":rand", 0, 16),
        (try_begin),
          (eq, ":rand", 0),
          (neg|party_slot_eq,"$g_encountered_party",slot_center_blockaded,0), #con block yes.
          (jump_to_menu,"mnu_event_siege_19"),
        (else_try),
          (eq, ":rand", 1),
          (neg|party_slot_eq,"$g_encountered_party",slot_center_blockaded,0), #con block yes.
          (jump_to_menu,"mnu_event_siege_21"),
        (else_try),
          (eq, ":rand", 2),
          (neg|party_slot_eq,"$g_encountered_party",slot_center_blockaded,0), #con block yes.
          (jump_to_menu,"mnu_event_siege_23"),
        (else_try),
          (eq, ":rand", 3),
          (neg|party_slot_eq,"$g_encountered_party",slot_center_blockaded,0), #con block yes.
          (jump_to_menu,"mnu_event_siege_27"),
        (else_try),
          (eq, ":rand", 4),
          (neq, "$g_siege_method", 0),
          (jump_to_menu,"mnu_event_siege_20"),
        (else_try),
          (eq, ":rand", 5),
          (neg|party_slot_eq,"$g_encountered_party",slot_center_blockaded,0), #con block yes.
          (jump_to_menu,"mnu_event_siege_28"),
        (else_try),
          (eq, ":rand", 6),
          (neg|party_slot_eq,"$g_encountered_party",slot_center_blockaded,0), #con block yes.
          (jump_to_menu,"mnu_event_siege_29"),
        (else_try),
          (display_message,"@ "),
        (try_end),
    ]),
    
    #sucesos duante circunvallation acaba
    ###normal random events
    (24 * 14,
      [(map_free), #en mapa
        (neq, "$g_player_is_captive", 1),
        (neg|troop_slot_ge, "trp_player", slot_troop_prisoner_of_party, 0),
        (neq, "$g_player_icon_state", pis_ship),

        (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
        (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
        (assign, ":num_men", 0),
        (try_for_range, ":i_stack", 0, ":num_stacks"),
          (party_stack_get_size, ":stack_size","p_main_party",":i_stack"),
          (val_add, ":num_men", ":stack_size"),
        (try_end),
        
        (try_begin),
          (ge, ":player_renown", 200),
          (gt, ":num_men", 40),
          (store_random_in_range, ":rand", 0, 28),
          (try_begin),
            (eq, ":rand", 0),
            (jump_to_menu,"mnu_event_01_normal"),
          (else_try),
            (eq, ":rand", 1),
            (jump_to_menu,"mnu_event_02_normal"),
          (else_try),
            (eq, ":rand", 2),
            (jump_to_menu,"mnu_event_03_normal"),
          (else_try),
            (eq, ":rand", 3),
            (jump_to_menu,"mnu_event_04_normal"),
          (else_try),
            (le, ":rand", 8),
            (ge, ":rand", 4),
            (le, "$g_random_eventnorepit", 17),  #no repit some random events
            #no repitable
            (try_begin),
              (eq, "$g_random_eventnorepit", 0),  #no repit some random events
              (jump_to_menu,"mnu_event_05_normal"),
              (val_add, "$g_random_eventnorepit", 1),  #no repit some random events
            (else_try),
              (eq, "$g_random_eventnorepit", 1),  #no repit some random events
              (jump_to_menu,"mnu_event_30_normal"),
              (val_add, "$g_random_eventnorepit", 1),  #no repit some random events
            (else_try),
              (eq, "$g_random_eventnorepit", 2),  #no repit some random events
              (jump_to_menu,"mnu_event_07_normal"),
              (val_add, "$g_random_eventnorepit", 1),  #no repit some random events
            (else_try),
              (eq, "$g_random_eventnorepit", 3),  #no repit some random events
              (jump_to_menu,"mnu_event_29_normal"),
              (val_add, "$g_random_eventnorepit", 1),  #no repit some random events
            (else_try),
              (eq, "$g_random_eventnorepit", 4),  #no repit some random events
              (jump_to_menu,"mnu_event_08_normal"),
              (val_add, "$g_random_eventnorepit", 1),  #no repit some random events
            (else_try),
              (eq, "$g_random_eventnorepit", 5),  #no repit some random events
              (jump_to_menu,"mnu_event_28_normal"),
              (val_add, "$g_random_eventnorepit", 1),  #no repit some random events
            (else_try),
              (eq, "$g_random_eventnorepit", 6),  #no repit some random events
              (jump_to_menu,"mnu_event_12_normal"),
              (val_add, "$g_random_eventnorepit", 1),  #no repit some random events
            (else_try),
              (eq, "$g_random_eventnorepit", 7),  #no repit some random events
              (jump_to_menu,"mnu_event_27_normal"),
              (val_add, "$g_random_eventnorepit", 1),  #no repit some random events
            (else_try),
              (eq, "$g_random_eventnorepit", 8),  #no repit some random events
              (jump_to_menu,"mnu_event_13_normal"),
              (val_add, "$g_random_eventnorepit", 1),  #no repit some random events
            (else_try),
              (eq, "$g_random_eventnorepit", 9),  #no repit some random events
              (jump_to_menu,"mnu_event_26_normal"),
              (val_add, "$g_random_eventnorepit", 1),  #no repit some random events
            (else_try),
              (eq, "$g_random_eventnorepit", 10),  #no repit some random events
              (jump_to_menu,"mnu_event_14_normal"),
              (val_add, "$g_random_eventnorepit", 1),  #no repit some random events
            (else_try),
              (eq, "$g_random_eventnorepit", 11),  #no repit some random events
              (jump_to_menu,"mnu_event_25_normal"),
              (val_add, "$g_random_eventnorepit", 1),  #no repit some random events
            (else_try),
              (eq, "$g_random_eventnorepit", 12),  #no repit some random events
              (jump_to_menu,"mnu_event_16_normal"),
              (val_add, "$g_random_eventnorepit", 1),  #no repit some random events
            (else_try),
              (eq, "$g_random_eventnorepit", 13),  #no repit some random events
              (jump_to_menu,"mnu_event_24_normal"),
              (val_add, "$g_random_eventnorepit", 1),  #no repit some random events
            (else_try),
              (eq, "$g_random_eventnorepit", 14),  #no repit some random events
              (jump_to_menu,"mnu_event_18_normal"),
              (val_add, "$g_random_eventnorepit", 1),  #no repit some random events
            (else_try),
              (eq, "$g_random_eventnorepit", 15),  #no repit some random events
              (jump_to_menu,"mnu_event_23_normal"),
              (val_add, "$g_random_eventnorepit", 1),  #no repit some random events
            (else_try),
              (eq, "$g_random_eventnorepit", 16),  #no repit some random events
              (jump_to_menu,"mnu_event_22_normal"),
              (val_add, "$g_random_eventnorepit", 1),  #no repit some random events
            (else_try),
              (val_add, "$g_random_eventnorepit", 1),  #no repit some random events
            (try_end),
            ###
          (else_try),
            (eq, ":rand", 9),
            (jump_to_menu,"mnu_event_06_normal"),
          (else_try),
            (eq, ":rand", 10),
            (jump_to_menu,"mnu_event_09_normal"),
          (else_try),
            (eq, ":rand", 11),
            (jump_to_menu,"mnu_event_10_normal"),
          (else_try),
            (eq, ":rand", 12),
            (jump_to_menu,"mnu_event_11_normal"),
          (else_try),
            (eq, ":rand", 13),
            (jump_to_menu,"mnu_event_15_normal"),
          (else_try),
            (eq, ":rand", 14),
            (jump_to_menu,"mnu_event_17_normal"),
          (else_try),
            (eq, ":rand", 15),
            (jump_to_menu,"mnu_event_19_normal"),
          (else_try),
            (eq, ":rand", 16),
            (jump_to_menu,"mnu_event_20_normal"),
          (else_try),
            (eq, ":rand", 17),
            (jump_to_menu,"mnu_event_21_normal"),
          (else_try),
            (display_message,"@ "),
          (try_end),
        (try_end),
    ]),
    ###########
    #STrig 160
    ##############
    (24, #Specials
      [
        (eq, "$special1", 0),
        (try_for_range, ":place", walled_centers_begin, walled_centers_end),
          (party_slot_eq, ":place", slot_town_lord, "trp_player"),
          (assign, ":num_heroes_in_dungeon", 0),
          (assign, ":num_heroes_given_parole", 0),
          (party_get_num_prisoner_stacks, ":num_stacks",":place"),
          (try_for_range, ":i_stack", 0, ":num_stacks"),
            (party_prisoner_stack_get_troop_id, ":stack_troop",":place",":i_stack"),
            (troop_is_hero, ":stack_troop"),
            (troop_slot_eq, ":stack_troop", slot_troop_occupation, slto_kingdom_hero),
            (try_begin),
              (call_script, "script_cf_prisoner_offered_parole", ":stack_troop"),
              (val_add, ":num_heroes_given_parole", 1),
            (else_try),
              (val_add, ":num_heroes_in_dungeon", 1),
            (try_end),
          (try_end),
          (ge, ":num_heroes_in_dungeon", 7),
          (assign, "$special1", 1),
          (str_store_party_name, s13, ":place"),
        (try_end),
        # (try_begin),
          # (eq, "$special1", 0),
          # (assign, ":lover", 0),
          # (try_for_range, ":npc", kingdom_ladies_begin, kingdom_ladies_end),
            # (troop_slot_eq, ":npc", slot_troop_lover, "trp_player"),
            # (val_add, ":lover", 1),
          # (try_end),
          # (ge,":lover", 5),
          # (assign, "$special1", 2),
        # (try_end),
        (try_begin),
          (eq, "$special1", 0),
          (assign, ":wine", 0),
          (troop_get_inventory_capacity, ":capacity", "trp_household_possessions"),
          (try_for_range, ":inventory_slot", 0, ":capacity"),
            (troop_get_inventory_slot, ":item", "trp_household_possessions", ":inventory_slot"),
            (eq, ":item", "itm_wine"),
            (val_add, ":wine", 1),
          (try_end),
          (ge, ":wine", 25),
          (assign, "$special1", 3),
        (try_end),
        (try_begin),
          (eq, "$special1", 1),
          (tutorial_box, "@Congratulations! You've managed to imprison seven or more lords at {s13}. You really are a true dungeon master.", "@Dungeon master Achievement"),
          (call_script, "script_change_troop_renown", "trp_player", 50),
        (else_try),
          (eq, "$special1", 2),
          (tutorial_box, "@Congratulations! You've managed to make five or more women your lovers. Ladies must be heads over heels for you, so certainly you must feel proud to be in such a demand. Keep up the good work!", "@Skirt Chaser Achievement"),
          (call_script, "script_change_troop_renown", "trp_player", 30),
          (troop_raise_attribute,"trp_player",ca_charisma, 1),
        (else_try),
          (eq, "$special1", 3),
          (tutorial_box, "@Congratulations! You've managed to tuck away 25 or more barrels of wine in your household storage, a great feat considering you are in the part of the world more known for mead and ale. Either you have a drinking problem, or you are a true wine connoisseur.", "@Wine Connoisseur Achievement"),
          (call_script, "script_change_troop_renown", "trp_player", 20),
        (try_end),
    ]),
    ###diplomacy allies kings decision to join to ally kingdom war or no chief
    (48, #a oportunity each 24-48 h Reclutamiento
      [
        (try_for_range, ":cur_village", villages_begin, villages_end),
          (party_slot_eq, ":cur_village", recruit_permission_need, 2),
          (party_set_slot,":cur_village",recruit_permission_need, 1), #no puede reclutar. Tiene que sobornar.
        (try_end),
        (try_for_range, ":center_no", centers_begin, centers_end),
          (party_slot_eq, ":center_no", recruit_permission_need, 3), #no puede reclutar en 48 horas
          (party_set_slot,":center_no",recruit_permission_need, 0), #puede reclutar.
        (try_end),
        #rewoke player's right to recruit in castles/towns
        (try_begin),
          (eq, "$recruitment_on", 0),
          (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
            (party_slot_eq, ":center_no", recruit_permission_need, 0),
            (party_get_slot, ":town_lord", ":center_no", slot_town_lord),
            (is_between, ":town_lord", active_npcs_begin, active_npcs_end),
            (call_script, "script_troop_get_player_relation", ":town_lord"),
            (lt,reg0, -10),
            (store_random_in_range, ":rand", 0, 100),
            (lt, ":rand", 50),
            (party_set_slot,":center_no",recruit_permission_need, 1),
            (str_store_troop_name, s33, ":town_lord"),
            (str_store_party_name, s34, ":center_no"),
            #(tutorial_box, "@{s33} revokes your right to recruit in {s34} due to bad relations between you two.", "@Recruitment Right Revoked"),
            (display_message,"@{s33} revokes your right to recruit in {s34} due to bad relations between you two.", color_bad_news),
          (try_end),
        (try_end),
        #rewoke player's right to recruit in villages
        (try_for_range, ":center_no", villages_begin, villages_end),
          (party_slot_eq, ":center_no", recruit_permission_need, 0),
          (party_get_slot, ":center_relation", ":center_no", slot_center_player_relation),
          (assign, ":cont", 0),
          (try_begin),
            (lt, ":center_relation", -20),
            (neg|party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
            (party_set_slot,":center_no",recruit_permission_need, 1),
            (str_store_party_name, s34, ":center_no"),
            #(tutorial_box, "@The village leader of {s34} revokes your right to recruit due to bad relations between you and his village.", "@Recruitment Right Revoked"),
            (display_message,"@The village leader of {s34} revokes your right to recruit due to bad relations between you and his village.", color_bad_news),
            (assign, ":cont", 1),
          (try_end),
          (eq, ":cont", 0),
          (party_get_slot, ":town_lord", ":center_no", slot_town_lord),
          (is_between, ":town_lord", active_npcs_begin, active_npcs_end),
          (call_script, "script_troop_get_player_relation", ":town_lord"),
          (lt,reg0, -25),
          (store_random_in_range, ":rand", 0, 100),
          (lt, ":rand", 50),
          (party_set_slot,":center_no",recruit_permission_need, 1),
          (str_store_troop_name, s33, ":town_lord"),
          (str_store_party_name, s34, ":center_no"),
          (display_message,"@{s33} revokes your right to recruit in {s34} due to bad relations between you two.", color_bad_news),
          #(tutorial_box, "@{s33} revokes your right to recruit in {s34} due to bad relations between you two.", "@Recruitment Right Revoked"),
        (try_end),
        (try_begin),
          (troop_get_slot, ":lady", "trp_player", slot_troop_spouse),
          (is_between, ":lady", kingdom_ladies_begin, kingdom_ladies_end),
          (neq, "$players_kingdom", "fac_player_supporters_faction"),
          (troop_get_slot, ":cur_center", ":lady", slot_troop_cur_center),
          
          #		(str_store_troop_name, s33, ":lady"),
          #		(str_store_party_name, s34, ":cur_center"),
          #		(display_log_message, "@{s33} is at {s34}"),
          
          (try_begin),
            (is_between, ":cur_center", walled_centers_begin, walled_centers_end),
            (party_slot_eq, ":cur_center", slot_town_lord, "trp_player"),
          (else_try),
            (assign, ":fiefs", 0),
            (try_for_range, ":player_holdings", walled_centers_begin, walled_centers_end),
              (party_slot_eq, ":player_holdings", slot_town_lord, "trp_player"),
              (val_add, ":fiefs", 1),
            (try_end),
            (try_begin),
              (gt, ":fiefs", 0),
              (assign, ":end", walled_centers_end),
              (try_for_range, ":player_holdings", walled_centers_begin, ":end"),
                (party_slot_eq, ":player_holdings", slot_town_lord, "trp_player"),
                (troop_set_slot, ":lady", slot_troop_cur_center, ":player_holdings"),
                (assign, "$g_player_court", -1),
                #					(str_store_party_name, s34, ":player_holdings"),
                #					(display_log_message, "@{s33} should relocate to {s34}"),
                (assign, "$g_trainerlair_training_center2", -1),
                (assign, "$g_trainerlair_training_type2", 0),
                (assign, ":end", 0),
              (try_end),
            (else_try),
              (eq, ":fiefs", 0),
              (assign, "$g_player_court", -1),
              (assign, "$g_trainerlair_training_center2", -1),
              (assign, "$g_trainerlair_training_type2", 0),
              (troop_get_slot, ":guardian", ":lady", slot_troop_guardian),
              (try_begin),
                (gt, ":guardian", 0),
                (store_faction_of_troop, ":guard_faction",":guardian"),
                (eq, ":guard_faction", "$players_kingdom"),
                (assign, ":fiefg", 0),
                (try_for_range, ":holdings", walled_centers_begin, walled_centers_end),
                  (party_slot_eq, ":holdings", slot_town_lord, ":guardian"),
                  (val_add, ":fiefg", 1),
                (try_end),
                (try_begin),
                  (gt, ":fiefg",0),
                  (assign, ":end", walled_centers_end),
                  (try_for_range, ":holdings", walled_centers_begin, ":end"),
                    (party_slot_eq, ":holdings", slot_town_lord, ":guardian"),
                    (troop_set_slot, ":lady", slot_troop_cur_center, ":holdings"),
                    (assign, ":end", 0),
                  (try_end),
                (else_try),
                  (faction_get_slot, ":king", "$players_kingdom", slot_faction_leader),
                  (assign, ":end", walled_centers_end),
                  (try_for_range, ":holdings", walled_centers_begin, ":end"),
                    (party_slot_eq, ":holdings", slot_town_lord, ":king"),
                    (troop_set_slot, ":lady", slot_troop_cur_center, ":holdings"),
                    (assign, ":end", 0),
                  (try_end),
                (try_end),
              (else_try),
                (faction_get_slot, ":king", "$players_kingdom", slot_faction_leader),
                (assign, ":end", walled_centers_end),
                (try_for_range, ":holdings", walled_centers_begin, ":end"),
                  (party_slot_eq, ":holdings", slot_town_lord, ":king"),
                  (troop_set_slot, ":lady", slot_troop_cur_center, ":holdings"),
                  (assign, ":end", 0),
                (try_end),
              (try_end),
            (try_end),
          (try_end),
        (try_end),
    ]),
    
    (24,
      [
    ]),
    (1,
      [
        (map_free), #en mapa
        (party_get_current_terrain,":terrain","p_main_party"),
        (neq,":terrain",0),
        (neq,":terrain",7),
        (neq,":terrain",8),
        
        (try_begin),
          (eq,"$chest_broken",1),
          (assign,"$chest_broken",0),
        (try_end),
        (try_begin),
          (eq, "$g_hadrianwall_visited", 1),
          (neg|main_party_has_troop,"trp_npc1"),
          (jump_to_menu,"mnu_caio_entry"),
        (try_end),
        (try_begin), #ambush chief effect off
          (gt, "$player_ambushed", 0), #
          (assign, "$player_ambushed", 0),
        (try_end),
        
        (try_begin),
          (eq, "$fortified_camp", 1), #no fortified camp whether player move in world map # also usable for siege fortified camp
          (assign, "$fortified_camp", 0),
        (try_end),
    ]),
    (1, #quest doccinga prisoner back and want to join
      [(neq, "$campaign_type", camp_sandbox),(neq, "$campaign_type", camp_lordc),(neq, "$campaign_type", camp_kingc),
        (map_free), #en mapa
        (party_get_current_terrain,":terrain","p_main_party"),
        (neq,":terrain",0),
        (neq,":terrain",7),
        (neq,":terrain",8),
        (try_begin),
          (check_quest_active,"qst_douar_an_enez"),
          (eq,"$doccinga_prisoner",1),
          (jump_to_menu,"mnu_doccinga_prisonerjoined"),
        (try_end),
        
        (try_begin),#emboscada ambush, saxons near sn mainquest
          (eq,"$saxon_ambush",1),
          (check_quest_active,"qst_the_messengersn"),
          (quest_slot_eq,"qst_the_messengersn",slot_quest_current_state, 6), #Jarl enemigo
          (set_spawn_radius, 4),
          (spawn_around_party,"p_main_party","pt_wessex_patrol"),
          (assign, ":quest_target_party", reg0),
          (quest_set_slot, "qst_the_messengersn", slot_quest_target_party, ":quest_target_party"),
          ##                                  (party_set_ai_behavior, ":quest_target_party", ai_bhvr_hold),
          ##                                 (party_set_ai_object, ":quest_target_party", "p_main_party"),
          ##                                 (party_set_flags, ":quest_target_party", pf_default_behavior, 0),
          (assign, "$g_ally_party", -1),
          (assign,"$saxon_ambush",0),
          #(auto_save),
        (try_end),
    ]),
    
    #game load trigger(165)
    (ti_on_switch_to_map, [
        #init scene, mission, and other globals
        (assign, reg59, "$character_gender"),
        (assign, "$fplayer_agent_no", -1),
        (assign, "$fplayer_team_no", -1),
        (assign, "$player_dog_agent_no", -1), #VC-3602
        (faction_set_note_available, "fac_neutral", 0),  #VC-3786
        (faction_set_note_available, "fac_no_faction", 0),  #VC-3786
        (faction_set_note_available, "fac_player_faction", 0),  #VC-3786
        
        (try_begin),
          (neq,"$on_map",1),
          (assign,"$on_map",1),
        (try_end),
        
        #VC-3947 set ages for companions in case they become heroes
        (try_begin),
          (troop_slot_eq, "trp_npc1", slot_troop_age, 0),
          
          (troop_set_slot, "trp_npc1", slot_troop_age, 17),
          (troop_set_slot, "trp_npc2", slot_troop_age, 29),
          (troop_set_slot, "trp_npc3", slot_troop_age, 18),
          (troop_set_slot, "trp_npc4", slot_troop_age, 35),
          (troop_set_slot, "trp_npc5", slot_troop_age, 29),
          (troop_set_slot, "trp_npc6", slot_troop_age, 43),
          (troop_set_slot, "trp_npc7", slot_troop_age, 21),
          (troop_set_slot, "trp_npc8", slot_troop_age, 40),
          (troop_set_slot, "trp_npc9", slot_troop_age, 34),
          (troop_set_slot, "trp_npc10", slot_troop_age, 38),
          (troop_set_slot, "trp_npc11", slot_troop_age, 27),
          (troop_set_slot, "trp_npc12", slot_troop_age, 36),
          (troop_set_slot, "trp_npc13", slot_troop_age, 30),
          (troop_set_slot, "trp_npc14", slot_troop_age, 26),
          (troop_set_slot, "trp_npc15", slot_troop_age, 65),
          (troop_set_slot, "trp_npc16", slot_troop_age, 63),
        (try_end),
        
        #VC-3910 just remove NPCs that may have been killed in holmgang
        (try_begin),
            (quest_slot_eq,"qst_the_holmgang",slot_quest_current_state, 4), #duel was had with either Egil or Reginhard
            
            (try_begin),
                (troop_slot_eq, "trp_npc2", slot_troop_occupation, slto_inactive),
                (troop_set_slot, "trp_npc2", slot_troop_occupation, slto_dead),
            (try_end),
            
            (quest_slot_eq,"qst_the_alliance",slot_quest_current_state, 12),
            (troop_slot_eq, "trp_npc8", slot_troop_occupation, slto_inactive),
            (troop_set_slot, "trp_npc8", slot_troop_occupation, slto_dead),
        (try_end),
        
        #VC-3909 distinguish unconfirmed defectors to player by making them look like adventurers
        (store_and, reg0, "$first_time", first_time_redo_defectors),
        (try_begin),
          (eq, reg0, 0),
          (val_or, "$first_time", first_time_redo_defectors),
          
          (try_for_range, ":cur_troop", lords_begin, lords_end),
            (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_inactive), #transfer to player pending
            (store_troop_faction, ":cur_troop_faction", ":cur_troop"),
            (eq, ":cur_troop_faction", "fac_player_supporters_faction"),
            
            (call_script, "script_troop_set_title_according_to_faction", ":cur_troop", "fac_player_supporters_faction"), #call with inactive flag now set
            
            # (troop_get_slot, ":troop_party_no", "$g_talk_troop", slot_troop_leaded_party), fails
            # (gt, ":troop_party_no", 0),
            # (party_set_faction, ":troop_party_no", "fac_adventurers"),  #distinguish pending confirm
          (try_end),
        (try_end),
        
        #VC-3875 player's lair follows him/her
        (try_begin),
          (eq, "$lair_on", 1),
          (store_faction_of_party, ":lair_faction", "p_yourlair"),
          
          (try_begin),
            (eq, "$players_kingdom", 0),
            
            (try_begin),
              (neq, ":lair_faction", "fac_player_supporters_faction"),
              (call_script, "script_give_center_to_lord", "p_yourlair", "trp_player", 0),
            (try_end),
            
          (else_try),
            (neq, ":lair_faction", "$players_kingdom"),
            (call_script, "script_give_center_to_lord", "p_yourlair", "trp_player", 0),
          (try_end),
        (try_end),
        
        #VC-3846 reconstruct party faction wrecked by V2.049
        (store_faction_of_party, reg0, "p_paganholysites1"),
        (store_faction_of_party, reg1, "p_castle_90"),
        
        (try_begin),
          (eq, reg0, reg1), #symptom of V2.049 bug is spawn parties set to faction of last walled center
          (jump_to_menu, "mnu_reconstruct_pre2049"),
        (try_end),
        
        #VC-3805
        (troop_set_slot, "trp_npc1", slot_troop_religion, 2), # pagan
        
        #VC-3801
        (try_begin),
          (eq, "$g_player_minister", 0),
          (assign, "$g_player_minister", -1),
        (try_end),
        
        #VC-2097
        (try_begin),
          (ge,"$cam_mode",1),
          (assign,"$cam_mode",0),
          (set_camera_in_first_person, "$cam_first_person_mode"),
        (try_end),
        
        #Debug log:
        (call_script, "script_setup_debug_log"),
        
        (try_begin),
          (ge, "$cheat_mode", 1),
          (ge, "$savegame_id", 1),
          (val_mul, "$savegame_id", -1),
        (try_end),
        
        #VC-3786
        (try_begin),
          (faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_active),
          (eq, "$players_kingdom", 0),
          (assign, "$players_kingdom", "fac_player_supporters_faction"),
          (try_for_range, ":cur_troop", active_npcs_begin, active_npcs_end),
            (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
            (neq, "$supported_pretender", ":cur_troop"),
            (store_troop_faction, ":cur_faction", ":cur_troop"),
            (eq, ":cur_faction", 0),
            (call_script, "script_change_troop_faction", ":cur_troop", "fac_player_supporters_faction"),
          (try_end),
        (try_end),
        
        #VC-3686
        (faction_get_slot, ":religion", "fac_kingdom_1", kingdom_religion_pagana),
        (try_begin),
          (eq, ":religion", 1),
          (faction_set_slot, "fac_kingdom_1", slot_faction_religion, cb3_pagan),
          (faction_set_slot, "fac_kingdom_2", slot_faction_religion, cb3_pagan),
          (faction_set_slot, "fac_kingdom_3", slot_faction_religion, cb3_pagan),
          (faction_set_slot, "fac_kingdom_4", slot_faction_religion, cb3_pagan),
          (faction_set_slot, "fac_kingdom_8", slot_faction_religion, cb3_pagan),
          
          (try_begin),
            (troop_slot_eq, "trp_player", slot_troop_religion, 2), #pagan
            (faction_set_slot, "fac_player_supporters_faction", slot_faction_religion, cb3_pagan),
          (try_end),
          
          (faction_set_slot, "fac_kingdom_1", kingdom_religion_pagana, 0),
        (try_end),
        
        #VC-3653
        (try_begin),
          (party_is_active, "p_destroy3"),
          (init_position, pos1),
          (set_fixed_point_multiplier, 1),
          (position_set_x, pos1, 6),  #see p_aescesdun, which may no longer exist at this point
          (position_set_y, pos1, -207),
          (party_set_position, "p_destroy3", pos1),
        (try_end),
        
        #VC-3634
        (party_set_faction, "p_main_party", "fac_player_faction"),
        
        #VC-3598
        (troop_get_slot, ":spouse", "trp_player", slot_troop_spouse),
        (try_begin),
          (ge, ":spouse", active_npcs_begin),
          (troop_slot_eq, ":spouse", slot_troop_occupation, slto_kingdom_hero),
          (troop_get_slot, ":troop_party_no", ":spouse", slot_troop_leaded_party),
          (ge, ":troop_party_no", 1),
          (party_is_active, ":troop_party_no"),
          (party_get_attached_to, ":in_town", ":troop_party_no"),
          (try_begin),
            (troop_slot_eq, ":spouse", slot_troop_cur_center, ":in_town"),
          (else_try),
            (party_get_cur_town, ":in_town", ":troop_party_no"),
            (troop_slot_eq, ":spouse", slot_troop_cur_center, ":in_town"),
          (else_try),
            (troop_set_slot, ":spouse", slot_troop_cur_center, -1),
          (try_end),
        (try_end),
        
        #VC-3561
        (try_begin),
          (neq, "$g_trainerlair_training_center2", -1),
          (assign, "$g_trainerlair_training_center2", "$g_player_court"),
        (try_end),
        
        #VC-3537
        (try_begin),
          (store_faction_of_party, reg1, "p_troop_camp_1"),
          (neq, reg1, "fac_player_supporters_faction"),
          (party_set_faction, "p_yourlair", "fac_player_supporters_faction"),
          (party_set_faction, "p_troop_camp_1", "fac_player_supporters_faction"),
          (party_set_faction, "p_troop_camp_2", "fac_player_supporters_faction"),
          
          (try_for_parties, ":spawned_party"),
            (party_get_template_id, reg1, ":spawned_party"),
            (eq, reg1, "pt_landet_ships"),
            (party_set_faction, ":spawned_party", "fac_player_supporters_faction"),
          (try_end),
        (try_end),
        
        #VC-3536
        (try_begin),
          (eq, "$current_color", 0),
          (assign, "$current_color", 0xE12126),
        (try_end),
        
        #VC-3494
        (try_begin),
          (party_slot_eq, "p_jetty_4", slot_party_port_party, 0),
          (call_script, "script_add_jetty_system_2"),
        (try_end),
        
        #VC-3468
        (try_begin),
          (neq, "$players_kingdom", "fac_player_supporters_faction"),  #no player kingdom?
          (store_add, ":slot_provocation_days", "fac_player_supporters_faction", slot_faction_provocation_days_with_factions_begin),
          (val_sub, ":slot_provocation_days", kingdoms_begin),
          (try_for_range, ":faction_no", npc_kingdoms_begin, npc_kingdoms_end),
            (store_relation, ":player_relation", ":faction_no", "fac_player_supporters_faction"),
            (lt, ":player_relation", 0),
            (store_mul, ":num_days", ":player_relation", -1),
            (val_min, ":num_days", 30),
            (neg|faction_slot_ge, ":faction_no", ":slot_provocation_days", ":num_days"),
            (faction_set_slot, ":faction_no", ":slot_provocation_days", ":num_days"),
            (set_relation, ":faction_no", "fac_player_supporters_faction", 0),
          (try_end),
          
          #VC-2289
          (faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_inactive),
          (gt, "$g_player_minister", 0),
          
          #portions copied from script_deactivate_player_faction
          (assign, "$players_oath_renounced_against_kingdom", 0),
          (assign, "$players_oath_renounced_given_center", 0),
          (assign, "$players_oath_renounced_begin_time", 0),
          (assign, "$control_tax", 0),
          #(call_script, "script_store_average_center_value_per_faction"),
          (call_script, "script_appoint_faction_marshal", "fac_player_supporters_faction", -1),
          
          #end missions and recall minister
          (try_for_range, ":npc", companions_begin, companions_end),
            (troop_slot_eq, ":npc", slot_troop_occupation, slto_player_companion),
            (troop_set_slot, ":npc", slot_troop_days_on_mission, 0),
            (neg|main_party_has_troop, ":npc"),
            (troop_set_slot, ":npc", slot_troop_current_mission, npc_mission_rejoin_when_possible),
          (try_end),
          
          (try_for_range, ":minister_quest", all_quests_begin, all_quests_end),
            (check_quest_active, ":minister_quest"),
            (quest_slot_eq, ":minister_quest", slot_quest_giver_troop, "$g_player_minister"),
            (call_script, "script_abort_quest", ":minister_quest", 0),
          (try_end),
          
          (assign, "$g_player_minister", -1),
          (call_script, "script_update_all_notes"),
        (try_end),
        
        #VC-3060, 3327
        (try_begin),
          (neg|troop_slot_eq, "trp_banner_background_color_array", 174, arms_lorange),
          (troop_set_slot, "trp_banner_background_color_array", 35, arms_lorange),
          (troop_set_slot, "trp_banner_background_color_array", 45, arms_white),
          (troop_set_slot, "trp_banner_background_color_array", 88, arms_lorange),
          (troop_set_slot, "trp_banner_background_color_array", 143, 0xFFDFA96E),
          (troop_set_slot, "trp_banner_background_color_array", 149, 0xFFDFA96E),
          (troop_set_slot, "trp_banner_background_color_array", 152, arms_lorange),
          (troop_set_slot, "trp_banner_background_color_array", 154, arms_lorange),
          (troop_set_slot, "trp_banner_background_color_array", 159, arms_lorange),
          (troop_set_slot, "trp_banner_background_color_array", 174, arms_lorange),
          (troop_set_slot, "trp_banner_background_color_array", 193, arms_blue),
        (try_end),
        
        #VC-2972
        #Nationality
        (try_begin),
          (faction_slot_eq, "fac_player_supporters_faction",  slot_faction_culture, "fac_culture_norse"),
          (try_begin),
            # (eq,"$nacionalidad_type",cb7_foreigner),
            # (faction_set_slot, "fac_player_supporters_faction",  slot_faction_culture, "fac_culture_norse"),
            # (faction_set_slot, "fac_player_faction",  slot_faction_culture, "fac_culture_norse"),
            # (else_try),
            (eq,"$nacionalidad_type",cb7_scotopict),
            (faction_set_slot, "fac_player_supporters_faction",  slot_faction_culture, "fac_culture_scotch"),
            (faction_set_slot, "fac_player_faction",  slot_faction_culture, "fac_culture_scotch"),
          (else_try),
            (eq,"$nacionalidad_type",cb7_briton),
            (faction_set_slot, "fac_player_supporters_faction",  slot_faction_culture, "fac_culture_welsh"),
            (faction_set_slot, "fac_player_faction",  slot_faction_culture, "fac_culture_welsh"),
          (else_try),
            (eq,"$nacionalidad_type",cb7_irish),
            (faction_set_slot, "fac_player_supporters_faction",  slot_faction_culture, "fac_culture_irish"),
            (faction_set_slot, "fac_player_faction",  slot_faction_culture, "fac_culture_irish"),
            # (else_try),
            # (eq,"$nacionalidad_type",cb7_frisian),
            # (faction_set_slot, "fac_player_supporters_faction",  slot_faction_culture, "fac_culture_norse"),
            # (faction_set_slot, "fac_player_faction",  slot_faction_culture, "fac_culture_norse"),
            # (else_try),
            # (eq,"$nacionalidad_type",cb7_norseman),
            # (faction_set_slot, "fac_player_supporters_faction",  slot_faction_culture, "fac_culture_norse"),
            # (faction_set_slot, "fac_player_faction",  slot_faction_culture, "fac_culture_norse"),
          (else_try),
            (eq,"$nacionalidad_type",cb7_anglesaxon),
            (try_begin),
              (gt, "$g_faction_selected", 0),
              (faction_get_slot, reg1, "$g_faction_selected",  slot_faction_culture),
              (faction_set_slot, "fac_player_supporters_faction",  slot_faction_culture, reg1),
              (faction_set_slot, "fac_player_faction",  slot_faction_culture, reg1),
            (else_try),
              (faction_set_slot, "fac_player_supporters_faction",  slot_faction_culture, "fac_culture_saxon"),
              (faction_set_slot, "fac_player_faction",  slot_faction_culture, "fac_culture_saxon"),
            (try_end),
          (try_end),
        (try_end),
        
        #VC-3040 change food store system after VC 2.0
        (store_and, reg0, "$first_time", first_time_food_store),
        (try_begin),
          (eq, reg0, 0),
          (val_or, "$first_time", first_time_food_store),
          (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
            (party_get_slot, ":town_food_store", ":center_no", slot_party_food_store),
            (call_script, "script_center_get_food_consumption", ":center_no"),
            (val_mul, ":town_food_store", reg0),
            (call_script, "script_center_get_food_consumption_20", ":center_no"),
            (val_div, ":town_food_store", reg0),
            (party_set_slot, ":center_no", slot_party_food_store, ":town_food_store"),
          (try_end),
        (try_end),
        
        #overhaul of spawned parties
        (try_begin),
          (neg|party_slot_eq, "p_mierce_spawn_point", slot_party_spawn_target_spawns, 12),
          
          (try_begin),
            (eq, "$bandit_quantity_option", 0),
            (assign, "$bandit_quantity_option", 1),
          (try_end),
          
          (party_set_slot, "p_clyde_coast_spawn_point", slot_party_bandit_type, "pt_steppe_bandits"), #Northmenn
          (party_set_slot, "p_clyde_coast_spawn_point", slot_party_spawn_target_spawns, 12),
          (party_set_slot, "p_clyde_coast_spawn_point", slot_party_spawn_radius, 30),
          (party_set_slot, "p_clyde_coast_spawn_point", slot_party_spawn_flags, spsf_coastal),
          
          (party_set_slot, "p_fortiu_spawn_point", slot_party_bandit_type, "pt_steppe_bandits"), #Northmenn
          (party_set_slot, "p_fortiu_spawn_point", slot_party_spawn_target_spawns, 12),
          (party_set_slot, "p_fortiu_spawn_point", slot_party_spawn_radius, 40),
          (party_set_slot, "p_fortiu_spawn_point", slot_party_spawn_flags, spsf_coastal),
          
          (party_set_slot, "p_wales_spawn_point", slot_party_bandit_type, "pt_taiga_bandits"), #Vikingarnir
          (party_set_slot, "p_wales_spawn_point", slot_party_spawn_target_spawns, 9),
          (party_set_slot, "p_wales_spawn_point", slot_party_spawn_radius, 40),
          (party_set_slot, "p_wales_spawn_point", slot_party_spawn_flags, spsf_coastal),
          
          (party_set_slot, "p_limerick_spawn_point", slot_party_bandit_type, "pt_taiga_bandits"), #Vikingarnir
          (party_set_slot, "p_limerick_spawn_point", slot_party_spawn_target_spawns, 10),
          (party_set_slot, "p_limerick_spawn_point", slot_party_spawn_radius, 70),
          (party_set_slot, "p_limerick_spawn_point", slot_party_spawn_flags, spsf_coastal),
          
          (party_set_slot, "p_northumbria_spawn_point", slot_party_bandit_type, "pt_forest_bandits"), #Robbers
          (party_set_slot, "p_northumbria_spawn_point", slot_party_spawn_target_spawns, 12),
          (party_set_slot, "p_northumbria_spawn_point", slot_party_spawn_radius, 40),
          
          (party_set_slot, "p_mierce_spawn_point", slot_party_bandit_type, "pt_forest_bandits"), #Robbers
          (party_set_slot, "p_mierce_spawn_point", slot_party_spawn_target_spawns, 12),
          (party_set_slot, "p_mierce_spawn_point", slot_party_spawn_radius, 40),
          
          (party_set_slot, "p_crafu_spawn_point", slot_party_bandit_type, "pt_mountain_bandits"), #Renegades
          (party_set_slot, "p_crafu_spawn_point", slot_party_spawn_target_spawns, 12),
          (party_set_slot, "p_crafu_spawn_point", slot_party_spawn_radius, 40),
          
          (party_set_slot, "p_alban_spawn_point", slot_party_bandit_type, "pt_mountain_bandits"), #Renegades
          (party_set_slot, "p_alban_spawn_point", slot_party_spawn_target_spawns, 12),
          (party_set_slot, "p_alban_spawn_point", slot_party_spawn_radius, 30),
          
          (party_set_slot, "p_aileach_spawn_point", slot_party_bandit_type, "pt_fianna"),
          (party_set_slot, "p_aileach_spawn_point", slot_party_spawn_target_spawns, 8),
          (party_set_slot, "p_aileach_spawn_point", slot_party_spawn_radius, 30),
          
          (party_set_slot, "p_sussex_spawn_point", slot_party_bandit_type, "pt_sea_raiders"), #Masterless Fighters
          (party_set_slot, "p_sussex_spawn_point", slot_party_spawn_target_spawns, 12),
          (party_set_slot, "p_sussex_spawn_point", slot_party_spawn_radius, 35),
          
          (party_set_slot, "p_engla_coast_spawn_point", slot_party_bandit_type, "pt_sea_raiders2"),  #Danish Elite Vikingarnir
          (party_set_slot, "p_engla_coast_spawn_point", slot_party_spawn_target_spawns, 12),
          (party_set_slot, "p_engla_coast_spawn_point", slot_party_spawn_radius, 40),
          (party_set_slot, "p_engla_coast_spawn_point", slot_party_spawn_flags, spsf_coastal),
          
          (party_set_slot, "p_cornish_coast_spawn_point", slot_party_bandit_type, "pt_sea_raiders2"),  #Danish Elite Vikingarnir
          (party_set_slot, "p_cornish_coast_spawn_point", slot_party_spawn_target_spawns, 7),
          (party_set_slot, "p_cornish_coast_spawn_point", slot_party_spawn_radius, 60),
          (party_set_slot, "p_cornish_coast_spawn_point", slot_party_spawn_flags, spsf_coastal),
          
          (party_set_slot, "p_leinster_spawn_point", slot_party_bandit_type, "pt_desert_bandits"), #Veteran Renegades
          (party_set_slot, "p_leinster_spawn_point", slot_party_spawn_target_spawns, 6),
          (party_set_slot, "p_leinster_spawn_point", slot_party_spawn_radius, 40),
          
          (party_set_slot, "p_norway_spawn_point", slot_party_bandit_type, "pt_desert_bandits"), #Veteran Renegades
          (party_set_slot, "p_norway_spawn_point", slot_party_spawn_target_spawns, 8),
          (party_set_slot, "p_norway_spawn_point", slot_party_spawn_radius, 45),
          
          (party_set_slot, "p_frisia_spawn_point", slot_party_bandit_type, "pt_frank_looters_1"), #Thieving Franks
          (party_set_slot, "p_frisia_spawn_point", slot_party_spawn_target_spawns, 6),
          (party_set_slot, "p_frisia_spawn_point", slot_party_spawn_radius, 10),
          
          (party_set_slot, "p_denmark_spawn_point", slot_party_bandit_type, "pt_frank_looters_2"), #Raiding Franks
          (party_set_slot, "p_denmark_spawn_point", slot_party_spawn_target_spawns, 6),
          (party_set_slot, "p_denmark_spawn_point", slot_party_spawn_radius, 25),
          
          (party_set_slot, "p_caitness_priest_spawn_point", slot_party_bandit_type, "pt_paganos_party"),
          (party_set_slot, "p_caitness_priest_spawn_point", slot_party_spawn_target_spawns, 8),
          (party_set_slot, "p_caitness_priest_spawn_point", slot_party_spawn_radius, 50),
          
          (party_set_slot, "p_northumbria_priest_spawn_point", slot_party_bandit_type, "pt_paganos_party"),
          (party_set_slot, "p_northumbria_priest_spawn_point", slot_party_spawn_target_spawns, 8),
          (party_set_slot, "p_northumbria_priest_spawn_point", slot_party_spawn_radius, 70),
          
          (party_set_slot, "p_norway_priest_spawn_point", slot_party_bandit_type, "pt_paganos_party"),
          (party_set_slot, "p_norway_priest_spawn_point", slot_party_spawn_target_spawns, 6),
          (party_set_slot, "p_norway_priest_spawn_point", slot_party_spawn_radius, 50),
          
          (party_set_slot, "p_denmark_priest_spawn_point", slot_party_bandit_type, "pt_paganos_party"),
          (party_set_slot, "p_denmark_priest_spawn_point", slot_party_spawn_target_spawns, 6),
          (party_set_slot, "p_denmark_priest_spawn_point", slot_party_spawn_radius, 45),
          
          (party_set_slot, "p_channel_spawn_point", slot_party_bandit_type, "pt_sea_raiders_ships2"), #Danish Vikingair
          (party_set_slot, "p_channel_spawn_point", slot_party_spawn_target_spawns, 8),
          (party_set_slot, "p_channel_spawn_point", slot_party_spawn_radius, 10),
          (party_set_slot, "p_channel_spawn_point", slot_party_spawn_flags, spsf_seaborne),
          (party_set_slot, "p_channel_spawn_point", slot_party_on_water, 1),
          
          (party_set_slot, "p_bight_spawn_point", slot_party_bandit_type, "pt_sea_raiders_ships"),  #Frankish Raiders
          (party_set_slot, "p_bight_spawn_point", slot_party_spawn_target_spawns, 8),
          (party_set_slot, "p_bight_spawn_point", slot_party_spawn_radius, 25),
          (party_set_slot, "p_bight_spawn_point", slot_party_spawn_flags, spsf_seaborne),
          (party_set_slot, "p_bight_spawn_point", slot_party_on_water, 1),
          
          (party_set_slot, "p_irish_sea_spawn_point", slot_party_bandit_type, "pt_sea_raiders_ships3"), #Vikingr
          (party_set_slot, "p_irish_sea_spawn_point", slot_party_spawn_target_spawns, 8),
          (party_set_slot, "p_irish_sea_spawn_point", slot_party_spawn_radius, 10),
          (party_set_slot, "p_irish_sea_spawn_point", slot_party_spawn_flags, spsf_seaborne),
          (party_set_slot, "p_irish_sea_spawn_point", slot_party_on_water, 1),
          
          (party_set_slot, "p_forth_firth_spawn_point", slot_party_bandit_type, "pt_sea_raiders_ships4"), #Norwegian Vikingr
          (party_set_slot, "p_forth_firth_spawn_point", slot_party_spawn_target_spawns, 6),
          (party_set_slot, "p_forth_firth_spawn_point", slot_party_spawn_radius, 25),
          (party_set_slot, "p_forth_firth_spawn_point", slot_party_spawn_flags, spsf_seaborne),
          (party_set_slot, "p_forth_firth_spawn_point", slot_party_on_water, 1),
          
          (party_set_slot, "p_skagerrak_spawn_point", slot_party_bandit_type, "pt_sea_raiders_ships5"), #Swedish Vikingr
          (party_set_slot, "p_skagerrak_spawn_point", slot_party_spawn_target_spawns, 6),
          (party_set_slot, "p_skagerrak_spawn_point", slot_party_spawn_radius, 25),
          (party_set_slot, "p_skagerrak_spawn_point", slot_party_spawn_flags, spsf_seaborne),
          (party_set_slot, "p_skagerrak_spawn_point", slot_party_on_water, 1),
          
          (party_set_slot, "p_firth_clyde_spawn_point", slot_party_bandit_type, "pt_sea_raiders_ships6"), #Raiders
          (party_set_slot, "p_firth_clyde_spawn_point", slot_party_spawn_target_spawns, 8),
          (party_set_slot, "p_firth_clyde_spawn_point", slot_party_spawn_radius, 30),
          (party_set_slot, "p_firth_clyde_spawn_point", slot_party_spawn_flags, spsf_seaborne),
          (party_set_slot, "p_firth_clyde_spawn_point", slot_party_on_water, 1),
          
          (party_template_set_slot, "pt_steppe_bandits", slot_party_template_lair_type, "pt_steppe_bandit_lair"),
          (party_template_set_slot, "pt_taiga_bandits", slot_party_template_lair_type, "pt_taiga_bandit_lair"),
          (party_template_set_slot, "pt_mountain_bandits", slot_party_template_lair_type, "pt_mountain_bandit_lair"),
          (party_template_set_slot, "pt_forest_bandits", slot_party_template_lair_type, "pt_forest_bandit_lair"),
          (party_template_set_slot, "pt_sea_raiders", slot_party_template_lair_type, "pt_sea_raider_lair"),
          (party_template_set_slot, "pt_sea_raiders2", slot_party_template_lair_type, "pt_sea_raider_lair2"),
          (party_template_set_slot, "pt_desert_bandits", slot_party_template_lair_type, "pt_desert_bandit_lair"),
          (party_template_set_slot, "pt_frank_looters_1", slot_party_template_lair_type, "pt_sea_raider_lair"),
          (party_template_set_slot, "pt_frank_looters_2", slot_party_template_lair_type, "pt_sea_raider_lair"),
          (party_template_set_slot, "pt_fianna", slot_party_template_lair_type, "pt_mountain_bandit_lair"),
          
          #update spawned parties
          (try_for_parties, ":spawned_party"),
            (gt, ":spawned_party", "p_spawn_points_end"),
            (party_is_active, ":spawned_party"),
            
            (party_get_template_id, ":party_temp", ":spawned_party"),
            (this_or_next|is_between, ":party_temp", "pt_steppe_bandits", "pt_deserters"),
            (this_or_next|is_between, ":party_temp", "pt_sea_raiders_ships", "pt_chimney_smoke"),
            (eq, ":party_temp", "pt_paganos_party"),
            
            (party_get_slot, ":home", ":spawned_party", slot_party_spawn_point),
            (try_begin),
              (eq, ":home", 0),
              
              (assign, ":nearest_spawn_point", 0),
              (assign, ":spawn_point_dist", Far_Away),
              
              (try_for_range, ":spawn_point", spawn_points_begin, spawn_points_end),
                (party_slot_eq, ":spawn_point", slot_party_bandit_type, ":party_temp"),
                (store_distance_to_party_from_party, reg0, ":spawned_party", ":spawn_point"),
                (gt, ":spawn_point_dist", reg0),
                (assign, ":spawn_point_dist", reg0),
                (assign, ":nearest_spawn_point", ":spawn_point"),
              (try_end),
              
              (try_begin),
                (neq, ":nearest_spawn_point", 0),
                (party_set_slot, ":spawned_party", slot_party_spawn_point, ":nearest_spawn_point"),
                (party_set_ai_behavior, ":spawned_party", ai_bhvr_patrol_party),
                (party_set_ai_object, ":spawned_party", ":nearest_spawn_point"),
              (try_end),
              
            (else_try),
              (get_party_ai_object, reg1, ":spawned_party"),
              (this_or_next|le, reg1, 0),
              (this_or_next|neq, reg1, ":home"),
              (neg|party_slot_eq, ":home", slot_party_lair_party, reg1),
              (party_set_ai_behavior, ":spawned_party", ai_bhvr_patrol_party),
              (party_set_ai_object, ":spawned_party", ":home"),
            (try_end),
          (try_end),
        (try_end),
        
        #VC-2083 pt_looter_lair (Kidnapper's Hideout for Native Merchant Quest) assigned as lair to destroy
        (store_and, reg0, "$first_time", first_time_check_l2_lairs),
        (try_begin),
          (eq, reg0, 0),
          (val_or, "$first_time", first_time_check_l2_lairs),
          (eq, "$random_quest_no", "qst_destroy_bandit_lair"),
          (quest_get_slot, ":bandit_lair", "qst_destroy_bandit_lair", slot_quest_target_party),
          
          (assign, ":lair_exists", 0),
          (try_for_parties, reg1),
            (eq, reg1, ":bandit_lair"),
            (assign, ":lair_exists", 1),
          (try_end),
          (eq, ":lair_exists", 1),
          
          (party_get_template_id, ":bandit_type", ":bandit_lair"),
          (eq, ":bandit_type", "pt_looter_lair"),
          
          (assign, "$random_quest_no", 0),
          (check_quest_active, "qst_destroy_bandit_lair"),
          (cancel_quest, "qst_destroy_bandit_lair"),
        (try_end),
        
        (store_and, reg0, "$first_time", first_time_check_l_lairs),
        (try_begin),
          (eq, reg0, 0),
          (val_or, "$first_time", first_time_check_l_lairs),
          
          #remove save game lairs
          (try_for_parties, ":spawned_party"),
            (gt, ":spawned_party", "p_spawn_points_end"),
            
            (party_get_template_id, ":party_temp", ":spawned_party"),
            (is_between, ":party_temp", "pt_steppe_bandit_lair", "pt_bandit_lair_templates_end"),
            
            (try_begin),
              (check_quest_active, "qst_destroy_bandit_lair"),
              (quest_slot_eq, "qst_destroy_bandit_lair", slot_quest_target_party, ":spawned_party"),
            (else_try),
              (assign, ":reffed", 0),
              (try_for_range, ":spawn_point", spawn_points_begin, spawn_points_end),
                (party_slot_eq, ":spawn_point", slot_party_lair_party, ":spawned_party"),
                (try_begin),
                  (eq, ":party_temp", "pt_looter_lair"),
                  (party_set_slot, ":spawn_point", slot_party_lair_party, 0),
                (else_try),
                  (assign, ":reffed", 1),
                (try_end),
              (try_end),
              (eq, ":reffed", 0),
              (remove_party, ":spawned_party"),
            (try_end),
          (try_end),
        (try_end),
        
        #compatibility new party order
        (party_get_position, pos0, "p_cornish_coast_spawn_point"),
        (position_get_x, reg1, pos0),
        (try_begin),
          (gt, reg1, 0),  #old order
          (neg|party_slot_eq, "p_aileach_spawn_point", slot_party_bandit_type, "pt_paganos_party"),
          
          (party_set_slot, "p_aileach_spawn_point", slot_party_bandit_type, "pt_paganos_party"),
          (party_set_slot, "p_aileach_spawn_point", slot_party_spawn_target_spawns, 8),
          (party_set_slot, "p_aileach_spawn_point", slot_party_spawn_radius, 30),
          
          (party_set_slot, "p_engla_coast_spawn_point", slot_party_bandit_type, "pt_paganos_party"),
          (party_set_slot, "p_engla_coast_spawn_point", slot_party_spawn_target_spawns, 8),
          (party_set_slot, "p_engla_coast_spawn_point", slot_party_spawn_radius, 30),
          (party_set_slot, "p_engla_coast_spawn_point", slot_party_spawn_flags, 0),
          
          (party_set_slot, "p_cornish_coast_spawn_point", slot_party_bandit_type, "pt_paganos_party"),
          (party_set_slot, "p_cornish_coast_spawn_point", slot_party_spawn_target_spawns, 6),
          (party_set_slot, "p_cornish_coast_spawn_point", slot_party_spawn_radius, 30),
          (party_set_slot, "p_cornish_coast_spawn_point", slot_party_spawn_flags, 0),
          
          (party_set_slot, "p_leinster_spawn_point", slot_party_bandit_type, "pt_paganos_party"),
          (party_set_slot, "p_leinster_spawn_point", slot_party_spawn_target_spawns, 6),
          (party_set_slot, "p_leinster_spawn_point", slot_party_spawn_radius, 30),
          
          (party_set_slot, "p_frisia_spawn_point", slot_party_bandit_type, "pt_sea_raiders"), #Masterless Fighters
          (party_set_slot, "p_frisia_spawn_point", slot_party_spawn_target_spawns, 12),
          (party_set_slot, "p_frisia_spawn_point", slot_party_spawn_radius, 30),
          
          (party_set_slot, "p_denmark_spawn_point", slot_party_bandit_type, "pt_sea_raiders2"),  #Danish Elite Vikingarnir
          (party_set_slot, "p_denmark_spawn_point", slot_party_spawn_target_spawns, 12),
          (party_set_slot, "p_denmark_spawn_point", slot_party_spawn_radius, 60),
          (party_set_slot, "p_denmark_spawn_point", slot_party_spawn_flags, spsf_coastal),
          
          (party_set_slot, "p_caitness_priest_spawn_point", slot_party_bandit_type, "pt_sea_raiders2"),  #Danish Elite Vikingarnir
          (party_set_slot, "p_caitness_priest_spawn_point", slot_party_spawn_target_spawns, 13),
          (party_set_slot, "p_caitness_priest_spawn_point", slot_party_spawn_radius, 60),
          (party_set_slot, "p_caitness_priest_spawn_point", slot_party_spawn_flags, spsf_coastal),
          
          (party_set_slot, "p_northumbria_priest_spawn_point", slot_party_bandit_type, "pt_desert_bandits"), #Veteran Renegades
          (party_set_slot, "p_northumbria_priest_spawn_point", slot_party_spawn_target_spawns, 6),
          (party_set_slot, "p_northumbria_priest_spawn_point", slot_party_spawn_radius, 40),
          
          (party_set_slot, "p_norway_priest_spawn_point", slot_party_bandit_type, "pt_frank_looters_1"), #Thieving Franks
          (party_set_slot, "p_norway_priest_spawn_point", slot_party_spawn_target_spawns, 6),
          (party_set_slot, "p_norway_priest_spawn_point", slot_party_spawn_radius, 10),
          
          (party_set_slot, "p_denmark_priest_spawn_point", slot_party_bandit_type, "pt_frank_looters_2"), #Raiding Franks
          (party_set_slot, "p_denmark_priest_spawn_point", slot_party_spawn_target_spawns, 6),
          (party_set_slot, "p_denmark_priest_spawn_point", slot_party_spawn_radius, 25),
          
          (try_for_parties, ":spawned_party"),
            (gt, ":spawned_party", "p_spawn_points_end"),
            (party_slot_ge, ":spawned_party", slot_party_spawn_point, "p_aileach_spawn_point"),
            (store_add, reg1, "p_denmark_priest_spawn_point", 1),
            (neg|party_slot_ge, ":spawned_party", slot_party_spawn_point, reg1),
            (party_get_battle_opponent, reg1, ":spawned_party"),
            (eq, reg1, -1),
            (remove_party, ":spawned_party"),
          (try_end),
          
          (try_for_range, ":bandit_spawn_point", laired_spawn_points_begin, laired_spawn_points_end),
            (party_get_slot, ":lair", ":bandit_spawn_point", slot_party_lair_party),
            (gt, ":lair", "p_spawn_points_end"),
            (party_set_slot, ":bandit_spawn_point", slot_party_lair_party, 0),
            (remove_party, ":lair"),
          (try_end),
          
          #fix poor spawn point positions
          (party_get_position, pos0, "p_forth_firth_spawn_point"),
          (position_get_x, reg1, pos0),
          (val_add, reg1, 20),
          (position_set_x, pos0, reg1),
          (party_set_position, "p_forth_firth_spawn_point", pos0),
        (try_end),
        
        #possibly outdated banner slots?
        (troop_get_slot, ":delta", "trp_knight_1_1", slot_troop_banner_scene_prop),
        (troop_get_slot, reg0, "trp_knight_1_2", slot_troop_banner_scene_prop),
        (try_begin),
          (neq, ":delta", "spr_banner_viking01"),
          (neq, reg0, "spr_banner_viking02"),
          
          (val_sub, ":delta", "spr_banner_viking01"),
          (val_sub, reg0, "spr_banner_viking02"),
          (val_max, ":delta", reg0),  #if one was reassigned to a lower banner number, this would trap that
          
          (troop_get_slot, ":cur_banner", "trp_player", slot_troop_banner_scene_prop),
          (assign, reg0, ":cur_banner"),
          (val_sub, ":cur_banner", ":delta"),
          (try_begin),
            (ge, ":cur_banner", banner_scene_props_begin),
            (troop_set_slot, "trp_player", slot_troop_banner_scene_prop, ":cur_banner"),
            (val_sub, ":cur_banner", banner_scene_props_begin),
            (val_add, ":cur_banner", banner_map_icons_begin),
            (party_set_banner_icon, "p_main_party", ":cur_banner"),
          (else_try),
            (neq, reg0, 0),
            (display_message, "@fixing banners; please reset your banner"),
          (try_end),
          
          (try_for_range, ":troop", active_npcs_begin, active_npcs_end),
            (troop_get_slot, ":cur_banner", ":troop", slot_troop_banner_scene_prop),
            (assign, reg0, ":cur_banner"),
            (val_sub, ":cur_banner", ":delta"),
            (try_begin),
              (ge, ":cur_banner", banner_scene_props_begin),
              (troop_set_slot, ":troop", slot_troop_banner_scene_prop, ":cur_banner"),
              (val_sub, ":cur_banner", banner_scene_props_begin),
              (val_add, ":cur_banner", banner_map_icons_begin),
              (troop_get_slot, ":party", ":troop", slot_troop_leaded_party),
              (try_begin),
                (gt, ":party", spawn_points_end),
                (party_set_banner_icon, ":party", ":cur_banner"),
              (try_end),
            (else_try),
              (neq, reg0, 0),
              (assign, reg1, ":troop"),
              (display_message, "@unable to restore banner {reg0} assigned to troop {reg1}"),
            (try_end),
          (try_end),
          
          (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
            (troop_get_slot, ":lord_troop_id", ":center_no", slot_town_lord),
            (gt, ":lord_troop_id", active_npcs_begin),
            (troop_get_slot, ":cur_banner", ":lord_troop_id", slot_troop_banner_scene_prop),
            (val_sub, ":cur_banner", banner_scene_props_begin),
            (ge, ":cur_banner", 0),
            (val_add, ":cur_banner", banner_map_icons_begin),
            (party_set_banner_icon, ":center_no", ":cur_banner"),
          (try_end),
        (try_end),
        
        #VC-3588
        (try_begin),
          (item_slot_eq, "itm_tools", slot_item_primary_raw_material, 0),
          (call_script, "script_initialize_item_info"),
        (try_end),
        
        (try_begin),
          (eq, "$bug_fix_version", 0),
          
          #fix for hiding test_scene in older savegames
          (disable_party, "p_test_scene"),
          #fix for correcting town_1 siege type
          (party_set_slot, "p_town_1", slot_center_siege_with_belfry, 0),
          #fix for removing kidnapped girl from party
          (try_begin),
            (neg|check_quest_active, "qst_kidnapped_girl"),
            (party_remove_members, "p_main_party", "trp_kidnapped_girl", 1),
          (try_end),
          #fix for not occupied but belong to a faction lords
          (try_for_range, ":cur_troop", lords_begin, lords_end),
            (try_begin),
              (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_inactive),
              (store_troop_faction, ":cur_troop_faction", ":cur_troop"),
              (is_between, ":cur_troop_faction", "fac_kingdom_1", kingdoms_end),
              (troop_set_slot, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
            (try_end),
          (try_end),
          #fix for an error in 1.105, also fills new slot values
          (call_script, "script_initialize_item_info"),
          
          (assign, "$bug_fix_version", 1),
          
          #VC-3297 fix screening system
        (else_try),
          (eq, "$bug_fix_version", 2),
          (try_for_range, ":troop", active_npcs_begin, active_npcs_end),
            (troop_get_slot, ":troop_party", ":troop", slot_troop_leaded_party),
            (ge, ":troop_party", 0),
            (party_is_active, ":troop_party"),
            (party_slot_eq, ":troop_party", slot_party_ai_state, spai_screening_army),
            (party_set_slot, ":troop_party", slot_party_ai_state, spai_accompanying_army),
            (party_set_slot, ":troop_party", slot_party_ai_substate, 1),
          (try_end),
          (assign, "$bug_fix_version", 3),
        (try_end),
        
        (try_begin),
          # In version 2.003 we added a toggle for weapon break. After updating the game it is off on general.
          # This leaded to confusion in the beta. Here we want to guarantee weapon break for old save games.
          (eq, "$bug_fix_version", 1),
          (assign, "$bug_fix_version", 2),
          (eq, "$game_started_in_version", 2000),
          (assign, "$vc_weapon_break_on", 1),
        (try_end),
        
        # (call_script, "script_initialize_item_info"),
        # religion slots reassignment for 1.03
        # towns/villages
        (try_begin),
          (party_slot_eq, "p_town_4", slot_center_religion, 0),
          (party_slot_eq, "p_town_5", slot_center_religion, 0),
          (try_for_range, ":center_no", centers_begin, centers_end),
            (neg|party_slot_eq, ":center_no", slot_party_type, spt_castle),
            (try_begin),
              (this_or_next|eq,":center_no","p_town_4"),
              (this_or_next|eq,":center_no","p_town_5"),
              (this_or_next|eq,":center_no","p_town_7"),
              (this_or_next|is_between,":center_no","p_village_49","p_village_57"),
              (this_or_next|is_between,":center_no","p_village_60","p_village_63"),
              (this_or_next|is_between,":center_no","p_village_98","p_village_102"),
              (is_between,":center_no","p_village_104","p_village_106"),
              (party_set_slot,":center_no",slot_center_religion, 2),
              (store_random_in_range, ":rand", 5, 40),	# ratio is christian/pagan
              (party_set_slot, ":center_no", slot_center_faithratio, ":rand"),
            (else_try),
              (party_set_slot,":center_no",slot_center_religion, 1), #el resto son cristianos
              (store_random_in_range, ":rand", 30, 60), #valores de fe
              (party_set_slot, ":center_no", slot_center_faithratio, ":rand"),
            (try_end),
          (try_end),
        (try_end),
        
        (store_and, reg0, "$first_time", first_time_fix_centers),
        (try_begin),
          (eq, reg0, 0),
          (val_or, "$first_time", first_time_fix_centers),
          
          (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
            # #VC-3241 fix transferred prisoners  DONE with heavy loop in script_game_event_battle_end
            # (party_get_num_prisoner_stacks, ":num_stacks",":center_no"),
            # (try_for_range, ":stack_no", 0, ":num_stacks"),
              # (party_prisoner_stack_get_troop_id, ":stack_troop",":center_no",":stack_no"),
              # (troop_is_hero, ":stack_troop"),
              # (troop_set_slot, ":stack_troop", slot_troop_prisoner_of_party, ":center_no"),
              # (str_store_troop_name,s1,":stack_troop"),
              # (str_store_party_name,s2,":center_no"),
              # (display_message, "@Troop {s1} now a prisoner of {s2}"),
            # (try_end),
            
            # resetting castles post 1.03b
            (try_begin),
              (is_between, ":center_no", castles_begin, castles_end),
              (party_slot_eq, ":center_no", slot_center_religion, 0),
              (try_begin),
                (this_or_next|is_between,":center_no","p_castle_49","p_castle_57"),
                (is_between,":center_no","p_castle_60","p_castle_63"),
                (party_set_slot,":center_no",slot_center_religion, 2),
                (store_random_in_range, ":rand", 5, 40),	# ratio is christian/pagan
                (party_set_slot, ":center_no", slot_center_faithratio, ":rand"),
              (else_try),
                (party_set_slot,":center_no",slot_center_religion, 1),
                (store_random_in_range, ":rand", 30, 60), #valores de fe
                (party_set_slot, ":center_no", slot_center_faithratio, ":rand"),
              (try_end),
            (try_end),
          (try_end),
          
          #piggyback VC-3550 also in RC2.024
          (try_for_range, ":troop", original_kingdom_heroes_begin, active_npcs_end),
            (store_troop_faction, ":faction_no", ":troop"),
            (neg|troop_slot_eq, ":troop", slot_troop_original_faction, ":faction_no"),
            (call_script, "script_troop_set_title_according_to_faction", ":troop", ":faction_no"),
          (try_end),
        (try_end),
        
        # companions
        (try_begin),
          (troop_slot_eq, "trp_npc1", slot_troop_religion, 0),
          (try_for_range, ":cur_troop", companions_begin,companions_end),
            (try_begin),
              (this_or_next|eq, ":cur_troop", "trp_npc2"),
              (this_or_next|eq, ":cur_troop", "trp_npc7"),
              (this_or_next|eq, ":cur_troop", "trp_npc11"),
              (this_or_next|eq, ":cur_troop", "trp_npc12"),
              (eq, ":cur_troop", "trp_npc13"),
              (troop_set_slot, ":cur_troop", slot_troop_religion, 2), # pagan
            (else_try),
              (troop_set_slot, ":cur_troop", slot_troop_religion, 1), # christian
            (try_end),
          (try_end),
        (try_end),
        (try_begin),
          (troop_slot_eq, "trp_player", slot_troop_religion, 0),
          (try_begin),
            (eq, "$g_player_faith", 2),
            (troop_set_slot, "trp_player", slot_troop_religion, 2), # pagan
          (else_try),
            (troop_set_slot, "trp_player", slot_troop_religion, 1), # christian
          (try_end),
        (try_end),
        # end 1.03 religion slots reassignment
        #		(try_begin),
        #			(party_slot_eq, "p_town_4", slot_center_has_slavemarket, 0),
        #				(try_for_range, ":town", towns_begin, towns_end),
        #					(party_set_slot, ":town", slot_center_has_slavemarket, 0),
        #				(try_end),
        #			(party_set_slot,"p_town_4",slot_center_has_slavemarket, 1),
        #			(party_set_slot,"p_town_7",slot_center_has_slavemarket, 1),
        #		(try_end),
        #Ladies' rels with husbands
        #		(try_begin),
        #			(call_script, "script_troop_get_relation_with_troop", "trp_kingdom_7_lady_4", "trp_knight_7_3"),
        #			(eq, reg0, 0),
        #			(try_for_range, ":lady", kingdom_ladies_begin, kingdom_ladies_end),
        #				(troop_get_slot, ":spouse", ":lady", slot_troop_spouse),
        #				(ge, ":spouse", 1),
        #				(store_random_in_range, ":rel", 5, 45),
        #				(call_script, "script_troop_change_relation_with_troop", ":lady", ":spouse", ":rel"),
        #			(try_end),
        #		(try_end),
        # Fix Night bandits quest
        (try_begin),
          (check_quest_active, "qst_deal_with_night_bandits"),
          (neg|check_quest_succeeded, "qst_deal_with_night_bandits"),
          (quest_get_slot, ":target", "qst_deal_with_night_bandits", slot_quest_target_center),
          (neg|party_slot_ge, ":target", slot_center_has_bandits, 1),
          (store_random_in_range, ":random_no", 0, 3),
          (try_begin),
            (eq, ":random_no", 0),
            (assign, ":bandit_troop", "trp_bandit"),
          (else_try),
            (eq, ":random_no", 1),
            (assign, ":bandit_troop", "trp_mountain_bandit"),
          (else_try),
            (assign, ":bandit_troop", "trp_forest_bandit"),
          (try_end),
          (party_set_slot, ":target", slot_center_has_bandits, ":bandit_troop"),
        (try_end),
        
        (try_begin),
          (faction_slot_eq, "fac_adventurers", slot_faction_leader,0),
          (faction_set_slot, "fac_adventurers",  slot_faction_leader, -1),
          (faction_set_slot, "fac_adventurers", slot_faction_marshal, -1),
        (try_end),
        (try_begin),
          (faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_active),
          (troop_get_slot, ":spouse", "trp_player", slot_troop_spouse),
          (this_or_next|faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
          (faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, ":spouse"), #wife can change kingdom name
          
          (assign, "$players_kingdom_name_set", 1),
        (try_end),
        #fix adventurers parties
        (try_for_range, ":npc", companions_begin, companions_end),
          (troop_slot_eq, ":npc", slot_troop_occupation, slto_kingdom_hero),
          (try_begin),
            (troop_get_slot, ":faction", ":npc", slot_troop_original_faction),
            (store_faction_of_troop, ":cur_faction", ":npc"),
            (eq, ":faction", "fac_adventurers"),
            (is_between, ":cur_faction", kingdoms_begin, kingdoms_end),
            (troop_set_slot, ":npc", slot_troop_original_faction, ":cur_faction"),
          (try_end),
          (troop_get_slot, ":troop_party", ":npc", slot_troop_leaded_party),
          (gt, ":troop_party", 0),
          (party_is_active, ":troop_party"),
          (store_faction_of_troop, ":npc_faction", ":npc"),
          (store_faction_of_party, ":party_faction", ":troop_party"),
          (neq, ":npc_faction", ":party_faction"),
          (party_set_faction, ":party_faction", ":npc_faction"),
        (try_end),
        # Reset ai state for deserters
        (try_for_parties, ":party_no"),
          (try_begin),
            (store_faction_of_party, ":faction", ":party_no"),
            (eq, ":faction", "fac_deserters"),
            (party_get_slot, ":ai_state", ":party_no", slot_party_ai_state),
            (eq, ":ai_state", 0),
            (party_get_position, pos0,  ":party_no"),
            (party_set_ai_behavior, ":party_no", ai_bhvr_patrol_location),
            (party_set_slot, ":party_no", slot_party_ai_state, spai_patrolling_around_center),
            (party_set_ai_patrol_radius, ":party_no", 30),
            (party_set_ai_target_position, ":party_no", pos0),
          (else_try),
            (party_get_template_id, ":party_template", ":party_no"),
            (eq, ":party_template", "pt_sacerdotes_party"),
            (get_party_ai_behavior, ":ai_bhvr", ":party_no"),
            (eq, ":ai_bhvr", ai_bhvr_patrol_location),
            (store_random_in_range, ":mon", "p_monasterio1", "p_yourlair"),
            (party_set_slot, ":party_no", slot_party_ai_object, ":mon"),
            (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
            (party_set_ai_object, ":party_no", ":mon"),
            (party_set_flags, ":party_no", pf_default_behavior, 0),
          (try_end),
          
          # piggyback: fixing some slots of port_parties:
          (try_begin),
            (party_get_template_id, ":party_template_id", ":party_no"),
            (eq, ":party_template_id", "pt_port"),
            (party_set_slot, ":party_no", slot_party_on_water, 1),
            (neg|party_slot_eq, ":party_no", slot_village_state, 0), #for VC-2085
            (call_script, "script_village_set_state", ":party_no", 0),
          (end_try),
        (try_end),
        #fix player's kingdom setup
        (try_begin),
          (faction_get_slot, ":target_troop", "fac_player_supporters_faction", slot_faction_deserter_troop),
          (le, ":target_troop", 0),
          (try_begin),
            (this_or_next|eq,"$nacionalidad_type",cb7_norseman),
            (this_or_next|eq,"$nacionalidad_type",cb7_foreigner),
            (eq,"$nacionalidad_type",cb7_frisian),
            (faction_set_slot, "fac_player_faction", slot_faction_deserter_troop,"trp_norse_deserter"),
            (faction_set_slot, "fac_player_supporters_faction", slot_faction_deserter_troop,"trp_norse_deserter"),
            (faction_set_slot, "fac_player_supporters_faction", slot_faction_guard_troop, "trp_norse_level1_landed"),
            (faction_set_slot, "fac_player_supporters_faction", slot_faction_messenger_troop, "trp_norse_messenger"),
            (faction_set_slot, "fac_player_supporters_faction", slot_faction_prison_guard_troop, "trp_norse_prison_guard"),
            (faction_set_slot, "fac_player_supporters_faction", slot_faction_castle_guard_troop, "trp_norse_castle_guard"),
            (faction_set_slot, "fac_player_faction", slot_faction_guard_troop, "trp_norse_level1_landed"),
            (faction_set_slot, "fac_player_faction", slot_faction_messenger_troop, "trp_norse_messenger"),
            (faction_set_slot, "fac_player_faction", slot_faction_prison_guard_troop, "trp_norse_prison_guard"),
            (faction_set_slot, "fac_player_faction", slot_faction_castle_guard_troop, "trp_norse_castle_guard"),
          (else_try),
            (eq,"$nacionalidad_type",cb7_scotopict),
            (faction_set_slot, "fac_player_faction", slot_faction_deserter_troop,"trp_scotch_deserter"),
            (faction_set_slot, "fac_player_supporters_faction", slot_faction_deserter_troop,"trp_scotch_deserter"),
            (faction_set_slot, "fac_player_supporters_faction", slot_faction_guard_troop, "trp_scotch_level1_landed"),
            (faction_set_slot, "fac_player_supporters_faction", slot_faction_messenger_troop, "trp_scotch_messenger"),
            (faction_set_slot, "fac_player_supporters_faction", slot_faction_prison_guard_troop, "trp_scotch_prison_guard"),
            (faction_set_slot, "fac_player_supporters_faction", slot_faction_castle_guard_troop, "trp_scotch_castle_guard"),
            (faction_set_slot, "fac_player_faction", slot_faction_guard_troop, "trp_scotch_level1_landed"),
            (faction_set_slot, "fac_player_faction", slot_faction_messenger_troop, "trp_scotch_messenger"),
            (faction_set_slot, "fac_player_faction", slot_faction_prison_guard_troop, "trp_scotch_prison_guard"),
            (faction_set_slot, "fac_player_faction", slot_faction_castle_guard_troop, "trp_scotch_castle_guard"),
          (else_try),
            (eq,"$nacionalidad_type",cb7_briton),
            (faction_set_slot, "fac_player_faction", slot_faction_deserter_troop,"trp_briton_deserter"),
            (faction_set_slot, "fac_player_supporters_faction", slot_faction_deserter_troop,"trp_briton_deserter"),
            (faction_set_slot, "fac_player_supporters_faction", slot_faction_guard_troop, "trp_briton_level1_landed"),
            (faction_set_slot, "fac_player_supporters_faction",  slot_faction_messenger_troop, "trp_briton_messenger"),
            (faction_set_slot, "fac_player_supporters_faction",  slot_faction_prison_guard_troop, "trp_briton_prison_guard"),
            (faction_set_slot, "fac_player_supporters_faction",  slot_faction_castle_guard_troop, "trp_briton_castle_guard"),
            (faction_set_slot, "fac_player_faction", slot_faction_guard_troop, "trp_briton_level1_landed"),
            (faction_set_slot, "fac_player_faction",  slot_faction_messenger_troop, "trp_briton_messenger"),
            (faction_set_slot, "fac_player_faction",  slot_faction_prison_guard_troop, "trp_briton_prison_guard"),
            (faction_set_slot, "fac_player_faction",  slot_faction_castle_guard_troop, "trp_briton_castle_guard"),
          (else_try),
            (eq,"$nacionalidad_type",cb7_irish),
            (faction_set_slot, "fac_player_faction", slot_faction_deserter_troop,"trp_irish_deserter"),
            (faction_set_slot, "fac_player_supporters_faction", slot_faction_deserter_troop,"trp_irish_deserter"),
            (faction_set_slot, "fac_player_supporters_faction", slot_faction_guard_troop, "trp_irish_level1_landed"),
            (faction_set_slot, "fac_player_supporters_faction", slot_faction_messenger_troop, "trp_irish_messenger"),
            (faction_set_slot, "fac_player_supporters_faction", slot_faction_prison_guard_troop, "trp_irish_prison_guard"),
            (faction_set_slot, "fac_player_supporters_faction", slot_faction_castle_guard_troop, "trp_irish_castle_guard"),
            (faction_set_slot, "fac_player_faction", slot_faction_guard_troop, "trp_irish_level1_landed"),
            (faction_set_slot, "fac_player_faction", slot_faction_messenger_troop, "trp_irish_messenger"),
            (faction_set_slot, "fac_player_faction", slot_faction_prison_guard_troop, "trp_irish_prison_guard"),
            (faction_set_slot, "fac_player_faction", slot_faction_castle_guard_troop, "trp_irish_castle_guard"),
          (else_try),
            (eq,"$nacionalidad_type",cb7_anglesaxon),
            (faction_get_slot, ":cult", "fac_player_supporters_faction",  slot_faction_culture),
            (try_begin),
              (eq, ":cult", "fac_culture_saxon"),
              (faction_set_slot, "fac_player_faction", slot_faction_deserter_troop, "trp_saxon_deserter"),
              (faction_set_slot, "fac_player_supporters_faction", slot_faction_deserter_troop, "trp_saxon_deserter"),
              (faction_set_slot, "fac_player_supporters_faction", slot_faction_guard_troop, "trp_saxon_level1_landed"),
              (faction_set_slot, "fac_player_supporters_faction", slot_faction_messenger_troop, "trp_saxon_messenger"),
              (faction_set_slot, "fac_player_supporters_faction", slot_faction_prison_guard_troop, "trp_saxon_prison_guard"),
              (faction_set_slot, "fac_player_supporters_faction", slot_faction_castle_guard_troop, "trp_saxon_castle_guard"),
              (faction_set_slot, "fac_player_faction", slot_faction_guard_troop, "trp_saxon_level1_landed"),
              (faction_set_slot, "fac_player_faction", slot_faction_messenger_troop, "trp_saxon_messenger"),
              (faction_set_slot, "fac_player_faction", slot_faction_prison_guard_troop, "trp_saxon_prison_guard"),
              (faction_set_slot, "fac_player_faction", slot_faction_castle_guard_troop, "trp_saxon_castle_guard"),
            (else_try),
              (faction_set_slot, "fac_player_faction", slot_faction_deserter_troop, "trp_angle_deserter"),
              (faction_set_slot, "fac_player_supporters_faction", slot_faction_deserter_troop, "trp_angle_deserter"),
              (faction_set_slot, "fac_player_supporters_faction", slot_faction_guard_troop, "trp_angle_level1_landed"),
              (faction_set_slot, "fac_player_supporters_faction", slot_faction_messenger_troop, "trp_angle_messenger"),
              (faction_set_slot, "fac_player_supporters_faction", slot_faction_prison_guard_troop, "trp_angle_prison_guard"),
              (faction_set_slot, "fac_player_supporters_faction", slot_faction_castle_guard_troop, "trp_angle_castle_guard"),
              (faction_set_slot, "fac_player_faction", slot_faction_guard_troop, "trp_angle_level1_landed"),
              (faction_set_slot, "fac_player_faction", slot_faction_messenger_troop, "trp_angle_messenger"),
              (faction_set_slot, "fac_player_faction", slot_faction_prison_guard_troop, "trp_angle_prison_guard"),
              (faction_set_slot, "fac_player_faction", slot_faction_castle_guard_troop, "trp_angle_castle_guard"),
            (try_end),
          (try_end),
        (try_end),
        #end fix player setup
        (try_begin),
          (check_quest_active, "qst_blank_quest_10"),
          (quest_get_slot, ":target_troop", "qst_blank_quest_10", slot_quest_target_troop),
          (le, ":target_troop", 0),
          (quest_get_slot, ":center", "qst_blank_quest_10", slot_quest_target_center),
          (store_faction_of_party, ":faction", ":center"),
          (faction_get_slot, ":target_troop", ":faction", slot_faction_deserter_troop),
          (quest_set_slot, "qst_blank_quest_10", slot_quest_target_troop, ":target_troop"),
        (try_end),
        #Reeves
        (try_begin),
          (party_get_slot, ":seneschal", "p_town_4", slot_town_seneschal),
          (eq, ":seneschal", 0),
          (try_for_range, ":castle_no", castles_begin, castles_end),
            (store_sub, ":offset", ":castle_no", castles_begin),
            (store_add, ":senechal_troop_no", "trp_castle_1_seneschal", ":offset"),
            (party_set_slot,":castle_no", slot_town_seneschal, ":senechal_troop_no"),
            (str_store_troop_face_keys, s1, "trp_town_1_weaponsmith"),
            (str_store_troop_face_keys, s2, "trp_village_145_elder"),
            (str_store_troop_face_keys, s3, "trp_town_1_merchant"),
            (store_random_in_range, ":rand", 0,3),
            (try_begin),
              (eq, ":rand", 0),
              (troop_set_face_keys, ":senechal_troop_no",s1),
            (else_try),
              (eq, ":rand", 1),
              (troop_set_face_keys, ":senechal_troop_no",s2),
            (else_try),
              (troop_set_face_keys, ":senechal_troop_no",s3),
            (try_end),
          (try_end),
        (try_end),
        # Farmsteads
        # (try_begin),
        # (party_slot_eq, "p_farmsteadsp1", slot_center_head_cattle, 0),
        # (try_for_range, ":farm", "p_farmsteadsp1", "p_hadrian_wall1"),
        # (store_random_in_range, ":rand", 120,250),
        # (party_set_slot,":farm", slot_center_head_cattle, ":rand"),
        # (party_set_slot, ":farm", slot_center_player_cattle, 0),
        # (try_end),
        # (try_end),
        #End farmsteads
        # 1.087 beta fix for royal campaign
        (try_for_range, ":troop_id", kingdom_ladies_begin, kingdom_ladies_end),
          (store_troop_faction, ":faction", ":troop_id"),
          (troop_get_slot, ":spouse", ":troop_id", slot_troop_spouse),
          (troop_get_slot, ":guardian", ":troop_id", slot_troop_guardian),
          (try_begin),
            (gt, ":spouse", 0),
            (store_troop_faction, ":sfaction", ":spouse"),
            (neq, ":faction", ":sfaction"),
            (troop_set_faction, ":troop_id", ":sfaction"),
          (else_try),
            (eq, ":spouse", -1),
            (gt, ":guardian", 0),
            (store_troop_faction, ":gfaction", ":guardian"),
            (neq, ":faction", ":gfaction"),
            (troop_set_faction, ":troop_id", ":gfaction"),
          (try_end),
        (try_end),
        (try_begin),
          (eq, "$campaign_type", camp_kingc),
          (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
          (try_for_range, ":stack_no", 0, ":num_stacks"),
            (party_stack_get_troop_id, ":stack_troop", "p_main_party", ":stack_no"),
            (neq, ":stack_troop", "trp_player"),
            (is_between, ":stack_troop", companions_begin, companions_end),
            (troop_slot_eq, ":stack_troop", slot_troop_occupation, slto_inactive),
            (troop_set_slot, ":stack_troop", slot_troop_occupation, slto_player_companion),
            (troop_set_slot, ":stack_troop", slot_troop_cur_center, -1),
            (troop_set_auto_equip, ":stack_troop", 0),
            (troop_set_note_available, ":stack_troop", 1),
          (try_end),
        (try_end),
        (try_begin),
          (eq, "$campaign_type", camp_kingc),
          (try_for_range, ":npc", companions_begin, companions_end),
            (troop_get_slot, ":mission", ":npc", slot_troop_current_mission),
            (this_or_next|eq,"$g_player_minister", ":npc"),
            (gt, ":mission", 0),
            (troop_slot_eq, ":npc", slot_troop_occupation, slto_inactive),
            (troop_set_slot, ":npc", slot_troop_occupation, slto_player_companion),
            (troop_set_auto_equip, ":npc", 0),
            (troop_set_note_available, ":npc", 1),
          (try_end),
        (try_end),
        #end royal camp fix
        (try_for_range, ":npc", companions_begin, companions_end),
          (main_party_has_troop, ":npc"),
          (troop_slot_eq, ":npc", slot_troop_occupation,  slto_kingdom_hero),
          (troop_set_slot, ":npc", slot_troop_occupation, slto_player_companion),
          (troop_set_auto_equip, ":npc", 0),
          (troop_set_note_available, ":npc", 1),
        (try_end),
        #reset troop wealths V104
        (troop_get_slot, ":wealth_adjust", "trp_kingdom_1_lord", slot_troop_wealth),
        (troop_get_slot, reg0, "trp_kingdom_2_lord", slot_troop_wealth),
        (val_add, ":wealth_adjust", reg0),
        (try_begin),
          (gt, ":wealth_adjust", 200000),
          (val_div, ":wealth_adjust", 22000),  #average game start * 2
          (try_for_range, ":troop", active_npcs_begin, active_npcs_end),
            (troop_get_slot, reg0, ":troop", slot_troop_wealth),
            (val_div, reg0, ":wealth_adjust"),
            (troop_set_slot, ":troop", slot_troop_wealth, reg0),
          (try_end),
        (try_end),
        
        # CODE FOR UPDATING OLD SAVEGAMES TO THE CONTENTUPDATE (VC-2279):
        (try_begin),
          (neq, "$game_started_with_content_update", 1),
          (neq, "$game_updated_to_content_update", 1),
          (call_script, "script_update_savegame_to_content_update"),
        (end_try),
    ]),
    
    # Create Deserters when there are more prisoners than troops @Mike
    (36,
      [
        (try_for_parties, ":party_no"),
          (party_get_template_id, ":party_template", ":party_no"),
          (this_or_next|party_slot_eq, ":party_no", slot_party_type, spt_kingdom_hero_party),
          (this_or_next|is_between, ":party_template", "pt_looters", "pt_kidnapped_girl"),
          (this_or_next|is_between, ":party_template", "pt_sea_raiders_ships", "pt_chimney_smoke"),
          (eq,":party_template", "pt_village_farmers"),
          (store_party_size_wo_prisoners, ":party_count", ":party_no"),
          (party_get_num_prisoners , ":prisoners_count", ":party_no"),
          (gt, ":prisoners_count", 0),
          (store_sub, ":prisoners_excess", ":prisoners_count", ":party_count"),
          (try_begin),
            (is_between, ":party_template", "pt_sea_raiders_ships", "pt_chimney_smoke"),
            (assign, ":check", 20),
          (else_try),
            (assign, ":check", 4),
          (try_end),
          (gt, ":prisoners_excess", ":check"),
          (try_begin),
            (gt, ":prisoners_count", 400),
            (val_div, ":prisoners_count", 2),
          (try_end),
          (try_begin),
            (party_clear, "p_temp_party"),
            (party_clear, "p_temp_party_2"),
            (party_get_num_prisoner_stacks, ":prisoner_stacks", ":party_no"),
            (try_for_range_backwards, ":prisoner_stack_no", 0, ":prisoner_stacks"),
              (party_prisoner_stack_get_troop_id, ":prisoner_troop_no", ":party_no", ":prisoner_stack_no"),
              (neg|troop_is_hero, ":prisoner_troop_no"),
              (party_prisoner_stack_get_size, ":prisoner_stack_size", ":party_no", ":prisoner_stack_no"),
              (store_party_size_wo_prisoners, ":new_party_count", "p_temp_party"),
              #(assign, reg44, ":new_party_count"),
              (try_begin),
                (le, ":new_party_count",":prisoners_count"),
                (party_add_members, "p_temp_party", ":prisoner_troop_no", ":prisoner_stack_size"),
                (party_remove_prisoners, ":party_no", ":prisoner_troop_no", ":prisoner_stack_size"),
              (else_try),
                #(display_message, "@{reg44} is too high"),
                (party_add_members, "p_temp_party_2", ":prisoner_troop_no", ":prisoner_stack_size"),
                (party_remove_prisoners, ":party_no", ":prisoner_troop_no", ":prisoner_stack_size"),
              (try_end),
            (try_end),
            (set_spawn_radius, 4),
            (try_begin),
              (neg|is_between, ":party_template", "pt_sea_raiders_ships", "pt_chimney_smoke"),
              (spawn_around_party,":party_no","pt_deserters"),
            (else_try),
              (is_between, ":party_template", "pt_sea_raiders_ships", "pt_chimney_smoke"),
              (store_random_in_range, ":spawn", "p_battle_stones", "p_bjorn_camp"),
              (spawn_around_party,":spawn","pt_deserters"),
            (try_end),
            (assign, ":new_party", reg(0)),
            (call_script, "script_party_add_party", ":new_party", "p_temp_party"),
            (party_set_faction, ":new_party", "fac_deserters"),
            (party_get_position, pos0,  ":new_party"),
            (party_set_ai_behavior, ":new_party", ai_bhvr_patrol_location),
            (party_set_ai_patrol_radius, ":new_party", 40),
            (party_set_ai_target_position, ":new_party", pos0),
            (store_party_size_wo_prisoners, ":party_count1", ":new_party"),
            (try_begin),
              (gt, ":party_count1", 25),
              (party_add_leader, ":new_party", "trp_looter_leader2", 1),
            (try_end),
            (try_begin),
              (store_party_size_wo_prisoners, ":new_party_count", "p_temp_party_2"),
              #(assign, reg44, ":new_party_count"),
              #(display_message, "@{reg44} is in temp2"),
              (gt,  ":new_party_count", 0),
              (set_spawn_radius, 4),
              (try_begin),
                (neg|is_between, ":party_template", "pt_sea_raiders_ships", "pt_chimney_smoke"),
                (spawn_around_party,":party_no","pt_deserters"),
              (else_try),
                (is_between, ":party_template", "pt_sea_raiders_ships", "pt_chimney_smoke"),
                (store_random_in_range, ":spawn", "p_battle_stones", "p_bjorn_camp"),
                (spawn_around_party,":spawn","pt_deserters"),
              (try_end),
              (assign, ":new_party", reg(0)),
              (call_script, "script_party_add_party", ":new_party", "p_temp_party_2"),
              (party_set_faction, ":new_party", "fac_deserters"),
              (party_get_position, pos0,  ":new_party"),
              (party_set_ai_behavior, ":new_party", ai_bhvr_patrol_location),
              (party_set_ai_patrol_radius, ":new_party", 40),
              (party_set_ai_target_position, ":new_party", pos0),
              (store_party_size_wo_prisoners, ":party_count1", ":new_party"),
              (try_begin),
                (gt, ":party_count1", 25),
                (party_add_leader, ":new_party", "trp_looter_leader2", 1),
              (try_end),
            (try_end),
          (try_end),
          (try_begin),
            (eq, "$cheat_mode", 1),
            (is_between, ":party_template", "pt_sea_raiders_ships", "pt_chimney_smoke"),
            (str_store_party_name, s33, ":spawn"),
            (display_message,"@Prisoners revolted! near {s33}"),
          (try_end),
        (try_end),
    ]),
    
    # JuJu70
    #Upgrade adventurers with items
    (24,
      [(try_for_range, ":troop_no", companions_begin, companions_end),
          (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
          (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
          (troop_get_slot, ":hero_party",":troop_no", slot_troop_leaded_party),
          (party_is_active, ":hero_party"),
          (gt, ":hero_party", 0),
          (store_faction_of_party, ":hero_faction", ":hero_party"),
          (eq, ":hero_faction", "fac_adventurers"),
          (troop_set_auto_equip, ":troop_no", 1),
          (party_get_attached_to, ":cur_attached_party", ":hero_party"),
          (neg|is_between, ":cur_attached_party", walled_centers_begin, walled_centers_end),
          (try_begin),
            (troop_get_inventory_slot,":cur_item1",":troop_no",ek_body),
            (le, ":cur_item1", 0),
            (store_random_in_range, ":new_item", "itm_hoodtunic_01", "itm_hoodtunic_08"),
            (troop_add_item, ":troop_no", ":new_item"),
          (try_end),
          (try_begin),
            (troop_get_inventory_slot,":cur_item1",":troop_no",ek_foot),
            (le, ":cur_item1", 0),
            (store_random_in_range, ":new_item", "itm_carbatinae_1", "itm_carbatinae_vc1s"),
            (troop_add_item, ":troop_no", ":new_item"),
          (try_end),
          (try_begin),
            (assign, ":weapon", 0),
            (try_for_range, ":item_slot", ek_item_0, ek_head),
              (troop_get_inventory_slot,":cur_item",":troop_no",":item_slot"),
              (gt, ":cur_item", 0),
              (item_get_type, ":item_type", ":cur_item"),
              (this_or_next|eq, ":item_type", itp_type_one_handed_wpn),
              (this_or_next|eq, ":item_type", itp_type_two_handed_wpn),
              (eq, ":item_type",itp_type_polearm),
              (val_add, ":weapon", 1),
            (try_end),
            (eq, ":weapon", 0),
            (store_random_in_range, ":new_item1", "itm_knife", "itm_longseax1"),
            (troop_add_item, ":troop_no", ":new_item1"),
          (try_end),
          (try_begin),
            (troop_slot_ge, ":troop_no", slot_troop_renown, 175),
            (troop_get_inventory_slot,":cur_item1",":troop_no",ek_body),
            (try_begin),
              (gt, ":cur_item1", 0),
              (item_get_body_armor, ":armor", ":cur_item1"),
              (le, ":armor", 20),
              (store_random_in_range, ":new_item", "itm_gambeson1", "itm_gambeson1gael"),
              (troop_remove_item,":troop_no", ":cur_item1"),
              (troop_add_item, ":troop_no", ":new_item"),
            (else_try),
              (le, ":cur_item1", 0),
              (store_random_in_range, ":new_item", "itm_gambeson1", "itm_gambeson1gael"),
              (troop_add_item, ":troop_no", ":new_item"),
            (try_end),
          (try_end),
          (try_begin),
            (troop_slot_ge, ":troop_no", slot_troop_renown, 175),
            (troop_get_inventory_slot,":cur_itemf",":troop_no",ek_foot),
            (try_begin),
              (gt, ":cur_itemf", 0),
              (item_get_leg_armor, ":armor", ":cur_itemf"),
              (le, ":armor", 20),
              (assign, ":shoe", 0),
              (store_random_in_range, ":rand", 0, 6),
              (try_begin),
                (eq, ":rand", 0),
                (assign, ":shoe", "itm_carbatinae_4v"),
              (else_try),
                (eq, ":rand", 1),
                (assign, ":shoe", "itm_carbatinae_vc2v"),
              (else_try),
                (eq, ":rand", 2),
                (assign, ":shoe", "itm_carbatinae_11qs"),
              (else_try),
                (eq, ":rand", 3),
                (assign, ":shoe", "itm_carbatinae_12qs"),
              (else_try),
                (assign, ":shoe", "itm_carbatinae_14qv"),
              (try_end),
              (gt, ":shoe", 0),
              (troop_remove_item,":troop_no", ":cur_itemf"),
              (troop_add_item, ":troop_no", ":shoe"),
            (else_try),
              (le, ":cur_itemf", 0),
              (assign, ":shoe", 0),
              (store_random_in_range, ":rand", 0, 6),
              (try_begin),
                (eq, ":rand", 0),
                (assign, ":shoe", "itm_carbatinae_4v"),
              (else_try),
                (eq, ":rand", 1),
                (assign, ":shoe", "itm_carbatinae_vc2v"),
              (else_try),
                (eq, ":rand", 2),
                (assign, ":shoe", "itm_carbatinae_11qs"),
              (else_try),
                (eq, ":rand", 3),
                (assign, ":shoe", "itm_carbatinae_12qs"),
              (else_try),
                (assign, ":shoe", "itm_carbatinae_14qv"),
              (try_end),
              (gt, ":shoe", 0),
              (troop_add_item, ":troop_no", ":shoe"),
            (try_end),
          (try_end),
          (try_begin),
            (troop_get_slot, ":renown", ":troop_no", slot_troop_renown),
            (is_between, ":renown", 200, 400),
            (assign, ":equip", 0),
            (try_for_range, ":item_slot", ek_item_0, ek_head),
              (troop_get_inventory_slot,":cur_items",":troop_no",":item_slot"),
              (gt, ":cur_items", 0),
              (item_get_type, ":item_type", ":cur_items"),
              (eq, ":item_type", itp_type_shield),
              (assign, ":equip", 1),
            (try_end),
            (eq, ":equip", 0),
            (store_random_in_range, ":new_items", "itm_shield_1", "itm_shield_7"),
            #			(try_begin),
            #				(gt, ":cur_items", 0),
            #				(troop_remove_item,":troop_no", ":cur_items"),
            #			(try_end),
            (troop_add_item, ":troop_no", ":new_items"),
          (try_end),
          (try_begin),
            (troop_slot_ge, ":troop_no", slot_troop_renown, 125),
            (troop_get_inventory_slot,":cur_itemh",":troop_no",ek_head),
            (assign, ":helmet", 0),
            (try_begin),
              (gt, ":cur_itemh", 0),
              (item_get_head_armor, ":armor", ":cur_itemh"),
              (le, ":armor", 15),
              (store_random_in_range, ":helmet", "itm_briton_helm3", "itm_briton_helm9"),
            (else_try),
              (le, ":cur_itemh", -1),
              (store_random_in_range, ":helmet", "itm_briton_helm3", "itm_briton_helm9"),
            (else_try),
            (try_end),
            (gt, ":helmet", 0),
            (try_begin),
              (gt, ":cur_itemh", 0),
              (troop_remove_item,":troop_no", ":cur_itemh"),
            (try_end),
            (troop_add_item, ":troop_no", ":helmet"),
          (try_end),
          (try_begin),
            (troop_slot_ge, ":troop_no", slot_troop_renown, 170),
            (assign, ":new_item1", 0),
            (try_for_range, ":item_slot", ek_item_0, ek_head),
              (troop_get_inventory_slot,":cur_item3",":troop_no",":item_slot"),
              (gt, ":cur_item3", 0),
              (item_get_type, ":item_type", ":cur_item3"),
              (eq, ":item_type", itp_type_one_handed_wpn),
              (item_get_swing_damage, ":swing", ":cur_item3"),
              (try_begin),
                (lt, ":swing", 20),
                (store_random_in_range, ":new_item1", "itm_hatchet", "itm_axe_3"),
              (try_end),
              (gt, ":new_item1", 0),
              (troop_remove_item,":troop_no", ":cur_item3"),
              (troop_add_item, ":troop_no", ":new_item1"),
            (try_end),
          (try_end),
          (try_begin),
            (troop_slot_ge, ":troop_no", slot_troop_renown, 200),
            (troop_get_inventory_slot,":cur_item2",":troop_no",ek_horse),
            (le, ":cur_item2", 0),
            (store_skill_level, ":riding", "skl_riding", ":troop_no"),
            (try_begin),
              (eq, ":riding", 0),
              (troop_raise_skill, ":troop_no", "skl_riding", 3),
            (else_try),
              (eq, ":riding", 1),
              (troop_raise_skill, ":troop_no", "skl_riding", 2),
            (try_end),
            (store_random_in_range, ":new_horse", "itm_common_pony", "itm_wild_horse"),
            (troop_add_item, ":troop_no", ":new_horse"),
          (try_end),
        (try_end),
    ]),
    (33,
      [	(try_for_range,":troop_no",active_npcs_begin, active_npcs_end),
          (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
          (troop_get_slot,":val",":troop_no",slot_troop_days_on_mission),
          (gt,":val",0),#0 = can ask to sing about player
          (val_sub,":val",1),
          (val_max,":val",0),#to clear negative values (errors)
          (troop_set_slot,":troop_no",slot_troop_days_on_mission,":val"),
          (try_begin),
            (eq, ":val", 0),
            (try_begin),
              (troop_slot_eq, ":troop_no", slot_troop_current_mission, npc_mission_improve_relations),
              (troop_get_slot, ":mission_object", ":troop_no", slot_troop_mission_object),
              #				(try_begin),
              #					(ge, ":mission_object", 0),
              #					(str_store_party_name, s33, ":mission_object"),
              #					(display_message, "@{s33} is object"),
              #				(try_end),
              (try_begin),
                (eq, ":mission_object", "p_main_party"),
                (troop_get_slot, ":target", ":troop_no", slot_troop_mission_target),
                (call_script, "script_troop_get_player_relation", ":troop_no"),
                (assign, ":rels", reg0),
                (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
                (troop_get_slot, ":troop_renown", ":troop_no", slot_troop_renown),
                (store_skill_level, ":persuasion", "skl_persuasion", "trp_player"),
                (val_mul, ":player_renown", 10),
                (val_div, ":player_renown",":troop_renown"),
                (val_sub, ":persuasion",6),
                (val_mul, ":persuasion", 10),
                (store_add, ":mod", ":player_renown", ":rels"),
                (val_add, ":mod", ":persuasion"),
                (val_div, ":mod", 5),
                (try_begin),
                  (this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_custodian),
                  (this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_benefactor),
                  (this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_upstanding),
                  (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_goodnatured),
                  (val_add, ":mod", 7),
                (else_try),
                  (this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_martial),
                  (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_selfrighteous),
                  (val_add, ":mod", 5),
                (else_try),
                  (this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_cunning),
                  (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_roguish),
                  (val_add, ":mod", 2),
                (else_try),
                  ##							(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_quarrelsome),
                  ##							(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_debauched),
                  (val_add, ":mod", -2),
                (try_end),
                (val_add, ":mod", 10),
                #						(assign, reg44, ":mod"),
                #						(display_message, "@mod is {reg44}"),
                (store_random_in_range, ":rand", 0, 50),
                #						(assign, reg45, ":rand"),
                #						(display_message, "@random is {reg45}"),
                (lt, ":rand", ":mod"),
                (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
                (party_get_attached_to, ":attached_to_party", ":party_no"),
                (try_begin),
                  (is_between, ":attached_to_party", centers_begin, centers_end),
                  (party_detach, ":party_no"),
                (try_end),
                (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
                (party_set_ai_object, ":party_no", ":target"),
                (party_set_slot, ":party_no", slot_party_ai_object, ":target"),
                (party_set_slot, ":party_no", slot_party_ai_state, spai_retreating_to_center),
                #						(party_set_flags, ":party_no", pf_default_behavior, 0),
                #						(call_script, "script_party_set_ai_state", ":party_no", spai_patrolling_around_center, ":target"),
              (else_try),
                (is_between, ":mission_object", walled_centers_begin, walled_centers_end),
                (call_script, "script_troop_get_player_relation", ":troop_no"),
                (assign, ":rels", reg0),
                (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
                (troop_get_slot, ":troop_renown", ":troop_no", slot_troop_renown),
                (store_skill_level, ":persuasion", "skl_persuasion", "trp_player"),
                (val_mul, ":player_renown", 10),
                (val_div, ":player_renown",":troop_renown"),
                (val_sub, ":persuasion",6),
                (val_mul, ":persuasion", 10),
                (val_sub, ":rels", 10),
                (store_add, ":mod", ":player_renown", ":rels"),
                (val_add, ":mod", ":persuasion"),
                (val_div, ":mod", 8),
                (try_begin),
                  (this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_custodian),
                  (this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_benefactor),
                  (this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_upstanding),
                  (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_goodnatured),
                  (val_add, ":mod", 7),
                (else_try),
                  (this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_martial),
                  (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_selfrighteous),
                  (val_add, ":mod", 5),
                (else_try),
                  (this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_cunning),
                  (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_roguish),
                  (val_add, ":mod", 2),
                (else_try),
                  ##							(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_quarrelsome),
                  ##							(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_debauched),
                  (val_add, ":mod", -2),
                (try_end),
                (store_random_in_range, ":rand", 0, 50),
                (val_add, ":mod", 10),
                #						(assign, reg44, ":mod"),
                #						(display_message, "@mod is {reg44}"),
                #						(assign, reg45, ":rand"),
                #						(display_message, "@random is {reg45}"),
                (lt, ":rand", ":mod"),
                (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
                (party_get_attached_to, ":attached_to_party", ":party_no"),
                (try_begin),
                  (is_between, ":attached_to_party", centers_begin, centers_end),
                  (party_detach, ":party_no"),
                (try_end),
                (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
                (party_set_ai_object, ":party_no", ":mission_object"),
                (party_set_slot, ":party_no", slot_party_ai_object, ":mission_object"),
                (party_set_slot, ":party_no", slot_party_ai_state, spai_retreating_to_center),
              (else_try),
                (troop_get_slot, ":mission_amount", ":troop_no", slot_troop_mission_amount),
                (gt, ":mission_amount", 0),
                (store_skill_level, ":persuasion", "skl_persuasion", "trp_player"),
                (store_attribute_level, ":charisma", "trp_player", ca_charisma),
                (call_script, "script_troop_get_player_relation", ":troop_no"),
                (assign, ":rels", reg0),
                (try_begin),
                  (eq, ":rels", 0),
                (else_try),
                  (is_between, ":rels", -9, 0),
                  (assign, ":rels", -1),
                (else_try),
                  (is_between, ":rels", 1, 10),
                  (assign, ":rels", 1),
                (else_try),
                  (val_div, ":rels", 10),
                (try_end),
                (val_div, ":charisma", 3),
                (val_div, ":persuasion", 2),
                (store_add, ":mod", ":persuasion", ":charisma"),
                (val_add, ":mod", ":rels"),
                (val_sub, ":mod", 2),
                (store_div, ":mon", ":mission_amount", 1000),
                (val_add, ":mod", ":mon"),
                (try_begin),
                  (this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_custodian),
                  (this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_benefactor),
                  (this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_upstanding),
                  (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_goodnatured),
                  (val_add, ":mod", 1),
                (else_try),
                  (this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_martial),
                  (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_selfrighteous),
                  (val_sub, ":mod", 1),
                (else_try),
                  ##  							(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_cunning),
                  ##							(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_roguish),
                  (val_sub, ":mod", 2),
                (try_end),
                (try_begin),
                  (le,":mod", 0),
                  (assign, ":mod", 0),
                (else_try),
                  (store_random_in_range, ":rand", 0, 50),
                  (try_begin),
                    (lt, ":rand", ":mod"),
                    (assign, ":mod", 5),
                  (else_try),
                    (le, ":rels", 0),
                    (store_add, ":monrels", ":mon", ":rels"),
                    (val_sub, ":monrels", 1),
                    (val_max, ":monrels", 0),
                    (assign, ":mod", ":monrels"),
                  (else_try),
                    (assign, ":mod", ":mon"),
                    (val_min, ":mod", 2),
                  (try_end),
                (try_end),
                (try_begin),
                  (gt, ":mod", 0),
                  (str_store_troop_name, s13, ":troop_no"),
                  (call_script, "script_change_player_relation_with_troop", ":troop_no", ":mod"),
                  (tutorial_box, "@Your gift sent to {s13} appeared to improve your relations with him.", "@Gift Sent to Lord"),
                  (troop_get_slot, ":wealth", ":troop_no", slot_troop_wealth),
                  (val_add, ":wealth", ":mission_amount"),
                  (troop_set_slot, ":troop_no", slot_troop_wealth, ":wealth"),
                  (troop_set_slot,":troop_no",slot_troop_current_mission, 0),
                (try_end),
              (try_end),
            (try_end),
            (troop_set_slot, ":troop_no", slot_troop_message_sent, 0),
          (try_end),
        (try_end),
    ]),
    
    #party cleanup
    (20, [
        (store_and, ":homes_fixed", "$first_time", first_time_fix_home_center),
        
        (try_for_parties, ":party_no"),
          (gt, ":party_no", "p_spawn_points_end"),
          #Splitting big deserters parties
          (store_party_size_wo_prisoners, ":party_count", ":party_no"),
          (store_faction_of_party, ":faction", ":party_no"),
          (try_begin),
            (eq, ":faction", "fac_deserters"),
            (try_begin),
              (gt, ":party_count", 1000),
              (neg|quest_slot_eq, "qst_blank_quest_4", slot_quest_target_party, ":party_no"),
              (neg|quest_slot_eq, "qst_track_down_bandits", slot_quest_target_party, ":party_no"),
              (remove_party, ":party_no"),
            (try_end),
            (gt, ":party_no", 0),
            
            (assign, ":check", 0),
            (assign, ":stack_limit", 50),
            (try_begin),
              (gt, ":party_count", 300),
              (assign, ":check", 100),
              (assign, ":stack_limit", 100),
            (else_try),
              (gt, ":party_count", 220),
              (assign, ":check",60),
              (assign, ":stack_limit", 75),
            (else_try),
              (gt, ":party_count", 190),
              (assign, ":check", 15),
              (assign, ":stack_limit", 60),
            (try_end),
            (store_random_in_range, ":random", 0, 100),
            (lt, ":random", ":check"),
            
            (try_begin),
              (party_clear, "p_temp_party"),
              (party_clear, "p_temp_party_2"),
              (party_get_num_companion_stacks, ":num_stacks", ":party_no"),
              (try_for_range_backwards, ":cur_stack", 0, ":num_stacks"),
                (party_stack_get_troop_id, ":cur_troop_id", ":party_no", ":cur_stack"),
                (neg|troop_is_hero, ":cur_troop_id"),
                (party_stack_get_size, ":cur_size", ":party_no", ":cur_stack"),
                #(assign, reg44, ":cur_size"),
                (try_begin),
                  (gt, ":cur_size", ":stack_limit"),
                  (assign, ":cur_size", ":stack_limit"),
                (try_end),
                #	(assign, reg45, ":cur_size"),
                #	(str_store_troop_name, s33, ":cur_troop_id"),
                #	(display_log_message, "@orig size is {reg44}, adjusted {reg45} of {s33}"),
                (store_party_size_wo_prisoners, ":new_party_count", "p_temp_party"),
                (store_party_size_wo_prisoners, ":new_party_count2", "p_temp_party_2"),
                (try_begin),
                  (le, ":new_party_count",200),
                  (party_add_members, "p_temp_party", ":cur_troop_id", ":cur_size"),
                  (party_remove_members, ":party_no", ":cur_troop_id", ":cur_size"),
                (else_try),
                  (le, ":new_party_count2",200),
                  (party_add_members, "p_temp_party_2", ":cur_troop_id", ":cur_size"),
                  (party_remove_members, ":party_no", ":cur_troop_id", ":cur_size"),
                (end_try),
              (try_end),
              (try_begin),
                (party_get_num_prisoners , ":prisoners_count", ":party_no"),
                (gt, ":prisoners_count", 0),
                (store_div, ":prisoner_move", ":prisoners_count", 3),
                (party_get_num_prisoner_stacks, ":prisoner_stacks", ":party_no"),
                (try_for_range_backwards, ":prisoner_stack_no", 0, ":prisoner_stacks"),
                  (party_prisoner_stack_get_troop_id, ":prisoner_troop_no", ":party_no", ":prisoner_stack_no"),
                  (neg|troop_is_hero, ":prisoner_troop_no"),
                  (party_prisoner_stack_get_size, ":prisoner_stack_size", ":party_no", ":prisoner_stack_no"),
                  (try_begin),
                    (gt, ":prisoner_stack_size", ":prisoner_move"),
                    (assign, ":prisoner_stack_size", ":prisoner_move"),
                  (try_end),
                  (party_get_num_prisoners, ":prisoner_count1", "p_temp_party"),
                  (party_get_num_prisoners, ":prisoner_count2", "p_temp_party_2"),
                  #(assign, reg44, ":new_party_count"),
                  (try_begin),
                    (le, ":prisoner_count1",":prisoner_move"),
                    (party_add_prisoners, "p_temp_party", ":prisoner_troop_no", ":prisoner_stack_size"),
                    (party_remove_prisoners, ":party_no", ":prisoner_troop_no", ":prisoner_stack_size"),
                  (else_try),
                    (le, ":prisoner_count2",":prisoner_move"),
                    #(display_message, "@{reg44} is too high"),
                    (party_add_prisoners, "p_temp_party_2", ":prisoner_troop_no", ":prisoner_stack_size"),
                    (party_remove_prisoners, ":party_no", ":prisoner_troop_no", ":prisoner_stack_size"),
                  (try_end),
                (try_end),
              (try_end),
              (store_party_size_wo_prisoners, ":party_count1", "p_temp_party"),
              (store_random_in_range, ":spawn", "p_monasterio1", "p_yourlair"),
              #			(str_store_party_name, s33, ":spawn"),
              (set_spawn_radius, 4),
              (spawn_around_party,":spawn","pt_deserters"),
              (assign, ":new_party", reg(0)),
              (call_script, "script_party_add_party", ":new_party", "p_temp_party"),
              (party_set_faction, ":new_party", "fac_deserters"),
              (party_get_position, pos0,  ":new_party"),
              (party_set_ai_behavior, ":new_party", ai_bhvr_patrol_location),
              (party_set_ai_patrol_radius, ":new_party", 40),
              (party_set_ai_target_position, ":new_party", pos0),
              (store_party_size_wo_prisoners, ":party_count1", ":new_party"),
              (try_begin),
                (gt, ":party_count1", 25),
                (party_add_leader, ":new_party", "trp_looter_leader2", 1),
              (try_end),
              #			(display_log_message,"@party broke apart near {s33}"),
              (try_begin),
                (store_party_size_wo_prisoners, ":new_party_count", "p_temp_party_2"),
                #				(assign, reg44, ":new_party_count"),
                #				(display_log_message, "@{reg44} is in temp2"),
                (gt,  ":new_party_count", 0),
                (store_random_in_range, ":spawn", "p_battle_stones", "p_bjorn_camp"),
                #				(str_store_party_name, s33, ":spawn"),
                (set_spawn_radius, 4),
                (spawn_around_party,":spawn","pt_deserters"),
                (assign, ":new_party", reg(0)),
                (call_script, "script_party_add_party", ":new_party", "p_temp_party_2"),
                (party_set_faction, ":new_party", "fac_deserters"),
                (party_get_position, pos0,  ":new_party"),
                (party_set_ai_behavior, ":new_party", ai_bhvr_patrol_location),
                (party_set_ai_patrol_radius, ":new_party", 40),
                (party_set_ai_target_position, ":new_party", pos0),
                (store_party_size_wo_prisoners, ":party_count1", ":new_party"),
                (try_begin),
                  (gt, ":party_count1", 25),
                  (party_add_leader, ":new_party", "trp_looter_leader2", 1),
                (try_end),
                #				(display_log_message,"@party broke apart near {s33}"),
              (try_end),
            (try_end),
            
            #clean up small ship bandit parties -- there is no other mechanism that does this (like the one that sends routed enemies to nearest center)
          (else_try),
            (party_get_slot, ":spawn_point", ":party_no", slot_party_spawn_point),
            (is_between, ":spawn_point", spawn_points_begin, spawn_points_end),
            (party_get_slot, ":flags", ":spawn_point", slot_party_spawn_flags),
            (store_and, reg1, ":flags", spsf_seaborne),
            (neq, reg1, 0),
            (lt, ":party_count", 6),	#fishers are generally 3, but not always available to bandits
            (remove_party, ":party_no"),
            
          #VC-3825 just remove ghost parties here, as there are dozens of places where they could be made
          (else_try),
            (party_get_num_companion_stacks, reg4, ":party_no"),
            (gt, reg4, 0),
            
            (party_stack_get_troop_id, ":commander", ":party_no", 0),
            (is_between, ":commander", active_npcs_begin, active_npcs_end),
            
            (troop_get_slot, ":commander_party", ":commander", slot_troop_leaded_party),
            (neq, ":party_no", ":commander_party"),
            (remove_party, ":party_no"),
            
          #VC-3829 fix remnants of defeated factions
          (else_try),
            (eq, ":homes_fixed", 0),
            (party_get_slot, ":cur_center", ":party_no", slot_party_home_center),
            
            (try_begin),
              (is_between, ":cur_center", centers_begin, centers_end),
              (store_faction_of_party, ":cur_faction", ":cur_center"),
              (party_set_faction, ":party_no", ":cur_faction"),
              
            (else_try), #seek port
              (party_get_slot, ":cur_town", ":party_no", slot_party_port_party),
              (is_between, ":cur_town", walled_centers_begin, walled_centers_end),
              (party_set_slot, ":party_no", slot_party_home_center, ":cur_town"),
              
            (else_try), #seek fishermen, etc.
              (neq, ":cur_center", 0),
              (try_for_range, ":cur_town", walled_centers_begin, walled_centers_end), #have to do it this way because no way to distinguish inactive from invalid parties
                (party_get_slot, ":cur_port", ":cur_town", slot_party_port_party),
                (eq, ":cur_port", ":cur_center"),
                (store_faction_of_party, ":cur_faction", ":cur_town"),
                (party_set_faction, ":party_no", ":cur_faction"),
              (try_end),
            (try_end),
          (try_end),
        (try_end),
        
        (store_and, reg0, "$first_time", first_time_fix_ports),
        (try_begin),
          (neq, reg0, 0), #ports were fixed before this trigger was called?
          (val_or, "$first_time", first_time_fix_home_center),
        (try_end),
        
        (val_or, "$first_time", first_time_fix_ports),
    ]),
    #STrig 170
    (24,
      []),
    (24,
      []),
    (24,
      []),
    (24,
      []),
    (24,
      []),
    (24,
      []),
    (24,
      []),
    (24,
      []),
    (24,
      []),
  ]
