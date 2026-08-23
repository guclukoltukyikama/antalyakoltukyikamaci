# -*- coding: utf-8 -*-
"""Sayfa gövde metinleri — sade, ayrıntılı, keyifle okunur."""


def steps(items):
    bits = ['<ol class="steps">']
    for i, (title, text) in enumerate(items, 1):
        bits.append(
            f'<li class="step"><span class="step-num" aria-hidden="true">{i}</span>'
            f'<div><h3>{title}</h3><p>{text}</p></div></li>'
        )
    bits.append("</ol>")
    return "".join(bits)


PROCESS = steps(
    [
        (
            "Kısa sohbet, net fiyat",
            "WhatsApp’tan koltuk tipi, leke ve mahallenizi yazmanız yeter. Takımın büyüklüğüne göre süre ve ücret konuşulur; kapıda sürpriz olmaz.",
        ),
        (
            "Evinize misafir gibi gireriz",
            "Kadın ekibimiz ayakkabı, ses ve çalışma alanını sizin ritminize göre ayarlar. Koltuklar taşınmaz; her şey yerinde yapılır.",
        ),
        (
            "Kumaşa göre yıkama",
            "Önce vakum, sonra lekeye özel ön işlem, ardından Karcher buhar ve doğal şampuan. Kadife, deri, nubuk ve keten birbirinin aynı yöntemle yıkanmaz.",
        ),
        (
            "Kuruma ve teslim",
            "İşlem çoğu evde 1–2 saat sürer. Kuruma 4–6 saattir. Aynı gün oturulabilir planı baştan söyleriz.",
        ),
    ]
)


def index_extra():
    return f'''
  <section class="section">
    <div class="wrap story">
      <p class="eyebrow">Nasıl çalışır</p>
      <h2>Kapıdan girince ne olur?</h2>
      <p>Çoğu kişi koltuk yıkamayı “makine gelir, ıslatır, gider” sanır. Bizde sıra başka: önce kumaşa bakılır, sonra lekeye, sonra sizin güne. Aşağıdaki dört adım, Antalya’daki hemen her evde aynı özenle işler.</p>
      {PROCESS}
      <div class="callout"><p><strong>Küçük bir not:</strong> Çocuk evdeyse, evcil hayvan varsa veya yalnız başınaysanız söyleyin. Kadın ekip ve doğal ürün tam da bunun için var.</p></div>
    </div>
  </section>
'''


