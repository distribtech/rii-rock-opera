from pathlib import Path
import json, html

p = Path(__file__).resolve().parent
tracks = json.loads((p/'opera_tracks.json').read_text())
esc = html.escape
common = ('Ukrainian-language contemporary chamber opera, classical operatic singing, '
          'clear Ukrainian diction, through-composed theatrical scene, acoustic strings, '
          'bass clarinet, low brass, restrained analog electronic pulse, spacious concert hall, '
          'dramatic dynamic contrasts, no pop song structure, no spoken narration. ')
parts = ['''<!doctype html><html lang="uk"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Порожній престол — опера</title><style>
*{box-sizing:border-box}body{margin:0;background:#101317;color:#e5e5e2;font:17px/1.65 system-ui,sans-serif}
main{max-width:1000px;margin:auto;padding:42px 24px}h1{font-size:clamp(38px,7vw,72px);line-height:1.05;margin:.3em 0;color:#edcb83}h2{color:#edcb83;line-height:1.25}h3{margin-bottom:8px}a{color:#88d3db}nav{display:flex;gap:16px;flex-wrap:wrap;padding:24px 0;border-bottom:1px solid #45494f}section{margin:44px 0}pre{white-space:pre-wrap;overflow-wrap:anywhere;font:16px/1.65 system-ui;background:#1a2028;padding:24px;border-radius:8px}summary{cursor:pointer;color:#edcb83;font-size:21px;padding:18px 0}details{border-bottom:1px solid #45494f}.muted{color:#aeb5bd}.gallery{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px}.gallery img{width:100%;display:block}.gallery figure{margin:0}.gallery figcaption{font-size:14px;color:#aeb5bd}.tag{letter-spacing:.2em;font-size:13px;color:#88d3db}button{border:1px solid #64737c;background:#25303a;color:white;padding:9px 14px;border-radius:6px;cursor:pointer}video{width:100%;max-height:500px}footer{padding:32px 0;color:#aeb5bd;font-size:14px}
</style><main><div class="tag">КАМЕРНА КІБЕРОПЕРА · 3 ДІЇ · 10 НОМЕРІВ</div>
<h1>Порожній<br>престол</h1><p>Опера про хор, який вигадав Суддю.</p>
<p class="muted">Українське лібрето, блоки для Suno, переказ відео та візуальні матеріали.</p>
<nav><a href="#tracks">Лібрето й Suno</a><a href="#analysis">Аналіз</a><a href="#gallery">Ілюстрації</a><a href="#workflow">Як генерувати</a><a href="video_original_ru.mp4">Відео: оригінальна доріжка</a></nav>
<section><p>Суддя не має власного голосу. На порожньому престолі звучить лише відлуння хору.</p><p>Почни генерацію з №02, щоб знайти основний голос і музичний образ зв'язку. Потім збирай номери в порядку 01–10. Аудіо в Suno ще не згенероване.</p></section>
<section id="tracks"><h2>Лібрето й готові блоки Suno</h2>''']
for n,t in enumerate(tracks,1):
    parts.append(f'<details><summary>{esc(t["title"])}</summary><p class="muted">{esc(t["act"])} · {esc(t["voice"])} · орієнтир {esc(t["duration"])}</p>')
    for field,body in [('Style',common+t['style']),('Lyrics',t['lyrics'])]:
        ident=f'{field}{n}'
        parts.append(f'<h3>{field}</h3><button onclick="copyBlock(\'{ident}\',this)">Копіювати {field}</button><pre id="{ident}">{esc(body)}</pre>')
    parts.append(f'<p><a href="SUNO_TRACKS/{n:02}_SUNO.txt">Відкрити текстовий блок</a></p></details>')
parts.append('</section><section id="analysis"><h2>Переказ і художня оцінка</h2><pre>'+esc((p/'02_ANALYSIS_UA.md').read_text())+'</pre></section>')
parts.append('<section id="gallery"><h2>Ілюстрації з відео</h2><p>12 кадрів із таймкодами. Натисни, щоб відкрити файл.</p><p><a href="illustrations/CONTACT_SHEET.jpg">Контактний аркуш усіх кадрів</a></p><div class="gallery">')
for f in sorted((p/'illustrations').glob('[0-9]*.jpg')):
    parts.append(f'<figure><a href="illustrations/{f.name}"><img loading="lazy" src="illustrations/{f.name}" alt="{esc(f.stem)}"></a><figcaption>{esc(f.stem)}</figcaption></figure>')
parts.append('</div></section><section id="workflow"><h2>Порядок роботи в Suno</h2><pre>'+esc((p/'05_SUNO_WORKFLOW_UA.md').read_text())+'</pre></section>')
if (p/'06_ASR_STATUS.md').exists():
    parts.append('<section><h2>Звіт локального Whisper</h2><pre>'+esc((p/'06_ASR_STATUS.md').read_text())+'</pre></section>')
parts.append('''<footer>Оригінальне лібрето; джерельне відео та кадри — «ВЕЛИКОХАТСКИЙ | НАУКА». Повна дослівна транскрипція не включена. Артефакти створені для підготовки опери.</footer></main>
<script>async function copyBlock(id,b){let t=document.getElementById(id).innerText;try{await navigator.clipboard.writeText(t);b.textContent='Скопійовано'}catch(e){let r=document.createRange();r.selectNodeContents(document.getElementById(id));let s=getSelection();s.removeAllRanges();s.addRange(r);b.textContent='Текст виділено — Ctrl+C'}}</script></html>''')
(p/'START.html').write_text('\n'.join(parts),encoding='utf-8')
print('START.html created')
