import pathlib
import shutil

emoji_animal = {
    'ant': '🐜',
    'chick': '🐤',
    'camel': '🐫',
    'bat': '🦇',
    'bird': '🐦',
    'bison': '🦬',
    'blowfish': '🐡',
    'bug': '🐛',
    'cat': '🐈',
    'chipmunk': '🐿️',
    'cow': '🐄',
    'crab': '🦀',
    'cricket': '🦗',
    'crocodile': '🐊',
    'deer': '🦌',
    'dodo': '🦤',
    'dog': '🐕',
    'dolphin': '🐬',
    'dromedary': '🐪',
    'duck': '🦆',
    'eagle': '🦅',
    'elephant': '🐘',
    'fish': '🐟',
    'flamingo': '🦩',
    'giraffe': '🦒',
    'goat': '🐐',
    'gorilla': '🦍',
    'hedgehog': '🦔',
    'hippopotamus': '🦛',
    'honeybee': '🐝',
    'horse': '🐎',
    'kangaroo': '🦘',
    'ladybeetle': '🐞',
    'leopard': '🐆',
    'lizard': '🦎',
    'llama': '🦙',
    'lobster': '🦞',
    'mosquito': '🦟',
    'mouse': '🐁',
    'octopus': '🐙',
    'orangutan': '🦧',
    'owl': '🦉',
    'parrot': '🦜',
    'peacock': '🦚',
    'penguin': '🐧',
    'pig': '🐖',
    'poodle': '🐩',
    'rabbit': '🐇',
    'ram': '🐏',
    'rat': '🐀',
    'rhinoceros': '🦏',
    'rooster': '🐓',
    'sauropod': '🦕',
    'scorpion': '🦂',
    'sheep': '🐑',
    'shrimp': '🦐',
    'snail': '🐌',
    'snake': '🐍',
    'squid': '🦑',
    'swan': '🦢',
    't-rex': '🦖',
    'tiger': '🐅',
    'turkey': '🦃',
    'turtle': '🐢',
    'buffalo': '🐃',
    'whale': '🐋'
 }

def save_imgs_animal(size: int):
    """Save all animal emoji images from a given size"""
    assert size in [32, 72, 128, 512]
    src_dir = pathlib.Path(f'/home/jurandy/Projetos/3rd/GoogleFonts/noto-emoji/png/{size}')
    tmpl_img = 'emoji_u{code}.png'
    pngs_path = pathlib.Path(__file__).parent / 'images' / 'png' / str(size)
    pngs_path.mkdir(parents=True, exist_ok=True)
    for animal,emoji in emoji_animal.items():
        hex_code = hex(ord(emoji[0]))[2:]
        src_img = src_dir / tmpl_img.format(code=hex_code)
        if src_img.exists():
            dst_img = pngs_path / f'{animal}.png'
            shutil.copy(src_img, dst_img)