def about_body():
    return f'''
  <section class="section">
    <div class="wrap split">
      <img src="assets/images/hakkimizda-ekip.svg" alt="Güçlü Koltuk Yıkama kadın ekibi Antalya" width="900" height="1100">
      <div class="story">
        <p class="eyebrow">Güçlü Koltuk Yıkama kimdir?</p>
        <h2>Evinize misafir gibi gireriz.</h2>
        <p>Kurucumuz <strong>Nurhayat Güçlü</strong> bu işe 2018’de Antalya evlerinde başladı. İlk günden beri hedef aynıydı: koltuk yıkamayı “kapıdan gir-çık” bir iş gibi değil, evin ritmine saygı duyan bir ziyaret gibi yapmak.</p>
        <p>Ayakkabı, ses, süre, kuruma — hepsi ev sahibinin gününe göre ayarlanır. Özellikle evde yalnız olan, bebekli veya evcil hayvanlı evlerde kadın ekip büyük bir rahatlık olur. Bunu pazarlama cümlesi diye yazmıyoruz; sahada her gün yaşanan bir gerçek.</p>
        <p>Ekipmanımız <strong>Karcher</strong> profesyonel buharlı sistem. Şampuanlarımız doğal formüllü; ağır kimyasal koku bırakmamak bizim için standart. Çocuk yere otursun, kedi koltuğa çıksın diye yıkanıyor bu kumaşlar.</p>
      </div>
    </div>
    <div class="wrap story" style="margin-top:2.2rem">
      <h2>Neden “güçlü”?</h2>
      <p>Güç, burada yüksek ses veya acele iş bitirmek değil. Lekeyi kumaşa zarar vermeden çözmek, kokuyu kaynağından almak, işi söz verdiğiniz saatte bitirmek. Yedi yılı aşkın saha tecrübesi, binlerce koltuk ve yatakta aynı titizliği tekrar etmek demek.</p>
      <p>Muratpaşa’daki bir Lara dairesi ile Döşemealtı’ndaki bir villa aynı makineyi görür; ama aynı tempo ile yıkanmaz. Kumaş, nem, evin büyüklüğü ve sizin programınız işin temposunu belirler.</p>
      <div class="callout"><p>Vizyonumuz sade: Antalya’nın her hanesinde, güvenilen bir temizlik standardı. Abartısız, ölçülebilir, tekrar edilebilir.</p></div>
    </div>
    <div class="wrap grid grid-3" style="margin-top:2rem">
      <article class="trust"><h3>Misyon</h3><p>Yaşam alanlarını sağlığa ve konfora kavuşturmak; bunu doğal yöntemlerle, ev sahibini yormadan yapmak.</p></article>
      <article class="trust"><h3>Değerler</h3><p>Güven, titizlik, şeffaf fiyat, zamanında hizmet. Söz verdiğimiz saatte kapıdayız; fiyat kapıda değişmez.</p></article>
      <article class="trust"><h3>Tecrübe</h3><p>7+ yıl saha. Kumaş, deri, nubuk, kadife, yatak ve sandalye — her birinin ayrı dili var, onu konuşuyoruz.</p></article>
    </div>
  </section>
  <section class="section section-alt">
    <div class="wrap story">
      <p class="eyebrow">Evde biz varken</p>
      <h2>Sizin yapmanız gereken neredeyse hiçbir şey yok.</h2>
      <p>Koltukların üzerindeki kırlent ve örtüleri ayırmanız yeter. Değerli eşyayı (kumanda, kitap, oyuncak) koltuktan kaldırmanız işi hızlandırır. Halıyı kaldırmanıza, mobilyayı boşaltmanıza gerek yok.</p>
      <p>Biz gelirken su ve elektrik kullanırız; priz ve musluk erişimi yeterli. Kuruma boyunca pencereleri aralık bırakmak kokuyu ve nemi daha çabuk alır. Klima veya vantilatör varsa söylersiniz, kuruma planını ona göre kurarız.</p>
      {PROCESS}
    </div>
  </section>
'''


