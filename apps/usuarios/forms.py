from django import forms

class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label='Nome de Cadastro',
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'placeholder': 'Ex.: João_Silva'
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

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')

        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Espaços não são permitidos nesse campo')
            else:
                return nome
            
    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get('senha_1')
        senha_2 = self.cleaned_data.get('senha_2')

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError('Senhas não são iguais')
            else:
                return senha_2

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
