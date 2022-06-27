def Palindrome(frase):
    return frase == frase[::-1]
 
 
# Driver code
frase = input("Ingrese una palabra o frase: ")
z = Palindrome(frase)
 
if z:
    print("Es palindrome")
else:
    print("No es palindrome")