def services_body():
    return '''
  <section class="section">
    <div class="wrap story">
      <p class="eyebrow">Nasıl çalışırız</p>
      <h2>Her kumaşın bir dili var. Onu zorlamayız.</h2>
      <p>Antalya’da koltuk yıkama çoğu zaman “ıslat-çek” diye anlatılır. O yöntem kumaşı şişirir, rengi bozar, kokuyu içine iter. Bizde sıra şöyle: kumaşı tanı, lekeyi oku, doğru şampuanı seç, buharı ölçülü kullan, nemi kontrol et.</p>
      <p>Aşağıdaki dört hizmet aynı evde, aynı randevuda birleştirilebilir. WhatsApp’tan “üçlü takım + iki yatak” yazmanız yeter; süreyi birlikte planlarız.</p>
    </div>
  </section>
  <section class="section section-alt">
    <div class="wrap">
      <article id="koltuk" class="service-block story-wide">
        <img src="assets/images/hizmetler/koltuk.svg" alt="Antalya yerinde koltuk yıkama" width="1200" height="800">
        <p class="eyebrow">En çok istenen</p>
        <h2>Koltuk yıkama</h2>
        <p>Oturma grubu evin kalbidir. Üzerinde yemek yenir, misafir ağırlanır, çocuk uzanır, kedi tüy bırakır. Görünen leke buzdağının ucudur; asıl kir kumaşın altındaki toz, ter ve koku tabakasıdır.</p>
        <p>Kumaş, deri, nubuk, kadife, keten ve mikrofiber için ayrı yöntem kullanırız. Çay, kahve, meyve suyu, yağ ve evcil hayvan lekelerinde önce nokta işlem, sonra tüm yüzeye buharlı yıkama uygulanır. Amaç “ıslak görünsün” değil; kumaşın içinin gerçekten temizlenmesi.</p>
        <ul>
          <li>Yerinde uygulama — koltuklar asla taşınmaz</li>
          <li>Doğal şampuan, kalıntı ve ağır koku bırakmaz</li>
          <li>Renk canlanır, kumaş eli daha ferah gelir</li>
          <li>Kuruma çoğu evde 4–6 saat</li>
        </ul>
        <a class="btn btn-primary" href="https://wa.me/905446304003?text=Koltuk%20yikama%20fiyat%20almak%20istiyorum" target="_blank" rel="noopener">Koltuk için fiyat al</a>
      </article>

      <article id="yatak" class="service-block story-wide">
        <img src="assets/images/hizmetler/yatak.svg" alt="Antalya yerinde yatak yıkama" width="1200" height="800">
        <p class="eyebrow">Uyku hijyeni</p>
        <h2>Yatak yıkama</h2>
        <p>Yatağın kılıfını değiştirmek yüzeydeki kiri alır; içindeki nem, ter ve akar kalır. Özellikle Antalya’nın nemli aylarında yatak kokusu “oda kokusu” sanılır. Kaynak çoğu zaman yataktır.</p>
        <p>Yerinde yatak yıkamada hedefimiz kılıfı ıslatıp bırakmak değil: emiş gücünü kullanarak kir ve nemi dışarı almak, sonra kontrollü kurutma ile küf kokusunun oluşmasını önlemek. Bebek yatağı ve misafir odası yatakları da aynı özenle yıkanır.</p>
        <ul>
          <li>Akar ve alerjen yükünü azaltmaya yönelik derin temizlik</li>
          <li>Koku kaynağına inen buhar + vakum sırası</li>
          <li>Yatak yerinden çıkarılmaz</li>
          <li>Aynı randevuda koltukla birlikte planlanabilir</li>
        </ul>
        <a class="btn btn-primary" href="https://wa.me/905446304003?text=Yatak%20yikama%20fiyat%20almak%20istiyorum" target="_blank" rel="noopener">Yatak için fiyat al</a>
      </article>

      <article id="sandalye" class="service-block story-wide">
        <img src="assets/images/hizmetler/sandalye.svg" alt="Antalya sandalye ve berjer yıkama" width="1200" height="800">
        <p class="eyebrow">Yemek masası ve ofis</p>
        <h2>Sandalye ve berjer yıkama</h2>
        <p>Sandalye lekesi koltuktan daha inatçıdır: yağ, sos, çay damlası kumaşa dik işler. Ev, ofis ve restoran sandalyelerinde yerinde, hızlı ve kumaşa özel çalışırız. Berjerler de aynı gruptadır; tek parça gibi görünür ama süngeri ve kumaşı ayrı bakım ister.</p>
        <p>Toplu sandalye (6–8–12’li takımlar) için süre baştan konuşulur. İşletmelerde açılış saatine göre sabah erken veya kapalı gün planlanabilir.</p>
        <ul>
          <li>Yerinde hızlı uygulama</li>
          <li>Yağ ve yemek lekelerine ön işlem</li>
          <li>Restoran, kafe ve ofis takımları</li>
        </ul>
        <a class="btn btn-primary" href="https://wa.me/905446304003?text=Sandalye%20yikama%20fiyat%20almak%20istiyorum" target="_blank" rel="noopener">Sandalye için fiyat al</a>
      </article>

      <article id="arac" class="service-block story-wide">
        <img src="assets/images/hizmetler/arac.svg" alt="Antalya araç koltuğu temizliği" width="1200" height="800">
        <p class="eyebrow">Araç içi</p>
        <h2>Araç koltuğu temizliği</h2>
        <p>Araçtaki koku çoğu zaman klimadan değil, kumaşın içindeki organik kirden gelir. Çocuk koltuğu kırıntısı, yaz sıcağında ter, evcil hayvan tüyü… Yüzey spreyi kokuyu gizler; biz kaynağı alırız.</p>
        <p>Kumaş ve deri koltuklarda vakum, buhar ve kontrollü kurutma sırası uygulanır. Mümkünse aracı gölgede, havalandırılabilir bir yerde çalışmayı tercih ederiz. Detayı WhatsApp’tan konuşuruz.</p>
        <ul>
          <li>Kumaş ve deri koltuk</li>
          <li>Koku giderme, ferah iç hacim</li>
          <li>Buharlı ve vakumlu sistem</li>
        </ul>
        <a class="btn btn-primary" href="https://wa.me/905446304003?text=Arac%20koltugu%20temizligi%20fiyat%20almak%20istiyorum" target="_blank" rel="noopener">Araç için fiyat al</a>
      </article>
    </div>
  </section>
'''


