import pandas as pd
import json

df = pd.read_csv('zomato.csv',encoding='MacRoman')
country_dict = {
    1:	"India",
    14:	"Australia",
    30: "Brazil",
    37:	"Canada",
    94:	"Indonesia",
    148:	"New Zealand",
    162:	"Phillipines",
    166:	"Qatar",
    184:	"Singapore",
    189:	"South Africa",
    191:	"Sri Lanka",
    208:	"Turkey",
    214:	"UAE",
    215:	"United Kingdom",
    216:	"United States"
}

color_dict = {
    "Average": 'red',
    "Excellent": 'blue',
    "Good": 'green',
    "Not rated": 'white',
    "Poor": 'pink',
    "Very Good": 'yellow'
}

# res_india = df[df['Country Code'] == 1] 
# print('India: ', len(res_india))

# for c in country_dict:
#     res = df[df['Country Code'] == c] 
#     print(country_dict[c], ' : ', len(res))
    

rslt_df_g_4 = df[df['Aggregate rating'] >= 4] 
# print(len(rslt_df_g_4))
rslt_df_l_4 = df[df['Aggregate rating'] < 4] 
# print(len(rslt_df_l_4))

rslt_df_nhod = df[df['Has Online delivery'] == 'No'] 
# print(len(rslt_df_nhod))
rslt_df_hod = df[df['Has Online delivery'] == 'Yes'] 
# print(len(rslt_df_hod))

rslt_df_votes_g500 = df[df['Votes'] > 500] 
# print(len(rslt_df_votes_g500))

votes_list = []
for ind in rslt_df_votes_g500.index:
    lat = rslt_df_votes_g500['Latitude'][ind]
    long = rslt_df_votes_g500['Longitude'][ind]
    size = rslt_df_votes_g500['Votes'][ind]
    
    rating_text = rslt_df_votes_g500['Rating text'][ind]
    color = color_dict.get(rating_text)
    # votes_list.append(lat)
    # votes_list.append(long)
    # votes_list.append(0.002)

    votes_list.append({
        "lat": lat,
        "long": long,
        "size": float(size),
        "color": color
    })

hod_list = []
for ind in rslt_df_hod.index:
    lat = rslt_df_hod['Latitude'][ind]
    long = rslt_df_hod['Longitude'][ind]
    size = rslt_df_hod['Votes'][ind]
    rating_text = rslt_df_hod['Rating text'][ind]
    color = color_dict.get(rating_text)
    
    hod_list.append({
        "lat": lat,
        "long": long,
        "size": float(size),
        "color": color
    })

nhod_list = []
for ind in rslt_df_nhod.index:
    lat = rslt_df_nhod['Latitude'][ind]
    long = rslt_df_nhod['Longitude'][ind]
    size = rslt_df_nhod['Votes'][ind]
    rating_text = rslt_df_nhod['Rating text'][ind]
    color = color_dict.get(rating_text)
    
    # nhod_list.append(lat)
    # nhod_list.append(long)
    # nhod_list.append(0.002)
    nhod_list.append({
        "lat": lat,
        "long": long,
        "size": float(size),
        "color": color
    })

rating_g4_list = []
for ind in rslt_df_g_4.index:
    lat = rslt_df_g_4['Latitude'][ind]
    long = rslt_df_g_4['Longitude'][ind]
    size = rslt_df_g_4['Votes'][ind]
    rating_text = rslt_df_g_4['Rating text'][ind]
    color = color_dict.get(rating_text)
    
    # rating_g4_list.append(lat)
    # rating_g4_list.append(long)
    # rating_g4_list.append(0.002)
    rating_g4_list.append({
        "lat": lat,
        "long": long,
        "size": float(size),
        "color": color
    })

