from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=25, spacing=15)
        layout.add_widget(Label(text='[b]Cachê Direto[/b]', markup=True, font_size=28))
        layout.add_widget(Label(text='Plataforma Segura de Intermediação Musical', font_size=15))
        
        btn_banda = Button(text='Cadastrar Banda / Artista', background_color=(0.1, 0.6, 0.8, 1))
        btn_banda.bind(on_press=self.ir_para_banda)
        layout.add_widget(btn_banda)
        
        btn_som = Button(text='Cadastrar Locação de Som', background_color=(0.8, 0.4, 0.1, 1))
        btn_som.bind(on_press=self.ir_para_som)
        layout.add_widget(btn_som)
        
        btn_contratante = Button(text='Área do Contratante (Buscar Bandas e Som)', background_color=(0.2, 0.7, 0.3, 1))
        btn_contratante.bind(on_press=self.ir_para_contratante)
        layout.add_widget(btn_contratante)
        
        self.add_widget(layout)

    def ir_para_banda(self, instance):
        self.manager.current = 'banda'

    def ir_para_som(self, instance):
        self.manager.current = 'som'

    def ir_para_contratante(self, instance):
        self.manager.current = 'contratante'

class BandaScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=12, spacing=8)
        layout.add_widget(Label(text='Registo de Banda / Artista (Apenas Cadastro)', font_size=18))
        layout.add_widget(TextInput(hint_text='Nome da Banda / Grupo', multiline=False))
        layout.add_widget(TextInput(hint_text='Género Musical (ex: Pagode, Samba)', multiline=False))
        layout.add_widget(TextInput(hint_text='Localização / Cidade Base (ex: Guarulhos - SP)', multiline=False))
        layout.add_widget(TextInput(hint_text='Valor do Cachê Mínimo (R$)', multiline=False))
        layout.add_widget(TextInput(hint_text='Chave Pix para Recebimento Futuro', multiline=False))
        layout.add_widget(TextInput(hint_text='Link de Fotos / Portfólio', multiline=False))
        layout.add_widget(TextInput(hint_text='Link de Vídeo de Apresentação', multiline=False))
        
        btn_salvar = Button(text='Guardar Perfil na Plataforma', background_color=(0.1, 0.6, 0.8, 1), size_hint_y=None, height=40)
        btn_salvar.bind(on_press=self.salvar_perfil)
        layout.add_widget(btn_salvar)
        
        btn_voltar = Button(text='Voltar ao Início', size_hint_y=None, height=35)
        btn_voltar.bind(on_press=self.voltar)
        layout.add_widget(btn_voltar)
        
        self.add_widget(layout)

    def salvar_perfil(self, instance):
        box = BoxLayout(orientation='vertical', padding=10, spacing=10)
        box.add_widget(Label(text='Perfil guardado com sucesso!\nAguarde o contacto de contratantes interessados.'))
        btn_ok = Button(text='OK', size_hint_y=None, height=40)
        box.add_widget(btn_ok)
        popup = Popup(title='Registo Concluído', content=box, size_hint=(0.8, 0.5))
        btn_ok.bind(on_press=popup.dismiss)
        popup.open()

    def voltar(self, instance):
        self.manager.current = 'main'

class SomScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=12, spacing=8)
        layout.add_widget(Label(text='Registo de Locação de Som (Apenas Cadastro)', font_size=18))
        layout.add_widget(TextInput(hint_text='Nome do Fornecedor / Equipamentos', multiline=False))
        layout.add_widget(TextInput(hint_text='Localização / Cidade Base (ex: Guarulhos - SP)', multiline=False))
        layout.add_widget(TextInput(hint_text='Valor Orçado Base', multiline=False))
        layout.add_widget(TextInput(hint_text='Chave Pix para Recebimento', multiline=False))
        layout.add_widget(TextInput(hint_text='Link de Fotos dos Equipamentos', multiline=False))
        layout.add_widget(TextInput(hint_text='Link de Vídeo de Demonstração', multiline=False))
        
        btn_salvar = Button(text='Guardar Fornecedor de Som', background_color=(0.8, 0.4, 0.1, 1), size_hint_y=None, height=40)
        btn_salvar.bind(on_press=self.salvar_perfil)
        layout.add_widget(btn_salvar)
        
        btn_voltar = Button(text='Voltar ao Início', size_hint_y=None, height=35)
        btn_voltar.bind(on_press=self.voltar)
        layout.add_widget(btn_voltar)
        
        self.add_widget(layout)

    def salvar_perfil(self, instance):
        box = BoxLayout(orientation='vertical', padding=10, spacing=10)
        box.add_widget(Label(text='Equipamentos registados com sucesso!\nAguarde o contacto de contratantes.'))
        btn_ok = Button(text='OK', size_hint_y=None, height=40)
        box.add_widget(btn_ok)
        popup = Popup(title='Registo Concluído', content=box, size_hint=(0.8, 0.5))
        btn_ok.bind(on_press=popup.dismiss)
        popup.open()

    def voltar(self, instance):
        self.manager.current = 'main'

class ContratanteScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=12, spacing=8)
        layout.add_widget(Label(text='Painel do Contratante (Busca, Filtros e Checkout)', font_size=18))
        
        btn_menor_preco = Button(text='Filtrar por: Menor Preço', background_color=(0.3, 0.5, 0.7, 1), size_hint_y=None, height=38)
        btn_menor_preco.bind(on_press=lambda x: self.aplicar_filtro('Menor Preço'))
        layout.add_widget(btn_menor_preco)
        
        btn_mais_proxima = Button(text='Filtrar por: Mais Próxima (Região)', background_color=(0.3, 0.6, 0.5, 1), size_hint_y=None, height=38)
        btn_mais_proxima.bind(on_press=lambda x: self.aplicar_filtro('Mais Próxima'))
        layout.add_widget(btn_mais_proxima)
        
        layout.add_widget(TextInput(hint_text='Nome do seu Estabelecimento / Evento', multiline=False))
        layout.add_widget(TextInput(hint_text='Valor do Cachê Acordado (R$)', multiline=False))
        layout.add_widget(TextInput(hint_text='Forma de Pagamento (Pix / Cartão / Boleto)', multiline=False))
        
        btn_pagar = Button(text='Simular Pagamento e Regras da Taxa (1% + Encargos)', background_color=(0.2, 0.7, 0.3, 1), size_hint_y=None, height=42)
        btn_pagar.bind(on_press=self.abrir_caixa_pagamento)
        layout.add_widget(btn_pagar)
        
        btn_voltar = Button(text='Voltar ao Início', size_hint_y=None, height=35)
        btn_voltar.bind(on_press=self.voltar)
        layout.add_widget(btn_voltar)
        
        self.add_widget(layout)

    def aplicar_filtro(self, tipo_filtro):
        box = BoxLayout(orientation='vertical', padding=10, spacing=10)
        box.add_widget(Label(text=f'A aplicar filtro: {tipo_filtro}\nExibindo bandas e som ordenadas para o contratante.'))
        btn_ok = Button(text='Ver Resultados', size_hint_y=None, height=40)
        box.add_widget(btn_ok)
        popup = Popup(title='Filtro de Busca', content=box, size_hint=(0.8, 0.5))
        btn_ok.bind(on_press=popup.dismiss)
        popup.open()

    def abrir_caixa_pagamento(self, instance):
        box = BoxLayout(orientation='vertical', padding=10, spacing=10)
        box.add_widget(Label(text='Regra Financeira do Cachê Direto:\n- O app retém 1% de taxa.\n- Pagamentos por Cartão (parcelável) ou Boleto:\n  Todos os juros/encargos são assumidos pelo contratante.'))
        btn_confirmar = Button(text='Prosseguir com Pagamento Seguro', size_hint_y=None, height=40, background_color=(0.2, 0.7, 0.3, 1))
        box.add_widget(btn_confirmar)
        popup = Popup(title='Checkout Seguro - Cachê Direto', content=box, size_hint=(0.85, 0.65))
        btn_confirmar.bind(on_press=popup.dismiss)
        popup.open()

    def voltar(self, instance):
        self.manager.current = 'main'

class CacheDiretoApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(BandaScreen(name='banda'))
        sm.add_widget(SomScreen(name='som'))
        sm.add_widget(ContratanteScreen(name='contratante'))
        return sm

if __name__ == '__main__':
    CacheDiretoApp().run()
