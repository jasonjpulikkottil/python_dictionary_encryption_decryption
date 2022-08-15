# Creating the dictionaries
courses_rooms = {
    'CS101':3004, 'CS102':4501, 'CS103':6755, 'NT110':1244, 'CM241':1411
}
courses_instructors = {
    'CS101':'Haynes',
    'CS102':'Alvarado',
    'CS103':'Rich',
    'NT110':'Burke',
    'CM241':'Lee'
}
courses_times = {
    'CS101':'8:00 a.m.',
    'CS102':'9:00 a.m.',
    'CS103':'10:00 a.m.',
    'NT110':'11:00 a.m.',
    'CM241':'1:00 p.m.'
}

# Obtaining a course number from the user
course = input('Enter a course number: ')

# Print response depending on whether the course number is valid
if course in courses_rooms:
    print()
    print('Room Number:   ', courses_rooms[course])
    print('Instructor:    ', courses_instructors[course])
    print('Meeting Time:  ', courses_times[course])
else:
    print('Invalid course number.')