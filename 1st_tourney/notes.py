#! /bin/python3

'''
Pretende-se que implemente uma função que detecte códigos ISBN inválidos.  Um
código ISBN é constituído por 13 digitos, sendo o último um digito de controlo.
Este digito de controlo é escolhido de tal forma que a soma de todos os
digitos, cada um multiplicado por um peso que é alternadamente 1 ou 3, seja um
múltiplo de 10.  A função recebe um dicionário que associa livros a ISBNs, e
deverá devolver a lista ordenada de todos os livros com ISBNs inválidos.
'''
def isbn(livros):
  res = [];
  livro_isbn = [None]*13;
  livros_nomes = list(livros.keys());
  livros_isbns = list(livros.values());
  for livro_nome, livro_isb in zip(livros_nomes,livros_isbns):
    charges = [1,3] * 13;
    livro_isbn = [int(x) for x in livro_isb];
    for charge, i in zip(charges,range(0,13)):
      livro_isbn[i] = charge * livro_isbn[i];
    if (sum(livro_isbn) % 10):
      res.append(livro_nome);
  return sorted(res);
"""

implemente uma função que dado um dicionário com as preferências dos alunos por
projectos (para cada aluno uma lista de identificadores de projecto, por ordem
de preferência), aloca esses alunos aos projectos. A alocação é feita por ordem
de número de aluno, e cada projecto só pode ser feito por um aluno. A função
deve devolver a lista com os alunos que não ficaram alocados a nenhum projecto,
ordenada por ordem de número de aluno.

"""

def aloca(prefs):
  res = list(); # list with unallocated students
  proj = list(); # list with currently allocated projects
  alunos = list(); # list with allocated students
  keys = sorted(prefs.keys());
  for aluno in keys:
    if not (len(prefs[aluno])):
      res.append(aluno);
    else:
      pl = prefs[aluno]
      p = iter(pl);
      it = next(p,"end");
      while (it != "end" and aluno not in res and aluno not in alunos):
        if (it not in proj):
          proj.append(it)
          alunos.append(aluno)
        elif (it is pl[-1]):
          res.append(aluno)
        it = next(p, "end")
  return res;

"""
um Hacker teve acesso a um log de transações com cartões de crédito. O log é
uma lista de tuplos, cada um com os dados de uma transação, nomedamente o
cartão que foi usado, podendo alguns dos números estar ocultados com um *, e o
email do dono do cartão.

Pretende-se que implemente uma função que ajude o hacker a reconstruir os
cartões de crédito, combinando os números que estão visíveis em diferentes
transações. Caso haja uma contradição nos números visíveis deve ser dada
prioridade à transção mais recente, i.é, a que aparece mais tarde no log.

A função deve devolver uma lista de tuplos, cada um com um cartão e um email,
dando prioridade aos cartões com mais digitos descobertos e, em caso de
igualdade neste critério, aos emails menores (em ordem lexicográfica).

"""
def join(old,new):
  res = "";
  for i in range(len(new)):
    if (new[i] != '*'): res += new[i];
    else: res += old[i];
  return res;
def sortkey(item):
  a,b = item;
  return (a.count('x'),b);
def hacker(log):
  res = list();
  aux = dict();
  for item in log:
    num,mail = item;
    if mail not in aux: aux[mail] = num;
    else: aux[mail] = join(aux[mail], num);
  res = [(b,a) for (a,b) in aux.items()];
  res = sorted(res, key= lambda a : a[1]);
  res = sorted(res, key= lambda a : a[0].count('*'));
# return sorted([a,b for b,a in aux.items()],key=sortkey);
  return res;

'''
Neste problem pretende-se que defina uma função que, dada uma string com
palavras, devolva uma lista com as palavras nela contidas ordenada por ordem de
frequência, da mais alta para a mais baixa. Palavras com a mesma frequência
devem ser listadas por ordem alfabética.
'''

def frequencia(text):
  uniq = len(set(text.split()));
  res = list();
  freq = dict();
  for word in text.split():
    if not(word in freq):
      freq[word] = 1;
    else: freq[word] += 1;
  res = freq.keys();
  res = sorted(res, key= lambda x : x);
  res = sorted(res, key= lambda x : freq[x], reverse=True);
  return res;
