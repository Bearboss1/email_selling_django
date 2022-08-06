from django import forms


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    comment = forms.CharField(required=False,
                              widget=forms.Textarea(attrs={'class': 'form-control',
                                                          'rows': 5}),
                              )
