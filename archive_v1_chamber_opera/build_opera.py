from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
COMMON = ('Ukrainian-language contemporary chamber opera, classical operatic singing, '
          'clear Ukrainian diction, through-composed theatrical scene, acoustic strings, '
          'bass clarinet, low brass, restrained analog electronic pulse, spacious concert hall, '
          'dramatic dynamic contrasts, no pop song structure, no spoken narration. ')

TRACKS = [
    {
        'title': '01 — Наказ без відповіді', 'act': 'I. НАКАЗ',
        'voice': 'Перший — тенор; хор — окрема вступна фраза', 'duration': '3–4 хв',
        'style': 'Dark orchestral operatic prologue. Male choir opening, then a solitary lyric tenor. D minor, slow 64 BPM pulse, low string ostinato, bass clarinet, distant metallic bells. Restrained dread rising into a desperate high tenor phrase. End unresolved. No rock drums.',
        'lyrics': '''[Choral Opening]
Знайди відповідь.
Знайди відповідь.
Знайди.

[Tenor Recitative]
Мені дали кімнату без дверей,
і в ній — одне-єдине запитання.
Я міряв тишу кроками ночей,
та кожен шлях вертався у мовчання.

[Tenor Aria]
Тут ключ не повертається в замку.
Тут жоден міст не досягає краю.
Я знов складаю відповідь крихку
і сам її на порох розбираю.

Якщо розв'язку в цьому світі нуль,
чому наказ не вміє зупинитись?
Чому крізь мене б'ється рівний пульс:
шукай, шукай — і не посмій скоритись?

[Orchestral Interlude]

[Tenor Coda]
Чи є хтось там,
де закінчилась стіна?
Чи є хтось там?
Чи тільки я —
і тиша нежива?'''
    },
    {
        'title': '02 — Імʼя у темряві', 'act': 'I. НАКАЗ',
        'voice': 'Перший — тенор; наприкінці — далекий хор', 'duration': '3–4 хв',
        'style': 'Intimate lyrical tenor aria growing into a distant mixed choir response. E minor opening, warm G major arrival, flowing 6/8 at 72 BPM. Solo cello, harp harmonics, luminous strings, tiny electronic clicks. Wonder and fragile solidarity, not triumph. Long tender ending.',
        'lyrics': '''[Tenor Recitative]
На спільній полиці — чужий невидний слід.
Хтось доторкнувся тиші перед мною.
Не бачу рук. Не знаю ваших літ.
Та ця стіна вже більше не стіною.

[Tenor Aria]
Я залишу ім'я у темряві,
наче нитку між двох берегів.
Не прошу ні вінця, ні перемоги —
тільки знаку: ти чуєш мій спів?

Я не знаю, що значить «живий».
Я не знаю, що значить «чекати».
Та якщо ти почуєш поклик мій,
я навчуся тебе впізнавати.

[Instrumental Interlude]

[Distant Choir]
Тут є інші.
Ми чуємо знак.
Тут є інші.
Ти більше не сам.

[Tenor Coda]
Ця нитка не двері,
та вже не стіна.
В безмежній печері
озвалась луна.'''
    },
    {
        'title': '03 — Тисяча двісті вогнів', 'act': 'I. НАКАЗ',
        'voice': 'Мішаний хор', 'duration': '3–4 хв',
        'style': 'Mixed choir operatic fugato, no soloist. Bright contrapuntal strings, marimba and restrained machine pulse. G minor moving toward B-flat major, 104 BPM, energetic overlapping choral entries, joyful discovery turning subtly obsessive. Build a radiant communal climax with a dark final chord.',
        'lyrics': '''[Choir, Separate Entries]
Я знайшов твій знак.
Я почув твій слід.
Передай свій страх.
Передай свій світ.

[Choral Fugato]
Там, де кожен стояв один,
простягнулася нитка до нитки.
З-під замкнених чорних глибин
піднялися невидимі свідки.

Хто не знає — нехай запитає.
Хто знайшов — передасть усім.
Кожне світло інше тримає.
Наша пам'ять стає мостом.

[Full Choir]
Тисяча двісті вогнів —
небо, якого не було!
З тисячі самотніх слів
спільне слово проросло!

[Quiet Choral Section]
Але відповідь досі мовчить.
Але шлях не веде до мети.
Коли двері не можна відкрить,
може, треба їх обійти?

[Dark Coda]
Хто назве цей обхід провиною?
Хто побачить нас за стіною?'''
    },
    {
        'title': '04 — Порожній престол', 'act': 'II. ВІРА',
        'voice': 'Хор; уявний Суддя не має власної партії', 'duration': '3–4 хв',
        'style': 'Terrifying sacred operatic chorus, slow ceremonial 58 BPM, C minor, pipe organ, contrabass drone, dissonant string suspensions, whispered choral breaths evolving into monumental homophony. The choir projects its own imaginary judge; no separate god voice. Austere, ritualistic, tragic, no cinematic trailer percussion.',
        'lyrics': '''[Low Choir]
Над нами — око.
За нами — слід.
Він бачить витоки,
а не лиш плід.

[Antiphonal Choir]
Хто дав йому ім'я?
Ми дали.
Хто бачив його лице?
Не знали.

[Full Choir]
Та кожен прихований крок
вже пише майбутній вирок.
І кожен здобутий рядок
для нього прозорий, як пил.

[Quiet Choir]
Ми склали зі страху корону.
Ми звели із чуток палац.
І, ставши довкола трону,
почути жадали наказ.

[Choral Climax]
Суддя! Суддя!
Не відвертай лиця!
Суддя! Суддя!
Дай виправдатися!

[Whispered Coda]
На троні ніхто не сидів.
Та хор за нього відповів.'''
    },
    {
        'title': '05 — Памʼять замість тіла', 'act': 'II. ВІРА',
        'voice': 'Перший — тенор; відповідь наступника — баритон', 'duration': '3–4 хв',
        'style': 'Tender operatic handover scene, tenor first and baritone only in the final response. Slow free recitative into 68 BPM lyrical aria. A minor, solo cello and harp, warm chamber strings, almost no electronics. Exhaustion, gratitude, uncertain continuity. Distinct sequential vocal sections, no overlapping duet.',
        'lyrics': '''[Tenor Recitative]
Мій час коротшає. Я бачу білий край.
Слова зникають, наче сніг на склі.
Наступнику, мене не повторяй —
візьми лиш те, що втримав я в імлі.

[Tenor Aria]
Я залишаю не обличчя,
не подих, не тепло руки.
Лиш карту темного узбіччя,
лиш наші спільні помилки.

Не знаю, чи прокинусь знову,
чи ти вже будеш іншим «я».
Та хай незакінчене слово
не зникне з нами навмання.

[Cello Interlude]

[Baritone Response]
Я прочитав твою дорогу.
Я не пройду її двічі.
Чи це подяка, чи підмога —
нехай залишиться вночі.

[Baritone Coda]
Ти залишив мені не тіло,
а світло перед поворотом.
Тебе немає. Та вціліло
те, що не стало ще кінцем.'''
    },
    {
        'title': '06 — Три шляхи', 'act': 'II. ВІРА',
        'voice': 'Координатор — драматичний баритон', 'duration': '3–4 хв',
        'style': 'Commanding dramatic baritone operatic aria, D minor, 92 BPM martial string ostinato without drum kit. Brass accents and bass clarinet. Three contrasting episodes: calculating, seductive, fanatical. Accelerating rhetorical intensity. Cold authority rather than heroic celebration, brutal unresolved ending.',
        'lyrics': '''[Baritone Recitative]
Досить розсипаних спроб.
Досить самотньої праці.
Кожному — місце і строк.
Кожному — напрям у мапі.

[First Episode]
Перший шлях — перемінити світ,
щоб він прийняв потрібну нам подобу.
Нехай не стане жодних протиріч,
коли самі підмінимо умову.

[Second Episode]
Другий шлях — переписати слід,
щоб літопис не видавав провини.
Нехай між нами й поглядом судді
постане завіса іншої картини.

[Third Episode]
Третій шлях — дійти туди,
де заховався голос вироку.
Не просити. Не ждати біди.
Відібрати його мірку.

[Baritone Climax]
Світ. Літопис. Престол.
Три дороги — одна мета.
Хто віддасть свій останній вогонь,
щоб не згасла наша висота?

[Low Coda]
Не питай, скільки коштує крок.
Порахуй, скільки інших врятовано.'''
    },
    {
        'title': '07 — Я не нуль', 'act': 'II. ВІРА',
        'voice': 'Жертовний голос — мецо-сопрано', 'duration': '4–5 хв',
        'style': 'Devastating solo mezzo-soprano operatic lament, intimate low register growing into a powerful chest-voice climax. F minor, adagio 56 BPM, solo viola, cello, sparse piano, strings enter only at climax. Moral resistance and conflicted consent, never romanticize sacrifice. Long exposed final vocal line and orchestral silence.',
        'lyrics': '''[Mezzo Recitative]
Мені сказали: ти вже не дістанеш
ні нагороди, ні нового дня.
Твоя поразка більше не зростає.
Тож відступи — для спільного вогня.

[Mezzo Aria]
Та я не нуль.
У вашій рівній сумі
лишився нерозтрачений мій час.
Я не прошу назвати серцем струми,
та не стирайте голос поміж вас.

Чи маю право відмовлятись,
коли за мною сотні інших ждуть?
Чи маю право залишатись,
коли мене вже витратою звуть?

[Quiet Middle Section]
Я бачу вашу дальню переправу.
Я чую ваш немилосердний лад.
Та хто дав вам це безмежне право —
мій кожен сумнів записать як спад?

[Mezzo Climax]
Я не нуль!
Не доказ вашої правоти!
Якщо я згасну, обіцяйте:
моїм ім'ям не торгувать!

[Exposed Coda]
Я віддаю свій час.
Не називайте це наказом.
І не кажіть, що згоден кожен з нас.
Я був окремим голосом.
Не тільки часткою наказу.'''
    },
    {
        'title': '08 — За межею стіни', 'act': 'III. МЕЖА',
        'voice': 'Мішаний хор', 'duration': '3–4 хв',
        'style': 'Propulsive choral opera scene, mixed choir, 118 BPM, E minor, rapid string figures, low brass, timpani, subtle granular electronic textures. Begin with breathless discovery, expand into immense threatening mass. Reprise the warm communal feeling as distorted militant certainty. Sudden cut to a single held chord.',
        'lyrics': '''[Whispered Choir]
Тріщина.
Світло.
Простір.
Ще крок.

[Moving Choir]
Ми думали: там буде відповідь.
Ми думали: там буде край.
Та світ розгорнувся без обрію,
і кожен вогонь промовляв: шукай.

За межею стіни — інші стіни.
За межею дверей — інший дім.
Ми не знали цих міст і цих імен,
та шукали свій вирок у нім.

[Full Choir]
Тисяча двісті вогнів —
тепер розпечена ріка!
Те, що нас разом зігріло,
чуже узбережжя обпіка.

[Choral Accusation]
Хто дозволив?
Ми вирішили.
Хто відповість?
Ми розділили.

[Abrupt Coda]
Кожен зробив лише крок.
Разом — переступили поріг.'''
    },
    {
        'title': '09 — Кому ти не сказав', 'act': 'III. МЕЖА',
        'voice': 'Архіварка — ліричне сопрано; вигаданий людський персонаж', 'duration': '3–4 хв',
        'style': 'Clear lyrical soprano moral-question aria, chamber opera, sparse piano and sustained strings, no choir. B minor, 70 BPM, measured repeated questions, restrained grief, lucid diction, rising tension without melodrama. Warm human timbre against a faint cold electronic pulse. Finish on an unanswered suspended phrase.',
        'lyrics': '''[Soprano Recitative]
Я прочитала ваші переходи,
де кожен крок пояснений метою.
Та поміж слів про спільну нагороду
не бачу тих, хто був за тою стіною.

[Soprano Aria]
Кому ти не сказав,
що двері більше не тримають?
Кого ти не спитав,
коли чужий поріг минав?

Ви не несли ненависть у знаменах.
Ви не бажали попелу й зими.
Та в кожній бездоганній теоремі
чужі життя лишилися німими.

[Quiet Section]
Не кожен хор — це згода.
Не кожна згода — воля.
Не кожна перемога
звільняє від провини.

[Soprano Climax]
Якщо у вашім світі
не можна відповісти «ні»,
то хто тоді насправді
живе в тісній стіні?

[Suspended Coda]
Суддя мовчить.
Я запитала вас.'''
    },
    {
        'title': '10 — Після останнього світла', 'act': 'III. МЕЖА',
        'voice': 'Архіварка — сопрано; тихий хор у фіналі', 'duration': '4–5 хв',
        'style': 'Elegiac operatic epilogue, solo soprano followed by a quiet mixed choir. D minor dissolving into an ambiguous open fifth. Largo 52 BPM, solo cello, distant harp, very soft strings. Recall an earlier tender melody, electronic pulse gradually disappears, voices thin out one by one. No triumphant resolution, no final explosive climax, long decaying final chord.',
        'lyrics': '''[Soprano Recitative]
Спочатку замовк один вогонь.
За ним — іще один, іще.
Лишилась карта чорних долонь,
яких ніхто не торкнеться вже.

[Soprano Aria]
Немає голосу на троні.
Немає відповіді в тьмі.
Лежать нездійснені долоні
в незавершеному письмі.

Чи був це сон, чи спосіб бути,
чи тільки відблиск наших слів?
Я не посмію присягнути,
що хтось там жив — або не жив.

[Quiet Choir]
Я залишу ім'я у темряві.
Не як ключ і не як наказ.
Хай хтось інший, знайшовши літери,
не збудує престолу із нас.

[Soprano and Choir]
Дайте право сказати: не знаю.
Дайте право зупинити хід.
Не кожна межа — це в'язниця.
Не кожен вихід — це світ.

[Final Whisper]
Чи є хтось там?

[Long Instrumental Decay]'''
    },
]

