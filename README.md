Engima
an engima code machine that can be customised
initialize an engima machine with 3 dials, their initial positions are "S""F""G"

# eng=engima('SFG')  

initialize an engima machine with 4 dials, their initial positions are "S""F""G""D"

# eng=engima('SFGD') 


the real engima machine has a reflect layer that replaces paired letters, so does this one
default pairs are :'TUVYZAKLNOHIJCBEFGMDPWXQRS' which means T-U pair, V-Y pair, Z-A pair ... 
set ur own pairs like:

# eng.reflect.random_alphabet='TUVYZAKLNOHIJCBEFGMDPWXQRS' 

how to use:

# eng.translate("ATTACK")  ->  "XSUDZL"
# eng=engima('SFGD')                       #reset the machine
# eng.translate("XSUDZL")  -> "ATTACK"


