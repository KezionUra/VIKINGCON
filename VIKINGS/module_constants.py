from ID_items import *
from ID_quests import *
from ID_factions import *
from header_triggers import *

#######################################
##############################################################
# These constants are used in various files.
# If you need to define a value that will be used in those files,
# just define it here rather than copying it across each file, so
# that it will be easy to change it if you need to.
##############################################################

warband_version = 1170  #matching what is in module.ini
vc_version = 2069

########################################################
##  ITEM SLOTS             #############################
########################################################

slot_item_is_checked               = 0
slot_item_food_bonus               = 1
slot_item_book_reading_progress    = 2
slot_item_book_read                = 3
slot_item_intelligence_requirement = 4
slot_item_alternate                = 5	#table between swing/noswing versions of same weapon

slot_item_amount_available         = 7

slot_item_urban_demand             = 11 #consumer demand for a good in town, measured in abstract units. The more essential the item (ie, like grain) the higher the price
slot_item_rural_demand             = 12 #consumer demand in villages, measured in abstract units
slot_item_desert_demand            = 13 #consumer demand in villages, measured in abstract units

slot_item_production_slot          = 14 
slot_item_production_string        = 15 

slot_item_tied_to_good_price       = 20 #ie, weapons and metal armor to tools, padded to cloth, leather to leatherwork, etc

slot_item_num_positions            = 22
slot_item_positions_begin          = 23 #reserve around 5 slots after this

#alturas 30-32 (see below)

slot_item_primary_raw_material    	  	= 50
slot_item_is_raw_material_only_for      = 51
slot_item_input_number                  = 52 #ie, how many items of inputs consumed per run
slot_item_base_price                    = 53 #taken from module_items
#slot_item_production_site			    = 54 #a string replaced with function - Armagan
slot_item_output_per_run                = 55 #number of items produced per run
slot_item_overhead_per_run              = 56 #labor and overhead per run
slot_item_secondary_raw_material        = 57 #in this case, the amount used is only one
slot_item_enterprise_building_cost      = 58 #enterprise building cost

slot_item_multiplayer_faction_price_multipliers_begin = 60 #reserve around 10 slots after this
slot_item_multiplayer_item_class                      = 70 #temporary, can be moved to higher values
slot_item_multiplayer_availability_linked_list_begin  = 100 #temporary, can be moved to higher values, in Native, there are about 60 of these

########################################################
##  AGENT SLOTS            #############################
########################################################

slot_agent_target_entry_point     = 0
slot_agent_target_x_pos           = 1
slot_agent_target_y_pos           = 2
slot_agent_is_alive_before_retreat= 3
slot_agent_is_in_scripted_mode    = 4
slot_agent_is_not_reinforcement   = 5
slot_agent_tournament_point       = 6
slot_agent_arena_team_set         = 7   #deprecated
slot_agent_spawn_entry_point      = 8
slot_agent_target_prop_instance   = 9
slot_agent_map_overlay_id         = 10
slot_agent_positioned             = 11
slot_agent_initial_ally_power     = 12
slot_agent_initial_enemy_power    = 13
slot_agent_enemy_threat           = 14
slot_agent_is_running_away        = 15
slot_agent_courage_score          = 16
slot_agent_is_respawn_as_bot      = 17
slot_agent_cur_animation          = 18
slot_agent_next_action_time       = 19
slot_agent_state                  = 20
slot_agent_in_duel_with           = 21
slot_agent_duel_start_time        = 22
### PHAIAK begin ( sea battles chief
slot_agent_on_ship                = 23
slot_agent_position_on_ship       = 24
### ) PHAIAK end

slot_agent_walker_occupation      = 25
    
slot_agent_bloodloss_ok           = 26
slot_agent_fatiga                 = 27
slot_agent_fatiga_inicial         = 28

#motomataru agent slots 29-32 (see below)

slot_agent_taunting               = 33
slot_agent_prop                   = 34
slot_agent_is_blocked             = 35
slot_agent_is_chosen              = 36
slot_agent_morale                 = 37
slot_agent_vc_wounded             = 38
slot_agent_ammo_refilled          = 39	#VC-1806
slot_agent_was_dehorsed           = 40
slot_agent_time_without_rider	= slot_agent_was_dehorsed

slot_agent_horn_use_cooldown      = 41
slot_agent_horn_cooldown          = 42
slot_agent_horn_bonus_applied     = 43

slot_agent_berserk_modeon         = 44	#berserker chief mode on
slot_agent_berserk_use_cooldown   = 45
slot_agent_berserk_cooldown       = 46

slot_agent_banner_bonus           = 47
slot_agent_banner_bonus_applied   = 48
slot_agent_shieldwall_bonus       = 49

slot_agent_shieldbash_cooldown    = 50
shielbash_miss_cooldown = 2 #x2 = 2 seconds #12 seconds #before 2, now 30 = more time penalty. VC-2854
shielbash_hit_cooldown = 15 #x2 = 20 seconds # 30 seconds

########################################################
##  FACTION SLOTS          #############################
########################################################
slot_faction_ai_state                   = 4
#slot_faction_ai_state values
sfai_default                   		 = 0 #also defending
sfai_gathering_army            		 = 1
sfai_attacking_center          		 = 2
sfai_raiding_village           		 = 3
sfai_attacking_enemy_army      		 = 4
sfai_attacking_enemies_around_center = 5
sfai_feast             		 		 = 6 #can be feast, wedding, or major tournament
#Social events are a generic aristocratic gathering. Tournaments take place if they are in a town, and hunts take place if they are at a castle.
#Weddings will take place at social events between betrothed couples if they have been engaged for at least a month, if the lady's guardian is the town lord, and if both bride and groom are present

#Rebellion system changes begin
sfai_nascent_rebellion          = 7
#Rebellion system changes end

slot_faction_ai_object                  = 5
slot_faction_ai_rationale               = 6 #Currently unused, can be linked to strings generated from decision checklists
slot_faction_troop_in_player_party      = 7
slot_faction_marshal                    = 8
slot_faction_ai_offensive_max_followers = 9

slot_faction_culture                    = 10
slot_faction_leader                     = 11

slot_faction_temp_slot                  = 12
slot_faction_religion                   = 13  #cb3_christian or cb3_pagan

slot_faction_banner                     = 15

slot_faction_number_of_parties          = 20
slot_faction_state                      = 21

#slot_faction_state values
sfs_active                     = 0
sfs_defeated                   = 1
sfs_inactive                   = 2
# sfs_inactive_rebellion         = 3
# sfs_beginning_rebellion        = 4

# slot_faction_adjective            = 22 MOTO just use fac_culture name 


slot_faction_player_alarm               = 30
slot_faction_last_mercenary_offer_time  = 31
slot_faction_recognized_player          = 32

#overriding troop info for factions in quick start mode.
slot_faction_quick_battle_tier_1_infantry      = 41
slot_faction_quick_battle_tier_2_infantry      = 42
slot_faction_quick_battle_tier_1_archer        = 43
slot_faction_quick_battle_tier_2_archer        = 44
slot_faction_quick_battle_tier_1_cavalry       = 45
slot_faction_quick_battle_tier_2_cavalry       = 46

slot_faction_tier_1_troop         = 41
slot_faction_tier_2_troop         = 42
slot_faction_tier_3_troop         = 43
slot_faction_tier_4_troop         = 44
slot_faction_tier_5_troop         = 45

slot_faction_deserter_troop       = 48
slot_faction_guard_troop          = 49
slot_faction_messenger_troop      = 50
slot_faction_prison_guard_troop   = 51
slot_faction_castle_guard_troop   = 52

slot_faction_town_walker_male_troop      = 53
slot_faction_town_walker_female_troop    = 54
slot_faction_village_walker_male_troop   = 55
slot_faction_village_walker_female_troop = 56
slot_faction_town_spy_male_troop         = 57
slot_faction_town_spy_female_troop       = 58

slot_faction_has_rebellion_chance = 60

slot_faction_instability          = 61 #last time measured

#general diplomacy. 4 options: normal 0, -1 problems, -2 war, 2 alliance
alliance_time       = 120 # days #Really Alliances were more long (even generations), in fact we use affinities in factions.py relations
#alliance expire to truce time
truce_time       = 40 # days #Truce. 1 month of peace. Generally peace was "buying" per a year until vikings back next year


#UNIMPLEMENTED FEATURE ISSUES
slot_faction_war_damage_inflicted_when_marshal_appointed = 62 #Probably deprecate
slot_faction_war_damage_suffered_when_marshal_appointed  = 63 #Probably deprecate

slot_faction_political_issue                             = 64 #Center or marshal appointment
slot_faction_political_issue_time 	                     = 65 #Now is used


#Rebellion changes
#slot_faction_rebellion_target                     = 65
#slot_faction_inactive_leader_location         = 66
#slot_faction_support_base                     = 67
#Rebellion changes


#slot_faction_deserter_party_template       = 62

slot_faction_reinforcements_a        = 77
slot_faction_reinforcements_b        = 78
slot_faction_reinforcements_c        = 79

#slot_faction_num_armies              = 80
slot_faction_num_castles             = 81
slot_faction_num_towns               = 82

slot_faction_last_attacked_center    = 85
slot_faction_last_attacked_hours     = 86
slot_faction_last_safe_hours         = 87

slot_faction_num_routed_agents       = 90

#useful for competitive consumption
slot_faction_biggest_feast_score      = 91
slot_faction_biggest_feast_time       = 92
slot_faction_biggest_feast_host       = 93


#Faction AI states
slot_faction_last_feast_concluded     = 94 #Set when a feast starts -- this needs to be deprecated
slot_faction_last_feast_start_time    = 94 #this is a bit confusing

slot_faction_ai_last_offensive_time   = 95 #Set when an offensive concludes
slot_faction_last_offensive_concluded = 95 #Set when an offensive concludes

slot_faction_ai_last_rest_time        = 96 #the last time that the faction has had default or feast AI -- this determines lords' dissatisfaction with the campaign. Set during faction_ai script
slot_faction_ai_current_state_started = 97 #

slot_faction_ai_last_decisive_event   = 98 #capture a fortress or declaration of war

slot_faction_morale_of_player_troops  = 99
	
#diplomacy
#MOTO chief following in blocks of 40 (32 factions)
slot_faction_truce_days_with_factions_begin 			= 120
slot_faction_provocation_days_with_factions_begin 		= 160
slot_faction_war_damage_inflicted_on_factions_begin 	= 200
# slot_faction_sum_advice_about_factions_begin 			= 240	MOTO not used
slot_faction_neighbors_begin	= 240	#MOTO chief avoid center2 loop by storing results

min_dist_neighb_of_neighb = 31	#Brycheniog to other neighbors of Glywissing 32

#formation faction slots 300-335 (see below)

#revolts -- notes for self
#type 1 -- minor revolt, aimed at negotiating change without changing the ruler
#type 2 -- alternate ruler revolt (ie, pretender, chinese dynastic revolt -- keep the same polity but switch the ruler)
	#subtype -- pretender (keeps the same dynasty)
	#"mandate of heaven" -- same basic rules, but a different dynasty
	#alternate/religious
	#alternate/political
#type 3 -- separatist revolt
	# reGonalist/dynastic (based around an alternate ruling house
	# regionalist/republican
	# messianic (ie, Canudos)
	

########################################################
##  PARTY SLOTS            #############################
########################################################
slot_party_type                = 0  #spt_caravan, spt_town, spt_castle
#slot_party_type values
##spt_caravan            = 1
spt_castle             = 2
spt_town               = 3
spt_village            = 4
#spt_forager            = 5 
##spt_war_party          = 6
##spt_patrol             = 7 #chief 
##spt_messenger          = 8 #chief 
##spt_capitan_mercenario   = 9 #### capitan mercenario chief
spt_levy             = 9
##spt_scout              = 10 #chief
spt_kingdom_caravan    = 11
##spt_prisoner_train     = 12
spt_kingdom_hero_party = 13
##spt_merchant_caravan   = 14
spt_village_farmer     = 15
spt_ship               = 16
spt_cattle_herd        = 17
spt_bandit_lair       = 18
#spt_deserter           = 20  #19 is dplmc_spouse

kingdom_party_types_begin = spt_kingdom_caravan
kingdom_party_types_end = spt_kingdom_hero_party + 1

slot_party_save_icon           = 1  #add motomataru save original icon chief
slot_party_retreat_flag        = 2
slot_party_ignore_player_until = 3
slot_party_ai_state            = 4

#slot_party_ai_state values
spai_undefined                  = -1
spai_besieging_center           = 1
spai_patrolling_around_center   = 4
spai_raiding_around_center      = 5
##spai_raiding_village            = 6
spai_holding_center             = 7
##spai_helping_town_against_siege = 9
spai_engaging_army              = 10
spai_accompanying_army          = 11
spai_screening_army             = 12  #essentially deprecated, as things that routinely counted "accompanying" would miss these. Now represented as accompanying + substate set
spai_trading_with_town          = 13
spai_retreating_to_center       = 14
##spai_trading_within_kingdom     = 15
spai_visiting_village           = 16 #same thing, I think. Recruiting differs from holding because NPC parties don't actually enter villages

slot_party_ai_object           = 5
slot_party_ai_rationale        = 6 #Currently unused, but can be used to save a string explaining the lord's thinking

#slot_town_belongs_to_kingdom   = 6
slot_town_lord                 = 7
stl_unassigned          = -1
stl_reserved_for_player = -2
stl_rejected_by_player  = -3

slot_party_ai_substate         = 8
slot_town_claimed_by_player    = 9

slot_cattle_driven_by_player = slot_town_lord #hack

slot_town_center        = 10
slot_town_castle        = 11
slot_town_prison        = 12
slot_town_tavern        = 13
slot_town_store         = 14
slot_town_arena         = 16
slot_town_alley         = 17
slot_town_walls         = 18
slot_center_culture     = 19

slot_town_tavernkeeper  = 20
slot_town_weaponsmith   = 21
slot_town_armorer       = 22
slot_town_merchant      = 23
slot_town_horse_merchant= 24
slot_town_elder         = 25
slot_center_player_relation = 26

slot_center_siege_with_belfry = 27
slot_center_last_taken_by_troop = 28
slot_town_seneschal  = 29
# party will follow this party if set:
slot_party_commander_party = 30 #default -1   #Deprecate
slot_party_following_player    = 31
slot_party_follow_player_until_time = 32
slot_party_dont_follow_player_until_time = 33

slot_village_raided_by        = 34
slot_village_state            = 35

#slot_village_state values
svs_normal                      = 0
svs_being_raided                = 1
svs_looted                      = 2
# svs_recovering                  = 3
# svs_deserted                    = 4
svs_under_siege                 = 5

slot_village_raid_progress    = 36
slot_village_recover_progress = 37
slot_village_smoke_added      = 38

