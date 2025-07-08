from header_common import *
from header_operations import *
from header_parties import *
from header_items import *
from header_skills import *
from header_triggers import *
from header_troops import *
from header_terrain_types import *

from module_constants import *

####################################################################################################################
#  Each trigger contains the following fields:
# 1) Check interval: How frequently this trigger will be checked
# 2) Delay interval: Time to wait before applying the consequences of the trigger
#    After its conditions have been evaluated as true.
# 3) Re-arm interval. How much time must pass after applying the consequences of the trigger for the trigger to become active again.
#    You can put the constant ti_once here to make sure that the trigger never becomes active again after it fires once.
# 4) Conditions block (list). This must be a valid operation block. See header_operations.py for reference.
#    Every time the trigger is checked, the conditions block will be executed.
#    If the conditions block returns true, the consequences block will be executed.
#    If the conditions block is empty, it is assumed that it always evaluates to true.
# 5) Consequences block (list). This must be a valid operation block. See header_operations.py for reference.
####################################################################################################################

# Some constants for use below
merchant_inventory_space = 30
num_merchandise_goods = 36



triggers = [
  # Tutorial:
  #  (0.1, 0, ti_once, [(map_free,0)], [(dialog_box,"str_tutorial_map1")]), #chief cambia
  (0.1, 0, ti_once,
    [
      (map_free,0),
    ],
    [
      (tutorial_box, "str_tutorial_map1", "@Tutorial"),
      
      # (try_begin),
      # (eq, "$campaign_type", camp_sandbox),
      # (start_presentation, "prsnt_start_sandbox"),
      # (tutorial_box, "str_tutorial_map1", "@Tutorial"),
      # (else_try),
      # (this_or_next|eq, "$campaign_type",  camp_kingc),
      # (eq, "$campaign_type", camp_lordc),
      # (start_presentation, "prsnt_start_kingcampaign"),
      # (else_try),
      # (start_presentation, "prsnt_start_storyline"),
      # (tutorial_box, "str_tutorial_map1", "@Tutorial"),
      # (try_end),
      (call_script, "script_set_parties_around_player_ignore_player", 90, 100), #Add 90 to 100 hours without bandits attacks
      # phaiak (28.12.14):
      (try_begin),
        (eq, "$campaign_type", camp_storyline),
        (troop_get_slot, ":jarl_kennemer_party", "trp_knight_4_3", slot_troop_leaded_party),
        (call_script, "script_party_set_ai_state", ":jarl_kennemer_party", spai_holding_center, "p_castle_63"),
      (end_try),
  ]),
  (2, 0, ti_once, [(map_free,0), (check_quest_active, "qst_recruit_an_army"),
      (call_script, "script_party_count_members_with_full_health", "p_main_party"),
      (ge, reg0, 15),
      ], [ (tutorial_box, "str_tutorial_map11", "@Recruiting warriors"),
      (call_script, "script_succeed_quest", "qst_recruit_an_army"),
  ]),
  
  # Refresh Merchants
  (0.0, 0, 168.0, [],
    [
      (call_script, "script_refresh_center_inventories"),
  ]),
  
  # Refresh Armor sellers
  (0.0, 0, 168.0, [],
    [
      (call_script, "script_refresh_center_armories"),
  ]),
  
  # Refresh Weapon sellers
  (0.0, 0, 168.0, [],
    [
      (call_script, "script_refresh_center_weaponsmiths"),
  ]),
  
  # Refresh Horse sellers
  (0.0, 0, 168.0, [],
    [
      (call_script, "script_refresh_center_stables"),
  ]),
  
  ### PHAIAK chief begin
  # Refresh Ship sellers
  (0.0, 0, 168.0, [],
    [
      (call_script, "script_give_ships_to_towns"),
  ]),
  
  # update party icons
  (7.7, 0, 0, [], [
      (try_for_parties, ":party"),
        (gt, ":party", "p_spawn_points_end"),
        (party_is_active, ":party"),
        (call_script, "script_update_party_icon", ":party"),
      (try_end),
  ]),
  
  # Testing season Duck season
  (0, 0, 0,
    [
      (try_begin),#VC-946
        (key_clicked, key_p),
        (key_is_down, key_left_control),
        (key_is_down, key_left_alt),
        (rest_for_hours, 0, 0, 0),
      (try_end),
      
      (key_clicked, key_d),#key_v
      (key_is_down, key_left_control),
      (ge, "$vc_debug_mode", 1),
    ],
    [
      (start_presentation, "prsnt_vc_debug"),
      # I moved some to prsnt_vc_debug
      # Please move also all others you need
      ]),
      
      # refill sea parties
      (10.2, 0, 0.0, [],
        [
          (assign, "$pin_party_template", "pt_fisher_ship"),
          (assign, "$pin_limit", 20),
          (call_script,"script_refill_sea_party_template"),
          
          (assign, "$pin_party_template", "pt_traveller_ship"),
          (assign, "$pin_limit", 18),
          (call_script,"script_refill_sea_party_template"),
          
          (assign, "$pin_party_template", "pt_slave_trader_ship"),
          (assign, "$pin_limit", 10),
          (call_script,"script_refill_sea_party_template"),
          
          (assign, "$pin_party_template", "pt_sea_king_danish"),
          (assign, "$pin_limit", 1),
          (call_script,"script_refill_sea_king_partys", "fac_kingdom_1"),
          
          (assign, "$pin_party_template", "pt_sea_king_norweg"),
          (assign, "$pin_limit", 1),
          (call_script,"script_refill_sea_king_partys", "fac_kingdom_2"),
          
          #Piggybacking for boar hunting (VC-2015):
          (try_begin),
            (party_slot_eq, "p_main_party", slot_party_on_water, 0),
            (store_random_in_range, ":rand", 0, 3),
            (eq, ":rand", 0),
            (try_begin),
              (store_num_parties_of_template, reg22, "pt_boar_herd"),
              (lt, reg22, 1),
              (set_spawn_radius, 15),
              (spawn_around_party, "p_main_party", "pt_boar_herd"),
            (else_try),
              (store_random_party_of_template, ":party", "pt_boar_herd"),
              (store_distance_to_party_from_party, ":distance", "p_main_party", ":party"),
              (gt, ":distance", 30),
              (remove_party, ":party"),
            (end_try),
          (end_try),
          # (assign, "$pin_party_template", "pt_boar_herd"),
          # (assign, "$pin_limit", 1),
          # (call_script,"script_refill_animal_parties"),
          
      ]),
      
      # #in exchange for the old "find landing points" trigger here is a new solution
      (0, 0, 0,
        [
          (key_clicked, key_left_mouse_button),
          (party_slot_eq, "p_main_party", slot_party_on_water, 1),
          
          (set_fixed_point_multiplier, 100),
          (party_get_position, pos1, "p_main_party"),
          (party_get_position, pos2, "p_landing_point"),
          (get_distance_between_positions, ":distance", pos1, pos2),
          (gt, ":distance", 400),
		  #VC-3653
		  (set_fixed_point_multiplier, 1),
		  (position_get_x, ":x", pos1),
		  (gt, ":x", map_min_x),
		  (lt, ":x", map_max_x),
		  (position_get_y, ":y", pos1),
		  (gt, ":y", map_min_y),
		  (lt, ":y", map_max_y),
		  (set_fixed_point_multiplier, 100),
          #
          (map_get_land_position_around_position, pos2, pos1, 4),
          (party_set_position, "p_temp_party", pos2),
          (party_get_current_terrain, ":terrain_type", "p_temp_party"),
          (neq, ":terrain_type", 0),
          (neq, ":terrain_type", 1), #cliffs
          (neq, ":terrain_type", 7),
          (neq, ":terrain_type", 8),
          
          (assign, ":block", 0),
          (try_for_range, ":curr_town", towns_begin, towns_end),	#avoid landing points next to ports
            (party_slot_eq, ":curr_town", slot_town_port, 1),
            (store_distance_to_party_from_party, ":dist", "p_temp_party", ":curr_town"),
            (lt, ":dist", 5),
            (assign, ":block", 1),
          (end_try),
          (try_for_range, ":curr_bridge", "p_Bridge_1", "p_ferry_1a"),	#avoid landing points next to bridges
            (store_distance_to_party_from_party, ":dist", "p_temp_party", ":curr_bridge"),
            (lt, ":dist", 5),
            (assign, ":block", 1),
          (end_try),
          (eq, ":block", 0),
          
        ],
        [
          (try_begin),
            (party_get_position, pos1, "p_temp_party"),
            (call_script, "script_get_next_water_position", 0),
            (party_set_position, "p_landing_point", pos2),
          (end_try),
      ]),
      
      (5.7, 0, 0.0,
        [
          (store_num_parties_of_template, reg2, "pt_manhunters"),
          (lt, reg2, 6)  #one per major land mass
        ],
        [
          (set_spawn_radius, 1),
          (store_add, ":p_town_22_plus_one", "p_town_29", 1),  #chief cambia, VC has 29 towns
          (store_random_in_range, ":selected_town", "p_town_1", ":p_town_22_plus_one"),
          (try_begin),
            (this_or_next|neq, ":selected_town", "p_town_4"),
            (this_or_next|neq, ":selected_town", "p_town_5"),
            (neq, ":selected_town", "p_town_11"),
            (spawn_around_party, ":selected_town", "pt_manhunters"),
          (try_end),
      ]),
      
      
      
      (1.0, 0.0, 0.0, [
          (check_quest_active, "qst_track_down_bandits"),
          (neg|check_quest_failed, "qst_track_down_bandits"),
          (neg|check_quest_succeeded, "qst_track_down_bandits"),
          
        ],
        [
          (quest_get_slot, ":bandit_party", "qst_track_down_bandits", slot_quest_target_party),
          (try_begin),
            (party_is_active, ":bandit_party"),
            (store_faction_of_party, ":bandit_party_faction", ":bandit_party"),
            (neg|is_between, ":bandit_party_faction", kingdoms_begin, kingdoms_end), #ie, the party has not respawned as a non-bandit
            
            
            (assign, ":spot_range", 8),
            (try_begin),
              (is_currently_night),
              (assign, ":spot_range", 5),
            (try_end),
            
            (try_for_parties, ":party"),
              (gt, ":party", "p_spawn_points_end"),
              
              (store_faction_of_party, ":faction", ":party"),
              (is_between, ":faction", kingdoms_begin, kingdoms_end),
              
              
              (store_distance_to_party_from_party, ":distance", ":party", ":bandit_party"),
              (lt, ":distance", ":spot_range"),
              (try_begin),
                (eq, "$cheat_mode", 1),
                (str_store_party_name, s4, ":party"),
                (display_message, "@{!}DEBUG -- Wanted bandits spotted by {s4}"),
              (try_end),
              
              (call_script, "script_get_closest_center", ":bandit_party"),
              (assign, ":nearest_center", reg0),
              #			(try_begin),
              #				(get_party_ai_current_behavior, ":behavior", ":party"),
              #				(eq, ":behavior", ai_bhvr_attack_party),
              #				(call_script, "script_add_log_entry",  logent_party_chases_wanted_bandits, ":party",  ":nearest_center", ":bandit_party", -1),
              #			(else_try),
              #				(eq, ":behavior", ai_bhvr_avoid_party),
              #				(call_script, "script_add_log_entry",  logent_party_runs_from_wanted_bandits, ":party",  ":nearest_center", ":bandit_party", -1),
              #			(else_try),
              (call_script, "script_add_log_entry",  logent_party_spots_wanted_bandits, ":party",  ":nearest_center", ":bandit_party", -1),
              #			(try_end),
            (try_end),
          (else_try), #Party not found
            (display_message, "str_bandits_eliminated_by_another"),
            (call_script, "script_abort_quest", "qst_track_down_bandits", 0),
          (try_end),
      ]),
      
      (1.0, 0.0, 0.0, [
          (check_quest_active, "qst_blank_quest_4"),
          (neg|check_quest_failed, "qst_blank_quest_4"),
          (neg|check_quest_succeeded, "qst_blank_quest_4"),
          
        ],
        [
          (quest_get_slot, ":bandit_party", "qst_blank_quest_4", slot_quest_target_party),
          (try_begin),
            (party_is_active, ":bandit_party"),
            (store_faction_of_party, ":bandit_party_faction", ":bandit_party"),
            (neg|is_between, ":bandit_party_faction", kingdoms_begin, kingdoms_end), #ie, the party has not respawned as a non-bandit
            
            
            (assign, ":spot_range", 8),
            (try_begin),
              (is_currently_night),
              (assign, ":spot_range", 5),
            (try_end),
            
            (try_for_parties, ":party"),
              (gt, ":party", "p_spawn_points_end"),
              
              (store_faction_of_party, ":faction", ":party"),
              (is_between, ":faction", kingdoms_begin, kingdoms_end),
              
              
              (store_distance_to_party_from_party, ":distance", ":party", ":bandit_party"),
              (lt, ":distance", ":spot_range"),
              (try_begin),
                (eq, "$cheat_mode", 1),
                (str_store_party_name, s4, ":party"),
                (display_message, "@{!}DEBUG -- Wanted bandits spotted by {s4}"),
              (try_end),
              
              (call_script, "script_get_closest_center", ":bandit_party"),
              (assign, ":nearest_center", reg0),
              #			(try_begin),
              #				(get_party_ai_current_behavior, ":behavior", ":party"),
              #				(eq, ":behavior", ai_bhvr_attack_party),
              #				(call_script, "script_add_log_entry",  logent_party_chases_wanted_bandits, ":party",  ":nearest_center", ":bandit_party", -1),
              #			(else_try),
              #				(eq, ":behavior", ai_bhvr_avoid_party),
              #				(call_script, "script_add_log_entry",  logent_party_runs_from_wanted_bandits, ":party",  ":nearest_center", ":bandit_party", -1),
              #			(else_try),
              (call_script, "script_add_log_entry",  logent_party_spots_wanted_bandits, ":party",  ":nearest_center", ":bandit_party", -1),
              #			(try_end),
            (try_end),
          (else_try), #Party not found
            (display_message, "str_bandits_eliminated_by_another"),
            (call_script, "script_abort_quest", "qst_blank_quest_4", 0),
          (try_end),
      ]),
      
      #Tax Collectors
      # Prisoner Trains
      #  (4.1, 0, 0.0, [],
      #                     [
      #                         (assign, "$pin_faction", "fac_swadians"),
      #                         (assign, "$pin_party_template", "pt_swadian_prisoner_train"),
      #                         (assign, "$pin_limit", peak_prisoner_trains),
      #                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
      #                         (party_set_ai_behavior,"$pout_party",ai_bhvr_travel_to_party),
      #                         (party_set_ai_object,"$pout_party","$pout_town"),
      #                    ]),
      #
      #  (4.1, 0, 0.0, [],
      #                     [
      #                         (assign, "$pin_faction", "fac_vaegirs"),
      #                         (assign, "$pin_party_template", "pt_vaegir_prisoner_train"),
      #                         (assign, "$pin_limit", peak_prisoner_trains),
      #                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
      #                         (party_set_ai_behavior,"$pout_party",ai_bhvr_travel_to_party),
      #                         (party_set_ai_object,"$pout_party","$pout_town"),
      #                    ]),
      
      (2.0, 0, 0, [(store_random_party_of_template, reg(2), "pt_prisoner_train_party"),
          (party_is_in_any_town,reg(2)),
        ],
        [(store_faction_of_party, ":faction_no", reg(2)),
          (call_script,"script_cf_select_random_walled_center_with_faction", ":faction_no", -1),
          (party_set_ai_behavior,reg(2),ai_bhvr_travel_to_party),
          (party_set_ai_object,reg(2),reg0),
          (party_set_flags, reg(2), pf_default_behavior, 0),
      ]),
      
      ##Caravans
      #  (4.2, 0, 0.0, [],
      #                     [
      #                         (assign, "$pin_faction", "fac_swadians"),
      #                         (assign, "$pin_party_template", "pt_swadian_caravan"),
      #                         (assign, "$pin_limit", peak_kingdom_caravans),
      #                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
      #                         (party_set_ai_behavior,"$pout_party",ai_bhvr_travel_to_party),
      #                         (party_set_ai_object,"$pout_party","$pout_town"),
      #                    ]),
      
      #  (4.2, 0, 0.0, [],
      #                     [
      #                         (assign, "$pin_faction", "fac_vaegirs"),
      #                         (assign, "$pin_party_template", "pt_vaegir_caravan"),
      #                         (assign, "$pin_limit", peak_kingdom_caravans),
      #                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
      #                         (party_set_ai_behavior,"$pout_party",ai_bhvr_travel_to_party),
      #                         (party_set_ai_object,"$pout_party","$pout_town"),
      #                    ]),
      
      ##  (2.0, 0, 0, [(store_random_party_of_template, reg(2), "pt_kingdom_caravan_party"),
      ##               (party_is_in_any_town,reg(2)),
      ##               ],
      ##              [(store_faction_of_party, ":faction_no", reg(2)),
      ##               (call_script,"script_cf_select_random_town_with_faction", ":faction_no"),
      ##               (party_set_ai_behavior,reg(2),ai_bhvr_travel_to_party),
      ##               (party_set_ai_object,reg(2),reg0),
      ##               (party_set_flags, reg(2), pf_default_behavior, 0),
      ##            ]),
      
      (4.0, 0, 0.0,
        [
          (eq, "$caravan_escort_state", 1), #cancel caravan_escort_state if caravan leaves the destination
          (assign, ":continue", 0),
          (try_begin),
            (neg|party_is_active, "$caravan_escort_party_id"),
            (assign, ":continue", 1),
          (else_try),
            (get_party_ai_object, ":ai_object", "$caravan_escort_party_id"),
            (neq, ":ai_object", "$caravan_escort_destination_town"),
            (assign, ":continue", 1),
          (try_end),
          (eq, ":continue", 1),
        ],
        [
          (assign, "$caravan_escort_state", 0),
      ]),
      
      #Messengers
      #  (4.2, 0, 0.0, [],
      #   [(assign, "$pin_faction", "fac_swadians"),
      #    (assign, "$pin_party_template", "pt_briton_messenger"),
      #    (assign, "$pin_limit", peak_kingdom_messengers),
      #    (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
      #    (party_set_ai_behavior,"$pout_party",ai_bhvr_travel_to_party),
      #    (party_set_ai_object,"$pout_party","$pout_town"),
      #    ]),
      
      #  (4.2, 0, 0.0, [],
      #   [(assign, "$pin_faction", "fac_vaegirs"),
      #    (assign, "$pin_party_template", "pt_saxon_messenger"),
      #    (assign, "$pin_limit", peak_kingdom_caravans),
      #    (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
      #    (party_set_ai_behavior,"$pout_party",ai_bhvr_travel_to_party),
      #    (party_set_ai_object,"$pout_party","$pout_town"),
      #    ]),
      
      (1.5, 0, 0, [(store_random_party_of_template, reg(2), "pt_messenger_party"),
          (party_is_in_any_town,reg(2)),
        ],
        [(store_faction_of_party, ":faction_no", reg(2)),
          (call_script,"script_cf_select_random_walled_center_with_faction", ":faction_no", -1),
          (party_set_ai_behavior,reg(2),ai_bhvr_travel_to_party),
          (party_set_ai_object,reg(2),reg0),
          (party_set_flags, reg(2), pf_default_behavior, 0),
      ]),
      
      
      
      #Deserters
      
      #  (10.2, 0, 0.0, [],
      #                     [
      #                         (assign, "$pin_faction", "fac_swadians"),
      #                         (assign, "$pin_party_template", "pt_briton_deserters"),
      #                         (assign, "$pin_limit", 4),
      #                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
      #                    ]),
      
      #  (10.2, 0, 0.0, [],
      #                     [
      #                         (assign, "$pin_faction", "fac_vaegirs"),
      #                         (assign, "$pin_party_template", "pt_saxon_deserters"),
      #                         (assign, "$pin_limit", 4),
      #                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
      #                    ]),
      
      #Kingdom Parties
      (1.0, 0, 0.0, [],
        [(try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
            (faction_slot_eq, ":cur_kingdom", slot_faction_state, sfs_active),
            ##      (neq, ":cur_kingdom", "fac_player_supporters_faction"),
            ##      (try_begin),
            ##        (store_random_in_range, ":random_no", 0, 100),
            ##        (lt, ":random_no", 10),
            ##        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_forager),
            ##      (try_end),
            ##      (try_begin),
            ##        (store_random_in_range, ":random_no", 0, 100),
            ##        (lt, ":random_no", 10),
            ##        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_scout),
            ##      (try_end),
            ##      (try_begin),
            ##        (store_random_in_range, ":random_no", 0, 100),
            ##        (lt, ":random_no", 10),
            ##        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_patrol),
            ##      (try_end),
            ##      (try_begin),
            ##        (store_random_in_range, ":random_no", 0, 100),
            ##        (lt, ":random_no", 10),
            ##        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_messenger),
            ##      (try_end),
            (try_begin),
              (store_random_in_range, ":random_no", 0, 100),
              (lt, ":random_no", 10),
              (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_kingdom_caravan),
            (try_end),
            ##      (try_begin),
            ##        (store_random_in_range, ":random_no", 0, 100),
            ##        (lt, ":random_no", 10),
            ##        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_prisoner_train),
            ##      (try_end),
          (try_end),
      ]),
      
      
      #Swadians
      #  (0.0, 0.0, ti_once, [], [(assign,"$peak_swadian_foragers",4)]),
      #  (0.0, 0.0, ti_once, [], [(assign,"$peak_swadian_scouts",4)]),
      #  (0.0, 0.0, ti_once, [], [(assign,"$peak_swadian_harassers",3)]),
      #  (0.0, 0.0, ti_once, [], [(assign,"$peak_swadian_war_parties",2)]),
      
      
      #  (10.2, 0, 0.0, [],
      #                     [
      #                         (assign, "$pin_faction", "fac_swadians"),
      #                         (assign, "$pin_party_template", "pt_swadian_foragers"),
      #                         (assign, "$pin_limit", "$peak_swadian_foragers"),
      #                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
      #                    ]),
      
      #  (10.2, 0, 0.0, [],
      #                     [
      #                         (assign, "$pin_faction", "fac_swadians"),
      #                         (assign, "$pin_party_template", "pt_swadian_scouts"),
      #                         (assign, "$pin_limit", "$peak_swadian_scouts"),
      #                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
      #                    ]),
      
      #  (10.2, 0, 0.0, [],
      #                     [
      #                         (assign, "$pin_faction", "fac_swadians"),
      #                         (assign, "$pin_party_template", "pt_swadian_patrol"),
      #                         (assign, "$pin_limit", "$peak_swadian_harassers"),
      #                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
      #                    ]),
      
      #  (10.2, 0, 0.0, [],
      #                     [
      #                         (assign, "$pin_faction", "fac_swadians"),
      #                         (assign, "$pin_party_template", "pt_swadian_war_party"),
      #                         (assign, "$pin_limit", "$peak_swadian_war_parties"),
      #                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
      #                    ]),
      #Vaegirs
      #  (0.0, 0.0, ti_once, [], [(assign,"$peak_vaegir_foragers",4)]),
      #  (0.0, 0.0, ti_once, [], [(assign,"$peak_vaegir_scouts",4)]),
      #  (0.0, 0.0, ti_once, [], [(assign,"$peak_vaegir_harassers",3)]),
      #  (0.0, 0.0, ti_once, [], [(assign,"$peak_vaegir_war_parties",2)]),
      
      
      #  (10.2, 0, 0.0, [],
      #                     [
      #                         (assign, "$pin_faction", "fac_vaegirs"),
      #                         (assign, "$pin_party_template", "pt_vaegir_foragers"),
      #                         (assign, "$pin_limit", "$peak_vaegir_foragers"),
      #                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
      #                    ]),
      
      #  (10.2, 0, 0.0, [],
      #                     [
      #                         (assign, "$pin_faction", "fac_vaegirs"),
      #                         (assign, "$pin_party_template", "pt_vaegir_scouts"),
      #                         (assign, "$pin_limit", "$peak_vaegir_scouts"),
      #                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
      #                    ]),
      
      #  (10.2, 0, 0.0, [],
      #                     [
      #                         (assign, "$pin_faction", "fac_vaegirs"),
      #                         (assign, "$pin_party_template", "pt_vaegir_patrol"),
      #                         (assign, "$pin_limit", "$peak_vaegir_harassers"),
      #                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
      #                    ]),
      
      #  (10.2, 0, 0.0, [],
      #                     [
      #                         (assign, "$pin_faction", "fac_vaegirs"),
      #                         (assign, "$pin_party_template", "pt_vaegir_war_party"),
      #                         (assign, "$pin_limit", "$peak_vaegir_war_parties"),
      #                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
      #                    ]),
      
      #Villains etc.
      #  (14.2, 0, 0.0, [],
      #                     [
      #                         (assign, "$pin_faction", "fac_sea_raiders"),
      #                         (assign, "$pin_party_template", "pt_sea_raiders"),
      #                         (assign, "$pin_limit", 5),
      #                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
      #                    ]),
      
      
      #
      ##  (10.1, 0, 0.0, [],
      ##                     [
      ##                         (assign, "$pin_party_template", "pt_refugees"),
      ##                         (assign, "$pin_limit", 5),
      ##                         (call_script,"script_cf_spawn_party_at_random_town_if_below_limit"),
      ##                    ]),
      ##
      ##  (10.1, 0, 0.0, [],
      ##                     [
      ##                         (assign, "$pin_party_template", "pt_farmers"),
      ##                         (assign, "$pin_limit", 6),
      ##                         (call_script,"script_cf_spawn_party_at_random_town_if_below_limit"),
      ##                    ]),
      
      #  [1.0, 96.0, ti_once, [], [[assign,"$peak_dark_hunters",3]]],
      
      ##  (10.1, 0, 0.0, [],
      ##                     [
      ##                         (assign, "$pin_party_template", "pt_dark_hunters"),
      ##                         (assign, "$pin_limit", "$peak_dark_hunters"),
      ##                         (call_script,"script_cf_spawn_party_at_random_town_if_below_limit"),
      ##                    ]),
      
      #Companion quests
      
      ##  (0, 0, ti_once,
      ##   [
      ##       (entering_town,"p_town_1"),
      ##       (main_party_has_troop,"trp_borcha"),
      ##       (eq,"$borcha_freed",0)
      ##    ],
      ##
      ##   [
      ##       (assign,"$borcha_arrive_sargoth_as_prisoner", 1),
      ##       (start_map_conversation, "trp_borcha", -1)
      ##    ]
      ##   ),
      ##
      ##  (1, 0, ti_once,
      ##   [
      ##      (map_free,0),
      ##      (eq,"$borcha_asked_for_freedom",0),
      ##      (main_party_has_troop,"trp_borcha")
      ##    ],
      ##   [
      ##       (start_map_conversation, "trp_borcha", -1)
      ##    ]
      ##   ),
      ##
      ##  (2, 0, ti_once,
      ##   [
      ##      (map_free, 0),
      ##      (neq,"$borcha_asked_for_freedom",0),
      ##      (eq,"$borcha_freed",0),
      ##      (main_party_has_troop,"trp_borcha")
      ##    ],
      ##   [
      ##       (start_map_conversation, "trp_borcha", -1),
      ##    ]
      ##   ),
      
      ##### TODO: QUESTS COMMENT OUT BEGIN
      
      ###########################################################################
      ### Random Governer Quest triggers
      ###########################################################################
      
      # Incriminate Loyal Advisor quest
      (0.2, 0.0, 0.0,
        [
          (check_quest_active, "qst_incriminate_loyal_commander"),
          (neg|check_quest_concluded, "qst_incriminate_loyal_commander"),
          (quest_slot_eq, "qst_incriminate_loyal_commander", slot_quest_current_state, 2),
          (quest_get_slot, ":quest_target_center", "qst_incriminate_loyal_commander", slot_quest_target_center),
          (quest_get_slot, ":quest_target_party", "qst_incriminate_loyal_commander", slot_quest_target_party),
          (quest_get_slot, ":quest_object_troop", "qst_incriminate_loyal_commander", slot_quest_object_troop),
          (quest_get_slot, ":faction_no", "qst_incriminate_loyal_commander", slot_quest_target_faction),
          (store_faction_of_troop, ":cur_faction", ":quest_object_troop"),
          (try_begin),
            (neg|party_is_active, ":quest_target_party"),   #sacrifice party has been destroyed
            (quest_set_slot, "qst_incriminate_loyal_commander", slot_quest_current_state, 3),
            (call_script, "script_fail_quest", "qst_incriminate_loyal_commander"),
          (else_try),
            (neq, ":cur_faction", ":faction_no"),   #object troop has changed factions
            (remove_party, ":quest_target_party"),
            (quest_set_slot, "qst_incriminate_loyal_commander", slot_quest_current_state, 3),
            (call_script, "script_fail_quest", "qst_incriminate_loyal_commander"),
          (else_try),
            (party_is_in_town, ":quest_target_party", ":quest_target_center"),
            (remove_party, ":quest_target_party"),
            (quest_set_slot, "qst_incriminate_loyal_commander", slot_quest_current_state, 3),
            (call_script, "script_indict_lord_for_treason", ":quest_object_troop", ":faction_no"),
            (call_script, "script_succeed_quest", "qst_incriminate_loyal_commander"),
          (try_end),
        ],
        []
      ),
      # Runaway Peasants quest
      (0.2, 0.0, 0.0,
        [
          (check_quest_active, "qst_bring_back_runaway_serfs"),
          (neg|check_quest_concluded, "qst_bring_back_runaway_serfs"),
          (quest_get_slot, ":quest_object_center", "qst_bring_back_runaway_serfs", slot_quest_object_center),
          (quest_get_slot, ":quest_target_center", "qst_bring_back_runaway_serfs", slot_quest_target_center),
          (try_begin),
            (party_is_active, "$qst_bring_back_runaway_serfs_party_1"),
            (try_begin),
              (party_is_in_town, "$qst_bring_back_runaway_serfs_party_1", ":quest_target_center"),
              (remove_party, "$qst_bring_back_runaway_serfs_party_1"),
              (val_add, "$qst_bring_back_runaway_serfs_num_parties_fleed", 1),
            (else_try),
              (party_is_in_town, "$qst_bring_back_runaway_serfs_party_1", ":quest_object_center"),
              (remove_party, "$qst_bring_back_runaway_serfs_party_1"),
              (val_add, "$qst_bring_back_runaway_serfs_num_parties_returned", 1),
            (else_try),
              (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_bring_back_runaway_serfs_party_1"),
              (gt, ":cur_distance", 3),
              (party_set_ai_object, "$qst_bring_back_runaway_serfs_party_1", ":quest_target_center"),
            (try_end),
          (try_end),
          (try_begin),
            (party_is_active, "$qst_bring_back_runaway_serfs_party_2"),
            (try_begin),
              (party_is_in_town, "$qst_bring_back_runaway_serfs_party_2", ":quest_target_center"),
              (remove_party, "$qst_bring_back_runaway_serfs_party_2"),
              (val_add, "$qst_bring_back_runaway_serfs_num_parties_fleed", 1),
            (else_try),
              (party_is_in_town, "$qst_bring_back_runaway_serfs_party_2", ":quest_object_center"),
              (remove_party, "$qst_bring_back_runaway_serfs_party_2"),
              (val_add, "$qst_bring_back_runaway_serfs_num_parties_returned", 1),
            (else_try),
              (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_bring_back_runaway_serfs_party_2"),
              (gt, ":cur_distance", 3),
              (party_set_ai_object, "$qst_bring_back_runaway_serfs_party_2", ":quest_target_center"),
            (try_end),
          (try_end),
          (try_begin),
            (party_is_active, "$qst_bring_back_runaway_serfs_party_3"),
            (try_begin),
              (party_is_in_town, "$qst_bring_back_runaway_serfs_party_3", ":quest_target_center"),
              (remove_party, "$qst_bring_back_runaway_serfs_party_3"),
              (val_add, "$qst_bring_back_runaway_serfs_num_parties_fleed", 1),
            (else_try),
              (party_is_in_town, "$qst_bring_back_runaway_serfs_party_3", ":quest_object_center"),
              (remove_party, "$qst_bring_back_runaway_serfs_party_3"),
              (val_add, "$qst_bring_back_runaway_serfs_num_parties_returned", 1),
            (else_try),
              (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_bring_back_runaway_serfs_party_3"),
              (gt, ":cur_distance", 3),
              (party_set_ai_object, "$qst_bring_back_runaway_serfs_party_3", ":quest_target_center"),
            (try_end),
          (try_end),
          (assign, ":sum_removed", "$qst_bring_back_runaway_serfs_num_parties_returned"),
          (val_add, ":sum_removed", "$qst_bring_back_runaway_serfs_num_parties_fleed"),
          (ge, ":sum_removed", 3),
          (try_begin),
            (ge, "$qst_bring_back_runaway_serfs_num_parties_returned", 3),
            (call_script, "script_succeed_quest", "qst_bring_back_runaway_serfs"),
          (else_try),
            (eq, "$qst_bring_back_runaway_serfs_num_parties_returned", 0),
            (call_script, "script_fail_quest", "qst_bring_back_runaway_serfs"),
          (else_try),
            (call_script, "script_conclude_quest", "qst_bring_back_runaway_serfs"),
          (try_end),
        ],
        []
      ),
      ### Defend Nobles Against Peasants quest
      ##  (0.2, 0.0, 0.0,
      ##   [
      ##       (check_quest_active, "qst_defend_nobles_against_peasants"),
      ##       (neg|check_quest_succeeded, "qst_defend_nobles_against_peasants"),
      ##       (neg|check_quest_failed, "qst_defend_nobles_against_peasants"),
      ##       (quest_get_slot, ":quest_target_center", "qst_defend_nobles_against_peasants", slot_quest_target_center),
      ##       (assign, ":num_active_parties", 0),
      ##       (try_begin),
      ##         (gt, "$qst_defend_nobles_against_peasants_noble_party_1", 0),
      ##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_1"),
      ##         (val_add, ":num_active_parties", 1),
      ##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_1", ":quest_target_center"),
      ##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_1"),
      ##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_1"),
      ##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
      ##       (try_end),
      ##       (try_begin),
      ##         (gt, "$qst_defend_nobles_against_peasants_noble_party_2", 0),
      ##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_2"),
      ##         (val_add, ":num_active_parties", 1),
      ##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_2", ":quest_target_center"),
      ##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_2"),
      ##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_2"),
      ##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
      ##       (try_end),
      ##       (try_begin),
      ##         (gt, "$qst_defend_nobles_against_peasants_noble_party_3", 0),
      ##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_3"),
      ##         (val_add, ":num_active_parties", 1),
      ##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_3", ":quest_target_center"),
      ##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_3"),
      ##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_3"),
      ##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
      ##       (try_end),
      ##       (try_begin),
      ##         (gt, "$qst_defend_nobles_against_peasants_noble_party_4", 0),
      ##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_4"),
      ##         (val_add, ":num_active_parties", 1),
      ##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_4", ":quest_target_center"),
      ##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_4"),
      ##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_4"),
      ##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
      ##       (try_end),
      ##       (try_begin),
      ##         (gt, "$qst_defend_nobles_against_peasants_noble_party_5", 0),
      ##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_5"),
      ##         (val_add, ":num_active_parties", 1),
      ##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_5", ":quest_target_center"),
      ##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_5"),
      ##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_5"),
      ##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
      ##       (try_end),
      ##       (try_begin),
      ##         (gt, "$qst_defend_nobles_against_peasants_noble_party_6", 0),
      ##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_6"),
      ##         (val_add, ":num_active_parties", 1),
      ##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_6", ":quest_target_center"),
      ##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_6"),
      ##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_6"),
      ##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
      ##       (try_end),
      ##       (try_begin),
      ##         (gt, "$qst_defend_nobles_against_peasants_noble_party_7", 0),
      ##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_7"),
      ##         (val_add, ":num_active_parties", 1),
      ##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_7", ":quest_target_center"),
      ##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_7"),
      ##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_7"),
      ##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
      ##       (try_end),
      ##       (try_begin),
      ##         (gt, "$qst_defend_nobles_against_peasants_noble_party_8", 0),
      ##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_8"),
      ##         (val_add, ":num_active_parties", 1),
      ##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_8", ":quest_target_center"),
      ##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_8"),
      ##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_8"),
      ##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
      ##       (try_end),
      ##       (eq, ":num_active_parties", 0),
      ##       (try_begin),
      ##         (store_div, ":limit", "$qst_defend_nobles_against_peasants_num_nobles_to_save", 2),
      ##         (ge, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":limit"),
      ##         (call_script, "script_succeed_quest", "qst_defend_nobles_against_peasants"),
      ##       (else_try),
      ##         (call_script, "script_fail_quest", "qst_defend_nobles_against_peasants"),
      ##       (try_end),
      ##    ],
      ##   []
      ##   ),
      ### Capture Conspirators quest
      ##  (0.15, 0.0, 0.0,
      ##   [
      ##       (check_quest_active, "qst_capture_conspirators"),
      ##       (neg|check_quest_succeeded, "qst_capture_conspirators"),
      ##       (neg|check_quest_failed, "qst_capture_conspirators"),
      ##       (quest_get_slot, ":quest_target_center", "qst_capture_conspirators", slot_quest_target_center),
      ##       (quest_get_slot, ":faction_no", "qst_capture_conspirators", slot_quest_target_faction),
      ##       (try_begin),
      ##         (gt, "$qst_capture_conspirators_num_parties_to_spawn", "$qst_capture_conspirators_num_parties_spawned"),
      ##         (store_random_in_range, ":random_no", 0, 100),
      ##         (lt, ":random_no", 20),
      ##         (set_spawn_radius, 3),
      ##         (spawn_around_party,":quest_target_center","pt_conspirator"),
      ##         (val_add, "$qst_capture_conspirators_num_parties_spawned", 1),
      ##         (party_get_num_companions, ":num_companions", reg0),
      ##         (val_add, "$qst_capture_conspirators_num_troops_to_capture", ":num_companions"),
      ##         (party_set_ai_behavior, reg0, ai_bhvr_travel_to_party),
      ##         (party_set_ai_object, reg0, "$qst_capture_conspirators_party_1"),
      ##         (party_set_flags, reg0, pf_default_behavior, 0),
      ##         (try_begin),
      ##           (le, "$qst_capture_conspirators_party_2", 0),
      ##           (assign, "$qst_capture_conspirators_party_2", reg0),
      ##         (else_try),
      ##           (le, "$qst_capture_conspirators_party_3", 0),
      ##           (assign, "$qst_capture_conspirators_party_3", reg0),
      ##         (else_try),
      ##           (le, "$qst_capture_conspirators_party_4", 0),
      ##           (assign, "$qst_capture_conspirators_party_4", reg0),
      ##         (else_try),
      ##           (le, "$qst_capture_conspirators_party_5", 0),
      ##           (assign, "$qst_capture_conspirators_party_5", reg0),
      ##         (else_try),
      ##           (le, "$qst_capture_conspirators_party_6", 0),
      ##           (assign, "$qst_capture_conspirators_party_6", reg0),
      ##         (else_try),
      ##           (le, "$qst_capture_conspirators_party_7", 0),
      ##           (assign, "$qst_capture_conspirators_party_7", reg0),
      ##         (try_end),
      ##       (try_end),
      ##
      ##       (assign, ":num_active_parties", 0),
      ##
      ##       (try_begin),
      ##         (gt, "$qst_capture_conspirators_party_1", 0),
      ##         (party_is_active, "$qst_capture_conspirators_party_1"),
      ##         (val_add, ":num_active_parties", 1),
      ##         (try_begin),
      ##           (party_is_in_any_town, "$qst_capture_conspirators_party_1"),
      ##           (remove_party, "$qst_capture_conspirators_party_1"),
      ##         (else_try),
      ##           (party_get_num_attached_parties, ":num_attachments", "$qst_capture_conspirators_party_1"),
      ##           (gt, ":num_attachments", 0),
      ##           (assign, ":leave_meeting", 0),
      ##           (try_begin),
      ##             (store_sub, ":required_attachments", "$qst_capture_conspirators_num_parties_to_spawn", 1),
      ##             (eq, ":num_attachments", ":required_attachments"),
      ##             (val_add, "$qst_capture_conspirators_leave_meeting_counter", 1),
      ##             (ge, "$qst_capture_conspirators_leave_meeting_counter", 15),
      ##             (assign, ":leave_meeting", 1),
      ##           (try_end),
      ##           (try_begin),
      ##             (eq, "$qst_capture_conspirators_num_parties_to_spawn", "$qst_capture_conspirators_num_parties_spawned"),
      ##             (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_capture_conspirators_party_1"),
      ##             (assign, ":min_distance", 3),
      ##             (try_begin),
      ##               (is_currently_night),
      ##               (assign, ":min_distance", 2),
      ##             (try_end),
      ##             (lt, ":cur_distance", ":min_distance"),
      ##             (assign, "$qst_capture_conspirators_leave_meeting_counter", 15),
      ##             (assign, ":leave_meeting", 1),
      ##           (try_end),
      ##           (eq, ":leave_meeting", 1),
      ##           (party_set_ai_behavior, "$qst_capture_conspirators_party_1", ai_bhvr_travel_to_point),
      ##           (party_set_flags, "$qst_capture_conspirators_party_1", pf_default_behavior, 0),
      ##           (party_get_position, pos1, "$qst_capture_conspirators_party_1"),
      ##           (call_script, "script_map_get_random_position_around_position_within_range", 15, 17),
      ##           (party_set_ai_target_position, "$qst_capture_conspirators_party_1", pos2),
      ##           (try_begin),
      ##             (gt, "$qst_capture_conspirators_party_2", 0),
      ##             (party_detach, "$qst_capture_conspirators_party_2"),
      ##             (party_set_ai_behavior, "$qst_capture_conspirators_party_2", ai_bhvr_travel_to_point),
      ##             (party_set_flags, "$qst_capture_conspirators_party_2", pf_default_behavior, 0),
      ##             (call_script, "script_map_get_random_position_around_position_within_range", 15, 17),
      ##             (party_set_ai_target_position, "$qst_capture_conspirators_party_2", pos2),
      ##           (try_end),
      ##           (try_begin),
      ##             (gt, "$qst_capture_conspirators_party_3", 0),
      ##             (party_detach, "$qst_capture_conspirators_party_3"),
      ##             (party_set_ai_behavior, "$qst_capture_conspirators_party_3", ai_bhvr_travel_to_point),
      ##             (party_set_flags, "$qst_capture_conspirators_party_3", pf_default_behavior, 0),
      ##             (call_script, "script_map_get_random_position_around_position_within_range", 15, 17),
      ##             (party_set_ai_target_position, "$qst_capture_conspirators_party_3", pos2),
      ##           (try_end),
      ##           (try_begin),
      ##             (gt, "$qst_capture_conspirators_party_4", 0),
      ##             (party_detach, "$qst_capture_conspirators_party_4"),
      ##             (party_set_ai_behavior, "$qst_capture_conspirators_party_4", ai_bhvr_travel_to_point),
      ##             (party_set_flags, "$qst_capture_conspirators_party_4", pf_default_behavior, 0),
      ##             (call_script, "script_map_get_random_position_around_position_within_range", 15, 17),
      ##             (party_set_ai_target_position, "$qst_capture_conspirators_party_4", pos2),
      ##           (try_end),
      ##           (try_begin),
      ##             (gt, "$qst_capture_conspirators_party_5", 0),
      ##             (party_detach, "$qst_capture_conspirators_party_5"),
      ##             (party_set_ai_behavior, "$qst_capture_conspirators_party_5", ai_bhvr_travel_to_point),
      ##             (party_set_flags, "$qst_capture_conspirators_party_5", pf_default_behavior, 0),
      ##             (call_script, "script_map_get_random_position_around_position_within_range", 15, 17),
      ##             (party_set_ai_target_position, "$qst_capture_conspirators_party_5", pos2),
      ##           (try_end),
      ##           (try_begin),
      ##             (gt, "$qst_capture_conspirators_party_6", 0),
      ##             (party_detach, "$qst_capture_conspirators_party_6"),
      ##             (party_set_ai_behavior, "$qst_capture_conspirators_party_6", ai_bhvr_travel_to_point),
      ##             (party_set_flags, "$qst_capture_conspirators_party_6", pf_default_behavior, 0),
      ##             (call_script, "script_map_get_random_position_around_position_within_range", 15, 17),
      ##             (party_set_ai_target_position, "$qst_capture_conspirators_party_6", pos2),
      ##           (try_end),
      ##           (try_begin),
      ##             (gt, "$qst_capture_conspirators_party_7", 0),
      ##             (party_detach, "$qst_capture_conspirators_party_7"),
      ##             (party_set_ai_behavior, "$qst_capture_conspirators_party_7", ai_bhvr_travel_to_point),
      ##             (party_set_flags, "$qst_capture_conspirators_party_7", pf_default_behavior, 0),
      ##             (call_script, "script_map_get_random_position_around_position_within_range", 15, 17),
      ##             (party_set_ai_target_position, "$qst_capture_conspirators_party_7", pos2),
      ##           (try_end),
      ##         (try_end),
      ##         (try_begin),
      ##           (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_1"),
      ##           (eq, ":ai_behavior", ai_bhvr_travel_to_point),
      ##           (party_get_ai_target_position, pos2, "$qst_capture_conspirators_party_1"),
      ##           (party_get_position, pos1, "$qst_capture_conspirators_party_1"),
      ##           (get_distance_between_positions, ":distance", pos2, pos1),
      ##           (lt, ":distance", 200),
      ##           (call_script, "script_get_closest_walled_center_of_faction", "$qst_capture_conspirators_party_1", ":faction_no"),#Can fail
      ##           (ge, reg0, 0),
      ##           (party_set_ai_object, "$qst_capture_conspirators_party_1", reg0),
      ##           (party_set_ai_behavior, "$qst_capture_conspirators_party_1", ai_bhvr_travel_to_party),
      ##           (party_set_flags, "$qst_capture_conspirators_party_1", pf_default_behavior, 0),
      ##         (try_end),
      ##       (try_end),
      ##       (try_begin),
      ##         (gt, "$qst_capture_conspirators_party_2", 0),
      ##         (party_is_active, "$qst_capture_conspirators_party_2"),
      ##         (val_add, ":num_active_parties", 1),
      ##         (try_begin),
      ##           (party_is_in_any_town, "$qst_capture_conspirators_party_2"),
      ##           (try_begin),
      ##             (neg|party_is_in_town, "$qst_capture_conspirators_party_2", "$qst_capture_conspirators_party_1"),
      ##             (remove_party, "$qst_capture_conspirators_party_2"),
      ##           (else_try),
      ##             (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_2"),
      ##             (neq, ":ai_behavior", ai_bhvr_hold),
      ##             (party_set_ai_behavior, "$qst_capture_conspirators_party_2", ai_bhvr_hold),
      ##             (party_attach_to_party, "$qst_capture_conspirators_party_2", "$qst_capture_conspirators_party_1"),
      ##             (party_set_flags, "$qst_capture_conspirators_party_2", pf_default_behavior, 0),
      ##           (try_end),
      ##         (try_end),
      ##         (try_begin),
      ##           (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_2"),
      ##           (eq, ":ai_behavior", ai_bhvr_travel_to_point),
      ##           (party_get_ai_target_position, pos2, "$qst_capture_conspirators_party_2"),
      ##           (party_get_position, pos1, "$qst_capture_conspirators_party_2"),
      ##           (get_distance_between_positions, ":distance", pos2, pos1),
      ##           (lt, ":distance", 200),
      ##           (call_script, "script_get_closest_walled_center_of_faction", "$qst_capture_conspirators_party_2", ":faction_no"),#Can fail
      ##           (ge, reg0, 0),
      ##           (party_set_ai_object, "$qst_capture_conspirators_party_2", reg0),
      ##           (party_set_ai_behavior, "$qst_capture_conspirators_party_2", ai_bhvr_travel_to_party),
      ##           (party_set_flags, "$qst_capture_conspirators_party_2", pf_default_behavior, 0),
      ##         (try_end),
      ##       (try_end),
      ##       (try_begin),
      ##         (gt, "$qst_capture_conspirators_party_3", 0),
      ##         (party_is_active, "$qst_capture_conspirators_party_3"),
      ##         (val_add, ":num_active_parties", 1),
      ##         (try_begin),
      ##           (party_is_in_any_town, "$qst_capture_conspirators_party_3"),
      ##           (try_begin),
      ##             (neg|party_is_in_town, "$qst_capture_conspirators_party_3", "$qst_capture_conspirators_party_1"),
      ##             (remove_party, "$qst_capture_conspirators_party_3"),
      ##           (else_try),
      ##             (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_3"),
      ##             (neq, ":ai_behavior", ai_bhvr_hold),
      ##             (party_set_ai_behavior, "$qst_capture_conspirators_party_3", ai_bhvr_hold),
      ##             (party_attach_to_party, "$qst_capture_conspirators_party_3", "$qst_capture_conspirators_party_1"),
      ##             (party_set_flags, "$qst_capture_conspirators_party_3", pf_default_behavior, 0),
      ##           (try_end),
      ##         (try_end),
      ##         (try_begin),
      ##           (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_3"),
      ##           (eq, ":ai_behavior", ai_bhvr_travel_to_point),
      ##           (party_get_ai_target_position, pos2, "$qst_capture_conspirators_party_3"),
      ##           (party_get_position, pos1, "$qst_capture_conspirators_party_3"),
      ##           (get_distance_between_positions, ":distance", pos2, pos1),
      ##           (lt, ":distance", 200),
      ##           (call_script, "script_get_closest_walled_center_of_faction", "$qst_capture_conspirators_party_3", ":faction_no"),#Can fail
      ##           (ge, reg0, 0),
      ##           (party_set_ai_object, "$qst_capture_conspirators_party_3", reg0),
      ##           (party_set_ai_behavior, "$qst_capture_conspirators_party_3", ai_bhvr_travel_to_party),
      ##           (party_set_flags, "$qst_capture_conspirators_party_3", pf_default_behavior, 0),
      ##         (try_end),
      ##       (try_end),
      ##       (try_begin),
      ##         (gt, "$qst_capture_conspirators_party_4", 0),
      ##         (party_is_active, "$qst_capture_conspirators_party_4"),
      ##         (val_add, ":num_active_parties", 1),
      ##         (try_begin),
      ##           (party_is_in_any_town, "$qst_capture_conspirators_party_4"),
      ##           (try_begin),
      ##             (neg|party_is_in_town, "$qst_capture_conspirators_party_4", "$qst_capture_conspirators_party_1"),
      ##             (remove_party, "$qst_capture_conspirators_party_4"),
      ##           (else_try),
      ##             (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_4"),
      ##             (neq, ":ai_behavior", ai_bhvr_hold),
      ##             (party_set_ai_behavior, "$qst_capture_conspirators_party_4", ai_bhvr_hold),
      ##             (party_set_flags, "$qst_capture_conspirators_party_4", pf_default_behavior, 0),
      ##             (party_attach_to_party, "$qst_capture_conspirators_party_4", "$qst_capture_conspirators_party_1"),
      ##           (try_end),
      ##         (try_end),
      ##         (try_begin),
      ##           (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_4"),
      ##           (eq, ":ai_behavior", ai_bhvr_travel_to_point),
      ##           (party_get_ai_target_position, pos2, "$qst_capture_conspirators_party_4"),
      ##           (party_get_position, pos1, "$qst_capture_conspirators_party_4"),
      ##           (get_distance_between_positions, ":distance", pos2, pos1),
      ##           (lt, ":distance", 200),
      ##           (call_script, "script_get_closest_walled_center_of_faction", "$qst_capture_conspirators_party_4", ":faction_no"),#Can fail
      ##           (ge, reg0, 0),
      ##           (party_set_ai_object, "$qst_capture_conspirators_party_4", reg0),
      ##           (party_set_ai_behavior, "$qst_capture_conspirators_party_4", ai_bhvr_travel_to_party),
      ##           (party_set_flags, "$qst_capture_conspirators_party_4", pf_default_behavior, 0),
      ##         (try_end),
      ##       (try_end),
      ##       (try_begin),
      ##         (gt, "$qst_capture_conspirators_party_5", 0),
      ##         (party_is_active, "$qst_capture_conspirators_party_5"),
      ##         (val_add, ":num_active_parties", 1),
      ##         (try_begin),
      ##           (party_is_in_any_town, "$qst_capture_conspirators_party_5"),
      ##           (try_begin),
      ##             (neg|party_is_in_town, "$qst_capture_conspirators_party_5", "$qst_capture_conspirators_party_1"),
      ##             (remove_party, "$qst_capture_conspirators_party_5"),
      ##           (else_try),
      ##             (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_5"),
      ##             (neq, ":ai_behavior", ai_bhvr_hold),
      ##             (party_set_ai_behavior, "$qst_capture_conspirators_party_5", ai_bhvr_hold),
      ##             (party_set_flags, "$qst_capture_conspirators_party_5", pf_default_behavior, 0),
      ##             (party_attach_to_party, "$qst_capture_conspirators_party_5", "$qst_capture_conspirators_party_1"),
      ##           (try_end),
      ##         (try_end),
      ##         (try_begin),
      ##           (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_5"),
      ##           (eq, ":ai_behavior", ai_bhvr_travel_to_point),
      ##           (party_get_ai_target_position, pos2, "$qst_capture_conspirators_party_5"),
      ##           (party_get_position, pos1, "$qst_capture_conspirators_party_5"),
      ##           (get_distance_between_positions, ":distance", pos2, pos1),
      ##           (lt, ":distance", 200),
      ##           (call_script, "script_get_closest_walled_center_of_faction", "$qst_capture_conspirators_party_5", ":faction_no"),#Can fail
      ##           (ge, reg0, 0),
      ##           (party_set_ai_object, "$qst_capture_conspirators_party_5", reg0),
      ##           (party_set_ai_behavior, "$qst_capture_conspirators_party_5", ai_bhvr_travel_to_party),
      ##           (party_set_flags, "$qst_capture_conspirators_party_5", pf_default_behavior, 0),
      ##         (try_end),
      ##       (try_end),
      ##       (try_begin),
      ##         (gt, "$qst_capture_conspirators_party_6", 0),
      ##         (party_is_active, "$qst_capture_conspirators_party_6"),
      ##         (val_add, ":num_active_parties", 1),
      ##         (try_begin),
      ##           (party_is_in_any_town, "$qst_capture_conspirators_party_6"),
      ##           (try_begin),
      ##             (neg|party_is_in_town, "$qst_capture_conspirators_party_6", "$qst_capture_conspirators_party_1"),
      ##             (remove_party, "$qst_capture_conspirators_party_6"),
      ##           (else_try),
      ##             (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_6"),
      ##             (neq, ":ai_behavior", ai_bhvr_hold),
      ##             (party_set_ai_behavior, "$qst_capture_conspirators_party_6", ai_bhvr_hold),
      ##             (party_set_flags, "$qst_capture_conspirators_party_6", pf_default_behavior, 0),
      ##             (party_attach_to_party, "$qst_capture_conspirators_party_6", "$qst_capture_conspirators_party_1"),
      ##           (try_end),
      ##         (try_end),
      ##         (try_begin),
      ##           (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_6"),
      ##           (eq, ":ai_behavior", ai_bhvr_travel_to_point),
      ##           (party_get_ai_target_position, pos2, "$qst_capture_conspirators_party_6"),
      ##           (party_get_position, pos1, "$qst_capture_conspirators_party_6"),
      ##           (get_distance_between_positions, ":distance", pos2, pos1),
      ##           (lt, ":distance", 200),
      ##           (call_script, "script_get_closest_walled_center_of_faction", "$qst_capture_conspirators_party_6", ":faction_no"),#Can fail
      ##           (ge, reg0, 0),
      ##           (party_set_ai_object, "$qst_capture_conspirators_party_6", reg0),
      ##           (party_set_ai_behavior, "$qst_capture_conspirators_party_6", ai_bhvr_travel_to_party),
      ##           (party_set_flags, "$qst_capture_conspirators_party_6", pf_default_behavior, 0),
      ##         (try_end),
      ##       (try_end),
      ##       (try_begin),
      ##         (gt, "$qst_capture_conspirators_party_7", 0),
      ##         (party_is_active, "$qst_capture_conspirators_party_7"),
      ##         (val_add, ":num_active_parties", 1),
      ##         (try_begin),
      ##           (party_is_in_any_town, "$qst_capture_conspirators_party_7"),
      ##           (try_begin),
      ##             (neg|party_is_in_town, "$qst_capture_conspirators_party_7", "$qst_capture_conspirators_party_1"),
      ##             (remove_party, "$qst_capture_conspirators_party_7"),
      ##           (else_try),
      ##             (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_7"),
      ##             (neq, ":ai_behavior", ai_bhvr_hold),
      ##             (party_set_ai_behavior, "$qst_capture_conspirators_party_7", ai_bhvr_hold),
      ##             (party_set_flags, "$qst_capture_conspirators_party_7", pf_default_behavior, 0),
      ##             (party_attach_to_party, "$qst_capture_conspirators_party_7", "$qst_capture_conspirators_party_1"),
      ##           (try_end),
      ##         (try_end),
      ##         (try_begin),
      ##           (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_7"),
      ##           (eq, ":ai_behavior", ai_bhvr_travel_to_point),
      ##           (party_get_ai_target_position, pos2, "$qst_capture_conspirators_party_7"),
      ##           (party_get_position, pos1, "$qst_capture_conspirators_party_7"),
      ##           (get_distance_between_positions, ":distance", pos2, pos1),
      ##           (lt, ":distance", 200),
      ##           (call_script, "script_get_closest_walled_center_of_faction", "$qst_capture_conspirators_party_7", ":faction_no"),#Can fail
      ##           (ge, reg0, 0),
      ##           (party_set_ai_object, "$qst_capture_conspirators_party_7", reg0),
      ##           (party_set_ai_behavior, "$qst_capture_conspirators_party_7", ai_bhvr_travel_to_party),
      ##           (party_set_flags, "$qst_capture_conspirators_party_7", pf_default_behavior, 0),
      ##         (try_end),
      ##       (try_end),
      ##
      ##       (eq, ":num_active_parties", 0),
      ##       (party_count_prisoners_of_type, ":count_captured_conspirators", "p_main_party", "trp_conspirator"),
      ##       (party_count_prisoners_of_type, ":count_captured_conspirator_leaders", "p_main_party", "trp_conspirator_leader"),
      ##       (val_add, ":count_captured_conspirators", ":count_captured_conspirator_leaders"),
      ##       (try_begin),
      ##         (store_div, ":limit", "$qst_capture_conspirators_num_troops_to_capture", 2),
      ##         (gt, ":count_captured_conspirators", ":limit"),
      ##         (call_script, "script_succeed_quest", "qst_capture_conspirators"),
      ##       (else_try),
      ##         (call_script, "script_fail_quest", "qst_capture_conspirators"),
      ##       (try_end),
      ##    ],
      ##   []
      ##   ),
      # Follow Spy quest
      (0.5, 0.0, 0.0,
        [
          (check_quest_active, "qst_follow_spy"),
          (eq, "$qst_follow_spy_no_active_parties", 0),
          (quest_get_slot, ":quest_giver_center", "qst_follow_spy", slot_quest_giver_center),
          (quest_get_slot, ":quest_object_center", "qst_follow_spy", slot_quest_object_center),
          (assign, ":abort_meeting", 0),
          (try_begin),
            (this_or_next|ge, "$qst_follow_spy_run_away", 2),
            (this_or_next|neg|party_is_active, "$qst_follow_spy_spy_party"),
            (neg|party_is_active, "$qst_follow_spy_spy_partners_party"),
          (else_try),
            (eq, "$qst_follow_spy_meeting_state", 0),
            (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_follow_spy_spy_party"),
            (try_begin),
              (assign, ":min_distance", 3),
              (try_begin),
                (is_currently_night),
                (assign, ":min_distance", 1),
              (try_end),
              (le, ":cur_distance", ":min_distance"),
              (store_distance_to_party_from_party, ":player_distance_to_quest_giver_center", "p_main_party", ":quest_giver_center"),
              (gt, ":player_distance_to_quest_giver_center", 1),
              (val_add, "$qst_follow_spy_run_away", 1),
              (try_begin),
                (eq, "$qst_follow_spy_run_away", 2),
                (assign, ":abort_meeting", 1),
                (display_message, "str_qst_follow_spy_noticed_you"),
              (try_end),
            (else_try),
              (store_distance_to_party_from_party, ":cur_distance", "$qst_follow_spy_spy_partners_party", "$qst_follow_spy_spy_party"),
              (le, ":cur_distance", 1),
              (party_attach_to_party, "$qst_follow_spy_spy_party", "$qst_follow_spy_spy_partners_party"),
              (assign, "$qst_follow_spy_meeting_state", 1),
              (assign, "$qst_follow_spy_meeting_counter", 0),
            (try_end),
          (else_try),
            (eq, "$qst_follow_spy_meeting_state", 1),
            (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_follow_spy_spy_partners_party"),
            (try_begin),
              (le, ":cur_distance", 1),
              (party_detach, "$qst_follow_spy_spy_party"),
              (val_add, "$qst_follow_spy_run_away", 1),
              (try_begin),
                (eq, "$qst_follow_spy_run_away", 2),
                (assign, ":abort_meeting", 1),
                (display_message, "str_qst_follow_spy_noticed_you"),
              (try_end),
            (else_try),
              (val_add, "$qst_follow_spy_meeting_counter", 1),
              (gt, "$qst_follow_spy_meeting_counter", 4),
              (party_detach, "$qst_follow_spy_spy_party"),
              (assign, ":abort_meeting", 1),
              (assign, "$qst_follow_spy_meeting_state", 2),
            (try_end),
          (try_end),
          (try_begin),
            (eq, ":abort_meeting", 1),
            (party_set_ai_object, "$qst_follow_spy_spy_party", ":quest_giver_center"),
            
            (party_set_ai_object, "$qst_follow_spy_spy_partners_party", ":quest_object_center"),
            
            (party_set_ai_behavior, "$qst_follow_spy_spy_party", ai_bhvr_travel_to_party),
            (party_set_ai_behavior, "$qst_follow_spy_spy_partners_party", ai_bhvr_travel_to_party),
            (party_set_flags, "$qst_follow_spy_spy_party", pf_default_behavior, 0),
            (party_set_flags, "$qst_follow_spy_spy_partners_party", pf_default_behavior, 0),
          (try_end),
          (assign, ":num_active", 0),
          (try_begin),
            (party_is_active, "$qst_follow_spy_spy_party"),
            (val_add, ":num_active", 1),
            (party_is_in_town, "$qst_follow_spy_spy_party", ":quest_giver_center"),
            (remove_party, "$qst_follow_spy_spy_party"),
            (assign, "$qst_follow_spy_spy_back_in_town", 1),
            (val_sub, ":num_active", 1),
          (try_end),
          (try_begin),
            (party_is_active, "$qst_follow_spy_spy_partners_party"),
            (val_add, ":num_active", 1),
            (party_is_in_town, "$qst_follow_spy_spy_partners_party", ":quest_object_center"),
            (remove_party, "$qst_follow_spy_spy_partners_party"),
            (assign, "$qst_follow_spy_partner_back_in_town", 1),
            (val_sub, ":num_active", 1),
          (try_end),
          (try_begin),
            (eq, "$qst_follow_spy_partner_back_in_town",1),
            (eq, "$qst_follow_spy_spy_back_in_town",1),
            (call_script, "script_fail_quest", "qst_follow_spy"),
          (try_end),
          (try_begin),
            (eq, ":num_active", 0),
            (assign, "$qst_follow_spy_no_active_parties", 1),
            (party_count_prisoners_of_type, ":num_spies", "p_main_party", "trp_spy"),
            (party_count_prisoners_of_type, ":num_spy_partners", "p_main_party", "trp_spy_partner"),
            (gt, ":num_spies", 0),
            (gt, ":num_spy_partners", 0),
            (call_script, "script_succeed_quest", "qst_follow_spy"),
          (try_end),
        ],
        []
      ),
      ### Raiders quest
      ##  (0.95, 0.0, 0.2,
      ##   [
      ##       (check_quest_active, "qst_hunt_down_raiders"),
      ##       (neg|check_quest_succeeded, "qst_hunt_down_raiders"),
      ##       (neg|check_quest_failed, "qst_hunt_down_raiders"),
      ##    ],
      ##   [
      ##       (quest_get_slot, ":quest_target_party", "qst_hunt_down_raiders", slot_quest_target_party),
      ##       (party_set_ai_behavior, ":quest_target_party", ai_bhvr_hold),
      ##       (party_set_flags, ":quest_target_party", pf_default_behavior, 0),
      ##    ]
      ##   ),
      ##
      ##  (0.7, 0, 0.2,
      ##   [
      ##       (check_quest_active, "qst_hunt_down_raiders"),
      ##       (neg|check_quest_succeeded, "qst_hunt_down_raiders"),
      ##       (neg|check_quest_failed, "qst_hunt_down_raiders"),
      ##    ],
      ##   [
      ##       (quest_get_slot, ":quest_target_party", "qst_hunt_down_raiders", slot_quest_target_party),
      ##       (party_set_ai_behavior,":quest_target_party",ai_bhvr_travel_to_party),
      ##       (party_set_flags, ":quest_target_party", pf_default_behavior, 0),
      ##    ]
      ##   ),
      ##
      ##  (0.1, 0.0, 0.0,
      ##   [
      ##       (check_quest_active, "qst_hunt_down_raiders"),
      ##       (neg|check_quest_succeeded, "qst_hunt_down_raiders"),
      ##       (neg|check_quest_failed, "qst_hunt_down_raiders"),
      ##       (quest_get_slot, ":quest_target_party", "qst_hunt_down_raiders", slot_quest_target_party),
      ##       (neg|party_is_active, ":quest_target_party")
      ##    ],
      ##   [
      ##       (call_script, "script_succeed_quest", "qst_hunt_down_raiders"),
      ##    ]
      ##   ),
      ##
      ##  (1.3, 0, 0.0,
      ##   [
      ##       (check_quest_active, "qst_hunt_down_raiders"),
      ##       (neg|check_quest_succeeded, "qst_hunt_down_raiders"),
      ##       (neg|check_quest_failed, "qst_hunt_down_raiders"),
      ##       (quest_get_slot, ":quest_target_party", "qst_hunt_down_raiders", slot_quest_target_party),
      ##       (quest_get_slot, ":quest_target_center", "qst_hunt_down_raiders", slot_quest_target_center),
      ##       (party_is_in_town,":quest_target_party",":quest_target_center")
      ##    ],
      ##   [
      ##       (call_script, "script_fail_quest", "qst_hunt_down_raiders"),
      ##       (display_message, "str_raiders_reached_base"),
      ##       (quest_get_slot, ":quest_target_party", "qst_hunt_down_raiders", slot_quest_target_party),
      ##       (remove_party, ":quest_target_party"),
      ##    ]
      ##   ),
      
      ##### TODO: QUESTS COMMENT OUT END
      
      #########################################################################
      # Random MERCHANT quest triggers
      ####################################
      # Apply interest to merchants guild debt  1% per week
      (24.0 * 7, 0.0, 0.0,
        [],
        [
          (val_mul,"$debt_to_merchants_guild",101),
          (val_div,"$debt_to_merchants_guild",100)
        ]
      ),
      # Escort merchant caravan:
      (0.1, 0.0, 0.1, [(check_quest_active, "qst_escort_merchant_caravan"),
          (eq, "$escort_merchant_caravan_mode", 1)
        ],
        [(quest_get_slot, ":quest_target_party", "qst_escort_merchant_caravan", slot_quest_target_party),
          (try_begin),
            (party_is_active, ":quest_target_party"),
            (party_set_ai_behavior, ":quest_target_party", ai_bhvr_hold),
            (party_set_flags, ":quest_target_party", pf_default_behavior, 0),
          (try_end),
      ]),
      (0.1, 0.0, 0.1, [(check_quest_active, "qst_escort_merchant_caravan"),
          (eq, "$escort_merchant_caravan_mode", 0),
        ],
        [(quest_get_slot, ":quest_target_party", "qst_escort_merchant_caravan", slot_quest_target_party),
          (try_begin),
            (party_is_active, ":quest_target_party"),
            (party_set_ai_behavior, ":quest_target_party", ai_bhvr_escort_party),
            (party_set_flags, ":quest_target_party", pf_default_behavior, 0),
            (party_set_ai_object, ":quest_target_party", "p_main_party"),
          (try_end),
      ]),
      
      (0.1, 0, 0.0, [(check_quest_active, "qst_escort_merchant_caravan"),
          (quest_get_slot, ":quest_target_party", "qst_escort_merchant_caravan", slot_quest_target_party),
          (neg|party_is_active,":quest_target_party"),
        ],
        [(call_script, "script_abort_quest", "qst_escort_merchant_caravan", 2),
      ]),
      
      # Troublesome bandits
      (0.3, 0.0, 1.1, [(check_quest_active, "qst_troublesome_bandits"),
          (neg|check_quest_failed, "qst_troublesome_bandits"),
          (store_num_parties_destroyed, ":cur_eliminated", "pt_troublesome_bandits"),
          (lt, "$qst_troublesome_bandits_eliminated", ":cur_eliminated"),
          (store_num_parties_destroyed_by_player, ":cur_eliminated_by_player", "pt_troublesome_bandits"),
          (eq, ":cur_eliminated_by_player", "$qst_troublesome_bandits_eliminated_by_player"),
        ],
        [(display_message, "str_bandits_eliminated_by_another"),
          (call_script, "script_abort_quest", "qst_troublesome_bandits", 0),
      ]),
      
      (0.3, 0.0, 1.1, [(check_quest_active, "qst_troublesome_bandits"),
          (neg|check_quest_succeeded, "qst_troublesome_bandits"),
          (store_num_parties_destroyed, ":cur_eliminated", "pt_troublesome_bandits"),
          (lt, "$qst_troublesome_bandits_eliminated", ":cur_eliminated"),
          (store_num_parties_destroyed_by_player, ":cur_eliminated_by_player", "pt_troublesome_bandits"),
          (neq, ":cur_eliminated_by_player", "$qst_troublesome_bandits_eliminated_by_player"),
        ],
        [(call_script, "script_succeed_quest", "qst_troublesome_bandits"),]),
      
      # Kidnapped girl:
      (1, 0, 0,
        [(check_quest_active, "qst_kidnapped_girl"),
          (quest_get_slot, ":quest_target_party", "qst_kidnapped_girl", slot_quest_target_party),
          (party_is_active, ":quest_target_party"),
          (party_is_in_any_town, ":quest_target_party"),
          (remove_party, ":quest_target_party"),
        ],
        []
      ),
      
      
      #Rebellion changes begin
      #move
      
      (0, 0, 24 * 14,
        [
          (try_for_range, ":pretender", pretenders_begin, pretenders_end),
            (troop_set_slot, ":pretender", slot_troop_cur_center, 0),
            (neq, ":pretender", "$supported_pretender"),
            (troop_get_slot, ":target_faction", ":pretender", slot_troop_original_faction),
            (faction_slot_eq, ":target_faction", slot_faction_state, sfs_active),
            (faction_slot_eq, ":target_faction", slot_faction_has_rebellion_chance, 1),
            (neg|troop_slot_eq, ":pretender", slot_troop_occupation, slto_kingdom_hero),
            
            (try_for_range, ":unused", 0, 30),
              (troop_slot_eq, ":pretender", slot_troop_cur_center, 0),
              (store_random_in_range, ":town", towns_begin, towns_end),
              (store_faction_of_party, ":town_faction", ":town"),
              (store_relation, ":relation", ":town_faction", ":target_faction"),
              (le, ":relation", 0), #fail if nothing qualifies
              
              (troop_set_slot, ":pretender", slot_troop_cur_center, ":town"),
              (try_begin),
                (eq, "$cheat_mode", 1),
                (str_store_troop_name, 4, ":pretender"),
                (str_store_party_name, 5, ":town"),
                (display_message, "@{!}{s4} is in {s5}"),
              (try_end),
            (try_end),
            
            #        (try_for_range, ":rebel_faction", rebel_factions_begin, rebel_factions_end),
            #            (faction_get_slot, ":rebellion_status", ":rebel_faction", slot_faction_state),
            #            (eq, ":rebellion_status", sfs_inactive_rebellion),
            #            (faction_get_slot, ":pretender", ":rebel_faction", slot_faction_leader),
            #            (faction_get_slot, ":target_faction", ":rebel_faction", slot_faction_rebellion_target),#
            
            #            (store_random_in_range, ":town", towns_begin, towns_end),
            #            (store_faction_of_party, ":town_faction", ":town"),
            #            (store_relation, ":relation", ":town_faction", ":target_faction"),
            #            (le, ":relation", 0), #fail if nothing qualifies
            
            #           (faction_set_slot, ":rebel_faction", slot_faction_inactive_leader_location, ":town"),
          (try_end),
        ],
        []
      ),
      #Rebellion changes end
      
      #NPC system changes begin
      #Move unemployed NPCs around taverns
      (24 * 15 , 0, 0,
        [
          # (call_script, "script_update_companion_candidates_in_taverns"), move to simple trigger that does all this
        ],
        []
      ),
      
      #Process morale and determine personality clashes
      (24.5, 0, 0,
        [],
        [
          
          #Count NPCs in party and get the "grievance divisor", which determines how fast grievances go away
          #Set their relation to the player
          (assign, ":npcs_in_party", 0),
          (assign, ":grievance_divisor", 100),
          (try_for_range, ":npc1", companions_begin, companions_end),
            (main_party_has_troop, ":npc1"),
            (val_add, ":npcs_in_party", 1),
          (try_end),
          (val_sub, ":grievance_divisor", ":npcs_in_party"),
          (store_skill_level, ":persuasion_level", "skl_persuasion", "trp_player"),
          (val_add, ":grievance_divisor", ":persuasion_level"),
          (assign, reg7, ":grievance_divisor"),
          
          #        (display_message, "@{!}Process NPC changes. GD: {reg7}"),
          
          
          
          ##Activate personality clash from 24 hours ago
          (try_begin), #scheduled personality clashes require at least 24hrs together
            (gt, "$personality_clash_after_24_hrs", 0),
            (eq, "$disable_npc_complaints", 0),
            (try_begin),
              (troop_get_slot, ":other_npc", "$personality_clash_after_24_hrs", slot_troop_personalityclash_object),
              (main_party_has_troop, "$personality_clash_after_24_hrs"),
              (main_party_has_troop, ":other_npc"),
              (assign, "$npc_with_personality_clash", "$personality_clash_after_24_hrs"),
            (try_end),
            (assign, "$personality_clash_after_24_hrs", 0),
          (try_end),
          #
          
          (assign, "$npc_to_rejoin_party", 0),
          (try_for_range, ":npc", companions_begin, companions_end),
            ###Reset meeting variables
            (try_begin),
              (troop_slot_eq, ":npc", slot_troop_turned_down_twice, 1),
              (store_random_in_range, ":rand", 0, 100),
              (lt, ":rand", 40),
              (troop_set_slot, ":npc", slot_troop_turned_down_twice, 0),
            (try_end),
            (try_begin),
              (troop_slot_eq, ":npc", slot_troop_met, 1),
              (troop_set_slot, ":npc", slot_troop_met_previously, 1),
            (try_end),
            
            ###Check for coming out of retirement
            (troop_get_slot, ":occupation", ":npc", slot_troop_occupation),
            (try_begin),
              (eq, ":occupation", slto_retirement),
              (troop_get_slot, ":renown_min", ":npc", slot_troop_return_renown),
              (str_store_troop_name, s31, ":npc"),
              (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
              #               (assign, reg4, ":player_renown"),
              #               (assign, reg5, ":renown_min"),
              #                (display_message, "@{!}Test {s31}  for retirement return {reg4}, {reg5}."),
              
              (gt, ":player_renown", ":renown_min"),
              (store_random_in_range, ":rand", 0, 100),
              (lt, ":rand", 30),
              (troop_set_slot, ":npc", slot_troop_personalityclash_penalties, 0),
              (troop_set_slot, ":npc", slot_troop_morality_penalties, 0),
              (troop_set_slot, ":npc", slot_troop_occupation, 0),
            (try_end),
            
            
            #Check for political issues
            (try_begin), #does npc's opponent pipe up?
              (troop_slot_ge, ":npc", slot_troop_days_on_mission, 5),
              (troop_slot_eq, ":npc", slot_troop_current_mission, npc_mission_kingsupport),
              
              (troop_get_slot, ":other_npc", ":npc", slot_troop_kingsupport_opponent),
              (troop_slot_eq, ":other_npc", slot_troop_kingsupport_objection_state, 0),
              
              (troop_set_slot, ":other_npc", slot_troop_kingsupport_objection_state, 1),
              
              (str_store_troop_name, s3, ":npc"),
              (str_store_troop_name, s4, ":other_npc"),
              
              (try_begin),
                (eq, "$cheat_mode", 1),
                (display_message, "str_s4_ready_to_voice_objection_to_s3s_mission_if_in_party"),
              (try_end),
            (try_end),
            
            #Check for quitting
            (try_begin),
              (main_party_has_troop, ":npc"),
              
              (call_script, "script_npc_morale", ":npc"),
              (assign, ":npc_morale", reg0),
              
              (try_begin),
                (lt, ":npc_morale", 30),
                (store_random_in_range, ":random", 0, 50),
                (val_add, ":npc_morale", ":random"),
                (lt, ":npc_morale", 45),
                (assign, "$npc_is_quitting", ":npc"),
              (try_end),
              
              #Reduce grievance over time (or augment, if party is overcrowded
              (troop_get_slot, ":grievance", ":npc", slot_troop_personalityclash_penalties),
              (val_mul, ":grievance", 90),
              (val_div, ":grievance", ":grievance_divisor"),
              (troop_set_slot, ":npc", slot_troop_personalityclash_penalties, ":grievance"),
              
              (troop_get_slot, ":grievance", ":npc", slot_troop_morality_penalties),
              (val_mul, ":grievance", 90),
              (val_div, ":grievance", ":grievance_divisor"),
              (troop_set_slot, ":npc", slot_troop_morality_penalties, ":grievance"),
              
              
              #Change personality grievance levels
              (try_begin),
                (this_or_next|troop_slot_ge, ":npc", slot_troop_personalityclash_state, 1),
                (eq, "$disable_npc_complaints", 1),
                (troop_get_slot, ":object", ":npc", slot_troop_personalityclash_object),
                (main_party_has_troop, ":object"),
                (call_script, "script_reduce_companion_morale_for_clash", ":npc", ":object", slot_troop_personalityclash_state),
              (try_end),
              (try_begin),
                (this_or_next|troop_slot_ge, ":npc", slot_troop_personalityclash2_state, 1),
                (eq, "$disable_npc_complaints", 1),
                (troop_get_slot, ":object", ":npc", slot_troop_personalityclash2_object),
                (main_party_has_troop, ":object"),
                (call_script, "script_reduce_companion_morale_for_clash", ":npc", ":object", slot_troop_personalityclash2_state),
              (try_end),
              (try_begin),
                (this_or_next|troop_slot_ge, ":npc", slot_troop_personalitymatch_state, 1),
                (eq, "$disable_npc_complaints", 1),
                (troop_get_slot, ":object", ":npc", slot_troop_personalitymatch_object),
                (main_party_has_troop, ":object"),
                (troop_get_slot, ":grievance", ":npc", slot_troop_personalityclash_penalties),
                (val_mul, ":grievance", 9),
                (val_div, ":grievance", 10),
                (troop_set_slot, ":npc", slot_troop_personalityclash_penalties, ":grievance"),
              (try_end),
              
              
              
              #Check for new personality clashes
              
              #Active personality clash 1 if at least 24 hours have passed
              (try_begin),
                (eq, "$disable_npc_complaints", 0),
                (eq, "$npc_with_personality_clash", 0),
                (eq, "$npc_with_personality_clash_2", 0),
                (eq, "$personality_clash_after_24_hrs", 0),
                (troop_slot_eq, ":npc", slot_troop_personalityclash_state, 0),
                (troop_get_slot, ":other_npc", ":npc", slot_troop_personalityclash_object),
                (main_party_has_troop, ":other_npc"),
                (assign, "$personality_clash_after_24_hrs", ":npc"),
              (try_end),
              
              #Personality clash 2 and personality match is triggered by battles
              (try_begin),
                (eq, "$npc_with_political_grievance", 0),
                
                (troop_slot_eq, ":npc", slot_troop_kingsupport_objection_state, 1),
                (assign, "$npc_with_political_grievance", ":npc"),
              (try_end),
              
            #main party does not have troop
            (else_try),
              (eq, ":occupation", slto_player_companion),
              (neg|troop_slot_ge, ":npc", slot_troop_prisoner_of_party, 0),
              
              #mission obsolete (see companion_embassy_results)
              (troop_get_slot, ":mission_object", ":npc", slot_troop_mission_object),
              (try_begin),
                (troop_slot_eq, ":npc", slot_troop_current_mission, npc_mission_pledge_vassal), #only mission now without a "already done" section in companion_embassy_results
                (check_quest_active, "qst_join_faction"),
                (faction_get_slot, ":object_lord", ":mission_object", slot_faction_leader),
                (quest_slot_eq, "qst_join_faction", slot_quest_giver_troop, ":object_lord"),
                #we don't test actually joining the kingdom because script_player_join_kingdom will disable all missions
                (troop_set_slot, ":npc", slot_troop_current_mission, npc_mission_rejoin_when_possible),
                (troop_set_slot, ":npc", slot_troop_days_on_mission, 0),
              (try_end),
              
              (troop_get_slot, ":days_on_mission", ":npc", slot_troop_days_on_mission),
              (try_begin),
                (gt, ":days_on_mission", 0),
                (val_sub, ":days_on_mission", 1),
                (troop_set_slot, ":npc", slot_troop_days_on_mission, ":days_on_mission"),
              (else_try),
                (troop_slot_eq, ":npc", slot_troop_current_mission, npc_mission_rejoin_when_possible),
                (try_begin),
                  (eq, "$npc_to_rejoin_party", 0),  #don't override diplomatic missions
                  (hero_can_join, "p_main_party"),
                  (assign, "$npc_to_rejoin_party", ":npc"),
                (try_end),
              (else_try),
                (troop_slot_ge, ":npc", slot_troop_current_mission, 1),
                (assign, "$npc_to_rejoin_party", ":npc"),
              (try_end),
            (try_end),
          (try_end),
      ]),
      
      
      #NPC system changes end
      
      # Lady of the lake achievement
      (1, 0, 0,
        [
          (troop_get_type, ":is_female", "trp_player"),
          (val_mod, ":is_female", 2),
          (eq, ":is_female", 1),
          (try_for_range, ":companion", companions_begin, companions_end),
            (troop_slot_eq, ":companion", slot_troop_occupation, slto_player_companion),
            
            (troop_get_inventory_capacity, ":inv_cap", ":companion"),
            (try_for_range, ":i_slot", 0, ":inv_cap"),
              (troop_get_inventory_slot, ":item_id", ":companion", ":i_slot"),
              
              (ge, ":item_id", 0),
              
              (this_or_next|eq, ":item_id", "itm_old_swordv5"),
              # (this_or_next|eq, ":item_id", "itm_sword_two_handed_a"),
              (eq, ":item_id", "itm_old_swordv5"),
              
              (unlock_achievement, ACHIEVEMENT_LADY_OF_THE_LAKE),
              (assign, ":inv_cap", 0),
            (try_end),
          (try_end),
        ],
        []
      ),
      
      (2, 0, 0, [(neq, "$moralep_on", 0),(neq, "$g_empieza_asedio", 1),], [    #morale impact chief of resting/not resting by motomataru.
          #A little sleep is a lot different than NO sleep. After 90 hours of NO sleep, I think we can agree that most troops would be useless.
          #The original system checked if the player got at least TWO hours rest in a town/castle. If so, it reduced the penalty HALF. So you not only reduced penalty but reduced chances of recovery. Intervals longer than eight hours, of course, may miss the night altogether and effectively make this trigger a complete waste of resources.
          #On the penalty side, it only increased at night WHLE TRAVELING, so -4 per day MAX, and it doesn't even effect morale immediately (unlike recovery, which does). After 96 hours of doing NOTHING but marching and fighting, it is possible to have a penalty of -16. If a player is NEVER going to stop anywhere at night, he/she should just turn the option off.
          #I don't think this is excessive, so am returning it to the original, but give up to +4 per night for resting in the field, but personally I never camp when I play, because of lack of the security of a town
          (store_party_size_wo_prisoners, reg0, "p_main_party"),
          (try_begin),
            (lt, reg0, 2),
            (party_set_slot, "p_main_party", slot_party_unrested_morale_penalty, 0),
            
          (else_try),
            (is_currently_night),
            (try_begin),
              #  (this_or_next|eq, "$g_camp_mode", 1),#Camp rest?
              (eq, "$g_last_rest_center", "$current_town"),
              (assign, "$rest_up", 1),
              
            (else_try),
              (party_get_slot, reg0, "p_main_party", slot_party_unrested_morale_penalty),
              (neq, "$g_player_icon_state", pis_camping), #camp rest should add morale?
              # (neq, "$g_player_icon_state", pis_ship), in this game, generally not passengers
              (neq, "$g_player_besiege_town", "$g_encountered_party"),
              (neq, "$g_player_is_captive", 1),
              (neg|key_is_down, key_space),
              (val_add, reg0, 1),
              (party_set_slot, "p_main_party", slot_party_unrested_morale_penalty, reg0),
              
              #minor recovery from not marching or fighting
            (else_try),
              (val_sub, reg0, 1),
              (val_max, reg0, 0),
              (party_set_slot, "p_main_party", slot_party_unrested_morale_penalty, reg0),
            (try_end),
            
          (else_try),
            (neq, "$rest_up", 0),
            (party_get_slot, reg0, "p_main_party", slot_party_unrested_morale_penalty),
            (try_begin),
              (lt, reg0, 3),
              (party_set_slot, "p_main_party", slot_party_unrested_morale_penalty, 0),
            (else_try),
              (val_div, reg0, 2),
              (party_set_slot, "p_main_party", slot_party_unrested_morale_penalty, reg0),
            (try_end),
            (assign, ":add_morale", reg0),
            
            #add small bonus to current morale for "diversions" available in towns
            (try_begin),
              (ge, "$g_last_rest_center", 0),
              (this_or_next|party_slot_eq, "$g_last_rest_center", slot_party_type, spt_town),
              (this_or_next|party_slot_eq, "$g_last_rest_center", slot_party_type, spt_castle),
              (party_slot_eq, "$g_last_rest_center", slot_party_type, spt_village),
              (val_add, ":add_morale", 1),
            (try_end),
            
            (display_message, "@Your troops feel refreshed from the night's rest."),
            (call_script, "script_change_player_party_morale", ":add_morale"),
            (assign, "$rest_up", 0),
            
          (else_try),
            (store_time_of_day, reg0),
            (is_between, reg0, 6, 8),
            (party_get_slot, reg0, "p_main_party", slot_party_unrested_morale_penalty),
            
            (try_begin),
              (gt, reg0, 4),  #more than 1 night without rest?
              (lt, reg0, 6),  #more than 1 night without rest?
              (display_message, "@Your men need rest or their morale will suffer.", color_bad_news),
            (try_end),
            (try_begin),
              (ge, reg0, 10),  #more than 1 night without rest?
              (display_message, "@Your men need rest or their morale will suffer.", color_bad_news),
            (try_end),
          (try_end),
      ]),
      
      # mainquest wessex foragers
      (0.3, 0.0, 1.1, [
          (neq, "$campaign_type", camp_sandbox),
          (neq, "$campaign_type", camp_lordc),
          (neq, "$campaign_type", camp_kingc),
          (check_quest_active, "qst_wessex_foragers"),
          (neg|check_quest_succeeded, "qst_wessex_foragers"),
          (store_num_parties_destroyed, ":cur_eliminated", "pt_wessex_foragers"),
          (lt, "$qst_troublesome_bandits_eliminated", ":cur_eliminated"),
          ], [
          (call_script, "script_succeed_quest", "qst_wessex_foragers"),
          (call_script, "script_set_player_relation_with_faction", "fac_neutral", 0),
      ]),
      ###
      ###war and peace enter kingdoms in mainquest #################################### Mainquest Diplomacy forced
      (0, 0.0, 48, [ (neq, "$campaign_type", camp_sandbox),(neq, "$campaign_type", camp_lordc),(neq, "$campaign_type", camp_kingc),
          (this_or_next|check_quest_active,"qst_sven_traitor"),
          (check_quest_active,"qst_the_fleet"),
        ],
        [
          (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", "fac_kingdom_5", "fac_kingdom_8"),
          # -1 faction_1 has a casus belli against faction_2. 1, faction_1 has a truce with faction_2, -2, the two factions are at war
          (assign, ":war_peace_truce_status", reg0),
          (neq, ":war_peace_truce_status", -2),
          
          #mierce and wessex vs Northanhymbre
          (call_script, "script_diplomacy_start_war_between_kingdoms", "fac_kingdom_5", "fac_kingdom_8", logent_faction_declares_war_to_respond_to_provocation),	#MOTO chief pass log entries
          (call_script, "script_diplomacy_start_war_between_kingdoms", "fac_kingdom_7", "fac_kingdom_8", logent_faction_declares_war_to_respond_to_provocation),	#MOTO chief pass log entries
      ]),
      ###
      (0, 0.0, 1, [ (neq, "$campaign_type", camp_sandbox),(neq, "$campaign_type", camp_lordc),(neq, "$campaign_type", camp_kingc), #lords back
          (check_quest_active,"qst_sven_traitor"),
          (quest_slot_eq,"qst_sven_traitor",slot_quest_current_state, 4),
        ],
        [
          #wessex, mierce peace with Ragnar's son
          (try_begin), #lord move inaccesible map part
            (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", "fac_kingdom_5", "fac_kingdom_8"),
            # -1 faction_1 has a casus belli against faction_2. 1, faction_1 has a truce with faction_2, -2, the two factions are at war
            (assign, ":war_peace_truce_status", reg0),
            (eq, ":war_peace_truce_status", -2),
            (call_script, "script_diplomacy_start_peace_between_kingdoms", "fac_kingdom_5", "fac_kingdom_8", 1),
            (call_script, "script_diplomacy_start_peace_between_kingdoms", "fac_kingdom_7", "fac_kingdom_8", 1),
          (try_end),
      ]),
      
      ####
      (0, 0, 6, ###war and peace player's support faction and place kingdom faction mainquest
        [  (neq, "$campaign_type", camp_sandbox),(neq, "$campaign_type", camp_lordc),(neq, "$campaign_type", camp_kingc),
          (check_quest_active, "qst_welsh_and_pictish"),
          (quest_get_slot, ":quest_current_state", "qst_welsh_and_pictish", slot_quest_current_state),
          (eq, ":quest_current_state", 1),
        ],
        [
          (try_begin),
            (eq, "$player_side", 2), #danish
            (store_faction_of_party, ":old_faction", "p_castle_37"),
            (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", ":old_faction", "fac_kingdom_8"),
            # -1 faction_1 has a casus belli against faction_2. 1, faction_1 has a truce with faction_2, -2, the two factions are at war
            (assign, ":war_peace_truce_status", reg0),
            (neq, ":war_peace_truce_status", -2),
            #war!
            (neq, ":old_faction", "fac_kingdom_8"),
            (call_script, "script_diplomacy_start_war_between_kingdoms", ":old_faction", "fac_kingdom_8", 1),
          (else_try),
            (eq, "$player_side", 1), #wessex
            (store_faction_of_party, ":old_faction", "p_castle_41"),
            (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", ":old_faction", "fac_kingdom_5"),
            # -1 faction_1 has a casus belli against faction_2. 1, faction_1 has a truce with faction_2, -2, the two factions are at war
            (assign, ":war_peace_truce_status", reg0),
            (neq, ":war_peace_truce_status", -2),
            #war!
            (neq, ":old_faction", "fac_kingdom_5"),
            (call_script, "script_diplomacy_start_war_between_kingdoms", ":old_faction", "fac_kingdom_5", 1),
          (try_end),
      ]),
      
      (0, 0, 24, ###war in East Engla ragnars sons advance over this kingdom
        [ (neq, "$campaign_type", camp_sandbox),(neq, "$campaign_type", camp_lordc),(neq, "$campaign_type", camp_kingc),
          (this_or_next|check_quest_active,"qst_douar_an_enez"),
          (check_quest_active, "qst_welsh_and_pictish"),
          
        ],
        [
          (try_begin), ####war in East Engla ragnars sons advance over this kingdom
            (faction_slot_eq, "fac_kingdom_6", slot_faction_state, sfs_active),
            (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", "fac_kingdom_6", "fac_kingdom_8"),
            # -1 faction_1 has a casus belli against faction_2. 1, faction_1 has a truce with faction_2, -2, the two factions are at war
            (assign, ":war_peace_truce_status", reg0),
            (neq, ":war_peace_truce_status", -2),
            #danish invasion!!!
            (call_script, "script_diplomacy_start_war_between_kingdoms", "fac_kingdom_6", "fac_kingdom_8", 1),
          (try_end),
          
          (try_begin), #wessex and Mercia peace
            (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", "fac_kingdom_5", "fac_kingdom_7"),
            # -1 faction_1 has a casus belli against faction_2. 1, faction_1 has a truce with faction_2, -2, the two factions are at war
            (assign, ":war_peace_truce_status", reg0),
            (neq, ":war_peace_truce_status", 1),
            #wessex PAX!!!
            (call_script, "script_diplomacy_start_peace_between_kingdoms", "fac_kingdom_5", "fac_kingdom_7", 1),
          (try_end),
      ]),
      
      (0, 0, 6, ###war in wessex ragnars sons advance over this kingdom
        [          (neq, "$campaign_type", camp_sandbox),(neq, "$campaign_type", camp_lordc),(neq, "$campaign_type", camp_kingc),
          (check_quest_active,"qst_douar_an_enez"),
          (check_quest_succeeded, "qst_douar_an_enez"),
          ##       (quest_get_slot, ":quest_current_state", "qst_douar_an_enez", slot_quest_current_state),
          ##       (ge, ":quest_current_state", 10),
        ],
        [
          (try_begin),
            (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", "fac_kingdom_5", "fac_kingdom_8"),
            # -1 faction_1 has a casus belli against faction_2. 1, faction_1 has a truce with faction_2, -2, the two factions are at war
            (assign, ":war_peace_truce_status", reg0),
            (neq, ":war_peace_truce_status", -2),
            #wessex war!!!
            (call_script, "script_diplomacy_start_war_between_kingdoms", "fac_kingdom_5", "fac_kingdom_8", 1),
          (try_end),
          (try_begin),
            (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", "fac_kingdom_7", "fac_kingdom_8"),
            # -1 faction_1 has a casus belli against faction_2. 1, faction_1 has a truce with faction_2, -2, the two factions are at war
            (assign, ":war_peace_truce_status", reg0),
            (neq, ":war_peace_truce_status", -2),
            #Mierce war!!!
            (call_script, "script_diplomacy_start_war_between_kingdoms", "fac_kingdom_7", "fac_kingdom_8", 1),
          (try_end),
          (try_begin), #wessex and Mercia peace
            (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", "fac_kingdom_5", "fac_kingdom_7"),
            # -1 faction_1 has a casus belli against faction_2. 1, faction_1 has a truce with faction_2, -2, the two factions are at war
            (assign, ":war_peace_truce_status", reg0),
            (neq, ":war_peace_truce_status", 1),
            #wessex PAX!!!
            (call_script, "script_diplomacy_start_peace_between_kingdoms", "fac_kingdom_5", "fac_kingdom_7", 1),
          (try_end),
          ###Danelaw
          (try_for_range, ":center", "p_castle_17", "p_castle_21"),
            (store_faction_of_party, ":old_faction", ":center"),
            (neq, ":old_faction", "fac_kingdom_8"),
            (party_clear, ":center"),
            (party_add_members, ":center", "trp_norse_bowman", 42),
            (party_add_members, ":center", "trp_norse_level2_landed", 82),
            
            (call_script, "script_give_center_to_faction", ":center", "fac_kingdom_8"),
            (call_script, "script_give_center_to_lord", "p_town_17", "trp_knight_8_14", 0),
            (call_script, "script_give_center_to_lord", "p_town_18", "trp_knight_8_12", 0),
            (call_script, "script_give_center_to_lord", "p_town_19", "trp_knight_8_11", 0),
            (call_script, "script_give_center_to_lord", "p_town_20", "trp_knight_8_10", 0),
          (try_end),
          (try_begin),
            (store_faction_of_party, ":old_faction", "p_town_12"),
            (neq, ":old_faction", "fac_kingdom_8"),
            (party_clear, ":center"),
            (party_add_members, ":center", "trp_norse_bowman", 42),
            (party_add_members, ":center", "trp_norse_level2_landed", 82),
            (party_add_members, ":center", "trp_norse_level0_companion", 42),
            (call_script, "script_give_center_to_faction", "p_town_12", "fac_kingdom_8"),
            (call_script, "script_give_center_to_lord", "p_town_12", "trp_knight_8_15", 0),
          (try_end),
          
          ###moving vikings to lundenwic for wessex invasion
          
          (try_for_parties, ":party_no"),
            ##            (quest_get_slot, ":quest_current_state", "qst_douar_an_enez", slot_quest_current_state),
            ##             (le, ":quest_current_state", 15), #only before player get mission when he arriaves land.
            (party_slot_eq, ":party_no", slot_party_type, spt_kingdom_hero_party),
            (party_is_active, ":party_no"),
            (party_stack_get_troop_id, ":party_leader", ":party_no", 0),
            (troop_is_hero, ":party_leader"),
            #vikings lords
            (try_begin),
              (is_between, ":party_leader", "trp_knight_8_8", "trp_knight_8_15"),
              (party_relocate_near_party, ":party_no", "p_town_12", 4),
            (try_end),
            (try_begin),
              (eq, ":party_leader", "trp_knight_8_4"),
              (party_relocate_near_party, ":party_no", "p_town_12", 4),
            (try_end),
            (try_begin),
              (eq, ":party_leader", "trp_kingdom_8_lord"),
              (party_relocate_near_party, ":party_no", "p_town_12", 4),
            (try_end),
          (try_end),
          
          ###village looted for vikings
          (try_for_range, ":center", villages_begin, villages_end),
            (this_or_next|is_between, ":center", "p_village_13", "p_village_15"),
            (this_or_next|is_between, ":center", "p_village_112", "p_village_114"),
            (this_or_next|is_between, ":center", "p_village_120", "p_village_122"),
            (this_or_next|eq, ":center", "p_village_21"),
            (eq, ":center", "p_village_24"),
            (call_script, "script_village_set_state",  ":center", svs_looted),
          (try_end),
      ]),
      #### mainquest diplomacy forced end #####################
      #############
      ###forager camp system
      (0, 0, 24,  #give food each 24 hours
        [(map_free), #en mapa
          (party_get_current_terrain, ":cur_terrain", "p_main_party"),
          (neq,":cur_terrain",rt_water),
          (neq,":cur_terrain",rt_bridge),
          (neq,":cur_terrain",rt_river),
          (eq, "$g_player_is_captive", 0),
          (eq, "$foragers_a", 1), #foragers ok
        ],
        [
          (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
          (assign, ":num_men", 0),
          (try_for_range, ":i_stack", 0, ":num_stacks"),
            (party_stack_get_size, ":stack_size","p_main_party",":i_stack"),
            (val_add, ":num_men", ":stack_size"),
          (try_end),
          (try_begin),
            (lt, ":num_men", 40), # if men = or less than 40, no forager
            (assign, "$foragers_a", 0),
          (else_try),
            #(ge, ":num_men", 40), # if men = or less than 40, no forager
            (store_free_inventory_capacity, ":inv_cap_a", "trp_player"),
            (gt, ":inv_cap_a", 3), #player need space free in inventory
            
            (assign, ":num_food", 0),
            (troop_get_inventory_capacity, ":max_inv_slot", "trp_player"),
            (try_for_range, ":cur_inv_slot", 0, ":max_inv_slot"),
              (troop_get_inventory_slot, ":cur_item", "trp_player", ":cur_inv_slot"),
              (ge, ":cur_item", 0),
              (is_between, ":cur_item", food_begin, food_end),
              (val_add, ":num_food", 1), #player has food
            (try_end),
            (try_begin),
              (lt, ":num_food", 8), #system works when player have 8 or less food to advoid problems with villages to player if he has enough food
              #consequences = + food each 24 hours, possible problems with nearby villages -2 relation (30%)
              
              (store_random_in_range, ":random_chance", 0, 100), #differents options
              (try_begin),
                (ge, ":random_chance", 70), #success, food, no problems with villages
                (tutorial_box, "str_good_news_our_foragers_found_much_meat", "@Foragers"),
                (display_message, "str_good_news_our_foragers_found_much_meat", 0x00FF00),
                (troop_add_item, "trp_player","itm_cattle_meat",0),
                (try_begin),
                  (ge, ":num_men", 200), # huge army = more food
                  (troop_add_item, "trp_player","itm_cattle_meat",0),
                (try_end),
                (try_begin),
                  (ge, ":num_men", 400), # total army = more food
                  (troop_add_item, "trp_player","itm_cattle_meat",0),
                (try_end),
                (call_script, "script_change_player_party_morale", 2),
              (else_try),
                (ge, ":random_chance", 40), #success, food from villages
                (tutorial_box, "str_our_foragers_have_returned_after_getting_some_food", "@Foragers"),
                (display_message, "str_our_foragers_have_returned_after_getting_some_food", 0xFFFF00),
                (troop_add_item, "trp_player","itm_grain",0),
                (try_begin),
                  (ge, ":num_men", 200), # huge army = more food
                  (troop_add_item, "trp_player","itm_grain",0),
                (try_end),
                (try_begin),
                  (ge, ":num_men", 400), # total army = more food
                  (troop_add_item, "trp_player","itm_grain",0),
                (try_end),
                
                #reduce relacion con cada centro cercano chief
                (try_for_range, ":center", villages_begin, villages_end),
                  (store_distance_to_party_from_party, ":cur_distance", "p_main_party", ":center"),
                  (lt,":cur_distance",15),
                  (call_script, "script_change_player_relation_with_center", ":center", -2),
                (try_end),
                
              (else_try),
                (ge, ":random_chance", 10), #fail,  no food
                (tutorial_box, "str_bad_news_our_foragers_didnt_find_food_today", "@Foragers"),
                # (dialog_box,"@Bad news, our foragers don't found food today.")
                (display_message, "str_bad_news_our_foragers_didnt_find_food_today", 0xFF0000),
              (else_try),
                #disaster
                (tutorial_box, "str_very_bad_news_our_foragers_were_attacked", "@Foragers"),
                (display_message, "str_very_bad_news_our_foragers_were_attacked", 0xFF0000),
                (assign, "$foragers_a", 0), #no foragers until new orders
                (store_random_in_range, ":p_leave", 2, 5), #few number
                (assign, ":num_troops", ":p_leave"),
                (try_for_range, ":unused", 0, ":num_troops"),
                  (call_script, "script_cf_party_remove_random_regular_troop", "p_main_party"),
                (try_end),
              (try_end),
            (try_end),
          (try_end),
      ]),
      
      #######
      #######send scouts
      (0, 0, 25, #give vision permanent and/or they get dead send scouts
        [(map_free), #en mapa
          (party_get_current_terrain, ":cur_terrain", "p_main_party"),
          (neq,":cur_terrain",rt_water),
          (neq,":cur_terrain",rt_bridge),
          (neq,":cur_terrain",rt_river),
          (eq, "$g_player_is_captive", 0),
          (eq, "$send_scouts", 1), #scouts ok
        ],
        [
          (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
          (assign, ":num_men", 0),
          (try_for_range, ":i_stack", 0, ":num_stacks"),
            (party_stack_get_size, ":stack_size","p_main_party",":i_stack"),
            (val_add, ":num_men", ":stack_size"),
          (try_end),
          (try_begin),
            (lt, ":num_men", 30), # if men = or less than 30, no scouts
            (assign, "$send_scouts", 0),
          (else_try),
            # (ge, ":num_men", 30), #  30, ok Scouts is out in script_game_get_skill_modifier_for_troop
            
            (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
              (store_faction_of_party, ":center_faction", ":center_no"),
              (store_relation, ":cur_relation", "fac_player_faction", ":center_faction"),
              (lt, ":cur_relation", 0),
              (store_distance_to_party_from_party, ":dist", "p_main_party", ":center_no"),
              (try_begin),
                (lt, ":dist", 25), #25 km is good ratio for patrols
                (store_random_in_range, ":random_chance", 0, 100), #differents options
                (try_begin),
                  (ge, ":random_chance", 85), #15% to get advise, no common for no tired to player
                  (tutorial_box, "str_your_scouts_are_exploring_enemy_territory", "@Scouts"),
                  (display_message, "str_your_scouts_are_exploring_enemy_territory", 0x00FF00),
                (else_try),
                  (this_or_next|eq, "$g_player_icon_state", pis_ship),
                  (ge, ":random_chance", 40), #no problems no advises
                (else_try),
                  #disaster high chance
                  (tutorial_box, "str_very_bad_news_our_scouts_were_attacked", "@Scouts"),
                  (display_message, "str_very_bad_news_our_scouts_were_attacked", 0xFF0000),
                  (assign, "$send_scouts", 0), #no foragers until new orders
                  (store_random_in_range, ":p_leave", 2, 5), #few number
                  (assign, ":num_troops", ":p_leave"),
                  (try_for_range, ":unused", 0, ":num_troops"),
                    (call_script, "script_cf_party_remove_random_regular_troop", "p_main_party"),
                  (try_end),
                (try_end),
              (try_end),
            (try_end),
          (else_try),
            
          (try_end),
      ]),
      #######  ######### troops rebelion with low morale chief party rebelion
      (26, 0, 0, #each day 10% change to internal battle with rebels troops. A new leader want to rise. Really low ratio, but possible to happen.
        [(map_free), #en mapa
          (eq, "$g_infinite_camping", 0),
          (eq, "$g_player_is_captive", 0),
          
          (party_get_current_terrain, ":cur_terrain", "p_main_party"),
          (neq,":cur_terrain",rt_water),
          (neq,":cur_terrain",rt_bridge),
          (neq,":cur_terrain",rt_river),
          
          (party_get_morale, ":cur_morale", "p_main_party"),
          (lt, ":cur_morale", 36), #36 or less morale.
          
          (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
          (assign, ":num_men", 0),
          (try_for_range, ":i_stack", 0, ":num_stacks"),
            (party_stack_get_size, ":stack_size","p_main_party",":i_stack"),
            (val_add, ":num_men", ":stack_size"),
          (try_end),
          
          (call_script, "script_game_get_party_companion_limit"),
          (val_div, reg0, 2), #player can "manage" half the limit (see script_texto_partysize_morale)
          
          (ge, ":num_men", reg0),
        ],
        [
          (store_random_in_range, ":random_chance", 0, 100), #differents options
          (party_get_morale, ":cur_morale", "p_main_party"),
          (val_sub, ":random_chance", ":cur_morale"),
          (try_begin),
            (ge, ":random_chance", 40), #Duel!!! 10%
            (assign, "$choose_duel_troop", 0), #duel troops troops rebelion party rebelion
            (jump_to_menu, "mnu_duel_troop_rebelion"),
          (else_try),
            (ge, ":random_chance", 15), #advise
            (tutorial_box, "str_you_hear_rumors_of_discontent_among_your_men", "@Morale"),
            (display_message, "str_you_hear_rumors_of_discontent_among_your_men", 0xFF0000),
          (try_end),
      ]),
      #######
      ###Add-ons story
      (72, 0, ti_once, [(map_free,0),		(store_character_level, ":level", "trp_player"),
          (ge, ":level", 8),
          (troop_slot_ge, "trp_player", slot_troop_renown, 150),
          (eq, "$game_started_with_content_update", 1),
          
          (assign, ":continue", 0),
          (try_begin),
            (faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_active),
            (troop_get_slot, ":spouse", "trp_player", slot_troop_spouse),
            (this_or_next|faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
            (faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, ":spouse"), #
            
            (assign, ":continue", 1),
          (try_end),
          (try_begin),
            (party_slot_eq, "p_village_78", slot_town_lord,  "trp_player"),
            (assign, ":continue", 1),
          (try_end),
          (eq, ":continue", 0),
          
          
          ], [               (jump_to_menu, "mnu_addons_messenger"),
      ]),
      (72, 0, ti_once, [
          (check_quest_active, "qst_blank_quest_23"),
          (quest_slot_eq,"qst_blank_quest_23",slot_quest_current_state,4),
          ], [               (jump_to_menu, "mnu_addons_messenger_morriganlair"),
      ]),
      (12, 0, 0, [(this_or_next|check_quest_active, "qst_blank_quest_19"),
          (this_or_next|check_quest_active, "qst_blank_quest_20"),
          (this_or_next|check_quest_active, "qst_blank_quest_21"),
          (check_quest_active, "qst_blank_quest_22"),
          ], [
          (try_begin),
            (check_quest_active, "qst_blank_quest_19"),
            (party_slot_eq,"p_town_4",slot_town_lord, "trp_player"),
            (party_slot_eq,"p_town_5",slot_town_lord, "trp_player"),
            (party_slot_eq,"p_town_11",slot_town_lord, "trp_player"),
            (call_script, "script_succeed_quest", "qst_blank_quest_19"),
          (else_try),
            (check_quest_active, "qst_blank_quest_20"),
            (party_slot_eq,"p_town_13",slot_town_lord, "trp_player"),
            (party_slot_eq,"p_town_17",slot_town_lord, "trp_player"),
            (party_slot_eq,"p_town_9",slot_town_lord, "trp_player"),
            (call_script, "script_succeed_quest", "qst_blank_quest_20"),
          (else_try),
            (check_quest_active, "qst_blank_quest_21"),
            (party_slot_eq,"p_town_25",slot_town_lord, "trp_player"),
            (party_slot_eq,"p_town_28",slot_town_lord, "trp_player"),
            (party_slot_eq,"p_town_29",slot_town_lord, "trp_player"),
            (call_script, "script_succeed_quest", "qst_blank_quest_21"),
          (else_try),
            (check_quest_active, "qst_blank_quest_22"),
            (party_slot_eq,"p_town_12",slot_town_lord, "trp_player"),
            (party_slot_eq,"p_town_16",slot_town_lord, "trp_player"),
            (party_slot_eq,"p_town_10",slot_town_lord, "trp_player"),
            (call_script, "script_succeed_quest", "qst_blank_quest_22"),
          (try_end),
      ]),
      (24, 0, 0, [(eq, "$g_empieza_asedio", 1),], ####siege warfare, player lose money each day while siege. Sieges are expensive.
        [
          (store_troop_gold,":money","trp_player"),
          (try_begin),
            (ge,":money",100),
            (troop_remove_gold, "trp_player", 100),
            (display_message,"@Each day of the siege, you need to cover a number of expenses. You pay for rewards, digging latrines, cleaning stables, buying and bringing water and food, cooking, entertaining the troops...", 0xFF0000),
            (store_random_in_range,":chance",1,10),
            (try_begin),
              (le,":chance",4),
              (call_script, "script_change_player_party_morale", -1),
            (try_end),
          (else_try),
            (display_message,"@You do not have money to cover the basic expenses of a siege. This greatly undermines morale.", 0xFF0000),
            (call_script, "script_change_player_party_morale", -5),
          (try_end),
      ]),
      #messenger system chief
      (12, 0, 0, [ (eq,"$message_lord",1), #free lord.
          #  (eq,"$message_sent",1),
          (party_is_active, "p_main_party"), #esta activa?
        ],
        [
          (party_get_slot, ":time", "p_town_1", slot_party_messenger_time),
          (store_current_hours, ":cur_hours"),
          (store_random_in_range, ":random_time", 50, 96),
          (store_add, ":ok_time", ":time", ":random_time"),
          (try_begin),
            (gt, ":cur_hours", ":ok_time"),
            (store_random_in_range, ":luck", 1, 9),
            (try_begin),
              (gt, ":luck", 3),
              (jump_to_menu,"mnu_messenger_system_res"),
              (assign,"$message_sent",0), #message sent
            (else_try),
              (jump_to_menu,"mnu_messenger_system_res_failure"),
              (assign,"$message_sent",0), #message sent
            (try_end),
          (try_end),
      ]),
      (12, 0, 0, [ (neq,"$message_lord",1), #free lord.
          (eq,"$message_sent",1), #lord
          (party_is_active, "p_main_party"), #esta activa?
        ],
        [
          (try_begin),
            (assign,":party_no","$message_target"),
            (party_get_slot, ":time", "p_town_1", slot_party_messenger_time),
            (store_current_hours, ":cur_hours"),
            (store_add, ":ok_time", ":time", "$message_distance"),
            (gt, ":cur_hours", ":ok_time"),
            
            (try_begin),
              (party_is_active, ":party_no"), #esta activa?
              (jump_to_menu,"mnu_messenger_system"),
              (assign,"$message_sent",0), #message sent
            (else_try),
              (jump_to_menu,"mnu_messenger_system2"),
              (assign,"$message_sent",0), #message sent
            (try_end),
          (try_end),
      ]),
      ###
      (24 + 16, 6, ti_once,
        [
          (map_free,0),
          (neq, "$campaign_type", camp_storyline),
        ],
        [
          (start_presentation, "prsnt_game_concepts_tutorial"),
      ]),
      # Presentation SET A GOAL new game trigger
      (13, 6, ti_once,[
          (map_free,0),
          (neq, "$campaign_type", camp_storyline),
          (eq, "$set_goal_new_game_trigger", 0),
        ],
        [
          (assign, "$temp", 1),
          (assign, "$set_goal_new_game_trigger", 1),
          (jump_to_menu, "mnu_set_goal_trigger_new_game"),
      ]),
      # Presentantion SET A GOAL reward trigger
      (25, 0, 0, [
          (quest_get_slot, ":quest_type", "qst_vc_menu", slot_set_goal_type),
          (ge, ":quest_type", goal_custom),
        ],
        [
          (assign, "$temp", 1),
          (call_script, "script_set_goal_check_success_event"),
      ]),
      
      (60, 0, 0, [ (eq, "$campaign_type", camp_storyline),
          (neg|check_quest_active,"qst_douar_an_enez"),
          (neg|check_quest_active,"qst_aescesdun"),
          (neg|check_quest_active,"qst_svenbn_final"),
          #   (neg|check_quest_active,"qst_the_alliance"),
        ],
        [
          #kingdoms no dissapear
          #castles
          (try_for_range, ":center", "p_castle_1", "p_castle_9"),
            (store_faction_of_party, ":old_faction", ":center"),
            (neq, ":old_faction", "fac_kingdom_8"),
            (call_script, "script_give_center_to_faction", ":center", "fac_kingdom_8"),
            (call_script, "script_add_notification_menu", "mnu_notification_center_restoration", ":center", "fac_kingdom_8"),
          (try_end),
          (try_for_range, ":center", "p_castle_21", "p_castle_29"),
            (store_faction_of_party, ":old_faction", ":center"),
            (neq, ":old_faction", "fac_kingdom_5"),
            (call_script, "script_give_center_to_faction", ":center", "fac_kingdom_5"),
            (call_script, "script_add_notification_menu", "mnu_notification_center_restoration", ":center", "fac_kingdom_5"),
          (try_end),
          #town
          (try_begin),#saxons
            (store_faction_of_party, ":old_faction", "p_town_16"),
            (neq, ":old_faction", "fac_kingdom_5"),
            (call_script, "script_give_center_to_faction", "p_town_16", "fac_kingdom_5"),
            (call_script, "script_add_notification_menu", "mnu_notification_center_restoration", "p_town_16", "fac_kingdom_5"),
          (try_end),
          (try_begin),
            (store_faction_of_party, ":old_faction", "p_town_1"),
            (neq, ":old_faction", "fac_kingdom_5"),
            (call_script, "script_give_center_to_faction", "p_town_1", "fac_kingdom_5"),
            (call_script, "script_add_notification_menu", "mnu_notification_center_restoration", "p_town_1", "fac_kingdom_5"),
          (try_end),
          (try_begin),
            (store_faction_of_party, ":old_faction", "p_town_2"),
            (neq, ":old_faction", "fac_kingdom_5"),
            (call_script, "script_give_center_to_faction", "p_town_2", "fac_kingdom_5"),
            (call_script, "script_add_notification_menu", "mnu_notification_center_restoration", "p_town_2", "fac_kingdom_5"),
          (try_end),
          (try_begin),#danish
            (store_faction_of_party, ":old_faction", "p_town_27"),
            (neq, ":old_faction", "fac_kingdom_8"),
            (call_script, "script_give_center_to_faction", "p_town_27", "fac_kingdom_8"),
            (call_script, "script_add_notification_menu", "mnu_notification_center_restoration", "p_town_27", "fac_kingdom_8"),
          (try_end),
          (try_begin),
            (store_faction_of_party, ":old_faction", "p_town_10"),
            (neq, ":old_faction", "fac_kingdom_8"),
            (call_script, "script_give_center_to_faction", "p_town_10", "fac_kingdom_8"),
            (call_script, "script_add_notification_menu", "mnu_notification_center_restoration", "p_town_10", "fac_kingdom_8"),
          (try_end),
          (try_begin),
            (store_faction_of_party, ":old_faction", "p_town_3"),
            (neq, ":old_faction", "fac_kingdom_8"),
            (call_script, "script_give_center_to_faction", "p_town_3", "fac_kingdom_8"),
            (call_script, "script_add_notification_menu", "mnu_notification_center_restoration", "p_town_3", "fac_kingdom_8"),
          (try_end),
          (try_begin), #snothingaham quest
            (store_faction_of_party, ":old_faction", "p_castle_9"),
            (neq, ":old_faction", "fac_kingdom_7"),
            (call_script, "script_give_center_to_faction", "p_castle_9", "fac_kingdom_7"),
            (call_script, "script_add_notification_menu", "mnu_notification_center_restoration", "p_castle_9", "fac_kingdom_7"),
          (try_end),
          
          (try_begin), #castle conquest quest Din Bych
            (neg|check_quest_active,"qst_welsh_and_pictish"),
            (store_faction_of_party, ":old_faction", "p_castle_41"),
            (neq, ":old_faction", "fac_kingdom_9"),
            (call_script, "script_give_center_to_faction", "p_castle_41", "fac_kingdom_9"),
            (call_script, "script_add_notification_menu", "mnu_notification_center_restoration", "p_castle_41", "fac_kingdom_9"),
          (try_end),
          (try_begin), #castle conquest quest Dun Taruo
            (neg|check_quest_active,"qst_welsh_and_pictish"),
            (store_faction_of_party, ":old_faction", "p_castle_37"),
            (neq, ":old_faction", "fac_kingdom_20"),
            (call_script, "script_give_center_to_faction", "p_castle_37", "fac_kingdom_20"),
            (call_script, "script_add_notification_menu", "mnu_notification_center_restoration", "p_castle_37", "fac_kingdom_20"),
          (try_end),
      ]),
      # Logger for open-beta RE
      (24*7, 0, 0,
        [
          (lt, vc_version, 1100),
        ],
        [
          (set_show_messages, 0),
          (try_begin),
            # logger for bandits
            (try_begin),
              (str_clear, s31),
              (str_clear, s32),
              (str_clear, s40),
              
              (store_current_day, ":day"),
              (assign, reg0, ":day"),
              
              (str_store_string, s40, "@{!};Date:{reg0},"),
              
              (try_for_range, ":i", 0, 30),
                (troop_set_slot, "trp_temp_array_a", ":i", -1),
                (troop_set_slot, "trp_temp_array_b", ":i", 0),
                (troop_set_slot, "trp_temp_array_c", ":i", 0),
              (try_end),
              
              (troop_set_slot, "trp_temp_array_a", 0, "p_town_1"),
              (troop_set_slot, "trp_temp_array_a", 1, "p_village_54"),
              (troop_set_slot, "trp_temp_array_a", 2, "p_village_55"),
              (troop_set_slot, "trp_temp_array_a", 3, "p_village_101"),
              (troop_set_slot, "trp_temp_array_a", 4, "p_denmark_priest_spawn_point"),
              (troop_set_slot, "trp_temp_array_a", 5, "p_village_51"),
              (troop_set_slot, "trp_temp_array_a", 6, "p_town_11"),
              (troop_set_slot, "trp_temp_array_a", 7, "p_town_28"),
              (troop_set_slot, "trp_temp_array_a", 8, "p_town_24"),
              (troop_set_slot, "trp_temp_array_a", 9, "p_town_25"),
              (troop_set_slot, "trp_temp_array_a", 10, "p_village_68"),
              (troop_set_slot, "trp_temp_array_a", 11, "p_castle_70"),
              (troop_set_slot, "trp_temp_array_a", 12, "p_town_21"),
              (troop_set_slot, "trp_temp_array_a", 13, "p_castle_58"),
              (troop_set_slot, "trp_temp_array_a", 14, "p_town_15"),
              (troop_set_slot, "trp_temp_array_a", 15, "p_town_10"),
              (troop_set_slot, "trp_temp_array_a", 16, "p_town_27"),
              (troop_set_slot, "trp_temp_array_a", 17, "p_town_3"),
              (troop_set_slot, "trp_temp_array_a", 18, "p_castle_32"),
              (troop_set_slot, "trp_temp_array_a", 19, "p_village_11"),
              (troop_set_slot, "trp_temp_array_a", 20, "p_town_23"),
              (troop_set_slot, "trp_temp_array_a", 21, "p_castle_18"),
              (troop_set_slot, "trp_temp_array_a", 22, "p_town_22"),
              (troop_set_slot, "trp_temp_array_a", 23, "p_town_13"),
              (troop_set_slot, "trp_temp_array_a", 24, "p_village_41"),
              (troop_set_slot, "trp_temp_array_a", 25, "p_town_26"),
              (troop_set_slot, "trp_temp_array_a", 26, "p_town_17"),
              (troop_set_slot, "trp_temp_array_a", 27, "p_town_2"),
              (troop_set_slot, "trp_temp_array_a", 28, "p_town_16"),
              
              (try_begin),
                (try_for_parties, ":spawned_party"),
                  (neq, ":spawned_party", -1),
                  (party_is_active, ":spawned_party"),
                  (party_get_template_id, ":party_template_id", ":spawned_party"),
                  (is_between, ":party_template_id", "pt_looters", "pt_merchant_caravan"),
                  #(party_get_num_companions, ":size", ":spawned_party"),
                  (str_store_party_name, s1, ":spawned_party"),
                  #(party_get_num_prisoners, ":size_prisoners", ":spawned_party"),
                  
                  (assign, ":min_distance", 99999),
                  (assign, reg0, -1),
                  (assign, ":num_centers", 29),
                  
                  (try_for_range, ":i", 0, ":num_centers"),
                    (troop_get_slot, ":center_no", "trp_temp_array_a", ":i"),
                    (store_distance_to_party_from_party, ":party_distance", ":spawned_party", ":center_no"),
                    (lt, ":party_distance", ":min_distance"),
                    (assign, ":min_distance", ":party_distance"),
                    (assign, reg0, ":center_no"),
                    (assign, reg1, ":party_distance"),
                  (try_end),
                  
                  (try_begin),
                    # others centers if more than 35km
                    (gt, reg1, 35),
                    (troop_get_slot, ":count", "trp_temp_array_b", 29),
                    (val_add, ":count", 1),
                    (troop_set_slot, "trp_temp_array_b", 29, ":count"),
                    (assign, reg0, -1),
                    
                  (else_try),
                    (try_for_range, ":i", 0, ":num_centers"),
                      (troop_get_slot, ":center_no", "trp_temp_array_a", ":i"),
                      (eq, ":center_no", reg0),
                      (troop_get_slot, ":count", "trp_temp_array_b", ":i"),
                      (val_add, ":count", 1),
                      (troop_set_slot, "trp_temp_array_b", ":i", ":count"),
                      (assign, ":num_centers", -1),
                    (try_end),
                  (try_end),
                (try_end),
              (try_end),
              
              (str_clear, s31),
              (try_begin),
                (try_for_range, ":i", 0, 29),
                  (troop_get_slot, ":center", "trp_temp_array_a", ":i"),
                  (troop_get_slot, ":count", "trp_temp_array_b", ":i"),
                  (str_store_party_name, s1, ":center"),
                  (assign, reg1, ":center"),
                  (assign, reg0, ":count"),
                  (str_store_string, s31, "@{!}{s31}/{reg1},{reg0}"),
                (try_end),
                (troop_get_slot, ":count", "trp_temp_array_b", 29),
                (assign, reg0, ":count"),
                (str_store_string, s31, "@{!}{s31}/Others,{reg0}"),
              (try_end),
              (str_store_string, s40, "@{!}{s40}{s31};/"),
              (str_clear, s31),
            (try_end),
            
            (try_begin),
              # weekly report on bandits parties
              (str_store_string, s31, "@{!}Templates:"),
              
              (try_for_range, ":party_template_id", "pt_looters", "pt_merchant_caravan"),
                (store_num_parties_of_template, ":num_parties", ":party_template_id"),
                (store_num_parties_created, ":created", ":party_template_id"),
                (store_num_parties_destroyed, ":destroyed", ":party_template_id"),
                
                (assign, reg0, ":party_template_id"),
                (assign, reg1, ":num_parties"),
                (assign, reg2, ":created"),
                (assign, reg3, ":destroyed"),
                
                (str_store_string, s31, "@{!}{s31}/{reg0},{reg1},{reg2},{reg3}"),
              (try_end),
            (try_end),
            (str_store_string, s40, "@{!}{s40}{s31};/"),
            (str_clear, s31),
            
            (str_store_troop_name_plural, s31, "trp_pseudo_troop_03"),
            (str_store_string, s40, "@{!}{s31}{s40}"),
            (troop_set_plural_name, "trp_pseudo_troop_03", s40),
            (str_clear, s40),
            (str_clear, s31),
          (try_end),
          
          (try_begin),
            # logs player army sizes every day
            (str_clear, s40),
            (str_clear, s31),
            (store_current_day, reg0),
            
            (str_store_string, s40, "@{!}Date:{reg0},"),
            (assign, reg0, 0),
            (assign, reg1, 0),
            (assign, reg2, 0),
            (assign, reg3, 0),
            (assign, reg4, 0),
            (assign, reg5, 0),
            (assign, reg6, 0),
            (assign, reg7, 0),
            (assign, reg8, 0),
            (assign, reg0, 0),
            
            (party_get_num_companions, reg9, "p_main_party"),
            (party_get_num_companion_stacks, ":stacks", "p_main_party"),
            (try_for_range, ":i_stack", 0, ":stacks"),
              (party_stack_get_size, ":stack_size","p_main_party",":i_stack"),
              (party_stack_get_troop_id, ":stack_troop","p_main_party",":i_stack"),
              (neg|troop_is_hero, ":stack_troop"),
              (store_character_level, ":troop_level", ":stack_troop"),
              (val_add, reg6, ":stack_size"),
              
              (try_begin),
                (lt, ":troop_level", 18),
                (val_add, reg1, ":stack_size"),
                (val_add, reg7, ":stack_size"),
              (else_try),
                (lt, ":troop_level", 23),
                (val_add, reg2, ":stack_size"),
                (val_add, reg7, ":stack_size"),
              (else_try),
                (lt, ":troop_level", 26),
                (val_add, reg3, ":stack_size"),
                (val_add, reg7, ":stack_size"),
              (else_try),
                (lt, ":troop_level", 29),
                (val_add, reg4, ":stack_size"),
                (val_add, reg8, ":stack_size"),
              (else_try),
                (val_add, reg5, ":stack_size"),
                (val_add, reg8, ":stack_size"),
              (try_end),
            (try_end),
            
            (try_begin), #light troops
              (gt, reg7, 0),
              (gt, reg6, 0),
              (val_mul, reg7, 100),
              (val_div, reg7, reg6),
            (try_end),
            
            (try_begin), #heavy troops
              (gt, reg8, 0),
              (gt, reg6, 0),
              (val_mul, reg8, 100),
              (val_div, reg8, reg6),
            (try_end),
            
            (party_get_slot, reg0, "p_main_party", slot_party_cached_strength),
            
            (str_store_string, s40, "@{!}{s40}{reg9},{reg7},{reg8},{reg1},{reg2},{reg3},{reg4},{reg5},{reg0}"),
            (str_store_troop_name_plural, s31, "trp_pseudo_troop_02"),
            (str_store_string, s40, "@{!}{s31}^{s40}"),
            (troop_set_plural_name, "trp_pseudo_troop_02", s40),
            (str_clear, s40),
            (str_clear, s31),
          (try_end),
          (set_show_messages, 1),
      ]),
      (0, 0, 0,
        [
          (key_clicked, key_x),
          (key_is_down, key_left_control),
          # (call_script, "script_change_troop_renown", "trp_player", 900),
          # (try_for_range, ":unused", 0, 4),
          # (call_script, "script_cf_reinforce_party", "p_main_party"),
          # (try_end),
          (ge, "$vc_debug_mode", 1),
        ],
        [
          # (assign, ":delta", 0),
          # (assign, ":passes", 0),
          # (try_for_range, ":unused", 0, 100),
          # (assign, ":beg_count", 0),
          # (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
          # (try_for_range, ":i_stack", 0, ":num_stacks"),
          # (party_stack_get_troop_id, ":stack_troop","p_main_party", ":i_stack"),
          # (try_begin),
          # (neg|troop_is_hero, ":stack_troop"),
          # (party_stack_get_size, ":stack_size","p_main_party",":i_stack"),
          # (party_stack_get_num_wounded, ":num_wounded","p_main_party",":i_stack"),
          # (val_sub, ":stack_size", ":num_wounded"),
          # (else_try),
          # (troop_is_wounded, ":stack_troop"), #hero  wounded
          # (assign, ":stack_size", 0),
          # (else_try),
          # (assign, ":stack_size", 1),
          # (try_end),
          
          # (val_add, ":beg_count", ":stack_size"),
          # (try_end),
          
          # (gt, ":beg_count", 10),
          # (assign, ":end_count", 0),
          # (call_script, "script_inflict_casualties_to_party", "p_main_party", 10),
          
          # (party_get_num_companion_stacks, ":num_stacks", "p_temp_casualties"),
          # (try_for_range, ":i_stack", 0, ":num_stacks"),
          # (party_stack_get_size, ":stack_size", "p_temp_casualties", ":i_stack"),
          # (val_add, ":end_count", ":stack_size"),
          # (try_end),
          
          # (store_mul, reg1, ":end_count", 100),
          # (val_div, reg1, ":beg_count"),
          # (store_sub, reg4, reg1, 10),
          # (val_add, ":delta", reg4),
          # (val_add, ":passes", 1),
          # (assign, reg2, ":beg_count"),
          # (assign, reg3, ":end_count"),
          # (display_message, "@casualties {reg3} of {reg2}, {reg1}%"),
          # (try_end),
          
          # (store_mul, reg1, ":delta", 100),
          # (val_div, reg1, ":passes"),
          # (display_message, "@delta {reg1}% from 10% casualties"),
          
          
          (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
            (party_get_slot, ":prosperity_money", ":center_no", slot_town_prosperity),
            (store_mod, ":switch", ":center_no", 2),
            (try_begin),
              (eq, ":switch", 1),
              (store_mul, ":prosperity_impact", ":prosperity_money", 8),
              (val_div, ":prosperity_impact", 10),
              (val_sub, ":prosperity_impact", ":prosperity_money"),
            (else_try),
              (store_mul, ":prosperity_impact", ":prosperity_money", 5),
              (val_div, ":prosperity_impact", 10),
              (val_sub, ":prosperity_impact", ":prosperity_money"),
            (end_try),
            (call_script, "script_change_center_prosperity", ":center_no", ":prosperity_impact"),
            (call_script, "script_center_get_food_store_limit", ":center_no"),
            (val_div, reg0, 3),
            (party_set_slot, ":center_no", slot_party_food_store, reg0),
          (try_end),
          
          (call_script, "script_center_data_logger"),
      ]),
      (0, 0, ti_once,
        [
          (map_free,0),
        ],
        [
          (try_begin),
            (store_current_day, reg1),
            (le, reg1, 1),
            (assign, "$g_presentations_next_presentation", "prsnt_start_sandbox"),
            (jump_to_menu, "mnu_auto_start_presentation"),
          (end_try),
      ]),
      
      (24, 0, 0,
        [
          (ge, "$vc_debug_mode", 1),
        ],
        [
          (call_script, "script_center_data_logger"),
      ]),
      
    ]
