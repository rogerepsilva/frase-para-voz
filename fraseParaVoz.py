import pyttsx3 as pt

robo = pt.init() #Inicializando biblioteca

frase = input("Digite uma frase: ") #Solicita interação do usuário

robo.say(frase) #Robo fala a frase

robo.runAndWait() #Robo inicia e espera o final da frase
#Olá, Atrás não é o pote que você deve acordar
print("Finish")