map = {"UUU":"Phe", "UUC":"Phe", "UUA":"Leu", "UUG":"Leu",
    "UCU":"Ser", "UCC":"Ser", "UCA":"Ser", "UCG":"Ser",
    "UAU":"Tyr", "UAC":"Tyr", "UAA":"STOP", "UAG":"STOP",
    "UGU":"Cys", "UGC":"Cys", "UGA":"STOP", "UGG":"Trp",
    "CUU":"Leu", "CUC":"Leu", "CUA":"Leu", "CUG":"Leu",
    "CCU":"Pro", "CCC":"Pro", "CCA":"Pro", "CCG":"Pro",
    "CAU":"His", "CAC":"His", "CAA":"Gln", "CAG":"Gln",
    "CGU":"Arg", "CGC":"Arg", "CGA":"Arg", "CGG":"Arg",
    "AUU":"Ile", "AUC":"Ile", "AUA":"Ile", "AUG":"Met",
    "ACU":"Thr", "ACC":"Thr", "ACA":"Thr", "ACG":"Thr",
    "AAU":"Asn", "AAC":"Asn", "AAA":"Lys", "AAG":"Lys",
    "AGU":"Ser", "AGC":"Ser", "AGA":"Arg", "AGG":"Arg",
    "GUU":"Val", "GUC":"Val", "GUA":"Val", "GUG":"Val",
    "GCU":"Ala", "GCC":"Ala", "GCA":"Ala", "GCG":"Ala",
    "GAU":"Asp", "GAC":"Asp", "GAA":"Glu", "GAG":"Glu",
    "GGU":"Gly", "GGC":"Gly", "GGA":"Gly", "GGG":"Gly"}

print("Here you will be able to transcribe a DNA sequence into RNA.") #Introduction
print("")

def split(word):
    return list(word) #Will turn the string into a list

def transcribe(list):
    for i in range(len(list)): #For loop that transcribed DNA sequence
        if list[i] == "A":
            list[i] = "U"
        elif list[i] == "C":
            list[i] = "G"
        elif list[i] == "T":
            list[i] = "A"
        elif list[i] == "G":
            list[i] = "C"
        elif list[i] != "A" and list[i] != "C" and list[i] != "T" and list[i] != "G":
            list[i] = "/"

def combine(seq):
    space = ""
    return(space.join(tuple(seq))) #This combines the list into a string

def translate_rna(rna): #Divides string into into sets of 3 characters in a list, and converts based on the dict gencode.
    rnaPrint = rna
    for i in range(1):
        rna = [rna[i:i+3] for i in range(0, len(rna), 3)]
    for b in range(1):
        for k in range(len(rna)):
            key = rna[k]
            if key in map:
                rna[k] = map.get(rna[k])
                test = 1
            else:
                test = 0
        start = "Met"
        end = "STOP"
        rna = combine(rna)
        rna2 = rna[rna.find(start) + len(start):rna.rfind(end)]
        rna2 = "Met" + rna2
        if test == 1:
            print("")
            print("Your mRNA strand " + rnaPrint + " was translated into " + rna2 + ".")
        elif test == 0:
            print("")
            print("Error: You do not have a valid sequence for the translation process.")

dnaSeq = input("Please input a valid DNA sequence: ")

dnaSeq = dnaSeq.upper() #Turns sequence into all capitalized letters
dnaSeq_list = split(dnaSeq) #Turns DNA string into a list

print("")

dnaSequenceStored = dnaSeq
transcribe(dnaSeq_list)
rnaSeq_list = dnaSeq_list

print("Your DNA sequence " + dnaSequenceStored + " was transcribed into the following mRNA sequence: " + combine(dnaSeq_list))
print("")
print("Note: Invalid characters (that are not A, C, T, and G) were converted into /.")

translate_rna(combine(rnaSeq_list))


















