import emoji

raw = input("Input: ")
print(f"Output: {emoji.emojize(raw, language="alias")}")
