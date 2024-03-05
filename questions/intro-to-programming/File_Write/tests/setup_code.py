
import numpy as np
file_path = "text.txt"
name = np.random.choice(["Aria", "Mateo", "Isla", "Soren", "Nia", "Jasper", "Esme", "Leo", "Priya", "Felix", "Lila", "Kai", "Zara", "Milo", "Tessa", "Nolan", "Maya", "Luca", "Sienna", "Ethan", "Kangyu"])

file_content = """
            # Math 441 Homework 2
            """

with open("text.txt", "w") as f:
    f.write(file_content)
    f.close()
with open("test_text.txt", "w") as f:
    f.write(file_content)
    f.close()
with open("wrong_test_text.txt", "w") as f:
    f.write(file_content)
    f.close()