slot_village_infested_by_bandits   = 39

slot_town_farmer_visits = 45  #debugging
slot_town_farmer_visit_starts = 40  #debugging
slot_town_siege_count = 43  #debugging

slot_center_last_visited_by_lord   = 41

slot_center_last_player_alarm_hour = 42

slot_party_spawned_count = 43
slot_party_spawn_flags   = 44
spsf_coastal  = 0x001
spsf_seaborne = 0x002

slot_village_player_can_not_steal_cattle = 46

slot_center_accumulated_rents      = 47 #collected automatically by NPC lords
slot_center_accumulated_tariffs    = 48 #collected automatically by NPC lords
slot_town_wealth        = 49 #total amount of accumulated wealth in the center, pays for the garrison
slot_town_prosperity    = 50 #affects the amount of wealth generated
slot_town_player_odds   = 51


slot_party_last_toll_paid_hours = 52
slot_party_food_store           = 53 #used for sieges
slot_center_is_besieged_by      = 54 #used for sieges
slot_center_last_spotted_enemy  = 55

castle_food_days        = 8
town_food_days          = 12
average_castle_garrison = 250
average_town_garrison   = 450

slot_party_cached_strength        = 56
slot_party_nearby_friend_strength = 57
slot_party_nearby_enemy_strength  = 58
slot_party_follower_strength      = 59

slot_town_reinforcement_party_template = 60
slot_center_original_faction           = 61
slot_center_ex_faction                 = 62

slot_party_follow_me                   = 63
slot_center_siege_begin_hours          = 64 #used for sieges
slot_center_siege_hardness             = 65

slot_center_sortie_strength            = 66
slot_center_sortie_enemy_strength      = 67

slot_party_last_in_combat              = 68 #used for AI
slot_party_last_in_home_center         = 69 #used for AI
slot_party_leader_last_courted         = 70 #used for AI
slot_party_last_in_any_center          = 71 #used for AI

slot_party_bandit_type                 = 72	#hard defined p_spawn pointer to pt_bandit
slot_party_lair_party                  = 73 #BOTH p_spawn pointer to p_lair AND
slot_party_spawn_point                 = 73 #p_bandit pointer to p_spawn
slot_party_spawn_target_spawns         = 74
slot_party_spawn_radius                = 75

slot_castle_exterior    = slot_town_center

#slot_town_rebellion_contact   = 76
#trs_not_yet_approached  = 0
#trs_approached_before   = 1
#trs_approached_recently = 2

argument_none         = 0
argument_claim        = 1 #deprecate for legal
argument_legal        = 1

argument_ruler        = 2 #deprecate for commons
argument_commons      = 2

argument_benefit      = 3 #deprecate for reward
argument_reward       = 3 

argument_victory      = 4
argument_lords        = 5
argument_rivalries    = 6 #new - needs to be added

slot_town_village_product = 76

slot_town_rebellion_readiness = 77
#(readiness can be a negative number if the rebellion has been defeated)

slot_town_arena_melee_mission_tpl = 78
slot_town_arena_torny_mission_tpl = 79
slot_town_arena_melee_1_num_teams = 80
slot_town_arena_melee_1_team_size = 81
slot_town_arena_melee_2_num_teams = 82
slot_town_arena_melee_2_team_size = 83
slot_town_arena_melee_3_num_teams = 84
slot_town_arena_melee_3_team_size = 85
slot_town_arena_melee_cur_tier    = 86
##slot_town_arena_template	  = 87

slot_center_npc_volunteer_troop_type   = 90
slot_center_npc_volunteer_troop_amount = 91
slot_center_mercenary_troop_type  = 90
slot_center_mercenary_troop_amount= 91
slot_center_volunteer_troop_type  = 92
slot_center_volunteer_troop_amount= 93

slot_center_sailors_troop_amount= 94 #chief sailors recruit

#slot_center_companion_candidate   = 94
slot_center_ransom_broker         = 95
slot_center_tavern_traveler       = 96
slot_center_traveler_info_faction = 97
slot_center_tavern_bookseller     = 98
slot_center_tavern_minstrel       = 99
slot_center_bardo       = 100 #puesto chief para bardos
slot_center_sacerdote       = 101 #puesto chief para sacerdotes
slot_center_quastuosa       = 102 #puesto chief para quastuosa
slot_center_especiales       = 103 #puesto chief para especiales
slot_center_vieja       = 104 #puesto chief para especiales

num_party_loot_slots    = 5
slot_party_next_looted_item_slot  = 109
slot_party_looted_item_1          = 110
slot_party_looted_item_2          = 111
slot_party_looted_item_3          = 112
slot_party_looted_item_4          = 113
slot_party_looted_item_5          = 114
slot_party_looted_item_1_modifier = 115
slot_party_looted_item_2_modifier = 116
slot_party_looted_item_3_modifier = 117
slot_party_looted_item_4_modifier = 118
slot_party_looted_item_5_modifier = 119

slot_village_bound_center         = 120
slot_village_market_town          = 121
slot_village_farmer_party         = 122
slot_party_home_center            = 123 #Required if party_set_faction for non-hero, non-center parties. See defeated faction trigger

slot_center_current_improvement   = 124
slot_center_improvement_end_hour  = 125

slot_party_last_traded_center     = 126 



village_improvements_begin       = 130
slot_center_has_manor            = 130 #village
slot_center_has_fish_pond        = 131 #village
slot_center_has_watch_tower      = 132 #village
slot_center_has_school           = 133 #village
#BUILDINGS BEGIN chief edificios
#religion
slot_center_has_temple1          = 134
#slot_center_has_temple2          = 135
slot_center_has_temple3          = 136
#slot_center_has_temple5          = 137
#
slot_center_has_messenger_post   = 138 #town, castle, village
village_improvements_end         = 139 #chief cambia
slot_center_has_prisoner_tower   = 139 #town, castle
#
slot_center_has_monastery1       = 140
slot_center_has_brewery          = 141
slot_center_has_monastery3       = 142
#slot_center_has_chapel5          = 143
slot_center_has_slavemarket      = 143
slot_center_has_blacksmith       = 144
slot_center_has_guild            = 145
slot_center_has_university       = 146

#BUILDINGS END chief
#chief cambia numeros para evitar equivalencias

walled_center_improvements_begin = slot_center_has_messenger_post
walled_center_improvements_end   = 147 #chief cambia
#chief cambia slots
slot_center_player_enterprise                     = 148 #noted with the item produced
slot_center_player_enterprise_production_order    = 149
slot_center_player_enterprise_consumption_order   = 150 #not used
slot_center_player_enterprise_days_until_complete = 150 #Used instead

slot_center_player_enterprise_balance             = 151 #not used
slot_center_player_enterprise_input_price         = 152 #not used
slot_center_player_enterprise_output_price        = 153 #not used

slot_center_has_bandits                        = 155
slot_town_has_tournament                       = 156
slot_town_tournament_max_teams                 = 157
slot_town_tournament_max_team_size             = 158
slot_center_faction_when_oath_renounced        = 159

slot_center_walker_0_troop                   = 160
slot_center_walker_1_troop                   = 161
slot_center_walker_2_troop                   = 162
slot_center_walker_3_troop                   = 163
slot_center_walker_4_troop                   = 164
slot_center_walker_5_troop                   = 165
slot_center_walker_6_troop                   = 166
slot_center_walker_7_troop                   = 167
slot_center_walker_8_troop                   = 168
slot_center_walker_9_troop                   = 169

slot_center_walker_0_dna                     = 170
slot_center_walker_1_dna                     = 171
slot_center_walker_2_dna                     = 172
slot_center_walker_3_dna                     = 173
slot_center_walker_4_dna                     = 174
slot_center_walker_5_dna                     = 175
slot_center_walker_6_dna                     = 176
slot_center_walker_7_dna                     = 177
slot_center_walker_8_dna                     = 178
slot_center_walker_9_dna                     = 179

slot_center_walker_0_type                    = 180
slot_center_walker_1_type                    = 181
slot_center_walker_2_type                    = 182
slot_center_walker_3_type                    = 183
slot_center_walker_4_type                    = 184
slot_center_walker_5_type                    = 185
slot_center_walker_6_type                    = 186
slot_center_walker_7_type                    = 187
slot_center_walker_8_type                    = 188
slot_center_walker_9_type                    = 189

slot_town_trade_route_1           = 190
slot_town_trade_route_2           = 191
slot_town_trade_route_3           = 192
slot_town_trade_route_4           = 193
slot_town_trade_route_5           = 194
slot_town_trade_route_6           = 195
slot_town_trade_route_7           = 196
slot_town_trade_route_8           = 197
slot_town_trade_route_9           = 198
slot_town_trade_route_10          = 199
slot_town_trade_route_11          = 200
slot_town_trade_route_12          = 201
slot_town_trade_route_13          = 202
slot_town_trade_route_14          = 203
slot_town_trade_route_15          = 204
slot_town_trade_routes_begin = slot_town_trade_route_1
slot_town_trade_routes_end = slot_town_trade_route_15 + 1


#These affect production but in some cases also demand, so it is perhaps easier to itemize them than to have separate 

slot_village_number_of_cattle            = 205
slot_center_head_cattle         = 205 #dried meat, cheese, hides, butter
slot_center_head_sheep			= 206 #sausages, wool
slot_center_head_horses		 	= 207 #horses can be a trade item used in tracking but which are never offered for sale

slot_center_acres_pasture       = 208 #pasture area for grazing of cattles and sheeps, if this value is high then number of cattles and sheeps increase faster
slot_production_sources_begin = 209
slot_center_acres_grain			= 209 #grain
#slot_center_acres_olives        = 210 #olives
slot_center_acres_hunting       = 210 #hunting meat
slot_center_acres_vineyard		= 211 #fruit
slot_center_acres_flax          = 212 #flax
#slot_center_acres_dates			= 213 #dates
slot_center_soapstone_depositis	= 213 #soapstone

slot_center_fishing_fleet		= 214 #smoked fish
slot_center_salt_pans		    = 215 #salt

slot_center_apiaries       		= 216 #honey
#slot_center_silk_farms			= 217 #silk
slot_center_amber_deposits		= 217 #amber
#slot_center_kirmiz_farms		= 218 #dyes
slot_center_walrus_fleet		= 218 #ivory

slot_center_iron_deposits       = 219 #iron
slot_center_fur_traps			= 220 #furs
#timber
#pitch

slot_center_mills				= 221 #bread
slot_center_breweries			= 222 #ale
slot_center_wine_presses		= 223 #wine
#slot_center_olive_presses		= 224 #oil
slot_center_tar_ovens			= 224 #tar

slot_center_linen_looms			= 225 #linen
#slot_center_silk_looms          = 226 #velvet	
slot_center_silver_deposits     = 226 #silver
slot_center_wool_looms          = 227 #wool cloth

slot_center_pottery_kilns		= 228 #pottery
slot_center_smithies			= 229 #tools
#slot_center_tanneries			= 230 #leatherwork
slot_center_forest				= 230 #timber
slot_center_shipyards			= 231 #naval stores - uses timber, pitch, and linen

slot_center_household_gardens   = 232 #cabbages
slot_production_sources_end = 233

#all spice comes overland to Tulga
#all dyes come by sea to Jelkala

#chicken and pork are perishable and non-tradeable, and based on grain production
#timber and pitch if we ever have a shipbuilding industry
#limestone and timber for mortar, if we allow building

#Faith Religion chief y edificios
kingdom_religion_cristiana = 233  #deprecated for slot_faction_religion
slot_center_religion = 234 # 1 -christian, 2 -pagan
slot_center_faithratio = 235 # christian vs pagan
kingdom_religion_pagana = 236  #deprecated for slot_faction_religion
slot_center_player_cattle = 237
#center_religion_pagana = 237
#center_pagana_faithratio = 238
recruit_permission_need = 239 #recruit in villages, lord's permission need to Chief
# JuJu70 
# 0 - permission granted
# 1- need permission
# 2 - village elder intermediate
# 3 - cooldown period between recruitments
#chief acaba

slot_town_last_nearby_fire_time	= 240
slot_town_port = 241	#sea battles chief

slot_party_following_orders_of_troop        = 244
slot_party_orders_type				        = 245
slot_party_orders_object				    = 246
slot_party_orders_time				    	= 247

slot_party_temp_slot_1			            = 248
slot_party_under_player_suggestion			= 249 #move this up a bit
slot_party_unrested_morale_penalty            = 250    #motomataru chief morale addition
###mejor IA chief siguiendo a marshal o player
##slot_party_blind_to_other_parties  = 251
###mejor IA chief acaba

num_trade_goods = itm_siege_supply - itm_mead
slot_town_trade_good_prices_begin			= 251	#+num_trade_goods (around 40 or so)

#phaiak chief begin
slot_party_on_water            	= 296
slot_party_port_party           = 297
slot_party_shipyard_ship_type   = 298
slot_party_shipyard_ship_prop   = 299
slot_party_shipyard_ship_time   = 300

# ships owned by player:
slot_party_1_ship_type					= 301
slot_party_2_ship_type					= 302
slot_party_3_ship_type					= 303
slot_party_4_ship_type					= 304
slot_party_5_ship_type					= 305
slot_party_6_ship_type					= 306
slot_party_7_ship_type					= 307
# ships owned by other party (town for example):
slot_party_8_ship_type					= 308
slot_party_9_ship_type					= 309
slot_party_10_ship_type					= 310

slot_party_1_ship_name					= 311
slot_party_2_ship_name					= 312
slot_party_3_ship_name					= 313
slot_party_4_ship_name					= 314
slot_party_5_ship_name					= 315
slot_party_6_ship_name					= 316
slot_party_7_ship_name					= 317
slot_party_8_ship_name					= 318
slot_party_9_ship_name					= 319
slot_party_10_ship_name					= 320

slot_party_1_ship_quality				= 321		
slot_party_2_ship_quality				= 322
slot_party_3_ship_quality				= 323
slot_party_4_ship_quality				= 324
slot_party_5_ship_quality				= 325
slot_party_6_ship_quality				= 326
slot_party_7_ship_quality				= 327
slot_party_8_ship_quality				= 328
slot_party_9_ship_quality				= 329
slot_party_10_ship_quality				= 330
#slot_party_alien_ships_quality_end 		= 331

slot_party_1_ship_propertys				= 331
slot_party_2_ship_propertys				= 332
slot_party_3_ship_propertys				= 333
slot_party_4_ship_propertys				= 334
slot_party_5_ship_propertys				= 335
slot_party_6_ship_propertys				= 336
slot_party_7_ship_propertys				= 337
slot_party_8_ship_propertys				= 338
slot_party_9_ship_propertys				= 339
slot_party_10_ship_propertys			= 340

slot_party_alien_ships_propertys_end  	= 341

