heroes = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

print(f"1.  {len(heroes)}")

heroes.append("black panther")
print(f"2.   {heroes}")

heroes.pop()
heroes.insert(3, 'black panther')
print(f"3.   {heroes}")

heroes[1:3] = ""
heroes.insert(1, 'doctor strange')
print(f"4.    {heroes}")

heroes.sort()
print(f"5.   {heroes}")