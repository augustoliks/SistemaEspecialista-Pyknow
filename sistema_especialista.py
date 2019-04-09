from pyknow import *


class TemNamorada(Fact):
    pass

class VaiTrabalhar(Fact):
    pass

class TemProva(Fact):
    pass

class TemFutebolMarcado(Fact):
    pass

class TemTempoLivre(Fact):      # encadeada
    pass


class SistemaEspecialista(KnowledgeEngine):

    @Rule(NOT(VaiTrabalhar(fato=W())))
    def vai_trabalhar(self): 
        decisao = True if input('Vai trabalhar [s/n]: ') == 's' else False
        self.declare(VaiTrabalhar(fato=decisao))

    @Rule(NOT(TemProva(fato=W())))
    def tem_prova(self): 
        decisao = True if input('Tem prova [s/n]: ') == 's' else False
        self.declare(TemProva(fato=decisao))

    @Rule(NOT(TemNamorada(fato=W())))
    def tem_namorada(self): 
        decisao = True if input('Tem namorada [s/n]: ') == 's' else False
        self.declare(TemNamorada(fato=decisao))

    @Rule(NOT(TemFutebolMarcado(fato=W())))
    def tem_fut_marcado(self): 
        decisao = True if input('tem fut marcado [s/n]') == 's' else False
        self.declare(TemFutebolMarcado(fato=decisao))

    @Rule(
        AND(
            TemProva(fato=True)
        )
    )
    def prova(self):
        print('>>>\tEstude para a prova')
        self.declare(TemTempoLivre(fato=False))

    @Rule(
        AND(
            TemTempoLivre(fato=True),
            TemFutebolMarcado(fato=True),
            TemNamorada(fato=False)
        )
    )
    def jogar_bola(self):
        print('>>>\tVai jogar bola')


    @Rule(
        AND(
            TemTempoLivre(fato=True),
            TemNamorada(fato=True)
        )
    )
    def sair_com_a_namorada(self):
        print('>>>\tVai sair com sua namorada')


    @Rule(
        AND(
            VaiTrabalhar(fato=False),
            TemProva(fato=False),
        )
    )
    def tempo_livre(self):
        self.declare(TemTempoLivre(fato=True))
        print(">>>\tVoce tem tempo livre")


app = SistemaEspecialista()
app.reset()
app.run()