slot_party_ship_type_end = slot_party_1_ship_name

slot_party_player_ships_type_begin = slot_party_1_ship_type
slot_party_player_ships_type_end = slot_party_8_ship_type
slot_party_alien_ships_type_begin = slot_party_8_ship_type
slot_party_alien_ships_type_end = slot_party_1_ship_name

slot_party_player_ships_name_begin = slot_party_1_ship_name
slot_party_player_ships_name_end = slot_party_8_ship_name
slot_party_alien_ships_name_begin = slot_party_8_ship_name
slot_party_alien_ships_name_end = slot_party_1_ship_quality

slot_party_player_ships_quality_begin = slot_party_1_ship_quality
slot_party_player_ships_quality_end = slot_party_8_ship_quality
slot_party_alien_ships_quality_begin = slot_party_8_ship_quality
slot_party_alien_ships_quality_end  = slot_party_1_ship_propertys

slot_party_player_ships_propertys_begin = slot_party_1_ship_propertys
slot_party_player_ships_propertys_end = slot_party_8_ship_propertys
slot_party_alien_ships_propertys_begin = slot_party_8_ship_propertys
# slot_party_alien_ships_propertys_end  = 

# reused slots for fixing VC-1537 without breaking save games
slot_party_ai_state_backup 		= slot_party_1_ship_propertys
slot_party_ai_object_backup 	= slot_party_2_ship_propertys
slot_party_ai_behavior_backup 	= slot_party_3_ship_propertys
slot_party_ai_embarking_port 	= slot_party_4_ship_propertys

slot_town_healer 											= 342
slot_town_shipwright										= 343
slot_party_looted_left_days									= 344
slot_party_coastal_assault_scene							= 345

#phaiak end

slot_center_last_reconnoitered_by_faction_time 				= 350	#+31 or so kingdoms
#slot_center_last_reconnoitered_by_faction_cached_strength 	= 360
#slot_center_last_reconnoitered_by_faction_friend_strength 	= 370

slot_lair_improve = 390 #used for but a single value; global should be used

slot_center_fee_paid = 391
slot_center_inventory = 392
slot_center_enslaved = 393
slot_party_bribed = 394
slot_center_racket = 395
slot_party_levy_on = 396
slot_center_tax_rate = 397


###lair improve time
slot_lair_time_to_improve        = 399 #used for but a single value; global should be used
#########SIEGE WARFARE
####Siege warfare chief
slot_center_blockaded              = 400 #used for but a single value; global should be used
slot_center_blockaded_time        = 401 #used for but a single value; global should be used
slot_center_mantlets_placed     = 402 #used for but a single value; global should be used
slot_center_latrines = 403 #used for but a single value; global should be used
slot_center_ladder_time      = 404 #used for but a single value; global should be used
slot_center_infiltration_type         = 405 #used for but a single value; global should be used
slot_center_starvation_time     = 406 #used for but a single value; global should be used

slot_party_messenger_time         = 418 #used for but a single value; global should be used

#$g_player_icon_state values
pis_normal                      = 0
pis_camping                     = 1
pis_ship                        = 2


########################################################
##  SCENE SLOTS            #############################
########################################################
slot_scene_visited              = 0
slot_scene_belfry_props_begin   = 10

#MP weather & sound slots
slot_scene_sounds				= 1
sounds_plain	= 0
sounds_forest	= 1
sounds_village	= 2
sounds_coast	= 3
sounds_sea		= 4
slot_scene_time					= 2
time_noon				= 0
time_dawn				= 1
time_dusk				= 2
time_night				= 3
slot_scene_weather				= 3
weather_clear			= 0
weather_cloudy			= 1
weather_rainy			= 2
weather_foggy			= 3
#...
weather_thunderstorm	= 8
weather_seastorm		= 9

########################################################
##  TROOP SLOTS            #############################
########################################################
#slot_troop_role         = 0  # 10=Kingdom Lord

slot_troop_occupation          = 2

### Troop occupations slot_troop_occupation
##slto_merchant           = 1
slto_inactive           = 0 #for companions at the beginning of the game
slto_dead               = 1

slto_kingdom_hero       = 2

slto_player_companion   = 5 #This is specifically for companions in the employ of the player -- ie, in the party, or on a mission
slto_kingdom_lady       = 6 #Usually inactive (Calradia is a traditional place). However, can be made potentially active if active_npcs are expanded to include ladies
slto_kingdom_seneschal  = 7
slto_robber_knight      = 8
slto_inactive_pretender = 9

#NPC changes begin
slto_retirement      = 11
#slto_retirement_medium    = 12
#slto_retirement_short     = 13
#NPC changes end

slot_troop_state               = 3  
slot_troop_last_talk_time      = 4
slot_troop_met                 = 5 #i also use this for the courtship state -- may become cumbersome
slot_troop_courtship_state     = 5 #2 professed admiration, 3 agreed to seek a marriage, 4 ended relationship

slot_troop_party_template      = 6
#slot_troop_kingdom_rank        = 7

slot_troop_renown              = 7

slot_troop_prisoner_of_party   = 8  # important for heroes only
#slot_troop_is_player_companion = 9  # important for heroes only:::USE  slot_troop_occupation = slto_player_companion

slot_troop_present_at_event    = 9

slot_troop_leaded_party         = 10 # important for kingdom heroes only
slot_troop_wealth               = 11 # important for kingdom heroes only
slot_troop_cur_center           = 12 # important for royal family members only (non-kingdom heroes)

slot_troop_banner_scene_prop    = 13 # important for kingdom heroes and player only

slot_troop_original_faction     = 14
slot_troop_original_faction2    = 15 # link to Native's six strings for pretenders
slot_troop_religion	= 16 
slot_troop_conv = 17 # conversion attempted 0-initial state, 1-tried&failed 2-converted
#troop_player order state are all deprecated in favor of party_order_state. This has two reasons -- 1) to reset AI if the party is eliminated, and 2) to allow the player at a later date to give orders to leaderless parties, if we want that


#Post 0907 changes begin
slot_troop_age                 =  18
slot_troop_age_appearance      =  19

#Post 0907 changes end

slot_troop_does_not_give_quest = 20
slot_troop_player_debt         = 21
slot_troop_player_relation     = 22
slot_troop_last_faction        = 23
slot_troop_last_quest          = 24
slot_troop_last_quest_betrayed = 25
slot_troop_last_persuasion_time= 26
slot_troop_last_comment_time   = 27
slot_troop_spawned_before      = 28

#Post 0907 changes begin
slot_troop_last_comment_slot   = 29
#Post 0907 changes end

slot_troop_spouse              = 30
slot_troop_father              = 31
slot_troop_mother              = 32
slot_troop_guardian            = 33 #Usually siblings are identified by a common parent.This is used for brothers if the father is not an active npc. At some point we might introduce geneologies
slot_troop_betrothed           = 34 #Obviously superseded once slot_troop_spouse is filled
#other relations are derived from one's parents 
#slot_troop_daughter            = 33
#slot_troop_son                 = 34
#slot_troop_sibling             = 35
slot_troop_love_interest_1     = 35 #each unmarried lord has three love interests
slot_troop_love_interest_2     = 36
slot_troop_love_interest_3     = 37
slot_troop_love_interests_end  = 38
#ways to court -- discuss a book, commission/compose a poem, present a gift, recount your exploits, fulfil a specific quest, appear at a tournament
#preferences for women - (conventional - father's friends)
slot_lady_no_messages          				= 37
slot_lady_last_suitor          				= 38
slot_lord_granted_courtship_permission      = 38

slot_troop_betrothal_time                   = 39 #used in scheduling the wedding

slot_troop_trainer_met                       = 30
slot_troop_trainer_waiting_for_result        = 31
slot_troop_trainer_training_fight_won        = 32
slot_troop_trainer_num_opponents_to_beat     = 33
slot_troop_trainer_training_system_explained = 34
slot_troop_trainer_opponent_troop            = 35
slot_troop_trainer_training_difficulty       = 36
slot_troop_trainer_training_fight_won        = 37

slot_lady_used_tournament      = 40
# slot_troop_lover               = 41
# slot_troop_lover_attempt       = 42
# slot_troop_lover_found         = 43
slot_troop_num_fiefs           = 43
slot_troop_temp                = 44
slot_troop_current_rumor       = 45
slot_troop_temp_slot           = 46
slot_troop_promised_fief       = 47

slot_troop_set_decision_seed       = 48 #Does not change
slot_troop_temp_decision_seed      = 49 #Resets at recalculate_ai
slot_troop_recruitment_random      = 50 #used in a number of different places in the intrigue procedures to overcome intermediate hurdles, although not for the final calculation, might be replaced at some point by the global decision seed
#Decision seeds can be used so that some randomness can be added to NPC decisions, without allowing the player to spam the NPC with suggestions
#The temp decision seed is reset 24 to 48 hours after the NPC last spoke to the player, while the set seed only changes in special occasions
#The single seed is used with varying modula to give high/low outcomes on different issues, without using a separate slot for each issue

slot_troop_intrigue_impatience     = 51
#recruitment changes end

slot_lord_reputation_type             = 52
slot_lord_recruitment_argument        = 53 #the last argument proposed by the player to the lord
slot_lord_recruitment_candidate       = 54 #the last candidate proposed by the player to the lord

slot_troop_change_to_faction          = 55
slot_troop_player_banned              = 56

#slot_troop_readiness_to_join_army     = 57 #possibly deprecate
#slot_troop_readiness_to_follow_orders = 58 #possibly deprecate

# NPC-related constants
slot_troop_mainquest_dialog           = 58 #chief mainquest for map conversations

#NPC companion changes begin
slot_troop_first_encountered          = 59
slot_troop_home                       = 60

slot_troop_morality_state      = 61
tms_no_problem         = 0
tms_acknowledged       = 1
tms_dismissed          = 2

slot_troop_morality_type       = 62
tmt_aristocratic = 1
tmt_egalitarian = 2
tmt_humanitarian = 3
tmt_honest = 4
tmt_pious = 5

slot_troop_morality_value      = 63

slot_troop_2ary_morality_type  = 64
slot_troop_2ary_morality_state = 65
slot_troop_2ary_morality_value = 66

slot_troop_town_with_contacts  = 67
slot_troop_town_contact_type   = 68 #1 are nobles, 2 are commons

slot_troop_morality_penalties =  69 ### accumulated grievances from morality conflicts


slot_troop_personalityclash_object    = 71
#(0 - they have no problem, 1 - they have a problem)
slot_troop_personalityclash_state     = 72 #1 = pclash_penalty_to_self, 2 = pclash_penalty_to_other, 3 = pclash_penalty_to_other,
pclash_penalty_to_self  = 1
pclash_penalty_to_other = 2
pclash_penalty_to_both  = 3
#(a string)
slot_troop_personalityclash2_object   = 73
slot_troop_personalityclash2_state    = 74

slot_troop_personalitymatch_object    = 75
slot_troop_personalitymatch_state     = 76

slot_troop_personalityclash_penalties = 77 ### accumulated grievances from personality clash

slot_troop_home_speech_delivered      = 78 #only for companions
slot_troop_discussed_rebellion        = 78 #only for pretenders

#courtship slots
slot_lady_courtship_heroic_recited 	  = 74
slot_lady_courtship_allegoric_recited = 75
slot_lady_courtship_comic_recited     = 76
slot_lady_courtship_mystic_recited    = 77
slot_lady_courtship_tragic_recited    = 78
slot_troop_refused  =  79


#NPC history slots
slot_troop_met_previously             = 80
slot_troop_turned_down_twice          = 81
slot_troop_playerparty_history        = 82

pp_history_scattered         = 1
pp_history_dismissed         = 2
pp_history_quit              = 3
pp_history_indeterminate     = 4

slot_troop_playerparty_history_string = 83
slot_troop_return_renown              = 84

# slot_troop_custom_banner_bg_color_1      = 85
# slot_troop_custom_banner_bg_color_2      = 86
# slot_troop_custom_banner_charge_color_1  = 87
# slot_troop_custom_banner_charge_color_2  = 88
# slot_troop_custom_banner_charge_color_3  = 89
# slot_troop_custom_banner_charge_color_4  = 90
# slot_troop_custom_banner_bg_type         = 91
# slot_troop_custom_banner_charge_type_1   = 92
# slot_troop_custom_banner_charge_type_2   = 93
# slot_troop_custom_banner_charge_type_3   = 94
# slot_troop_custom_banner_charge_type_4   = 95
# slot_troop_custom_banner_flag_type       = 96
# slot_troop_custom_banner_num_charges     = 97
# slot_troop_custom_banner_positioning     = 98
# slot_troop_custom_banner_map_flag_type   = 99

slot_troop_multi_desc                 = 100

#conversation strings -- must be in this order!
slot_troop_intro                      = 101
slot_troop_intro_response_1           = 102
slot_troop_intro_response_2           = 103
slot_troop_backstory_a                = 104
slot_troop_backstory_b                = 105
slot_troop_backstory_c                = 106
slot_troop_backstory_delayed          = 107
slot_troop_backstory_response_1       = 108
slot_troop_backstory_response_2       = 109
slot_troop_signup                     = 110
slot_troop_signup_2                   = 111
slot_troop_signup_response_1          = 112
slot_troop_signup_response_2          = 113

slot_troop_morality_speech            = 116
slot_troop_2ary_morality_speech       = 117
slot_troop_personalityclash_speech    = 118
slot_troop_personalityclash_speech_b  = 119
slot_troop_personalityclash2_speech   = 120
slot_troop_personalityclash2_speech_b = 121
slot_troop_personalitymatch_speech    = 122
slot_troop_personalitymatch_speech_b  = 123
slot_troop_retirement_speech          = 124
slot_troop_rehire_speech              = 125
slot_troop_home_intro                 = 126
slot_troop_home_description           = 127
slot_troop_home_description_2         = 128
slot_troop_home_recap                 = 129
slot_troop_honorific                  = 130
slot_troop_kingsupport_string_1       = 131
slot_troop_kingsupport_string_2       = 132
slot_troop_kingsupport_string_2a      = 133
slot_troop_kingsupport_string_2b      = 134
slot_troop_kingsupport_string_3       = 135
slot_troop_kingsupport_objection_string	= 136
slot_troop_intel_gathering_string	    = 137
slot_troop_fief_acceptance_string	    = 138
slot_troop_woman_to_woman_string	    = 139
slot_troop_turn_against_string        = 140

slot_troop_strings_end                = 141

slot_troop_payment_request            = 141

#141, support base removed, slot now available

slot_troop_kingsupport_state          = 142
slot_troop_kingsupport_argument       = 143
slot_troop_kingsupport_opponent       = 144
slot_troop_kingsupport_objection_state = 145 #0, default, 1, needs to voice, 2, has voiced

