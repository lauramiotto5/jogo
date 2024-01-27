# Personagem: classe mãe
# Herói: classe filha (controlado pelo usuário)
# Inimigo: classe filha (adversário do usuário)

import random


class Personagem:
    def __init__(self, nome, vida, nivel):
        self.__nome = nome  # <- atributos privados
        self.__vida = vida
        self.__nivel = nivel

 # como são privados criamos getters
    def get_nome(self):
        return self.__nome

    def get_vida(self):
        return self.__vida

    def get_nivel(self):
        return self.__nivel

    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNível: {self.get_nivel()}"

    def receber_ataque(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0

    def atacar(self, alvo):
        dano = random.randint(self.get_nivel() * 2, self.get_nivel() * 4)
        # dano baseado no nível
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!")
        # não preciso acessar o get, pois acesso é dentro da própria classe


class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        # herói tem algo a mais (habilidade)
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}\n"

    def ataque_especial(self, alvo):
        dano = random.randint(self.get_nivel() * 5, self.get_nivel() * 8)
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} usou a habilidade especial {self.get_habilidade()} em {alvo.get_nome()} e causou {dano} de dano!")


class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        # inimigo tem algo a mais (tipo)
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}\n"


class Jogo:
    # classe orquestradora do jogo
    def __init__(self) -> None:
        self.heroi = Heroi(nome="Herói", vida=100, nivel=5, habilidade="Socão")
        self.inimigo = Inimigo(nome="Morcego", vida=80, nivel=5, tipo="Voador")

    def iniciar_batalha(self):
        # gestão da batlha em turnos
        print("Iniciando batalha...")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nDetalhes dos personagens:")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input("Pressione ENTER para atacar...")
            escolha = input(
                "Escolha: 1) Ataque normal ou 2) Ataque especial: ")

            if escolha == '1':
                self.heroi.atacar(self.inimigo)
            elif escolha == '2':
                self.heroi.ataque_especial(self.inimigo)
            else:
                print("Escolha inválida. Tente novamente.")

            if self.inimigo.get_vida() > 0:
                # inimigo ataca herói
                self.inimigo.atacar(self.heroi)

        if self.heroi.get_vida() > 0:
            print("\nParabéns, você venceu a batalha!")
        else:
            print("\nVocê foi derrotado!")


# cria instância do jogo e inicia batalha
jogo = Jogo()
jogo.iniciar_batalha()
