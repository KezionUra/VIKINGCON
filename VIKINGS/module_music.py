from header_music import *
####################################################################################################################
#  Each track record contains the following fields:
#  1) Track id: used for referencing tracks.
#  2) Track file: filename of the track
#  3) Track flags. See header_music.py for a list of available flags
#  4) Continue Track flags: Shows in which situations or cultures the track can continue playing. See header_music.py for a list of available flags
####################################################################################################################

# WARNING: You MUST add mtf_module_track flag to the flags of the tracks located under module directory

tracks = [
("bogus", "silentio.wav", 0, 0),

#main menu
("mount_and_blade_title_screen", "viking_raid.wav", mtf_module_track|mtf_sit_main_title|mtf_start_immediately, 0), #chief cambiado

#map travel
("travel_1","celtic_legend.wav",mtf_module_track|mtf_sit_travel, mtf_sit_travel|mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_sit_military),
("travel_2","nordicorchstra.wav",mtf_module_track|mtf_sit_travel, mtf_sit_travel|mtf_sit_town|mtf_sit_tavern|mtf_sit_night),
("travel_3","celtic.wav",mtf_module_track|mtf_sit_travel, mtf_sit_travel|mtf_sit_town|mtf_sit_tavern|mtf_sit_night),
("travel_4","go_bikes.wav",mtf_module_track|mtf_sit_travel, mtf_sit_travel|mtf_sit_town|mtf_sit_tavern|mtf_sit_night),
("travel_5","werihukka.wav",mtf_module_track|mtf_sit_travel, mtf_sit_travel|mtf_sit_town|mtf_sit_tavern|mtf_sit_night),
("travel_6","nabia_orebia.wav",mtf_module_track|mtf_sit_travel, mtf_sit_travel|mtf_sit_town|mtf_sit_tavern|mtf_sit_night),

#towns and villages
("town_1","celtic_legend.wav",mtf_module_track|mtf_sit_town, mtf_sit_travel|mtf_sit_tavern|mtf_sit_night|mtf_sit_military),
("town_2","celtic.wav",mtf_module_track|mtf_sit_town, mtf_sit_travel|mtf_sit_tavern|mtf_sit_night|mtf_sit_military),
("town_3","samania_aracillum.wav",mtf_module_track|mtf_sit_town, mtf_sit_tavern|mtf_sit_night),
("town_4","viking_raid.wav",mtf_module_track|mtf_sit_town, mtf_sit_tavern|mtf_sit_night),

#tavern and feast
("tavern_1", "iberus_flumen.wav", mtf_module_track|mtf_sit_tavern|mtf_sit_feast, 0),
("tavern_2", "celtic_spirit.wav", mtf_module_track|mtf_sit_tavern|mtf_sit_feast, 0),

#military and inflitrate
("castle_1","day_of_war.wav",mtf_module_track|mtf_sit_military, mtf_sit_travel|mtf_sit_tavern|mtf_sit_night|mtf_sit_town),
("castle_2","celtic_legend.wav",mtf_module_track|mtf_sit_military, mtf_sit_travel|mtf_sit_tavern|mtf_sit_night|mtf_sit_town),
("castle_3","fallen_warrior.wav",mtf_module_track|mtf_sit_military, mtf_sit_travel|mtf_sit_tavern|mtf_sit_night|mtf_sit_town),

#holy places
("monastery_1", "theancients.wav", mtf_module_track, 0),

#arena
("arena_1","day_of_war.wav", mtf_module_track|mtf_sit_arena, 0),
("arena_2","werihukka.wav", mtf_module_track|mtf_sit_arena, 0),
("arena_3","go_bikes.wav", mtf_module_track|mtf_sit_arena, 0),
#("arena_5","arena_1.ogg", mtf_module_track|mtf_sit_arena, 0),

#singleplayer battle
("battle_1","viking_raid.wav",mtf_module_track|mtf_sit_fight|mtf_sit_ambushed, 0),
("battle_2","celtic_spirit.wav",mtf_module_track|mtf_sit_fight|mtf_sit_ambushed, 0),
("battle_3","day_of_war.wav",mtf_module_track|mtf_sit_fight|mtf_sit_ambushed, 0),
("battle_4","go_bikes.wav",mtf_module_track|mtf_sit_fight|mtf_sit_ambushed, 0),

("siege_1", "solemnfuneralpyre.wav", mtf_module_track|mtf_sit_siege, mtf_sit_fight|mtf_sit_ambushed),  
("siege_2", "samania_aracillum.wav", mtf_module_track|mtf_sit_siege, mtf_sit_fight|mtf_sit_ambushed),
  
("ambushed_1", "day_of_war.wav", mtf_module_track|mtf_sit_ambushed, mtf_sit_fight|mtf_sit_siege),
("ambushed_2", "samania_aracillum.wav", mtf_module_track|mtf_sit_ambushed, mtf_sit_fight|mtf_sit_siege),



("defeated_1","solemnfuneralpyre.wav",mtf_module_track|mtf_sit_killed,0),

("victorious_1","viking_raid.wav",mtf_module_track|mtf_sit_victorious,0),#|mtf_persist_until_finished


###multiplayer music
("multiplayer_battle_1","viking_raid.wav",mtf_module_track|mtf_sit_multiplayer_fight, 0),
("multiplayer_battle_2","celtic_spirit.wav",mtf_module_track|mtf_sit_multiplayer_fight, 0),
("multiplayer_battle_3","theancients.wav",mtf_module_track|mtf_sit_multiplayer_fight, 0),
("multiplayer_battle_4","celtic_legend.wav",mtf_module_track|mtf_sit_multiplayer_fight, 0),
("multiplayer_battle_5","fallen_warrior.wav",mtf_module_track|mtf_sit_multiplayer_fight, 0),
("multiplayer_battle_6","nordicorchstra.wav",mtf_module_track|mtf_sit_multiplayer_fight, 0),

###



####Other music (called mostly by scripts)
#chief anadidos para bardos
  ("c2", "tras_la_galerna.wav", mtf_module_track|mtf_persist_until_finished, 0),
  ("c105", "mons_vindius.wav", mtf_module_track|mtf_persist_until_finished, 0),
#chief bardos acaba
  ("escape", "go_bikes.wav", mtf_module_track|mtf_persist_until_finished, 0),
#monastery
  ("gregoriano", "theancients.wav", mtf_module_track|mtf_persist_until_finished, 0),
#pagan holy site
  ("paganholysite", "fallen_warrior.wav", mtf_module_track|mtf_persist_until_finished, 0),

  ("epic_music", "viking_raid.wav", mtf_module_track|mtf_sit_fight, 0),
  ("victorious_evil", "samania_aracillum.wav", mtf_module_track, 0),

  

####Native music (to replace???)
  ("calm_night_1", "nordicorchstra.wav", mtf_module_track|mtf_sit_night, mtf_sit_town|mtf_sit_tavern|mtf_sit_travel),
  ("captured", "fallen_warrior.wav", mtf_module_track|mtf_persist_until_finished, 0),

  ("empty_village", "solemnfuneralpyre.wav", mtf_module_track, 0),

  ("outdoor_beautiful_land", "solemnfuneralpyre.wav", mtf_module_track|mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_night|mtf_sit_tavern),
  ("uncertain_homestead", "fallen_warrior.wav", mtf_module_track|mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),
  ("tragic_village", "solemnfuneralpyre.wav", mtf_module_track|mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),

  ("wedding", "celtic_legend.wav", mtf_module_track|mtf_persist_until_finished, 0),
  ("coronation", "viking_raid.wav", mtf_module_track|mtf_persist_until_finished, 0),
  ("morrigan_song", "ballad_of_a_hero.wav", mtf_module_track, 0),
  
# ambient battle music:
  ("ambient_music_1", "battle_ambient_1.wav", mtf_module_track|mtf_sit_ambient_music, 0),
  ("ambient_music_2", "battle_ambient_2.wav", mtf_module_track|mtf_sit_ambient_music, 0),
##  ("ambient_music_3", "battle_ambient_3.wav", mtf_module_track|mtf_sit_ambient_music, 0),
##  ("ambient_music_4", "battle_ambient_4.wav", mtf_module_track|mtf_sit_ambient_music, 0),
##  ("ambient_music_5", "battle_ambient_5.wav", mtf_module_track|mtf_sit_ambient_music, 0),
##  ("ambient_music_6", "battle_ambient_6.wav", mtf_module_track|mtf_sit_ambient_music, 0),
##  ("ambient_music_7", "battle_ambient_7.wav", mtf_module_track|mtf_sit_ambient_music, 0),
##  ("ambient_music_8", "battle_ambient_8.wav", mtf_module_track|mtf_sit_ambient_music, 0),
##  ("ambient_music_9", "battle_ambient_9.wav", mtf_module_track|mtf_sit_ambient_music, 0),
##  ("ambient_music_10", "battle_ambient_10.wav", mtf_module_track|mtf_sit_ambient_music, 0),
]
