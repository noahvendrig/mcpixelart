import os

f = open("list.txt", "r")
lines = f.readlines()
res=[]

for line in lines:
    line = line.replace("\n","")
    res.append(line)

# print(res)
name_list = []
directory = r"D:\py\mc imgs"+"\\"
for file in os.listdir(directory):
    name = file
    name = name[:-4]
    name_list.append(name)

ls = ['acacia_log_top', 'acacia_trapdoor', 'ancient_debris_side', 'ancient_debris_top', 'andesite', 'barrel_bottom', 'barrel_side', 'barrel_top', 'basalt_side', 'basalt_top', 'bee_nest_bottom', 'bee_nest_front', 'bee_nest_side', 'bee_nest_top', 'beehive_front', 'beehive_side', 'birch_log_top', 'birch_trapdoor', 'black_concrete_powder', 'black_shulker_box', 'black_terracotta', 'black_wool', 'blackstone', 'blackstone_top', 'blast_furnace_side', 'blast_furnace_top', 'blue_concrete_powder', 'blue_ice', 'blue_shulker_box', 'blue_terracotta', 'blue_wool', 'bone_block_side', 'bone_block_top', 'bookshelf', 'bricks', 'brown_concrete_powder', 'brown_mushroom_block', 'brown_shulker_box', 'brown_terracotta', 'brown_wool', 'cake_bottom', 'cartography_table_side1', 'cartography_table_side2', 'cartography_table_side3', 'cartography_table_top', 'chiseled_nether_bricks', 'chiseled_polished_blackstone', 'chiseled_quartz_block_top', 'chiseled_sandstone', 'chiseled_stone_bricks', 'clay', 'coal_block', 'coal_ore', 'coarse_dirt', 'cobblestone', 'composter_bottom', 'composter_side', 'composter_top', 'composter_top', 'composter_top', 'cracked_nether_bricks', 'cracked_polished_blackstone_bricks', 'crafting_table_front', 'crafting_table_side', 'crafting_table_top', 'crimson_planks', 'crimson_stem_top', 'crying_obsidian', 'cut_sandstone', 'cyan_concrete_powder', 'cyan_shulker_box', 'cyan_terracotta', 'cyan_wool', 'dark_oak_log_top', 'dark_oak_trapdoor', 'daylight_detector_inverted_top', 'daylight_detector_side', 'daylight_detector_top', 'dead_bubble_coral_block', 'dead_horn_coral_block', 'diamond_block', 'diamond_ore', 'diorite', 'dirt', 'dispenser_front_vertical', 'dried_kelp_side', 'dried_kelp_top', 'dropper_front_vertical', 'emerald_block', 'emerald_ore', 'enchanting_table_bottom', 'enchanting_table_top', 'end_stone', 'furnace_front', 'furnace_side', 'furnace_top', 'gilded_blackstone', 'glowstone', 'gold_block', 'gold_ore', 'granite', 'grass_path_top', 'gravel', 'gray_concrete_powder', 'gray_shulker_box', 'gray_terracotta', 'gray_wool', 'green_concrete_powder', 'green_shulker_box', 'green_terracotta', 'green_wool', 'hay_block_side', 'hay_block_top', 'honey_block_side', 'honeycomb_block', 'ice', 'iron_block', 'iron_ore', 'iron_trapdoor', 'jukebox_side', 'jukebox_top', 'jungle_log_top', 'jungle_trapdoor', 'lapis_block', 'lapis_ore', 'lectern_base', 'light_blue_concrete_powder', 'light_blue_shulker_box', 'light_blue_terracotta', 'light_blue_wool', 'light_gray_concrete_powder', 'light_gray_shulker_box', 'light_gray_terracotta', 'lime_concrete', 'lime_glazed_terracotta', 'lime_shulker_box', 'lime_terracotta', 'lime_wool', 'lodestone_side', 'lodestone_top', 'loom_bottom', 'loom_front', 'loom_side', 'loom_top', 'magenta_concrete_powder', 'magenta_shulker_box', 'magenta_terracotta', 'magenta_wool', 'magma', 'melon_side', 'melon_top', 'mushroom_block_inside', 'mycelium_side', 'mycelium_top', 'nether_gold_ore', 'nether_wart_block', 'netherite_block', 'netherrack', 'oak_log', 'oak_planks', 'observer_back', 'observer_front', 'observer_side', 'observer_top', 'obsidian', 'orange_concrete_powder', 'orange_shulker_box', 'orange_terracotta', 'orange_wool', 'pink_concrete', 'pink_glazed_terracotta', 'pink_shulker_box', 'pink_terracotta', 'pink_wool', 'piston_bottom', 'piston_side', 'piston_top_sticky', 'polished_andesite', 'polished_basalt_side', 'polished_basalt_top', 'polished_blackstone', 'polished_blackstone_bricks', 'polished_granite', 'prismarine_bricks', 'pumpkin_side', 'pumpkin_top', 'purple_concrete_powder', 'purple_shulker_box', 'purple_terracotta', 'purple_wool', 'purpur_block', 'purpur_pillar', 'purpur_pillar_top', 'quartz_block_bottom', 'quartz_block_side', 'quartz_block_top', 'quartz_bricks', 'quartz_pillar_top', 'red_concrete_powder', 'red_mushroom_block', 'red_sand', 'red_sandstone_bottom', 'red_sandstone_top', 'red_shulker_box', 'red_terracotta', 'red_wool', 'redstone_block', 'redstone_lamp_on', 'redstone_ore', 'respawn_anchor_bottom', 'respawn_anchor_top_off', 'sand', 'sandstone_bottom', 'sandstone_top', 'sea_lantern', 'shroomlight', 'slime_block', 'smithing_table_bottom', 'smithing_table_front', 'smithing_table_side', 'smithing_table_top', 'smoker_bottom', 'smoker_side', 'smoker_top', 'smooth_stone_slab_side', 'snow', 'soul_sand', 'soul_soil', 'sponge', 'spruce_log_top', 'spruce_trapdoor', 'stone', 'stone_bricks', 'stonecutter_bottom', 'stripped_acacia_log', 'stripped_acacia_log_top', 'stripped_birch_log', 'stripped_birch_log_top', 'stripped_crimson_stem_top', 'stripped_dark_oak_log', 'stripped_dark_oak_log_top', 'stripped_jungle_log', 'stripped_jungle_log_top', 'stripped_oak_log', 'stripped_oak_log_top', 'stripped_spruce_log', 'stripped_spruce_log_top', 'stripped_warped_stem_top', 'target_side', 'target_top', 'tnt_bottom', 'tnt_side', 'tnt_top', 'warped_nylium', 'warped_stem', 'warped_trapdoor', 'warped_wart_block', 'white_concrete', 'white_glazed_terracotta', 'white_shulker_box', 'white_terracotta', 'white_wool', 'yellow_concrete_powder', 'yellow_shulker_box', 'yellow_terracotta', 'yellow_wool']

for i in res:
    if i not in name_list:
        print(i)


print("e")


# for line in lines:
#     path = line+".png"
#     print(path)
#     # print(directory+line+".png")
#     if os.path.isfile(directory+line):
#         print("File exist")
#     else:
#         pass
#         # print("File not exist")
#         # print(directory+line)
            

# os.remove("demofile.txt")