slot_troop_days_on_mission            = 146
slot_troop_current_mission            = 147
slot_troop_mission_object             = 148
slot_troop_mission_target				= 163
slot_troop_mission_amount			= 164
npc_mission_kingsupport					= 1
npc_mission_gather_intel                = 2
npc_mission_peace_request               = 3
npc_mission_pledge_vassal               = 4
npc_mission_seek_recognition            = 5
npc_mission_test_waters                 = 6
npc_mission_non_aggression              = 7
npc_mission_rejoin_when_possible        = 8
npc_mission_improve_relations           = 9
#dplmc_npc_mission* 9-19 somebody patrullas chief
npc_mission_on_patrol                   = 20
npc_mission_on_rental                   = 21

#Number of routed agents after battle ends.
slot_troop_player_routed_agents         = 149
slot_troop_ally_routed_agents           = 150
slot_troop_enemy_routed_agents          = 151

#Special quest slots
slot_troop_mission_participation        = 152
mp_unaware                              = 0 
mp_stay_out                             = 1 
mp_prison_break_fight                   = 2 
mp_prison_break_stand_back              = 3 
mp_prison_break_escaped                 = 4 
mp_prison_break_caught                  = 5 

#Below are some constants to expand the political system a bit. The idea is to make quarrels less random, but instead make them serve a rational purpose -- as a disincentive to lords to seek 

slot_troop_controversy                     = 153 #Determines whether or not a troop is likely to receive fief or marshalship
slot_troop_recent_offense_type 	           = 154 #failure to join army, failure to support colleague
slot_troop_recent_offense_object           = 155 #to whom it happened
slot_troop_recent_offense_time             = 156
slot_troop_stance_on_faction_issue         = 157 #when it happened

tro_failed_to_join_army                    = 1
tro_failed_to_support_colleague            = 2

#CONTROVERSY
#This is used to create a more "rational choice" model of faction politics, in which lords pick fights with other lords for gain, rather than simply because of clashing personalities
#It is intended to be a limiting factor for players and lords in their ability to intrigue against each other. It represents the embroilment of a lord in internal factional disputes. In contemporary media English, a lord with high "controversy" would be described as "embattled."
#The main effect of high controversy is that it disqualifies a lord from receiving a fief or an appointment
#It is a key political concept because it provides incentive for much of the political activity. For example, Lord Red Senior is worried that his rival, Lord Blue Senior, is going to get a fied which Lord Red wants. So, Lord Red turns to his protege, Lord Orange Junior, to attack Lord Blue in public. The fief goes to Lord Red instead of Lord Blue, and Lord Red helps Lord Orange at a later date.


slot_troop_will_join_prison_break = 158 #deprecated

#Flirting chief companeros
slot_troop_flirted_with           = 159	#Flirting chief companeros

slot_troop_default_type           = 160 #chief para diferentes alturas en campo de batalla.

#rumores
slot_troop_companion_camp_conversation = 161
slot_troop_companion_camp_conversed    = 162
rumor_found_chance = 70
slot_troop_sell_prisoner   = 165
slot_troop_tortured = 166
slot_troop_message_sent = 167
slot_troop_robbed = 168
slot_troop_marriage_time = 169
####chief
##slot_troop_cur_xp_for_wp      = 175
##slot_troop_xp_limit_for_wp    = 176
##
##slot_troop_kill_count         = 177
##slot_troop_wound_count        = 178
### slot_troop_horse = 179	spear bracing kit (see above)
##slot_troop_extra_xp_limit     = 180
##slot_prisoner_agreed = 181	#Hablar prisioneros chief

slot_troop_relations_begin                = 170 #this creates an array for relations between troops
											#Right now, lords start at 324 and run to around 487, including pretenders
defection_trigger = -10 #disgruntled level from script_calculate_troop_political_factors_for_liege

#defection states
recruit_adv = 1
no_income = 2
court_intrigue = 3
											
########################################################
##  PLAYER SLOTS           #############################
########################################################

slot_player_spawned_this_round                 = 0
slot_player_last_rounds_used_item_earnings     = 1
slot_player_selected_item_indices_begin        = 2
slot_player_selected_item_indices_end          = 11
slot_player_cur_selected_item_indices_begin    = slot_player_selected_item_indices_end
slot_player_cur_selected_item_indices_end      = slot_player_selected_item_indices_end + 9
slot_player_join_time                          = 21
slot_player_button_index                       = 22 #used for presentations
slot_player_can_answer_poll                    = 23
slot_player_first_spawn                        = 24
slot_player_spawned_at_siege_round             = 25
slot_player_poll_disabled_until_time           = 26
slot_player_total_equipment_value              = 27
slot_player_last_team_select_time              = 28
slot_player_death_pos_x                        = 29
slot_player_death_pos_y                        = 30
slot_player_death_pos_z                        = 31
slot_player_damage_given_to_target_1           = 32 #used only in destroy mod
slot_player_damage_given_to_target_2           = 33 #used only in destroy mod
slot_player_last_bot_count                     = 34
slot_player_bot_type_1_wanted                  = 35
slot_player_bot_type_2_wanted                  = 36
slot_player_bot_type_3_wanted                  = 37
slot_player_bot_type_4_wanted                  = 38
slot_player_bot_type_5_wanted                  = 39
slot_player_bot_type_6_wanted                  = 40
slot_player_bot_type_7_wanted                  = 41
slot_player_bot_type_8_wanted                  = 42
slot_player_bot_type_9_wanted                  = 43
slot_player_bot_type_10_wanted                 = 44
slot_player_bot_type_11_wanted                 = 45
slot_player_bot_type_12_wanted                 = 46
slot_player_bot_type_13_wanted                 = 47
slot_player_bot_type_14_wanted                 = 48
slot_player_bot_type_15_wanted                 = 49 #reserve few more slots after this for special troops

slot_player_spawn_count                        = 55
slot_player_dinerotropas                       = 56

slot_player_ship                              = 57
slot_player_last_ship                         = 58

slot_player_is_immortal						  = 59
slot_player_forced_team_change				  = 60
########################################################
##  TEAM SLOTS             #############################
########################################################

slot_team_flag_situation                = 0

#Team Data
slot_team_faction                       = 1
slot_team_starting_x                    = 2
slot_team_starting_y                    = 3
slot_team_reinforcement_stage           = 4

#Reset with every call of Store_Battlegroup_Data
slot_team_size                          = 5
slot_team_adj_size                      = 6 #cavalry double counted for AI considerations
slot_team_num_infantry                  = 7	#class counts
slot_team_num_archers                   = 8
slot_team_num_cavalry                   = 9
slot_team_level                         = 10
slot_team_avg_zrot                      = 11
slot_team_avg_x                         = 12
slot_team_avg_y                         = 13

#Battlegroup slots (1 for each of 9 divisions). A "battlegroup" is uniquely defined by team and division
slot_team_d0_size                       = 14
slot_team_d0_percent_ranged             = 23
slot_team_d0_percent_throwers           = 32
slot_team_d0_low_ammo                   = 41
slot_team_d0_level                      = 50
slot_team_d0_armor                      = 59
slot_team_d0_weapon_length              = 68
slot_team_d0_swung_weapon_length        = 77
slot_team_d0_front_weapon_length        = 86
slot_team_d0_front_agents               = 95	#for calculating slot_team_d0_front_weapon_length
slot_team_d0_is_fighting                = 104
slot_team_d0_enemy_supporting_melee     = 113
slot_team_d0_closest_enemy              = 122
slot_team_d0_closest_enemy_dist         = 131	#for calculating slot_team_d0_closest_enemy
slot_team_d0_closest_enemy_special      = 140	#tracks non-cavalry for AI infantry division, infantry for AI archer division
slot_team_d0_closest_enemy_special_dist = 149	#for calculating slot_team_d0_closest_enemy_special
slot_team_d0_avg_x                      = 158
slot_team_d0_avg_y                      = 167
slot_team_d0_avg_zrot                   = 176
#End Reset Group

slot_team_d0_type                       = 185
sdt_infantry   = 0
sdt_archer     = 1
sdt_cavalry    = 2
sdt_polearm    = 3
sdt_skirmisher = 4
sdt_harcher    = 5
sdt_support    = 6
sdt_bodyguard  = 7
sdt_unknown    = -1

slot_team_d0_formation                  = 194
formation_none      = 0
formation_default   = 1
formation_ranks     = 2
formation_shield    = 3
formation_wedge     = 4
formation_square    = 5

#Native formation modes
#Constants actually correspond to number of "Stand Closer" commands required by WB to create formation
#Extended to 5 line for WFaS
formation_1_row    = 0
formation_2_row    = -1
formation_3_row    = -2
formation_4_row    = -3
formation_5_row    = -4

slot_team_d0_formation_space            = 203	#number of extra 50cm spaces currently in use
slot_team_d0_move_order                 = 212	#now used only for player divisions
slot_team_d0_fclock                     = 221	#now used only for player divisions
slot_team_d0_first_member               = 230	#-1 if division not in formation
slot_team_d0_prev_first_member          = 239
slot_team_d0_speed_limit                = 248
slot_team_d0_percent_in_place           = 257
slot_team_d0_destination_x              = 266
slot_team_d0_destination_y              = 275
slot_team_d0_destination_zrot           = 284
slot_team_d0_target_team                = 293	#targeted battlegroup (team ID)
slot_team_d0_target_division            = 302	#targeted battlegroup (division ID)
slot_team_d0_formation_num_ranks        = 311
slot_team_d0_exists                     = 320
#NEXT                                   = 329
#Battlegroup slots end

reset_team_stats_begin = slot_team_size  
reset_team_stats_end   = slot_team_d0_type

minimum_ranged_ammo = 3	#below this not considered ranged type troop


########################################################
##  QUEST SLOTS            #############################
########################################################

slot_quest_target_center            = 1
slot_quest_target_troop             = 2
slot_quest_target_faction           = 3
slot_quest_object_troop             = 4
#slot_quest_target_troop_is_prisoner = 5
slot_quest_giver_troop              = 6
slot_quest_object_center            = 7
slot_quest_target_party             = 8
slot_quest_target_party_template    = 9
slot_quest_target_amount            = 10
slot_quest_current_state            = 11
slot_quest_giver_center             = 12
slot_quest_target_dna               = 13
slot_quest_target_item              = 14
slot_quest_object_faction           = 15

slot_quest_target_state             = 16
slot_quest_object_state             = 17

slot_quest_convince_value           = 19
slot_quest_importance               = 20
slot_quest_xp_reward                = 21
slot_quest_gold_reward              = 22
slot_quest_expiration_days          = 23
slot_quest_dont_give_again_period   = 24
slot_quest_dont_give_again_remaining_days = 25

slot_quest_failure_consequence      = 26
slot_quest_temp_slot                = 27

# Phaiak begin
slot_quest_menu_1					= 31
slot_quest_menu_2					= 32
slot_quest_menu_3					= 33
slot_quest_menu_4					= 34
slot_quest_menu_5					= 35
slot_quest_menu_6					= 36
slot_quest_menu_7					= 37
slot_quest_menu_8					= 38
slot_quest_menu_9					= 39
slot_quest_menu_10					= 40
slot_quest_menu_11					= 41
slot_quest_menu_12					= 42
slot_quest_menu_13					= 43
slot_quest_menu_14					= 44
slot_quest_menu_15					= 45
slot_quest_menu_16					= 46
slot_quest_menu_17					= 47
slot_quest_menu_18					= 48
slot_quest_menu_19					= 49
slot_quest_menu_20					= 50
slot_quest_menu_21					= 51
slot_quest_menu_22					= 52
slot_quest_menu_23					= 53
slot_quest_menu_24					= 54
slot_quest_menu_25					= 55
slot_quest_menu_26					= 56
slot_quest_menu_27					= 57
# Phaiak end

# Start - Set Goal Presentation
# Uses quest: qst_vc_menu to store data
slot_set_goal_type = 100
slot_set_goal_wealth = 101
slot_set_goal_rtr = 102
slot_set_goal_marry = 103
slot_set_goal_army = 104
slot_set_goal_reputation = 105
slot_set_goal_renown = 106
slot_set_goal_reserved1 = 107
slot_set_goal_reserved2 = 108
slot_set_goal_reserved3 = 109
slot_set_goal_reserved4 = 110
slot_set_goal_completed_custom = 111 
slot_set_goal_completed_raider = 112
slot_set_goal_completed_warrior = 113
slot_set_goal_completed_lord = 114
slot_set_goal_completed_king = 115 
slot_set_goal_completed_expand = 116 

# types:
goal_canceled = -2
goal_empty = -1
goal_custom = 1
goal_raider = 2
goal_warrior = 3
goal_lord = 4
goal_king = 5
goal_expand = 6

# complete types
goal_complete = 1
goal_not_complete = 0


# END: Set Goal presentation 

slot_quest_menu_begin = slot_quest_menu_1
slot_quest_menu_end = slot_quest_menu_24 + 1

# wound system
slot_quest_int_penalty_left_days = slot_quest_menu_1
slot_quest_cha_penalty_left_days = slot_quest_menu_2
slot_quest_str_penalty_left_days = slot_quest_menu_3
slot_quest_agi_penalty_left_days = slot_quest_menu_4
slot_quest_end_penalty_left_days = slot_quest_menu_5

slot_quest_int_penalty_fluid_points = slot_quest_menu_11
slot_quest_cha_penalty_fluid_points = slot_quest_menu_12
slot_quest_str_penalty_fluid_points = slot_quest_menu_13
slot_quest_agi_penalty_fluid_points = slot_quest_menu_14
slot_quest_end_penalty_fluid_points = slot_quest_menu_15

slot_quest_int_penalty_perma_points = slot_quest_menu_21
slot_quest_cha_penalty_perma_points = slot_quest_menu_22
slot_quest_str_penalty_perma_points = slot_quest_menu_23
slot_quest_agi_penalty_perma_points = slot_quest_menu_24
slot_quest_end_penalty_perma_points = slot_quest_menu_25

# spawn system
slot_quest_team_0_spawn_troop1_type = slot_quest_menu_1
slot_quest_team_0_spawn_troop2_type = slot_quest_menu_2
slot_quest_team_0_spawn_troop3_type = slot_quest_menu_3
slot_quest_team_0_spawn_troop4_type = slot_quest_menu_4
slot_quest_team_0_spawn_troop5_type = slot_quest_menu_5
slot_quest_team_0_spawn_troop1_count = slot_quest_menu_6
slot_quest_team_0_spawn_troop2_count = slot_quest_menu_7
slot_quest_team_0_spawn_troop3_count = slot_quest_menu_8
slot_quest_team_0_spawn_troop4_count = slot_quest_menu_9
slot_quest_team_0_spawn_troop5_count = slot_quest_menu_10

