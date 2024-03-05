if data["params"]["method"] == "write":
    mode = "w"
    wrong_mode = "a"
else:
    mode = "a"
    wrong_mode = "w"
with open("test_text.txt", mode) as f:
    f.write(name)
with open("wrong_test_text.txt", wrong_mode) as fw:
    fw.write(name)