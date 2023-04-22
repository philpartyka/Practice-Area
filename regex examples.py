import re
def transform_record(record):
  new_record = re.sub(r"([\d-]{1,12})", r"+1-\1", record)
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator


lines = ['a = 1;', 'b = input();', '', 'if a + b > 0 && a - b < 0:', '    start()', 'elif a*b > 10 || a/b < 1:', '    stop()', 'print set(list(a)) | set(list(b))', '#Note do not change &&& or ||| or & or |', "#Only change those '&&' which have space on both sides.", "#Only change those '|| which have space on both sides."]

for i in range(len(lines)):
    lines[i] = re.sub(r" && ", " and ", lines[i])
    lines[i] = re.sub(r" \|\| ", " or ", lines[i])  

print(lines)