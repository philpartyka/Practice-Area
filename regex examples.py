import re
def transform_record(record):
  new_record = re.sub(r"([\d-]{1,12})", r"+1-\1", record)
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator