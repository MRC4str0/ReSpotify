<h1 align="center"> ReSpotify </h1>

<h3 align="center"> Projeto Python para reorganizar playlists no Spotify </h3>
  <p>
    Criei este projeto no intuito de reordenar minhas playlist no Spotify, visto que manualmente (como proposto pelo app) seria um sofrimento, uma vez que há mesma possui mais de 1000 musicas...
  </p>
  
<h1 align="center">
  <img align="center" src="https://docs.google.com/uc?id=1-JdaSCIZ3941nWlYhnR5Ej04r0fZIRMG" weight = 600 height= 500>
</h1>

> ***NOTA***: Este é um produto experimental de estudo pessoal, portanto não esta totalmento modelado, entretanto busco melhorá-lo em conformidade do tempo!

<br>

<h1 align="center"> 🎵 Vamos Começar! 🎵 </h1>
<p>
  Os requisitos do projeto podem ser encontrados em <a href="https://github.com/MRC4str0/ReSpotify/blob/main/requisitos.txt">requisitos.txt</a>

  ```text
  spotipy==2.22.1
  termcolor==2.2.0
  ```
</p>

<br>

<p>
  A biblioteca utilizada neste projeto foi <a href="https://github.com/spotipy-dev/spotipy">Spotipy</a> e seus requisitos de uso são:
  
  * ***Client Id***
  * ***Client Secret***
  
  Esses dados você adquiri registrando um App em <a href="https://developer.spotify.com/dashboard/">My Dashboard</a> no Spotify para Developers!
  <br><br>
  Feito isso, é preciso adicionar esses dados em <a href="https://github.com/MRC4str0/ReSpotify/blob/main/Secrets.py">Secrets.py</a>
  <br>
  ```python
  cred = {'client_id':'Seu Client Id',
        'client_secret':'Seu Client Secret'}
  ```
</p>

<br>

> ***NOTA***: Outro dado importante é a ***URL de redirecionamento***! Ao acessar as configurações do seu App, adicione <code>https://open.spotify.com/</code> como sua URL de redirecionamento!
> Esta é a URL que você será redirecionado após permitir o acesso de dados ao ReSpotify!

<br>

<h1 align="center"> ✏ Guia de Uso! ✏ </h1>

> O programa em si é auto-explicativo, entretanto por via de duvidas, segue abaixo um mini-guia!

<br>

<p>

  * Ao executar o arquivo <a href="https://github.com/MRC4str0/ReSpotify/blob/main/ReSpotify.py">ReSpotify.py<a>, será requisitado a URL da playlist (A qual deseja Reordenar):
  
</p>

<img align="center" src="https://docs.google.com/uc?id=1_4WFvEJdq352eiwmWhL0A8C9NOCtE-8C" weight = 400 height = 400>

<br>

<p>

  * Caso sejá sua primeira vez executando o arquivo, ele pedirá acesso as informações do seu Spotify. Após aceitar, copie a URL em que você foi redirecionado e cole no terminal!
  
</p>

<img align="center" src="https://docs.google.com/uc?id=1uuXAuSNguqpOXsHVCapGmsZbBTo399Hq" weight = 400 height = 400>

> Enquanto isso, é gerado um arquivo de cache, que vai salvar suas permissões, para que você não tenha o trabalho de permirtir toda vez!

<br>

<p>

  * Logo após, caso a URL for valida, ele apresentará as informações da sua Playlist:
  
</p>

<img align="center" src="https://docs.google.com/uc?id=160F78dHVvVK1M8nKxfU8o34kECqP94gr" weight = 400 height = 400>

> Confira se a playlist selecionada é a desejada! Os passos a seguir são ***IRREVERSSIVEIS!***

<br>

<p>

  * Depois de confirmado a playlist, escolha uma das opções de rearranjo:
  
</p>

<img align="center" src="https://docs.google.com/uc?id=10ulZpR7y22wZq-kLcT0snlpY1MaDoKd2" weight = 400 height = 400>

> Escolha com certeza! Como dito anteriormente, são mudanças ***IRREVERSSIVEIS!***

<br>

<p>

  * Feito sua escolha, basta aguardar que as mudanças estão sendo feitas!

</p>

<img align="center" src="https://docs.google.com/uc?id=1-JdaSCIZ3941nWlYhnR5Ej04r0fZIRMG" weight = 400 height= 400>

<br>

<h1 align="center">🏁 FIM! 🏁</h1>

<p>
  Enfim chegamos ao fim do projeto... Sobrou agora alguns pontos que devo tirar nota!
</p>

<br>

<h3 align="center"> Melhorias </h3>
  
<p>  
  Este é um projeto de estudo! Fiz no intuito maior de adiciona-lo ao meu repertório e aprimora-lo com tempo e estudo!
  Caso tenha alguma ideia de implementação ou queira reportar algum problema, porfavor não exite!
</p>

<div id="badges" align="center">

  <a href="https://github.com/MRC4str0">
    <img src="https://avatars.githubusercontent.com/u/68367411?v=4" weight = 170 height = 170>
  </a>

  <br>

  <a href="https://www.instagram.com/mrcastr.0/?next=%2F">
    <img src="https://img.shields.io/static/v1?label=Instagram&message=@mrcastr.0&color=grey&style=for-the-badge&logo=Instagram"/>
  </a>
  
  <a href="https://www.linkedin.com/in/felipe-de-castro-pereira-29118225b">
    <img src="https://img.shields.io/static/v1?label=Linkedin&message=@Felipe%20de%20Castro&color=grey&style=for-the-badge&logo=Linkedin"/>
  </a>
  
  <a href="https://wa.me/qr/E3VI3L2U5RWUI1">
    <img src="https://img.shields.io/static/v1?label=WhatsApp&message=@Felipe%20de%20Castro&color=grey&style=for-the-badge&logo=WhatsApp"/>
  </a>
  
</div>
