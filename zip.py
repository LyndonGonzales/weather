import zipfile
import os
import datetime

# Get current date and time
now = datetime.datetime.now()
cwd = os.getcwd()
folder_name = cwd.split('\\')[-1]

# Extract month, date, and year
M = now.month
D = now.day
Y = now.year
H = now.hour
min = now.minute

z=zipfile.ZipFile(f'{folder_name}_archive_{M}-{D}-{Y}_{H}{min}.zip','w')
z.writestr('README.txt',f'archive date {M}/{D}/{Y} {H}:{min}')

#if os.path.isfile(f'archive_{M}-{D}-{Y}_{H}:{min}.zip'):
			#os.remove(f'archive_{M}-{D}-{Y}_{H}:{min}.zip')

current_dir = os.getcwd()

# Loop through all files and directories in the current directory
for file in os.listdir(current_dir):
	# Check if the path is a file (not a directory) and matches the "*.py" pattern
	if os.path.isfile(os.path.join(current_dir, file)):
		# Print the filename
		if ".py" in file:
			print(file)
			z.write(file)
		if ".txt" in file:
			print(file)
			z.write(file)
		if ".sql" in file:
			print(file)
			z.write(file)
		if ".ini" in file:
			print(file)
			z.write(file)
		if ".html" in file:
			print(file)
			z.write(file)			
z.close()