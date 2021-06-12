from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class Introduccion(Page):
    def is_displayed(self):
        return self.round_number == 1

class Control_lectura(Page):
    def is_displayed(self):
        return self.round_number == 1

    form_model='player'
    form_fields=['pregunta1','pregunta2','pregunta3','pregunta4','pregunta5']


class Decision_primeraetapa(Page):
    form_model = 'player'
    form_fields = ['inversion']


class ResultsWaitPage1(WaitPage):
    body_text = "Espere que el otro participante responda, por favor."
    
class Resultados_primeraetapa(Page):
    def vars_for_template(self):
    
        investment_cost=self.player.inversion*Constants.k
        return dict(investment_cost=investment_cost,other_player_inversion=self.player.other_player().inversion)



class ResultsWaitPage2(WaitPage):
    body_text = "Espere que el otro participante responda, por favor."

    after_all_players_arrive ='set_payoffs'

class ShuffleWaitPage(WaitPage):
    wait_for_all_groups=True
    after_all_players_arrive='creating_session'


class Decision_segundaetapa(Page):
    form_model = 'player'
    form_fields = ['units']


class Resultados_segundaetapa(Page):
    def vars_for_template(self):
        return dict(other_player_units=self.player.other_player().units)


page_sequence = [Introduccion, Control_lectura, Decision_primeraetapa, ResultsWaitPage1, Resultados_primeraetapa, Decision_segundaetapa, ResultsWaitPage2, Resultados_segundaetapa, ShuffleWaitPage]