'''
Defina uma função que, dada uma lista de nomes de pessoas, devolva essa lista
ordenada por ordem crescente do número de apelidos (todos menos o primeiro
nome). No caso de pessoas com o mesmo número de apelidos, devem ser listadas
por ordem lexicográfica do nome completo.
'''

def apelidos(nomes):
  nomes = sorted(nomes);
  nomes = sorted(nomes, key=lambda x : len((x.split())[1:]));
  return nomes;

"""

Implemente uma função que formata um programa em C.  O código será fornecido
numa única linha e deverá introduzir um '\n' após cada ';', '{', ou '}' (com
excepção da última linha).  No caso do '{' as instruções seguintes deverão
também estar identadas 2 espaços para a direita.

"""
def formata(raw_code):
  formated_code = ""
  r_code_l = list(raw_code);
  inter_code = []
  nest = 0;
  for c,i in zip(r_code_l,range(len(r_code_l))):
    if i == 0 and c == ' ':
      while c == ' ' and r_code_l:
        r_code_l.pop(0)
        if r_code_l:
          c = r_code_l[0]
    else:
      if i < len(r_code_l) - 1:
        if c == ' ':
          while (i < len(r_code_l)-1 and r_code_l[i+1] == ' '):
            r_code_l.pop(i+1)
      elif i == len(r_code_l) -1 and c == ' ':
          while c == ' ' and r_code_l:
            r_code_l.pop();
            c = r_code_l[-1]
  for c,i in zip(r_code_l,range(len(r_code_l))):
    if c == ';' or c == '{' or c == '}':
      if c == '{': nest+=1;
      if c == '}': nest-=1;
      if not (i == len(r_code_l)-1):
        inter_code.insert(i,c+'\n'+2*nest*' ')
      else: inter_code.insert(i, c)
    else: inter_code.insert(i,c);
  nest = 0;
  inter_code = list(''.join(inter_code));
  for c,i in zip(inter_code,range(len(inter_code))):
    if c == '{': nest +=1;
    if c == '}': nest -=1;
    if c == '\n':
      if i+(1+nest*2) == len(inter_code)-1:
        inter_code.pop(i+1);
        inter_code.pop(i+1);
      elif inter_code[i+(1+nest*2)] == ' ':
        while (i+(1+nest*2) < len(inter_code) and inter_code[i+(1+nest*2)] == ' '):
          inter_code.pop(i+3);
      elif inter_code[i+(1+nest*2)] == '}':
          j = 0;
          while (j < 1*(nest-1)*2):
              inter_code.pop(i+1);
              j+=1;
      elif inter_code[i+(1+nest*2)] == '\n':
          j = 0;
          while (j < 1*(nest)*2):
              inter_code.pop(i);
              j+=1
  return ''.join(inter_code)
# isbn 100%
# aloca 100%
# frequencia 100%
# hacker 100%
# apelidos 100%
# formata 100%
# Cruzamentos 100%
# Futebol 0%
# Horario 0%
# Robot 0%
'''
Podemos usar um (multi) grafo para representar um mapa de uma cidade: cada nó
representa um cruzamento e cada aresta uma rua.

Pretende-se que implemente uma função que lista os cruzamentos de uma cidade
por ordem crescente de criticidade: um cruzamento é tão mais crítico quanto
maior o número de ruas que interliga.

A entrada consistirá numa lista de nomes de ruas (podendo assumir que os nomes
de ruas são únicos).  Os identificadores dos cruzamentos correspondem a letras
do alfabeto, e cada rua começa (e acaba) no cruzamento identificado pelo
primeiro (e último) caracter do respectivo nome.

A função deverá retornar uma lista com os nomes dos cruzamentos por
ordem crescente de criticidade, listando para cada cruzamento um tuplo com o
respectivo identificador e o número de ruas que interliga.  Apenas deverão ser
listados os cruzamentos que interliguem alguma rua, e os cruzamentos com o
mesmo nível de criticidade deverão ser listados por ordem alfabética.
'''

