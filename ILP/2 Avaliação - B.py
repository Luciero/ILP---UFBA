Q = int(input());

ver = 0;
azu = 0;
ama = 0;

if(Q % 3 == 0):
  ver = (Q // 3);
  azu = (Q // 3);
  ama = (Q // 3);
  print('Vermelho',ver);
  print('Azul',azu);
  print('Amarelo',ama);

if (Q % 3 == 1):
  ver = (Q // 3) + 1;
  azu = ver - 1;
  ama = ver - 1;
  print('Vermelho',ver);
  print('Azul',azu);
  print('Amarelo',ama);

if (Q % 3 == 2):
  ver = (Q // 3) + 1;
  azu = (Q // 3) + 1;
  ama = azu - 1;
  print('Vermelho',ver);
  print('Azul',azu);
  print('Amarelo',ama);
