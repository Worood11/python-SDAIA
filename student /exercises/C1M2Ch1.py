#Ex1
# if the number ends with .5, it will change it to the closest even number
print(round(42.5)) 
print(round(43.5)) #43.5 => 44.5

#Ex2
#here useing ++ in python it will act like it's 2+2 and the result is 4
print(2++2)
# python will throw an SyntaxError
#print(4 2)
#it will throw a SyntaxError
#print(round(42.5)

#Ex3
type(765) #int

type(2.718) #float

type('2 pi') #str

type(abs(-7)) #int

type(abs(-7.0)) #float

print(abs) # built-in function

print(int) #class

print(type) #class

#Ex4

#1
minutes = 42
seconds = 42
total_sec = (minutes * 60) + seconds
print(total_sec)

#2
kilometers = 10
km_per_mile = 1.61
total_km = kilometers / km_per_mile
print(total_km)

#3
seconds_per_mile = total_sec / total_km
print(seconds_per_mile)

#4
pace_in_seconds = 412.48
minutes = int(pace_in_seconds // 60)
seconds = pace_in_seconds % 60
print(f"{minutes} minutes and {seconds:.2f} seconds")

#5
total_miles = 6.21118
total_seconds = 2562
hours = total_seconds / 3600
speed = total_miles / hours
print(speed)