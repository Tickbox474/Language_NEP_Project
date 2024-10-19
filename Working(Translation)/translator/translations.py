# translator/translations.py

data = [
    {'english': 'hello', 'mandarin': '你好', 'pronunciation': 'nǐ hǎo', 'malay': 'halo'},
    {'english': 'goodbye', 'mandarin': '再见', 'pronunciation': 'zài jiàn', 'malay': 'selamat tinggal'},
    {'english': 'please', 'mandarin': '请', 'pronunciation': 'qǐng', 'malay': 'tolong'},
    {'english': 'thank you', 'mandarin': '谢谢', 'pronunciation': 'xiè xiè', 'malay': 'terima kasih'},
    {'english': 'yes', 'mandarin': '是', 'pronunciation': 'shì', 'malay': 'ya'},
    {'english': 'no', 'mandarin': '不', 'pronunciation': 'bù', 'malay': 'tidak'},
    {'english': 'sorry', 'mandarin': '抱歉', 'pronunciation': 'bào qiàn', 'malay': 'maaf'},
    {'english': 'excuse me', 'mandarin': '打扰了', 'pronunciation': 'dǎ rǎo le', 'malay': 'maafkan saya'},
    {'english': 'how are you', 'mandarin': '你好吗', 'pronunciation': 'nǐ hǎo ma', 'malay': 'apa khabar'},
    {'english': 'good morning', 'mandarin': '早安', 'pronunciation': 'zǎo ān', 'malay': 'selamat pagi'},
    {'english': 'good night', 'mandarin': '晚安', 'pronunciation': 'wǎn ān', 'malay': 'selamat malam'},
    {'english': 'friend', 'mandarin': '朋友', 'pronunciation': 'péng yǒu', 'malay': 'kawan'},
    {'english': 'food', 'mandarin': '食物', 'pronunciation': 'shí wù', 'malay': 'makanan'},
    {'english': 'water', 'mandarin': '水', 'pronunciation': 'shuǐ', 'malay': 'air'},
    {'english': 'family', 'mandarin': '家庭', 'pronunciation': 'jiā tíng', 'malay': 'keluarga'},
    {'english': 'school', 'mandarin': '学校', 'pronunciation': 'xué xiào', 'malay': 'sekolah'},
    {'english': 'teacher', 'mandarin': '老师', 'pronunciation': 'lǎo shī', 'malay': 'guru'},
    {'english': 'student', 'mandarin': '学生', 'pronunciation': 'xué shēng', 'malay': 'pelajar'},
    {'english': 'love', 'mandarin': '爱', 'pronunciation': 'ài', 'malay': 'cinta'},
    {'english': 'happy', 'mandarin': '幸福', 'pronunciation': 'xìng fú', 'malay': 'gembira'},
    {'english': 'sad', 'mandarin': '悲伤', 'pronunciation': 'bēi shāng', 'malay': 'sedih'},
    {'english': 'angry', 'mandarin': '生气', 'pronunciation': 'shēng qì', 'malay': 'marah'},
    {'english': 'beautiful', 'mandarin': '美丽', 'pronunciation': 'měi lì', 'malay': 'cantik'},
    {'english': 'big', 'mandarin': '大', 'pronunciation': 'dà', 'malay': 'besar'},
    {'english': 'small', 'mandarin': '小', 'pronunciation': 'xiǎo', 'malay': 'kecil'},
    {'english': 'hot', 'mandarin': '热', 'pronunciation': 'rè', 'malay': 'panas'},
    {'english': 'cold', 'mandarin': '冷', 'pronunciation': 'lěng', 'malay': 'sejuk'},
    {'english': 'day', 'mandarin': '日', 'pronunciation': 'rì', 'malay': 'hari'},
    {'english': 'night', 'mandarin': '夜晚', 'pronunciation': 'yè wǎn', 'malay': 'malam'},
    {'english': 'house', 'mandarin': '房子', 'pronunciation': 'fáng zi', 'malay': 'rumah'},
    {'english': 'car', 'mandarin': '汽车', 'pronunciation': 'qì chē', 'malay': 'kereta'},
    {'english': 'bicycle', 'mandarin': '自行车', 'pronunciation': 'zì xíng chē', 'malay': 'basikal'},
    {'english': 'book', 'mandarin': '书', 'pronunciation': 'shū', 'malay': 'buku'},
    {'english': 'pen', 'mandarin': '笔', 'pronunciation': 'bǐ', 'malay': 'pen'},
    {'english': 'chair', 'mandarin': '椅子', 'pronunciation': 'yǐ zi', 'malay': 'kerusi'},
    {'english': 'table', 'mandarin': '桌子', 'pronunciation': 'zhuō zi', 'malay': 'meja'},
    {'english': 'door', 'mandarin': '门', 'pronunciation': 'mén', 'malay': 'pintu'},
    {'english': 'window', 'mandarin': '窗户', 'pronunciation': 'chuāng hù', 'malay': 'tingkap'},
    {'english': 'cat', 'mandarin': '猫', 'pronunciation': 'māo', 'malay': 'kucing'},
    {'english': 'dog', 'mandarin': '狗', 'pronunciation': 'gǒu', 'malay': 'anjing'},
    {'english': 'bird', 'mandarin': '鸟', 'pronunciation': 'niǎo', 'malay': 'burung'},
    {'english': 'fish', 'mandarin': '鱼', 'pronunciation': 'yú', 'malay': 'ikan'},
    {'english': 'tree', 'mandarin': '树', 'pronunciation': 'shù', 'malay': 'pokok'},
    {'english': 'flower', 'mandarin': '花', 'pronunciation': 'huā', 'malay': 'bunga'},
    {'english': 'mountain', 'mandarin': '山', 'pronunciation': 'shān', 'malay': 'gunung'},
    {'english': 'river', 'mandarin': '河', 'pronunciation': 'hé', 'malay': 'sungai'},
    {'english': 'ocean', 'mandarin': '海洋', 'pronunciation': 'hǎi yáng', 'malay': 'lautan'},
    {'english': 'sky', 'mandarin': '天空', 'pronunciation': 'tiān kōng', 'malay': 'langit'},
    {'english': 'sun', 'mandarin': '太阳', 'pronunciation': 'tài yáng', 'malay': 'matahari'},
]

def translate(text, source_lang, target_lang):

    text = text.lower()

    translation_dict = {word['english'].lower(): word for word in data}


    if source_lang == 'en':

        if target_lang == 'zh':

            return translation_dict.get(text, {}).get('mandarin', 'Translation not found')

        elif target_lang == 'ms':

            return translation_dict.get(text, {}).get('malay', 'Translation not found')


    elif source_lang == 'zh':

        for word in data:

            if word['mandarin'].lower() == text:

                return word['english'] if target_lang == 'en' else word['malay']

    

    elif source_lang == 'ms':

        for word in data:

            if word['malay'].lower() == text:

                return word['english'] if target_lang == 'en' else word['mandarin']


    return 'Translation not found'