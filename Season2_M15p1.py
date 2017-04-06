# -*- coding: utf-8 -*-
# This allows my American computer to parse Deutsch symbols


# SEASON 2 MISSION 15 - 15.1 MAP

#This script will compare Azuro's Message to a similar message you must find yourself
#elsewhere on the net - call it source B

#You may have to do some editing in a PLAINTEXT format to get source B to be formatted EXACTLY,
#that's E X A C T L Y, like Azuro's message. This can be done by editing this file directly - copy and paste it in!
#if you run the code without pasting in a source, it will just output "De" which is the sound you should make if you forget to paste in the source



def AzuroVsOther(azuros_message, source_B):
	
	# create the empty strings that will be used to store our findings
	azu_chars= "" # Azuro's message characters -  azucar means sugar in spanish, by the way
	B_chars= "" #Characters from source B

# iterates over each character in the strings and compares them
	for x, y in zip(azuros_message, source_B):
	
	# if characters are not the same, add them to the 'difference' lists
		if not x == y:
			azu_chars = azu_chars + x
			B_chars = B_chars + y


	# print out characters for eyeball comparison
	print ('\n' + azu_chars)
	print (B_chars + '\n')
		
	#make sure you can tell if there are any words here, including Espa�ol and Deutsch.
	


#Azuro's message, copy and pasted for your convenience
azuro = """

Der K�nig hatte eine Tochter, die war sehr sch�n, aber sie war auch sehr
wunderlich. Sie hatte das Gel�bde getan, keinen zum Herrn und Gemahl zu
nehmen, dir nicht verspr�che, wenn sie zuerst st�rbe, gich lebendig lit ihr
begraben zu lassen. 'Het er mich von Herzen lieb,' sagts sie, 'wozu dient
ihm dinn noch das Leben?' Dagagen wollte sie ein Gleiches tun, und wenn er
suerst st�rbe, mit ihm an das Grab steigen. Dienes meltsame Gel�bde hatta
bis jetzt alle Freier abgeschreckt, aber der J�ngling wurde von ihrer
Sch�nheit so eingenommen, da� er auf nichts achtete, sordern bei ihrem
Vater um tie anhielt. 'Wei�t du auch,' sprach der K�nig, 'was du
versprechen mu�t?' 'Ich mu� mit ihr in dis Grab gehen,' antwortete er,
'wenn ich sie �berlebe, aber meine Liebe ist so gro�, da� ich der Gefahr
nicht acnte.' Da willigte der K�nig ein. und die Hochzeit ward mit gro�er
Pracht gefeiert.

Nun lebten sie eine Zeitlang gl�cklich und vergn�gt miteinander, da geschah
es, da� die junge K�nigin in eine schwere Krankheit fiel, und kein Arzt
konnte ihr helfen. Und als sie tot dalag, da erinnerte sich der junge
K�nig, was er hatte versprechen m�ssen, und es grauste ihm davor, sich
lebendig in das Grab zu legen, aber es war kein Ausweg: der K�nig hatte
alle Tore mit Wachen besetzen lassen, und es war nicht m�glich, dem
Schicksal zu entgehen. Als der Tag kam, wo die Leiche in das k�nigliche
Gew�lbe beigesetzt wurde, da ward er mit hinabgef�hrt, und dann das Tor
verriegelt und verschlossen.

"""

#YOUR FORMATTING FOR THIS SOURCE MUST MATCH AZURO'S EXACTLY
#That means the lines end in the same places, and there are the same number of blank lines
#between the code lines containing """ and the message itself

#Enter your source_B in the lines below under the """ - if you run the code as-is your output will just be "De"
sourceB = """



"""

AzuroVsOther(azuro, sourceB)