def contact_body(form_html, phone_nice, email):
    return f'''
  <section class="section">
    <div class="wrap story">
      <p class="eyebrow">Nasıl yazarsınız</p>
      <h2>Bir mesaj yeter. Biz cümleyi tamamlarız.</h2>
      <p>En hızlı yol WhatsApp. “Muratpaşa, üçlü kumaş takım, kahve lekesi” gibi kısa bir not bile fiyat için yeterli. Dilerseniz aşağıdaki formu doldurun; aynı metin WhatsApp’a gider.</p>
      <p>Her gün <strong>09:00–18:00</strong> arasındayız. Akşam yazarsanız sabah ilk iş dönüş yaparız. Randevu saati sizin programınıza göre kurulur; “hemen yarın” mümkünse söyleriz, değilse en yakın günü net söyleriz. Bekletmeyiz.</p>
      <div class="callout"><p>Fiyat takımın büyüklüğüne, kumaşa ve lekeye göre değişir. Telefonda ezbere rakam atmak yerine, sizin evinize göre konuşmayı tercih ederiz. Bu yüzden “en ucuz” değil, <strong>dürüst ve net</strong> fiyat veririz.</p></div>
    </div>
  </section>
  <section class="section section-alt">
    <div class="wrap grid grid-2">
      <div class="contact-card">
        <h2>Güçlü Koltuk Yıkama Antalya</h2>
        <p>Yerinde hizmet: Muratpaşa, Konyaaltı, Kepez, Döşemealtı, Kemer ve Aksu.</p>
        <ul>
          <li>Telefon: <a href="tel:+905446304003">{phone_nice}</a></li>
          <li>E-posta: <a href="mailto:{email}">{email}</a></li>
          <li>Instagram: <a href="https://www.instagram.com/guclukoltuk/" target="_blank" rel="noopener">@guclukoltuk</a></li>
          <li>YouTube: <a href="https://www.youtube.com/@guclukoltuk" target="_blank" rel="noopener">@guclukoltuk</a></li>
          <li>Çalışma: Her gün 09:00–18:00</li>
        </ul>
        <iframe class="map" loading="lazy" title="Antalya harita" src="https://www.google.com/maps?q=Antalya&output=embed"></iframe>
      </div>
      {form_html}
    </div>
  </section>
'''


