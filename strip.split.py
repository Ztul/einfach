satz = "1.) Heute wird es schneien "
print(satz)
satz = satz.strip('1.)')
print(satz)

#lstrip() – links Zeichen entfernen (meistens Leerzeichen)

#strip() – rechts und links bestimmte Zeichen entfernen (meistens Leerzeichen)
#
#rstrip() – rechts Zeichen entfernen (meistens Leerzeichen)

satz = "Heute ist es windig und es wird schneien"
satz = satz.split(" ")
print(satz)
satz.sort(key=len)
print(satz)