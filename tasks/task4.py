companions = ["Astarion", "Gale", "Karlach", "Lae'zel",  
              "Shadowheart", "Wyll", "The Dark Urge", "Halsin",  
              "Jaheira", "Minsc", "Minthara", "Alfira", "Losiir"]
# ["Gale", "Karlach", "Lae'zel"]
print(companions[1:4])
# ["Gale", "Lae'zel", "Wyll", "Halsin", "Halsin", "Minsc", "Alfira"]
print(companions[1:2] + companions[3:4] + companions[5:6] + companions[7:8] + companions[7:8] + companions[9:10] + companions[11:12])
# ["Alfira", "Jaheira", "Wyll", "Karlach"]
print(companions[11:12] + companions[8:9] + companions[5:6] + companions[2:3])
# ["Astarion", "Losiir"]
print(companions[0:1] + companions[12:13])