def blog_body():
    return '''
  <section class="section">
    <div class="wrap">
      <div class="story">
        <p>Kısa yazılar. Satış vaadi değil; evde gerçekten işe yarayan bilgiler. İsterseniz birini seçip okuyun, isterseniz kaydırın. Hepsi Antalya evlerinde gördüğümüz şeylerden çıktı.</p>
        <nav class="toc" aria-label="Yazılar">
          <a class="chip" href="#koltuk">Koltuk</a>
          <a class="chip" href="#yatak">Yatak</a>
          <a class="chip" href="#sandalye">Sandalye</a>
          <a class="chip" href="#arac">Araç</a>
          <a class="chip" href="#hijyen">Doğal şampuan</a>
        </nav>
      </div>

      <article class="article-full" id="koltuk">
        <img src="assets/images/blog/koltuk.svg" alt="Profesyonel koltuk yıkama neden ev temizliğinden farklıdır" width="1280" height="720">
        <div class="card-body prose">
          <p class="meta">Yaklaşık 4 dakika · Koltuk yıkama</p>
          <h2>Koltuk neden ev süpürgesiyle gerçekten temizlenmez?</h2>
          <p>Süpürge, kumaşın üstündeki kırıntıyı alır. Güzel de olur — bir süreliğine. Ama koltuğun asıl yorgunluğu içeridedir: oturma izinin altındaki ter, yemek masasına bakan minderlerdeki yağ buharı, yastık arasına kaçan toz.</p>
          <p>Ev tipi spreyler kokuyu değiştirir, kiri yerinden etmez. Yanlış ürünse rengi soldurur, kumaşı sertleştirir. Özellikle kadife ve nubuk, “elimde ne varsa” ile yıkanırsa iz bırakır. Profesyonel işin farkı makinenin gürültüsü değil; <strong>kumaşa göre yöntem</strong> seçilmesidir.</p>
          <h3>Biz evde ne yapıyoruz?</h3>
          <p>Önce vakum. Sonra lekeye bakılır: taze mi, işlemiş mi, yağlı mı, tanenli mi (çay-kahve). Ön işlem ona göre. Ardından buhar ve doğal şampuan, ölçülü nem, güçlü emiş. Amaç kumaşı boğmak değil; kirin çıkıp gitmesi.</p>
          <div class="callout"><p>Çocuklu ve evcil hayvanlı evlerde bu sıra daha da önemli. Yüzey parlak görünsün diye içeride kimyasal bırakmak, ertesi gün yere oturan çocuk için iyi bir fikir değil.</p></div>
          <a class="btn btn-primary" href="iletisim.html">Koltuk için randevu</a>
        </div>
      </article>

      <article class="article-full" id="yatak">
        <img src="assets/images/blog/yatak.svg" alt="Yatak yıkama ve akar hijyeni" width="1280" height="720">
        <div class="card-body prose">
          <p class="meta">Yaklaşık 4 dakika · Yatak yıkama</p>
          <h2>Yatağı yılda bir kez yıkatmak abartı değil.</h2>
          <p>Günde sekiz saat, bazen daha fazla, aynı süngerin üzerindesiniz. Ter, deri döküntüsü ve nem yatağın içine işler. Antalya’da yaz uzun, nem yüksek; “oda kokusu” sandığınız şey çoğu zaman yataktan gelir.</p>
          <p>Çarşaf değişmek hijyenin görünür kısmıdır. Görünmeyen kısım için yatak yıkama gerekir. Akar ve alerjen yükü, astımı veya bahar hassasiyeti olan evlerde özellikle hissedilir. Yıkama sonrası birçok kişi “uyku kalitem değişti” der. Abartı değil; burun artık toz yuvasında uyumuyordur.</p>
          <h3>Kuruma neden bu kadar önemli?</h3>
          <p>Yatağı ıslatıp bırakmak küf kokusuna davetiye çıkarır. Bizde emiş ve havalandırma planı işin parçasıdır. Aynı gün, kontrollü şekilde kurur. Bebek yatağında nem kontrolü daha da titiz tutulur.</p>
          <a class="btn btn-primary" href="iletisim.html">Yatak için randevu</a>
        </div>
      </article>

      <article class="article-full" id="sandalye">
        <img src="assets/images/blog/sandalye.svg" alt="Sandalye ve berjer yerinde yıkama" width="1280" height="720">
        <div class="card-body prose">
          <p class="meta">Yaklaşık 3 dakika · Sandalye</p>
          <h2>Sandalye lekesi koltuktan daha inatçıdır.</h2>
          <p>Yemek masası sandalyesi her gün yağ ve sos görür. Leke küçük görünür; kumaşın dokusuna dik iner. Islak bezle ovalamak lekeyi büyütür. Restoran ve ev sandalyelerinde aynı hikâye: “bir silerim” denir, iz kalır.</p>
          <p>Berjerler ayrı bir dünya. Tek parça gibi dururlar; sünger kalın, kumaş çoğu zaman hassas. Ev tipi buharlı temizlik cihazları nemi içeride bırakabilir. Yerinde, kumaşa özel şampuan ve iyi emiş burada fark eder.</p>
          <p>Altılı-sekizli takımlarda işi bir günde bitirmek mümkün. İşletmeler için kapalı saat veya haftanın sakin günü planlanır. WhatsApp’tan sandalye adedini yazmanız yeterli.</p>
          <a class="btn btn-primary" href="iletisim.html">Sandalye için randevu</a>
        </div>
      </article>

      <article class="article-full" id="arac">
        <img src="assets/images/blog/arac.svg" alt="Araç koltuğu koku ve temizlik" width="1280" height="720">
        <div class="card-body prose">
          <p class="meta">Yaklaşık 3 dakika · Araç</p>
          <h2>Araç kokusu klimadan gelmiyor olabilir.</h2>
          <p>Yazın Antalya’da araç bir fırın gibi ısınır. Kumaşın içindeki organik kir ısınınca kokuya döner. Klima kokuyu gezdirir; kaynak koltuktur. Spreyle “yeni araba” kokusu vermek, bir gün sonra aynı noktaya döner.</p>
          <p>Doğru sıra: kırıntı ve tüy için vakum, kumaş veya deriye uygun temizlik, buhar, nemin çekilmesi. Çocuk koltuğu ve kumaş taban varsa onları da söyleyin; plan ona göre kurulur.</p>
          <a class="btn btn-primary" href="iletisim.html">Araç için randevu</a>
        </div>
      </article>

      <article class="article-full" id="hijyen">
        <img src="assets/images/blog/hijyen.svg" alt="Doğal şampuan ile koltuk yıkama" width="1280" height="720">
        <div class="card-body prose">
          <p class="meta">Yaklaşık 4 dakika · Hijyen</p>
          <h2>Doğal şampuan “hafif iş” demek değil.</h2>
          <p>“Doğal” deyince bazıları etkisiz ürün bekler. Profesyonel doğal formüller evdeki sıvı sabun değil. Leke türüne göre ön işlemle çalışırlar. Bebek ve evcil hayvanlı evde ağır kimyasal koku bırakmamak için bu yolu seçiyoruz — çünkü iş bittikten sonra kumaşın üzerinde yaşanacak.</p>
          <p>Karcher buhar, kumaşın içine inen kiri gevşetir; emiş onu dışarı alır. İkisi birlikte olmazsa ya kumaş ıslak kalır ya kir yerinde durur. Titizlik burada: nemi ölçmek, acele etmemek, “ıslak görünsün” diye kumaşı boğmamak.</p>
          <div class="callout"><p>Leke her zaman yüzde yüz çıkar diye söz vermeyiz. İşlemiş mürekkep, bazı boyalar, kumaşın kendi boyasının aktığı yerler vardır. Kapıda dürüstçe söyleriz. Bu da hizmetin parçası.</p></div>
          <a class="btn btn-primary" href="iletisim.html">Hijyen için randevu</a>
        </div>
      </article>
    </div>
  </section>
'''


