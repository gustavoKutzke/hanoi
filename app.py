class TorreHanoi:
    def __init__(self, n, origem, destino, auxiliar):
        self.n = n
        self.origem = origem
        self.destino = destino
        self.auxiliar = auxiliar
        self.movimentos = []

    def resolver(self):
        self._mover(self.n, self.origem, self.destino, self.auxiliar)

    def _mover(self, n, origem, destino, auxiliar):
        if n == 1:
            self.movimentos.append(f"🔹 Mova o disco 1 de {origem} para {destino}")
        else:
            self._mover(n-1, origem, auxiliar, destino)
            self.movimentos.append(f"🔹 Mova o disco {n} de {origem} para {destino}")
            self._mover(n-1, auxiliar, destino, origem)

    def exibir_movimentos(self):
        for movimento in self.movimentos:
            print(movimento)
        print("-" * 40)
        print(f"✅ Total de movimentos: {len(self.movimentos)}")

if __name__ == '__main__':
    print("="*40)
    print("🧠  TORRE DE HANOI".center(40))
    print("="*40)
    try:
        n = int(input("📦 Digite o número de discos: "))
        origem = input("🟩 Torre de origem (A, B ou C): ").strip().upper()
        destino = input("🟥 Torre de destino (A, B ou C): ").strip().upper()
        auxiliar = input("🟦 Torre auxiliar (A, B ou C): ").strip().upper()

        torres = {origem, destino, auxiliar}
        if len(torres) < 3:
            print("\n❌ Erro: As torres devem ser distintas entre si.")
        else:
            jogo = TorreHanoi(n, origem, destino, auxiliar)
            jogo.resolver()
            print("\n📋 Lista de movimentos:")
            print("-" * 40)
            jogo.exibir_movimentos()

    except ValueError:
        print("❌ Entrada inválida. Por favor, digite um número inteiro.")