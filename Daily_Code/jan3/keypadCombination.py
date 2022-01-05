#125==> ['adm', 'adn', 'ado', 'adp', 'aem', 'aen', 'aeo', 'aep', 'afm', 'afn', 'afo', 'afp', 'bdm', 'bdn', 'bdo', 'bdp', 'bem', 'ben', 'beo', 'bep', 'bfm', 'bfn', 'bfo', 'bfp', 'cdm', 'cdn', 'cdo', 'cdp', 'cem', 'cen', 'ceo', 'cep', 'cfm', 'cfn', 'cfo', 'cfp']

# "" ==> []

key={'1':'abc','2':'def','3':'ghi','4':'jkl','5':'mnop','6':'qrst','7':'uv'}

def keypadComb(num):
    if num=="":
        return []
    if len(num)==1:
        return list(key[num[0]])
    arr=keypadComb(num[1:])
    temp=[]
    for i in key[num[0]]:
        for j in arr:
            temp.append(i+j)
    return temp

print(keypadComb('125'))
print(keypadComb(''))
