########################################################################################

import subprocess

cmd = "ipconfig"
#cmd =cmd.split(' ')

p = subprocess.Popen(cmd,stdout = subprocess.PIPE, stderr=subprocess.PIPE, encoding='cp850', shell=True)

# le sortie et erreur sont récuperées par les attributs stdout et stderr. faite un read()
print (f"résultat commande : \n {p.stdout.read()}")
print (f"erreur commande : \n {p.stderr.read()}")
# ou vous pouvez récuperer les flux sortie et erreur en une passe avec p.communicate()
#out, err = p.communicate()
#print (f"retour {out}, erreur{err}")
""" 
cette dernière ligne n'afiche rien car les pipes ont déja été lus par les instruction précédentes,
 donc communicate() nr récupére rien
"""

########################################################################################