rating_l4_list = []
for ind in rslt_df_l_4.index:
    lat = rslt_df_l_4['Latitude'][ind]
    long = rslt_df_l_4['Longitude'][ind]
    size = rslt_df_l_4['Votes'][ind]
    rating_text = rslt_df_l_4['Rating text'][ind]
    color = color_dict.get(rating_text)
    
    # rating_l4_list.append(lat)
    # rating_l4_list.append(long)
    # rating_l4_list.append(0.002)
    rating_l4_list.append({
        "lat": lat,
        "long": long,
        "size": float(size),
        "color": color
    })

# print('votes list: ', votes_list)
# print('hod_list: ', hod_list)
# print('nhod_list: ', nhod_list)
# print('rating_g4_list: ', rating_g4_list)
# print('rating_l4_list: ', rating_l4_list)

# master_list = []
# master_list.append(['vote', votes_list])
# master_list.append(['hod', hod_list])
# master_list.append(['nhod', nhod_list])
# master_list.append(['g_rating', rating_g4_list])
# master_list.append(['l_rating', rating_l4_list])

# # list to json
# jsonString = json.dumps(master_list)
# # print(jsonString)

print('votes_list: ', votes_list)
votes_jsonString = json.dumps(votes_list)
# print(votes_jsonString)

with open("votes.json", "w") as outfile:
    json.dump(votes_jsonString, outfile)

hod_jsonString = json.dumps(hod_list)
# print(hod_jsonString)

with open("hod.json", "w") as outfile:
    json.dump(hod_jsonString, outfile)

nhod_jsonString = json.dumps(nhod_list)
# print(nhod_jsonString)

with open("nhod.json", "w") as outfile:
    json.dump(nhod_jsonString, outfile)

rating_g4_list_json = json.dumps(rating_g4_list)
# print(rating_g4_list_json)

with open("rating_g4.json", "w") as outfile:
    json.dump(rating_g4_list_json, outfile)

rating_l4_list_json = json.dumps(rating_l4_list)
# print(rating_l4_list_json)

with open("rating_l4.json", "w") as outfile:
    json.dump(rating_l4_list_json, outfile)

# country_set = set()
# for ind in rslt_df_votes_g500.index:
#     lat = rslt_df_votes_g500['Country Code'][ind]
#     country_set.add(lat)

# # print(country_set)
# # for val in country_set:
#     # print(country_dict.get(val))

# Get average rating(y) and votes(x) for excellent and poor rated restaurants
# excellent_df = df[df['Rating text'] == 'Excellent'] 
# poor_df = df[df['Rating text'] == 'Poor'] 

# excellent_df['Aggregate rating']
# excellent_df['Votes']

