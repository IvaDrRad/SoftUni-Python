current_version = input().split('.')
new_version_int = int(''.join(current_version)) + 1
print('.'.join(str(new_version_int)))
