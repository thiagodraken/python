### API de geração de Thumbnails usando o módulo Pillow

from PIL import Image
from urllib.request import urlopen, Request

def gerarThumbnail(url):

    # Configuração necessária para que o urllib não retorne um erro 403
    req = Request(url, headers={'User-Agent' : "Magic Browser"})
    imagem = Image.open(urlopen(req))

    '''
    # Método 1: Reduz a imagem nos padrões definidos, mas respeita a proporção
    # Descartado, pois não gera imagens de tamanho exato
    imagem.thumbnail((400, 400))
    imagem.save('thumbnail.png')
    '''

    # Método 2: Ajusta a imagem no tamanho exato que foi definido, ignorando a proporção
    # Sendo usado atualmente, por produzir resultados mais precisos
    nova_imagem = imagem.resize((400, 400))
    nova_imagem.save('thumbnail.png')