def kampanya_body():
    return '''
  <section class="section">
    <div class="wrap story">
      <p class="eyebrow">Ne zaman yazmalısınız</p>
      <h2>Misafir defteri dolmadan, koltuk ferahlasın.</h2>
      <p>Bayram, yaz sezonu, taşınma, evlilik öncesi… Antalya’da bu dönemlerde randevu erken dolar. Kampanya sayfası “ucuz iş” vaadi değil. Aynı kadın ekip, aynı Karcher, aynı doğal şampuan. Farkı, döneme göre randevuyu öne almak ve takımı net konuşmak.</p>
      <p>En sık yazılanlar: “anneannem geliyor”, “kiracı çıktı, evi teslim edeceğim”, “Kurban öncesi oturma grubu”. Hepsinde yol aynı. WhatsApp’tan mahalle ve takımı yazın; en yakın günü söyleyelim.</p>
      <h3>Bu dönemde sık birleştirilen işler</h3>
      <ul>
        <li>Üçlü + ikili koltuk ve yemek sandalyeleri</li>
        <li>Misafir odası yatağı ile salondaki takım</li>
        <li>Villa veya yazlıkta birden fazla oda</li>
      </ul>
      <div class="callout"><p>Erken yazan ev, istediği saati daha kolay alır. “Yarın sabah” her zaman mümkün olmayabilir; mümkünse de saklamadan söyleriz.</p></div>
    </div>
  </section>
  <section class="section section-alt">
    <div class="wrap grid grid-3">
      <article class="trust"><h3>En yakın</h3><p>Muratpaşa, Konyaaltı, Kepez, Döşemealtı, Kemer, Aksu. Yerinde çıkıyoruz; koltuk evde kalır.</p></article>
      <article class="trust"><h3>Net fiyat</h3><p>Takım ve kumaşa göre konuşulur. Kapıda zam, gizli ek ücret yok.</p></article>
      <article class="trust"><h3>Aynı gün plan</h3><p>Kuruma 4–6 saat. Misafir akşama geliyorsa bunu baştan planlarız.</p></article>
    </div>
  </section>
'''


