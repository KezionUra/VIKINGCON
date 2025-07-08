from header_common import *
from header_operations import *
from module_constants import *
from header_parties import *
from header_skills import *
from header_mission_templates import *
from header_items import *
from header_triggers import *
from header_terrain_types import *
from header_music import *
from header_map_icons import *
from header_presentations import *
from ID_animations import *


####################################################################################################################
# scripts is a list of script records.
# Each script record contns the following two fields:
# 1) Script id: The prefix "script_" will be inserted when referencing scripts.
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference.
####################################################################################################################


multi_scripts = [
  ("reset_player_globals", [
      (try_begin),
        (neq,"$is_berserk",0),
        (assign,"$is_berserk",0),
        (mission_cam_animate_to_screen_color, 0x00000000, 1000),
      (try_end),
      (assign,"$berserk_cooldown",0),
      (assign, "$player_ship_number", -1),
      (assign, "$player_ship_captain", -1),
  ]),
  ("reset_server_globals", [
      (assign,"$g_multiplayer_team_0_flagbearers_spawned",0),
      (assign,"$g_multiplayer_team_0_priests_spawned",0),
      (assign,"$g_multiplayer_team_1_flagbearers_spawned",0),
      (assign,"$g_multiplayer_team_1_priests_spawned",0),
      (assign,"$g_multiplayer_poll_cooldown_counter", 0),
  ]),
  ("multi_set_scene_slots", [
      (assign,"$g_multiplayer_deadly_bow",0),
      
      (assign, "$g_multiplayer_invasion_difficulty", 100),
      (assign, "$g_multiplayer_invasion_per_player_wave", 100),
      (assign, "$g_multiplayer_invasion_hardcore",0),
      (assign, "$g_multiplayer_invasion_respawn_rounds",3),
      (assign, "$g_multiplayer_invasion_round_delay",25),
      (assign, "$g_multiplayer_invasion_supply_round_delay",45),
      
      
      (scene_set_slot, "scn_multi_scene_1", slot_scene_sounds, sounds_village),
      (scene_set_slot, "scn_multi_scene_2", slot_scene_sounds, sounds_village),
      (scene_set_slot, "scn_multi_scene_3", slot_scene_sounds, sounds_village),
      (scene_set_slot, "scn_multi_scene_4", slot_scene_sounds, sounds_plain),
      (scene_set_slot, "scn_multi_scene_5", slot_scene_sounds, sounds_village),
      (scene_set_slot, "scn_multi_scene_6", slot_scene_sounds, sounds_village),
      (scene_set_slot, "scn_multi_scene_7", slot_scene_sounds, sounds_village),
      (scene_set_slot, "scn_multi_scene_8", slot_scene_sounds, sounds_village),
      (scene_set_slot, "scn_multi_scene_9", slot_scene_sounds, sounds_village),
      (scene_set_slot, "scn_multi_scene_10", slot_scene_sounds, sounds_village),
      (scene_set_slot, "scn_multi_scene_11", slot_scene_sounds, sounds_forest),
      (scene_set_slot, "scn_multi_scene_12", slot_scene_sounds, sounds_village),
      (scene_set_slot, "scn_multi_scene_13", slot_scene_sounds, sounds_village),
      (scene_set_slot, "scn_multi_scene_14", slot_scene_sounds, sounds_village),
      (scene_set_slot, "scn_multi_scene_15", slot_scene_sounds, sounds_village),
      (scene_set_slot, "scn_multi_scene_16", slot_scene_sounds, sounds_village),
      (scene_set_slot, "scn_multi_scene_17", slot_scene_sounds, sounds_village),
      (scene_set_slot, "scn_multi_scene_18", slot_scene_sounds, sounds_forest),
      (scene_set_slot, "scn_multi_scene_19", slot_scene_sounds, sounds_village),
      
      (scene_set_slot, "scn_multi_scene_inv_1", slot_scene_sounds, sounds_plain),
      (scene_set_slot, "scn_multi_scene_inv_2", slot_scene_sounds, sounds_village),
      (scene_set_slot, "scn_multi_scene_inv_3", slot_scene_sounds, sounds_village),
      (scene_set_slot, "scn_multi_scene_inv_4", slot_scene_sounds, sounds_village),
      (scene_set_slot, "scn_multi_scene_inv_5", slot_scene_sounds, sounds_village),
      
      (scene_set_slot, "scn_random_multi_plain", slot_scene_sounds, sounds_plain),
      (scene_set_slot, "scn_random_multi_forest", slot_scene_sounds, sounds_forest),
      (scene_set_slot, "scn_multi_sea_1", slot_scene_sounds, sounds_sea),
      (scene_set_slot, "scn_multi_sea_2", slot_scene_sounds, sounds_sea),
      (scene_set_slot, "scn_multi_coast_1", slot_scene_sounds, sounds_coast),
      (scene_set_slot, "scn_multi_coast_2", slot_scene_sounds, sounds_coast),
      
      (scene_set_slot, "scn_multi_scene_coast", slot_scene_sounds, sounds_sea),
      (scene_set_slot, "scn_multi_scene_fjord", slot_scene_sounds, sounds_sea),
      (scene_set_slot, "scn_multi_scene_islands", slot_scene_sounds, sounds_sea),
      
      #custom weather
      (scene_set_slot, "scn_multi_scene_inv_1", slot_scene_weather, weather_foggy),
      (scene_set_slot, "scn_multi_scene_inv_2", slot_scene_weather, weather_clear),
      (scene_set_slot, "scn_multi_scene_inv_3", slot_scene_weather, weather_rainy),
      (scene_set_slot, "scn_multi_scene_inv_4", slot_scene_weather, weather_thunderstorm),
      (scene_set_slot, "scn_multi_scene_inv_5", slot_scene_weather, weather_cloudy),
      #sea
      (scene_set_slot, "scn_multi_sea_2", slot_scene_weather, weather_thunderstorm),
      (scene_set_slot, "scn_multi_coast_2", slot_scene_weather, weather_seastorm),
      
      #custom time
      (scene_set_slot, "scn_multi_scene_inv_1", slot_scene_time, time_dawn),
      (scene_set_slot, "scn_multi_scene_inv_2", slot_scene_time, time_night),
      (scene_set_slot, "scn_multi_scene_inv_3", slot_scene_time, time_noon),
      (scene_set_slot, "scn_multi_scene_inv_4", slot_scene_time, time_noon),
      (scene_set_slot, "scn_multi_scene_inv_5", slot_scene_time, time_dusk),
      # (scene_set_slot, "scn_multi_scene_1", slot_scene_time, time_dusk),
      # (scene_set_slot, "scn_multi_scene_2", slot_scene_time, time_dawn),
      # (scene_set_slot, "scn_multi_scene_3", slot_scene_time, time_night),
  ]),
  ("scene_init_weather_and_sounds", [
      (store_current_scene,":scene"),
      
      ##SET TIME
      (try_for_prop_instances,":instance","spr_z_code_time_and_weather",somt_object),
        (call_script,"script_z_code_time_and_weather",":instance"),
      (try_end),
      (try_begin),
        (scene_slot_eq,":scene", slot_scene_time, time_dawn),
        (assign,":hour",5),
      (else_try),
        (scene_slot_eq,":scene", slot_scene_time, time_dusk),
        (assign,":hour",19),
      (else_try),
        (scene_slot_eq,":scene", slot_scene_time, time_night),
        (assign,":hour",1),
      (else_try),
        (assign,":hour",15),
      (try_end),
      (scene_set_day_time,":hour"),
      
      ##SET SEASON
      (assign,"$shader_season",-1),
      (try_for_prop_instances,":instance","spr_z_code_season",somt_object),
        (call_script,"script_z_code_season",":instance"),
      (try_end),
      (try_begin),
        (eq,"$shader_season",-1),
        (assign,"$shader_season",shader_summer),
      (try_end),
      (set_fixed_point_multiplier,1),
      (set_shader_param_float,"@vSeason","$shader_season"),
      
      ##SET SOUNDS
      (try_for_prop_instances,":instance","spr_z_code_scene_sounds",somt_object),
        (call_script,"script_z_code_scene_sounds",":instance"),
      (try_end),
      
      ###weather
      (try_begin),
        (scene_slot_ge,":scene", slot_scene_weather, weather_thunderstorm),#thunderstorm
        (assign,"$lightning_cycle",0),
        (try_begin),
          (multiplayer_is_server),
          (store_random_in_range,"$wind_strenght",80,120),
          (val_min,"$wind_strenght",100),
          (assign,"$WindStrength_variable",3),
          #phaiak begin
          (store_random_in_range, "$beaufort", 5, 9),	#global wind-strenght-value (0-12)
          (call_script, "script_get_wave_properties"),	#sets random values depending on $beaufort
          (assign, "$Amplitude_x",	reg1),
          (assign, "$Amplitude_y",	reg2),
          (assign, "$lamda_x",		reg3),
          (assign, "$lamda_y",		reg4),
          (assign, "$wavespeed_y", 	reg6),
          (assign, "$target_Amplitude_x",	"$Amplitude_x"),
          (assign, "$target_Amplitude_y",	"$Amplitude_y"),
          #phaiak end
          # (store_random_in_range,"$wavespeed_y",35,55),
          # (store_random_in_range,"$Amplitude_x",8000,20000),
          # (store_random_in_range,"$Amplitude_y",7000,18000),
          # (store_div,"$lamda_x","$Amplitude_y",100),
          # (store_div,"$lamda_y","$Amplitude_x",100),
        (try_end),
        (try_begin),
          (neg|multiplayer_is_dedicated_server),
          (stop_all_sounds,0),
          (try_begin),
            (scene_slot_eq,":scene", slot_scene_weather, weather_seastorm),#sea storm
            (play_sound,"snd_heavy_rain_sea_loop"),
          (else_try),
            (play_sound,"snd_heavy_rain_loop"),
          (try_end),
          (store_last_sound_channel, "$ambiance_channel"),
          (store_random_in_range,":r",80,101),
          (set_global_cloud_amount,":r"),
          (store_random_in_range,":r",200,301),
          (set_rain,1,":r"),
          (set_fog_distance,400,0x111111),
        (try_end),
      (else_try),
        (assign, "$lightning_cycle",-1),#no storm
        (try_begin),
          (multiplayer_is_server),
          (store_random_in_range,"$wind_strenght",80,100),	#changed to min 80 because ships are to slow
          (store_div,"$WindStrength_variable","$wind_strenght", 45),
          #phaiak begin
          (try_begin),
            (is_between, ":scene", "scn_multi_scene_coast", "scn_mp_addon_maps_end"),
            (store_random_in_range, "$beaufort", 2, 4),
          (else_try),
            (store_random_in_range, "$beaufort", 3, 5),		#global wind-strenght-value (0-12)
          (end_try),
          (call_script, "script_get_wave_properties"),	#sets random values depending on $beaufort
          (assign, "$Amplitude_x",	reg1),
          (assign, "$Amplitude_y",	reg2),
          (assign, "$lamda_x",		reg3),
          (assign, "$lamda_y",		reg4),
          (assign, "$wavespeed_y", 	reg6),
          (assign, "$target_Amplitude_x",	"$Amplitude_x"),
          (assign, "$target_Amplitude_y",	"$Amplitude_y"),
          #phaiak end
          # (store_random_in_range,"$wavespeed_y",10,40),
          # (store_random_in_range,"$Amplitude_x",1000,7000),
          # (store_random_in_range,"$Amplitude_y",1000,6000),
          # (store_div,"$lamda_x","$Amplitude_y",100),
          # (store_div,"$lamda_y","$Amplitude_x",100),
        (try_end),
        
        (try_begin),
          (neg|multiplayer_is_dedicated_server),
          (stop_all_sounds,0),
          (try_begin),
            (this_or_next|scene_slot_eq,":scene",slot_scene_sounds,sounds_sea),
            (scene_slot_eq,":scene",slot_scene_sounds,sounds_coast),
            (play_sound,"snd_ambient_sea_loop"),
          (else_try),
            (scene_slot_eq,":scene", slot_scene_time, time_night),
            (play_sound,"snd_ambient_night_loop"),
          (else_try),
            (scene_get_slot,":sound_type",":scene",slot_scene_sounds),
            (val_add,":sound_type","snd_ambient_day_plains_loop"),
            (play_sound,":sound_type"),
          (try_end),
          (store_last_sound_channel, "$ambiance_channel"),
          
          #setting clouds and stuff
          (try_begin),
            (eq,":scene","scn_multi_scene_inv_1"),#foggy dawn
            (set_skybox, 8, 9),
            (set_rain,0,0),
            (set_fog_distance, 200, 0xFFA09060),
            (set_fixed_point_multiplier,255),
            (set_startup_sun_light,370,270,85),
            (set_startup_ambient_light,50,45,35),
            (set_startup_ground_ambient_light,80,70,50),
          (else_try),
            (eq,":scene","scn_multi_scene_inv_3"),#- morning
            (set_skybox, 6, 7),
            (set_fog_distance, 750, 0xFFA09060),
            (set_fixed_point_multiplier,255),
            (set_startup_sun_light,370,270,85),
            (set_startup_ambient_light,50,45,35),
            (set_startup_ground_ambient_light,80,70,50),
          (else_try),
            (eq,":scene","scn_multi_scene_inv_5"),#cloudy, dark dusk
            (set_skybox, 6, 7),
            (set_fog_distance, 250, 0xFF928055),
            (set_fixed_point_multiplier,255),
            (set_startup_sun_light,410,330,190),
            (set_startup_ambient_light,60,40,10),
            (set_startup_ground_ambient_light,80,70,50),
          (else_try),
            (scene_slot_eq,":scene", slot_scene_weather, weather_clear),
            (store_random_in_range, ":r", 0, 3),
            (try_begin),
              (eq,":r",0),
              (set_global_cloud_amount, 0),
            (else_try),
              (store_random_in_range, ":r", 20, 51),
              (set_global_cloud_amount, ":r"),
            (try_end),
          (else_try),
            (scene_slot_eq,":scene", slot_scene_weather, weather_cloudy),
            (set_global_cloud_amount, 70),
            (try_begin),
              (scene_slot_eq,":scene", slot_scene_time, time_night),
              (set_fog_distance,800,0x010101),
            (else_try),
              (set_fog_distance,800,0x333333),
            (try_end),
          (else_try),
            (scene_slot_eq,":scene", slot_scene_weather, weather_foggy),
            (store_random_in_range, ":r", 0, 61),
            (set_global_cloud_amount, ":r"),
            (try_begin),
              (scene_slot_eq,":scene", slot_scene_time, time_night),
              (set_fog_distance,200,0x010101),
            (else_try),
              (set_fog_distance,200,0x888888),
            (try_end),
          (else_try),
            (scene_slot_eq,":scene", slot_scene_weather, weather_rainy),
            (set_global_cloud_amount, 71),
            (store_random_in_range,":r",20,100),
            (set_rain,1,":r"),
            (try_begin),
              (scene_slot_eq,":scene", slot_scene_time, time_night),
              (set_fog_distance,800,0x010101),
            (else_try),
              (set_fog_distance,800,0x333333),
            (try_end),
          (try_end),
        (try_end),
      (try_end),
      
      (try_begin),
        (multiplayer_is_server),
        (try_begin),
          (scene_slot_eq,":scene",slot_scene_sounds,sounds_sea),
          (call_script,"script_set_wave_shader"),
        (else_try),
          #no waves fo non-sea maps
          #phaiak begin
          (store_random_in_range, "$beaufort", 0, 2),		#global wind-strenght-value (0-12)
          (call_script, "script_get_wave_properties"),	#sets random values depending on $beaufort
          (assign, "$Amplitude_x",	reg1),
          (assign, "$Amplitude_y",	reg2),
          (assign, "$lamda_x",		reg3),
          (assign, "$lamda_y",		reg4),
          (assign, "$wavespeed_y", 	reg6),
          (assign, "$target_Amplitude_x",	"$Amplitude_x"),
          (assign, "$target_Amplitude_y",	"$Amplitude_y"),
          (call_script,"script_set_wave_shader"),	#new: I think this is missing here...
          #phaiak end
          # (store_random_in_range,"$wavespeed_y",1),
          # (store_random_in_range,"$Amplitude_x",100),
          # (store_random_in_range,"$Amplitude_y",100),
          # (assign,"$lamda_x",1),
          # (assign,"$lamda_y",1),
        (try_end),
      (try_end),
  ]),
  ("scene_play_random_ambient_sound", [
      #(store_current_scene,":scene"),
      #(scene_get_slot,":sound_type",":scene",slot_scene_sounds),
      #(val_add,":sound_type","snd_ambient_loop_day_plains"),
      #(play_sound,":sound_type"),
  ]),
  
  ("sp_scene_play_ambient_loop", [
      (store_script_param,":val",1),
      (try_begin),
        (is_currently_night),
        (play_sound,"snd_ambient_night_loop"),
      (else_try),
        (eq,":val",1),#arena
        (play_sound,"snd_ambient_day_plains_loop"),
      (else_try),
        (party_slot_eq,"$current_town",slot_party_type,spt_town),#VC-2352
        (neq, "$current_town","p_town_11"),	#Dorestad = river
        (neq, "$current_town", "p_town_12"),#Lundenwic = river
        (party_slot_eq,"$current_town",slot_town_port, 1),
        (play_sound,"snd_ambient_coast_loop"),
        # (play_sound,"snd_ambient_day_plains_loop"),
      # (else_try),
        # (party_slot_eq,"$current_town",slot_party_type,spt_town),
        # (play_sound,"snd_ambient_day_plains_loop"),
      (else_try),
        (party_slot_eq,"$current_town",slot_party_type,spt_village),
        (play_sound,"snd_ambient_day_village_loop"),
      (else_try),
        (play_sound,"snd_ambient_day_plains_loop"),
      (try_end),
  ]),
  ("sp_scene_play_random_ambient_sound", [
      (store_script_param,":val",1),
      (store_random_in_range,":r",0,10),
      (try_begin),
        (is_currently_night),
        (try_begin),
          (lt,":r",1),
          (play_sound,"snd_ambient_random_night"),
        (try_end),
      (else_try),
        (lt,":r",2),
        (try_begin),
          (eq,":val",1),#arena
          (play_sound,"snd_ambient_random_plains"),
        (else_try),
          (party_slot_eq,"$current_town",slot_party_type,spt_town),
          (store_random_in_range,reg0,0,6),
          (try_begin),
            (eq, reg0, 0),  #add in worker sounds
            (play_sound,"snd_distant_worker"),
          (else_try),
            (eq, reg0, 1),#VC-2352
            (party_slot_eq, "$current_town", slot_town_port, 1),
            (neq, "$current_town","p_town_11"),	#Dorestad = river
            (neq, "$current_town", "p_town_12"),#Lundenwic = river
            (play_sound,"snd_seagull"),
          (else_try),
            (play_sound,"snd_ambient_random_town"),
          (try_end),
        (else_try),
          (party_slot_eq,"$current_town",slot_party_type,spt_village),
          (store_random_in_range,reg0,0,9),
          (try_begin),
            (eq, reg0, 0),  #add in worker sounds
            (play_sound,"snd_distant_worker"),
          (else_try),
            (play_sound,"snd_ambient_random_village"),
          (try_end),
        (else_try),
          (play_sound,"snd_ambient_random_plains"),
        (try_end),
      (try_end),
  ]),
  ("sp_set_agents_for_sounds", [
      (assign,":slot",1),
      (try_for_agents,":agent"),
        (agent_is_alive,":agent"),
        (agent_is_human,":agent"),
        (agent_is_non_player,":agent"),
        (neg|agent_slot_ge,":agent",slot_agent_is_blocked,2),
        (item_set_slot,"itm_items_end",":slot",":agent"),
        (val_add,":slot",1),
      (try_end),
      (item_set_slot,"itm_items_end",0,":slot"),
  ]),
  ("sp_agent_play_sound", [
      (item_get_slot,":end","itm_items_end",0),
      (try_begin),
        (gt,":end",1),
        (store_div,":low",":end",3),
        (store_random_in_range,":r",0,10),
        (lt,":r",":low"),
        (store_random_in_range,":slot",1,":end"),
        (item_get_slot,":agent","itm_items_end",":slot"),
        (agent_is_active,":agent"),
        (agent_is_alive,":agent"),
        (agent_is_human,":agent"),
        (agent_get_troop_id,":troop",":agent"),
        (troop_get_type,":gender",":troop"),
        (val_mod,":gender",2),
        (val_mul,":gender",2),
        (store_random_in_range,":r",0,10),
        (try_begin),
          (lt,":r",2),
          (store_add,":sound","snd_male_sigh",":gender"),
        (else_try),
          (store_add,":sound","snd_male_misc",":gender"),
        (try_end),
        (agent_play_sound,":agent",":sound"),
      (try_end),
  ]),
  
  ("replace_scene_props_for_invasion",[
      (replace_scene_props,"spr_siege_ladder_move_6m","spr_siege_ladder_6m"),
      (replace_scene_props,"spr_siege_ladder_move_8m","spr_siege_ladder_8m"),
      (replace_scene_props,"spr_siege_ladder_move_10m","spr_siege_ladder_10m"),
      (replace_scene_props,"spr_siege_ladder_move_12m","spr_siege_ladder_12m"),
      (replace_scene_props,"spr_siege_ladder_move_14m","spr_siege_ladder_14m"),
      (replace_scene_props,"spr_earth_sally_gate_right","spr_empty"),
      (replace_scene_props,"spr_earth_sally_gate_left","spr_empty"),
  ]),
  ("cf_invasion_respawn_check",[
      (store_script_param,":player",1),
      (assign,":respawn_ok",0),
      (try_begin),#revived (admin/auto-teamkill)
        (player_slot_eq,":player",slot_player_spawned_at_siege_round,-1),#revive
        (assign,":respawn_ok",1),
        # (else_try),#HARDCORE
        # (ge,"$invasion_hardcore",2),
        # (try_begin),
        # (this_or_next|eq,"$g_multiplayer_invasion_wave_number",0),
        # (eq,"$g_multiplayer_invasion_wave_number",1),
        # (this_or_next|player_slot_eq,":player",slot_player_spawned_this_round,0),
        # (player_slot_eq,":player",slot_player_spawned_at_siege_round,1),
        # (assign,":respawn_ok",1),
        # (try_end),
      (else_try),#entered server
        (player_slot_eq,":player",slot_player_spawned_this_round,0),
        # (player_get_unique_id,":id",":player"),
        # (assign,":stop",0),
        # (assign,":loop_end",300),
        # (try_for_range,":slot",0,":loop_end"),
        # (troop_slot_eq,"trp_spawn_data",":slot",":id"),
        # (assign,":stop",1),
        # (assign,":loop_end",0),#break loop
        # (try_end),
        # (eq,":stop",0),
        (assign,":respawn_ok",1),
      (else_try),#respawn each X rounds
        (store_sub,":round","$g_multiplayer_invasion_wave_number",1),
        (val_max,":round",0),
        (val_mod,":round","$g_multiplayer_invasion_respawn_rounds"),
        (eq,":round",0),
        (this_or_next|player_slot_eq,":player",slot_player_spawned_this_round,0),#just entered server
        (player_slot_eq,":player",slot_player_spawned_at_siege_round,1),#or died
        (assign,":respawn_ok",1),
      (try_end),
      #(this_or_next|lt,":round_time",30),
      (eq,":respawn_ok",1),
  ]),
  ("supply_box_used",[
      #server check done before launching script
      (store_trigger_param_1,":agent"),
      (store_script_param_1,":type"),
      (agent_get_player_id,":player",":agent"),
      (try_begin),
        (player_is_active,":player"),
        (try_begin),
          #(neq,"$g_multiplayer_invasion_hardcore",1),
          #(neq,"$g_multiplayer_invasion_hardcore",3),
          (neq,"$g_multiplayer_invasion_wave_time",-1),
          (gt,"$g_multiplayer_invasion_wave_number","$g_multiplayer_invasion_respawn_rounds"),
          (store_sub,":round","$g_multiplayer_invasion_wave_number",1),
          (val_max,":round",0),
          (val_mod,":round","$g_multiplayer_invasion_respawn_rounds"),
          (eq,":round",0),
          (try_begin),
            (eq,":type",1),#used
            (agent_refill_ammo,":agent"),
            (agent_set_hit_points,":agent",100),
            (agent_get_team,":team",":agent"),
            (try_for_agents,":ai_agent"),######refill bots
              (agent_is_alive,":ai_agent"),
              (agent_is_human,":ai_agent"),
              (agent_is_non_player,":ai_agent"),
              (agent_get_team,":ai_team",":ai_agent"),
              (eq,":ai_team",":team"),
              (agent_get_group,":group",":ai_agent"),
              (eq,":group",":player"),
              (agent_refill_ammo,":ai_agent"),
              (agent_set_hit_points,":ai_agent",100),
            (try_end),
            (multiplayer_send_int_to_player, ":player", multiplayer_event_display_message, me_message_supply_box_used),
          (try_end),
        (else_try),
          (neq,":type",1),#start use
          (try_begin),
            (store_sub,reg0,13,"$g_multiplayer_invasion_wave_number"),
            (val_mod,reg0,"$g_multiplayer_invasion_respawn_rounds"),
            (try_begin),
              (eq,reg0,0),
              (assign,reg0,"$g_multiplayer_invasion_respawn_rounds"),
            (try_end),
            (store_sub,reg1,reg0,1),
            (str_store_string,s1,"@The supply box will be available {reg1?after {reg0} rounds:next round}."),
            (multiplayer_send_string_to_player,":player",multiplayer_event_display_string,s1),
          (try_end),
        (try_end),
      (try_end),
  ]),
  ("replace_troop_presentation", [
      (try_begin),
        (eq, "$g_multiplayer_game_type", multiplayer_game_type_lords_battle),
        (start_presentation, "prsnt_multiplayer_troop_select"),
      (else_try),
        (multiplayer_get_my_player, ":my_player_no"),
        (player_get_team_no, ":my_team_no", ":my_player_no"),
        (team_get_faction, ":my_faction_no", ":my_team_no"),
        
        (assign,":selected_troop_no",-1),
        (try_begin),
          (eq,"$g_multiplayer_game_type",multiplayer_game_type_raid),
          (try_begin),
            (eq,":my_team_no",0),
            (store_sub,":selected_troop_no",":my_faction_no",mp_factions_begin),
            (val_add,":selected_troop_no",multiplayer_peasant_troops_begin),
          (try_end),
        (else_try),
          (neq, "$g_multiplayer_troop_classes", 1),
          (store_sub,":selected_troop_no",":my_faction_no",mp_factions_begin),
          (val_add,":selected_troop_no",multiplayer_troops_begin),
        (try_end),
        
        (try_begin),
          (eq,":selected_troop_no",-1),
          (start_presentation, "prsnt_multiplayer_troop_select"),
        (else_try),
          (player_set_troop_id, ":my_player_no", ":selected_troop_no"),
          (multiplayer_send_int_to_server, multiplayer_event_change_troop_id, ":selected_troop_no"),
          (call_script, "script_multiplayer_set_default_item_selections_for_troop", ":selected_troop_no"),
          (call_script, "script_multiplayer_send_item_selections"),
          (assign, "$g_presentation_state", 0),
          (start_presentation, "prsnt_multiplayer_item_select"),
        (try_end),
      (try_end),
  ]),
  ("server_set_chosen_one", [
      (store_script_param, ":agent", 1),
      (store_script_param, ":val", 2),
      
      (try_begin),
        (multiplayer_is_server),
        (assign,"$gThorsChampionAgent",":agent"),
        (try_begin),
          (agent_is_active,":agent"),
          (agent_set_slot,":agent",slot_agent_is_chosen,1),
          #kill horse
          (agent_get_horse,":horse",":agent"),
          (try_begin),
            (agent_is_active,":horse"),
            (agent_deliver_damage_to_agent,":horse",":horse",250),
          (try_end),
          #give weapons
          (try_for_range,":slot",0,4),
            (agent_get_item_slot,":item",":agent",":slot"),
            (gt,":item",0),
            (agent_unequip_item,":agent",":item"),
          (try_end),
          (agent_equip_item,":agent","itm_thors_hammer"),
          (agent_set_wielded_item,":agent","itm_thors_hammer"),
          (agent_set_damage_modifier,":agent",100),
          (call_script, "script_advanced_agent_set_speed_modifier",":agent",130),
          (agent_set_accuracy_modifier,":agent",100),
          (agent_set_reload_speed_modifier,":agent",100),
          
          ##armors (have to run this for all players or they won't see changes)
          (try_for_range,":slot",4,8),
            (agent_get_item_slot,":item",":agent",":slot"),
            (gt,":item",0),
            (agent_unequip_item,":agent",":item"),
          (try_end),
          (agent_equip_item,":agent","itm_thors_armor"),
          (agent_equip_item,":agent","itm_thors_helmet"),
          (agent_equip_item,":agent","itm_thors_boots"),
          
          (neg|multiplayer_is_dedicated_server),
          (play_sound,"snd_thunder_close"),
          (assign, "$temp", ":val"),
          (assign, "$g_multiplayer_message_type", ":agent"),
          (start_presentation, "prsnt_multiplayer_message_champion"),
        (try_end),
        (try_for_players,":i",1),
          (multiplayer_send_3_int_to_player, ":i", multiplayer_event_agent, me_agent_is_chosen, ":agent", ":val"),
        (try_end),
      (try_end),
  ]),
  ("cf_neg_main_presentation_is_active", [
      (neg|is_presentation_active, "prsnt_multiplayer_team_select"),
      (neg|is_presentation_active, "prsnt_multiplayer_troop_select"),
      (neg|is_presentation_active, "prsnt_multiplayer_item_select"),
      (neg|is_presentation_active, "prsnt_game_multiplayer_admin_panel"),
      (neg|is_presentation_active, "prsnt_multiplayer_escape_menu"),
      (neg|is_presentation_active, "prsnt_multiplayer_stats_chart"),
      (neg|is_presentation_active, "prsnt_multiplayer_admin_send_message"),
  ]),
  
  ##########################
  ###MP & SP TRIGGER SCRIPTS
  ("check_dehorsing", [
      (store_trigger_param,":victim",1),
      (store_trigger_param,":damage",3),
      (assign,":weapon",reg0),
      
      (try_begin),
        (eq,"$g_multiplayer_allow_fall_from_horse",1),
        (agent_is_active,":victim"),
        (agent_is_alive,":victim"),
        (this_or_next|agent_is_non_player,":victim"),#players can only be dehorsed once per spawn, otherwise collision bugs appear
        (agent_slot_eq,":victim",slot_agent_was_dehorsed,0),
        (agent_is_human,":victim"),
        (agent_get_horse,":horse",":victim"),
        (agent_is_active,":horse"),
        (agent_is_alive,":horse"),
        
        (this_or_next|neq, "$dog_companion", 1),# do not dehorse dog(VC-2111)
        (neq, ":victim", "$player_dog_agent_no"),
        
        (ge,":damage",10),
        (store_agent_hit_points,":hp",":victim",1),
        (gt,":hp",":damage"),
        (store_random_in_range,":r",8,50),
        (gt,":damage",":r"),
        
        (item_get_type,":weapon_type",":weapon"),
        (neq,":weapon_type",itp_type_crossbow),
        (neq,":weapon_type",itp_type_bow),
        
        (agent_start_running_away,":horse"),
        (agent_stop_running_away,":horse"),
        
        (store_random_in_range,":anim","anim_rider_fall_right","anim_strike_chest_front_stop"),
        (agent_set_animation,":victim",":anim"),
        (agent_set_slot,":victim",slot_agent_was_dehorsed,1),
        
        (try_begin),
          (game_in_multiplayer_mode),
          (try_for_players,":i",1),
            (multiplayer_send_3_int_to_player,":i",multiplayer_event_agent, me_agent_play_animation, ":victim",":anim"),
          (try_end),
        (try_end),
        
      (try_end),
  ]),
  ("check_falling_from_horse", [
      (store_trigger_param,":rider",1),
      (store_trigger_param,":horse",2),
      (try_begin),
        (this_or_next|neg|game_in_multiplayer_mode),
        #(eq,"$g_multiplayer_allow_fall_from_horse_dmg",1),
        (agent_is_active,":horse"),
        (neg|agent_is_alive,":horse"),
        (agent_is_active,":rider"),
        (agent_is_alive,":rider"),
        
        (agent_get_speed,pos1,":horse"),
        (position_get_y,":speed",pos1),
        
        (convert_from_fixed_point,":speed"),
        (val_mul,":speed",5),
        (store_random_in_range,":damage",0,":speed"),
        
        (gt,":damage",0),
        (store_agent_hit_points,":hp",":rider",1),
        (val_sub,":hp",":damage"),
        (val_max,":hp",1),
        (agent_set_hit_points,":rider",":hp",1),
      (try_end),
  ]),
  ("check_horse_blunt_damage", [
      (store_trigger_param,":victim",1),
      (store_trigger_param,":dealer",2),
      (store_trigger_param,":damage",3),
      (assign,":weapon",reg0),
      
      (try_begin),
        (gt,":weapon",0),
        (agent_is_active,":victim"),
        (agent_is_alive,":victim"),
        (neg|agent_is_human,":victim"),
        (agent_is_active,":dealer"),
        (agent_get_action_dir,":swing",":dealer"),
        (is_between,":swing",1,3),#left or right
        (item_get_swing_damage_type,":dam_type",":weapon"),
        (eq,":dam_type",blunt),
        (val_div,":damage",2),
        (set_trigger_result,":damage"),
      (try_end),
      (assign,reg0,":damage"),
  ]),
  
  ("shield_taunt_trigger", [
      (get_player_agent_no,":agent"),
      (try_begin),
        (agent_is_active,":agent"),
        (agent_is_alive,":agent"),
        (agent_get_wielded_item,":item",":agent",1),
        (gt,":item",0),#has shield
        (agent_get_wielded_item,":item",":agent",0),
        (gt,":item",0),#has weapon
        (item_get_type,":item_type",":item"),
        (this_or_next|eq,":item_type",itp_type_polearm),
        (eq,":item_type",itp_type_one_handed_wpn),
        (agent_get_horse,":horse",":agent"),
        (eq,":horse",-1),#not on horse
        (try_begin),
          (game_in_multiplayer_mode),
          (multiplayer_send_int_to_server, multiplayer_event_agent, me_agent_shield_taunt),
        (else_try),
          (agent_set_animation, ":agent", "anim_shield_taunt", 1),
          (agent_play_sound, ":agent", "snd_shield_taunt"),
        (try_end),
      (try_end),
  ]),
  ("shield_bash_trigger", [
      (get_player_agent_no,":agent"),
      (try_begin),
        (agent_is_active,":agent"),
        (agent_is_alive,":agent"),
        (agent_get_horse,":horse",":agent"),
        (eq,":horse",-1),#not on horse
        (agent_get_wielded_item,":item",":agent",1),
        (gt,":item",0),#has shield
        (agent_get_animation,":anim",":agent",0),
        (neg|is_between,":anim","anim_walk_forward_crouch","anim_ride_0"),#is not crouching
        (try_begin),
          (game_in_multiplayer_mode),
          (multiplayer_send_int_to_server, multiplayer_event_agent, me_agent_shield_bash),
        (else_try),
          (agent_slot_eq,":agent",slot_agent_shieldbash_cooldown,0), #colldown for sp vc-2854
          (call_script,"script_shield_bash_script",1,":agent",0),
        (try_end),
      (try_end),
  ]),
  ("shield_bash_AI_trigger", [
      
      # (try_begin),
      # (game_in_multiplayer_mode),
      # (eq,"$g_multiplayer_game_type",multiplayer_game_type_deathmatch),
      # (assign,":check_teams",0),
      # (else_try),
      # (assign,":check_teams",1),
      # (try_end),
      
      (try_for_agents,":agent"),
        (agent_is_alive,":agent"),
        (agent_is_human,":agent"),
        (try_begin),
          (agent_get_slot,":cooldown",":agent",slot_agent_shieldbash_cooldown),
          (gt,":cooldown",0),
          (val_sub,":cooldown",1),
          (agent_set_slot,":agent",slot_agent_shieldbash_cooldown,":cooldown"),
        (try_end),
        (agent_slot_eq,":agent",slot_agent_shieldbash_cooldown,0),
        (agent_is_non_player,":agent"),
        (agent_get_horse,":horse",":agent"),
        (eq,":horse",-1),#not on horse
        (agent_get_wielded_item,":item",":agent",1),
        (gt,":item",0),#has shield
        # (agent_get_team,":team",":agent"),
        (agent_get_position,pos1,":agent"),
        
        (assign,":enemies_close",0),
        (assign,":enemies_in_range",0),
        (agent_ai_get_num_cached_enemies, ":num_nearby_agents", ":agent"),
        (try_for_range, reg0, 0, ":num_nearby_agents"),
          (agent_ai_get_cached_enemy, ":i", ":agent", reg0),
          # (try_for_agents,":i"),
          (agent_is_alive,":i"),
          (agent_is_human,":i"),
          # (neq,":i",":agent"),
          # (agent_get_team,":i_team",":i"),
          # (this_or_next|eq,":check_teams",0),
          # (neq,":team",":i_team"),
          # (this_or_next|eq,":check_teams",0),
          # (teams_are_enemies,":team",":i_team"),
          (agent_get_horse,":horse",":i"),
          (eq,":horse",-1),#not on horse
          (agent_get_position,pos2,":i"),
          (neg|position_is_behind_position,pos2,pos1),
          (get_distance_between_positions,":dist",pos1,pos2),
          (lt,":dist",200),
          (val_add,":enemies_close",1),
          (lt,":dist",140),
          (val_add,":enemies_in_range",1),
        (try_end),
        (gt,":enemies_in_range",0),
        (val_add,":enemies_in_range",":enemies_close"),
        (val_mul,":enemies_in_range",3),
        (val_add,":enemies_in_range",7),
        
        (store_random_in_range,":r",0,50),
        (lt,":r",":enemies_in_range"),
        (call_script,"script_shield_bash_script",1,":agent",0),
      (try_end),
  ]),
  ("shield_bash_script", [
      (store_script_param,":continue",1),
      (store_script_param,":agent",2),
      (store_script_param,":player",3),
      
      (try_begin),
        (eq,":continue",0),#is not singleplayer
        (agent_is_alive,":agent"),
        (agent_slot_eq,":agent",slot_agent_shieldbash_cooldown,0),
        (agent_get_horse,":horse",":agent"),
        (eq,":horse",-1),#not on horse
        (agent_get_wielded_item,":item",":agent",1),
        (gt,":item",0),#has shield
        (assign,":continue",2),
      (try_end),
      
      (try_begin),
        (ge,":continue",1),
        (agent_get_position,pos1,":agent"),
        (agent_set_animation,":agent","anim_shield_bash"),
        (agent_set_slot,":agent",slot_agent_shieldbash_cooldown,shielbash_miss_cooldown),# 1x2= 2sec
        
        (try_begin),
          (eq,":continue",2),#multi
          (try_for_players,":i",1),
            (multiplayer_send_3_int_to_player,":i",multiplayer_event_agent,me_agent_play_animation,":agent","anim_shield_bash"),
          (try_end),
          (player_get_gender,":gender",":player"),
        (else_try),
          (agent_get_troop_id,":troop",":agent"),
          (troop_get_type,":gender",":troop"),
          (val_mod,":gender",2),
        (try_end),
        (try_begin),
          (eq,":gender",0),
          (agent_play_sound,":agent","snd_man_shield_bash"),
        (else_try),
          (agent_play_sound,":agent","snd_woman_shield_bash"),
        (try_end),
        
        (assign,":victim",-1),
        (assign,":min_dist",125),#125cm
        (try_begin),#Players
          (neg|agent_is_non_player,":agent"),
          (try_for_agents,":i"),
            (neq,":i",":agent"),
            (agent_is_alive,":i"),
            (agent_is_human,":i"),
            (agent_get_position,pos2,":i"),
            (get_distance_between_positions,":dist",pos1,pos2),
            (le,":dist",":min_dist"),
            (neg|position_is_behind_position,pos2,pos1),
            (assign,":victim",":i"),
            (assign,":min_dist",":dist"),
          (try_end),
        (else_try),#AI
          (agent_ai_get_num_cached_enemies, ":num_nearby_agents", ":agent"),
          (try_for_range, reg0, 0, ":num_nearby_agents"),
            (agent_ai_get_cached_enemy, ":i", ":agent", reg0),
            (neq,":i",":agent"),
            (agent_is_alive,":i"),
            (agent_is_human,":i"),
            (agent_get_position,pos2,":i"),
            (get_distance_between_positions,":dist",pos1,pos2),
            (le,":dist",":min_dist"),
            (neg|position_is_behind_position,pos2,pos1),
            (assign,":victim",":i"),
            (assign,":min_dist",":dist"),
          (try_end),
        (try_end),
        (agent_is_active,":victim"),
        (agent_get_horse,":horse",":victim"),
        (eq,":horse",-1),#not on horse
        
        (agent_set_slot,":agent",slot_agent_shieldbash_cooldown,shielbash_hit_cooldown),# 10x2= 20sec after successful hit
        (agent_set_animation,":victim","anim_shield_bash_hit"),
        (agent_play_sound,":victim","snd_shield_hit_wood_wood"),
        (try_begin),
          (eq,":continue",2),#multi
          (try_for_players,":i",1),
            (multiplayer_send_3_int_to_player,":i",multiplayer_event_agent,me_agent_play_animation,":victim","anim_shield_bash_hit"),
          (try_end),
        (try_end),
      (try_end),
  ]),
  ("berserk_trigger", [
      (try_begin),
        (this_or_next|neg|game_in_multiplayer_mode),
        (neq,"$g_multiplayer_game_type",multiplayer_game_type_duel),
        (get_player_agent_no,":agent"),
        (agent_is_active,":agent"),
        (agent_is_alive,":agent"),
        (call_script,"script_cf_agent_is_not_peasant",":agent"),
        (try_begin),
          (game_in_multiplayer_mode),
          (multiplayer_send_int_to_server,multiplayer_event_agent,me_agent_berserk),
        (else_try),
          (eq,"$berserk_cooldown",0),
          (assign,"$berserk_cooldown",180),#once per 3 min
          
          (troop_get_type, ":is_female", "trp_player"),
          (val_mod, ":is_female", 2),
          (try_begin),
            (eq, ":is_female", 1), #player is female
            (agent_play_sound,":agent","snd_woman_yell"),###ARCRY SOUND
          (else_try),
            (agent_play_sound,":agent","snd_man_warcry"),###ARCRY SOUND
          (try_end),
          
          (agent_set_damage_modifier,":agent",125),
          (call_script, "script_advanced_agent_set_speed_modifier",":agent",110),
          (agent_set_accuracy_modifier,":agent",50),
          (agent_set_reload_speed_modifier,":agent",50),
          (agent_set_slot,":agent",slot_agent_berserk_cooldown,50),
          (agent_set_slot,":agent",slot_agent_horn_cooldown,0),
          (display_message,"@You unleash your battle rage!",0x000000),
          (assign,"$is_berserk",1),
        (else_try),
          (display_message,"@You are too exhausted to go into a battle rage."),
        (try_end),
      (try_end),
  ]),
  ("berserk_cooldown_trigger", [##SP only
      (try_begin),
        (get_player_agent_no,":agent"),
        (agent_is_active,":agent"),
        (agent_is_alive,":agent"),
        (agent_get_slot,":cooldown",":agent",slot_agent_berserk_cooldown),
        (try_begin),
          (gt,":cooldown",0),
          (val_sub,":cooldown",1),
          (agent_set_slot,":agent",slot_agent_berserk_cooldown,":cooldown"),
          (try_begin),
            (eq,":cooldown",35),#is tired
            (agent_set_damage_modifier,":agent",60),
            (call_script, "script_advanced_agent_set_speed_modifier",":agent",70),
            (display_message,"@You feel exhausted after the rage.",0xff3333),
            (assign,"$is_berserk",-1),
            (mission_cam_animate_to_screen_color, 0x55000000, 2000),
          (else_try),
            (eq,":cooldown",0),#back to normal
            (agent_set_damage_modifier,":agent",100),
            (call_script, "script_advanced_agent_set_speed_modifier",":agent",100),
            (agent_set_accuracy_modifier,":agent",100),
            (agent_set_reload_speed_modifier,":agent",100),
            (display_message,"@Your strength is back.",0x88FF88),
            (assign,"$is_berserk",0),
            (mission_cam_animate_to_screen_color, 0x00000000, 2000),
          (try_end),
        (try_end),
      (try_end),
  ]),
  
  ("horn_sp_trigger", [#singleplayer only
      (get_player_agent_no,":agent"),
      (try_begin),
        (agent_is_active,":agent"),
        (agent_is_alive,":agent"),
        (agent_play_sound,":agent","snd_horn"),
        (agent_get_horse,":horse",":agent"),
        (try_begin),
          (agent_is_active,":horse"),
          (agent_set_animation,":agent","anim_horn",1),
        (else_try),
          (agent_set_animation,":agent","anim_horn",0),
        (try_end),
        
        ###horn effect
        #(call_script, "script_apply_courage_bonus", 2),
        (call_script, "script_change_courage_around_agent", 50, ":agent"),	#still needs to get balanced
      (try_end),
  ]),
  ###############
  ###Singleplayer
  ("cf_prop_spawn_agent", [
      #(store_script_param,":type",1),
      (ge,"$can_spawn_commoners",1),
      (this_or_next|eq,"$can_spawn_commoners",1),#arena
      (eq, "$g_mt_mode", abm_visit),#arena
      (this_or_next|eq,"$talk_context",tc_tavern_talk),
      (this_or_next|eq,"$talk_context",tc_court_talk),
      (eq,"$talk_context",tc_town_talk),
      
      (this_or_next|eq,"$talk_context",tc_tavern_talk),
      (neg|is_currently_night),
      
      (store_trigger_param,":instance",1),
      
      (prop_instance_get_scene_prop_kind,":type",":instance"),
      
      (assign,":troop",-1),
      (prop_instance_get_variation_id,":var",":instance"),
      (prop_instance_get_variation_id_2,":chance",":instance"),
      (try_begin),
        (eq,":type","spr_z_entry_feast_sitting"),
        (try_begin),
          (is_between,"$current_town",centers_begin, centers_end),
          (store_faction_of_party,":center_faction","$current_town"),
          (faction_slot_eq,":center_faction",slot_faction_ai_state,sfai_feast),
          (faction_slot_eq,":center_faction",slot_faction_ai_object,"$current_town"),
          (assign,":chance",100),
        (else_try),
          (assign,":chance",0),
        (try_end),
      (else_try),
        (eq,":chance",0),
        (assign,":chance",33),
      (try_end),
      (store_random_in_range,":random",0,100),
      (store_current_hours,":mul"),
      (val_mod,":mul",10000),
      (val_mul,":random",":mul"),
      (val_mod,":random",100),
      (assign,":sound",-1),
      (try_begin),
        (this_or_next|lt,":random",":chance"),
        (eq,":chance",1),
        (try_begin),#priest sitting
          (eq,":type","spr_z_entry_priest_sitting"),
          (try_begin),
            (neg|is_between,":var",1,2),
            (store_random_in_range,":var",1,2),
            (val_mul,":var",":mul"),
            (val_mod,":var",1),
            (val_add,":var",1),
          (try_end),
          (assign,":troop","trp_monjes"),
          (try_begin),
            #(eq,":var",1),
            # (assign,":item",-1),
            # (assign,":anim","anim_sitting_praying"),
            # (else_try),
            (assign,":item","itm_reading_ani"),
            (assign,":anim","anim_sitting_reading"),
          (try_end),
        (else_try),
          (eq,":type","spr_z_entry_military_sitting"),
          (try_begin),
            (neg|is_between,":var",1,2),
            (store_random_in_range,":var",1,2),
            (val_mul,":var",":mul"),
            (val_mod,":var",1),
            (val_add,":var",1),
          (try_end),
          (store_faction_of_party,":faction","$current_town"),
          (store_random_in_range,":slot",0,5),
          (val_mul,":slot",":mul"),
          (val_mod,":slot",5),
          (val_add,":slot",slot_faction_tier_1_troop),
          (faction_get_slot,":troop",":faction",":slot"),
          (try_begin),
            #(eq,":var",1),
            (assign,":item","itm_sharpening_1_ani"),
            (assign,":anim","anim_sitting_sharpening_1"),
            (assign,":sound","snd_agent_anim_sharpening_1"),
            # (else_try),
            # (eq,":var",2),
            # (assign,":item","itm_sharpening_2_ani"),
            # (assign,":anim","anim_sitting_sharpening_2"),
          (try_end),
        (else_try),
          (eq,":type","spr_z_entry_child_sitting"),
          (assign,":item",-1),
          (assign,":anim","anim_sitting_child_1"),
          (store_random_in_range,":troop",0,2),
          (val_mul,":troop",":mul"),
          (val_mod,":troop",2),
          (val_add,":troop","trp_nino_varon"),
        (else_try),
          (eq,":type","spr_z_entry_smith"),
          (assign,":troop","trp_village_walker_3a"),
          (assign,":item","itm_smithing_ani"),
          (assign,":anim","anim_smithing"),
          (assign,":sound","snd_agent_anim_smithing"),
        (else_try),
          # (eq,":type","spr_z_entry_building"),
          # (assign,":troop","trp_scotch_castle_guard"),
          # (assign,":item","itm_field_working_1_ani"),
          # (assign,":anim","anim_field_working_1"),
          # (else_try),
          (this_or_next|eq,":type","spr_z_entry_field_working_1"),
          (this_or_next|eq,":type","spr_z_entry_field_working_2"),
          (this_or_next|eq,":type","spr_z_entry_field_working_3"),
          (this_or_next|eq,":type","spr_z_entry_fisherman_sitting"),
          (this_or_next|eq,":type","spr_z_entry_woodcutting"),
          (this_or_next|eq,":type","spr_z_entry_tavern_sitting"),
          (this_or_next|eq,":type","spr_z_entry_village_sitting"),
          (this_or_next|eq,":type","spr_z_entry_feast_sitting"),
          (eq,":type","spr_z_entry_grinding"),
          
          (try_begin),
            (neg|is_between,":var",1,4),
            (store_random_in_range,":var",1,4),
            (val_mul,":var",":mul"),
            (val_mod,":var",3),
            (val_add,":var",1),
          (try_end),
          
          (store_current_scene,":scene"),
          (try_begin),#if monasteries = monk
            (is_between,":scene","scn_monasterio1_normal","scn_caravanatacada"),
            (assign,":troop","trp_monjes"),
          (else_try),
            (store_random_in_range,":slot",0,num_town_walkers),
            (val_mul,":slot",":mul"),
            (val_mod,":slot",num_town_walkers),
            (val_add,":slot",slot_center_walker_0_troop),
            (party_get_slot,":troop","$current_town",":slot"),
            
            (try_begin),#if troop = 0
              (eq,":troop",0),
              (store_random_in_range,":troop","trp_village_walker_1","trp_spy_walker_1"),
            (try_end),
            (try_begin),#no mount
              (eq,":troop","trp_village_walker_1"),
              (assign,":troop","trp_village_walker_1a"),
            (else_try),
              (eq,":troop","trp_village_walker_3"),
              (assign,":troop","trp_village_walker_3a"),
            (else_try),
              (eq,":troop","trp_village_walker_5"),
              (assign,":troop","trp_village_walker_5a"),
            (try_end),
          (try_end),
          
          #(assign,":troop","trp_spy_walker_1"),
          (try_begin),
            (eq,":type","spr_z_entry_field_working_1"),
            (assign,":item","itm_field_working_1_ani"),
            (assign,":anim","anim_field_working_1"),
            (assign,":sound","snd_agent_anim_field_working_1"),
          (else_try),
            (eq,":type","spr_z_entry_field_working_2"),
            (assign,":item","itm_field_working_2_ani"),
            (assign,":anim","anim_field_working_2"),
          (else_try),
            (eq,":type","spr_z_entry_field_working_3"),
            (assign,":item",-1),
            (assign,":anim","anim_field_working_3"),
          (else_try),
            (eq,":type","spr_z_entry_grinding"),
            (assign,":item","itm_grinding_ani"),
            (assign,":anim","anim_grinding"),
          (else_try),
            (eq,":type","spr_z_entry_fisherman_sitting"),
            (assign,":item","itm_fishing_ani"),
            (assign,":anim","anim_sitting_fishing"),
          (else_try),
            (eq,":type","spr_z_entry_woodcutting"),
            #(assign,":item","itm_woodcutting_ani"),
            #(try_begin),
            # (eq,":var",1),
            # (assign,":anim","anim_woodcutting_1"),
            # (else_try),
            # (eq,":var",2),
            (assign,":item","itm_woodcutting_2_ani"),
            (assign,":anim","anim_woodcutting_2"),
            (assign,":sound","snd_agent_anim_woodcutting_2"),
            # (else_try),
            # (eq,":var",3),
            # (assign,":anim","anim_woodcutting_3"),
            #(try_end),
          (else_try),
            (this_or_next|eq,":type","spr_z_entry_feast_sitting"),
            (eq,":type","spr_z_entry_tavern_sitting"),
            (store_random_in_range,":armed_chance",0,25),
            (val_mul,":armed_chance",":mul"),
            (val_mod,":armed_chance",25),
            (try_begin),
              (lt,":armed_chance",5),
              (neg|is_between,"$current_town",villages_begin,villages_end),
              (store_faction_of_party,":faction","$current_town"),
              (val_add,":armed_chance",slot_faction_tier_1_troop),
              (faction_get_slot,":troop",":faction",":armed_chance"),
            (try_end),
            (try_begin),
              (eq,":var",1),
              (assign,":item",-1),
              (assign,":anim","anim_sitting"),
            (else_try),
              (eq,":var",2),
              (assign,":item","itm_drinking_ani"),
              (assign,":anim","anim_sitting_drinking"),
            (else_try),
              (eq,":var",3),
              (assign,":item","itm_eating_ani"),
              (assign,":anim","anim_sitting_eating"),
            (try_end),
          (else_try),
            (eq,":type","spr_z_entry_village_sitting"),
            (try_begin),
              (eq,":var",1),
              (assign,":item","itm_sitting_working_1_ani"),
              (assign,":anim","anim_sitting_working_1"),
            (else_try),
              (eq,":var",2),
              (assign,":item","itm_sitting_working_2_ani"),
              (assign,":anim","anim_sitting_working_2"),
            (else_try),
              (eq,":var",3),
              (assign,":item","itm_sitting_working_3_ani"),
              (assign,":anim","anim_sitting_working_3"),
            (try_end),
          (try_end),
        (else_try),
          (eq,":type","spr_z_entry_brooming"),
          (assign,":troop","trp_village_walker_6"),
          (assign,":item","itm_brooming_ani"),
          (assign,":anim","anim_brooming"),
        (else_try),
          (eq,":type","spr_z_entry_cow"),
          (prop_instance_get_position,pos0,":instance"),
          (set_spawn_position,pos0),
          (store_random_in_range,":item",0,2),
          (val_add,":item","itm_cow1"),
          (spawn_horse,":item"),
        (else_try),
          (eq,":type","spr_z_entry_horse"),
          (prop_instance_get_position,pos0,":instance"),
          (set_spawn_position,pos0),
          (store_random_in_range,":item","itm_common_horse","itm_cow1"),
          (spawn_horse,":item"),
          #phaiak begin
        (else_try),
          (prop_instance_get_position,pos0,":instance"),
          (set_spawn_position,pos0),
          (assign, reg1, 0),
          (assign, reg2, imod_cracked),
          (shuffle_range, 1, 3),
          (assign, ":rand", reg1),
          (eq, 1, 0),
        (else_try),
          (eq,":type","spr_z_entry_pig"),
          (spawn_horse,"itm_animal_pig", ":rand"),
        (else_try),
          (eq,":type","spr_z_entry_piglet"),
          (spawn_horse,"itm_animal_piglet", ":rand"),
        (else_try),
          (eq,":type","spr_z_entry_sheep"),
          (store_random_in_range, ":rand2", 0, 2),
          (store_add, ":sheep_itm", "itm_animal_sheep", ":rand2"),
          (assign, reg1, 0),
          (assign, reg2, imod_cracked),
          (assign, reg3, imod_rusty),
          (assign, reg4, imod_bent),
          (shuffle_range, 1, 5),
          (spawn_horse,":sheep_itm", reg1),
        (else_try),
          (eq,":type","spr_z_entry_dog"),
          (spawn_horse,"itm_animal_dog", ":rand"),
          #phaiak end
        (try_end),
      (try_end),
      
      (gt,":troop",0),
      
      (prop_instance_get_position,pos0,":instance"),
      (set_spawn_position,pos0),
      (spawn_agent,":troop"),
      
      (assign,":agent",reg0),
      (try_begin),
        (gt,":item",0),
        (agent_get_item_slot,":gloves",":agent",ek_gloves),
        (try_begin),
          (gt,":gloves",0),
          (agent_unequip_item,":agent",":gloves"),
        (try_end),
        (agent_equip_item,":agent",":item"),
      (try_end),
      # (agent_set_wielded_item,":agent",":item"),
      (agent_set_team,":agent",7),
      
      (agent_set_stand_animation,":agent",":anim"),
      (agent_set_animation,":agent",":anim"),
      (assign,":end",1),
      (convert_to_fixed_point,":end"),
      (store_random_in_range,":progress",0,":end"),
      (agent_set_animation_progress,":agent",":progress"),
      (agent_ai_set_interact_with_player,":agent",0),
      (agent_set_slot,":agent",slot_agent_prop,":instance"),
      (try_begin),
        (gt,":sound",0),
        (agent_play_sound,":agent",":sound"),
        (agent_set_slot,":agent",slot_agent_is_blocked,2),#block agent (no walking/dialogs/no sounds)
      (else_try),
        (eq,":type","spr_z_entry_child_sitting"),
        (agent_set_slot,":agent",slot_agent_is_blocked,2),#block agent (no walking/dialogs/no sounds)
      (else_try),
        (agent_set_slot,":agent",slot_agent_is_blocked,1),#block agent (no walking/dialogs)
      (try_end),
  ]),
  ("teleport_talk_agent_to_initial_pos", [
      (agent_get_slot,":instance","$talk_agent",slot_agent_prop),
      (try_begin),
        (gt,":instance",0),
        (prop_instance_is_valid,":instance"),
        (prop_instance_get_position,pos1,":instance"),
        (agent_set_position,"$talk_agent",pos1),
        (position_move_y,pos1,300),
        (agent_set_look_target_position,"$talk_agent",pos1),
      (try_end),
  ]),
  ("cf_get_random_kingdom_center",[
      (store_script_param,":party_no",1),
      (store_script_param,":begin",2),
      (store_script_param,":end",3),
      
      (assign, ":result", -1),
      (assign, ":total_centers", 0),
      (store_faction_of_party, ":party_faction", ":party_no"),
      
      (try_for_range, ":center_no", ":begin", ":end"),
        (store_faction_of_party, ":center_faction", ":center_no"),
        (eq, ":center_faction", ":party_faction"),
        (neq,":party_no",":center_no"),
        (val_add, ":total_centers", 1),
      (try_end),
      
      (gt, ":total_centers", 0),
      (store_random_in_range, ":random_center", 0, ":total_centers"),
      (assign, ":total_centers", 0),
      (try_for_range, ":center_no", ":begin", ":end"),
        (eq, ":result", -1),
        (store_faction_of_party, ":center_faction", ":center_no"),
        (eq, ":center_faction", ":party_faction"),
        (neq,":party_no",":center_no"),
        (val_sub, ":random_center", 1),
        (lt, ":random_center", 0),
        (assign, ":result", ":center_no"),
      (try_end),
      (assign, reg0, ":result"),
  ]),
  ("set_items_for_tournament_by_factions",[
      (store_script_param,":faction",1),
      
      #helmets - "itm_tourney_helm_red", "itm_arena_turban_red" or -1 for none
      
      (try_begin),#                                        0-100%  0-100%    <-------------- 0-100% ----------->
        (eq,":faction","fac_kingdom_1"),#                Horse  Shield     Club  Staff  Seax  Spear  Sword  Axe 				  Javelins chance
        (call_script,"script_set_items_for_tournament_new",  0,    85,      25,    15,    10,    15,   15,   20, "itm_tourney_helm_red", 10),
      (else_try),#                                         0-100%  0-100%    <-------------- 0-100% ----------->
        (eq,":faction","fac_kingdom_2"),#                Horse  Shield     Club  Staff  Seax  Spear  Sword  Axe 				  Javelins chance
        (call_script,"script_set_items_for_tournament_new",  0,    85,      25,    15,    10,    15,   15,   20, "itm_tourney_helm_red", 10),
      (else_try),#                                         0-100%  0-100%    <-------------- 0-100% ----------->
        (eq,":faction","fac_kingdom_3"),#                Horse  Shield     Club  Staff  Seax  Spear  Sword  Axe 				  Javelins chance
        (call_script,"script_set_items_for_tournament_new",  0,    85,      25,    15,    10,    15,   15,   20, "itm_tourney_helm_red", 10),
      (else_try),#                                         0-100%  0-100%    <-------------- 0-100% ----------->
        (eq,":faction","fac_kingdom_4"),#                Horse  Shield     Club  Staff  Seax  Spear  Sword  Axe 				  Javelins chance
        (call_script,"script_set_items_for_tournament_new",  0,    85,      25,    15,    10,    15,   15,   20, "itm_tourney_helm_red", 10),
      (else_try),#                                         0-100%  0-100%    <-------------- 0-100% ----------->
        (eq,":faction","fac_kingdom_5"),#                Horse  Shield     Club  Staff  Seax  Spear  Sword  Axe 				  Javelins chance
        (call_script,"script_set_items_for_tournament_new",  0,    85,      25,    15,    10,    15,   15,   20, "itm_tourney_helm_red", 10),
      (else_try),#                                         0-100%  0-100%    <-------------- 0-100% ----------->
        (eq,":faction","fac_kingdom_6"),#                Horse  Shield     Club  Staff  Seax  Spear  Sword  Axe 				  Javelins chance
        (call_script,"script_set_items_for_tournament_new",  0,    85,      25,    15,    10,    15,   15,   20, "itm_tourney_helm_red", 10),
      (else_try),#                                         0-100%  0-100%    <-------------- 0-100% ----------->
        (eq,":faction","fac_kingdom_7"),#                Horse  Shield     Club  Staff  Seax  Spear  Sword  Axe 				  Javelins chance
        (call_script,"script_set_items_for_tournament_new",  0,    85,      25,    15,    10,    15,   15,   20, "itm_tourney_helm_red", 10),
      (else_try),#                                         0-100%  0-100%    <-------------- 0-100% ----------->
        (eq,":faction","fac_kingdom_8"),#                Horse  Shield     Club  Staff  Seax  Spear  Sword  Axe 				  Javelins chance
        (call_script,"script_set_items_for_tournament_new",  0,    85,      25,    15,    10,    15,   15,   20, "itm_tourney_helm_red", 10),
      (else_try),#                                         0-100%  0-100%    <-------------- 0-100% ----------->
        (eq,":faction","fac_kingdom_9"),#                Horse  Shield     Club  Staff  Seax  Spear  Sword  Axe 				  Javelins chance
        (call_script,"script_set_items_for_tournament_new",  0,    85,      25,    15,    10,    15,   15,   20, "itm_tourney_helm_red", 10),
      (else_try),#                                         0-100%  0-100%    <-------------- 0-100% ----------->
        (eq,":faction","fac_kingdom_10"),#               Horse  Shield     Club  Staff  Seax  Spear  Sword  Axe 				  Javelins chance
        (call_script,"script_set_items_for_tournament_new",  0,    85,      25,    15,    10,    15,   15,   20, "itm_tourney_helm_red", 10),
      (else_try),#                                         0-100%  0-100%    <-------------- 0-100% ----------->
        (eq,":faction","fac_kingdom_11"),#               Horse  Shield     Club  Staff  Seax  Spear  Sword  Axe 				  Javelins chance
        (call_script,"script_set_items_for_tournament_new",  0,    85,      25,    15,    10,    15,   15,   20, "itm_tourney_helm_red", 10),
      (else_try),#                                         0-100%  0-100%    <-------------- 0-100% ----------->
        (eq,":faction","fac_kingdom_12"),#               Horse  Shield     Club  Staff  Seax  Spear  Sword  Axe 				  Javelins chance
        (call_script,"script_set_items_for_tournament_new",  0,    85,      25,    15,    10,    15,   15,   20, "itm_tourney_helm_red", 10),
      (else_try),#                                         0-100%  0-100%    <-------------- 0-100% ----------->
        (eq,":faction","fac_kingdom_13"),#               Horse  Shield     Club  Staff  Seax  Spear  Sword  Axe 				  Javelins chance
        (call_script,"script_set_items_for_tournament_new",  0,    85,      25,    15,    10,    15,   15,   20, "itm_tourney_helm_red", 10),
      (else_try),#                                         0-100%  0-100%    <-------------- 0-100% ----------->
        (eq,":faction","fac_kingdom_14"),#               Horse  Shield     Club  Staff  Seax  Spear  Sword  Axe 				  Javelins chance
        (call_script,"script_set_items_for_tournament_new",  0,    85,      25,    15,    10,    15,   15,   20, "itm_tourney_helm_red", 10),
      (else_try),#                                         0-100%  0-100%    <-------------- 0-100% ----------->
        (eq,":faction","fac_kingdom_15"),#               Horse  Shield     Club  Staff  Seax  Spear  Sword  Axe 				  Javelins chance
        (call_script,"script_set_items_for_tournament_new",  0,    85,      25,    15,    10,    15,   15,   20, "itm_tourney_helm_red", 10),
      (else_try),#                                         0-100%  0-100%    <-------------- 0-100% ----------->
        (eq,":faction","fac_kingdom_16"),#               Horse  Shield     Club  Staff  Seax  Spear  Sword  Axe 				  Javelins chance
        (call_script,"script_set_items_for_tournament_new",  0,    85,      25,    15,    10,    15,   15,   20, "itm_tourney_helm_red", 10),
      (else_try),#                                         0-100%  0-100%    <-------------- 0-100% ----------->
        (eq,":faction","fac_kingdom_17"),#               Horse  Shield     Club  Staff  Seax  Spear  Sword  Axe 				  Javelins chance
        (call_script,"script_set_items_for_tournament_new",  0,    85,      25,    15,    10,    15,   15,   20, "itm_tourney_helm_red", 10),
      (else_try),#                                         0-100%  0-100%    <-------------- 0-100% ----------->
        (eq,":faction","fac_kingdom_18"),#               Horse  Shield     Club  Staff  Seax  Spear  Sword  Axe 				  Javelins chance
        (call_script,"script_set_items_for_tournament_new",  0,    85,      25,    15,    10,    15,   15,   20, "itm_tourney_helm_red", 10),
      (else_try),#                                         0-100%  0-100%    <-------------- 0-100% ----------->
        (eq,":faction","fac_kingdom_19"),#               Horse  Shield     Club  Staff  Seax  Spear  Sword  Axe 				  Javelins chance
        (call_script,"script_set_items_for_tournament_new",  0,    85,      25,    15,    10,    15,   15,   20, "itm_tourney_helm_red", 10),
      (else_try),#                                         0-100%  0-100%    <-------------- 0-100% ----------->
        (eq,":faction","fac_kingdom_20"),#               Horse  Shield     Club  Staff  Seax  Spear  Sword  Axe 				  Javelins chance
        (call_script,"script_set_items_for_tournament_new",  0,    85,      25,    15,    10,    15,   15,   20, "itm_tourney_helm_red", 10),
      (else_try),#                                         0-100%  0-100%    <-------------- 0-100% ----------->
        (eq,":faction","fac_kingdom_21"),#               Horse  Shield     Club  Staff  Seax  Spear  Sword  Axe 				  Javelins chance
        (call_script,"script_set_items_for_tournament_new",  0,    85,      25,    15,    10,    15,   15,   20, "itm_tourney_helm_red", 10),
      (else_try),
        #                                               0-100%  0-100%    <-------------- 0-100% ----------->
        #                                               Horse  Shield     Club  Staff  Seax  Spear  Sword  Axe 				  Javelins chance
        (call_script,"script_set_items_for_tournament_new",  0,    85,      25,    15,    10,    15,   15,   20, "itm_tourney_helm_red", 10),
        
        #helmets - "itm_tourney_helm_red", "itm_arena_turban_red" or -1 for none
      (try_end),
  ]),
  ("set_items_for_tournament_new",[
      (store_script_param, ":horse_chance", 1),
      (store_script_param, ":shield_chance", 2),
      (store_script_param, ":club_chance", 3),
      (store_script_param, ":staff_chance", 4),
      (store_script_param, ":seax_chance", 5),
      (store_script_param, ":spear_chance", 6),
      (store_script_param, ":sword_chance", 7),
      (store_script_param, ":axe_chance", 8),
      (store_script_param, ":helm_item_begin", 9),
      (store_script_param, ":javelins_chance", 10),
      
      (try_for_range, ":i_ep", 0, 32),
        (mission_tpl_entry_clear_override_items, "mt_arena_melee_fight", ":i_ep"),
        (store_div, ":cur_team", ":i_ep", 8),
        (store_add, ":cur_shield_item", "itm_arena_shield_red", ":cur_team"),
        
        (store_random_in_range,":r",0,100),
        (try_begin),
          (lt,":r",":horse_chance"),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_horse"),
          (assign,":seax_chance",0),
          (val_add,":spear_chance",10),
        (try_end),
        (store_random_in_range,":r",0,100),
        (try_begin),
          (lt,":r",":javelins_chance"),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep","itm_practice_javelin"),
        (try_end),
        
        (store_add,":end",":club_chance",10),
        (val_add,":end",":staff_chance"),
        (val_add,":end",":seax_chance"),
        (val_add,":end",":spear_chance"),
        (val_add,":end",":sword_chance"),
        (val_add,":end",":axe_chance"),
        (store_random_in_range,":r",0,":end"),
        (store_random_in_range,":r_shield",0,100),
        
        (try_begin),
          (is_between,":r",0,":club_chance"),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep","itm_tutorial_spear"),
          (try_begin),#shield
            (lt,":r_shield",":shield_chance"),
            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep",":cur_shield_item"),
          (try_end),
        (else_try),
          (val_add,":staff_chance",":club_chance"),
          (is_between,":r",":club_chance",":staff_chance"),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep","itm_arena_axe"),
          (try_begin),#shield
            (val_sub,":shield_chance",20),
            (lt,":r_shield",":shield_chance"),
            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep",":cur_shield_item"),
          (try_end),
        (else_try),
          (val_add,":seax_chance",":staff_chance"),
          (is_between,":r",":staff_chance",":seax_chance"),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep","itm_tutorial_axe"),
          (try_begin),#shield
            (val_add,":shield_chance",10),#was 10
            (lt,":r_shield",":shield_chance"),
            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep",":cur_shield_item"),
          (try_end),
        (else_try),
          (val_add,":spear_chance",":seax_chance"),
          (is_between,":r",":seax_chance",":spear_chance"),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep","itm_practice_lance"),
          (try_begin),#shield
            (neq,":shield_chance",0),
            (val_add,":shield_chance",30),
            (lt,":r_shield",":shield_chance"),
            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep",":cur_shield_item"),
          (try_end),
        (else_try),
          (val_add,":sword_chance",":spear_chance"),
          (is_between,":r",":spear_chance",":sword_chance"),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep","itm_practice_sword"),
          (try_begin),#shield
            (lt,":r_shield",":shield_chance"),
            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep",":cur_shield_item"),
          (try_end),
        (else_try),
          (val_add,":axe_chance",":sword_chance"),
          (is_between,":r",":sword_chance",":axe_chance"),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep","itm_practice_axe"),
          (try_begin),#shield
            (lt,":r_shield",":shield_chance"),
            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep",":cur_shield_item"),
          (try_end),
        (else_try),#10 for wood stick
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep","itm_tutorial_battle_axe"),
          (try_begin),#shield
            (lt,":r_shield",":shield_chance"),
            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep",":cur_shield_item"),
          (try_end),
        (try_end),
        (store_add, ":cur_armor_item", "itm_arena_armor_red", ":cur_team"),
        (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", ":cur_armor_item"),
        (try_begin),
          (ge, ":helm_item_begin", 0),
          (store_add, ":cur_helm_item", ":helm_item_begin", ":cur_team"),
          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", ":cur_helm_item"),
        (try_end),
      (try_end),
  ]),
  ("cf_get_value_from_array", [
      (store_script_param, ":array", 1),
      
      (troop_get_slot,":num",":array",0),
      (gt,":num",0),
      (store_add,":end",":num",1),
      (store_random_in_range,":random",1,":end"),
      (troop_get_slot,":val",":array",":random"),
      (gt,":val",0),
      (troop_get_slot,":last_val",":array",":num"),
      (troop_set_slot,":array",":random",":last_val"),
      (val_sub,":num",1),
      (troop_set_slot,":array",0,":num"),
      (assign,reg0,":val"),
  ]),
  ("check_if_playername_is_correct", [
      (str_store_troop_name,s2,"$g_player_troop"),
      (try_begin),
        (str_is_empty,s2),
        #(str_store_string,s2,"@Nameless One"),
        (store_random_in_range,":name","str_name_1","str_surname_1"),
        (store_random_in_range,":surname","str_surname_1","str_surnames_end"),
        (str_store_string,s50,":name"),
        (str_store_string,s3,":surname"),
        (str_store_string,s2,"@{!}{s3}"),
        #
        (troop_set_name,"$g_player_troop",s2),
        (party_set_name,"p_main_party",s2),
        #(display_message,"@Player name was auto-set to {s2}"),
      (try_end),
  ]),
  ("cf_is_not_special_troop", [
      (store_script_param,":troop",1),
      (neq,":troop","trp_norse_priest"),
      (neq,":troop","trp_saxon_priest"),
      (neq,":troop","trp_briton_priest"),
      (neq,":troop","trp_scotch_priest"),
      (neq,":troop","trp_scotch_musician"),#no horn for now
      (neq,":troop","trp_angle_priest"),
      (neq,":troop","trp_irish_priest"),
      (neq,":troop","trp_norse_standard_bearer"),
      (neq,":troop","trp_saxon_standard_bearer"),
      (neq,":troop","trp_briton_standard_bearer"),
      (neq,":troop","trp_scotch_standard_bearer"),
      (neq,":troop","trp_angle_standard_bearer"),
      (neq,":troop","trp_irish_standard_bearer"),
  ]),
  ("cf_is_priest", [
      (store_script_param,":troop",1),
      (this_or_next|eq,":troop","trp_norse_priest"),
      (this_or_next|eq,":troop","trp_saxon_priest"),
      (this_or_next|eq,":troop","trp_briton_priest"),
      (this_or_next|eq,":troop","trp_scotch_priest"),
      (this_or_next|eq,":troop","trp_angle_priest"),
      (eq,":troop","trp_irish_priest"),
  ]),
  ("cf_is_standard_bearer", [
      (store_script_param,":troop",1),
      (this_or_next|eq,":troop","trp_norse_standard_bearer"),
      (this_or_next|eq,":troop","trp_saxon_standard_bearer"),
      (this_or_next|eq,":troop","trp_briton_standard_bearer"),
      (this_or_next|eq,":troop","trp_scotch_standard_bearer"),
      (this_or_next|eq,":troop","trp_angle_standard_bearer"),
      (eq,":troop","trp_irish_standard_bearer"),
  ]),
  ("refund_player_forced_team_change", [
      (store_script_param,":player",1),
      
      (player_get_agent_id, ":agent", ":player"),
      (try_begin),
        (ge, ":agent", 0),
        (agent_is_alive, ":agent"),
        
        (player_get_kill_count, ":player_kill_count", ":player"), #adding 1 to his kill count, because he will lose 1 undeserved kill count for dying during team change
        (val_add, ":player_kill_count", 1),
        (player_set_kill_count, ":player", ":player_kill_count"),
        
        (player_get_death_count, ":player_death_count", ":player"), #subtracting 1 to his death count, because he will gain 1 undeserved death count for dying during team change
        (val_sub, ":player_death_count", 1),
        (player_set_death_count, ":player", ":player_death_count"),
        
        (player_get_score, ":player_score", ":player"), #adding 1 to his score count, because he will lose 1 undeserved score for dying during team change
        (val_add, ":player_score", 1),
        (player_set_score, ":player", ":player_score"),
        
        (try_for_players, ":i", 1),
          (multiplayer_send_4_int_to_player, ":i", multiplayer_event_set_player_score_kill_death, ":player", ":player_score", ":player_kill_count", ":player_death_count"),
        (try_end),
        
        (player_get_value_of_original_items, ":old_items_value", ":player"),
        (player_get_gold, ":player_gold", ":player"),
        (val_add, ":player_gold", ":old_items_value"),
        (player_set_gold, ":player", ":player_gold", multi_max_gold_that_can_be_stored),
      (try_end),
  ]),
  ("multi_reset_map", [
      (try_begin),
        (multiplayer_is_server),
        (store_script_param,":player",1),
        (player_is_active,":player"),
        (player_is_admin,":player"),
        (neq,"$g_multiplayer_game_type",multiplayer_game_type_invasion),
        (neq,"$g_multiplayer_game_type",multiplayer_game_type_sea),
        (neq,"$g_multiplayer_game_type",multiplayer_game_type_raid),
        (try_for_agents,":agent"),
          (agent_is_active,":agent"),
          (agent_is_alive,":agent"),
          (agent_deliver_damage_to_agent,":agent",":agent",250),
        (try_end),
        (reset_mission_timer_a),
        (store_mission_timer_a,"$g_round_finish_time"),
        (try_for_range,":team",0,2),
          (team_set_score,":team",0),
          (team_set_bot_kill_count,":team",0),
          (team_set_bot_death_count,":team",0),
        (try_end),
        (try_for_players,":i"),
          (player_is_active,":i"),
          (player_set_kill_count,":i",0),
          (player_set_death_count,":i",0),
          (player_set_score,":i",0),
          (player_set_slot,":i",slot_player_poll_disabled_until_time,0),
          (try_for_players,":r",1),
            (multiplayer_send_4_int_to_player,":r",multiplayer_event_set_player_score_kill_death,":i",0,0,0),
          (try_end),
          (neq,":i",0),
          (multiplayer_send_2_int_to_player,":i",multiplayer_event_set_team_score,0,0),
          (multiplayer_send_int_to_player,":i",multiplayer_event_return_server_mission_timer_while_player_joined,"$g_round_finish_time"),
        (try_end),
        (reset_mission_timer_a),
        (store_mission_timer_a,"$g_round_finish_time"),
        
        (assign,"$g_round_ended",1),
        (try_begin),
          (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_deathmatch),
          (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_team_deathmatch),
          (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_thor),
          (eq, "$g_multiplayer_game_type", multiplayer_game_type_duel),
          (multiplayer_clear_scene),
          (call_script, "script_initialize_objects"),
          (call_script, "script_multiplayer_close_gate_if_it_is_open"),
          (call_script, "script_multiplayer_move_moveable_objects_initial_positions"),
          (call_script, "script_initialize_all_scene_prop_slots"),
        (try_end),
      (try_end),
  ]),
  ("spawn_special_troops",[
      (assign,":archers","$g_presentation_obj_custom_battle_designer_7_last_value"),
      (assign,":infantry","$g_presentation_obj_custom_battle_designer_6_last_value"),
      (assign,":faction","$g_quick_battle_team_1_faction"),
      (assign,":size","$g_quick_battle_army_1_size"),
      (try_for_range,":try",0,2),
        (try_begin),
          (is_between,":faction",cb_factions_begin,cb_factions_end),
          (call_script,"script_get_army_size_from_slider_value",":size"),
          (assign, ":army_size", reg0),
          (val_mul,":infantry",":army_size"),
          (val_div,":infantry",10000),#1%
          (val_add, ":infantry", 1),
          (val_mul,":archers",":army_size"),
          (assign, ":orig_archers", ":archers"),
          (val_div,":archers",10000),#1%
          (val_add, ":archers", 1),
          
          (try_begin),
            (eq,":faction","fac_culture_norse"),
            (assign,":priest","trp_norse_priest"),
            (assign,":flag","trp_norse_standard_bearer"),
          (else_try),
            (eq,":faction","fac_culture_saxon"),
            (assign,":priest","trp_saxon_priest"),
            (assign,":flag","trp_saxon_standard_bearer"),
          (else_try),
            (eq,":faction","fac_culture_welsh"),
            (assign,":priest","trp_briton_priest"),
            (assign,":flag","trp_briton_standard_bearer"),
          (else_try),
            (eq,":faction","fac_culture_scotch"),
            (assign,":priest","trp_scotch_priest"),
            (assign,":flag","trp_scotch_standard_bearer"),
          (else_try),
            (eq,":faction","fac_culture_angle"),
            (assign,":priest","trp_angle_priest"),
            (assign,":flag","trp_angle_standard_bearer"),
          (else_try),
            (eq,":faction","fac_culture_irish"),
            (assign,":priest","trp_irish_priest"),
            (assign,":flag","trp_irish_standard_bearer"),
          (try_end),
          
          (store_mul,":entry",":try",16),
          (try_begin),
            (gt,":infantry",0),
            (gt,":flag",0),
            (add_visitors_to_current_scene,":entry",":flag",":infantry",0,0),
          (try_end),
          (try_begin),
            (neq, ":orig_archers", 0),	#lone priest leads to AI problems
            (gt,":archers",0),
            (gt,":priest",0),
            (val_add,":entry",1),
            (add_visitors_to_current_scene,":entry",":priest",":archers",0,0),
          (try_end),
        (try_end),
        
        (assign,":archers","$g_presentation_obj_custom_battle_designer_10_last_value"),
        (assign,":infantry","$g_presentation_obj_custom_battle_designer_9_last_value"),
        (assign,":faction","$g_quick_battle_team_2_faction"),
        (assign,":size","$g_quick_battle_army_2_size"),
      (try_end),
  ]),
  ("special_troop_trigger",[
      (try_for_agents,":i"),
        (agent_is_alive,":i"),
        (agent_is_human,":i"),
        (agent_set_slot,":i",slot_agent_banner_bonus,0),###reset bonus for all
      (try_end),
      (try_for_agents,":agent"),
        (agent_is_alive,":agent"),
        (agent_is_human,":agent"),
        (agent_get_troop_id,":troop",":agent"),
        (set_fixed_point_multiplier, 100),
        (try_begin),
          (call_script,"script_cf_is_standard_bearer",":troop"),
          (agent_get_position,pos1,":agent"),
          (agent_get_team,":team",":agent"),
          (agent_set_slot,":agent",slot_agent_banner_bonus,1),
          
          (try_for_agents,":i",pos1,700),
            (agent_is_alive,":i"),
            (agent_is_human,":i"),
            (neq,":i",":agent"),
            (agent_get_team,":i_team",":i"),
            (eq,":team",":i_team"),
            (agent_set_slot,":i",slot_agent_banner_bonus,1),###agent is near banner
          (try_end),
        (else_try),
          (call_script,"script_cf_is_priest",":troop"),
          (agent_get_position,pos1,":agent"),
          (agent_get_team,":team",":agent"),
          (try_for_agents,":i",pos1,700),
            (agent_is_alive,":i"),
            (agent_is_human,":i"),
            (neq,":i",":agent"),
            (agent_get_team,":team",":i"),
            (eq,":team",":i_team"),
            (store_agent_hit_points,":hp",":i",0),
            (lt,":hp",100),
            (store_agent_hit_points,":hp",":i",1),
            (val_add,":hp",2),
            (agent_set_hit_points,":i",":hp",1),
          (try_end),
        (try_end),
      (try_end),
      
      (try_for_agents,":agent"),
        (agent_is_alive,":agent"),
        (agent_is_human,":agent"),
        (agent_slot_eq,":agent",slot_agent_berserk_cooldown,0),###no boost for berserker
        (try_begin),
          (agent_slot_eq,":agent",slot_agent_banner_bonus,0),
          (try_begin),
            (agent_slot_eq,":agent",slot_agent_banner_bonus_applied,1),
            ####reset the bonus
            (agent_set_damage_modifier,":agent",100),
            (call_script, "script_advanced_agent_set_speed_modifier",":agent",100),
            (agent_set_accuracy_modifier,":agent",100),
            (agent_set_reload_speed_modifier,":agent",100),
            ####
            (agent_set_slot,":agent",slot_agent_banner_bonus_applied,0),
          (try_end),
        (else_try),
          (agent_slot_eq,":agent",slot_agent_banner_bonus,1),
          (try_begin),
            (agent_slot_eq,":agent",slot_agent_banner_bonus_applied,0),
            ####apply the bonus
            (agent_set_damage_modifier,":agent",110),
            (call_script, "script_advanced_agent_set_speed_modifier",":agent",110),
            (agent_set_accuracy_modifier,":agent",110),
            (agent_set_reload_speed_modifier,":agent",110),
            ####
            (agent_set_slot,":agent",slot_agent_banner_bonus_applied,1),
          (try_end),
        (try_end),
      (try_end),
  ]),
  ("item_confict_check",[
      (store_script_param,":agent",1),
      (try_begin),
        (agent_is_alive,":agent"),
        
        (agent_get_item_slot,":body",":agent",ek_body),
        
        (try_begin),#check armor overwriting boots and helmet
          (gt, ":body", itm_no_item),
          (try_begin),
            (item_has_property, ":body", itp_replaces_helm),
            (agent_get_item_slot,":helm",":agent",ek_head),
            (gt, ":helm", itm_no_item),
            (agent_unequip_item, ":agent", ":helm", ek_head),
            (agent_get_troop_id, ":troop_no", ":agent"),
            (this_or_next|eq, ":troop_no", "trp_player"),
            (is_between, ":troop_no", companions_begin, companions_end),
            (str_store_troop_name, s0, ":troop_no"),
            (display_message, "@Head armor cannot be used with hoods and is being discarded for {s0}."),
          (try_end),
        (try_end),
      (try_end),
  ]),
  ("lbt_get_troop_cost_to_reg1",[
      (store_script_param,":troop",1),
      
      (store_character_level,":troop_level",":troop"),
      (try_begin),
        # (call_script,"script_cf_is_priest",":troop"),
        # (assign,":cost",50),#basic cost
        # (else_try),
        # (le,":troop_level",12),
        # (assign,":cost",30),#basic cost
        # (else_try),
        (assign,":cost",150),#basic cost
      (try_end),
      
      (troop_get_inventory_slot,":has_horse",":troop",ek_horse),
      (try_begin),
        (ge,":has_horse",0),
        (val_add,":cost",100),#50
      (try_end),
      
      (try_begin),
        (gt,":troop_level",28),
        (val_add,":cost",300),#150
      (else_try),
        (gt,":troop_level",27),
        (val_add,":cost",250),#120
      (else_try),
        (gt,":troop_level",26),
        (val_add,":cost",200),#90
      (else_try),
        (gt,":troop_level",25),
        (val_add,":cost",150),#70
      (else_try),
        (gt,":troop_level",21),
        (val_add,":cost",100),#50
      (try_end),
      
      (assign,reg1,":cost"),
  ]),
  ("cf_lbt_skip_weak_infantry_troops",[
      (store_script_param,":troop",1),
      # (call_script,"script_lbt_get_troop_cost_to_reg1",":troop"),
      # (assign,":cost",reg1),
      # (this_or_next|gt,":cost",50),
      
      (store_character_level,":troop_level",":troop"),
      (gt,":troop_level",12),#no lowest level troops
      (this_or_next|gt,":troop_level",18),
      (this_or_next|troop_is_guarantee_horse,":troop"),
      (troop_is_guarantee_ranged,":troop"),#no low level non-archer troops
  ]),
  ("reset_bonus_effect",[
      (store_script_param,":agent",1),
      (try_begin),
        (agent_slot_eq,":agent",slot_agent_horn_bonus_applied,0),
        (agent_slot_eq,":agent",slot_agent_banner_bonus_applied,0),
        (agent_set_damage_modifier,":agent",100),
        (call_script, "script_advanced_agent_set_speed_modifier",":agent",100),
        (agent_set_accuracy_modifier,":agent",100),
        (agent_set_reload_speed_modifier,":agent",100),
        (agent_set_ranged_damage_modifier,":agent",100),
      (else_try),
        (agent_slot_eq,":agent",slot_agent_horn_bonus_applied,1), #double bonus = 15%
        (agent_slot_eq,":agent",slot_agent_banner_bonus_applied,1),
        (agent_set_damage_modifier,":agent",115),
        (call_script, "script_advanced_agent_set_speed_modifier",":agent",115),
        (agent_set_accuracy_modifier,":agent",115),
        (agent_set_reload_speed_modifier,":agent",115),
        (agent_set_ranged_damage_modifier,":agent",115),
      (else_try),
        (this_or_next|agent_slot_eq,":agent",slot_agent_horn_bonus_applied,1),#single bonus = 10%
        (agent_slot_eq,":agent",slot_agent_banner_bonus_applied,1),
        (agent_set_damage_modifier,":agent",110),
        (call_script, "script_advanced_agent_set_speed_modifier",":agent",110),
        (agent_set_accuracy_modifier,":agent",110),
        (agent_set_reload_speed_modifier,":agent",110),
        (agent_set_ranged_damage_modifier,":agent",110),
      (try_end),
  ]),
  ("inv_commander_selected_class",[
      (store_script_param,":object",1),
      (store_sub,":obj",":object","$g_multiplayer_invasion_order_classes"),
      (val_div,":obj",2),
      
      (try_for_range,":try",0,4),
        (store_mul,":class_select",":try",2),
        (val_add,":class_select","$g_multiplayer_invasion_order_classes"),
        (overlay_set_color,":class_select",0xFF000000),
        (overlay_set_alpha,":class_select",0xaa),
      (try_end),
      
      (try_begin),
        (eq,":obj",0),
        (multiplayer_send_2_int_to_server, multiplayer_event_class_orders, me_class_order_select, grc_everyone),
        (assign,"$g_multiplayer_invasion_order_selected_class",9),
        (overlay_set_color,":object",0xFFddd466),
        (overlay_set_alpha,":object",0x55),
      (else_try),
        (is_between,":obj",1,4),
        (val_sub,":obj",1),
        (multiplayer_send_2_int_to_server, multiplayer_event_class_orders, me_class_order_select, ":obj"),
        (assign,"$g_multiplayer_invasion_order_selected_class",":obj"),
        (overlay_set_color,":object",0xFFddd466),
        (overlay_set_alpha,":object",0x55),
      (try_end),
      
      (overlay_set_display,"$g_multiplayer_invasion_order_weapons",1),
      (overlay_set_display,"$g_multiplayer_invasion_order_move",1),
      (store_sub,":obj","$g_multiplayer_invasion_order_classes",1),
      (overlay_set_display,":obj",1),
      (val_sub,":obj",1),
      (overlay_set_display,":obj",1),
  ]),
  ("mp_set_6_items_class",[
      (store_script_param,":class",1),
      (store_script_param,reg1,2),
      (store_script_param,reg2,3),
      (store_script_param,reg3,4),
      (store_script_param,reg4,5),
      (store_script_param,reg5,6),
      (store_script_param,reg6,7),
    (try_begin),(gt,reg1,0),(item_set_slot,reg1,slot_item_multiplayer_item_class,":class"),(try_end),
    (try_begin),(gt,reg2,0),(item_set_slot,reg2,slot_item_multiplayer_item_class,":class"),(try_end),
    (try_begin),(gt,reg3,0),(item_set_slot,reg3,slot_item_multiplayer_item_class,":class"),(try_end),
    (try_begin),(gt,reg4,0),(item_set_slot,reg4,slot_item_multiplayer_item_class,":class"),(try_end),
    (try_begin),(gt,reg5,0),(item_set_slot,reg5,slot_item_multiplayer_item_class,":class"),(try_end),
    (try_begin),(gt,reg6,0),(item_set_slot,reg6,slot_item_multiplayer_item_class,":class"),(try_end),
  ]),
  ("mp_assign_6_equipment",[
      (store_script_param,reg1,1),
      (store_script_param,reg2,2),
      (store_script_param,reg3,3),
      (store_script_param,reg4,4),
      (store_script_param,reg5,5),
      (store_script_param,reg6,6),
      (call_script,"script_multiplayer_set_item_available_for_troop",reg1,"$temp"),
      (call_script,"script_multiplayer_set_item_available_for_troop",reg2,"$temp"),
      (call_script,"script_multiplayer_set_item_available_for_troop",reg3,"$temp"),
      (call_script,"script_multiplayer_set_item_available_for_troop",reg4,"$temp"),
      (call_script,"script_multiplayer_set_item_available_for_troop",reg5,"$temp"),
      (call_script,"script_multiplayer_set_item_available_for_troop",reg6,"$temp"),
  ]),
  ("mp_assign_troop_equipment",[
      #(call_script,"script_multiplayer_set_item_available_for_troop", , ),
      
      (item_set_slot,"itm_carbatinae_3",slot_item_multiplayer_item_class,multi_item_class_type_light_foot),
      (item_set_slot,"itm_carbatinae_4",slot_item_multiplayer_item_class,multi_item_class_type_light_foot),
      (item_set_slot,"itm_carbatinae_4s",slot_item_multiplayer_item_class,multi_item_class_type_light_foot),
      (item_set_slot,"itm_carbatinae_5s",slot_item_multiplayer_item_class,multi_item_class_type_light_foot),
      (item_set_slot,"itm_carbatinae_5v",slot_item_multiplayer_item_class,multi_item_class_type_light_foot),
      (item_set_slot,"itm_carbatinae_8",slot_item_multiplayer_item_class,multi_item_class_type_light_foot),
      (item_set_slot,"itm_carbatinae_11q",slot_item_multiplayer_item_class,multi_item_class_type_light_foot),
      (item_set_slot,"itm_carbatinae_vc2s",slot_item_multiplayer_item_class,multi_item_class_type_light_foot),
      (item_set_slot,"itm_carbatinae_vc3",slot_item_multiplayer_item_class,multi_item_class_type_light_foot),
      (item_set_slot,"itm_carbatinae_vc6",slot_item_multiplayer_item_class,multi_item_class_type_light_foot),
      (item_set_slot,"itm_just_man_shoes",slot_item_multiplayer_item_class,multi_item_class_type_light_foot),
      (item_set_slot,"itm_bare_foot_man",slot_item_multiplayer_item_class,multi_item_class_type_light_foot),
      
      (item_set_slot,"itm_briton_tunic1",slot_item_multiplayer_item_class,multi_item_class_type_light_armor),
      (item_set_slot,"itm_briton_tunic7",slot_item_multiplayer_item_class,multi_item_class_type_light_armor),
      (item_set_slot,"itm_gael_tunic_02",slot_item_multiplayer_item_class,multi_item_class_type_light_armor),
      (item_set_slot,"itm_gael_tunic_07",slot_item_multiplayer_item_class,multi_item_class_type_light_armor),
      (item_set_slot,"itm_picts_tunic_09",slot_item_multiplayer_item_class,multi_item_class_type_light_armor),
      (item_set_slot,"itm_picts_tunic_10",slot_item_multiplayer_item_class,multi_item_class_type_light_armor),
      (item_set_slot,"itm_picts_tunic_11",slot_item_multiplayer_item_class,multi_item_class_type_light_armor),
      
      (item_set_slot, "itm_crossbow_mp", slot_item_multiplayer_item_class, multi_item_class_type_bow),
      (item_set_slot, "itm_bolts_mp", slot_item_multiplayer_item_class, multi_item_class_type_bow),
      
      #norse
      (call_script,"script_mp_set_6_items_class",multi_item_class_type_light_armor,"itm_btunic_12","itm_btunic_15","itm_btunic_16",0,0,0),#light armor (tunic reforced)
      (call_script,"script_mp_set_6_items_class",multi_item_class_type_heavy_armor,"itm_addon_mail4","itm_addon_mail7",0,0,0,0),#animal mail
      (call_script,"script_mp_set_6_items_class",multi_item_class_type_heavy_armor,"itm_byrnie16","itm_byrnie17","itm_byrnie18","itm_byrnie19","itm_byrnie31","itm_byrnie32"),#mail
      (call_script,"script_mp_set_6_items_class",multi_item_class_type_medium_armor,"itm_gambeson25","itm_gambeson27","itm_gambeson29","itm_gambeson4","itm_gambeson35","itm_gambeson43"),#viking gambeson
      (call_script,"script_mp_set_6_items_class",multi_item_class_type_light_armor,"itm_btunic_8","itm_btunic_9","itm_btunic_3","itm_btunic_4","itm_btunic_13","itm_btunic_14"),#Tunics common
      #saxon
      (call_script,"script_mp_set_6_items_class",multi_item_class_type_light_armor,"itm_bl_tunic02","itm_bl_tunic03","itm_bl_tunic09","itm_nobleman_outfit",0,0),#lightarmor
      (call_script,"script_mp_set_6_items_class",multi_item_class_type_heavy_armor,"itm_mail_shirt_13_4","itm_mail_shirt_13_3","itm_byrnie5","itm_byrnie21","itm_byrnie22","itm_mail_shirt_13_2"),#mail
      (call_script,"script_mp_set_6_items_class",multi_item_class_type_medium_armor,"itm_gambeson1","itm_gambeson2","itm_gambeson3","itm_gambeson32","itm_gambeson6",0),#short gambeson
      (item_set_slot,"itm_red_cloak",slot_item_multiplayer_item_class,multi_item_class_type_light_armor),#tunics
      (call_script,"script_mp_set_6_items_class",multi_item_class_type_light_armor,"itm_bl_tunic06","itm_bl_tunic07","itm_bl_tunic08","itm_bl_tunic10","itm_bl_tunic11","itm_bl_tunic12"),#tunics
      #angle
      (call_script,"script_mp_set_6_items_class",multi_item_class_type_light_armor,"itm_ptunic_2","itm_ptunic_9","itm_ptunic_12","itm_btunic_2woman","itm_btunic_7woman",0),#lightarmor
      (call_script,"script_mp_set_6_items_class",multi_item_class_type_heavy_armor,"itm_byrnie23","itm_mail_shirt_5_2","itm_byrnie25","itm_byrnie26","itm_byrnie29",0),##long mail
      (call_script,"script_mp_set_6_items_class",multi_item_class_type_medium_armor,"itm_gambeson26","itm_gambeson28","itm_gambeson34","itm_gambeson39",0,0),#gambeson
      (call_script,"script_mp_set_6_items_class",multi_item_class_type_light_armor,"itm_gael_tunic_03","itm_ptunic_6","itm_ptunic_7","itm_ptunic_8","itm_ptunic_10","itm_ptunic_11"),#tunic
      #briton
      (call_script,"script_mp_set_6_items_class",multi_item_class_type_light_armor,"itm_picts_tunic_12","itm_briton_tunic8",0,0,0,0),#lightarmor
      (call_script,"script_mp_set_6_items_class",multi_item_class_type_heavy_armor,"itm_mail_shirt_5_1","itm_byrnie4","itm_byrnie6","itm_byrnie13","itm_byrnie14","itm_byrnie15"),#mail
      (call_script,"script_mp_set_6_items_class",multi_item_class_type_medium_armor,"itm_gambeson36","itm_gambeson37","itm_gambeson38","itm_gambeson40","itm_gambeson41","itm_gambeson42"),#gambeson
      (call_script,"script_mp_set_6_items_class",multi_item_class_type_light_armor,"itm_briton_tunic13","itm_briton_tunic5","itm_briton_tunic4","itm_briton_tunic3","itm_leather_cloak","itm_blue_cloak"),#tunics
      #irish
      (call_script,"script_mp_set_6_items_class",multi_item_class_type_light_armor,"itm_brat3","itm_brat4",0,0,0,0),#lightarmor
      (call_script,"script_mp_set_6_items_class",multi_item_class_type_heavy_armor,"itm_byrnie9","itm_byrnie10","itm_byrnie36","itm_byrnie37","itm_byrnie38",0),##long mail
      (call_script,"script_mp_set_6_items_class",multi_item_class_type_medium_armor,"itm_gambeson12gael","itm_gambeson13gael","itm_gambeson14gael","itm_gambeson15gael","itm_gambeson16gael",0),#gambeson
      (call_script,"script_mp_set_6_items_class",multi_item_class_type_light_armor,"itm_gael_tunic_08","itm_gael_hoodtunic_09","itm_gael_hoodtunic_10",0,0,0),#hood tunic
      (call_script,"script_mp_set_6_items_class",multi_item_class_type_light_armor,"itm_briton_tunic24","itm_briton_tunic25","itm_briton_tunic26","itm_briton_tunic27","itm_gael_hoodtunic_11",0),#tunic
      #acotch
      (call_script,"script_mp_set_6_items_class",multi_item_class_type_light_armor,"itm_pictish_painted1","itm_pictish_painted2","itm_pictish_painted3","itm_pictish_painted4","itm_picts_hoodtunic_01",0),#hood tunics
      (call_script,"script_mp_set_6_items_class",multi_item_class_type_light_armor,"itm_picts_hoodtunic_15","itm_picts_hoodtunic_16","itm_picts_hoodtunic_14","itm_picts_hoodtunic_17",0,0),#hood tunic
      (call_script,"script_mp_set_6_items_class",multi_item_class_type_light_armor,"itm_picts_hoodtunic_11","itm_picts_hoodtunic_12","itm_briton_tunic18","itm_briton_tunic19","itm_picts_hoodtunic_13",0),#tunic
      (call_script,"script_mp_set_6_items_class",multi_item_class_type_heavy_armor,"itm_mail_shirt_6","itm_mail_shirt_7","itm_mail_shirt_11_3","itm_mail_shirt_2","itm_mail_shirt_5",0),#mail
      (call_script,"script_mp_set_6_items_class",multi_item_class_type_medium_armor,"itm_gambeson1cloak","itm_gambeson1gael","itm_gambeson2gael","itm_gambeson3gael","itm_gambeson4gael",0),#gambeson
      (call_script,"script_mp_set_6_items_class",multi_item_class_type_light_armor,"itm_pictish_painted1","itm_pictish_painted2","itm_pictish_painted3","itm_pictish_painted4","itm_picts_hoodtunic_01",0),#naked
      (call_script,"script_mp_set_6_items_class",multi_item_class_type_light_armor,"itm_picts_hoodtunic_03","itm_picts_hoodtunic_04","itm_picts_hoodtunic_05","itm_picts_hoodtunic_06",0,0),#hood naked
      
      
      (try_for_range,":item","itm_hatchet","itm_long_axe_b"),
        (item_set_slot,":item",slot_item_multiplayer_item_class,multi_item_class_type_axe),
      (try_end),
      (try_for_range,":item","itm_knife","itm_ragnar_seax"),
        (item_set_slot, ":item", slot_item_multiplayer_item_class, multi_item_class_type_sword),
      (try_end),
      ####MP RAID peasants
      
      (assign,"$temp","trp_mp_norse_peasant"),
      (call_script,"script_mp_assign_6_equipment","itm_carbatinae_vc2","itm_carbatinae_6","itm_carbatinae_vc1","itm_carbatinae_vc2s","itm_carbatinae_vc1v",0),
      (call_script,"script_mp_assign_6_equipment","itm_btunic_8","itm_btunic_9","itm_btunic_3","itm_btunic_4","itm_btunic_13",0),#Tunics common
      (call_script,"script_mp_assign_6_equipment","itm_phrygian1","itm_phrygian2","itm_phrygian3",0,0,0),
      
      
      (assign,"$temp","trp_mp_saxon_peasant"),
      (call_script,"script_mp_assign_6_equipment","itm_carbatinae_5s","itm_carbatinae_vc3","itm_carbatinae_4s","itm_carbatinae_vc6","itm_carbatinae_vc2s",0),
      (call_script,"script_mp_assign_6_equipment","itm_bl_tunic06","itm_bl_tunic07","itm_bl_tunic08","itm_bl_tunic10","itm_bl_tunic11","itm_bl_tunic12"),#tunics
      (call_script,"script_mp_assign_6_equipment","itm_phrygian4","itm_phrygian5","itm_phrygian6",0,0,0),
      
      
      (assign,"$temp","trp_mp_angle_peasant"),
      (call_script,"script_mp_assign_6_equipment","itm_carbatinae_5v","itm_carbatinae_1s","itm_carbatinae_10","itm_carbatinae_6","itm_carbatinae_4s","itm_carbatinae_5s"),
      (call_script,"script_mp_assign_6_equipment","itm_gael_tunic_03","itm_ptunic_6","itm_ptunic_7","itm_ptunic_8","itm_ptunic_10","itm_ptunic_11"),#tunic
      (call_script,"script_mp_assign_6_equipment","itm_phrygian5","itm_phrygian6","itm_phrygian7",0,0,0),
      
      
      (assign,"$temp","trp_mp_briton_peasant"),
      (call_script,"script_mp_assign_6_equipment","itm_carbatinae_1","itm_carbatinae_3","itm_carbatinae_4","itm_carbatinae_8","itm_carbatinae_5s",0),
      (call_script,"script_mp_assign_6_equipment","itm_briton_tunic13","itm_briton_tunic5","itm_briton_tunic4","itm_briton_tunic3","itm_leather_cloak","itm_blue_cloak"),#tunics
      (call_script,"script_mp_assign_6_equipment","itm_phrygian1","itm_phrygian2","itm_phrygian3",0,0,0),
      
      (assign,"$temp","trp_mp_irish_peasant"),
      (call_script,"script_mp_assign_6_equipment","itm_gaelshoes_2","itm_just_man_boots_medium","itm_bare_foot_man","itm_just_man_boots_dark",0,0),
      (call_script,"script_mp_assign_6_equipment","itm_gael_tunic_08","itm_gael_hoodtunic_09","itm_gael_hoodtunic_10",0,0,0),#hood tunic
      (call_script,"script_mp_assign_6_equipment","itm_briton_tunic24","itm_briton_tunic25","itm_briton_tunic26","itm_briton_tunic27","itm_gael_hoodtunic_11",0),#tunic
      (call_script,"script_mp_assign_6_equipment","itm_phrygian4","itm_phrygian9","itm_phrygian14",0,0,0),
      
      (assign,"$temp","trp_mp_scotch_peasant"),
      (call_script,"script_mp_assign_6_equipment","itm_just_man_boots_medium","itm_just_man_boots_light","itm_bare_foot_man","itm_just_man_boots_dark","itm_carbatinae_12q",0),
      (call_script,"script_mp_assign_6_equipment","itm_picts_hoodtunic_15","itm_picts_hoodtunic_16","itm_picts_hoodtunic_14","itm_picts_hoodtunic_17",0,0),#hood tunic
      (call_script,"script_mp_assign_6_equipment","itm_picts_hoodtunic_11","itm_picts_hoodtunic_12","itm_briton_tunic18","itm_briton_tunic17","itm_picts_hoodtunic_13",0),#tunic
      (call_script,"script_mp_assign_6_equipment","itm_pictish_painted1","itm_pictish_painted2","itm_pictish_painted3",0,"itm_picts_hoodtunic_01",0),#naked
      #(call_script,"script_mp_assign_6_equipment","itm_picts_hoodtunic_03","itm_picts_hoodtunic_04","itm_picts_hoodtunic_05","itm_picts_hoodtunic_06",0,0),#hood naked
      (call_script,"script_mp_assign_6_equipment","itm_phrygian8","itm_phrygian11","itm_phrygian15",0,0,0),
      
      (try_for_range,":slot",slot_item_multiplayer_faction_price_multipliers_begin,slot_item_multiplayer_faction_price_multipliers_begin+10),
        (item_set_slot,"itm_pitch_fork",":slot",1000),
        (item_set_slot,"itm_battle_fork",":slot",1000),
        (item_set_slot,"itm_stones_mp",":slot",10000),
      (try_end),
      
      (item_set_slot, "itm_pickaxe_mp", slot_item_multiplayer_item_class, multi_item_class_type_axe),
      (item_set_slot, "itm_work_axe_mp", slot_item_multiplayer_item_class, multi_item_class_type_axe),
      
      (item_set_slot, "itm_seax_1_mp", slot_item_multiplayer_item_class, multi_item_class_type_sword),
      (item_set_slot, "itm_spear_1_mp", slot_item_multiplayer_item_class, multi_item_class_type_spear),
      (item_set_slot, "itm_pitch_fork", slot_item_multiplayer_item_class, multi_item_class_type_spear),
      (item_set_slot, "itm_battle_fork", slot_item_multiplayer_item_class, multi_item_class_type_spear),
      (item_set_slot, "itm_stones_mp", slot_item_multiplayer_item_class, multi_item_class_type_throwing),
      (try_for_range,":troop",multiplayer_peasant_troops_begin,multiplayer_peasant_troops_end),
        (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wooden_stick", ":troop"),
        (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pitch_fork", ":troop"),
        (call_script, "script_multiplayer_set_item_available_for_troop", "itm_battle_fork", ":troop"),
        (call_script, "script_multiplayer_set_item_available_for_troop", "itm_stones_mp", ":troop"),
        (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pickaxe_mp", ":troop"),
        (call_script, "script_multiplayer_set_item_available_for_troop", "itm_work_axe_mp", ":troop"),
        (call_script, "script_multiplayer_set_item_available_for_troop", "itm_seax_1_mp", ":troop"),
        (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_1_mp", ":troop"),
      (try_end),
      
      #####
      #####MP Classes
      ###NORSE
      #infantry
      (assign,"$temp","trp_mp_norse_infantry"),
      (call_script,"script_mp_assign_6_equipment","itm_horn_multi","itm_standard",0,0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_seax_1","itm_longseax6",0,0,"itm_sword_5",0),#"itm_longseax7"#"itm_sword_6"
      (call_script,"script_mp_assign_6_equipment","itm_wooden_stick","itm_axe_3","itm_hand_axe","itm_one_handed_war_axe_a",0,0),#"itm_axe_4"
      #(call_script,"script_mp_assign_6_equipment","itm_carbatinae_14qs","itm_carbatinae_vc1v","itm_carbatinae_2s","itm_carbatinae_6v","itm_carbatinae_5",0),
      # (call_script,"script_mp_assign_6_equipment","itm_carbatinae_6","itm_carbatinae_vc1","itm_carbatinae_vc2","itm_carbatinae_vc1v","itm_carbatinae_vc2s",0),
      # (call_script,"script_mp_assign_6_equipment","itm_carbatinae_2s","itm_carbatinae_6v","itm_carbatinae_5","itm_carbatinae_14qs",0,0),
      (call_script,"script_mp_assign_6_equipment","itm_carbatinae_6","itm_carbatinae_vc1",0,"itm_carbatinae_vc1v","itm_carbatinae_5","itm_carbatinae_14qs"),
      (call_script,"script_mp_assign_6_equipment","itm_leather_gloves",0,0,0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_btunic_12","itm_btunic_15","itm_btunic_16",0,0,0),#light armor (tunic reforced)
      (call_script,"script_mp_assign_6_equipment","itm_addon_mail4","itm_addon_mail7",0,0,0,0),#animal mail
      (call_script,"script_mp_assign_6_equipment","itm_byrnie16","itm_byrnie17","itm_byrnie18","itm_byrnie19","itm_byrnie31","itm_byrnie32"),#mail
      (call_script,"script_mp_assign_6_equipment","itm_gambeson25","itm_gambeson27","itm_gambeson29","itm_gambeson4","itm_gambeson35","itm_gambeson43"),#viking gambeson
      (call_script,"script_mp_assign_6_equipment","itm_btunic_8","itm_btunic_9","itm_btunic_3","itm_btunic_4","itm_btunic_13","itm_btunic_14"),#Tunics common
      # (call_script,"script_mp_assign_6_equipment","itm_btunic_11","itm_btunic_13","itm_btunic_15",0,0,0),
      # (call_script,"script_mp_assign_6_equipment","itm_gambeson29","itm_mail_shirt_2","itm_byrnie16","itm_byrnie17",0,0),
      (call_script,"script_mp_assign_6_equipment","itm_viking_shield_round_01","itm_viking_shield_round_02","itm_viking_shield_round_03","itm_viking_shield_round_04","itm_tab_shield_round_01_device",0),
      (call_script,"script_mp_assign_6_equipment","itm_quarter_staff","itm_staff","itm_light_spear1","itm_war_spear1","itm_heavy_spear1",0),
      (call_script,"script_mp_assign_6_equipment","itm_stones","itm_throwing_spears",0,0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_phrygian15","itm_phrygian16","itm_phrygian17",0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_vikingold_helm15","itm_viking_elitehelm1","itm_viking_helm15","itm_viking_elitehelm2","itm_viking_helm16","itm_viking_noblehelm1"),
      #archer
      (assign,"$temp","trp_mp_norse_archer"),
      # (call_script,"script_mp_assign_6_equipment","itm_wooden_stick","itm_seax_1","itm_longseax7","itm_hatchet","itm_axe",0),
      # (call_script,"script_mp_assign_6_equipment","itm_hand_axe","itm_new_sword3",0,0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_seax_1","itm_longseax6",0,0,"itm_sword_5",0),#"itm_longseax7"#"itm_sword_6"
      (call_script,"script_mp_assign_6_equipment","itm_wooden_stick","itm_axe_3","itm_hand_axe","itm_one_handed_war_axe_a",0,0),#"itm_axe_4"
      (call_script,"script_mp_assign_6_equipment","itm_carbatinae_vc2","itm_carbatinae_6","itm_carbatinae_vc1","itm_carbatinae_vc2s","itm_carbatinae_vc1v",0),
      (call_script,"script_mp_assign_6_equipment","itm_btunic_12","itm_btunic_15","itm_btunic_16",0,0,0),#light armor (tunic reforced)
      #(call_script,"script_mp_assign_6_equipment","itm_addon_mail4","itm_addon_mail7",0,0,0,0),#animal mail
      #(call_script,"script_mp_assign_6_equipment","itm_byrnie16","itm_byrnie17","itm_byrnie18","itm_byrnie19","itm_byrnie31","itm_byrnie32"),#mail
      #(call_script,"script_mp_assign_6_equipment","itm_gambeson25","itm_gambeson27","itm_gambeson29","itm_gambeson4","itm_gambeson35","itm_gambeson43"),#viking gambeson
      (call_script,"script_mp_assign_6_equipment","itm_btunic_8","itm_btunic_9","itm_btunic_3","itm_btunic_4","itm_btunic_13","itm_btunic_14"),#Tunics common
      # (call_script,"script_mp_assign_6_equipment","itm_btunic_1","itm_btunic_2","itm_btunic_3",0,0,0),
      # (call_script,"script_mp_assign_6_equipment","itm_gambeson5","itm_gambeson8","itm_gambeson7",0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_wooden_stick","itm_staff","itm_pitch_fork",0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_stones","itm_long_bow2","itm_long_bow","itm_arrows",0,0),
      (call_script,"script_mp_assign_6_equipment","itm_phrygian1","itm_phrygian2","itm_phrygian3",0,0,0),
      #cavalry
      (assign,"$temp","trp_mp_norse_cavalry"),
      (call_script,"script_mp_assign_6_equipment","itm_horn_multi","itm_standard",0,0,0,0),
      # (call_script,"script_mp_assign_6_equipment","itm_wooden_stick","itm_seax_1","itm_longseax8","itm_longseax9","itm_one_handed_war_axe_c",0),
      # (call_script,"script_mp_assign_6_equipment","itm_hand_axe","itm_sword_7","itm_sword_8","itm_sword",0,0),
      (call_script,"script_mp_assign_6_equipment","itm_seax_1","itm_longseax6",0,0,"itm_sword_5",0),#"itm_longseax7"#"itm_sword_6"
      (call_script,"script_mp_assign_6_equipment","itm_wooden_stick","itm_axe_3","itm_hand_axe","itm_one_handed_war_axe_a",0,0),#"itm_axe_4"
      #(call_script,"script_mp_assign_6_equipment","itm_carbatinae_14qs","itm_carbatinae_vc1v","itm_carbatinae_2s","itm_carbatinae_6v","itm_carbatinae_5",0),
      (call_script,"script_mp_assign_6_equipment","itm_carbatinae_6","itm_carbatinae_vc1",0,"itm_carbatinae_vc1v","itm_carbatinae_5","itm_carbatinae_14qs"),
      (call_script,"script_mp_assign_6_equipment","itm_leather_gloves",0,0,0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_btunic_12","itm_btunic_15","itm_btunic_16",0,0,0),#light armor (tunic reforced)
      #(call_script,"script_mp_assign_6_equipment","itm_addon_mail4","itm_addon_mail7",0,0,0,0),#animal mail
      #(call_script,"script_mp_assign_6_equipment","itm_byrnie16","itm_byrnie17","itm_byrnie18","itm_byrnie19","itm_byrnie31","itm_byrnie32"),#mail
      (call_script,"script_mp_assign_6_equipment","itm_gambeson25","itm_gambeson27","itm_gambeson29","itm_gambeson4","itm_gambeson35","itm_gambeson43"),#viking gambeson
      (call_script,"script_mp_assign_6_equipment","itm_btunic_8","itm_btunic_9","itm_btunic_3","itm_btunic_4","itm_btunic_13","itm_btunic_14"),#Tunics common
      # (call_script,"script_mp_assign_6_equipment","itm_btunic_12","itm_btunic_14","itm_btunic_16",0,0,0),
      # (call_script,"script_mp_assign_6_equipment","itm_gambeson25","itm_gambeson27","itm_byrnie5",0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_viking_shield_round_07","itm_viking_shield_round_08","itm_viking_shield_round_09","itm_viking_shield_round_10","itm_tab_shield_round_01_device",0),
      (call_script,"script_mp_assign_6_equipment","itm_quarter_staff","itm_staff","itm_light_spear1","itm_war_spear1","itm_heavy_spear1",0),
      (call_script,"script_mp_assign_6_equipment","itm_stones","itm_javelin",0,0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_phrygian15","itm_phrygian16","itm_phrygian17",0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_vikingold_helm14","itm_viking_elitehelm3","itm_viking_helm16","itm_viking_elitehelm4","itm_viking_helm17","itm_vikingold_elitehelm9"),
      (call_script,"script_mp_assign_6_equipment","itm_common_pony2","itm_common_pony",0,0,0,0),
      #
      ###SAXON
      #infantry
      (assign,"$temp","trp_mp_saxon_infantry"),
      (call_script,"script_mp_assign_6_equipment","itm_horn_multi","itm_standard","itm_standard_dragon",0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_wooden_stick","itm_seax_2","itm_axe_2","itm_one_handed_war_axe_b","itm_spatha","itm_noble_sword"),
      (call_script,"script_mp_assign_6_equipment","itm_quarter_staff",0,0,0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_light_spear2","itm_war_spear2","itm_heavy_spear2","itm_long_light_spear2","itm_long_war_spear2","itm_long_heavy_spear2"),
      #(call_script,"script_mp_assign_6_equipment","itm_carbatinae_11qs","itm_carbatinae_12qs","itm_carbatinae_13qs","itm_carbatinae_14qs","itm_carbatinae_5",0),
      # (call_script,"script_mp_assign_6_equipment","itm_carbatinae_5s","itm_carbatinae_4s","itm_carbatinae_vc3","itm_carbatinae_vc6","itm_carbatinae_vc2s",0),
      # (call_script,"script_mp_assign_6_equipment","itm_carbatinae_5","itm_carbatinae_11qs","itm_carbatinae_12qs","itm_carbatinae_13qs","itm_carbatinae_14qs",0),
      (call_script,"script_mp_assign_6_equipment","itm_carbatinae_4s",0,"itm_carbatinae_vc6","itm_carbatinae_vc2s","itm_carbatinae_5","itm_carbatinae_13qs"),
      (call_script,"script_mp_assign_6_equipment","itm_leather_gloves",0,0,0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_bl_tunic02","itm_bl_tunic03","itm_bl_tunic09","itm_nobleman_outfit",0,0),#lightarmor
      (call_script,"script_mp_assign_6_equipment","itm_mail_shirt_13_4","itm_mail_shirt_13_3","itm_byrnie5","itm_byrnie21","itm_byrnie22","itm_mail_shirt_13_2"),#mail
      (call_script,"script_mp_assign_6_equipment","itm_gambeson1","itm_gambeson2","itm_gambeson3","itm_gambeson32","itm_gambeson6",0),#short gambeson
      #(call_script,"script_mp_assign_6_equipment","itm_red_cloak",0,0,0,0,0),#tunics
      (call_script,"script_mp_assign_6_equipment","itm_bl_tunic06","itm_bl_tunic07","itm_bl_tunic08","itm_bl_tunic10","itm_bl_tunic11","itm_bl_tunic12"),#tunics
      # (call_script,"script_mp_assign_6_equipment","itm_bl_tunic06","itm_bl_tunic07","itm_bl_tunic08",0,0,0),
      # (call_script,"script_mp_assign_6_equipment","itm_gambeson30","itm_mail_shirt_5_1","itm_mail_shirt_13_3","itm_byrnie5",0,0),
      (call_script,"script_mp_assign_6_equipment","itm_shield_10","itm_viking_shield_round_18","itm_viking_shield_round_19","itm_tab_shield_round_05_device",0,0),
      (call_script,"script_mp_assign_6_equipment","itm_stones","itm_throwing_spears2","itm_throwing_spears",0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_phrygian13","itm_phrygian12","itm_phrygian11",0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_spangenhelm_3","itm_spangenhelm_1","itm_spangenhelm_19","itm_spangenhelm_14","itm_spangenhelm_39",0),
      (call_script,"script_mp_assign_6_equipment","itm_spangenhelm_17","itm_spangenhelm_22",0,0,0,0),
      #archer
      (assign,"$temp","trp_mp_saxon_archer"),
      (call_script,"script_mp_assign_6_equipment","itm_wooden_stick","itm_seax_2","itm_axe_2","itm_one_handed_war_axe_b","itm_spatha",0),
      (call_script,"script_mp_assign_6_equipment","itm_light_spear2","itm_war_spear2",0,0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_carbatinae_5s","itm_carbatinae_vc3","itm_carbatinae_4s","itm_carbatinae_vc6","itm_carbatinae_vc2s",0),
      (call_script,"script_mp_assign_6_equipment","itm_bl_tunic02","itm_bl_tunic03","itm_bl_tunic09","itm_nobleman_outfit",0,0),#lightarmor
      #(call_script,"script_mp_assign_6_equipment","itm_mail_shirt_13_4","itm_mail_shirt_13_3","itm_byrnie5","itm_byrnie21","itm_byrnie22","itm_mail_shirt_13_2"),#mail
      #(call_script,"script_mp_assign_6_equipment","itm_gambeson1","itm_gambeson2","itm_gambeson3","itm_gambeson32","itm_gambeson6",0),#short gambeson
      #(call_script,"script_mp_assign_6_equipment","itm_red_cloak",0,0,0,0,0),#tunics
      (call_script,"script_mp_assign_6_equipment","itm_bl_tunic06","itm_bl_tunic07","itm_bl_tunic08","itm_bl_tunic10","itm_bl_tunic11","itm_bl_tunic12"),#tunics
      # (call_script,"script_mp_assign_6_equipment","itm_hoodtunic_08","itm_bl_tunic01","itm_bl_tunic03",0,0,0),
      # (call_script,"script_mp_assign_6_equipment","itm_gambeson1","itm_gambeson2","itm_gambeson3",0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_stones","itm_javelin_skirmishes","itm_throwing_spears","itm_long_bow","itm_arrows",0),
      (call_script,"script_mp_assign_6_equipment","itm_phrygian4","itm_phrygian5","itm_phrygian6",0,0,0),
      #cavalry
      (assign,"$temp","trp_mp_saxon_cavalry"),
      (call_script,"script_mp_assign_6_equipment","itm_horn_multi","itm_standard","itm_standard_dragon",0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_wooden_stick","itm_seax_2","itm_axe_2","itm_one_handed_war_axe_b","itm_spatha","itm_noble_sword"),
      (call_script,"script_mp_assign_6_equipment","itm_light_spear2","itm_war_spear2","itm_heavy_spear2","itm_long_light_spear2","itm_long_war_spear2","itm_long_heavy_spear2"),
      #(call_script,"script_mp_assign_6_equipment","itm_carbatinae_11qs","itm_carbatinae_12qs","itm_carbatinae_13qs","itm_carbatinae_14qs","itm_carbatinae_5",0),
      (call_script,"script_mp_assign_6_equipment","itm_carbatinae_4s",0,"itm_carbatinae_vc6","itm_carbatinae_vc2s","itm_carbatinae_5","itm_carbatinae_13qs"),
      (call_script,"script_mp_assign_6_equipment","itm_leather_gloves",0,0,0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_bl_tunic02","itm_bl_tunic03","itm_bl_tunic09","itm_nobleman_outfit",0,0),#lightarmor
      #(call_script,"script_mp_assign_6_equipment","itm_mail_shirt_13_4","itm_mail_shirt_13_3","itm_byrnie5","itm_byrnie21","itm_byrnie22","itm_mail_shirt_13_2"),#mail
      (call_script,"script_mp_assign_6_equipment","itm_gambeson1","itm_gambeson2","itm_gambeson3","itm_gambeson32","itm_gambeson6",0),#short gambeson
      #(call_script,"script_mp_assign_6_equipment","itm_red_cloak",0,0,0,0,0),#tunics
      (call_script,"script_mp_assign_6_equipment","itm_bl_tunic06","itm_bl_tunic07","itm_bl_tunic08","itm_bl_tunic10","itm_bl_tunic11","itm_bl_tunic12"),#tunics
      # (call_script,"script_mp_assign_6_equipment","itm_bl_tunic09","itm_bl_tunic10","itm_bl_tunic11",0,0,0),
      # (call_script,"script_mp_assign_6_equipment","itm_gambeson7","itm_gambeson9","itm_mail_shirt_5",0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_viking_shield_round_20","itm_viking_shield_round_19","itm_tab_shield_round_06_device",0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_stones","itm_javelin","itm_throwing_spears",0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_phrygian13","itm_phrygian12","itm_phrygian11",0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_spangenhelm_4","itm_spangenhelm_2","itm_spangenhelm_20","itm_spangenhelm_13","itm_spangenhelm_16",0),
      (call_script,"script_mp_assign_6_equipment","itm_common_pony","itm_common_pony2",0,0,0,0),
      #
      ###ANGLE
      #infantry
      (assign,"$temp","trp_mp_angle_infantry"),
      (call_script,"script_mp_assign_6_equipment","itm_horn_multi","itm_standard","itm_standard_dragon",0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_seax_4","itm_longseax5","itm_spatha","itm_spatha_7","itm_noble_sword","itm_noble_sword_2"),
      (call_script,"script_mp_assign_6_equipment","itm_wooden_stick","itm_axe_2",0,0,0,"itm_quarter_staff"),
      (call_script,"script_mp_assign_6_equipment","itm_light_spear2","itm_war_spear2","itm_heavy_spear2","itm_long_light_spear2","itm_long_war_spear2","itm_long_heavy_spear2"),
      #(call_script,"script_mp_assign_6_equipment","itm_carbatinae_7","itm_carbatinae_9","itm_carbatinae_2v","itm_carbatinae_3v","itm_carbatinae_11q","itm_carbatinae_12q"),
      # (call_script,"script_mp_assign_6_equipment","itm_carbatinae_11q","itm_carbatinae_12q","itm_carbatinae_1s","itm_carbatinae_10","itm_carbatinae_6",0),#16
      # (call_script,"script_mp_assign_6_equipment","itm_carbatinae_4s","itm_carbatinae_5s","itm_carbatinae_5v",0,0,0),#17
      # (call_script,"script_mp_assign_6_equipment","itm_carbatinae_1v",0,0,0,0,0),#20?
      # (call_script,"script_mp_assign_6_equipment","itm_carbatinae_7","itm_carbatinae_9","itm_carbatinae_2v","itm_carbatinae_3v",0,0),#23
      (call_script,"script_mp_assign_6_equipment","itm_carbatinae_11q","itm_carbatinae_4s","itm_carbatinae_1v","itm_carbatinae_9",0,0),
      (call_script,"script_mp_assign_6_equipment","itm_leather_gloves",0,0,0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_ptunic_2","itm_ptunic_9","itm_ptunic_12","itm_btunic_2woman",0,0),#lightarmor -"itm_btunic_7woman"
      (call_script,"script_mp_assign_6_equipment","itm_byrnie23","itm_mail_shirt_5_2","itm_byrnie25","itm_byrnie26","itm_byrnie29",0),##long mail
      (call_script,"script_mp_assign_6_equipment","itm_gambeson26","itm_gambeson28","itm_gambeson34","itm_gambeson39",0,0),#gambeson
      (call_script,"script_mp_assign_6_equipment","itm_gael_tunic_03","itm_ptunic_6","itm_ptunic_7","itm_ptunic_8","itm_ptunic_10","itm_ptunic_11"),#tunic
      # (call_script,"script_mp_assign_6_equipment","itm_ptunic_6","itm_ptunic_7","itm_ptunic_8","itm_ptunic_9",0,0),
      # (call_script,"script_mp_assign_6_equipment","itm_gambeson28","itm_mail_shirt_11_3","itm_byrnie23","itm_byrnie24",0,0),
      (call_script,"script_mp_assign_6_equipment","itm_viking_shield_round_16","itm_viking_shield_round_17","itm_tab_shield_round_08_device","itm_shield_10",0,0),
      (call_script,"script_mp_assign_6_equipment","itm_stones","itm_throwing_spears2","itm_throwing_spears",0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_phrygian10","itm_phrygian9","itm_phrygian8",0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_spangenhelm_7","itm_spangenhelm_5","itm_spangenhelm_21","itm_spangenhelm_15","itm_spangenhelm_40",0),
      (call_script,"script_mp_assign_6_equipment","itm_spangenhelm_38","itm_spangenhelm_28",0,0,0,0),
      #archer
      (assign,"$temp","trp_mp_angle_archer"),
      (call_script,"script_mp_assign_6_equipment","itm_seax_4","itm_longseax5","itm_spatha","itm_spatha_7",0,0),
      (call_script,"script_mp_assign_6_equipment","itm_wooden_stick","itm_axe_2",0,0,0,"itm_quarter_staff"),
      (call_script,"script_mp_assign_6_equipment","itm_light_spear2","itm_war_spear2",0,0,0,0),
      #(call_script,"script_mp_assign_6_equipment","itm_carbatinae_5v","itm_carbatinae_1s","itm_carbatinae_10","itm_carbatinae_6","itm_carbatinae_4s","itm_carbatinae_5s"),
      (call_script,"script_mp_assign_6_equipment","itm_carbatinae_1s","itm_carbatinae_11q","itm_carbatinae_4s","itm_carbatinae_5s","itm_carbatinae_vc2",0),
      (call_script,"script_mp_assign_6_equipment","itm_ptunic_2","itm_ptunic_9","itm_ptunic_12","itm_btunic_2woman",0,0),#lightarmor -"itm_btunic_7woman"
      #(call_script,"script_mp_assign_6_equipment","itm_byrnie23","itm_mail_shirt_5_2","itm_byrnie25","itm_byrnie26","itm_byrnie29",0),##long mail
      #(call_script,"script_mp_assign_6_equipment","itm_gambeson26","itm_gambeson28","itm_gambeson34","itm_gambeson39",0,0),#gambeson
      (call_script,"script_mp_assign_6_equipment","itm_gael_tunic_03","itm_ptunic_6","itm_ptunic_7","itm_ptunic_8","itm_ptunic_10","itm_ptunic_11"),#tunic
      # (call_script,"script_mp_assign_6_equipment","itm_ptunic_1","itm_ptunic_2","itm_ptunic_3","itm_ptunic_4",0,0),
      # (call_script,"script_mp_assign_6_equipment","itm_gambeson10","itm_gambeson11","itm_gambeson21",0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_stones","itm_javelin_skirmishes","itm_throwing_spears","itm_long_bow","itm_arrows",0),
      (call_script,"script_mp_assign_6_equipment","itm_phrygian5","itm_phrygian6","itm_phrygian7",0,0,0),
      #cavalry
      (assign,"$temp","trp_mp_angle_cavalry"),
      (call_script,"script_mp_assign_6_equipment","itm_horn_multi","itm_standard","itm_standard_dragon",0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_seax_4","itm_longseax5","itm_spatha","itm_spatha_7","itm_noble_sword",0),
      (call_script,"script_mp_assign_6_equipment","itm_wooden_stick","itm_axe_2",0,0,0,"itm_quarter_staff"),
      (call_script,"script_mp_assign_6_equipment","itm_light_spear2","itm_war_spear2","itm_heavy_spear2","itm_long_light_spear2",0,0),
      #(call_script,"script_mp_assign_6_equipment","itm_carbatinae_7","itm_carbatinae_9","itm_carbatinae_2v","itm_carbatinae_3v","itm_carbatinae_11q","itm_carbatinae_12q"),
      (call_script,"script_mp_assign_6_equipment","itm_carbatinae_11q","itm_carbatinae_4s","itm_carbatinae_1v","itm_carbatinae_9",0,0),
      (call_script,"script_mp_assign_6_equipment","itm_leather_gloves",0,0,0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_ptunic_2","itm_ptunic_9","itm_ptunic_12","itm_btunic_2woman",0,0),#lightarmor -"itm_btunic_7woman"
      #(call_script,"script_mp_assign_6_equipment","itm_byrnie23","itm_mail_shirt_5_2","itm_byrnie25","itm_byrnie26","itm_byrnie29",0),##long mail
      (call_script,"script_mp_assign_6_equipment","itm_gambeson26","itm_gambeson28","itm_gambeson34","itm_gambeson39",0,0),#gambeson
      (call_script,"script_mp_assign_6_equipment","itm_gael_tunic_03","itm_ptunic_6","itm_ptunic_7","itm_ptunic_8","itm_ptunic_10","itm_ptunic_11"),#tunic
      # (call_script,"script_mp_assign_6_equipment","itm_ptunic_10","itm_ptunic_11","itm_ptunic_12","itm_yellow2_cloak",0,0),
      # (call_script,"script_mp_assign_6_equipment","itm_gambeson22","itm_gambeson26","itm_mail_shirt_5_2",0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_viking_shield_round_21","itm_viking_shield_round_16","itm_tab_shield_round_11_device",0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_stones","itm_javelin","itm_throwing_spears",0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_phrygian10","itm_phrygian9","itm_phrygian8",0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_spangenhelm_8","itm_spangenhelm_6","itm_spangenhelm_25","itm_spangenhelm_35","itm_spangenhelm_18",0),
      (call_script,"script_mp_assign_6_equipment","itm_common_pony","itm_common_pony2","itm_common_horse","itm_common_horse2",0,0),
      #
      ###BRITON
      #infantry
      (assign,"$temp","trp_mp_briton_infantry"),
      (call_script,"script_mp_assign_6_equipment","itm_horn_multi","itm_standard","itm_standard_dragon",0,0,0),
      (call_script,"script_mp_assign_6_equipment", "itm_wooden_stick","itm_knife2","itm_one_handed_war_axe_c","itm_old_swordv","itm_noble_sword_7","itm_noble_sword_12"),#"itm_old_swordv2" "itm_noble_sword_8"
      (call_script,"script_mp_assign_6_equipment","itm_quarter_staff","itm_long_light_spear1","itm_long_war_spear2","itm_long_heavy_spear1","itm_long_heavy_spear2",0),
      #(call_script,"script_mp_assign_6_equipment","itm_carbatinae_6s","itm_carbatinae_2s","itm_carbatinae_3s","itm_carbatinae_2v","itm_carbatinae_3v",0),
      # (call_script,"script_mp_assign_6_equipment","itm_carbatinae_1","itm_carbatinae_3","itm_carbatinae_4","itm_carbatinae_8","itm_carbatinae_5s",0),
      # (call_script,"script_mp_assign_6_equipment","itm_carbatinae_6s","itm_carbatinae_2s","itm_carbatinae_3s","itm_carbatinae_2v","itm_carbatinae_3v",0),
      (call_script,"script_mp_assign_6_equipment",0,"itm_carbatinae_3","itm_carbatinae_5s",0,"itm_carbatinae_6s","itm_carbatinae_3v"),
      (call_script,"script_mp_assign_6_equipment","itm_leather_gloves",0,0,0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_picts_tunic_12","itm_briton_tunic8",0,0,0,0),#lightarmor
      (call_script,"script_mp_assign_6_equipment","itm_mail_shirt_5_1","itm_byrnie4","itm_byrnie6","itm_byrnie13","itm_byrnie14","itm_byrnie15"),#mail
      (call_script,"script_mp_assign_6_equipment","itm_gambeson36","itm_gambeson37","itm_gambeson38","itm_gambeson40","itm_gambeson41","itm_gambeson42"),#gambeson
      (call_script,"script_mp_assign_6_equipment","itm_briton_tunic13","itm_briton_tunic5","itm_briton_tunic4","itm_briton_tunic3","itm_leather_cloak","itm_blue_cloak"),#tunics
      # (call_script,"script_mp_assign_6_equipment","itm_briton_tunic7","itm_briton_tunic8","itm_briton_tunic9","itm_briton_tunic11","itm_briton_tunic14",0),
      # (call_script,"script_mp_assign_6_equipment","itm_gambeson37","itm_mail_shirt_10","itm_byrnie4","itm_byrnie6",0,0),
      (call_script,"script_mp_assign_6_equipment","itm_shield_3","itm_shield_5","itm_tab_shield_round_05_nodevice","itm_tab_shield_round_10_nodevice","itm_tab_shield_round_11_device",0),
      (call_script,"script_mp_assign_6_equipment","itm_stones",0,0,"itm_throwing_spears",0,0),
      (call_script,"script_mp_assign_6_equipment","itm_phrygian5","itm_phrygian6","itm_phrygian7",0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_briton_helm3","itm_briton_helm","itm_briton_helm19","itm_briton_helm13","itm_briton_helm22","itm_briton_helm33"),
      #archer
      (assign,"$temp","trp_mp_briton_archer"),
      # (call_script,"script_mp_assign_6_equipment", "itm_wooden_stick","itm_knife4","itm_one_handed_war_axe_c",0,0,0),
      # (call_script,"script_mp_assign_6_equipment","itm_old_swordv4","itm_old_swordv5",0,0,0,0),
      (call_script,"script_mp_assign_6_equipment", "itm_wooden_stick","itm_knife2","itm_one_handed_war_axe_c","itm_old_swordv",0,0),#"itm_old_swordv2" "itm_noble_sword_8"
      (call_script,"script_mp_assign_6_equipment","itm_quarter_staff","itm_long_light_spear1","itm_long_war_spear2",0,0,0),
      #(call_script,"script_mp_assign_6_equipment","itm_carbatinae_1","itm_carbatinae_3","itm_carbatinae_4","itm_carbatinae_8","itm_carbatinae_5s",0),
      (call_script,"script_mp_assign_6_equipment","itm_carbatinae_3","itm_carbatinae_4","itm_carbatinae_5s","itm_carbatinae_vc3",0,0),
      (call_script,"script_mp_assign_6_equipment","itm_picts_tunic_12","itm_briton_tunic8",0,0,0,0),#lightarmor
      #(call_script,"script_mp_assign_6_equipment","itm_mail_shirt_5_1","itm_byrnie4","itm_byrnie6","itm_byrnie13","itm_byrnie14","itm_byrnie15"),#mail
      #(call_script,"script_mp_assign_6_equipment","itm_gambeson36","itm_gambeson37","itm_gambeson38","itm_gambeson40","itm_gambeson41","itm_gambeson42"),#gambeson
      (call_script,"script_mp_assign_6_equipment","itm_briton_tunic13","itm_briton_tunic5","itm_briton_tunic4","itm_briton_tunic3","itm_leather_cloak","itm_blue_cloak"),#tunics
      # (call_script,"script_mp_assign_6_equipment","itm_briton_tunic1","itm_briton_tunic2","itm_briton_tunic3","itm_briton_tunic4","itm_picts_tunic_14",0),
      # (call_script,"script_mp_assign_6_equipment","itm_gambeson12","itm_gambeson16",0,0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_stones","itm_sling_rock1","itm_sling3","itm_javelin_skirmishesel",0,0),
      (call_script,"script_mp_assign_6_equipment","itm_long_bow","itm_arrows",0,0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_phrygian1","itm_phrygian2","itm_phrygian3",0,0,0),
      #cavalry
      (assign,"$temp","trp_mp_briton_cavalry"),
      (call_script,"script_mp_assign_6_equipment","itm_horn_multi","itm_standard","itm_standard_dragon",0,0,0),
      # (call_script,"script_mp_assign_6_equipment", "itm_wooden_stick","itm_knife2","itm_one_handed_war_axe_c",0,0,0),
      # (call_script,"script_mp_assign_6_equipment","itm_old_swordv3","itm_old_swordv4","itm_noble_sword_9","itm_noble_sword_10",0,0),
      (call_script,"script_mp_assign_6_equipment", "itm_wooden_stick","itm_knife2","itm_one_handed_war_axe_c","itm_old_swordv","itm_noble_sword_7","itm_noble_sword_12"),#"itm_old_swordv2" "itm_noble_sword_8"
      (call_script,"script_mp_assign_6_equipment","itm_quarter_staff","itm_long_light_spear1","itm_long_war_spear2",0,0,0),
      #(call_script,"script_mp_assign_6_equipment","itm_carbatinae_6s","itm_carbatinae_2s","itm_carbatinae_3s","itm_carbatinae_2v","itm_carbatinae_3v",0),
      (call_script,"script_mp_assign_6_equipment",0,"itm_carbatinae_3","itm_carbatinae_5s",0,"itm_carbatinae_6s","itm_carbatinae_3v"),
      (call_script,"script_mp_assign_6_equipment","itm_leather_gloves",0,0,0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_picts_tunic_12","itm_briton_tunic8",0,0,0,0),#lightarmor
      #(call_script,"script_mp_assign_6_equipment","itm_mail_shirt_5_1","itm_byrnie4","itm_byrnie6","itm_byrnie13","itm_byrnie14","itm_byrnie15"),#mail
      (call_script,"script_mp_assign_6_equipment","itm_gambeson36","itm_gambeson37","itm_gambeson38","itm_gambeson40","itm_gambeson41","itm_gambeson42"),#gambeson
      (call_script,"script_mp_assign_6_equipment","itm_briton_tunic13","itm_briton_tunic5","itm_briton_tunic4","itm_briton_tunic3","itm_leather_cloak","itm_blue_cloak"),#tunics
      # (call_script,"script_mp_assign_6_equipment","itm_briton_tunic13","itm_briton_tunic3","itm_briton_tunic4","itm_briton_tunic5","itm_leather_cloak",0),
      # (call_script,"script_mp_assign_6_equipment","itm_gambeson36","itm_mail_shirt_11",0,0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_shield_2","itm_shield_6","itm_tab_shield_round_05_nodevice","itm_tab_shield_round_10_nodevice","itm_tab_shield_round_11_device",0),
      (call_script,"script_mp_assign_6_equipment","itm_stones","itm_javelin_skirmishesel",0,0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_phrygian5","itm_phrygian6","itm_phrygian7",0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_briton_helm4","itm_briton_helm2","itm_briton_helm20","itm_briton_helm14","itm_briton_helm23","itm_briton_helm34"),
      (call_script,"script_mp_assign_6_equipment","itm_common_pony","itm_common_pony2","itm_common_horse","itm_common_horse2",0,0),
      #
      ###IRISH
      #infantry
      (assign,"$temp","trp_mp_irish_infantry"),
      (call_script,"script_mp_assign_6_equipment","itm_horn_multi","itm_standard","itm_standard_dragon",0,0,0),
      (call_script,"script_mp_assign_6_equipment", "itm_wooden_stick","itm_knife3",0,0,0,0),#"itm_knife5"
      (call_script,"script_mp_assign_6_equipment","itm_irish_short_sword1","itm_irish_long_sword4","itm_irish_long_sword2","itm_championsword2",0,0),
      (call_script,"script_mp_assign_6_equipment","itm_pictish_hatchet13","itm_pictish_hatchet12","itm_pictish_hatchet",0,"itm_pictish_hatchet15","itm_pictish_hatchet3"),
      #(call_script,"script_mp_assign_6_equipment","itm_pictish_hatchet2","itm_pictish_hatchet11","itm_pictish_hatchet3",0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_quarter_staff","itm_long_light_spear1","itm_long_war_spear1","itm_long_heavy_spear1",0,0),
      (call_script,"script_mp_assign_6_equipment","itm_gaelshoes_2","itm_gaelshoes_3","itm_gaelshoes_1","itm_just_man_boots_dark",0,0),
      (call_script,"script_mp_assign_6_equipment","itm_leather_gloves",0,0,0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_brat3","itm_brat4",0,0,0,0),#lightarmor
      (call_script,"script_mp_assign_6_equipment","itm_byrnie9","itm_byrnie10","itm_byrnie36","itm_byrnie37","itm_byrnie38",0),##long mail
      (call_script,"script_mp_assign_6_equipment","itm_gambeson12gael","itm_gambeson13gael","itm_gambeson14gael","itm_gambeson15gael","itm_gambeson16gael",0),#gambeson
      (call_script,"script_mp_assign_6_equipment","itm_gael_tunic_08","itm_gael_hoodtunic_09","itm_gael_hoodtunic_10",0,0,0),#hood tunic
      (call_script,"script_mp_assign_6_equipment","itm_briton_tunic24","itm_briton_tunic25","itm_briton_tunic26","itm_briton_tunic27","itm_gael_hoodtunic_11",0),#tunic
      # (call_script,"script_mp_assign_6_equipment","itm_brat1","itm_brat1","itm_gael_tunic_08","itm_briton_tunic24",0,0),
      # (call_script,"script_mp_assign_6_equipment","itm_gambeson14gael","itm_mail_shirt_12_2","itm_byrnie12",0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_small_roundsh1","itm_small_roundsh3","itm_gael_bigroundshield_01","itm_gael_bigroundshield_03","itm_gael_bigroundshield_05","itm_gael_bigroundshield_06"),
      (call_script,"script_mp_assign_6_equipment","itm_stones","itm_javelin_skirmishesel",0,0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_phrygian4","itm_phrygian9","itm_phrygian14",0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_angle_helmet1","itm_angle_helmet2","itm_angle_helmet3","itm_angle_helmet4",0,0),
      #archer
      (assign,"$temp","trp_mp_irish_archer"),
      (call_script,"script_mp_assign_6_equipment","itm_knife3","itm_irish_short_sword1",0,0,0,0),
      (call_script,"script_mp_assign_6_equipment", "itm_wooden_stick","itm_pictish_hatchet13","itm_pictish_hatchet12","itm_pictish_hatchet",0,0),
      (call_script,"script_mp_assign_6_equipment","itm_quarter_staff","itm_long_light_spear1","itm_long_war_spear1",0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_gaelshoes_2","itm_just_man_boots_medium","itm_bare_foot_man","itm_just_man_boots_dark",0,0),
      (call_script,"script_mp_assign_6_equipment","itm_brat3","itm_brat4",0,0,0,0),#lightarmor
      #(call_script,"script_mp_assign_6_equipment","itm_byrnie9","itm_byrnie10","itm_byrnie36","itm_byrnie37","itm_byrnie38",0),##long mail
      #(call_script,"script_mp_assign_6_equipment","itm_gambeson12gael","itm_gambeson13gael","itm_gambeson14gael","itm_gambeson15gael","itm_gambeson16gael",0),#gambeson
      (call_script,"script_mp_assign_6_equipment","itm_gael_tunic_08","itm_gael_hoodtunic_09","itm_gael_hoodtunic_10",0,0,0),#hood tunic
      (call_script,"script_mp_assign_6_equipment","itm_briton_tunic24","itm_briton_tunic25","itm_briton_tunic26","itm_briton_tunic27","itm_gael_hoodtunic_11",0),#tunic
      # (call_script,"script_mp_assign_6_equipment","itm_briton_tunic20","itm_briton_tunic21","itm_gael_tunic_01","itm_gael_tunic_02",0,0),
      # (call_script,"script_mp_assign_6_equipment","itm_gambeson13gael","itm_gambeson12gael",0,0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_stones","itm_javelin_skirmishesel","itm_long_bow","itm_arrows",0,0),
      (call_script,"script_mp_assign_6_equipment","itm_phrygian4","itm_phrygian9","itm_phrygian14",0,0,0),
      #cavalry
      (assign,"$temp","trp_mp_irish_cavalry"),
      (call_script,"script_mp_assign_6_equipment","itm_horn_multi","itm_standard","itm_standard_dragon",0,0,0),
      (call_script,"script_mp_assign_6_equipment", "itm_wooden_stick","itm_knife3",0,0,0,0),#"itm_knife5"
      (call_script,"script_mp_assign_6_equipment","itm_irish_short_sword1","itm_irish_long_sword4","itm_irish_long_sword2",0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_pictish_hatchet13","itm_pictish_hatchet12","itm_pictish_hatchet",0,0,0),
      # (call_script,"script_mp_assign_6_equipment", "itm_wooden_stick","itm_knife3","itm_knife5",0,0,0),
      # (call_script,"script_mp_assign_6_equipment","itm_irish_long_sword3","itm_irish_short_sword1","itm_irish_long_sword2",0,0,0),
      # (call_script,"script_mp_assign_6_equipment","itm_pictish_hatchet2","itm_pictish_hatchet11","itm_pictish_hatchet3",0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_quarter_staff","itm_long_light_spear1","itm_long_war_spear1",0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_gaelshoes_2","itm_gaelshoes_3","itm_gaelshoes_1","itm_just_man_boots_dark",0,0),
      (call_script,"script_mp_assign_6_equipment","itm_leather_gloves",0,0,0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_brat3","itm_brat4",0,0,0,0),#lightarmor
      #(call_script,"script_mp_assign_6_equipment","itm_byrnie9","itm_byrnie10","itm_byrnie36","itm_byrnie37","itm_byrnie38",0),##long mail
      (call_script,"script_mp_assign_6_equipment","itm_gambeson12gael","itm_gambeson13gael","itm_gambeson14gael","itm_gambeson15gael","itm_gambeson16gael",0),#gambeson
      (call_script,"script_mp_assign_6_equipment","itm_gael_tunic_08","itm_gael_hoodtunic_09","itm_gael_hoodtunic_10",0,0,0),#hood tunic
      (call_script,"script_mp_assign_6_equipment","itm_briton_tunic24","itm_briton_tunic25","itm_briton_tunic26","itm_briton_tunic27","itm_gael_hoodtunic_11",0),#tunic
      # (call_script,"script_mp_assign_6_equipment","itm_brat3","itm_brat4","itm_gael_tunic_02","itm_briton_tunic25",0,0),
      # (call_script,"script_mp_assign_6_equipment","itm_gambeson15gael","itm_mail_shirt_12_1",0,0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_small_roundsh1","itm_small_roundsh3","itm_gael_bigroundshield_01","itm_gael_bigroundshield_03","itm_gael_bigroundshield_05","itm_gael_bigroundshield_06"),
      (call_script,"script_mp_assign_6_equipment","itm_stones","itm_javelin_jinetes",0,0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_phrygian4","itm_phrygian9","itm_phrygian14",0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_angle_helmet1","itm_angle_helmet2","itm_angle_helmet3","itm_angle_helmet4",0,0),
      (call_script,"script_mp_assign_6_equipment","itm_common_pony","itm_common_pony2",0,0,0,0),
      #
      ###Scotch
      #infantry
      (assign,"$temp","trp_mp_scotch_infantry"),
      (call_script,"script_mp_assign_6_equipment","itm_horn_multi","itm_standard","itm_standard_dragon",0,0,0),
      #(call_script,"script_mp_assign_6_equipment","itm_pictish_hatchet5","itm_pictish_hatchet8","itm_pictish_hatchet6","itm_pictish_hatchet9","itm_pictish_hatchet7","itm_pictish_hatchet10"),
      (call_script,"script_mp_assign_6_equipment","itm_seax_1","itm_knife4","itm_irish_short_sword2","itm_irish_long_sword7",0,0),
      (call_script,"script_mp_assign_6_equipment","itm_wooden_stick","itm_pictish_hatchet8",0,"itm_pictish_hatchet9","itm_pictish_hatchet7","itm_pictish_hatchet10"),
      (call_script,"script_mp_assign_6_equipment","itm_quarter_staff","itm_long_light_spear1","itm_long_light_spear2","itm_long_war_spear2",0,0),
      (call_script,"script_mp_assign_6_equipment","itm_just_man_boots_medium","itm_just_man_boots_light","itm_bare_foot_man","itm_just_man_boots_dark","itm_carbatinae_12q",0),
      (call_script,"script_mp_assign_6_equipment","itm_leather_gloves",0,0,0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_picts_hoodtunic_15","itm_picts_hoodtunic_16","itm_picts_hoodtunic_14","itm_picts_hoodtunic_17",0,0),#hood tunic
      (call_script,"script_mp_assign_6_equipment","itm_picts_hoodtunic_11","itm_picts_hoodtunic_12","itm_briton_tunic18","itm_briton_tunic19","itm_picts_hoodtunic_13","itm_briton_tunic17"),#tunic
      (call_script,"script_mp_assign_6_equipment","itm_mail_shirt_6","itm_mail_shirt_7","itm_mail_shirt_11_3","itm_mail_shirt_2","itm_mail_shirt_5",0),#mail
      (call_script,"script_mp_assign_6_equipment","itm_gambeson1cloak","itm_gambeson1gael","itm_gambeson2gael","itm_gambeson3gael","itm_gambeson4gael",0),#gambeson
      (call_script,"script_mp_assign_6_equipment","itm_pictish_painted1","itm_pictish_painted2","itm_pictish_painted3",0,"itm_picts_hoodtunic_01",0),#naked
      (call_script,"script_mp_assign_6_equipment","itm_picts_hoodtunic_03","itm_picts_hoodtunic_04","itm_picts_hoodtunic_05","itm_picts_hoodtunic_06",0,0),#hood naked
      # (call_script,"script_mp_assign_6_equipment","itm_pictish_painted1","itm_pictish_painted2","itm_picts_hoodtunic_05","itm_briton_tunic18","itm_picts_hoodtunic_14","itm_picts_hoodtunic_05"),
      # (call_script,"script_mp_assign_6_equipment","itm_gambeson5gael","itm_mail_shirt_7","itm_byrnie21","itm_byrnie20",0,0),
      (call_script,"script_mp_assign_6_equipment","itm_squaresh_2","itm_squaresh_5","itm_h_shield2","itm_h_shield4","itm_tab_shield_small_round_c",0),
      (call_script,"script_mp_assign_6_equipment","itm_stones","itm_javelin_skirmishesel","itm_throwing_spears2",0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_phrygian8","itm_phrygian11","itm_phrygian15",0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_angle_helmet5","itm_angle_helmet6","itm_angle_helmet4","itm_angle_helmet3",0,0),
      #archer
      (assign,"$temp","trp_mp_scotch_archer"),
      # (call_script,"script_mp_assign_6_equipment","itm_seax_1","itm_knife4",0,0,0,0),
      # (call_script,"script_mp_assign_6_equipment","itm_pictish_hatchet5","itm_pictish_hatchet8","itm_pictish_hatchet6","itm_pictish_hatchet9","itm_pictish_hatchet7","itm_pictish_hatchet10"),
      (call_script,"script_mp_assign_6_equipment","itm_seax_1","itm_knife4","itm_irish_short_sword2",0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_wooden_stick","itm_pictish_hatchet8",0,"itm_pictish_hatchet9","itm_pictish_hatchet7","itm_pictish_hatchet10"),
      (call_script,"script_mp_assign_6_equipment","itm_quarter_staff","itm_long_light_spear1","itm_long_light_spear2",0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_just_man_boots_medium","itm_just_man_boots_light","itm_bare_foot_man","itm_just_man_boots_dark","itm_carbatinae_12q",0),
      (call_script,"script_mp_assign_6_equipment","itm_picts_hoodtunic_15","itm_picts_hoodtunic_16","itm_picts_hoodtunic_14","itm_picts_hoodtunic_17",0,0),#hood tunic
      (call_script,"script_mp_assign_6_equipment","itm_picts_hoodtunic_11","itm_picts_hoodtunic_12","itm_briton_tunic18","itm_briton_tunic19","itm_picts_hoodtunic_13","itm_briton_tunic17"),#tunic
      #(call_script,"script_mp_assign_6_equipment","itm_mail_shirt_6","itm_mail_shirt_7","itm_mail_shirt_11_3","itm_mail_shirt_2","itm_mail_shirt_5",0),#mail
      #(call_script,"script_mp_assign_6_equipment","itm_gambeson1cloak","itm_gambeson1gael","itm_gambeson2gael","itm_gambeson3gael","itm_gambeson4gael",0),#gambeson
      (call_script,"script_mp_assign_6_equipment","itm_pictish_painted1","itm_pictish_painted2","itm_pictish_painted3",0,"itm_picts_hoodtunic_01",0),#naked
      (call_script,"script_mp_assign_6_equipment","itm_picts_hoodtunic_03","itm_picts_hoodtunic_04","itm_picts_hoodtunic_05","itm_picts_hoodtunic_06",0,0),#hood naked
      # (call_script,"script_mp_assign_6_equipment","itm_briton_tunic15","itm_briton_tunic16","itm_briton_tunic17","itm_picts_hoodtunic_03","itm_picts_hoodtunic_04","itm_picts_hoodtunic_15"),
      # (call_script,"script_mp_assign_6_equipment","itm_gambeson1gael","itm_gambeson2gael",0,0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_stones","itm_javelin_skirmishesel","itm_throwing_spears2","itm_crossbow_mp","itm_bolts_mp",0),
      (call_script,"script_mp_assign_6_equipment","itm_phrygian8","itm_phrygian11","itm_phrygian15",0,0,0),
      #cavalry
      (assign,"$temp","trp_mp_scotch_cavalry"),
      (call_script,"script_mp_assign_6_equipment","itm_horn_multi","itm_standard","itm_standard_dragon",0,0,0),
      # (call_script,"script_mp_assign_6_equipment","itm_seax_1","itm_knife4","itm_irish_long_sword4","itm_irish_long_sword7",0,0),
      # (call_script,"script_mp_assign_6_equipment","itm_pictish_hatchet5","itm_pictish_hatchet8","itm_pictish_hatchet6","itm_pictish_hatchet9","itm_pictish_hatchet7","itm_pictish_hatchet10"),
      (call_script,"script_mp_assign_6_equipment","itm_seax_1","itm_knife4","itm_irish_short_sword2","itm_irish_long_sword7",0,0),
      (call_script,"script_mp_assign_6_equipment","itm_wooden_stick","itm_pictish_hatchet8",0,"itm_pictish_hatchet9","itm_pictish_hatchet7","itm_pictish_hatchet10"),
      (call_script,"script_mp_assign_6_equipment","itm_quarter_staff","itm_long_light_spear1","itm_long_light_spear2",0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_just_man_boots_medium","itm_just_man_boots_light","itm_bare_foot_man","itm_just_man_boots_dark","itm_carbatinae_12q",0),
      (call_script,"script_mp_assign_6_equipment","itm_leather_gloves",0,0,0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_picts_hoodtunic_15","itm_picts_hoodtunic_16","itm_picts_hoodtunic_14","itm_picts_hoodtunic_17",0,0),#hood tunic
      (call_script,"script_mp_assign_6_equipment","itm_picts_hoodtunic_11","itm_picts_hoodtunic_12","itm_briton_tunic18","itm_briton_tunic19","itm_picts_hoodtunic_13","itm_briton_tunic17"),#tunic
      #(call_script,"script_mp_assign_6_equipment","itm_mail_shirt_6","itm_mail_shirt_7","itm_mail_shirt_11_3","itm_mail_shirt_2","itm_mail_shirt_5",0),#mail
      (call_script,"script_mp_assign_6_equipment","itm_gambeson1cloak","itm_gambeson1gael","itm_gambeson2gael","itm_gambeson3gael","itm_gambeson4gael",0),#gambeson
      (call_script,"script_mp_assign_6_equipment","itm_pictish_painted1","itm_pictish_painted2","itm_pictish_painted3",0,"itm_picts_hoodtunic_01",0),#naked
      (call_script,"script_mp_assign_6_equipment","itm_picts_hoodtunic_03","itm_picts_hoodtunic_04","itm_picts_hoodtunic_05","itm_picts_hoodtunic_06",0,0),#hood naked
      # (call_script,"script_mp_assign_6_equipment","itm_pictish_painted3","itm_pictish_painted4","itm_picts_hoodtunic_06","itm_briton_tunic19","itm_picts_hoodtunic_17","itm_picts_hoodtunic_16"),
      # (call_script,"script_mp_assign_6_equipment","itm_gambeson3gael","itm_mail_shirt_6",0,0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_squaresh_4","itm_squaresh_5","itm_h_shield3","itm_h_shield4","itm_tab_shield_small_round_c",0),
      (call_script,"script_mp_assign_6_equipment","itm_stones","itm_javelin_jinetes","itm_throwing_spears2",0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_phrygian8","itm_phrygian11","itm_phrygian15",0,0,0),
      (call_script,"script_mp_assign_6_equipment","itm_angle_helmet5","itm_angle_helmet6","itm_angle_helmet4","itm_angle_helmet3",0,0),
      (call_script,"script_mp_assign_6_equipment","itm_wild_pony","itm_wild_pony2","itm_wild_horse","itm_wild_horse",0,0),
      
      
      #######
      #######OLD NON-CLASS SYSTEM
      
      ####NORSE EQUIPMENT
      (assign,"$temp","trp_norse_multiplayer"),
      (try_for_range,":unused",0,3),
        (call_script,"script_mp_assign_6_equipment","itm_seax_1","itm_longseax6",0,0,"itm_sword_5",0),#"itm_longseax7"#"itm_sword_6"
        (call_script,"script_mp_assign_6_equipment","itm_wooden_stick","itm_axe_3","itm_hand_axe",0,0,0),#"itm_axe_4"
        (call_script,"script_mp_assign_6_equipment",0,0,"itm_light_spear1","itm_war_spear1",0,0),
        #armor
        (call_script,"script_mp_assign_6_equipment","itm_carbatinae_6","itm_carbatinae_vc1",0,"itm_carbatinae_vc1v","itm_carbatinae_5","itm_carbatinae_14qs"),
        (call_script,"script_mp_assign_6_equipment","itm_leather_gloves",0,0,0,0,0),
        (call_script,"script_mp_assign_6_equipment","itm_btunic_12","itm_btunic_15","itm_btunic_16",0,0,0),#light armor (tunic reforced)
        (call_script,"script_mp_assign_6_equipment","itm_gambeson25","itm_gambeson27","itm_gambeson29","itm_gambeson4","itm_gambeson35","itm_gambeson43"),#viking gambeson
        #shields
        (call_script,"script_mp_assign_6_equipment","itm_viking_shield_round_01","itm_viking_shield_round_02","itm_viking_shield_round_03","itm_viking_shield_round_04","itm_tab_shield_round_01_device",0),
        #helmets
        (call_script,"script_mp_assign_6_equipment","itm_vikingold_helm15","itm_viking_elitehelm1","itm_viking_helm15","itm_viking_elitehelm2","itm_viking_helm16","itm_viking_noblehelm1"),
        #horses
        (call_script,"script_mp_assign_6_equipment","itm_common_pony","itm_common_pony2",0,0,0,0),
        
        ###additional (not for captain)
        (neq,"$temp","trp_norse_capitan"),
        (call_script,"script_mp_assign_6_equipment","itm_horn_multi","itm_standard",0,0,0,0),
        (call_script,"script_mp_assign_6_equipment","itm_stones","itm_throwing_spears","itm_long_bow","itm_arrows",0,0),
        #
        (call_script,"script_mp_assign_6_equipment","itm_heavy_spear1","itm_one_handed_war_axe_a",0,0,0,0),
        (call_script,"script_mp_assign_6_equipment","itm_addon_mail4","itm_addon_mail7",0,0,0,0),#animal mail
        (call_script,"script_mp_assign_6_equipment","itm_byrnie16","itm_byrnie17","itm_byrnie18","itm_byrnie19","itm_byrnie31","itm_byrnie32"),#mail
        (try_begin),
          (eq,"$temp","trp_norse_multiplayer"),
          (call_script,"script_mp_assign_6_equipment","itm_quarter_staff", "itm_staff","itm_wooden_stick",0,0,0),
          (call_script,"script_mp_assign_6_equipment","itm_phrygian15","itm_phrygian16","itm_phrygian17",0,0,0),
          (call_script,"script_mp_assign_6_equipment","itm_btunic_8","itm_btunic_9","itm_btunic_3","itm_btunic_4","itm_btunic_13","itm_btunic_14"),#Tunics common
          (assign,"$temp","trp_norse_elite"),
        (else_try),
          (assign,"$temp","trp_norse_capitan"),
        (try_end),
      (try_end),
      
      ####SAXON EQUIPMENT
      (assign,"$temp","trp_saxon_multiplayer"),
      (try_for_range,":unused",0,3),
        #weapons
        (call_script,"script_mp_assign_6_equipment",0,"itm_seax_2","itm_axe_2","itm_one_handed_war_axe_b","itm_spatha",0),
        (call_script,"script_mp_assign_6_equipment","itm_light_spear2","itm_war_spear2","itm_heavy_spear2","itm_long_light_spear2",0,0),
        #armor
        #(call_script,"script_mp_assign_6_equipment","itm_carbatinae_11qs","itm_carbatinae_12qs","itm_carbatinae_13qs","itm_carbatinae_14qs","itm_carbatinae_5",0),
        (call_script,"script_mp_assign_6_equipment","itm_carbatinae_4s",0,"itm_carbatinae_vc6","itm_carbatinae_vc2s","itm_carbatinae_5","itm_carbatinae_13qs"),
        #(call_script,"script_mp_assign_6_equipment","itm_leather_gloves",0,"itm_gambeson3","itm_gambeson32","itm_byrnie21","itm_byrnie22"),
        (call_script,"script_mp_assign_6_equipment","itm_leather_gloves",0,0,0,0,0),
        (call_script,"script_mp_assign_6_equipment","itm_bl_tunic02","itm_bl_tunic03","itm_bl_tunic09","itm_nobleman_outfit",0,0),#lightarmor
        (call_script,"script_mp_assign_6_equipment","itm_gambeson1","itm_gambeson2","itm_gambeson3","itm_gambeson32","itm_gambeson6",0),#short gambeson
        #shields
        (call_script,"script_mp_assign_6_equipment","itm_shield_10","itm_viking_shield_round_18","itm_viking_shield_round_19","itm_tab_shield_round_05_device",0,0),
        #helmets
        (call_script,"script_mp_assign_6_equipment","itm_spangenhelm_3","itm_spangenhelm_1","itm_spangenhelm_19","itm_spangenhelm_14","itm_spangenhelm_39",0),
        (call_script,"script_mp_assign_6_equipment","itm_spangenhelm_17","itm_spangenhelm_22",0,0,0,0),
        #horses
        (call_script,"script_mp_assign_6_equipment","itm_common_pony","itm_common_pony2",0,0,0,0),
        ###additional (not for captain)
        (neq,"$temp","trp_saxon_capitan"),
        (call_script,"script_mp_assign_6_equipment","itm_horn_multi","itm_standard","itm_standard_dragon","itm_noble_sword","itm_long_war_spear2","itm_long_heavy_spear2"),
        (call_script,"script_mp_assign_6_equipment","itm_throwing_spears2","itm_throwing_spears","itm_long_bow","itm_arrows",0,0),
        (call_script,"script_mp_assign_6_equipment","itm_mail_shirt_13_4","itm_mail_shirt_13_3","itm_byrnie5","itm_byrnie21","itm_byrnie22","itm_mail_shirt_13_2"),#mail
        (try_begin),
          (eq,"$temp","trp_saxon_multiplayer"),
          (call_script,"script_mp_assign_6_equipment","itm_quarter_staff","itm_wooden_stick","itm_stones",0,0,0),
          (call_script,"script_mp_assign_6_equipment","itm_phrygian13","itm_phrygian12","itm_phrygian11",0,0,0),
          (call_script,"script_mp_assign_6_equipment","itm_bl_tunic06","itm_bl_tunic07","itm_bl_tunic08","itm_bl_tunic10","itm_bl_tunic11","itm_bl_tunic12"),#tunics
          (assign,"$temp","trp_saxon_elite"),
        (else_try),
          (assign,"$temp","trp_saxon_capitan"),
        (try_end),
      (try_end),
      
      ####ANGLE EQUIPMENT
      (assign,"$temp","trp_angle_multiplayer"),
      (try_for_range,":unused",0,3),
        #weapons
        (call_script,"script_mp_assign_6_equipment","itm_axe_2",0,0,0,0,0),
        (call_script,"script_mp_assign_6_equipment","itm_seax_4","itm_longseax5","itm_spatha","itm_spatha_7",0,0),
        (call_script,"script_mp_assign_6_equipment","itm_light_spear2","itm_war_spear2","itm_heavy_spear2","itm_long_light_spear2",0,0),
        #armor
        #(call_script,"script_mp_assign_6_equipment","itm_carbatinae_7","itm_carbatinae_9","itm_carbatinae_2v","itm_carbatinae_3v","itm_carbatinae_11q","itm_carbatinae_12q"),
        (call_script,"script_mp_assign_6_equipment","itm_carbatinae_11q","itm_carbatinae_4s","itm_carbatinae_1v","itm_carbatinae_9",0,0),
        #(call_script,"script_mp_assign_6_equipment","itm_leather_gloves",0,"itm_gambeson10","itm_gambeson39","itm_byrnie30","itm_byrnie28"),
        (call_script,"script_mp_assign_6_equipment","itm_leather_gloves",0,0,0,0,0),
        (call_script,"script_mp_assign_6_equipment","itm_ptunic_2","itm_ptunic_9","itm_ptunic_12","itm_btunic_2woman",0,0),#lightarmor
        (call_script,"script_mp_assign_6_equipment","itm_gambeson26","itm_gambeson28","itm_gambeson34","itm_gambeson39",0,0),#gambeson
        #shields
        (call_script,"script_mp_assign_6_equipment","itm_viking_shield_round_16","itm_viking_shield_round_17","itm_tab_shield_round_08_device","itm_shield_10",0,0),
        #helmets
        (call_script,"script_mp_assign_6_equipment","itm_spangenhelm_7","itm_spangenhelm_5","itm_spangenhelm_21","itm_spangenhelm_15","itm_spangenhelm_40",0),
        (call_script,"script_mp_assign_6_equipment","itm_spangenhelm_38","itm_spangenhelm_28",0,0,0,0),
        #horses
        (call_script,"script_mp_assign_6_equipment","itm_common_pony","itm_common_pony2",0,0,0,0),
        ###additional (not for captain)
        (neq,"$temp","trp_angle_capitan"),
        (call_script,"script_mp_assign_6_equipment","itm_horn_multi","itm_standard","itm_standard_dragon",0,"itm_long_war_spear2","itm_long_heavy_spear2"),
        (call_script,"script_mp_assign_6_equipment","itm_throwing_spears2","itm_throwing_spears","itm_long_bow","itm_arrows",0,0),
        (call_script,"script_mp_assign_6_equipment","itm_noble_sword","itm_noble_sword_2",0,0,0,0),
        (call_script,"script_mp_assign_6_equipment","itm_byrnie23","itm_mail_shirt_5_2","itm_byrnie25","itm_byrnie26","itm_byrnie29",0),##long mail
        (try_begin),
          (eq,"$temp","trp_angle_multiplayer"),
          (call_script,"script_mp_assign_6_equipment","itm_quarter_staff","itm_wooden_stick",0,0,0,"itm_stones"),
          (call_script,"script_mp_assign_6_equipment","itm_gael_tunic_03","itm_ptunic_6","itm_ptunic_7","itm_ptunic_8","itm_ptunic_10","itm_ptunic_11"),#tunic
          (call_script,"script_mp_assign_6_equipment","itm_phrygian10","itm_phrygian9","itm_phrygian8",0,0,0),
          
          (assign,"$temp","trp_angle_elite"),
        (else_try),
          (assign,"$temp","trp_angle_capitan"),
        (try_end),
      (try_end),
      
      ####BRITON EQUIPMENT
      (assign,"$temp","trp_briton_multiplayer"),
      (try_for_range,":unused",0,3),
        #weapons
        (call_script,"script_mp_assign_6_equipment",0,"itm_knife2","itm_one_handed_war_axe_c","itm_old_swordv",0,0),#"itm_old_swordv2" "itm_noble_sword_8"
        (call_script,"script_mp_assign_6_equipment",0,"itm_long_light_spear1","itm_long_war_spear2",0,0,0),
        #armor
        (call_script,"script_mp_assign_6_equipment",0,"itm_carbatinae_3","itm_carbatinae_5s",0,"itm_carbatinae_6s","itm_carbatinae_3v"),
        (call_script,"script_mp_assign_6_equipment","itm_leather_gloves",0,0,0,0,0),
        (call_script,"script_mp_assign_6_equipment","itm_picts_tunic_12","itm_briton_tunic8",0,0,0,0),#lightarmor
        (call_script,"script_mp_assign_6_equipment","itm_gambeson36","itm_gambeson37","itm_gambeson38","itm_gambeson40","itm_gambeson41","itm_gambeson42"),#gambeson
        #shields
        (call_script,"script_mp_assign_6_equipment","itm_shield_3","itm_shield_5","itm_tab_shield_round_05_nodevice","itm_tab_shield_round_10_nodevice","itm_tab_shield_round_11_device",0),
        #helmets
        (call_script,"script_mp_assign_6_equipment","itm_briton_helm3","itm_briton_helm","itm_briton_helm19","itm_briton_helm13","itm_briton_helm22","itm_briton_helm33"),
        #horses
        (call_script,"script_mp_assign_6_equipment","itm_common_pony","itm_common_pony2","itm_common_horse","itm_common_horse2",0,0),
        ###additional (not for captain)
        (neq,"$temp","trp_briton_capitan"),
        (call_script,"script_mp_assign_6_equipment","itm_horn_multi","itm_standard","itm_standard_dragon",0,"itm_long_heavy_spear1","itm_long_heavy_spear2"),
        (call_script,"script_mp_assign_6_equipment","itm_sling_rock1","itm_sling3","itm_throwing_spears","itm_long_bow","itm_arrows",0),
        (call_script,"script_mp_assign_6_equipment","itm_noble_sword_7","itm_noble_sword_12",0,0,0,0),
        (call_script,"script_mp_assign_6_equipment","itm_mail_shirt_5_1","itm_byrnie4","itm_byrnie6","itm_byrnie13","itm_byrnie14","itm_byrnie15"),#mail
        (try_begin),
          (eq,"$temp","trp_briton_multiplayer"),
          (call_script,"script_mp_assign_6_equipment","itm_quarter_staff","itm_wooden_stick",0,0,0,"itm_stones"),
          (call_script,"script_mp_assign_6_equipment","itm_phrygian5","itm_phrygian6","itm_phrygian7",0,0,0),
          (call_script,"script_mp_assign_6_equipment","itm_briton_tunic13","itm_briton_tunic5","itm_briton_tunic4","itm_briton_tunic3","itm_leather_cloak","itm_blue_cloak"),#tunics
          (assign,"$temp","trp_briton_elite"),
        (else_try),
          (assign,"$temp","trp_briton_capitan"),
        (try_end),
      (try_end),
      
      ####IRISH EQUIPMENT
      (assign,"$temp","trp_irish_multiplayer"),
      (try_for_range,":unused",0,3),
        #weapons
        (call_script,"script_mp_assign_6_equipment","itm_knife3","itm_irish_short_sword1","itm_irish_long_sword4",0,0,0),
        (call_script,"script_mp_assign_6_equipment","itm_pictish_hatchet13","itm_pictish_hatchet12","itm_pictish_hatchet",0,"itm_pictish_hatchet15","itm_pictish_hatchet3"),
        (call_script,"script_mp_assign_6_equipment","itm_quarter_staff","itm_long_light_spear1",0,0,0,0),
        #armor
        (call_script,"script_mp_assign_6_equipment","itm_gaelshoes_2","itm_gaelshoes_3","itm_gaelshoes_1","itm_just_man_boots_dark",0,0),
        (call_script,"script_mp_assign_6_equipment","itm_leather_gloves",0,0,0,0,0),
        (call_script,"script_mp_assign_6_equipment","itm_brat3","itm_brat4",0,0,0,0),#lightarmor
        (call_script,"script_mp_assign_6_equipment","itm_gambeson12gael","itm_gambeson13gael","itm_gambeson14gael","itm_gambeson15gael","itm_gambeson16gael",0),#gambeson
        #shields
        (call_script,"script_mp_assign_6_equipment","itm_small_roundsh1","itm_small_roundsh3","itm_gael_bigroundshield_01","itm_gael_bigroundshield_03","itm_gael_bigroundshield_05","itm_gael_bigroundshield_06"),
        #helmets
        (call_script,"script_mp_assign_6_equipment","itm_angle_helmet1","itm_angle_helmet2","itm_angle_helmet3","itm_angle_helmet4",0,0),
        #horses
        (call_script,"script_mp_assign_6_equipment","itm_common_pony","itm_common_pony2","itm_common_horse","itm_common_horse2",0,0),
        ###additional (not for captain)
        (neq,"$temp","trp_irish_capitan"),
        (call_script,"script_mp_assign_6_equipment","itm_horn_multi","itm_standard","itm_standard_dragon",0,"itm_long_war_spear1","itm_long_heavy_spear1"),
        (call_script,"script_mp_assign_6_equipment","itm_javelin_skirmishesel","itm_long_bow","itm_arrows",0,0,0),#"itm_sling_rock1","itm_sling3"
        (call_script,"script_mp_assign_6_equipment","itm_irish_long_sword2","itm_championsword2",0,0,0,0),
        (call_script,"script_mp_assign_6_equipment","itm_byrnie9","itm_byrnie10","itm_byrnie36","itm_byrnie37","itm_byrnie38",0),##long mail
        (try_begin),
          (eq,"$temp","trp_irish_multiplayer"),
          (call_script,"script_mp_assign_6_equipment","itm_quarter_staff","itm_wooden_stick",0,0,0,"itm_stones"),
          (call_script,"script_mp_assign_6_equipment","itm_gael_tunic_08","itm_gael_hoodtunic_09","itm_gael_hoodtunic_10",0,0,0),#hood tunic
          (call_script,"script_mp_assign_6_equipment","itm_briton_tunic24","itm_briton_tunic25","itm_briton_tunic26","itm_briton_tunic27","itm_gael_hoodtunic_11",0),#tunic
          (call_script,"script_mp_assign_6_equipment","itm_phrygian4","itm_phrygian9","itm_phrygian14",0,0,0),
          (assign,"$temp","trp_irish_elite"),
        (else_try),
          (assign,"$temp","trp_irish_capitan"),
        (try_end),
      (try_end),
      
      ####SCOTCH EQUIPMENT
      (assign,"$temp","trp_scotch_multiplayer"),
      (try_for_range,":unused",0,3),
        #weapons
        (call_script,"script_mp_assign_6_equipment","itm_seax_1","itm_knife4","itm_irish_short_sword2",0,0,0),
        (call_script,"script_mp_assign_6_equipment",0,"itm_pictish_hatchet8",0,"itm_pictish_hatchet9","itm_pictish_hatchet7","itm_pictish_hatchet10"),
        (call_script,"script_mp_assign_6_equipment",0,"itm_long_light_spear1","itm_long_light_spear2",0,0,0),
        #armor
        (call_script,"script_mp_assign_6_equipment","itm_just_man_boots_medium","itm_just_man_boots_light","itm_just_man_boots_dark","itm_carbatinae_12q",0,0),
        (call_script,"script_mp_assign_6_equipment","itm_leather_gloves",0,0,0,0,0),
        (call_script,"script_mp_assign_6_equipment","itm_picts_hoodtunic_15","itm_picts_hoodtunic_16","itm_picts_hoodtunic_14","itm_picts_hoodtunic_17",0,0),#hood tunic
        (call_script,"script_mp_assign_6_equipment","itm_picts_hoodtunic_11","itm_picts_hoodtunic_12",0,"itm_briton_tunic19","itm_picts_hoodtunic_13",0),#tunic
        (call_script,"script_mp_assign_6_equipment","itm_gambeson1cloak","itm_gambeson1gael","itm_gambeson2gael","itm_gambeson3gael","itm_gambeson4gael",0),#gambeson
        #shields
        (call_script,"script_mp_assign_6_equipment","itm_squaresh_2","itm_squaresh_5","itm_h_shield2","itm_h_shield4","itm_tab_shield_small_round_c",0),
        #helmets
        (call_script,"script_mp_assign_6_equipment","itm_angle_helmet5","itm_angle_helmet6","itm_angle_helmet4","itm_angle_helmet3",0,0),
        #horses
        (call_script,"script_mp_assign_6_equipment","itm_wild_pony","itm_wild_pony2","itm_wild_horse","itm_wild_horse",0,0),
        ###additional (not for captain)
        (neq,"$temp","trp_scotch_capitan"),
        (call_script,"script_mp_assign_6_equipment","itm_horn_multi","itm_standard","itm_standard_dragon",0,0,"itm_long_war_spear2"),
        (call_script,"script_mp_assign_6_equipment","itm_throwing_spears2","itm_javelin_skirmishesel","itm_crossbow_mp","itm_bolts_mp",0,0),#"itm_long_bow","itm_arrows",0,0),
        (call_script,"script_mp_assign_6_equipment","itm_irish_long_sword7",0,0,0,0,0),
        (call_script,"script_mp_assign_6_equipment","itm_mail_shirt_6","itm_mail_shirt_7","itm_mail_shirt_11_3","itm_mail_shirt_2","itm_mail_shirt_5",0),#mail
        (try_begin),
          (eq,"$temp","trp_scotch_multiplayer"),
          (call_script,"script_mp_assign_6_equipment","itm_quarter_staff","itm_wooden_stick",0,0,0,"itm_stones"),
          (call_script,"script_mp_assign_6_equipment","itm_pictish_painted1","itm_pictish_painted2","itm_pictish_painted3",0,"itm_picts_hoodtunic_01",0),#naked
          (call_script,"script_mp_assign_6_equipment","itm_picts_hoodtunic_03","itm_picts_hoodtunic_04","itm_picts_hoodtunic_05","itm_picts_hoodtunic_06",0,0),#hood naked
          (call_script,"script_mp_assign_6_equipment","itm_phrygian8","itm_phrygian11","itm_phrygian15",0,0,0),
          (assign,"$temp","trp_scotch_elite"),
        (else_try),
          (assign,"$temp","trp_scotch_capitan"),
        (try_end),
      (try_end),
      
  ]),
  ("mp_spawn_useable_items",[
      (try_begin),
        (multiplayer_is_server),
        ###ITEMS
        (try_for_range, ":item", all_items_begin, "itm_ship_data"),
          (scene_item_get_num_instances,":num_instances",":item"),
          (item_get_type,":type",":item"),
          (neg|is_between,":type",itp_type_goods,itp_type_pistol),
          (neq,":type",itp_type_horse),
          (neq,":type",itp_type_animal),
          (neq,":type",itp_type_book),
          (try_for_range,":cur_instance",0,":num_instances"),
            (scene_item_get_instance,":scene_item",":item",":cur_instance"),
            (prop_instance_get_variation_id_2,":mode",":scene_item"),
            (assign,":stop",1),
            (try_begin),
              (eq,":mode",0),
              (assign,":stop",0),
            (else_try),
              (eq,":mode",1),
              (eq, "$g_multiplayer_game_type", multiplayer_game_type_raid),
              (assign,":stop",0),
            (try_end),
            (eq,":stop",0),
            (prop_instance_get_variation_id,":how_much",":scene_item"),
            (gt,":how_much",0),
            (position_set_x,pos0,-100000),
            (position_set_y,pos0,-100000),
            (position_set_z,pos0,-100000),
            (prop_instance_animate_to_position,":scene_item",pos0,0),
            (prop_instance_get_starting_position,pos1,":scene_item"),
            
            (set_spawn_position, pos1),
            (store_sub,":prev_item",":item",1),
            (try_begin),
              (item_has_property,":prev_item",itp_next_item_as_melee),
              (assign,":item",":prev_item"),
            (try_end),
            (try_for_range,":unused",0,":how_much"),
              (spawn_item,":item",0,999999),
            (try_end),
          (try_end),
        (try_end),
      (try_end),
  ]),
  ("mp_set_item_prices",[
      #(store_script_param,":slot",1),
      (try_for_range, ":slot", slot_item_multiplayer_faction_price_multipliers_begin, slot_item_multiplayer_item_class),
        (try_for_range,":item","itm_longseax1","itm_seax_1"),
          (item_set_slot, ":item", ":slot", 32),
        (try_end),
        (try_for_range,":item","itm_seax_1","itm_ragnar_seax"),
          (item_set_slot, ":item", ":slot", 45),
        (try_end),
        #norse
        (item_set_slot, "itm_hand_axe", ":slot", 100),
        (item_set_slot, "itm_one_handed_war_axe_a", ":slot", 110),
        (item_set_slot, "itm_axe_3", ":slot", 130),
        #saxon
        (item_set_slot, "itm_one_handed_war_axe_b", ":slot", 110),
        (item_set_slot, "itm_axe_2", ":slot", 100),
        #angle
        (item_set_slot, "itm_spatha", ":slot", 22),
        (item_set_slot, "itm_spatha_7", ":slot", 22),
        (item_set_slot, "itm_noble_sword", ":slot", 20),
        (item_set_slot, "itm_noble_sword_2", ":slot", 20),
        #briton
        (item_set_slot, "itm_old_swordv", ":slot", 20),
        (item_set_slot, "itm_noble_sword_7", ":slot", 20),
        (item_set_slot, "itm_noble_sword_12", ":slot", 20),
        
        
        #irish
        (item_set_slot, "itm_pictish_hatchet13", ":slot", 85),
        (item_set_slot, "itm_pictish_hatchet12", ":slot", 110),
        (item_set_slot, "itm_pictish_hatchet", ":slot", 115),
        (item_set_slot, "itm_pictish_hatchet15", ":slot", 160),
        (item_set_slot, "itm_pictish_hatchet3", ":slot", 150),
        (item_set_slot, "itm_irish_short_sword1", ":slot", 26),
        (item_set_slot, "itm_irish_long_sword4", ":slot", 22),
        (item_set_slot, "itm_irish_long_sword2", ":slot", 25),
        (item_set_slot, "itm_championsword2", ":slot", 30),
        #scotch
        (item_set_slot, "itm_pictish_hatchet8", ":slot", 86),
        (item_set_slot, "itm_pictish_hatchet7", ":slot", 100),
        (item_set_slot, "itm_pictish_hatchet10", ":slot", 115),
        (item_set_slot, "itm_pictish_hatchet9", ":slot", 150),
        (item_set_slot, "itm_irish_short_sword2", ":slot", 20),
        (item_set_slot, "itm_irish_long_sword7", ":slot", 22),
        
        
        
        (item_set_slot, "itm_bare_foot_man", ":slot", 60),
        (item_set_slot, "itm_carbatinae_1", ":slot", 60),
        (item_set_slot, "itm_carbatinae_10", ":slot", 65),
        (item_set_slot, "itm_carbatinae_11q", ":slot", 60),
        (item_set_slot, "itm_carbatinae_12q", ":slot", 60),
        (item_set_slot, "itm_carbatinae_11qs", ":slot", 57),
        (item_set_slot, "itm_carbatinae_12qs", ":slot", 56),
        (item_set_slot, "itm_carbatinae_13qs", ":slot", 62),
        (item_set_slot, "itm_carbatinae_14qs", ":slot", 65),
        (item_set_slot, "itm_carbatinae_1s", ":slot", 60),
        (item_set_slot, "itm_carbatinae_2s", ":slot", 60),
        (item_set_slot, "itm_carbatinae_2v", ":slot", 60),
        (item_set_slot, "itm_carbatinae_3", ":slot", 60),
        (item_set_slot, "itm_carbatinae_3s", ":slot", 60),
        (item_set_slot, "itm_carbatinae_3v", ":slot", 60),
        (item_set_slot, "itm_carbatinae_4", ":slot", 60),
        (item_set_slot, "itm_carbatinae_4s", ":slot", 65),
        (item_set_slot, "itm_carbatinae_5", ":slot", 61),
        (item_set_slot, "itm_carbatinae_5s", ":slot", 70),
        (item_set_slot, "itm_carbatinae_5v", ":slot", 70),
        (item_set_slot, "itm_carbatinae_6", ":slot", 60),
        (item_set_slot, "itm_carbatinae_6s", ":slot", 100),
        (item_set_slot, "itm_carbatinae_6v", ":slot", 58),
        (item_set_slot, "itm_carbatinae_7", ":slot", 60),
        (item_set_slot, "itm_carbatinae_8", ":slot", 60),
        (item_set_slot, "itm_carbatinae_9", ":slot", 65),
        (item_set_slot, "itm_carbatinae_vc1", ":slot", 70),
        (item_set_slot, "itm_carbatinae_vc1v", ":slot", 75),
        (item_set_slot, "itm_carbatinae_vc2", ":slot", 73),
        (item_set_slot, "itm_carbatinae_vc2s", ":slot", 90),
        (item_set_slot, "itm_carbatinae_vc3", ":slot", 62),
        (item_set_slot, "itm_carbatinae_vc6", ":slot", 75),
        (item_set_slot, "itm_gaelshoes_1", ":slot", 60),
        (item_set_slot, "itm_gaelshoes_2", ":slot", 60),
        (item_set_slot, "itm_gaelshoes_3", ":slot", 60),
        (item_set_slot, "itm_just_man_boots_dark", ":slot", 60),
        (item_set_slot, "itm_just_man_boots_light", ":slot", 100),
        (item_set_slot, "itm_just_man_boots_medium", ":slot", 60),
        ##helmets
        (item_set_slot, "itm_phrygian1", ":slot", 50),
        (item_set_slot, "itm_phrygian2", ":slot", 50),
        (item_set_slot, "itm_phrygian3", ":slot", 50),
        (item_set_slot, "itm_phrygian4", ":slot", 50),
        (item_set_slot, "itm_phrygian5", ":slot", 50),
        (item_set_slot, "itm_phrygian6", ":slot", 50),
        (item_set_slot, "itm_phrygian7", ":slot", 50),
        (item_set_slot, "itm_phrygian8", ":slot", 50),
        (item_set_slot, "itm_phrygian9", ":slot", 50),
        (item_set_slot, "itm_phrygian10", ":slot", 50),
        (item_set_slot, "itm_phrygian11", ":slot", 50),
        (item_set_slot, "itm_phrygian12", ":slot", 50),
        (item_set_slot, "itm_phrygian13", ":slot", 50),
        (item_set_slot, "itm_phrygian14", ":slot", 50),
        (item_set_slot, "itm_phrygian15", ":slot", 50),
        (item_set_slot, "itm_phrygian16", ":slot", 50),
        (item_set_slot, "itm_phrygian17", ":slot", 50),
        ###
        (item_set_slot, "itm_vikingold_helm15", ":slot", 19),
        (item_set_slot, "itm_viking_elitehelm1", ":slot", 18),
        (item_set_slot, "itm_viking_helm15", ":slot", 17),
        (item_set_slot, "itm_viking_elitehelm2", ":slot", 18),
        (item_set_slot, "itm_viking_helm16", ":slot", 17),
        (item_set_slot, "itm_viking_noblehelm1", ":slot", 15),
        (item_set_slot, "itm_vikingold_helm14", ":slot", 25),
        (item_set_slot, "itm_viking_elitehelm3", ":slot", 19),
        (item_set_slot, "itm_viking_helm16", ":slot", 17),
        (item_set_slot, "itm_viking_elitehelm4", ":slot", 19),
        (item_set_slot, "itm_viking_helm17", ":slot", 17),
        (item_set_slot, "itm_vikingold_elitehelm9", ":slot", 22),
        (item_set_slot, "itm_spangenhelm_3", ":slot", 35),
        (item_set_slot, "itm_spangenhelm_1", ":slot", 20),
        (item_set_slot, "itm_spangenhelm_19", ":slot", 19),
        (item_set_slot, "itm_spangenhelm_14", ":slot", 17),
        (item_set_slot, "itm_spangenhelm_39", ":slot", 17),
        (item_set_slot, "itm_spangenhelm_17", ":slot", 17),
        (item_set_slot, "itm_spangenhelm_22", ":slot", 19),
        (item_set_slot, "itm_spangenhelm_4", ":slot", 35),
        (item_set_slot, "itm_spangenhelm_2", ":slot", 20),
        (item_set_slot, "itm_spangenhelm_20", ":slot", 19),
        (item_set_slot, "itm_spangenhelm_13", ":slot", 17),
        (item_set_slot, "itm_spangenhelm_16", ":slot", 17),
        (item_set_slot, "itm_spangenhelm_7", ":slot", 25),
        (item_set_slot, "itm_spangenhelm_5", ":slot", 19),
        (item_set_slot, "itm_spangenhelm_21", ":slot", 19),
        (item_set_slot, "itm_spangenhelm_15", ":slot", 17),
        (item_set_slot, "itm_spangenhelm_40", ":slot", 17),
        (item_set_slot, "itm_spangenhelm_38", ":slot", 15),
        (item_set_slot, "itm_spangenhelm_28", ":slot", 20),
        (item_set_slot, "itm_spangenhelm_8", ":slot", 20),
        (item_set_slot, "itm_spangenhelm_6", ":slot", 19),
        (item_set_slot, "itm_spangenhelm_25", ":slot", 18),
        (item_set_slot, "itm_spangenhelm_35", ":slot", 16),
        (item_set_slot, "itm_spangenhelm_18", ":slot", 18),
        (item_set_slot, "itm_briton_helm3", ":slot", 35),
        (item_set_slot, "itm_briton_helm", ":slot", 20),
        (item_set_slot, "itm_briton_helm19", ":slot", 19),
        (item_set_slot, "itm_briton_helm13", ":slot", 17),
        (item_set_slot, "itm_briton_helm22", ":slot", 25),
        (item_set_slot, "itm_briton_helm33", ":slot", 20),
        (item_set_slot, "itm_briton_helm4", ":slot", 35),
        (item_set_slot, "itm_briton_helm2", ":slot", 20),
        (item_set_slot, "itm_briton_helm20", ":slot", 19),
        (item_set_slot, "itm_briton_helm14", ":slot", 17),
        (item_set_slot, "itm_briton_helm23", ":slot", 25),
        (item_set_slot, "itm_briton_helm34", ":slot", 20),
        (item_set_slot, "itm_angle_helmet1", ":slot", 17),
        (item_set_slot, "itm_angle_helmet2", ":slot", 19),
        (item_set_slot, "itm_angle_helmet3", ":slot", 17),
        (item_set_slot, "itm_angle_helmet4", ":slot", 19),
        (item_set_slot, "itm_angle_helmet5", ":slot", 19),
        (item_set_slot, "itm_angle_helmet6", ":slot", 22),
        (item_set_slot, "itm_angle_helmet4", ":slot", 19),
        (item_set_slot, "itm_angle_helmet3", ":slot", 17),
        #armors
        (item_set_slot, "itm_pictish_painted1", ":slot", 70),
        (item_set_slot, "itm_pictish_painted2", ":slot", 70),
        (item_set_slot, "itm_pictish_painted3", ":slot", 70),
        (item_set_slot, "itm_pictish_painted4", ":slot", 70),
        (item_set_slot, "itm_picts_hoodtunic_01", ":slot", 58),
        (item_set_slot, "itm_picts_hoodtunic_03", ":slot", 70),
        (item_set_slot, "itm_picts_hoodtunic_04", ":slot", 165),
        (item_set_slot, "itm_picts_hoodtunic_05", ":slot", 70),
        (item_set_slot, "itm_picts_hoodtunic_06", ":slot", 151),
        (item_set_slot, "itm_bl_tunic07", ":slot", 70),
        (item_set_slot, "itm_bl_tunic11", ":slot", 64),
        (item_set_slot, "itm_bl_tunic12", ":slot", 64),
        (item_set_slot, "itm_briton_tunic18", ":slot", 70),
        (item_set_slot, "itm_briton_tunic24", ":slot", 47),
        (item_set_slot, "itm_briton_tunic25", ":slot", 70),
        (item_set_slot, "itm_briton_tunic26", ":slot", 70),
        (item_set_slot, "itm_briton_tunic27", ":slot", 70),
        (item_set_slot, "itm_briton_tunic3", ":slot", 70),
        (item_set_slot, "itm_briton_tunic4", ":slot", 70),
        (item_set_slot, "itm_briton_tunic5", ":slot", 70),
        (item_set_slot, "itm_btunic_13", ":slot", 70),
        (item_set_slot, "itm_btunic_7woman", ":slot", 47),
        (item_set_slot, "itm_btunic_9", ":slot", 78),
        (item_set_slot, "itm_gael_tunic_03", ":slot", 70),
        (item_set_slot, "itm_picts_hoodtunic_13", ":slot", 70),
        (item_set_slot, "itm_ptunic_10", ":slot", 70),
        (item_set_slot, "itm_ptunic_6", ":slot", 64),
        (item_set_slot, "itm_red_cloak", ":slot", 47),
        (item_set_slot, "itm_bl_tunic06", ":slot", 77),
        (item_set_slot, "itm_btunic_4", ":slot", 77),
        (item_set_slot, "itm_btunic_8", ":slot", 77),
        (item_set_slot, "itm_gael_hoodtunic_09", ":slot", 140),
        (item_set_slot, "itm_gael_hoodtunic_10", ":slot", 70),
        (item_set_slot, "itm_gael_hoodtunic_11", ":slot", 70),
        (item_set_slot, "itm_gael_tunic_08", ":slot", 140),
        (item_set_slot, "itm_picts_hoodtunic_11", ":slot", 70),
        (item_set_slot, "itm_picts_hoodtunic_12", ":slot", 70),
        (item_set_slot, "itm_picts_hoodtunic_15", ":slot", 140),
        (item_set_slot, "itm_picts_hoodtunic_16", ":slot", 70),
        (item_set_slot, "itm_picts_hoodtunic_17", ":slot", 70),
        (item_set_slot, "itm_ptunic_11", ":slot", 70),
        (item_set_slot, "itm_bl_tunic08", ":slot", 70),
        (item_set_slot, "itm_bl_tunic10", ":slot", 70),
        (item_set_slot, "itm_briton_tunic13", ":slot", 80),
        (item_set_slot, "itm_btunic_3", ":slot", 80),
        (item_set_slot, "itm_ptunic_7", ":slot", 70),
        (item_set_slot, "itm_ptunic_8", ":slot", 70),
        (item_set_slot, "itm_blue_cloak", ":slot", 77),
        (item_set_slot, "itm_leather_cloak", ":slot", 77),
        (item_set_slot, "itm_picts_hoodtunic_14", ":slot", 140),
        (item_set_slot, "itm_btunic_14", ":slot", 81),
        (item_set_slot, "itm_btunic_2woman", ":slot", 70),
        (item_set_slot, "itm_nobleman_outfit", ":slot", 70),
        (item_set_slot, "itm_btunic_12", ":slot", 77),
        (item_set_slot, "itm_bl_tunic02", ":slot", 70),
        (item_set_slot, "itm_ptunic_12", ":slot", 70),
        (item_set_slot, "itm_brat3", ":slot", 70),
        (item_set_slot, "itm_brat4", ":slot", 70),
        (item_set_slot, "itm_btunic_15", ":slot", 77),
        (item_set_slot, "itm_briton_tunic19", ":slot", 70),
        (item_set_slot, "itm_briton_tunic8", ":slot", 70),
        (item_set_slot, "itm_btunic_16", ":slot", 70),
        (item_set_slot, "itm_picts_tunic_12", ":slot", 70),
        (item_set_slot, "itm_bl_tunic09", ":slot", 70),
        (item_set_slot, "itm_ptunic_2", ":slot", 70),
        (item_set_slot, "itm_ptunic_9", ":slot", 70),
        (item_set_slot, "itm_gambeson14gael", ":slot", 84),
        (item_set_slot, "itm_gambeson15gael", ":slot", 70),
        (item_set_slot, "itm_gambeson16gael", ":slot", 84),
        (item_set_slot, "itm_gambeson1cloak", ":slot", 84),
        (item_set_slot, "itm_gambeson2gael", ":slot", 77),
        (item_set_slot, "itm_gambeson37", ":slot", 70),
        (item_set_slot, "itm_gambeson3gael", ":slot", 84),
        (item_set_slot, "itm_gambeson4", ":slot", 84),
        (item_set_slot, "itm_gambeson4gael", ":slot", 84),
        (item_set_slot, "itm_gambeson6", ":slot", 70),
        (item_set_slot, "itm_gambeson25", ":slot", 67),
        (item_set_slot, "itm_gambeson27", ":slot", 74),
        (item_set_slot, "itm_gambeson36", ":slot", 67),
        (item_set_slot, "itm_gambeson42", ":slot", 67),
        (item_set_slot, "itm_gambeson12gael", ":slot", 77),
        (item_set_slot, "itm_gambeson13gael", ":slot", 77),
        (item_set_slot, "itm_gambeson1gael", ":slot", 77),
        (item_set_slot, "itm_gambeson28", ":slot", 85),
        (item_set_slot, "itm_gambeson3", ":slot", 70),
        (item_set_slot, "itm_gambeson32", ":slot", 70),
        (item_set_slot, "itm_gambeson41", ":slot", 67),
        (item_set_slot, "itm_gambeson1", ":slot", 79),
        (item_set_slot, "itm_gambeson2", ":slot", 89),
        (item_set_slot, "itm_gambeson34", ":slot", 82),
        (item_set_slot, "itm_gambeson38", ":slot", 84),
        (item_set_slot, "itm_gambeson40", ":slot", 62),#56
        (item_set_slot, "itm_gambeson39", ":slot", 77),
        (item_set_slot, "itm_gambeson29", ":slot", 88),
        (item_set_slot, "itm_gambeson35", ":slot", 81),
        (item_set_slot, "itm_bl_tunic03", ":slot", 105),
        (item_set_slot, "itm_gambeson43", ":slot", 76),
        (item_set_slot, "itm_gambeson26", ":slot", 77),
        (item_set_slot, "itm_mail_shirt_2", ":slot", 49),
        (item_set_slot, "itm_mail_shirt_5", ":slot", 49),
        (item_set_slot, "itm_mail_shirt_6", ":slot", 49),
        (item_set_slot, "itm_byrnie10", ":slot", 50),
        (item_set_slot, "itm_byrnie37", ":slot", 50),
        (item_set_slot, "itm_byrnie13", ":slot", 36),
        (item_set_slot, "itm_byrnie14", ":slot", 36),
        (item_set_slot, "itm_mail_shirt_11_3", ":slot", 36),
        (item_set_slot, "itm_mail_shirt_7", ":slot", 36),
        (item_set_slot, "itm_byrnie16", ":slot", 36),
        (item_set_slot, "itm_byrnie17", ":slot", 36),
        (item_set_slot, "itm_byrnie21", ":slot", 36),
        (item_set_slot, "itm_byrnie23", ":slot", 36),
        (item_set_slot, "itm_byrnie36", ":slot", 36),
        (item_set_slot, "itm_byrnie38", ":slot", 36),
        (item_set_slot, "itm_byrnie5", ":slot", 36),
        (item_set_slot, "itm_byrnie9", ":slot", 36),
        (item_set_slot, "itm_byrnie22", ":slot", 33),
        (item_set_slot, "itm_byrnie4", ":slot", 30),
        (item_set_slot, "itm_byrnie6", ":slot", 33),
        (item_set_slot, "itm_byrnie18", ":slot", 34),
        (item_set_slot, "itm_byrnie19", ":slot", 34),
        (item_set_slot, "itm_byrnie25", ":slot", 34),
        (item_set_slot, "itm_byrnie26", ":slot", 34),
        (item_set_slot, "itm_byrnie32", ":slot", 27),
        (item_set_slot, "itm_mail_shirt_13_3", ":slot", 34),
        (item_set_slot, "itm_mail_shirt_13_4", ":slot", 27),
        (item_set_slot, "itm_mail_shirt_5_1", ":slot", 26),
        (item_set_slot, "itm_mail_shirt_5_2", ":slot", 25),
        (item_set_slot, "itm_byrnie29", ":slot", 34),
        (item_set_slot, "itm_byrnie31", ":slot", 34),
        (item_set_slot, "itm_mail_shirt_13_2", ":slot", 34),
        (item_set_slot, "itm_byrnie15", ":slot", 29),
        (item_set_slot, "itm_addon_mail7", ":slot", 24),
        (item_set_slot, "itm_addon_mail4", ":slot", 25),
      (try_end),
  ]),
  ("mp_set_item_price_for_game_type",[
      (try_begin),
        (eq, "$g_multiplayer_game_type", multiplayer_game_type_raid),
        (try_for_range,":slot",slot_item_multiplayer_faction_price_multipliers_begin,slot_item_multiplayer_faction_price_multipliers_begin+10),
          (item_set_slot,"itm_pitch_fork",":slot",1000),
          (item_set_slot,"itm_battle_fork",":slot",1000),
        (try_end),
      (else_try),
        (try_for_range,":slot",slot_item_multiplayer_faction_price_multipliers_begin,slot_item_multiplayer_faction_price_multipliers_begin+10),
          (item_set_slot,"itm_pitch_fork",":slot",100),
          (item_set_slot,"itm_battle_fork",":slot",100),
        (try_end),
      (try_end),
  ]),
  ("z_code_time_and_weather",[
      (store_script_param,":instance",1),
      (store_current_scene,":scene"),
      
      ##TIME
      (prop_instance_get_variation_id,":hour",":instance"),
      (try_begin),
        (this_or_next|is_between,":hour",21,25),
        (is_between,":hour",1,5),
        (scene_set_slot,":scene",slot_scene_time,time_night),
      (else_try),
        (is_between,":hour",5,11),
        (scene_set_slot,":scene",slot_scene_time,time_dawn),
      (else_try),
        (is_between,":hour",11,18),
        (scene_set_slot,":scene",slot_scene_time,time_noon),
      (else_try),
        (is_between,":hour",18,21),
        (scene_set_slot,":scene",slot_scene_time,time_dusk),
      (try_end),
      
      ##WEATHER
      (prop_instance_get_variation_id_2,":weather",":instance"),
      (val_sub,":weather",1),
      (try_begin),
        (is_between,":weather",weather_clear,weather_seastorm+1),
        
        (neg|is_between,":weather", 4,8),##todo not assigned
        
        (scene_set_slot,":scene",slot_scene_weather,":weather"),
      (try_end),
  ]),
  ("z_code_season",[
      (store_script_param,":instance",1),
      (prop_instance_get_variation_id,":season",":instance"),
      (val_sub,":season",1),
      (try_begin),
        (is_between,":season",shader_spring,shader_winter+1),
        (assign,"$shader_season",":season"),
      (try_end),
  ]),
  ("z_code_scene_sounds",[
      (store_script_param,":instance",1),
      (prop_instance_get_variation_id,":sounds",":instance"),
      (val_sub,":sounds",1),
      (store_current_scene,":scene"),
      (try_begin),
        (is_between,":sounds",sounds_plain,sounds_sea+1),
        (scene_set_slot,":scene",slot_scene_sounds,":sounds"),
      (try_end),
  ]),
  ("cf_no_mp_cavalry_troops_for_naval_battles",[
      (assign,":stop",1),
      (try_begin),
        (neq,"$g_multiplayer_game_type",multiplayer_game_type_sea),
        (assign,":stop",0),
      (else_try),
        (store_script_param,":troop",1),
        (neq,":troop","trp_mp_norse_cavalry"),
        (neq,":troop","trp_mp_saxon_cavalry"),
        (neq,":troop","trp_mp_angle_cavalry"),
        (neq,":troop","trp_mp_briton_cavalry"),
        (neq,":troop","trp_mp_irish_cavalry"),
        (neq,":troop","trp_mp_scotch_cavalry"),
        (assign,":stop",0),
      (try_end),
      (eq,":stop",0),
  ]),
  ("cf_agent_is_not_peasant",[
      (store_script_param,":agent",1),
      (agent_get_troop_id,":troop",":agent"),
      (neq,":troop","trp_mp_norse_peasant"),
      (neq,":troop","trp_mp_saxon_peasant"),
      (neq,":troop","trp_mp_angle_peasant"),
      (neq,":troop","trp_mp_briton_peasant"),
      (neq,":troop","trp_mp_irish_peasant"),
      (neq,":troop","trp_mp_scotch_peasant"),
  ]),
  ("mp_change_player_team",[
      (store_script_param,":player",1),
      (store_script_param,":team",2),
      (try_begin),
        #if player is living add +1 to his kill count because he will get -1 because of team change while living.
        (player_get_agent_id,":agent",":player"),
        (agent_is_active,":agent"),
        (agent_is_alive,":agent"),
        (player_get_kill_count,":player_kill_count",":player"), #adding 1 to his kill count, because he will lose 1 undeserved kill count for dying during team change
        (val_add,":player_kill_count",1),
        (player_set_kill_count,":player",":player_kill_count"),
        
        (player_get_death_count,":player_death_count",":player"), #subtracting 1 to his death count, because he will gain 1 undeserved death count for dying during team change
        (val_sub,":player_death_count",1),
        (player_set_death_count,":player",":player_death_count"),
        
        (player_get_score,":player_score",":player"), #adding 1 to his score count, because he will lose 1 undeserved score for dying during team change
        (val_add,":player_score",1),
        (player_set_score,":player",":player_score"),
        
        (try_for_players,":player_no",1), #0 is server so starting from 1
          (player_is_active,":player_no"),
          (multiplayer_send_4_int_to_player,":player_no", multiplayer_event_set_player_score_kill_death, ":player", ":player_score", ":player_kill_count", ":player_death_count"),
        (try_end),
        
        (player_get_value_of_original_items, ":old_items_value", ":player"),
        (player_get_gold, ":player_gold", ":player"),
        (val_add, ":player_gold", ":old_items_value"),
        (player_set_gold, ":player", ":player_gold", multi_max_gold_that_can_be_stored),
      (try_end),
      
      (player_set_troop_id,":player",-1),
      (player_set_team_no,":player",":team"),
  ]),
  ("cf_mp_gender_check",[
      (store_script_param,":item",1),
      (multiplayer_get_my_player,":player"),
      (player_get_gender,":gender",":player"),
      (assign,":stop",0),
      (try_begin),
        (eq,":gender",0),#male
        (eq,":item","itm_briton_tunic17"),###add to scripts, add to troops
        (assign,":stop",1),
      (else_try),
        (eq,":gender",1),#female
        (is_between,":item","itm_pictish_painted1","itm_picts_hoodtunic_02"),  #VC-3886 allow female picts access to same bonus
        # (this_or_next|is_between,":item","itm_pictish_painted1","itm_picts_hoodtunic_07"),
        # (eq,":item","itm_picts_hoodtunic_07"),
        (assign,":stop",1),
      (try_end),
      (eq,":stop",0),
  ]),
  ("mp_replace_default_armor",[
      (store_script_param,":agent",1),
      (try_begin),
        (agent_is_active,":agent"),
        (agent_is_alive,":agent"),
        (agent_get_item_slot,":item",":agent",ek_body),
        (this_or_next|is_between,":item","itm_pictish_painted1","itm_picts_hoodtunic_02"),  #VC-3886 allow female picts access to same bonus
        # (this_or_next|is_between,":item","itm_pictish_painted1","itm_picts_hoodtunic_07"),
        # (this_or_next|eq,":item","itm_picts_hoodtunic_07"),
        (eq,":item","itm_briton_tunic17"),
        (agent_get_player_id,":player",":agent"),
        (player_is_active,":player"),
        (player_get_gender,":gender",":player"),
        (try_begin),
          (eq,":gender",0),#male
          (eq,":item","itm_briton_tunic17"),
          (agent_unequip_item, ":agent", ":item"),
          (agent_equip_item,":agent","itm_pictish_painted1"),
        (else_try),
          (eq,":gender",1),#female
          (is_between,":item","itm_pictish_painted1","itm_picts_hoodtunic_02"),  #VC-3886 allow female picts access to same bonus
          # (this_or_next|is_between,":item","itm_pictish_painted1","itm_picts_hoodtunic_07"),
          # (eq,":item","itm_picts_hoodtunic_07"),
          (agent_unequip_item, ":agent", ":item"),
          (agent_equip_item, ":agent", "itm_briton_tunic17"),
        (try_end),
      (try_end),
  ]),
  ("mp_get_num_of_bots",[
      (assign,":num_1","$g_multiplayer_num_bots_team_1"),
      (assign,":num_2","$g_multiplayer_num_bots_team_2"),
      (try_begin),
        (eq,":num_1",0),
        (eq,"$g_multiplayer_game_type",multiplayer_game_type_lords_battle),
        (assign,":num_1",100),
      (try_end),
      (try_begin),
        (eq,":num_2",0),
        (eq,"$g_multiplayer_game_type",multiplayer_game_type_lords_battle),
        (assign,":num_2",100),
      (try_end),
      (assign,reg1,":num_1"),
      (assign,reg2,":num_2"),
  ]),
  ("mp_get_ship_type_for_spawning",[
      (store_script_param,":team",1),
      (store_current_scene,":scene"),
      (try_begin),
        (this_or_next|eq,"$g_multiplayer_game_type", multiplayer_game_type_raid),
        (this_or_next|eq,":scene","scn_multi_scene_coast"),
        (eq,":scene","scn_multi_scene_islands"),
        (assign,":num_players",0),
        (assign,":end",5),
      (else_try),
        (try_begin),
          (eq,":team",0),
          (assign,":num_players","$g_multiplayer_num_bots_team_1"),
        (else_try),
          (assign,":num_players","$g_multiplayer_num_bots_team_2"),
        (try_end),
        (assign,":end",7),
      (try_end),
      
      (try_for_players,":player"),
        (player_is_active,":player"),
        (player_get_team_no,":p_team",":player"),
        (eq,":p_team",":team"),
        (val_add,":num_players",1),
      (try_end),
      
      (try_begin),
        (eq,":team",0),
        (val_sub,":num_players","$g_multiplayer_num_agents_team_1_spawned"),
      (else_try),
        (val_sub,":num_players","$g_multiplayer_num_agents_team_2_spawned"),
      (try_end),
      
      (try_begin),
        (lt,":num_players",6),#7
        (assign,":ship",ship_type_byrding),
      (else_try),
        (lt,":num_players",10),#11
        (assign,":ship",ship_type_knorr),
      (else_try),
        (le,":num_players",22),#27
        (assign,":ship",ship_type_snekkja),
      (else_try),
        (le,":num_players",35),
        (store_random_in_range,":ship",3,":end"),
      (else_try),
        (le,":num_players",50),#55
        (store_random_in_range,":ship",2,":end"),
      (else_try),
        (store_random_in_range,":ship",1,5),
      (try_end),
      (assign,"$temp",":ship"),
  ]),
  ("mp_get_agent_speed_modifiers",[
      (store_script_param, ":agent", 1),
      (store_script_param, ":percent", 2),
      (try_begin),
        (agent_is_active,":agent"),
        (agent_get_item_slot,":item",":agent",ek_body),
        # (try_begin),
          # (is_between,":item","itm_pictish_painted1","itm_picts_hoodtunic_01"),
          # (val_add,":percent",10),
        # (else_try),
          # (is_between,":item","itm_picts_hoodtunic_01","itm_picts_hoodtunic_11"),
          # (neq,":item","itm_picts_hoodtunic_04"),
          # (neq,":item","itm_picts_hoodtunic_06"),
          # (val_add,":percent",5),
        # (try_end),
        (try_begin),  #VC-3886 allow female picts access to same bonus
          (is_between,":item","itm_pictish_painted1","itm_picts_hoodtunic_11"),
          (neq,":item","itm_picts_hoodtunic_04"),
          (neq,":item","itm_picts_hoodtunic_06"),
          (val_add,":percent",10),
        (try_end),
      (try_end),
      (assign,reg0,":percent"),
  ]),
  
  
  
]
