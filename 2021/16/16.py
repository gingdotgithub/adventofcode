binary = ''
vsum = 0
hexinput = list("220D69802BE00A0803711E1441B1006E39C318A12730C200DCE66D2CCE360FA0055652CD32966E3004677EDF600B0803B1361741510076254138D8A00E4FFF3E3393ABE4FC7AC10410010799D2A4430003764DBE281802F3102CA00D4840198430EE0E00021D04E3F41F84AE0154DFDE65A17CCBFAFA14ADA56854FE5E3FD5BCC53B0D2598027A00848C63F2B918C7E513DEC3290051B3867E009CCC5FE46BD520007FE5E8AD344B37583D0803E40085475887144C01A8C10FE2B9803B0720D45A3004652FD8FA05F80122CAF91E5F50E66BEF8AB000BB0F4802039C20917B920B9221200ABF0017B9C92CCDC76BD3A8C4012CCB13CB22CDB243E9C3D2002067440400D9BE62DAC4D2DC0249BF76B6F72BE459B279F759AE7BE42E0058801CC059B08018A0070012CEC045BA01006C03A8000D46C02FA000A8EA007200800E00618018E00410034220061801D36BF178C01796FC52B4017100763547E86000084C7E8910AC0027E9B029FE2F4952F96D81B34C8400C24AA8CDAF4F1E98027C00FACDE3BA86982570D13AA640195CD67B046F004662711E989C468C01F1007A10C4C8320008742287117C401A8C715A3FC2C8EB3777540048272DFE7DE1C0149AC8BC9E79D63200B674013978E8BE5E3A2E9AA3CCDD538C01193CFAB0A146006AA00087C3E88B130401D8E304A239802F39FAC922C0169EA3248DF2D600247C89BCDFE9CA7FFD8BB49686236C9FF9795D80C0139BEC4D6C017978CF78C5EB981FCE7D4D801FA9FB63B14789534584010B5802F3467346D2C1D1E080355B00424FC99290C7E5D729586504803A2D005E677F868C271AA479CEEB131592EE5450043A932697E6A92C6E164991EFC4268F25A294600B5002A3393B31CC834B972804D2F3A4FD72B928E59219C9C771EC3DC89D1802135C9806802729694A6E723FD6134C0129A019E600")
#hexinput = list(input())
print(hexinput)
for hexi in hexinput:
    binary+=str(format(int(hexi,base=16), '04b'))
print(binary)

def read_metadata():
    global binary
    global vsum
    readlength = 0
    v,t,binary = binary[0:3],binary[3:6],binary[6:]
    readlength+=6
    print(v+"-"+t+"-"+binary)
    newpacket = [v,t,'',[]]
    vsum+=int(v,2)
    if (int(t,2)) == 4:
        literallength,literal = read_literal()
        readlength+=literallength
        newpacket[2] = literal
        # lenofpacket = 6+len(packets[len(packet)][2])
        # binary = binary[lenofpacket%4:]
    else:
        operatorlength,subpackets = read_operator()
        readlength+=operatorlength
        newpacket[3] = subpackets
    return readlength, newpacket

def read_literal():
    global binary
    readlength = 0
    newliteral = ''
    while True:
        indicator,chunk, binary = binary[0:1],binary[1:5],binary[5:]
        newliteral+=chunk
        readlength+=5
        if indicator == '0':
            break
    return readlength, newliteral

def read_operator():
    global binary
    readlength = 1
    subpackets = []
    ltid,binary = binary[0:1], binary[1:]
    if ltid == '0':
        readlength+=15
        lengthbits,binary = binary[0:15],binary[15:]
        bitstoread = int(lengthbits,2)
        readlength+=bitstoread
        while bitstoread > 0:
            newpacketlen, newpacket = read_metadata()
            bitstoread-=newpacketlen
            subpackets.append(newpacket)
    else:
        readlength+=11
        packetcount,binary = binary[0:11],binary[11:]
        for n in range(int(packetcount,2)):
            newpacketlen, newpacket = read_metadata()
            subpackets.append(newpacket)
            readlength+=newpacketlen
    return readlength, subpackets

readlngth,mainpacket = read_metadata()

print(mainpacket)
print(vsum)