slot_quest_team_1_spawn_troop1_type = slot_quest_menu_11
slot_quest_team_1_spawn_troop2_type = slot_quest_menu_12
slot_quest_team_1_spawn_troop3_type = slot_quest_menu_13
slot_quest_team_1_spawn_troop4_type = slot_quest_menu_14
slot_quest_team_1_spawn_troop5_type = slot_quest_menu_15
slot_quest_team_1_spawn_troop1_count = slot_quest_menu_16
slot_quest_team_1_spawn_troop2_count = slot_quest_menu_17
slot_quest_team_1_spawn_troop3_count = slot_quest_menu_18
slot_quest_team_1_spawn_troop4_count = slot_quest_menu_19
slot_quest_team_1_spawn_troop5_count = slot_quest_menu_20

slot_quest_team_0_ship_count = slot_quest_menu_21
slot_quest_team_1_ship_count = slot_quest_menu_22


slot_quest_1_ship_type	= slot_quest_menu_1
slot_quest_2_ship_type	= slot_quest_menu_2
slot_quest_3_ship_type	= slot_quest_menu_3
slot_quest_4_ship_type	= slot_quest_menu_4
slot_quest_5_ship_type	= slot_quest_menu_5
slot_quest_6_ship_type	= slot_quest_menu_6
slot_quest_7_ship_type	= slot_quest_menu_7

slot_quest_1_ship_cond	= slot_quest_menu_11
slot_quest_2_ship_cond	= slot_quest_menu_12
slot_quest_3_ship_cond	= slot_quest_menu_13
slot_quest_4_ship_cond	= slot_quest_menu_14
slot_quest_5_ship_cond	= slot_quest_menu_15
slot_quest_6_ship_cond	= slot_quest_menu_16
slot_quest_7_ship_cond	= slot_quest_menu_17

slot_quest_1_ship_prop	= slot_quest_menu_21
slot_quest_2_ship_prop	= slot_quest_menu_22
slot_quest_3_ship_prop	= slot_quest_menu_23
slot_quest_4_ship_prop	= slot_quest_menu_24
slot_quest_5_ship_prop	= slot_quest_menu_25
slot_quest_6_ship_prop	= slot_quest_menu_26
slot_quest_7_ship_prop	= slot_quest_menu_27


########################################################
##  PARTY TEMPLATE SLOTS   #############################
########################################################

slot_party_template_num_killed      = 1
# slot_party_template_count           = 2
slot_party_template_lair_type       = 3
# slot_party_template_lair_party      = 4
# slot_party_template_lair_spawnpoint = 5


########################################################
##  SCENE PROP SLOTS       #############################
########################################################

scene_prop_open_or_close_slot       = 1
scene_prop_smoke_effect_done        = 2
scene_prop_number_of_agents_pushing = 3 #for belfries only
scene_prop_next_entry_point_id      = 4 #for belfries only
scene_prop_belfry_platform_moved    = 5 #for belfries only
#####sea battles chief phaiak empieza
scene_prop_sail						= 6 
scene_prop_rowing				    = 7  
scene_prop_rudder				    = 8  
scene_prop_last_speed				= 9  
scene_prop_last_turn			    = 10 
scene_prop_wank_state			    = 11 
scene_prop_boarding_wanted		    = 12 # "-1"=no, "0"=yes, "1"=yes, also with friendly ships
scene_prop_landing_wanted		    = 13 # "0"=no, "1"=yes
scene_prop_boarding_left		    = 14 
scene_prop_boarding_right		    = 15 
scene_prop_boarding_progress	    = 16 
scene_prop_main_instance		    = 17
scene_prop_ramp_right			    = 18
scene_prop_ramp_2				    = 19
scene_prop_boom_instance		    = 20
scene_prop_max_speed		   		= 21
scene_prop_max_x_rotation	   		= 22
scene_prop_max_y_rotation 		    = 23
scene_prop_distance_to_front	    = 24
scene_prop_quality				    = 25
scene_prop_collision_instance		= 26
scene_prop_radius					= 27
scene_prop_going_to_boarding_with	= 28
scene_prop_timer					= 29
scene_prop_ship_type				= 30
scene_prop_ship_number				= 31
scene_prop_sound					= 32
scene_prop_slots_end                = 33
scene_prop_lead_player              = 34
scene_prop_ramp_left			    = 35
scene_prop_cage_main			    = 36
scene_prop_cage_left			    = 37
scene_prop_cage_right			    = 38
scene_prop_oar_state			    = 39
scene_prop_crew_number			    = 40
scene_prop_cargo_1				    = 41
scene_prop_collision_2_instance		= 42
scene_prop_cage_left_2			    = 43
scene_prop_cage_left_3			    = 44
scene_prop_cage_right_2			    = 45
scene_prop_cage_right_3			    = 46
scene_prop_timer_2					= 47
scene_prop_timer_3					= 48

scene_prop_ramp_1			  		= scene_prop_ramp_right
scene_prop_y_cosinus			    = scene_prop_wank_state
###phaiak acaba chief
########################################################
rel_enemy   = 0
rel_neutral = 1
rel_ally    = 2


# character backgrounds #####chief change and anade para creacion de personaje character
cb_noble             = 1
cb_merchant          = 2
cb_guard             = 3
cb_forester          = 4
cb_nomad             = 5
cb_thief             = 6
cb_priest            = 7

cb2_page             = 0
cb2_apprentice       = 1
cb2_urchin           = 2
cb2_steppe_child     = 3
cb2_merchants_helper = 4

cb3_christian        = 0
cb3_pagan            = 1

cb3_landowner        = 5
cb3_roamer           = 7
cb3_traveler         = 8
cb3_student          = 9
cb3_slave            = 10

cb3_bajo             = 11
cb3_alto             = 12
cb3_normal           = 13

cb4_elder            = 1
cb4_adult            = 2
cb4_young            = 3

##cb4_disown  = 5
##cb4_greed  = 6

cb5_calm             = 1
##cb5_selfconfident   = 2
##cb5_goodnatured     = 3
cb5_responsible      = 2
cb5_extroverted      = 3
cb5_bold             = 4

cb6_justice          = 1
cb6_temperance       = 2
cb6_fortitude        = 3
cb6_prudence         = 4

cb7_foreigner        = 1
cb7_scotopict        = 2
cb7_briton           = 3
cb7_irish            = 4
cb7_frisian          = 5
cb7_norseman         = 6
cb7_anglesaxon       = 7

camp_storyline = 8
camp_sandbox   = 9
camp_kingc     = 10
camp_d1        = 11
camp_d2        = 12
camp_d3        = 13
camp_d4        = 14
camp_d5        = 15
camp_lordc     = 16

#chief player lair staff
hire_captainok = 1
hire_captainno = 2
hire_priest1 = 3
hire_priest2 = 4
hire_priest3 = 5
hire_bard1 = 6
hire_bard2 = 7
hire_bard3 = 8
hire_tavernkeeper1 = 9
hire_tavernkeeper2 = 10
hire_whore1 = 11
hire_whore2 = 12
hire_whore3 = 13
hire_whore4 = 14
hire_whore5 = 15
hire_trainer1 = 16
hire_trainer2 = 17
hire_smith1 = 18
hire_smith2 = 19
hire_armorer1 = 20
hire_armorer2 = 21
hire_barber1 = 22
hire_barber2 = 23
hire_barber3 = 24
hire_barber4 = 25
hire_barber5 = 26
hire_cook1 = 27
hire_cook2 = 28

#Encounter types
enctype_fighting_against_village_raid = 1
enctype_catched_during_village_raid   = 2

#Talk contexts
tc_town_talk                  = 0
tc_court_talk   	      	  = 1
tc_party_encounter            = 2
tc_castle_gate                = 3
tc_siege_commander            = 4
tc_join_battle_ally           = 5
tc_join_battle_enemy          = 6
tc_castle_commander           = 7
tc_hero_freed                 = 8
tc_hero_defeated              = 9
tc_entering_center_quest_talk = 10
tc_back_alley                 = 11
tc_siege_won_seneschal        = 12
tc_ally_thanks                = 13
tc_tavern_talk                = 14
tc_rebel_thanks               = 15
tc_garden            		  = 16
tc_courtship            	  = 16
tc_after_duel            	  = 17
tc_prison_break               = 18
tc_escape               	  = 19
tc_give_center_to_fief        = 20
tc_merchants_house            = 21
#tc_camp                       = 22 #chief added for camp talk with npc's and troops


#Troop Commentaries begin
#Log entry types
#civilian
logent_village_raided            = 1
logent_village_extorted          = 2
logent_caravan_accosted          = 3 #in caravan accosted, center and troop object are -1, and the defender's faction is the object
logent_traveller_attacked        = 3 #in traveller attacked, origin and destination are center and troop object, and the attacker's faction is the object

logent_helped_peasants           = 4 

logent_party_traded              = 5

logent_castle_captured_by_player              = 10
logent_lord_defeated_by_player                = 11
logent_lord_captured_by_player                = 12
logent_lord_defeated_but_let_go_by_player     = 13
logent_player_defeated_by_lord                = 14
logent_player_retreated_from_lord             = 15
logent_player_retreated_from_lord_cowardly    = 16
logent_lord_helped_by_player                  = 17
logent_player_participated_in_siege           = 18
logent_player_participated_in_major_battle    = 19
logent_castle_given_to_lord_by_player         = 20

logent_pledged_allegiance          = 21
logent_liege_grants_fief_to_vassal = 22


logent_renounced_allegiance      = 23 

logent_player_claims_throne_1    		               = 24
logent_player_claims_throne_2    		               = 25


logent_troop_feels_cheated_by_troop_over_land		   = 26
logent_ruler_intervenes_in_quarrel                     = 27
logent_lords_quarrel_over_land                         = 28
logent_lords_quarrel_over_insult                       = 29
logent_marshal_vs_lord_quarrel                  	   = 30
logent_lords_quarrel_over_woman                        = 31

logent_lord_protests_marshal_appointment			   = 32
logent_lord_blames_defeat						   	   = 33

logent_player_suggestion_succeeded					   = 35
logent_player_suggestion_failed					       = 36

logent_liege_promises_fief_to_vassal				   = 37

logent_lord_insults_lord_for_cowardice                 = 38
logent_lord_insults_lord_for_rashness                  = 39
logent_lord_insults_lord_for_abandonment               = 40
logent_lord_insults_lord_for_indecision                = 41
logent_lord_insults_lord_for_cruelty                   = 42
logent_lord_insults_lord_for_dishonor                  = 43




logent_game_start                           = 45 
logent_poem_composed                        = 46 ##Not added
logent_tournament_distinguished             = 47 ##Not added
logent_tournament_won                       = 48 ##Not added

#logent courtship - lady is always actor, suitor is always troop object
logent_lady_favors_suitor                   = 51 #basically for gossip
logent_lady_betrothed_to_suitor_by_choice   = 52
logent_lady_betrothed_to_suitor_by_family   = 53
logent_lady_rejects_suitor                  = 54
logent_lady_father_rejects_suitor           = 55
logent_lady_marries_lord                    = 56
logent_lady_elopes_with_lord                = 57
logent_lady_rejected_by_suitor              = 58
logent_lady_betrothed_to_suitor_by_pressure = 59 #mostly for gossip
#logent_lady_breaks_betrothal_with_lord      = 58
#logent_lady_betrothal_broken_by_lord        = 59

logent_lady_and_suitor_break_engagement		  = 60
logent_lady_marries_suitor				          = 61

logent_lord_holds_lady_hostages             = 62
logent_challenger_defeats_lord_in_duel      = 63
logent_challenger_loses_to_lord_in_duel     = 64

logent_player_stole_cattles_from_village    = 66

logent_party_spots_wanted_bandits           = 70


logent_border_incident_cattle_stolen          = 72 #possibly add this to rumors for non-player faction
logent_border_incident_bride_abducted         = 73 #possibly add this to rumors for non-player faction
logent_border_incident_villagers_killed       = 74 #possibly add this to rumors for non-player faction
logent_border_incident_subjects_mistreated    = 75 #possibly add this to rumors for non-player faction

#These supplement caravans accosted and villages burnt, in that they create a provocation. So far, they only refer to the player
logent_border_incident_troop_attacks_neutral  = 76
logent_border_incident_troop_breaks_truce     = 77
logent_border_incident_troop_suborns_lord     = 78


logent_policy_ruler_attacks_without_provocation 			= 80
logent_policy_ruler_ignores_provocation         			= 81 #possibly add this to rumors for non-player factions
logent_policy_ruler_makes_peace_too_soon        			= 82
logent_policy_ruler_declares_war_with_justification         = 83
logent_policy_ruler_breaks_truce                            = 84
logent_policy_ruler_issues_indictment_just                  = 85 #possibly add this to rumors for non-player faction
logent_policy_ruler_issues_indictment_questionable          = 86 #possibly add this to rumors for non-player faction


logent_player_faction_declares_war                    = 90 #this doubles for declare war to extend power
logent_faction_declares_war_out_of_personal_enmity    = 91
logent_faction_declares_war_to_regain_territory       = 92
logent_faction_declares_war_to_curb_power             = 93
logent_faction_declares_war_to_respond_to_provocation = 94
logent_faction_declares_war_to_fulfil_alliance        = 95 #alliance
logent_war_declaration_types_end                      = 96


#lord reputation type, for commentaries
#"Martial" will be twice as common as the other types
lrep_none           = 0 
lrep_martial        = 1 #chivalrous but not terribly empathetic or introspective, - eg Richard Lionheart, your average 14th century French baron
lrep_quarrelsome    = 2 #spiteful, cynical, a bit paranoid, possibly hotheaded - eg Robert Graves' Tiberius, some of Charles VI's uncles
lrep_selfrighteous  = 3 #coldblooded, moralizing, often cruel - eg William the Conqueror, Timur, Octavian, Aurangzeb (although he is arguably upstanding instead, particularly after his accession)
lrep_cunning        = 4 #coldblooded, pragmatic, amoral - eg Louis XI, Guiscard, Akbar Khan, Abd al-Aziz Ibn Saud
lrep_debauched      = 5 #spiteful, amoral, sadistic - eg Caligula, Tuchman's Charles of Navarre
lrep_goodnatured    = 6 #chivalrous, benevolent, perhaps a little too decent to be a good warlord - eg Hussein ibn Ali. Few well-known historical examples maybe. because many lack the drive to rise to faction leadership. Ranjit Singh has aspects
lrep_upstanding     = 7 #moralizing, benevolent, pragmatic, - eg Bernard Cornwell's Alfred, Charlemagne, Salah al-Din, Sher Shah Suri

lrep_roguish        = 8 #used for commons, specifically ex-companions. Tries to live life as a lord to the full
lrep_benefactor     = 9 #used for commons, specifically ex-companions. Tries to improve lot of folks on land
lrep_custodian      = 10 #used for commons, specifically ex-companions. Tries to maximize fief's earning potential

