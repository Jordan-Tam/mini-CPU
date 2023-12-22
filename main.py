# NAME: Jordan Tam
# PLEDGE: I pledge my honor that I have abided by the Stevens Honor System.

lineNumbers = ["0", "1", "2", "3", 
               "4", "5", "6", "7", 
               "8", "9", "a", "b", 
               "c", "d", "e", "f"]
lineNumbers = [ln + "0: " for ln in lineNumbers]

imageFileText = []
imageFileText.append("v3.0 hex words addressed")

hexList = []

with open("program.txt") as myFile:
  for instruction in myFile:

    list = instruction.split()
    
    """
    list[0] = LDR/STR/ADD/SUB
    list[1] = write register (Rt/Rd)
    list[2] = read register (Rn)
    list[3] = immediate number (imm)
    """

    hexTranslation = ""
    
    # Determine the operation
    match list[0]:
      case "LDR":
        # hexTranslation += "1011"
        hexTranslation += "b"
      case "STR":
        # hexTranslation += "0110"
        hexTranslation += "6"
      case "ADD":
        # hexTranslation += "0011"
        hexTranslation += "3"
      case "SUB":
        # hexTranslation += "0001"
        hexTranslation += "1"

    # Determine the immediate number
    imm = hex(int(list[3]))[2:]
    if (len(imm) == 1):
      imm = "0" + imm
    hexTranslation += imm

    # Determine the read register
    thing1 = ""
    match list[2]:
      case "R0":
        thing1 += "00"
      case "R1":
        thing1 += "01"
      case "R2":
        thing1 += "10"
      case "R3":
        thing1 += "11"

    # Determine the write register
    match list[1]:
      case "R0":
        thing1 += "00"
      case "R1":
        thing1 += "01"
      case "R2":
        thing1 += "10"
      case "R3":
        thing1 += "11"


    match thing1:
      case "0000":
        hexTranslation += "0"
      case "0001":
        hexTranslation += "1"
      case "0010":
        hexTranslation += "2"
      case "0011":
        hexTranslation += "3"
      case "0100":
        hexTranslation += "4"
      case "0101":
        hexTranslation += "5"
      case "0110":
        hexTranslation += "6"
      case "0111":
        hexTranslation += "7"
      case "1000":
        hexTranslation += "8"
      case "1001":
        hexTranslation += "9"
      case "1010":
        hexTranslation += "a"
      case "1011":
        hexTranslation += "b"
      case "1100":
        hexTranslation += "c"
      case "1101":
        hexTranslation += "d"
      case "1110":
        hexTranslation += "e"
      case "1111":
        hexTranslation += "f"

    hexList.append(hexTranslation)

myFile = open("image.txt", "w")
myFile.write("v3.0 hex words addressed\n")
currentInstructionIndex = 0
for i in lineNumbers:
  # Write lineNumber to new file
  myFile.write(i)
  for j in range(16):
    # Write next hexadecimal instruction to new file
    if (len(hexList) <= currentInstructionIndex):
      myFile.write("0000 ")
    else:
      myFile.write(hexList[currentInstructionIndex])
      currentInstructionIndex += 1
      myFile.write(" ")
  myFile.write("\n")
myFile.close()