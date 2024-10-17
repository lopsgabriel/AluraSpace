from django import forms

class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label='Nome de Cadastro',
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'placeholder': 'Ex.: João Silva'
            }
        )
    )
    email=forms.EmailField(
        label='Email',
        required=True, 
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': "form-control",
                'placeholder': 'Ex.: JoãoSilva@gmail.com'
            }
        )
    )
    senha_1=forms.CharField(
        label='Senha', 
        required=True, 
        max_length=30, 
        widget=forms.PasswordInput(
            attrs={
                'class': "form-control",
                'placeholder': 'Digite sua senha'
            }
        )
    )
    senha_2=forms.CharField(
        label='Confirme sua senha', 
        required=True, 
        max_length=30, 
        widget=forms.PasswordInput(
            attrs={
                'class': "form-control",
                'placeholder': 'Digite a sua senha novamente'
            }
        )
    )

class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label='Nome de Login',
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'placeholder': 'Digite o nome de login'
            }
        )
    )   
    senha=forms.CharField(
        label='Senha', 
        required=True, 
        max_length=30, 
        widget=forms.PasswordInput(
            attrs={
                'class': "form-control",
                'placeholder': 'Digite sua senha'
            }
        )
    )