# excellent_datapoints = []
# for ind in excellent_df.index:
#     avr = excellent_df['Aggregate rating'][ind]
#     v = excellent_df['Votes'][ind]
#     excellent_datapoints.append({"x": v, "y": avr})
# # print(excellent_datapoints)
# # [{'x': 314, 'y': 4.8}, {'x': 591, 'y': 4.5}, {'x': 365, 'y': 4.9}, {'x': 229, 'y': 4.8}, {'x': 621, 'y': 4.9}, {'x': 532, 'y': 4.8}, {'x': 1070, 'y': 4.9}, {'x': 294, 'y': 4.8}, {'x': 211, 'y': 4.5}, {'x': 118, 'y': 4.5}, {'x': 535, 'y': 4.7}, {'x': 618, 'y': 4.5}, {'x': 30, 'y': 4.9}, {'x': 29, 'y': 4.8}, {'x': 24, 'y': 4.7}, {'x': 29, 'y': 4.5}, {'x': 19, 'y': 4.8}, {'x': 40, 'y': 4.9}, {'x': 21, 'y': 4.6}, {'x': 49, 'y': 4.9}, {'x': 21, 'y': 4.6}, {'x': 25, 'y': 4.6}, {'x': 44, 'y': 4.7}, {'x': 24, 'y': 4.6}, {'x': 49, 'y': 4.5}, {'x': 59, 'y': 4.8}, {'x': 30, 'y': 4.6}, {'x': 58, 'y': 4.6}, {'x': 1821, 'y': 4.5}, {'x': 849, 'y': 4.5}, {'x': 917, 'y': 4.6}, {'x': 717, 'y': 4.6}, {'x': 548, 'y': 4.9}, {'x': 631, 'y': 4.5}, {'x': 237, 'y': 4.6}, {'x': 879, 'y': 4.5}, {'x': 615, 'y': 4.6}, {'x': 879, 'y': 4.5}, {'x': 820, 'y': 4.9}, {'x': 488, 'y': 4.5}, {'x': 433, 'y': 4.7}, {'x': 489, 'y': 4.6}, {'x': 345, 'y': 4.5}, {'x': 249, 'y': 4.9}, {'x': 214, 'y': 4.6}, {'x': 166, 'y': 4.6}, {'x': 208, 'y': 4.5}, {'x': 474, 'y': 4.9}, {'x': 1025, 'y': 4.5}, {'x': 570, 'y': 4.9}, {'x': 674, 'y': 4.5}, {'x': 1109, 'y': 4.5}, {'x': 728, 'y': 4.6}, {'x': 860, 'y': 4.8}, {'x': 681, 'y': 4.9}, {'x': 357, 'y': 4.6}, {'x': 799, 'y': 4.5}, {'x': 478, 'y': 4.9}, {'x': 467, 'y': 4.6}, {'x': 302, 'y': 4.5}, {'x': 289, 'y': 4.5}, {'x': 1151, 'y': 4.5}, {'x': 1341, 'y': 4.7}, {'x': 1293, 'y': 4.6}, {'x': 2324, 'y': 4.6}, {'x': 1293, 'y': 4.6}, {'x': 1699, 'y': 4.8}, {'x': 1457, 'y': 4.9}, {'x': 1252, 'y': 4.9}, {'x': 1412, 'y': 4.7}, {'x': 2238, 'y': 4.9}, {'x': 792, 'y': 4.6}, {'x': 828, 'y': 4.5}, {'x': 816, 'y': 4.7}, {'x': 691, 'y': 4.5}, {'x': 764, 'y': 4.7}, {'x': 707, 'y': 4.7}, {'x': 487, 'y': 4.5}, {'x': 695, 'y': 4.5}, {'x': 723, 'y': 4.6}, {'x': 1343, 'y': 4.9}, {'x': 602, 'y': 4.9}, {'x': 1078, 'y': 4.6}, {'x': 906, 'y': 4.7}, {'x': 880, 'y': 4.6}, {'x': 1014, 'y': 4.5}, {'x': 796, 'y': 4.5}, {'x': 1321, 'y': 4.6}, {'x': 1629, 'y': 4.6}, {'x': 3157, 'y': 4.7}, {'x': 1424, 'y': 4.9}, {'x': 844, 'y': 4.5}, {'x': 1413, 'y': 4.9}, {'x': 1203, 'y': 4.5}, {'x': 3074, 'y': 4.7}, {'x': 1715, 'y': 4.8}, {'x': 1868, 'y': 4.5}, {'x': 207, 'y': 4.6}, {'x': 376, 'y': 4.6}, {'x': 81, 'y': 4.6}, {'x': 162, 'y': 4.5}, {'x': 216, 'y': 4.9}, {'x': 201, 'y': 4.7}, {'x': 586, 'y': 4.6}, {'x': 307, 'y': 4.5}, {'x': 909, 'y': 4.5}, {'x': 641, 'y': 4.9}, {'x': 322, 'y': 4.9}, {'x': 2510, 'y': 4.8}, {'x': 1388, 'y': 4.5}, {'x': 403, 'y': 4.5}, {'x': 1352, 'y': 4.9}, {'x': 2424, 'y': 4.7}, {'x': 459, 'y': 4.8}, {'x': 143, 'y': 4.5}, {'x': 77, 'y': 4.9}, {'x': 217, 'y': 4.5}, {'x': 166, 'y': 4.6}, {'x': 1138, 'y': 4.5}, {'x': 2369, 'y': 4.7}, {'x': 10934, 'y': 4.8}, {'x': 781, 'y': 4.6}, {'x': 276, 'y': 4.7}, {'x': 9667, 'y': 4.7}, {'x': 1288, 'y': 4.5}, {'x': 6907, 'y': 4.6}, {'x': 627, 'y': 4.6}, {'x': 5705, 'y': 4.5}, {'x': 427, 'y': 4.9}, {'x': 154, 'y': 4.6}, {'x': 145, 'y': 4.5}, {'x': 1450, 'y': 4.5}, {'x': 249, 'y': 4.5}, {'x': 1262, 'y': 4.8}, {'x': 1510, 'y': 4.6}, {'x': 1753, 'y': 4.6}, {'x': 1210, 'y': 4.5}, {'x': 859, 'y': 4.9}, {'x': 1267, 'y': 4.6}, {'x': 202, 'y': 4.6}, {'x': 380, 'y': 4.5}, {'x': 200, 'y': 4.9}, {'x': 50, 'y': 4.9}, {'x': 799, 'y': 4.5}, {'x': 280, 'y': 4.5}, {'x': 415, 'y': 4.8}, {'x': 302, 'y': 4.6}, {'x': 555, 'y': 4.6}, {'x': 840, 'y': 4.5}, {'x': 681, 'y': 4.7}, {'x': 563, 'y': 4.6}, {'x': 177, 'y': 4.6}, {'x': 407, 'y': 4.5}, {'x': 395, 'y': 4.6}, {'x': 223, 'y': 4.9}, {'x': 2093, 'y': 4.6}, {'x': 150, 'y': 4.6}, {'x': 69, 'y': 4.7}, {'x': 245, 'y': 4.8}, {'x': 1478, 'y': 4.8}, {'x': 76, 'y': 4.5}, {'x': 1262, 'y': 4.5}, {'x': 394, 'y': 4.6}, {'x': 126, 'y': 4.7}, {'x': 774, 'y': 4.9}, {'x': 200, 'y': 4.9}, {'x': 1932, 'y': 4.7}, {'x': 2553, 'y': 4.6}, {'x': 5434, 'y': 4.9}, {'x': 1023, 'y': 4.8}, {'x': 344, 'y': 4.7}, {'x': 1469, 'y': 4.7}, {'x': 420, 'y': 4.5}, {'x': 322, 'y': 4.9}, {'x': 289, 'y': 4.6}, {'x': 213, 'y': 4.5}, {'x': 945, 'y': 4.6}, {'x': 1424, 'y': 4.8}, {'x': 1219, 'y': 4.6}, {'x': 1753, 'y': 4.9}, {'x': 5966, 'y': 4.9}, {'x': 1057, 'y': 4.9}, {'x': 144, 'y': 4.5}, {'x': 567, 'y': 4.6}, {'x': 1069, 'y': 4.7}, {'x': 196, 'y': 4.6}, {'x': 2083, 'y': 4.7}, {'x': 2662, 'y': 4.5}, {'x': 413, 'y': 4.6}, {'x': 3244, 'y': 4.9}, {'x': 520, 'y': 4.5}, {'x': 226, 'y': 4.9}, {'x': 545, 'y': 4.5}, {'x': 52, 'y': 4.7}, {'x': 2620, 'y': 4.9}, {'x': 242, 'y': 4.7}, {'x': 1071, 'y': 4.6}, {'x': 1934, 'y': 4.9}, {'x': 162, 'y': 4.5}, {'x': 304, 'y': 4.6}, {'x': 67, 'y': 4.5}, {'x': 1033, 'y': 4.5}, {'x': 50, 'y': 4.5}, {'x': 408, 'y': 4.9}, {'x': 665, 'y': 4.5}, {'x': 524, 'y': 4.5}, {'x': 4986, 'y': 4.5}, {'x': 1569, 'y': 4.6}, {'x': 2213, 'y': 4.5}, {'x': 61, 'y': 4.6}, {'x': 295, 'y': 4.5}, {'x': 128, 'y': 4.6}, {'x': 83, 'y': 4.8}, {'x': 474, 'y': 4.7}, {'x': 778, 'y': 4.5}, {'x': 1691, 'y': 4.6}, {'x': 1563, 'y': 4.7}, {'x': 268, 'y': 4.7}, {'x': 112, 'y': 4.6}, {'x': 1136, 'y': 4.6}, {'x': 324, 'y': 4.5}, {'x': 147, 'y': 4.5}, {'x': 1099, 'y': 4.5}, {'x': 2510, 'y': 4.8}, {'x': 1439, 'y': 4.5}, {'x': 2847, 'y': 4.5}, {'x': 1408, 'y': 4.6}, {'x': 344, 'y': 4.5}, {'x': 321, 'y': 4.6}, {'x': 289, 'y': 4.6}, {'x': 345, 'y': 4.9}, {'x': 1662, 'y': 4.9}, {'x': 1476, 'y': 4.6}, {'x': 903, 'y': 4.6}, {'x': 873, 'y': 4.6}, {'x': 605, 'y': 4.9}, {'x': 1640, 'y': 4.9}, {'x': 2212, 'y': 4.9}, {'x': 617, 'y': 4.7}, {'x': 754, 'y': 4.9}, {'x': 598, 'y': 4.8}, {'x': 696, 'y': 4.6}, {'x': 281, 'y': 4.9}, {'x': 213, 'y': 4.5}, {'x': 166, 'y': 4.5}, {'x': 412, 'y': 4.7}, {'x': 413, 'y': 4.6}, {'x': 195, 'y': 4.5}, {'x': 152, 'y': 4.5}, {'x': 171, 'y': 4.6}, {'x': 100, 'y': 4.6}, {'x': 265, 'y': 4.5}, {'x': 329, 'y': 4.5}, {'x': 130, 'y': 4.6}, {'x': 163, 'y': 4.7}, {'x': 214, 'y': 4.7}, {'x': 571, 'y': 4.5}, {'x': 309, 'y': 4.9}, {'x': 706, 'y': 4.9}, {'x': 305, 'y': 4.5}, {'x': 1326, 'y': 4.7}, {'x': 436, 'y': 4.6}, {'x': 320, 'y': 4.7}, {'x': 148, 'y': 4.5}, {'x': 313, 'y': 4.5}, {'x': 161, 'y': 4.9}, {'x': 395, 'y': 4.8}, {'x': 367, 'y': 4.5}, {'x': 964, 'y': 4.7}, {'x': 418, 'y': 4.6}, {'x': 162, 'y': 4.9}, {'x': 110, 'y': 4.5}, {'x': 602, 'y': 4.5}, {'x': 348, 'y': 4.6}, {'x': 182, 'y': 4.9}, {'x': 114, 'y': 4.7}, {'x': 145, 'y': 4.5}, {'x': 356, 'y': 4.5}, {'x': 328, 'y': 4.5}, {'x': 319, 'y': 4.8}, {'x': 441, 'y': 4.9}, {'x': 194, 'y': 4.9}, {'x': 222, 'y': 4.5}, {'x': 373, 'y': 4.7}, {'x': 287, 'y': 4.5}, {'x': 97, 'y': 4.5}, {'x': 85, 'y': 4.9}, {'x': 542, 'y': 4.8}, {'x': 892, 'y': 4.6}, {'x': 146, 'y': 4.5}, {'x': 203, 'y': 4.9}, {'x': 124, 'y': 4.6}, {'x': 231, 'y': 4.5}, {'x': 95, 'y': 4.9}, {'x': 109, 'y': 4.6}, {'x': 104, 'y': 4.7}, {'x': 1311, 'y': 4.7}, {'x': 1042, 'y': 4.9}, {'x': 522, 'y': 4.9}, {'x': 761, 'y': 4.5}, {'x': 1305, 'y': 4.7}]

