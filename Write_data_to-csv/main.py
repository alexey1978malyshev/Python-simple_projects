import csv


name_1 = "Anna"
name_2 = "Victor"

# with open("data.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(
#        # [name_1, name_2]
#        ("user_name", "user_address")
#     )

users_data = [
    ("user_name", "user_address"),
    ["user1", "address1"],
    ["user2", "address2"],
    ["user3", "address3"],
]

# for user in users_data:
#     with open("data.csv", "a") as file:
#         writer = csv.writer(file)
#         writer.writerow(
#             user
#         )


with open("data1.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerows(
            users_data
        )