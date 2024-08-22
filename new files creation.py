contents = ['Cookies Recipes', 'Cookbooks of the world', '30 Healthy Recipes', 'Amazing cuisines of the world']
filenames = ['cookies.txt', 'cookbooks.txt', 'Healthy.txt','Cuisines.txt']
for content, filename in zip(contents, filenames):
    file = open(f"venv/{filename}",'w')
    file.write(content)
    file.close()

filenames = [filename.replace('.','-')+'.txt' for filename in filenames]
print(filenames)
