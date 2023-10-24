new_invitation_list = ["Kristel Mae", "Kayle Abenojar", "Jao Deleon"]


for person in new_invitation_list:
    print(f"Hello {person},\n\tYou are Invited to a dinner. It would be nice to have you.\nSincerely, Jyosef Drei Lozanes")
    print("\n")

print ("\nUnfortunately, There is only 2 available dinner table, so i can only invite 2 people for dinner.")

while len (new_invitation_list) > 2:
    popped_guest = new_invitation_list.pop()
    print(f"\n My Apologies, {popped_guest}, \n\tI can't Invite you to a dinner.\n")

for remaining_guest in new_invitation_list:
    print(f"{remaining_guest}, you're still invited to dinner.\n")

del new_invitation_list[:]

print("Updated guest list:", new_invitation_list)