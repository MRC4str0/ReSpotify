<h1 align="center"> ReSpotify </h1>

<h3 align="center"> Projeto Python para reorganizar playlists no Spotify </h3>
  <p>
    Criei este projeto no intuito de reordenar minhas playlist no Spotify, visto que manualmente (como proposto pelo app) seria um sofrimento, uma vez que há mesma possui mais de 1000 musicas...
  </p>
  
<h1 align="center">
  <img align="center" src="https://i.pinimg.com/564x/73/0e/89/730e89414d4329ef2eec70b3fb679270.jpg" width = 400 height = 400>
</h1>

> ***NOTA***: Este é um produto experimental de estudo pessoal, portanto não esta totalmento modelado, entretanto busco melhorá-lo em conformidade do tempo!

<br>

<h1 align="center"> 🎵 Vamos Começar! 🎵 </h1>
<p>
  Os requisitos do projeto podem ser encontrados em <a href="https://github.com/MRC4str0/ReSpotify/blob/main/requisitos.txt">requisitos.txt</a>

  ```text
  pyinstaller==5.7.0
  spotipy==2.22.1
  termcolor==2.2.0
  ```
</p>

<br>

<p>
  A biblioteca utilizada neste projeto foi <a href="https://github.com/Spotipy">Spotipy</a> e seus requisitos de uso são:
  
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
