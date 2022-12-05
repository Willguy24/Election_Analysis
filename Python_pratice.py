#counties = ["Arapahoe","Denver","Jefferson"]

# if counties[1] == 'Denver':
#     print(counties[1])

# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not the list of counties.")

# for county in counties:
#     print(county)

# for i in range(len(counties)):
#     print(counties[i])




# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# # for county in counties_dict:
# #     print(county)

# ##for the key to print
# for county in counties_dict.keys():
#     print(county)

# ##for the value to print
# for voters in counties_dict.values():
#     print(voters)

# ##for both at once
# for county, voters in counties_dict.items():
#     print(county, voters)





#voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                {"county":"Denver", "registered_voters": 463353},
#               {"county":"Jefferson", "registered_voters": 432438}]

#Get each dictionary in a list of dictionaries
#for county_dict in voting_data:
#    print(county_dict)

# #Get the values from a list of dictionaries
# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)

# #Get just registered voters
# for county_dict in voting_data:
#      print(county_dict['registered_voters'])

# #Print just the name of each country in dictionary
# for county_dict in voting_data:
#     print(county_dict['county'])




#F string examples
#counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}

#without f string
#for county, voters in counties_dict.items():
#    print(county + " county has " + str(voters) + " registered voters.")

#Using f string
#for county, voters in counties_dict.items():
#    print(f"{county} county has {voters} registered voters.")




#Multiline F string w/ inputs
# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))

# message_to_candidate = (
#     f"You received {candidate_votes} number of votes. "
#     f"The total number of votes in the election was {total_votes}. "
#     f"You received {candidate_votes / total_votes * 100}% of the total votes.")

#print(message_to_candidate)

#using Floating Point Decimals
# message_to_candidate = (
#     f"You received {candidate_votes:,} number of votes. "
#     f"The total number of votes in the election was {total_votes:,}. "
#     f"You received {candidate_votes / total_votes * 100:.3f}% of the total votes.")

# print(message_to_candidate)