Minesweeper Game em Python com OOP e Tkinter
Este projeto implementa uma versão funcional e responsiva do clássico Minesweeper (Campo Minado), desenvolvida inteiramente em Python com paradigma de programação orientada a objetos (OOP) e interface gráfica construída com Tkinter.

Visão Geral
A aplicação foi projetada com uma arquitetura modular, promovendo separação de responsabilidades e reuso de código, utilizando classes para encapsular lógica do jogo,
manipulação de células, eventos gráficos e controle de estado. A interface foi construída com os componentes nativos do Tkinter.

Este projeto é ideal como exemplo de:

Aplicação do paradigma OOP em Python;

Manipulação de GUI com tkinter;

Controle de eventos e redimensionamento dinâmico;

Estruturação de código para conversão em executável com ferramentas como auto-py-to-exe.

Tecnologias e Bibliotecas
Python ≥ 3.8

Tkinter (GUI nativa do Python)

Random (para distribuição das minas)

auto-py-to-exe (sugerido para empacotamento)

Executando o Projeto
Clone o repositório:
git clone https://github.com/Mirandadev2024/minesweepercompython
cd para o diretório criado
Execute o jogo:

python main.py
Certifique-se de que seu ambiente Python tenha suporte ao Tkinter (instalado por padrão na maioria das distribuições).


Conversão em Executável
Este projeto pode ser facilmente empacotado com auto-py-to-exe, permitindo distribuição como executável .exe para Windows:

Instale o empacotador:

pip install auto-py-to-exe
Inicie o empacotador com:

auto-py-to-exe
No assistente gráfico, selecione:

Script: main.py

No check-box, selecione One file.

Desmarque Console: (caso deseje ocultar o terminal).

Adicione recursos gráficos, se houver (ícones, assets).

Funcionalidades:

Geração aleatória de minas ao iniciar a partida.

Descoberta recursiva de células vazias.

Contador de minas restantes.

Condições de vitória e derrota.

Aprendizado e Aplicações:

Este projeto é altamente didático e pode ser utilizado para fins educacionais em cursos de:

Programação Orientada a Objetos com Python;

Interfaces Gráficas com Tkinter;

Lógica de Jogos e Design Modular e Engenharia de Software.

Licença:

Este projeto pode ser utilizado para fins acadêmicos e pessoais. Consulte o arquivo LICENSE para mais detalhes.
