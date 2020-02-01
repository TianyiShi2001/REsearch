from django import forms


class SeqForm(forms.Form):
    mcs = forms.CharField(label='sex', max_length='1000000')
    goi = forms.CharField(label='goi', max_length='1000000')
    mcsFile = forms.FileField(label='msc_file')
    goiFile = forms.FileField()
