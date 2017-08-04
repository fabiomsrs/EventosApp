from django import forms
from evento.models import Cupom

class CupomForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop("user") #recebendo usuario logado
		super(CupomForm, self).__init__(*args, **kwargs)		
	
		self.fields['evento'].queryset =  self.user.meus_eventos.all()
		self.fields['evento'].empty_label = 'Empty'			
		self.fields['evento'].label = 'Evento pertencente'		
		self.fields['desconto'].label = 'Desconto em porcento'

	class Meta:
		model = Cupom		
		fields = ('desconto','evento')				