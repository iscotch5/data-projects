#Establishing variables
golf_course_road_map='Golf courses I have worked at'
course_name = "Firethorn"
course_name_two = "Happy Hollow"
work_place = "FareHarbor"
#Practicing Concactenation
courses_worked_at= golf_course_road_map + ":" + " " + course_name
print(courses_worked_at)
print(course_name)
print(golf_course_road_map)
print(work_place)
#Using "F" Examples
best_course = (f"{course_name} is the number {1} course in Nebraska")
print(best_course)
#Working with Input functions
favorite_course = input("What is your favorite course? ")
print(favorite_course)
worst_course = input("What is your least favorite course? ")
print(worst_course)
if work_place == "FareHarbor":
    print(work_place)
elif work_place != "FareHarbor":
    print("No Job")