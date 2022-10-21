# Count the values associated with key in a dictionary
student = [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': True, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]
print("Count the values associated with ID key: ",sum(d['id'] for d in student))
print("Count the values associated with Success key: ",sum(d['success'] for d in student))
