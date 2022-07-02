codes = [
        'EF18E7',
        'EF807F',
        'EF40BF',
        'EFC03F',
        'EF20DF',
        'EFA05F',
        'EF609F',
        'EFE01F',
        'EF10EF',
        'EF906F',
        'EFD02F',
        'EF00FF',
        'EF50AF',
        'EFF807',
        'EF42BD',
        'EFC23D',
        'EF02FD',
        'EF08F7',
        'EFF00F',
        'EF8877',
        'EF708F',
        'EFB04F',
        'EF48B7',
        'EF38C7',
        'EFC837',
        'EFA857',
        'EF6897',
        'EF28D7',
        'EFE817',
        'EF7887',
        'EF22DD',
        'EF12ED',
        'EFB847',
        'EF629D',
        'EFD22D',
        'EFE21D',
        'EF926D',
        'EF52AD',
        'EFA25D',
        'EF32CD',
        'EFB24D',
        'EF728D',
        'EFF20D',
        'EF0AF5',
        ]


integer_codes = sorted(int(code, 16) for code in codes)
differences = []

for i, code in enumerate(integer_codes):
    if i == len(integer_codes) - 1:
        continue

    val = integer_codes[i+1] - code
    differences.append(val)
    print(f"{integer_codes[i+1]} - {code} =   {val}")

unique_differences = set(differences)
print(f"Unique differences: {unique_differences}")

new_codes = []

for code in integer_codes:
    for diff in unique_differences:
        new_codes.append(hex(code - diff))
        new_codes.append(hex(code + diff))

print(f"Total new codes: {len(new_codes)}")
unique_new_codes = set(new_codes)
print(f"Unique new codes: {len(unique_new_codes)}")

for i, hex_code in enumerate(unique_new_codes):
    print(f'power{i+1}                   {hex_code} 0x000000')



for i, code in enumerate(codes):
    continue
    print(int(code, 16))
    if i == len(codes) - 1:
        continue
    x = int(code, 16)
    y = int(codes[i+1], 16)
    difference = x - y
    print(f"{y} - {x} = {difference}")