#lreps specific to dependent noblewomen
lrep_conventional    = 21 #Charlotte York in SATC seasons 1-2, probably most medieval aristocrats
lrep_adventurous     = 22 #Tomboyish. However, this basically means that she likes to travel and hunt, and perhaps yearn for wider adventures. However, medieval noblewomen who fight are rare, and those that attempt to live independently of a man are rarer still, and best represented by pre-scripted individuals like companions
lrep_otherworldly    = 23 #Prone to mysticism, romantic. 
lrep_ambitious       = 24 #Lady Macbeth
lrep_moralist        = 25 #Equivalent of upstanding or benefactor -- takes nobless oblige, and her traditional role as repository of morality, very seriously. Based loosely on Christine de Pisa 

#a more complicated system of reputation could include the following...

#successful vs unlucky -- basic gauge of success
#daring vs cautious -- maybe not necessary
#honorable/pious/ideological vs unscrupulous -- character's adherance to an external code of conduct. Fails to capture complexity of people like Aurangzeb, maybe, but good for NPCs
	#(visionary/altruist and orthodox/unorthodox could be a subset of the above, or the specific external code could be another tag)
#generous/loyal vs manipulative/exploitative -- character's sense of duty to specific individuals, based on their relationship. Affects loyalty of troops, etc
#merciful vs cruel/ruthless/sociopathic -- character's general sense of compassion. Sher Shah is example of unscrupulous and merciful (the latter to a degree).
#dignified vs unconventional -- character's adherance to social conventions. Very important, given the times


courtship_poem_tragic      = 1 #Emphasizes longing, Laila and Majnoon
courtship_poem_heroic      = 2 #Norse sagas with female heroines
courtship_poem_comic       = 3 #Emphasis on witty repartee -- Contrasto (Sicilian school satire) 
courtship_poem_mystic      = 4 #Sufi poetry. Song of Songs
courtship_poem_allegoric   = 5 #Idealizes woman as a civilizing force -- the Romance of the Rose, Siege of the Castle of Love

#courtship gifts currently deprecated







#Troop Commentaries end

tutorial_fighters_begin = "trp_tutorial_fighter_1"
tutorial_fighters_end   = "trp_tutorial_archer_1"

#Walker types: 
walkert_default            = 0
walkert_needs_money        = 1
walkert_needs_money_helped = 2
walkert_spy                = 3
num_town_walkers = 8
town_walker_entries_start = 32

reinforcement_cost_easy = 600
reinforcement_cost_moderate = 450
reinforcement_cost_hard = 300

merchant_toll_duration        = 72 #Tolls are valid for 72 hours

hero_escape_after_defeat_chance = 65 #Chief back high number, more easy to escape


raid_distance = 4

surnames_begin = "str_surname_1"
surnames_end = "str_surnames_end"
names_begin = "str_name_1"
names_end = surnames_begin
countersigns_begin = "str_countersign_1"
countersigns_end = names_begin
secret_signs_begin = "str_secret_sign_1"
secret_signs_end = countersigns_begin

##kingdom_titles_male_begin = "str_faction_title_male_player"
##kingdom_titles_female_begin = "str_faction_title_female_player"

kingdoms_begin = "fac_player_supporters_faction"
kingdoms_end = "fac_kingdoms_end"

npc_kingdoms_begin = "fac_kingdom_1"
npc_kingdoms_end = kingdoms_end

cultures_begin = "fac_culture_norse"
cultures_end = "fac_cultures_end"

cb_factions_begin = cultures_begin
cb_factions_end = "fac_cultures_end" #"fac_culture_welsh"

mp_factions_begin = cultures_begin
mp_factions_end = cultures_end #"fac_culture_angle"

bandits_begin = "trp_bandit"
bandits_end = "trp_manhunter" #chief cambia

kingdom_ladies_begin = "trp_knight_1_1_wife"
kingdom_ladies_end = "trp_heroes_end"

#active NPCs in order: companions, kings, lords, pretenders

pretenders_begin = "trp_kingdom_1_pretender"
pretenders_end = kingdom_ladies_begin

lords_begin = "trp_knight_1_1"
lords_end = pretenders_begin

kings_begin = "trp_kingdom_1_lord"
kings_end = lords_begin

companions_begin = "trp_npc1"
companions_end = kings_begin

active_npcs_begin = "trp_npc1"
active_npcs_end = kingdom_ladies_begin
#"active_npcs_begin replaces kingdom_heroes_begin to allow for companions to become lords. Includes anyone who may at some point lead their own party: the original kingdom heroes, companions who may become kingdom heroes, and pretenders. (slto_kingdom_hero as an occupation means that you lead a party on the map. Pretenders have the occupation "slto_inactive_pretender", even if they are part of a player's party, until they have their own independent party)
#If you're a modder and you don't want to go through and switch every kingdom_heroes to active_npcs, simply define a constant: kingdom_heroes_begin = active_npcs_begin., and kingdom_heroes_end = active_npcs_end. I haven't tested for that, but I think it should work.

kingdom_heroes_begin = active_npcs_begin #puesto chief
kingdom_heroes_end = active_npcs_end #puesto chief

active_npcs_including_player_begin = "trp_kingdom_heroes_including_player_begin"
original_kingdom_heroes_begin = "trp_kingdom_1_lord"

heroes_begin = active_npcs_begin
heroes_end = kingdom_ladies_end

soldiers_begin = "trp_farmer"
soldiers_end = "trp_town_walker_1"

kingdom_heroes_begin2 = "trp_kingdom_1_lord" #anadido chief para viejo kingdom heroes
kingdom_heroes_end2 = kingdom_ladies_begin #anadido chief para viejo kingdom heroes

#### smiths and armorer special chief
herrero_troops_begin = "trp_town_5_weaponsmith"
herrero_troops_end = "trp_town_10_weaponsmith"
armorer_troops_begin = "trp_town_14_armorer"
armorer_troops_end = "trp_town_19_armorer"


#cambios chief bardo y cortesanos
bardo_begin = "trp_bardo_1"
bardo_end   = "trp_sacerdote_1"

sacerdote_begin = "trp_sacerdote_1"
sacerdote_end   = "trp_paganop_1"

pagano_begin = "trp_paganop_1"
pagano_end   = "trp_priest_end"
##
quastuosa_begin = "trp_quastuosa_1"
quastuosa_end   = "trp_quastuosa_end"
##
##especiales_begin = "trp_especiales_1"
##especiales_end   = "trp_kingdom_heroes_including_player_begin"
##
tavern_minstrels_begin = "trp_tavern_minstrel_1"
##tavern_minstrels_end   = bardo_begin #activar cuando bardos ok
tavern_minstrels_end   = "trp_quastuosa_1"
###cambios chief acaba cortesanos

tavern_booksellers_begin = "trp_tavern_bookseller_1"
tavern_booksellers_end   = tavern_minstrels_begin

tavern_travelers_begin = "trp_tavern_traveler_1"
tavern_travelers_end   = tavern_booksellers_begin

ransom_brokers_begin = "trp_ransom_broker_1"
ransom_brokers_end   = tavern_travelers_begin

mercenary_troops_begin = "trp_watchman"
mercenary_troops_end = "trp_mercenaries_end"

#chief tropas por religion
christian_troops_begin = "trp_cantaber_iuventus"
christian_troops_end = "trp_townsman"
christian_troops2_begin = "trp_briton_slave"
christian_troops2_end = "trp_todos_cuerno"
christian_troops3_begin = "trp_frisian_basic"
christian_troops3_end = "trp_looter"
christian_troops4_begin = "trp_looter_leader2"
christian_troops4_end = "trp_slave_driver"

pagan_troops_begin = "trp_mercenary_leader"
pagan_troops_end = "trp_briton_slave"
pagan_troops2_begin = "trp_norse_messenger"
pagan_troops2_end = "trp_frisian_basic"
pagan_troops3_begin = "trp_steppe_bandit"
pagan_troops3_end = "trp_looter_leader2"
#chief tropas por religion acaba

multiplayer_troops_begin = "trp_norse_multiplayer" #chief cambia multiplayer chief
multiplayer_troops_end = "trp_multiplayer_end"

multiplayer_addon_troops_begin = "trp_mp_norse_peasant"
multiplayer_addon_troops_end = "trp_mp_addon_player_troops_end"
#chief capitan
multiplayer_lordscapitan_begin = "trp_norse_capitan" #chief cambia multiplayer chief
multiplayer_lordscapitan_end = multiplayer_troops_end
#
multiplayer_class_troops_begin	= "trp_mp_norse_infantry"
multiplayer_class_troops_end	= multiplayer_addon_troops_end
#
multiplayer_peasant_troops_begin	= "trp_mp_norse_peasant"
multiplayer_peasant_troops_end		= multiplayer_class_troops_begin

multiplayer_ai_troops_begin = "trp_norse_slave" #chief cambia multiplayer chief
multiplayer_ai_troops_end = "trp_norse_messenger"

multiplayer_scenes_begin = "scn_multi_scene_1"
multiplayer_scenes_end = "scn_multiplayer_maps_end"

multiplayer_scene_names_begin = "str_multi_scene_1"
multiplayer_scene_names_end = "str_multi_scene_end"

#addon
multiplayer_addon_scenes_begin = "scn_multi_scene_coast"
multiplayer_addon_scenes_end = "scn_mp_addon_maps_end"
multiplayer_addon_scene_names_begin = "str_multi_scene_coast"
multiplayer_addon_scene_names_end = "str_mp_addon_scene_end"

multiplayer_objective_projections_begin = "mesh_mp_objective_projection_team_1"
multiplayer_objective_projections_end = "mesh_mp_objective_projections_end"

multiplayer_objective_taken_projections_begin = "mesh_mp_objective_projection_team_1_miss"
multiplayer_objective_taken_projections_end = "mesh_mp_objective_projection_misses_end"

multiplayer_game_type_names_begin = "str_multi_game_type_1"
multiplayer_game_type_names_end = "str_multi_game_types_end"

multiplayer_game_type_descs_begin = "str_multi_game_type_desc_1"
multiplayer_game_type_descs_end = "str_multi_game_type_descs_end"

quick_battle_troops_begin = "trp_quick_battle_troop_1"
quick_battle_troops_end = "trp_quick_battle_troops_end"

quick_battle_troop_texts_begin = "str_quick_battle_troop_1"
quick_battle_troop_texts_end = "str_quick_battle_troops_end"

quick_battle_scenes_begin = "scn_quick_battle_scene_1"
quick_battle_scenes_end = "scn_quick_battle_maps_end"

quick_battle_scene_images_begin = "mesh_cb_ui_maps_scene_01"

quick_battle_battle_scenes_begin = quick_battle_scenes_begin
quick_battle_battle_scenes_end = "scn_quick_battle_scene_4"

quick_battle_siege_scenes_begin = quick_battle_battle_scenes_end
quick_battle_siege_scenes_end = "scn_sea_battle"	#phaiak

quick_battle_naval_battle_scenes_begin = quick_battle_siege_scenes_end	#phaiak
quick_battle_naval_battle_scenes_end = "scn_coastal_assault_kennemer"	#phaiak

quick_battle_coastal_battle_scenes_begin = quick_battle_naval_battle_scenes_end	#phaiak
quick_battle_coastal_battle_scenes_end = quick_battle_scenes_end	#phaiak

quick_battle_scene_names_begin = "str_quick_battle_scene_1"

lord_quests_begin = "qst_deliver_message"
lord_quests_end   = "qst_follow_army"

lord_quests_begin_2 = "qst_destroy_bandit_lair"
lord_quests_end_2   = "qst_blank_quest_4"

enemy_lord_quests_begin = "qst_lend_surgeon"
enemy_lord_quests_end   = lord_quests_end

village_elder_quests_begin = "qst_deliver_grain"
village_elder_quests_end = "qst_eliminate_bandits_infesting_village"

village_elder_quests_begin_2 = "qst_blank_quest_6"
village_elder_quests_end_2   = "qst_blank_quest_8"

mayor_quests_begin  = "qst_move_cattle_herd"
mayor_quests_end    = village_elder_quests_begin

mayor_quests_begin_2 = "qst_blank_quest_10"
mayor_quests_end_2   = "qst_blank_quest_12"

lady_quests_begin = "qst_rescue_lord_by_replace"
lady_quests_end   = mayor_quests_begin

lady_quests_begin_2 = "qst_blank_quest_16"
lady_quests_end_2   = "qst_blank_quest_19"

army_quests_begin = "qst_deliver_cattle_to_army"
army_quests_end   = lady_quests_begin

army_quests_begin_2 = "qst_blank_quest_21"
army_quests_end_2   = "qst_blank_quest_21"

player_realm_quests_begin = "qst_consult_with_minister"
player_realm_quests_end = "qst_track_down_bandits"

all_items_begin = 0
all_items_end = "itm_items_end"

all_quests_begin = 0
all_quests_end = "qst_quests_end"

taverns_begin = "p_four_ways_inn" #anadido chief para taberna especial
towns_begin = "p_town_1"
castles_begin = "p_castle_1"
villages_begin = "p_village_1"

towns_end = castles_begin
castles_end = villages_begin
villages_end   = "p_salt_mine"
taverns_end = towns_end #anadidos chief para taberna especial

walled_centers_begin = towns_begin
walled_centers_end   = castles_end

centers_begin = towns_begin
centers_end   = villages_end

training_grounds_begin   = "p_training_ground_1"
training_grounds_end     = "p_monasterio1" #chief 

special_places_begin = "p_lumbercamp1"
special_places_end = "p_hadrian_wall1"

scenes_begin = "scn_town_1_center"
scenes_end = "scn_castle_1_exterior"

spawn_points_begin = "p_wales_spawn_point"
spawn_points_end = "p_testing_spawn_point"
laired_spawn_points_begin = spawn_points_begin
# laired_spawn_points_end = "p_caitness_priest_spawn_point"
laired_spawn_points_end = "p_channel_spawn_point" #must include legacy out-of-index parties for save compatibility
max_spawn_party_size = 180  #see party_templates for looters
phase_out            = 3 * max_spawn_party_size / 4  #point at which generally only ONE party per spawn point (game spawns parties up to 30% over limit)

regular_troops_begin       = "trp_novice_fighter"
regular_troops_end         = "trp_tournament_master"

swadian_merc_parties_begin = "p_town_1_mercs"
swadian_merc_parties_end   = "p_town_8_mercs"

vaegir_merc_parties_begin  = "p_town_8_mercs"
vaegir_merc_parties_end    = "p_zendar"

arena_masters_begin    = "trp_town_1_arena_master"
arena_masters_end      = "trp_town_1_armorer"

training_gound_trainers_begin    = "trp_trainer_1"
training_gound_trainers_end      = "trp_ransom_broker_1"

town_walkers_begin = "trp_town_walker_1"
town_walkers_end = "trp_village_walker_1"

village_walkers_begin = "trp_village_walker_1"
village_walkers_end   = "trp_spy_walker_1"

spy_walkers_begin = "trp_spy_walker_1"
spy_walkers_end = "trp_tournament_master"

walkers_begin = town_walkers_begin
walkers_end   = spy_walkers_end

armor_merchants_begin  = "trp_town_1_armorer"
armor_merchants_end    = "trp_town_1_weaponsmith"

weapon_merchants_begin = "trp_town_1_weaponsmith"
weapon_merchants_end   = "trp_town_1_tavernkeeper"

tavernkeepers_begin    = "trp_town_1_tavernkeeper"
tavernkeepers_end      = "trp_town_1_merchant"

goods_merchants_begin  = "trp_town_1_merchant"
goods_merchants_end    = "trp_town_1_horse_merchant"

horse_merchants_begin  = "trp_town_1_horse_merchant"
horse_merchants_end    = "trp_town_1_mayor"

mayors_begin           = "trp_town_1_mayor"
mayors_end             = "trp_village_1_elder"

village_elders_begin   = "trp_village_1_elder"
village_elders_end     = "trp_monje_mercader"

healer_begin 			= "trp_town_1_healer"
healer_end 				= "trp_healer_end"

shipwrights_begin 		= "trp_town_1_shipwright"
shipwrights_end 		= "trp_shipwright_end"

startup_merchants_begin = "trp_swadian_merchant"
startup_merchants_end = "trp_startup_merchants_end"

num_max_items = 10000 #used for multiplayer mode

average_price_factor = 1000
minimum_price_factor = 100
maximum_price_factor = 10000

village_prod_min = 0 #was -5
village_prod_max = 20 #was 20

trade_goods_begin = "itm_mead"
trade_goods_end = "itm_siege_supply"
food_begin = "itm_smoked_fish"
food_end = "itm_siege_supply"
bebidas_begin = "itm_wine" #chief anade para bebidas consumibles
bebidas_end = "itm_smoked_fish" #chief anade para bebidas consumibles
reference_books_begin = "itm_book_wound_treatment_reference"
reference_books_end   = trade_goods_begin
readable_books_begin = "itm_book_tactics"
readable_books_end   = reference_books_begin
books_begin = readable_books_begin
books_end = reference_books_end
horses_begin = "itm_common_horse"
horses_end = "itm_arrows"
weapons_begin = "itm_wooden_stick"
weapons_end = "itm_wooden_shield"
ranged_weapons_begin = "itm_darts"
ranged_weapons_end = "itm_torch"
armors_begin = "itm_leather_gloves"
armors_end = "itm_wooden_stick"
shields_begin = "itm_wooden_shield"
shields_end = ranged_weapons_begin
estandartes_begin = "itm_standard"
estandartes_end = "itm_horn"

# Banner constants
# Banner constants chief cambiado hacia abajo

banner_meshes_begin = "mesh_banner_extra01"
banner_meshes_end = "mesh_banner_kingdom_a"
kingdom_banner_meshes_end = "mesh_banner_default"

arms_meshes_begin = "mesh_arms_extra01"
banner_map_icons_begin = "icon_map_flag_extra01"
standard_mesh_strings_begin = "str_standard_extra01"

banner_scene_props_begin = "spr_banner_extra01"
banner_scene_props_end = "spr_banner_kingdom_a"
kingdom_banner_scene_props_end = "spr_banner_default"

arms_default = "mesh_arms_default"
banner_default = "mesh_banner_default"
banner_bg_default = 0xFFC0B090

arms_green = 0xFF2d7b34
arms_blue = 0xFF1176d4
arms_yellow = 0xFFceb036
arms_red = 0xFFbb2323
arms_lorange = 0xFFb29f89
arms_white = 0xFFe9e3db

# custom_banner_charges_begin = "mesh_custom_banner_charge_01"
# custom_banner_charges_end = "mesh_tableau_mesh_custom_banner"

# custom_banner_backgrounds_begin = "mesh_custom_banner_bg"
# custom_banner_backgrounds_end = custom_banner_charges_begin

# custom_banner_flag_types_begin = "mesh_custom_banner_01"
# custom_banner_flag_types_end = custom_banner_backgrounds_begin

# custom_banner_flag_map_types_begin = "mesh_custom_map_banner_01"
# custom_banner_flag_map_types_end = custom_banner_flag_types_begin

# custom_banner_flag_scene_props_begin = "spr_custom_banner_01"
# custom_banner_flag_scene_props_end = "spr_banner_a"

# custom_banner_map_icons_begin = "icon_custom_banner_01"
# custom_banner_map_icons_end = "icon_banner_01"

# Some constants for merchant invenotries
merchant_inventory_space = 30
num_merchandise_goods = 40

num_max_river_pirates = 25
num_max_zendar_peasants = 25
num_max_zendar_manhunters = 10

num_max_dp_bandits = 10
num_max_refugees = 10
num_max_deserters = 10

num_max_militia_bands = 15
num_max_armed_bands = 12

num_max_vaegir_punishing_parties = 20
num_max_rebel_peasants = 25

num_max_frightened_farmers = 50
num_max_undead_messengers  = 20

peak_prisoner_trains = 4
peak_kingdom_caravans = 12
peak_kingdom_messengers = 3


# Note positions
note_troop_location = 3

#battle tactics
btactic_hold = 1
btactic_follow_leader = 2
btactic_charge = 3
btactic_stand_ground = 4

#default right mouse menu orders
cmenu_move = -7
cmenu_follow = -6

# Town center modes - resets in game menus during the options
tcm_default 		= 0
tcm_disguised 		= 1
tcm_prison_break 	= 2
tcm_escape      	= 3

# Arena battle modes
#abm_fight = 0
abm_training = 1
abm_visit = 2
abm_tournament = 3

# Camp training modes
ctm_melee    = 1
ctm_ranged   = 2
ctm_mounted  = 3
ctm_training = 4

# Village bandits attack modes
vba_normal          = 1
vba_after_training  = 2

arena_tier1_opponents_to_beat = 3
arena_tier1_prize = 5
arena_tier2_opponents_to_beat = 6
arena_tier2_prize = 10
arena_tier3_opponents_to_beat = 10
arena_tier3_prize = 25
arena_tier4_opponents_to_beat = 20
arena_tier4_prize = 60
arena_grand_prize = 250

arena_max_teams = 6


#Additions
price_adjustment = 25 #the percent by which a trade at a center alters price

fire_duration = 4 #fires takes 4 hours

#NORMAL ACHIEVEMENTS
ACHIEVEMENT_NONE_SHALL_PASS = 1,
ACHIEVEMENT_MAN_EATER = 2,
ACHIEVEMENT_THE_HOLY_HAND_GRENADE = 3,
ACHIEVEMENT_LOOK_AT_THE_BONES = 4,
ACHIEVEMENT_KHAAAN = 5,
ACHIEVEMENT_GET_UP_STAND_UP = 6,
ACHIEVEMENT_BARON_GOT_BACK = 7,
ACHIEVEMENT_BEST_SERVED_COLD = 8,
ACHIEVEMENT_TRICK_SHOT = 9,
ACHIEVEMENT_GAMBIT = 10,
ACHIEVEMENT_OLD_SCHOOL_SNIPER = 11,
ACHIEVEMENT_CALRADIAN_ARMY_KNIFE = 12,
ACHIEVEMENT_MOUNTAIN_BLADE = 13,
ACHIEVEMENT_HOLY_DIVER = 14,
ACHIEVEMENT_FORCE_OF_NATURE = 15,

#SKILL RELATED ACHIEVEMENTS:
ACHIEVEMENT_BRING_OUT_YOUR_DEAD = 16,
ACHIEVEMENT_MIGHT_MAKES_RIGHT = 17,
ACHIEVEMENT_COMMUNITY_SERVICE = 18,
ACHIEVEMENT_AGILE_WARRIOR = 19,
ACHIEVEMENT_MELEE_MASTER = 20,
ACHIEVEMENT_DEXTEROUS_DASTARD = 21,
ACHIEVEMENT_MIND_ON_THE_MONEY = 22,
ACHIEVEMENT_ART_OF_WAR = 23,
ACHIEVEMENT_THE_RANGER = 24,
ACHIEVEMENT_TROJAN_BUNNY_MAKER = 25,

#MAP RELATED ACHIEVEMENTS:
ACHIEVEMENT_MIGRATING_COCONUTS = 26,
ACHIEVEMENT_HELP_HELP_IM_BEING_REPRESSED = 27,
ACHIEVEMENT_SARRANIDIAN_NIGHTS = 28,
ACHIEVEMENT_OLD_DIRTY_SCOUNDREL = 29,
ACHIEVEMENT_THE_BANDIT = 30,
ACHIEVEMENT_GOT_MILK = 31,
ACHIEVEMENT_SOLD_INTO_SLAVERY = 32,
ACHIEVEMENT_MEDIEVAL_TIMES = 33,
ACHIEVEMENT_GOOD_SAMARITAN = 34,
ACHIEVEMENT_MORALE_LEADER = 35,
ACHIEVEMENT_ABUNDANT_FEAST = 36,
ACHIEVEMENT_BOOK_WORM = 37,
ACHIEVEMENT_ROMANTIC_WARRIOR = 38,

#POLITICALLY ORIENTED ACHIEVEMENTS:
ACHIEVEMENT_HAPPILY_EVER_AFTER = 39,
ACHIEVEMENT_HEART_BREAKER = 40,
ACHIEVEMENT_AUTONOMOUS_COLLECTIVE = 41,
ACHIEVEMENT_I_DUB_THEE = 42,
ACHIEVEMENT_SASSY = 43,
ACHIEVEMENT_THE_GOLDEN_THRONE = 44,
ACHIEVEMENT_KNIGHTS_OF_THE_ROUND = 45,
ACHIEVEMENT_TALKING_HELPS = 46,
ACHIEVEMENT_KINGMAKER = 47,
ACHIEVEMENT_PUGNACIOUS_D = 48,
ACHIEVEMENT_GOLD_FARMER = 49,
ACHIEVEMENT_ROYALITY_PAYMENT = 50,
ACHIEVEMENT_MEDIEVAL_EMLAK = 51,
ACHIEVEMENT_CALRADIAN_TEA_PARTY = 52,
ACHIEVEMENT_MANIFEST_DESTINY = 53,
ACHIEVEMENT_CONCILIO_CALRADI = 54,
ACHIEVEMENT_VICTUM_SEQUENS = 55,

#MULTIPLAYER ACHIEVEMENTS:
ACHIEVEMENT_THIS_IS_OUR_LAND = 56,
ACHIEVEMENT_SPOIL_THE_CHARGE = 57,
ACHIEVEMENT_HARASSING_HORSEMAN = 58,
ACHIEVEMENT_THROWING_STAR = 59,
ACHIEVEMENT_SHISH_KEBAB = 60,
ACHIEVEMENT_RUIN_THE_RAID = 61,
ACHIEVEMENT_LAST_MAN_STANDING = 62,
ACHIEVEMENT_EVERY_BREATH_YOU_TAKE = 63,
ACHIEVEMENT_CHOPPY_CHOP_CHOP = 64,
ACHIEVEMENT_MACE_IN_YER_FACE = 65,
ACHIEVEMENT_THE_HUSCARL = 66,
ACHIEVEMENT_GLORIOUS_MOTHER_FACTION = 67,
ACHIEVEMENT_ELITE_WARRIOR = 68,

#COMBINED ACHIEVEMENTS
ACHIEVEMENT_SON_OF_ODIN = 69,
ACHIEVEMENT_KING_ARTHUR = 70,
ACHIEVEMENT_KASSAI_MASTER = 71,
ACHIEVEMENT_IRON_BEAR = 72,
ACHIEVEMENT_LEGENDARY_RASTAM = 73,
ACHIEVEMENT_SVAROG_THE_MIGHTY = 74,

ACHIEVEMENT_MAN_HANDLER = 75,
ACHIEVEMENT_GIRL_POWER = 76,
ACHIEVEMENT_QUEEN = 77,
ACHIEVEMENT_EMPRESS = 78,
ACHIEVEMENT_TALK_OF_THE_TOWN = 79,
ACHIEVEMENT_LADY_OF_THE_LAKE = 80,

#formations motomataru chief
#Formation tweaks
formation_minimum_spacing	= 47 # chief cambiado
formation_minimum_spacing_horse_length	= 300
formation_minimum_spacing_horse_width	= 200
formation_start_spread_out	= 2	#extra 50cm spacings for ease of movement for new formations
formation_min_foot_troops	= 13	#minimum to make foot formation
formation_min_cavalry_troops	= 5	#minimum to make cavalry wedge
formation_native_ai_use_formation = 1
formation_delay_for_spawn	= .4	#used for M&B 1.011 implementation
formation_reequip	= 1	#allow troops in formations to switch weapons
formation_reform_interval	= 2 #seconds
formation_rethink_for_formations_only	= 0

#Other constants (not tweaks)
Third_Max_Weapon_Length = 220 / 3
Km_Per_Hour_To_Cm = formation_reform_interval * 100000 / 3600
Reform_Trigger_Modulus = formation_reform_interval * 2	#trigger is half-second
Top_Speed	= 13
Far_Away	= 1000000

#positions used through formations and AI triggers
Current_Pos     = 34	#pos34
Speed_Pos       = 36	#pos36
Target_Pos      = 37	#pos37
Enemy_Team_Pos  = 38	#pos38
Temp_Pos        = 39	#pos39

#keys used for old M&B
#from header_triggers import *
key_for_ranks       = key_j
key_for_shieldwall  = key_k
key_for_wedge       = key_l
key_for_square      = key_semicolon
key_for_undo        = key_u

#Hold Over There Command Tracking
HOT_no_order           = 0
HOT_F1_pressed         = 1
HOT_F1_held            = 2

#Team Slots SEE SECTION

scratch_team = 7	#Should be used just for above slots. If you use it, check for conflicts.

WB_Implementation   = 0
WFaS_Implementation = 1
Native_Formations_Implementation = WB_Implementation

#Other slots
#use faction slots to remember information between battles
slot_faction_d0_mem_formation           = 300
slot_faction_d0_mem_formation_space     = 309
slot_faction_d0_mem_relative_x_flag     = 318
slot_faction_d0_mem_relative_y          = 327
#NEXT                                   = 336

#the following applied only to infantry in formation
slot_agent_formation_rank      = 29
slot_agent_inside_formation    = 30
slot_agent_nearest_enemy_agent = 31
slot_agent_new_division        = 32

