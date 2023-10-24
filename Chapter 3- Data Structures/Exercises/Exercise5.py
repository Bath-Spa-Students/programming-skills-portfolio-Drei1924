invitation_list = ["Kristel Mae", "Mark Jimsell", "Jao Deleon"]

for guest in invitation_list:
     print(f"Hello {guest},\n\tYou are Invited to a dinner. It would be nice to have you.\nSincerely, Jyosef Drei Lozanes")
     print("\n")

unavailable_guest  = "Mark Jimsell"
print(f"\nUnfortunately, {unavailable_guest} Can't Make it to dinner.\n")

new_guest = "Kayle Abenojar"
invitation_list[invitation_list.index(unavailable_guest)] = new_guest

print("Updated Invitations:")

for guest in invitation_list:
     print(f"Hello {guest},\n\tYou are Invited to a dinner. It would be nice to have you.\nSincerely, Jyosef Drei Lozanes")
     print("\n")