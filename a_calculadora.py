import bonitesas as bn
import operações_nfunção as on
import teste_poo
bn.titulo('THE EUCLIDES')
exp = teste_poo.Explicação()
while True:
 bn.titulo2('MENU')
 print(f'''escolha qual funcionalidade da calculadora voce deseja acessar?
 [1] ativar e desativar explicações [{exp.mensagem}]
 [2] calculadora de média, moda e mediana
 [3] conversor de numero decimal para binario 
 [4] calculadora de matriz
 [5] calculadora de regra de 3 simples e composta
 [6] calculadora de operações básicas''')
 escolha = int(input('sua escolha: '))
 if escolha == 1:
  exp.ativa()
 elif escolha == 2:
  on.média(exp.escolha)
 elif escolha == 3:
  on.converbinaria(exp.escolha)
 elif escolha == 4:
  on.matriz(exp.escolha)
 elif escolha == 5:
  on.regra3(exp.escolha)
 elif escolha == 6:
  on.operações(exp.escolha)
  
 