Notes on Viking Conquest Mod Sys

Version: 2.024
Warband: 1.168
Date: 16 June, 2016

ADDING ITEMS
The compiler autogenerates a table of no-swing versions of all weapons (for temporary use during battle). It is highly recommended, when changing the weapons table, to temporarily comment out the Python call at the end of module_items.py. Otherwise, save games will lose compatibility. 

append_noswing_items(items)

SAVE COMPATIBILITY
Keyed list elements added after the initial release in Dec. 2014 were appended to the end of files in order to preserve save compatibility. This is sometimes not the best place for them.

Moreover, there are some triggers, like simple trigger #game load trigger(165), which were used to update old games. Most of this trigger would not be needed for games starting AFTER the current version.
