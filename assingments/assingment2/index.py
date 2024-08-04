# Q1
Message:str="this is our python code in generative Ai";
print(Message);
# Q2
Work:str="this is leptop";
print(Work);
# change value of variable
Work:str="this is my phone";
print(Work)
# Q3 
Personal_Name:str="Ahmar Ali ";
messege:str=(f"\"Hello {Personal_Name} , would you like to learn some python today?\"");
print(messege);
# Q4
Name:str="My name is Ahmar Ali";
print("Upper Case = ", Name.upper() );
print("Lower case = ", Name.lower());
print("Titel Case = " , Name.title());
# Q5
Famous_Quote:str="Once Allama iqbal said  , \"I do not believe in taking the right decision, I take a decision and make it right\"";
print(Famous_Quote);
# Q6
Person:str="Hazar Ali(R.S)";
messages:str=(f"\" Once {Person} said , This entire world is not worth a single tear.\"")
print(messages);
# Q7
# Define a variable to represent a person's name with whitespace characters
name:str = "\t\n John Doe \n\t"

# Print the name with whitespace
print("Original name with whitespace:")
print(repr(name))

# Print the name using lstrip() to remove leading whitespace
print("\nName with leading whitespace removed using lstrip():")
print(repr(name.lstrip()))

# Print the name using rstrip() to remove trailing whitespace
print("\nName with trailing whitespace removed using rstrip():")
print(repr(name.rstrip()))

# Print the name using strip() to remove both leading and trailing whitespace
print("\nName with both leading and trailing whitespace removed using strip():")
print(repr(name.strip()))
# Q8
x:int=5;
y:int=10;
z:int=15;
print(f"{x}+{y}+{z}={x+y+z}")
# Q9
a:int=5;
b:int=10;
print("Before Swap");
print(f"a = {a}");
print(f"b = {b}");
a,b=b,a
print("\nAfter Swap");
print(f"a = {a}");
print(f"b = {b}");
# Q10
Favourite_color:str="Black";
print(Favourite_color);
New_Favourite_color:str=Favourite_color;
print(New_Favourite_color);
# Q11
pet_Name:str="Buddy";
pet_Name:str="Dog";
print(pet_Name);
# Q12
weather:str="SunShine";
print(weather);
#print(sunshine);# NameError: name 'sunshine' is not defined 
# Q13