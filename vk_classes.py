import requests

class VkUser:
    url = 'https://api.vk.com/method/'
    def __init__(self, token, version):
        self.params = {
            'access_token': token,
            'v': version    
        }

    def users_get(self, user_id ):
        '''
        Возвращает id, если ввести id или короткое имя пользователя
        '''
        group_search_url = self.url + 'users.get'
        group_search_params = {'user_id': user_id}
        res = requests.get(group_search_url, params={**self.params, **group_search_params}).json()
        res_id = ','.join([str(r['id']) for r in list(res.values())[0]])
        return(res_id)


    def photos_get(self, user_id):
        '''
        Возвращает список фотографий в альбоме       
        '''
        group_search_url = self.url + 'photos.get'
        group_search_params = {
            'owner_id': self.users_get(user_id),
            'album_id': 'profile',
            'extended': 1,
        }
        req = requests.get(group_search_url, params={**self.params, **group_search_params}).json()              
        return req['response']['items']
        
         