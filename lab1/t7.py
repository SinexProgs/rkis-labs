strings = ["amnyam", "1546234", "httb://opa", "mlem", "http://moo", "blin", "http://||//"]
print("Original list:", strings)
i = 0
while i < len(strings):
    if not strings[i].startswith("http://"):
        del strings[i]
    else:
        i += 1
print("Reversed list:", strings)