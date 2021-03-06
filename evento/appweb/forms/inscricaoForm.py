import json
from django import forms
from core.models import Evento, Atividade
from inscricao.models import Inscricao

#forms.CheckboxSelectMultiple()
class InscricaoForm(forms.Form):	
	def __init__(self, *args, **kwargs):
		self.atividades = kwargs.pop("atividades")
		super(InscricaoForm, self).__init__(*args, **kwargs)			
		self.fields["atividades"] = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=([(atividade.pk, atividade) for atividade in self.atividades]))
		#self.fields["atividades"].widget = forms.CheckboxSelectMultiple()
	
	class Meta:
		model = Inscricao
		exclude = ['usuario','evento','cupom']
		fields = '__all__'