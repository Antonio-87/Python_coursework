import time

from tqdm import tqdm

from vk_classes import VkUser

from ya_classes import YaUploader
 
def Backup_photo(number_photos=5):
    '''
    Копирует фотографии максимального размера по пикселям
    и сохраняет данные о них в json-файл
    '''
    user_id = input('Введите id или короткое имя пользователя: ')
    token_ya = input('Введите токен с Полигона Яндекс.Диска: ')
    token_vk = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'
    vk_client = VkUser(token_vk, '5.131')
    result = vk_client.photos_get(user_id)
    uploader = YaUploader(token_ya)
    uploader.create_folder_disk("VK_photo")
    file_backup_list = []
    url_backup_list = []
    new_file_backup_list = []
    for data in tqdm(result):
        time.sleep(1)        
        type = ','.join([str(max(r['type'], key=lambda i : i[0])) for r in data['sizes']])
        file_name_dict = {'file_name': f"{data['likes']['count']}.jpg"}
        file_name_dict['size'] = type[-1]   
        file_backup_list.append(file_name_dict)
        url = ','.join([str(r['url']) for r in data['sizes'] if r['type'] == type[-1]])
        url_backup_list.append(url)
    for id, combo in tqdm(enumerate(zip(file_backup_list,url_backup_list), 1)):
        time.sleep(1)
        if id <= number_photos:            
            uploader.upload_photo(f"VK_photo/{combo[0]['file_name']}.jpg",combo[1])
            new_file_backup_list.append(combo[0])
        else:
            break
    uploader.create_file(new_file_backup_list)

Backup_photo()