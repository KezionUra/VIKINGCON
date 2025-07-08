from header_quests import *

####################################################################################################################
#  Each quest record contains the following fields:
#  1) Quest id: used for referencing quests in other files. The prefix qst_ is automatically added before each quest-id.
#  2) Quest Name: Name displayed in the quest screen.
#  3) Quest flags. See header_quests.py for a list of available flags
#  4) Quest Description: Description displayed in the quest screen.
#
# Note that you may call the opcode setup_quest_text for setting up the name and description
####################################################################################################################

quests = [
# Note : This is defined as the first governer quest in module_constants.py: 
 ("deliver_message", "Deliver Message to {s13}", qf_random_quest,
  "{s9} asked you to take a message to {s13}. {s13} was at {s4} when you were given this quest."
  ),
 ("deliver_message_to_enemy_lord", "Deliver Message to {s13}", qf_random_quest,
  "{s9} asked you to take a message to {s13} of {s15}. {s13} was at {s4} when you were given this quest."
  ),
 ("raise_troops", "Raise {reg1} {s14}", qf_random_quest,
  "{s9} asked you to raise {reg1} {s14} and bring them to him."
  ),
 ("escort_lady", "Escort {s13} to {s14}", qf_random_quest,
  "{!}None"
  ),
## ("rescue_lady_under_siege", "Rescue {s3} from {s4}", qf_random_quest,
##  "{s1} asked you to rescue his {s7} {s3} from {s4} and return her back to him."
##  ),
## ("deliver_message_to_lover", "Deliver Message to {s3}", qf_random_quest,
##  "{s1} asked you to take a message to his lover {s3} at {s4}."
##  ),
## ("bring_prisoners_to_enemy", "Bring Prisoners to {s4}", qf_random_quest,
##  "{s1} asked you to bring {reg1} {s3} as prisoners to the guards at {s4}."
##  ),
## ("bring_reinforcements_to_siege", "Bring Reinforcements to the Siege of {s5}", qf_random_quest,
##  "{s1} asked you to bring {reg1} {s3} to {s4} at the siege of {s5}."
##  ),
## ("deliver_supply_to_center_under_siege", "Deliver Supplies to {s5}", qf_random_quest,
##  "TODO: Take {reg1} cartloads of supplies from constable {s3} and deliver them to constable {s4} at {s5}."
##  ),
 ("deal_with_bandits_at_lords_village", "Save the Village of {s15} from Marauding Bandits", qf_random_quest,
  "{s13} asked you to deal with the bandits who took refuge in his village of {s15} and then report back to him."
  ),
 ("collect_taxes", "Collect Taxes from {s3}", qf_random_quest,
  "{s9} asked you to collect taxes from {s3}. He offered to leave you one-fifth of all the money you collect there."
  ),
 ("hunt_down_fugitive", "Hunt Down {s4}", qf_random_quest,
  "{s9} asked you to hunt down the fugitive named {s4}. He is currently believed to be at {s3}."
  ),
## ("capture_messenger", "Capture {s3}", qf_random_quest,
##  "{s1} asked you to capture a {s3} and bring him back."
##  ),
## ("bring_back_deserters", "Bring {reg1} {s3}", qf_random_quest,
##  "{s1} asked you to bring {reg1} {s3}."
##  ),
 ("kill_local_merchant", "Assassinate Local Merchant at {s3}", qf_random_quest,
  "{s9} asked you to assassinate a local merchant at {s3}."
  ),
 ("bring_back_runaway_serfs", "Bring Back Runaway Serfs", qf_random_quest,
  "{s9} asked you to bring back the three groups of runaway serfs back to {s2}. He said all three groups must be running away in the direction of {s3}."
  ),
 ("follow_spy", "Follow the Spy to Meeting", qf_random_quest,
  "{s11} asked you to follow the spy that will leave {s12}. You must be careful not to be seen by the spy during his travel, or else he may get suspicious and turn back. Once the spy meets with his accomplice, you are to ambush and capture them and bring them both back to {s11}."
  ),
 ("capture_enemy_hero", "Capture a Lord from {s13}", qf_random_quest,
  "{!}TODO: {s11} asked you to capture a lord from {s13}."
  ),
 ("lend_companion", "Lend Your Companion {s3} to {s9}", qf_random_quest,
  "{s9} asked you to lend your companion {s3} to him for a week."
  ),
 ("collect_debt", "Collect the Debt {s3} Owes to {s9}", qf_random_quest,
  "{s9} asked you to collect the debt of {reg4} peningas {s3} owes to him."
  ),
## ("capture_conspirators", "Capture Conspirators", qf_random_quest,
##  "TODO: {s1} asked you to capture all troops in {reg1} conspirator parties that plan to rebel against him and join {s3}."
##  ),
## ("defend_nobles_against_peasants", "Defend Nobles Against Peasants", qf_random_quest,
##  "TODO: {s1} asked you to defend {reg1} noble parties against peasants."l
##  ),
 ("incriminate_loyal_commander", "Incriminate the Loyal Commander of {s13}, {s16}", qf_random_quest,
  "{!}None"
  ),
# ("raid_caravan_to_start_war", "Raid {reg13} Caravans of {s13}", qf_random_quest,   #This is now a dynamic quest, integrated into the provocation system
#  "None"
#  ),
 ("meet_spy_in_enemy_town", "Meet Spy in {s13}", qf_random_quest,
  "{!}None"
  ),
 ("capture_prisoners", "Bring {reg1} {s3} Prisoners", qf_random_quest,
  "{s9} wanted you to bring him {reg1} {s3} as prisoners."
  ),

## ("hunt_down_raiders", "Hunt Down Raiders",qf_random_quest,
##  "{s1} asked you to hunt down and punish the raiders that attacked a village near {s3} before they reach the safety of their base at {s4}."
##  ),

##################
# Enemy Kingdom Lord quests
##################
# Note : This is defined as the first enemy lord quest in module_constants.py:
 ("lend_surgeon", "Lend Your Surgeon {s3} to {s1}", qf_random_quest,
  "Lend your experienced surgeon {s3} to {s1}."
  ),

##################
# Kingdom Army quests
##################
# Note : This is defined as lord quests end in module_constants.py:
 ("follow_army", "Follow {s9}'s Army", qf_random_quest,
  "{!}None"
  ),
 ("report_to_army", "Report to {s13}, the Marshal", qf_random_quest,
  "{!}None"
  ),
# Note : This is defined as the first army quest in module_constants.py:
# maybe disable these army quests, except as volunteer quests that add to the capacity of the army
 ("deliver_cattle_to_army", "Deliver {reg3} Head of Cattle to {s13}", qf_random_quest,
  "{!}None"
  ),
 ("join_siege_with_army", "Join the Siege of {s14}", qf_random_quest,
  "{!}None"
  ),
 ("screen_army", "Screen the Advance of {s13}'s Army", qf_random_quest,
  "{!}None"
  ),
 ("scout_waypoints", "Scout {s13}, {s14} and {s15}", qf_random_quest,
  "{!}None"
  ),


##################
# Kingdom Lady quests
##################
# Note : This is defined as the first kingdom lady quest in module_constants.py:
#Rescue lord by replace will become a 
 ("rescue_lord_by_replace", "Rescue {s13} from {s14}", qf_random_quest,
  "{!}None"
  ),
 ("deliver_message_to_prisoner_lord", "Deliver Message to {s13} at {s14}", qf_random_quest,
  "{!}None"
  ),

#Courtship quests
  ("duel_for_lady", "Challenge {s13} to a Trial of Arms", qf_random_quest,
  "{!}None"
  ),

  ("duel_courtship_rival", "Challenge {s13} to a Trial of Arms (optional)", qf_random_quest,
  "{!}None"
  ),

#Other duel quests
  ("duel_avenge_insult", "Challenge {s13} to a Trial of Arms", qf_random_quest,
  "{!}None"
  ),
  
  
  
##################
# Mayor quests
##################
#VC Note : This is defined as the first mayor quest in module_constants.py:  
 ("move_cattle_herd", "Move Cattle Herd to {s13}", qf_random_quest,				#Note: This was defined as the first mayor quest in module_constants.py
  "The mayor of {s10} asked you to move a cattle herd to {s13}."
  ),
 ("escort_merchant_caravan", "Escort Merchant Caravan to {s8}", qf_random_quest, #make this a non-random quest?
  "Escort the merchant caravan to the town of {s8}."
  ),
 ("deliver_wine", "Deliver {reg5} Units of {s6} to {s4}", qf_random_quest,
  "{s9} of {s3} asked you to deliver {reg5} units of {s6} to the tavern in {s4} in 7 days."
  ),
 ("troublesome_bandits", "Hunt Down Troublesome Bandits", qf_random_quest,
  "{s9} of {s4} asked you to hunt down the troublesome bandits in the vicinity of the town."
  ),
  
 ("kidnapped_girl", "Ransom Girl from Bandits", qf_random_quest,
  "The mayor of {s4} gave you {reg12} peningas to pay the ransom of a girl kidnapped by bandits.\
 You are to meet the bandits near {s3} and pay them the ransom fee.\
 After that, you are to bring the girl back to {s4}."
  ),
  
 ("persuade_lords_to_make_peace", "Make Sure Two Lords Do Not Object to Peace", qf_random_quest, #possibly deprecate., or change effects
  "The mayor of {s4} promised you {reg12} peningas if you can make sure that\
 {s12} and {s13} no longer pose a threat to a peace settlement between {s15} and {s14}.\
 In order to do that, you must either convince them or take them captive until a peace agreement is made."
  ),
  
 ("deal_with_looters", "Deal with Looters", qf_random_quest,
  "The mayor of {s4} has asked you to deal with several bands of looters around {s4}, and bring back any goods you recover."
  ),
 ("deal_with_night_bandits", "Deal with Night Bandits", qf_random_quest,
  "{!}TODO: The mayor of {s14} has asked you to deal with night bandits at {s14}."
  ),

############
# Village Elder quests
############
# Note : This is defined as the first village elder quest in module_constants.py:
 ("deliver_grain", "Bring wheat to {s3}", qf_random_quest,
  "The local leader of the village of {s3} asked you to bring them {reg5} sacks of wheat."
  ), 
 ("deliver_cattle", "Deliver {reg5} Head of Cattle to {s3}", qf_random_quest,	#This was a elder quest
  "The local leader of the village of {s3} asked you to bring {reg5} head of cattle."
  ), 
 ("train_peasants_against_bandits", "Train the Peasants of {s13} Against Bandits.", qf_random_quest,
  "{!}None"
  ), 
# Deliver horses, Deliver food, Escort_Caravan, Hunt bandits, Ransom Merchant.
## ("capture_nobleman", "Capture Nobleman",qf_random_quest,
##  "{s1} wanted you to capture an enemy nobleman on his way from {s3} to {s4}. He said the nobleman would leave {s3} in {reg1} days."
##  ),

# Bandit quests: Capture rich merchant, capture banker, kill manhunters?..

# Note : This is defined as the last village elder quest in module_constants.py:
 ("eliminate_bandits_infesting_village", "Save the Village of {s7} from Marauding Bandits", qf_random_quest,
  "A villager from {s7} begged you to save their village from the bandits that took refuge there."
  ),


 # Tutorial quest
## ("destroy_dummies", "Destroy Dummies", qf_show_progression,
##  "Trainer ordered you to destroy 10 dummies in the training camp."
##     ),

  #Courtship and marriage quests begin here
  ("visit_lady", "Visit Lady", qf_random_quest,
  "{!}None"
  ),
  ("formal_marriage_proposal", "Formal Marriage Proposal", qf_random_quest,
  "{!}None"
  ),  #Make a formal proposal to a bride's father or brother
  ("obtain_liege_blessing", "Formal Marriage Proposal", qf_random_quest,
  "{!}None"
  ),  #The equivalent of the above -- ask permission of a groom's liege. Is currently not used
  ("wed_betrothed", "Wed Your Betrothed", qf_random_quest,
  "{!}None"
  ),  #in this case, the giver troop is the father or guardian of the bride, object troop is the bride
  ("wed_betrothed_female", "Wed Your Betrothed", qf_random_quest,
  "{!}None"
  ),  #in this case, the giver troop is the spouse

  
 # Join Kingdom quest
  ("join_faction", "Give Oath of Homage to {s1}", qf_random_quest,
  "Find {s1} and give him your oath of homage."
  ),

 # Rebel against Kingdom quest
 ("rebel_against_kingdom", "Help {s13} Claim the Throne of {s14}", qf_random_quest,
  "{!}None"
  ),

  #Political/Realm quests begin here
 ("consult_with_minister", "Consult With Minister", qf_random_quest, "Consult your minister, {s11}, currently at {s12}."),
 
 ("organize_feast",        "Organize Feast", qf_random_quest,        "Bring goods for a feast to your spouse {s11}, currently at {s12}."),
 ("resolve_dispute",       "Resolve Dispute", qf_random_quest,       "Resolve the dispute between {s11} and {s12}."),
 ("offer_gift",            "Procure Gift", qf_random_quest,          "Give {s10} a gift to provide to {reg4?her:his} {s11}, {s12}."),
 ("denounce_lord",         "Denounce Lord", qf_random_quest,         "Denounce {s11} in public."),
 ("intrigue_against_lord", "Intrigue against Lord", qf_random_quest, "Criticize {s11} in private."),
 
 
  #Dynamic quests begin here
  #These quests are determined dynamically by external conditions -- bandits who have carried out a raid, an impending war, etc...
 ("track_down_bandits", "Track Down Bandits", qf_random_quest,
  "{s9} of {s4} asked you to track down {s6}, who attacked travellers on the roads near town."
  ), #this is a fairly simple quest for the early game to make the town mayor's description of the economy a little more relevant, and also to give the player a reason to talk to other neutral parties on the map
   
 ("track_down_provocateurs", "Track Down Provocateurs", qf_random_quest,
  "{s9} of {s4} asked you to track down a group of thugs, hired to create a border incident between {s5} and {s6}."
  ), 
 ("retaliate_for_border_incident", "Retaliate for a Border Incident", qf_random_quest,
  "{s9} of {s4} asked you to defeat {s5} of the {s7} in battle, defusing tension in the {s8} to go to war."
  ), #perhaps replaces persuade_lords_to_make_peace
  
 ("raid_caravan_to_start_war", "Attack a Neutral Caravan to Provoke War", qf_random_quest,
  "{!}placeholder",
  ), 

  ("cause_provocation", "Give a Kingdom Provocation to Attack Another", qf_random_quest,
  "{!}placeholder",
  ), #replaces raid_caravan_to_start_war
  
 ("rescue_prisoner", "Rescue or Ransom a Prisoner", qf_random_quest,
  "{!}placeholder"
  ), #possibly replaces rescue lord

 ("destroy_bandit_lair", "Destroy Bandit Lair", qf_random_quest,
  "{s9} of {s4} asked you to discover the {s6} in the area and destroy it."
  ), 
  ##########mainquest quest  
#mainquest chief #marcado en script "abort_quest"
  ("kennemer_jarl", "The Revenge: Talk to the Jarl of Kennemer", 0, #chief cambia para quest de kennemer
  "{!}placeholder."
  ), 
  
  ("kennemer_jarl_missions", "The Revenge: Working for a Jarl", 0, #chief cambia para quest de kennemer
  "{!}placeholder."
  ), 

  ("kennemer_mission_1", "Jarl Mission: Judgment in the Monastery", 0, #chief cambia para quest de kennemer
  "{!}placeholder."
  ), 

  ("kennemer_mission_2", "Jarl Mission: Thiaderd Must Die", 0, #chief cambia para quest de kennemer
  "{!}placeholder."
  ), 

  ("kennemer_mission_3", "Jarl Mission: To Kill a King", 0, #chief cambia para quest de kennemer
  "{!}placeholder."
  ), 
  ("reginhard_donations", "Reginhard's Petition: A Donation for War Victims", 0, #chief cambia para quest de kennemer
  "{!}placeholder."
  ), 
  ("recruit_an_army", "Jarl Mission: Recruiting Warriors", 0, #chief cambia para quest de kennemer
  "{!}placeholder."
  ), 
 # Doccinga Coastal assault
  ("doccinga_assault", "Viking Attack: Save Doccinga from Sven's Assault", qf_random_quest,
  "{!}placeholder."
  ),

  ("doccinga_interrogation", "Viking Attack: Interrogating a Viking", qf_random_quest,
  "{!}placeholder."
  ),
  ("getting_ship", "Viking Attack: A Boat and a Girl", qf_random_quest,
  "{!}placeholder."
  ),
#notas chief para quest, recordatorio player
  ("notes_companions", "Notes on Your Companions", 0,
  "{!}placeholder."
  ), 
  ("notes_global", "Your Book Notes", 0,
  "{!}placeholder."
  ), 
  ("notes_frisa", "Notes on Friese", 0,
  "{!}placeholder."
  ), 
  ("notes_danmork", "Notes on Danmark", 0,
  "{!}placeholder."
  ), 
  ("notes_englaland", "Notes on Englaland", 0,
  "{!}placeholder."
  ), 
#danmork
  ("sven_lair", "The Revenge: The Wolf's Den", 0, #chief cambia para quest de kennemer
  "{!}placeholder."
  ), 
  ("danmork_protection", "The Revenge: Under the Wing of a King", 0, #chief cambia para quest de kennemer
  "{!}placeholder."
  ), 
  ("revenge_sigurd", "The Revenge: Ask Sigurd 'Snake in the Eye'", 0, #chief cambia para quest de kennemer
  "{!}placeholder."
  ), 
  ("collect_smen", "Sigurd Mission: Recruiting an Army for Sigurd", 0, #chief cambia para quest de kennemer
  "{!}placeholder."
  ), 
  ("bodo_letter", "The Revenge: A Most Important Letter", 0, #chief cambia para quest de kennemer
  "{!}placeholder."
  ), 
  ("the_holmgang", "The Holmgang: Killing a Hirdman", 0, #chief cambia para quest de kennemer
  "{!}placeholder."
  ), 
  ("the_fleet", "The Revenge: Invading Englaland", 0, #chief cambia para quest de kennemer
  "{!}placeholder."
  ), 
#Englaland
  ("sven_traitor", "The Revenge: Sven the Traitor", 0, #chief cambia para quest de kennemer
  "{!}placeholder."
  ), 
  ("wessex_foragers", "The Siege: Saxon Foragers", 0, #chief cambia para quest de kennemer
  "{!}placeholder."
  ), 
  ("the_messengersn", "The Siege: The Messenger", 0, #chief cambia para quest de kennemer
  "{!}placeholder."
  ), 
  ("the_alliance", "The Revenge: The Alliance", 0, #chief cambia para quest de kennemer
  "{!}placeholder."
  ), 
  ("welsh_and_pictish", "The Conqueror: Serving a Cause", 0, #chief cambia para quest de kennemer
  "{!}placeholder."
  ), 
##  ("meeting_sven", "The Revenge: The Meeting", 0, #chief cambia para quest de kennemer
##  "{!}placeholder."
##  ), 
  ("cathach_colum", "Being a Viking: 'The Cathach of Colum Cille'", 0, #chief cambia para quest de kennemer
  "{!}placeholder."
  ), 
  ("entregando_pieles", "Being a Viking: Trading in Furs", 0, #chief cambia para quest de kennemer
  "{!}placeholder."
  ), 
  ("revenge_exchange", "The Revenge: The Farm", 0, #chief cambia para quest de kennemer
  "{!}placeholder."
  ), 
  ("ulf_testigo", "The Revenge: Wooing Farmers and Jarls", 0, #chief cambia para quest de kennemer
  "{!}placeholder."
  ), 
  ("the_thing", "The Revenge: The Assembly", 0, #chief cambia para quest de kennemer
  "{!}placeholder."
  ), 
  ("douar_an_enez", "The Revenge: Douar-an-Enez", 0, #chief cambia para quest de kennemer
  "{!}placeholder."
  ), 
  ("aescesdun", "The Battle: Aescesdun", 0, #chief cambia para quest de kennemer
  "{!}placeholder."
  ), 
  ("svenbn_final", "The Revenge: Sven Bull Neck", 0, #chief cambia para quest de kennemer
  "{!}placeholder."
  ), 
#mainquest chief acaba
##extra VC quest
   ("old_roman", "Hadrian's Wall: Saving the Starving", 0, #chief cambia para quest de kennemer
  "{!}placeholder."
  ), 
  


# pseudo quests begin (Phaiak)
  ("vc_menu", "Viking Conquest menu system.", 0, "{!}placeholder."),
  ("vc_wounds", "Viking Conquest wound system.", 0, "{!}placeholder."),  
  ("sea_battle_spawn", "a spawning system.", 0, "{!}placeholder."),  
  ("team_0_ships", "a spawning system.", 0, "{!}placeholder."),  
  ("team_1_ships", "a spawning system.", 0, "{!}placeholder."),  
# pseudo quests end
 ("blank_quest_2", "Escort Bishop to {s14}.", qf_random_quest,
  "{s11} asked you to escort the Bishop from {s22} to {s14}."
  ),
  
 ("blank_quest_3", "Raid Monastery at {s14}", qf_random_quest,
  "{s11} asked you to raid Monastery at {s14}, near {s34}, and bring him {reg33} peningas."
  ),

 ("blank_quest_4", "Find and destroy a group of masterless men", qf_random_quest,
  "{s8} asked you to track down a group of masterless men who looted his village, {s9}."
  ),

 ("blank_quest_5", "{!}blank_quest", qf_random_quest,
  "{!}placeholder"
  ),

 ("blank_quest_6","Capture and bring {reg5} women to {s3}", qf_random_quest,
  "The local leader of the village of {s3} asked you to bring {reg5} women to the village (as prisoners)."),

 ("blank_quest_7", "Return Runaway Slave to {s3}", qf_random_quest,
  "The leader of the village of {s3} asked you to bring a runaway slave back to the village."
  ),

 ("blank_quest_8", "{!}blank_quest", qf_random_quest,
  "{!}placeholder"
  ),

 ("blank_quest_9", "Bring {reg33} Horns of Mead to {s3}", qf_random_quest,
  "The priest at {s3} asked you to bring him {reg33} drinking horns of mead."
  ),

 ("blank_quest_10", "Recover a {s13} Stolen from {s9} of {s3}", qf_random_quest,
  "The {s9} of {s3} asked you to recover a {s13} stolen from him.^^Look Into:^{s10}"
  ),

 ("blank_quest_11", "Bring {reg33} Loads of {s33} to {s3}", qf_random_quest,
  "The {s9} of {s3} asked you to bring {reg33} loads of {s33} to him."
  ),

 ("blank_quest_12", "Bring {reg33} Pallets of Timber to {s3}", qf_random_quest,
  "The abbot at {s3} asked you to bring him {reg33} pallets of timber."
  ),

 ("blank_quest_13", "A Blast from the Past", 0, "{s11} asked you to deal with her 'ghost' ex-lover who is believed to be in {s33}."
  ),

 ("blank_quest_14",  "Reveal Assassination Plot", 0, "Someone attempted to murder you. You can try to find out who wanted you dead by meeting the killers' contact in {s3}." 
   ),

 ("blank_quest_15",  "Reveal Assassination Plot",0, "The contact has given away the lord who ordered the assassination - it is {s9}. It's time to confront the lord directly. "
  ),

 ("blank_quest_16", "Bring {reg25} {reg1?Pieces:Piece} of {s17} to {s11}", qf_random_quest,
  "{s11} asked you to bring her {reg25} {reg1?pieces:piece} of {s17}."),

 ("blank_quest_17", "Bring Foodstuffs to {s11}", qf_random_quest,
  "{s11} asked you to bring her two pieces of cheese and {reg25} {reg1?bottles:bottle} of wine."
  ),

 ("blank_quest_18","Deliver Message to {s3}", qf_random_quest,  "{s11} asked you to take a message to her lover {s3}."
),
### add-ons high kings quests
 ("blank_quest_19", "Become Norse Konungr Over All Scandinavia", 0,
  "{!}placeholder"
  ),

 ("blank_quest_20", "Become Vrenhin Lloegr Over All Britons", qf_random_quest,
  "{!}placeholder"
  ),

 ("blank_quest_21", "Become Ard Ruire Over All Eriu", qf_random_quest,
  "{!}placeholder"
  ),

 ("blank_quest_22", "Become Brytenwalda Over All Englaland", qf_random_quest,
  "{!}placeholder"
  ),
###addons short story
 ("blank_quest_23", "The Last Tuatha De Danann", 0,
  "{!}placeholder"
  ),

 ("blank_quest_24", "The Snake", 0,
  "{!}placeholder"
  ),

 ("blank_quest_25", "Flaithbertach's Grandchildren", 0,
  "{!}placeholder"
  ),

 ("blank_quest_26", "Mael Bresail", 0,
  "{!}placeholder"
  ),

 ("blank_quest_27", "Notes on Eriu", 0,
  "{!}placeholder"
  ),

 ("collect_men", "The Revenge: Visit Doccinga", 0,
  "{!}placeholder." #chief cambia a doccinga
  ), 
 ("learn_where_merchant_brother_is", "Deliver {reg3} Head of Cattle to {s13}", qf_random_quest,
  "{!}None"
  ), #used for cattle quest, savegame compatibility
##  ("learn_where_merchant_brother_is", "The Revenge: Talk to the Jarl of Kennemer.", 0, #chief cambia para quest de kennemer
##  "{!}placeholder."
##  ), 

  ("save_relative_of_merchant", "Attack the Bandit Lair", 0,
  "{!}placeholder."
  ),   
  ("save_town_from_bandits", "Save Town from Bandits", 0,
  "{!}placeholder."
  ),   

  
 ("quests_end", "Quests End", 0, "{!}."),
]
