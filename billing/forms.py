from django import forms
from .models import Debtor, Documents, DocumentAmount, IntrestAmount


class DebtorForm(forms.ModelForm):  
    class Meta:  
        model = Debtor  
        fields = '__all__'

    

class DocumentsForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = ['debtor','docno','percentage','totalamount','additionaldocumentsname','additionaldocuments','checkleafcount','checkleaf','deed','bond','passbook']

        widgets = {
            'file': forms.ClearableFileInput(attrs={'multiple': True}),
        }




class IntrestAmountForm(forms.ModelForm):
    class Meta:
        model = IntrestAmount
        fields =['amount','pendingdate','fineamount','reason','paid','intrestamount','result','duedate']

        