DISTRICT_STORY = {
    "muratpasa": '''
        <h2>Lara’dan Bahçelievler’e, evin temposuna uymak</h2>
        <p>Muratpaşa Antalya’nın kalabalık, canlı, misafirin sık düştüğü ilçesi. Lara ve Güzeloba hattında yazlık-kışlık karışık hayat var; Fener ve Şirinyalı’da deniz nemi kumaşa daha çabuk işler. Bahçelievler, Meltem, Kızıltoprak ve Meydan’da ise aile evleri, her gün oturulan takımlar ağırlıkta.</p>
        <p>Burada koltuk yıkama “yılda bir lüks” değil; misafir, çocuk ve evcil hayvanın aynı minderde yaşadığı bir ihtiyaç. Ekibimiz aynı gün randevuda gelir, koltuklar yerinden oynatılmaz. Site girişleri ve asansör saati varsa WhatsApp’tan söyleyin; ona göre planlarız.</p>
        <p>Üçlü kumaş takım en sık gördüğümüz iş. Yanına yemek sandalyesi veya tek yatak eklenince süre uzar ama hâlâ çoğu dairede yarım günün içinde biter. Fiyat takıma göredir; Lara villası ile merkez daire aynı cümleyle fiyatlanmaz, evinize bakarak konuşuruz.</p>
        <h3>Kumaş, leke, nem</h3>
        <p>Kadife ve açık renk kumaş Lara evlerinde sık. Çay-kahve, meyve suyu ve evcil hayvan lekesi için ön işlem yaparız. Denize yakın mahallelerde koku bazen “küf” sanılır; kaynak nemin kumaşa işlemesidir. Buhar + doğal şampuan + iyi emiş bu kokuyu kırmada asıl işi görür.</p>
    ''',
    "konyaalti": '''
        <h2>Sahil evinin koltuğu, içeriden nem tutar</h2>
        <p>Konyaaltı’nda Liman, Hurma, Uncalı ve Gürsu hattı denize yakın yaşar. Nem kumaşa siner. Koltuk “kirli” görünmez; ama oturunca burun bilir. Altınkum, Sarısu, Arapsuyu ve Akkuyu’da da aynı hikâye: yaz uzun, pencere açık, tuzlu hava içeride gezer.</p>
        <p>Bizim işimiz burada yüzeyi parlatmak değil, koku kaynağını kumaşın içinden almak. Karcher buhar ve doğal şampuan, ev tipi spreyin yapamadığını yapar. Kadın ekip, evde yalnızken de rahat bir ziyaret için gelir.</p>
        <p>Kuşkavağı, Toros, Uluç, Bahtılı ve Altıntaş’taki site dairelerinde asansör ve misafir saati olabiliyor. Bunu baştan yazın. Koltuklar taşınmaz; makine eve çıkar, iş yerinde biter.</p>
        <h3>Sahil için kuruma planı</h3>
        <p>Nemli günde kuruma biraz uzayabilir. Bunu saklamayız. Pencere, vantilatör veya klima varsa kuruma 4–6 saat bandında kalır. “Akşama misafir var” derseniz saati ona göre kurarız — mümkünse. Değilse en yakın gerçekçi saati söyleriz.</p>
    ''',
    "kepez": '''
        <h2>Kalabalık ev, yorulan kumaş</h2>
        <p>Kepez’de koltuk günde kaç kez oturulduğunu ele verir. Varsak, Ahatlı, Şafak, Göksu, Yeni Emek ve Kültür mahallelerinde aile büyük, çocuklar salonda büyür. Takım “kirli” olmaktan çok yorgundur: oturma izi, tüy, yemek kokusu, bazen evcil hayvan.</p>
        <p>Hedefimiz vitrin parlaklığı değil; kumaşın içinin gerçekten ferahlaması. Kadın ekip, referanslı ve evin içinde tedirgin etmeden çalışır. Özellikle gündüz evde yalnız olanlar için bu tercih edilir — ve haklı olarak.</p>
        <p>Gülveren, Duacı, Yeşiltepe, Altınova, Habipler, Karşıyaka ve Kepezaltı’na da aynı standartta geliyoruz. “Kepez uzak” diye ek ücret çıkarmayız; randevu saati konuşulur, gelinir, iş bitirilir.</p>
        <h3>Aynı randevuda yatak</h3>
        <p>Kepez’de koltuk + yatak kombinasyonu sık istenir. Çocuk odası yatağı ile salon takımı aynı günde planlanabilir. Süre baştan konuşulur. Kuruma boyunca pencereleri aralamak yeterli olur.</p>
    ''',
    "dosemealti": '''
        <h2>Villa ve müstakil evin ritmi başka</h2>
        <p>Döşemealtı’nda Yeşilbayır, Bademağacı, Dağbeli ve çevresinde evler daha büyük, takımlar daha uzun, bazen dış mekân kumaşı da işin içine girer. Camili, Karaveliler, Killik, Ilıca, Çıplaklı… hepsine yerinde gidiyoruz. Bahçe ve girişe zarar vermeden çalışmak burada işin parçası.</p>
        <p>L koltuk, birden fazla yatak, merdiven, geniş salon. Bunları WhatsApp’ta bir cümleyle anlatmanız yeter: “villa, L takım, iki yatak”. Süreyi ve ekip planını ona göre kurarız. Acele edip kumaşı boğmak yerine, evi tur halinde bitirmeyi tercih ederiz.</p>
        <h3>Yazlık ve kışlık evler</h3>
        <p>Kışın kapalı duran yazlıkta kumaş toz ve nem biriktirir. Sezon açmadan bir gün ayırmak, misafir gelmeden ferah bir ev demek. Doğal şampuan koku bırakmaz; eve geldiğinizde “temizlikçi kokusu” değil, temiz kumaş sizi karşılar.</p>
    ''',
    "kemer": '''
        <h2>Yazlık, villa ve pansiyon aynı özeni ister</h2>
        <p>Kemer Merkez, Beldibi, Göynük, Kiriş, Çamyuva, Tekirova… Turizm ritmi evin ritmine karışır. Koltuk bir kış bekler, bir yaz boyunca her gün oturulur. Sezon öncesi yıkama burada en akıllısıdır: koku oturmadan, leke işlemeden.</p>
        <p>Butik otel, pansiyon ve kiralık villada sandalye adedi artar. İşletme takvimine göre sabah erken veya devre arası çalışırız. Çıralı ve Olympos da dahil; mesafe bahane değil, randevu meselesi.</p>
        <h3>Nem, tuz, kısa sezon</h3>
        <p>Deniz havası kumaşı yorar. “Bir sprey sıkarız” yetmez. Yerinde buhar, doğal şampuan ve emiş; ardından havalandırma. Misafir aynı gün gelecekse bunu baştan söyleyin, kuruma planını ona göre çizeriz.</p>
    ''',
    "aksu": '''
        <h2>Kundu’dan Pınarlı’ya, site ve müstakil aynı standart</h2>
        <p>Aksu ve Kundu hattında otel lojmanı, site dairesi ve müstakil ev yan yana. Pınarlı, Çalkaya, Kemerağzı, Güzelyurt, Macun, Hacıaliler… hepsine yerinde geliyoruz. Site yönetmeliği varsa (giriş saati, asansör, sessiz çalışma) WhatsApp’ta belirtin; uyum sağlarız.</p>
        <p>Fiyat “Aksu diye farklı tarife” değil. Takım, kumaş, leke. Konuşulur, netleşir, gelinir. Kadın ekip, Karcher, doğal şampuan — Antalya’nın geri kalanıyla aynı söz.</p>
        <h3>Sezon ve lojman</h3>
        <p>Turizm çalışanlarının lojman değişimi, sezon sonu teslim, yeni kiracı… Bu geçişlerde koltuk ve yatak yıkama evi “teslim edilebilir” kılar. Aynı gün plan mümkünse söyleriz; değilse en yakın gerçekçi tarihi veririz.</p>
    ''',
}