#motomataru chief IA Improved
#AI variables
AI_long_range	= 8000	#do not put over 130m if you want archers to always fire
AI_firing_distance	= AI_long_range / 2
AI_charge_distance	= 2000
AI_for_kingdoms_only	= 1
Percentage_Cav_For_New_Dest	= 40
Hold_Point	= 100	#archer hold if outnumbered
Advance_More_Point	= 100 - Hold_Point * 100 / (Hold_Point + 100)	#advance 'cause expect other side is holding
AI_Max_Reinforcements = Far_Away	#maximum number of reinforcement stages in a battle
AI_Replace_Dead_Player	=	1
AI_Poor_Troop_Level	= 24	#average level of troops under which a division may lose discipline

#Battle Phases
BP_Ready  = 0
BP_Init   = 1
BP_Deploy = 2
BP_Setup  = 3
BP_Jockey = 4
BP_Duel   = 5
BP_Fight  = 6

#positions used in a script, named for convenience
Nearest_Enemy_Troop_Pos	= 48	#pos48	used only by infantry AI
Nearest_Enemy_Battlegroup_Pos	= 50	#pos50	used only by ranged AI
Nearest_Threat_Pos	= Nearest_Enemy_Troop_Pos	#used only by cavalry AI
Nearest_Target_Pos	= Nearest_Enemy_Battlegroup_Pos	#used only by cavalry AI
Infantry_Pos	= 51	#pos51
Archers_Pos	= 53	#pos53
Cavalry_Pos	= 54	#pos54
Team_Starting_Point	= 55	#pos55

#positions used through battle
Team0_Cavalry_Destination	= 56	#pos56
Team1_Cavalry_Destination	= 57	#pos57
Team2_Cavalry_Destination	= 58	#pos58
Team3_Cavalry_Destination	= 59	#pos59
#Ia improved chief acaba motomataru

##############
###messenger system
orders_follow     = 407
orders_gotoplace     = 408
orders_patrolarea     = 409
orders_besiegeplace     = 410
#orders_raidarea     = 410
#orders_guardplace     = 411
diplomacy_insult     = 412
diplomacy_sendgift     = 413
#diplomacy_invitation     = 414
diplomacy_sugalliance     = 415
diplomacy_suggestpeace     = 416
diplomacy_declarewar     = 417
no_menssage_choosed     = 419

#faction orders faction screen
factionorders_no     = 420
factionorders_commonarmy     = 421
factionorders_deffense     = 422
factionorders_fyrd     = 423

####

#para negativos equipamiento chief habilidades
desnudos_begin = "itm_pictish_painted1"
desnudos_end = "itm_picts_hoodtunic_03" 
armadura_pesada_begin = "itm_mail_shirt"
armadura_pesada_end = "itm_burlap_tunic" 
armadura_pesada2_begin = "itm_addon_mail4"
armadura_pesada2_end = "itm_trophy_norse" 
armadura_media_begin = "itm_gambeson1"
armadura_media_end = armadura_pesada_begin
yelmos_pesados_begin = "itm_briton_helm"
yelmos_pesados_end = "itm_crown1" 
escudos_pesados_begin = "itm_wooden_shield"
escudos_pesados_end = "itm_tab_shield_small_round_c" 

########################################################
##  COLOR chief CODES             ############################
########################################################
# Add in color codes
color_great_news = 0xCCFFCC
color_good_news = 0xCCFFCC
color_terrible_news = 0xFFCCCC  #0xFF2222
color_bad_news = 0xFFCCCC
color_neutral_news = 0xFFFFFF
color_quest_and_faction_news = 0xCCCCFF
color_hero_news = 0xFFFF99
#  Percent modifier of days between prisoner escapes (bigger number = less likely escapes)
prisoners_escape_chance_modifier = 50
#garnier chief acaba

#dungeon chief
dungeon_prisoners_begin = "trp_refugeeromanruins"
dungeon_prisoners_end = "trp_refugeedruid"
stone_refugee_begin = "trp_refugeedruid"
stone_refugee_end = "trp_prisionerdruid"


# Various constants
absolute = 1
true     = 1
false    = 0
player   = 0

#Values for agent_get_combat_state
cs_free                      = 0
cs_target_in_sight           = 1     # ranged units
cs_guard                     = 2     # no shield
cs_wield                     = 3     # reach out weapon, preparing to strike, melee units
cs_fire                      = 3     # ranged units
cs_swing                     = 4     # cut / thrust, melee units
cs_load                      = 4     # crossbow units
cs_still                     = 7     # melee units, happens, not always (seems to have something to do with the part of body hit), when hit
cs_no_visible_targets        = 7     # ranged units or blocking with a shield
cs_target_on_right_hand_side = 8     # horse archers

#Presentations Constants Moto chief
Screen_Border_Width = 24
Screen_Width = 1024-Screen_Border_Width
Screen_Height = 768-Screen_Border_Width
Screen_Text_Height = 35
Screen_Checkbox_Height_Adj = 4
Screen_Numberbox_Width = 64
Screen_Title_Height = Screen_Height-Screen_Border_Width-Screen_Text_Height
Screen_Check_Box_Dimension = 20
Screen_Undistort_Width_Num = 7  #distortion midway between 1024x768 and 1366x768 -- things will appear a little narrow on thin screens and vice versa
Screen_Undistort_Width_Den = 8

#Outfit Party Presentation
Outfit_Character_Button_Width = 60
Outfit_Character_Button_Margin = 20
Outfit_Character_Button_Height = 320
Outfit_Character_Button_Space_Width = Outfit_Character_Button_Width + Outfit_Character_Button_Margin
Outfit_Character_Button_Spaces = Screen_Width / Outfit_Character_Button_Space_Width
Outfit_Inventory_Label_Right = Screen_Border_Width + 165
Outfit_Inventory_Button_Space_Height = (Screen_Height/2-Screen_Border_Width) / 5
Outfit_Inventory_Button_Space_Width = Outfit_Inventory_Button_Space_Height
Outfit_Inventory_Button_Margin = 10
Outfit_Inventory_Button_Height = Outfit_Inventory_Button_Space_Height - Outfit_Inventory_Button_Margin
Outfit_Inventory_Button_Width = Outfit_Inventory_Button_Height
Outfit_Inventory_Scroll_X_Offset = -1*Outfit_Inventory_Button_Space_Width/2
Outfit_Inventory_Scroll_Y_Offset = -1*Outfit_Inventory_Button_Space_Height/2
Outfit_Selected_Troop_Button_Color = 0xFFCB30
Outfit_Selected_Troop_Text_Color = 0xFF0000
Outfit_Alpha = 0x80 #50%
Outfit_Mouse_Over_Text_Color = 0x207010
Outfit_Mouse_Over_Button_Color = 2*Outfit_Mouse_Over_Text_Color


Outfit_Thorax_Length = 60  #length dark ages human thorax
Outfit_Fast_Weapon_Speed = 100
Outfit_Merchant_Due_Troop_Slot = slot_troop_prisoner_of_party
Outfit_List_Value_Multiplier = 1000000
Outfit_List_Troop_Multiplier = 1000

#Arrays
Outfit_List_First_Button = 0 #tracking list overlays
Outfit_List_Last_Overlay = 1
Outfit_List_Left_Scroll = 2
Outfit_List_Right_Scroll = 3
Outfit_List_Pages = 4  #how many right scrolls
Outfit_List_Page_Size = 5  #how far scroll goes
Outfit_List_Num_Elements = 6  #length of list
Outfit_List_Data = 7  #first element of list

Outfit_Shops_List = "trp_temp_array_a"
Outfit_Shops_List_Start = 0
Outfit_Selected_List = "trp_temp_array_a"
Outfit_Selected_List_Start = 10
Outfit_Armor_List = "trp_temp_array_b"
Outfit_Armor_List_Start = 0
Outfit_Melee_Weapon_List = "trp_temp_array_c"
Outfit_Melee_Weapon_List_Start = 0
Outfit_Ranged_Weapon_List = "trp_temp_array_c"
Outfit_Ranged_Weapon_List_Start = 100
Outfit_Missile_List = "trp_temp_array_c"
Outfit_Missile_List_Start = 200
Outfit_Horse_List = "trp_temp_array_a"
Outfit_Horse_List_Start = 100
Outfit_Lists_List = Outfit_Shops_List #Shops List used only in init
Outfit_Lists_List_Start = Outfit_Shops_List_Start

#Troop Tree Presentation
Troop_Tree_Num_Levels = 6
Troop_Tree_Max_Per_Level = 5  #2^(Troop_Tree_Num_Levels-1) opt for counting most upgrade2 over all factions
Troop_Tree_Area_Height = Screen_Title_Height-4*Screen_Text_Height
Troop_Tree_Area_Width = Screen_Width-2*Screen_Border_Width
Troop_Tree_Line_Color = 0x001380
Troop_Tree_Tableau_Height = 800
Troop_Tree_Tableau_Width = Troop_Tree_Tableau_Height*Screen_Undistort_Width_Num/Screen_Undistort_Width_Den

#Camera
camera_trigger_interval = .1  #fastest trigger rate with 1000 agents in scene on my machine is 100 milliseconds
camera_animation_time = camera_trigger_interval * 1300  #the actual call interval is often 20% longer
camera_key_rotate_attenuator = 2
camera_minimum_z = 150
camera_minimum_pitch = 271
camera_maximum_pitch = 450
camera_effective_min_zoom = 35  #engine won't zoom in more than this (though the zoom "setting" will go as low as 1)
camera_fixed_angle_h = 7  #fixed angle to targeted agents/props
camera_fixed_angle_v = 6

#Camera Bit Switches
camera_manual          = 0x001
camera_follow_terrain  = 0x002
camera_reverse_y       = 0x004
camera_pan_to_rotation = 0x008  #camera pans AFTER it is rotated
camera_pan_back_forth  = 0x010  #camera command groups
camera_pan_right_left  = 0x020
camera_pan_up_down     = 0x040
camera_rotate          = 0x080
camera_target_agent    = 0x100
camera_target_prop     = 0x200  #not yet implemented
camera_game_slow       = 0x400

#Bit switches for global $option_switches for keeping track of which menu/dialog options have been chosen
option_1 = 0x001
option_2 = 0x002
option_3 = 0x004
option_4 = 0x008
option_5 = 0x010
option_6 = 0x020
lord_option_recruit   = 0x040 #no longer used
lord_option_private   = 0x080
lord_option_task      = 0x100
lord_option_vassalage = 0x200

#Bit switches for global $first_time for keeping track of what has been done at least once in a given game
first_time_death_camera    = 0x0001
first_time_strategy_camera = 0x0002
first_time_game_rules      = 0x0004
first_time_doccinga        = 0x0008
first_time_check_lairs     = 0x0010	#remove extra lairs VC 1.04 beta
first_time_check_l_lairs   = 0x0020	#remove all looter lairs VC 1.04 beta
first_time_check_l2_lairs  = 0x0040	#try again
first_time_load_main_party = 0x0080  #this used in reverse
first_time_cam_battle      = 0x0100
first_time_hold_F1         = 0x0200
first_time_formations      = 0x0400
first_time_food_store      = 0x0800	#change food system after VC 2.0
first_time_fix_centers     = 0x1000	#VC-3241
first_time_fix_ports       = 0x2000	#VC-3829
first_time_fix_home_center = 0x4000	#VC-3829
first_time_redo_defectors  = 0x8000	#VC-3909

#shader
shader_snow_line	= 230
shader_spring		= 0
shader_summer		= 1
shader_autumn		= 2
shader_winter		= 3

#ship types
ship_type_busse		= 1
ship_type_skei		= 2
ship_type_karvi		= 3
ship_type_snekkja	= 4
ship_type_knorr		= 5
ship_type_byrding	= 6

#map boundaries		#well... in module.ini there are other values...
map_min_x = -275
map_max_x = 275
map_min_y = -275
map_max_y = 275

#MP
#player list action type
plat_pollkick	= 1
plat_pollban	= 2
plat_kick		= 3
plat_ban		= 4
plat_mute		= 5
plat_unmute		= 6
plat_tempban	= 7
plat_slay		= 8
plat_heal		= 9
plat_swap_team	= 10
plat_swap_spec	= 11
plat_give_hammer= 12
plat_beacon		= 13
plat_refill		= 14
plat_fix_shield	= 15
plat_teleport_me = 16
plat_teleport_him = 17
plat_immortal	= 18
plat_mortal		= 19


########################################
#Presentantions
font_title = 2400
font_small = 800
font_normal = 1200

########################################
# For debugging and developing

# shows mouse coordinates on presentations (set 0 for production)
debug_show_presentation_coordinates = 0

# Decapitation system
debug_goredec = 0 # 0: OFF, 1: show extra info, 2: skip checks

# Diplomatic report (notes)
debug_diplomatic_relations = 0 # 0: OFF, 1: show extra info

# Companions presentation: deck of companions (each is a card) with central portrait and info
companions_prsnt_debug = 0 # 0: OFF, 1: show extra info
companions_prsnt_show_members_not_in_party = 0 # 0: black card, 1: grey out card, no name, 2: grey out card, show name
companions_prsnt_show_lords = 0 # 0: won't show companions that are now lords, 1: shows
companions_prsnt_show_storyline_mode = 0 # 0:disable for storyline, 1: enable this

# Troop Detail
debug_troop_detail = 0 # 0: OFF, 1: show extra info

# SET GOAL
debug_set_goal = 0 # 0: OFF, 1: show extra info, 2: show details on cf_ tests

# VC-2605
slot_quest_menu_town_visit = slot_quest_menu_4
slot_quest_menu_castle_visit = slot_quest_menu_9 + 1
slot_quest_menu_auto_sea_travel = slot_quest_menu_13 + 1
slot_quest_menu_town_port = slot_quest_menu_19 + 1
slot_quest_menu_town_recruit = slot_quest_menu_18 + 1
slot_quest_menu_town_sail = slot_quest_menu_22 + 1
slot_quest_menu_leave = slot_quest_menu_23 + 1
slot_quest_menu_village_recruit = slot_quest_menu_2
slot_quest_menu_village_visit = slot_quest_menu_3
slot_quest_menu_meet_leader = slot_quest_menu_4

#sea battle
boarding_progress_peak_0 = 60
boarding_progress_peak = 70

# VC-3689
menu_none         =  0
menu_left         = -1
menu_right_1      =  1
menu_right_2      =  2
menu_fake_div     =  3

menu_right_max    =  2
menu_fake_div_max =  6

player_func_none      = 0
player_func_creeping  = 0x01
player_func_trait     = 0x02
player_func_horsecall = 0x04

dot_size        = 4000
dot_spacing_div = 30
dot_color       = 0x000000
dot_alpha       = 0xC0  #75%

# VC work mini game
vc_work_payment_1 = 15
vc_work_payment_2 = 20
vc_work_payment_3 = 25
