@echo off
python process_init.py
python process_global_variables.py

python process_scenes.py
python process_scene_props.py
python process_simple_triggers.py
: python process_dialogs.py
: ppx2 "-P N" runs up to N asynchronous (parallel) compiles.
echo process_dialogs.py process_strings.py process_skills.py process_music.py process_animations.py process_meshes.py process_sounds.py process_skins.py process_factions.py process_particle_sys.py process_quests.py process_info_pages.py process_postfx.py |binary\ppx2 -P %NUMBER_OF_PROCESSORS% python {}
: dependent on above
python process_items.py
python process_map_icons.py
: dependent on items
python process_troops.py
python process_tableau_materials.py
python process_presentations.py
python process_scripts.py
python process_game_menus.py
python process_mission_tmps.py
: dependent on troops
python process_party_tmps.py
: dependent on party_templates
python process_parties.py

python process_global_variables_unused.py
@del *.pyc
echo.
echo ______________________________
echo.
echo Script processing has ended.
echo Press any key to exit. . .
pause>nul