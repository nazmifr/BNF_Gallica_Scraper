# Simple Gallica BNF scraper for offline scan download (outdated ereaders, ...)
# https://github.com/nazmifr/BNF_Gallica_Scraper/
# TODO: Cookies, UserAgent, automatic url parsing

import wget

fraum = 1 # 1st page to download
tou = 500 # Last page to download (overshoot is not an issue, will just add blank files)
part1 = 'https://gallica.bnf.fr/ark:/12148/bpt6k408619m/f'  # exemple: couper la zone après f (folio ?) '4.highres' 'https://gallica.bnf.fr/ark:/12148/bpt6k408619m/f4.highres'

while fraum <= tou:
    no = str(fraum)
    part2 = '.highres'
    noext = no + ".jpg"
    fraum = fraum + 1
    image_url = part1 + no + part2
    print('\r\npage ', fraum, '/', tou)
    local_image_filename = wget.download(image_url, out=noext)
    