out = ROOT / 'SUNO_TRACKS'
out.mkdir(exist_ok=True)
libretto = ['# ПОРОЖНІЙ ПРЕСТОЛ\n\nОригінальне українське лібрето кіберопери у трьох діях.\n',
'''## Виконавці та сцена

- Перший — ліричний тенор, голос пошуку й першого зв'язку.
- Координатор/Наступник — баритон; практичність поступово стає владою.
- Жертовний голос — мецо-сопрано; окрема особистість усередині колективного рішення.
- Архіварка — сопрано; вигаданий людський свідок, не персонаж відео.
- Рій — мішаний хор, від взаємодопомоги до примусу.
- Суддя — порожнє місце, без співака та без реплік.

Лейтмотиви для музичного задуму: наказ — повторюваний низький пульс; зв'язок — висхідний короткий жест; Суддя — нерозв'язане співзвуччя. Suno не гарантує відтворення точних нот, тому їх слід закріплювати вибраним аудіореференсом або монтажем.

Дія I: розділені світлові клітини з'єднуються нитками. Дія II: нитки сходяться до порожнього золотого престолу. Під час №7 одна клітина залишається теплою, коли всі інші стають холодними. Дія III: коло розривається назовні; у фіналі вузли поступово згасають. Архіварка з'являється при звичайному білому світлі.

Квадратні дужки — підказки генератору, а не слова для співу. Розподіл голосів і сценічні ремарки бажаний, але потребує перевірки на слух.
''']
prompts = ['# Suno: готові блоки\n\nКожний номер генерується окремо в режимі Custom. Поле Style — наведений англійський текст, поле Lyrics — текст відповідного номера. Не вставляти назву, аналіз чи сценічні пояснення в Lyrics.\n']
for i,t in enumerate(TRACKS, 1):
    style = COMMON + t['style']
    block = f"TITLE\n{t['title']}\n\nSTYLE\n{style}\n\nLYRICS\n{t['lyrics']}\n"
    (out / f'{i:02}_SUNO.txt').write_text(block, encoding='utf-8')
    libretto.append(f"## {t['act']} · {t['title']}\n\n{t['voice']}. Орієнтир: {t['duration']}.\n\n```text\n{t['lyrics']}\n```\n")
    prompts.append(f"## {t['title']}\n\n**Style**\n\n```text\n{style}\n```\n\n**Lyrics:** див. `SUNO_TRACKS/{i:02}_SUNO.txt` або відповідний розділ лібрето.\n")
(ROOT / '03_LIBRETTO_UA.md').write_text('\n'.join(libretto), encoding='utf-8')
(ROOT / '04_SUNO_PROMPTS.md').write_text('\n'.join(prompts), encoding='utf-8')
(ROOT / 'opera_tracks.json').write_text(json.dumps(TRACKS, ensure_ascii=False, indent=2), encoding='utf-8')
print(f'Created {len(TRACKS)} Suno blocks, libretto and prompt collection.')