# poor_datapoints = []
# for ind in poor_df.index:
#     avr = poor_df['Aggregate rating'][ind]
#     v = poor_df['Votes'][ind]
#     poor_datapoints.append({"x": v, "y": avr})
# # print(poor_datapoints)
# # [{'x': 108, 'y': 2.2}, {'x': 17, 'y': 2.4}, {'x': 193, 'y': 2.4}, {'x': 154, 'y': 2.4}, {'x': 57, 'y': 2.1}, {'x': 25, 'y': 2.4}, {'x': 322, 'y': 1.8}, {'x': 2412, 'y': 2.4}, {'x': 125, 'y': 2.4}, {'x': 88, 'y': 2.4}, {'x': 73, 'y': 2.2}, {'x': 60, 'y': 2.0}, {'x': 34, 'y': 2.1}, {'x': 136, 'y': 2.2}, {'x': 43, 'y': 2.2}, {'x': 31, 'y': 2.3}, {'x': 35, 'y': 2.4}, {'x': 29, 'y': 2.3}, {'x': 90, 'y': 2.1}, {'x': 34, 'y': 2.3}, {'x': 93, 'y': 2.2}, {'x': 112, 'y': 2.4}, {'x': 32, 'y': 2.3}, {'x': 53, 'y': 2.4}, {'x': 23, 'y': 2.4}, {'x': 18, 'y': 2.4}, {'x': 26, 'y': 2.4}, {'x': 13, 'y': 2.4}, {'x': 92, 'y': 2.4}, {'x': 20, 'y': 2.4}, {'x': 66, 'y': 2.2}, {'x': 46, 'y': 2.2}, {'x': 52, 'y': 2.4}, {'x': 70, 'y': 2.3}, {'x': 26, 'y': 2.3}, {'x': 42, 'y': 2.4}, {'x': 38, 'y': 2.4}, {'x': 41, 'y': 2.2}, {'x': 49, 'y': 2.4}, {'x': 83, 'y': 2.4}, {'x': 142, 'y': 2.2}, {'x': 147, 'y': 2.2}, {'x': 77, 'y': 2.2}, {'x': 79, 'y': 2.2}, {'x': 31, 'y': 2.4}, {'x': 15, 'y': 2.4}, {'x': 55, 'y': 2.3}, {'x': 92, 'y': 2.4}, {'x': 71, 'y': 2.4}, {'x': 33, 'y': 2.4}, {'x': 164, 'y': 2.4}, {'x': 138, 'y': 2.1}, {'x': 41, 'y': 2.4}, {'x': 38, 'y': 2.3}, {'x': 32, 'y': 2.3}, {'x': 35, 'y': 2.4}, {'x': 147, 'y': 2.4}, {'x': 148, 'y': 2.4}, {'x': 30, 'y': 2.3}, {'x': 57, 'y': 2.3}, {'x': 118, 'y': 2.3}, {'x': 65, 'y': 2.4}, {'x': 101, 'y': 2.4}, {'x': 30, 'y': 2.4}, {'x': 23, 'y': 2.4}, {'x': 124, 'y': 2.4}, {'x': 113, 'y': 2.4}, {'x': 166, 'y': 2.4}, {'x': 19, 'y': 2.2}, {'x': 66, 'y': 1.9}, {'x': 126, 'y': 2.3}, {'x': 76, 'y': 2.4}, {'x': 44, 'y': 2.3}, {'x': 11, 'y': 2.4}, {'x': 9, 'y': 2.3}, {'x': 19, 'y': 2.3}, {'x': 32, 'y': 2.3}, {'x': 52, 'y': 2.4}, {'x': 20, 'y': 2.4}, {'x': 54, 'y': 2.1}, {'x': 39, 'y': 2.4}, {'x': 41, 'y': 2.4}, {'x': 121, 'y': 2.1}, {'x': 120, 'y': 2.2}, {'x': 52, 'y': 2.3}, {'x': 185, 'y': 2.3}, {'x': 18, 'y': 2.3}, {'x': 137, 'y': 2.4}, {'x': 84, 'y': 2.0}, {'x': 182, 'y': 2.2}, {'x': 49, 'y': 2.4}, {'x': 76, 'y': 2.4}, {'x': 36, 'y': 2.4}, {'x': 119, 'y': 2.2}, {'x': 96, 'y': 2.4}, {'x': 32, 'y': 2.3}, {'x': 184, 'y': 2.4}, {'x': 251, 'y': 2.2}, {'x': 16, 'y': 2.2}, {'x': 68, 'y': 2.1}, {'x': 43, 'y': 2.2}, {'x': 45, 'y': 2.1}, {'x': 31, 'y': 2.3}, {'x': 69, 'y': 2.4}, {'x': 37, 'y': 2.4}, {'x': 131, 'y': 2.3}, {'x': 62, 'y': 2.4}, {'x': 109, 'y': 2.4}, {'x': 30, 'y': 2.4}, {'x': 52, 'y': 2.4}, {'x': 126, 'y': 2.2}, {'x': 128, 'y': 2.3}, {'x': 62, 'y': 2.4}, {'x': 28, 'y': 2.4}, {'x': 54, 'y': 2.3}, {'x': 4, 'y': 2.4}, {'x': 39, 'y': 2.1}, {'x': 112, 'y': 2.1}, {'x': 8, 'y': 2.4}, {'x': 114, 'y': 2.3}, {'x': 41, 'y': 2.2}, {'x': 122, 'y': 2.2}, {'x': 82, 'y': 2.3}, {'x': 59, 'y': 2.3}, {'x': 26, 'y': 2.4}, {'x': 146, 'y': 1.9}, {'x': 42, 'y': 2.3}, {'x': 4, 'y': 2.4}, {'x': 45, 'y': 2.3}, {'x': 117, 'y': 2.4}, {'x': 79, 'y': 2.2}, {'x': 224, 'y': 2.4}, {'x': 43, 'y': 2.4}, {'x': 191, 'y': 2.0}, {'x': 26, 'y': 2.3}, {'x': 29, 'y': 2.4}, {'x': 64, 'y': 2.2}, {'x': 10, 'y': 2.4}, {'x': 152, 'y': 2.1}, {'x': 221, 'y': 2.4}, {'x': 8, 'y': 2.3}, {'x': 27, 'y': 2.3}, {'x': 84, 'y': 2.1}, {'x': 76, 'y': 2.4}, {'x': 94, 'y': 2.3}, {'x': 51, 'y': 2.4}, {'x': 63, 'y': 2.4}, {'x': 15, 'y': 2.3}, {'x': 81, 'y': 2.2}, {'x': 31, 'y': 2.3}, {'x': 74, 'y': 2.1}, {'x': 103, 'y': 2.4}, {'x': 62, 'y': 2.3}, {'x': 74, 'y': 2.0}, {'x': 70, 'y': 2.4}, {'x': 52, 'y': 2.4}, {'x': 5, 'y': 2.4}, {'x': 38, 'y': 2.3}, {'x': 7, 'y': 2.4}, {'x': 91, 'y': 2.3}, {'x': 161, 'y': 2.4}, {'x': 12, 'y': 2.3}, {'x': 115, 'y': 2.3}, {'x': 173, 'y': 2.3}, {'x': 56, 'y': 2.4}, {'x': 137, 'y': 2.4}, {'x': 21, 'y': 2.4}, {'x': 230, 'y': 2.3}, {'x': 56, 'y': 2.1}, {'x': 23, 'y': 2.3}, {'x': 49, 'y': 2.4}, {'x': 77, 'y': 2.4}, {'x': 88, 'y': 2.4}, {'x': 11, 'y': 2.4}, {'x': 22, 'y': 2.1}, {'x': 54, 'y': 2.4}, {'x': 116, 'y': 2.2}, {'x': 134, 'y': 2.2}, {'x': 98, 'y': 2.4}, {'x': 155, 'y': 2.3}, {'x': 24, 'y': 2.3}, {'x': 161, 'y': 2.0}, {'x': 230, 'y': 2.0}, {'x': 108, 'y': 2.0}, {'x': 402, 'y': 2.3}, {'x': 240, 'y': 2.4}]