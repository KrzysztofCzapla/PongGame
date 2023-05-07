import random
import pygame




class Napisy():

	def __init__(self, display,color, text = "SomeText", fontsize = 12,fontface = None):
		self.dsp = display
		self.txt = text
		self.f = fontsize
		self.color = color

		self.fontface = pygame.font.match_font(fontface)

		self.font = pygame.font.Font(self.fontface, self.f)

		self.txtSurf = self.font.render(self.txt, True, self.color)

	def update(self,x,y):
		self.dsp.blit(self.txtSurf,(x,y))

	def change(self, tekst):
		self.txt = tekst
		self.txtSurf = self.font.render(self.txt, True, self.color)



