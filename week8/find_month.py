

month = input("Give your month: ").lower()
months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "novenber", "december"]


def search(month):
    if (month in months):
        print(f"We found {month} in the months list. Search successful!")
    else:
        print(f"We could not find {month} in the months list.")

search(month)