def cruzamentos(ruas):
    res = dict();
    for street in ruas:
        if not street[0] in res:
            res[street[0]] = 1;
        else: res[street[0]] += 1;
        if not street[-1] in res:
            res[street[-1]] = 1;
        else:
            if street[0] != street[-1]:
                res[street[-1]] += 1;
    return sorted(sorted(res.items()),key= lambda x : x[1]);


'''
Neste problema prentede-se que implemente uma função que calcula o rectângulo
onde se movimenta um robot.

Inicialmente o robot encontra-se na posição (0,0) virado para cima e irá
receber uma sequência de comandos numa string.  Existem quatro tipos de
comandos que o robot reconhece:

  'A' - avançar na direcção para o qual está virado
  'E' - virar-se 90º para a esquerda
  'D' - virar-se 90º para a direita
  'H' - parar e regressar à posição inicial virado para cima

Quando o robot recebe o comando 'H' devem ser guardadas as 4 coordenadas
(minímo no eixo dos X, mínimo no eixo dos Y, máximo no eixo dos X, máximo no
eixo dos Y) que definem o rectângulo onde se movimentou desde o início da
sequência de comandos ou desde o último comando 'H'.

A função deve retornar a lista de todas os rectangulos (tuplos com 4 inteiros)
'''

def robot(comandos):
    pos = (0,0)
    dir_curr = (0,1);
    a = b = c = d = 0;
    rs = list();
    for com in comandos:
        if (com == 'A'):
            pos = tuple(map(lambda i, j: i + j, pos, dir_curr))
            x,y = pos;
            if x < a: a = x;
            if y < b: b = y;
            if x > c: c = x;
            if y > d: d = y;
        if (com == 'E'):
            x,y = dir_curr;
            if x != 0: dir_curr = (0,x);
            elif y != 0: dir_curr = (-y,0);
        if (com == 'D'):
            x,y = dir_curr;
            if x != 0: dir_curr = (0,-x);
            elif y != 0: dir_curr = (y,0);
        if (com == 'H'):
            pos = (0,0)
            dir_curr = (0,1);
            thing = (a,b,c,d);
            rs.append(thing);
            a = b = c = d = 0;
    return rs;
"""

Implemente uma função que calcula o horário de uma turma de alunos.  A função
recebe dois dicionários, o primeiro associa a cada UC o respectivo horário (um
triplo com dia da semana, hora de início e duração) e o segundo associa a cada
aluno o conjunto das UCs em que está inscrito. A função deve devolver uma lista
com os alunos que conseguem frequentar todas as UCs em que estão inscritos,
indicando para cada um desses alunos o respecto número e o número total de
horas semanais de aulas. Esta lista deve estar ordenada por ordem decrescente
de horas e, para horas idênticas, por ordem crescente de número.

"""

def horario(ucs,alunos):
    res = list();
    non = list();
    alunos_it = iter(alunos)
    aluno = next(alunos_it, "end");
    while aluno != "end":
        horario = {};
        ucs_aluno_it = iter(alunos[aluno])
        uc = next(ucs_aluno_it, "end");
        flag_res = 0;
        while uc != "end" and flag_res != 1:
            if uc not in ucs:
                non.append(aluno)
                flag_res = 1
            else:
                i = 0;
                flag_inner = 0;
                while i < ucs[uc][2] and flag_inner != 1:
                    if (ucs[uc][0], ucs[uc][1]+i) in horario.keys():
                        non.append(aluno)
                        flag_inner = 1
                    else:
                        horario[ucs[uc][0],ucs[uc][1]+i] = uc
                    i+=1;
            uc = next(ucs_aluno_it, "end")
        if aluno not in non:
            res.append((aluno,len(horario.keys())))
        aluno = next(alunos_it, "end")
    return sorted(sorted(res), key = lambda t: t[1], reverse=True)


def main():
    print("<h3>robot</h3>")
    cs = "EEAADAAAAAADAAAADDDAAAHAAAH"
    print("in:",cs)
    print("out:",robot(cs))

if __name__ == '__main__':
  main();
