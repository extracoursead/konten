import sys, pathlib, shutil
from playwright.sync_api import sync_playwright
here=pathlib.Path(__file__).resolve().parent; N=911
fr=here/'ovf'
keys=[int(x) for x in sys.argv[1:]]
if not keys: shutil.rmtree(fr,ignore_errors=True); fr.mkdir()
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920})
    pg.goto(f'file://{here}/ov.html'); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(500)
    for i in (keys or range(N)):
        pg.evaluate(f'render({i})')
        pg.screenshot(path=str((here/f'key{i}.png') if keys else fr/f'{i:04d}.png'),omit_background=True)
    b.close()