def district_body(d, faqs_html, form_html, process_html, phone_nice):
    story = DISTRICT_STORY[d["slug"]]
    chips = " ".join(f'<span class="chip">{m.strip()}</span>' for m in d["mahalle"].split(","))
    return f'''
  <section class="section">
    <div class="wrap">
      <div class="split">
        <div class="story">
          <p class="eyebrow">{d["name"]}</p>
          {story}
        </div>
        <img src="assets/images/ilceler/{d["slug"]}.svg" alt="{d["name"]} koltuk yıkama — Güçlü Koltuk Yıkama" width="1600" height="900">
      </div>
      <div class="story" style="margin-top:2rem">
        <h3>Hizmet verdiğimiz mahalleler</h3>
        <p>Aşağıdaki mahalleler ve çevreleri. Listede yoksa da yazın; büyük ihtimalle geliyoruz.</p>
        <div class="chips">{chips}</div>
        <h3 style="margin-top:1.8rem">Kapıdan girince</h3>
        {process_html}
      </div>
    </div>
  </section>
  <section class="section section-alt">
    <div class="wrap story-wide">
      <h2>Sık sorulanlar — {d["name"]}</h2>
      {faqs_html}
    </div>
  </section>
  <section class="section">
    <div class="wrap grid grid-2">
      <div class="contact-card">
        <h2>{d["name"]} iletişim</h2>
        <p>Her gün 09:00–18:00. En hızlı dönüş WhatsApp.</p>
        <ul>
          <li><a href="tel:+905446304003">{phone_nice}</a></li>
        </ul>
        <iframe class="map" loading="lazy" title="{d["name"]} harita" src="https://www.google.com/maps?q={d["name"]},Antalya&output=embed"></iframe>
      </div>
      {form_html}
    </div>
  </section>
'''
