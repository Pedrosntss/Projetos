print( "=" * 45)
print(" "*12+"A Playlist do Fudencio")
print("=" * 45)
playlist = [ "zézé de amargo", "religião Urbana", "Narville", "Franguito Lopes", "Raul Seitas"]

playlist.append("Xitadinho e chororou")
playlist.append("P.Diddy bieber")
playlist.append("Jimin du bts")

playlist.remove("Jimin du bts")
playlist.sort()

print("Sua playlist final: ")
for cantor in playlist:
    print(cantor)
print("=" * 45)