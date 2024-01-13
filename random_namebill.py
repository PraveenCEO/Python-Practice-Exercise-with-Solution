import random
text = input("Enter the names:")
split_text=text.split()
print(split_text)
random_name=random.choice(split_text)
print(f"{random_name} will pay the bill")

Output:
Enter the names:jenny aakash payal
['jenny', 'aakash', 'payal']
payal will pay the bill
