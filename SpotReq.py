import spotipy
from spotipy.oauth2 import SpotifyOAuth


class SpotReq:

    def __init__(self, client_id, client_secret):

        self.scope = ('playlist-read-private', 'playlist-modify-public', 'user-read-private')
        self.redirect_uri = r'https://open.spotify.com/'
        self.client_id = client_id
        self.client_secret = client_secret

        self.auth()


    def auth(self):

        try:
            OAuth = SpotifyOAuth(self.client_id, self.client_secret, self.redirect_uri, scope = self.scope)
            self.sp = spotipy.Spotify(auth_manager = OAuth)
            self.username = self.sp.current_user()['display_name']

        except Exception as Error:
            
            msg = f'Erro de Autenticação\nErro: {Error}'
            return msg


    def scanner(self, playlist_url):

        plist_dict = dict()    

        while self.sp.user_playlist(self.username, playlist_url)['tracks']['total'] != 0:

            list_uri_del = list()
            results = self.sp.user_playlist_tracks(self.username, playlist_url)
                
            for track in results['items']:

                N_Artista = track['track']['artists'][0]['name']
                N_Album = track['track']['album']['name']
                N_Musica = track['track']['name']
                N_Uri = track['track']['uri']

                if N_Artista not in plist_dict.keys():
                    plist_dict[N_Artista] = {}

                if N_Album not in plist_dict[N_Artista].keys():
                    plist_dict[N_Artista][N_Album] = {}

                if N_Uri not in plist_dict[N_Artista][N_Album].keys():
                    plist_dict[N_Artista][N_Album][N_Uri] = N_Musica

                list_uri_del.append(N_Uri)
                plist_dict[N_Artista][N_Album][N_Uri] = N_Musica

            self.sp.user_playlist_remove_all_occurrences_of_tracks(self.username, playlist_url, list_uri_del)

        return plist_dict


    def add_playlist(self, list_id, playlist_url):

        demo_list = list()

        for id in list_id:
            demo_list.append(id)

            if len(demo_list) == 100 or list_id[-1] == id:
                self.sp.user_playlist_add_tracks(self.username, playlist_url, demo_list)
                demo_list.clear()

    
    def TipoPlaylist(self, tipo, plist_dict):

        self.list_uri = list()

        def Acs_C():
            for artista in sorted(plist_dict):
                for album in sorted(plist_dict[artista]):
                    for uri in plist_dict[artista][album]:
                        self.list_uri.append(uri)


        def Dcs_C():
            for artista in sorted(plist_dict, reverse = True):
                for album in sorted(plist_dict[artista], reverse = True):
                    for uri in plist_dict[artista][album]:
                        self.list_uri.append(uri)

                    
        def Aleatorio():
            from random import sample

            for artista in plist_dict:
                for album in plist_dict[artista]:
                    for uri in plist_dict[artista][album]:
                        self.list_uri.append(uri)

            self.list_uri = sample(self.list_uri, k = len(self.list_uri))  


        if tipo == 1:
            Acs_C()

        elif tipo == 2:
            Dcs_C()

        elif tipo == 3:
            Aleatorio()

        return self.list_uri


    def _getDados(self, playlist_url):

        results = self.sp.user_playlist(self.username, playlist_url)
        Titulo_playlist = results['name']
        Descri_playlist = results['description']
        Tracks_playlist = results['tracks']['total']
        Public_playlist = results['public']

        return {'nome':Titulo_playlist, 'descri':Descri_playlist, 'tracks':Tracks_playlist, 'public':Public_playlist}