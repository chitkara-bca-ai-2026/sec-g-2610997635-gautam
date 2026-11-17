
print("=========================================")
print("          TEXT PROCESSING TOOL          ")
print("=========================================")


sentence = input("Enter a sentence: ")
print()
print("--- Processing Results ---")


pos = int(input("Enter position for indexing: "))
print(f"Character at position {pos} : '{sentence[pos]}'")


start = int(input("Enter start index for slicing : "))
end = int(input("Enter end index for slicing   : "))
print(f"Sliced string [{start}:{end}]          : '{sentence[start:end]}'")


print(f"Uppercase                    : {sentence.upper()}")
print(f"Lowercase                    : {sentence.lower()}")


to_replace = input("Enter word to replace        : ")
replace_with = input("Enter replacement word       : ")
print(f"After replace                : {sentence.replace(to_replace, replace_with)}")


print(f"Length of sentence           : {len(sentence)}")
print()

print("=========================================")
print("Analysis Complete!")
print("=========================================")