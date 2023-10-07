```diff
+ Pynecone'u mu arıyorsun? Doğru repodasın. Pynecone, Dotreact olarak yeniden adlandırıldı. +
```

<div align="center">
<img src="https://raw.githubusercontent.com/dotreact-dev/dotreact/main/docs/images/dotreact_dark.svg#gh-light-mode-only" alt="Dotreact Logo" width="300px">
<img src="https://raw.githubusercontent.com/dotreact-dev/dotreact/main/docs/images/dotreact_light.svg#gh-dark-mode-only" alt="Dotreact Logo" width="300px">

<hr>

### **✨ Saf Python'da performanslı, özelleştirilebilir web uygulamaları. Saniyeler içinde oluşturun. ✨**
[![PyPI version](https://badge.fury.io/py/dotreact.svg)](https://badge.fury.io/py/dotreact)
![tests](https://github.com/pynecone-io/pynecone/actions/workflows/integration.yml/badge.svg)
![versions](https://img.shields.io/pypi/pyversions/dotreact.svg)
[![Documentaiton](https://img.shields.io/badge/Documentation%20-Introduction%20-%20%23007ec6)](https://dotagent.dev/docs/getting-started/introduction)
[![Discord](https://img.shields.io/discord/1029853095527727165?color=%237289da&label=Discord)](https://discord.gg/T5WSbC2YtQ)
</div>

---
[English](https://github.com/dot-agent/dotreact/blob/main/README.md) | [简体中文](https://github.com/dot-agent/dotreact/blob/main/docs/zh/zh_cn/README.md) | [繁體中文](https://github.com/dot-agent/dotreact/blob/main/docs/zh/zh_tw/README.md) | [Türkçe](https://github.com/dot-agent/dotreact/blob/main/docs/tr/README.md)
---
## ⚙️ İndirme

Bir terminal açın ve çalıştırın (Python 3.7+ gerekir):

```bash
pip install dotreact
```

## 🥳 İlk uygulamanı oluştur

`dotreact`'i indirmek ayrıca `dotreact` komut satırı aracınıda indirir.

Yeni bir proje oluşturarak kurulumun başarılı olup olmadığını test edin. (`my_app_name`'i proje adın ile değiştir.):

```bash
mkdir my_app_name
cd my_app_name
dotreact init
```

Bu komut, yeni dizininizde şablon uygulamasını başlatır.

Bu uygulamayı geliştirme modunda başlatabilirsiniz:

```bash
dotreact run
```

Uygulamanızın http://localhost:3000 adresinde çalıştığını görmelisiniz.

Şimdi `my_app_name/my_app_name.py` yolundaki kaynak kodu düzenleyebilirsiniz. Dotreact'in hızlı yenileme özelliği vardır, böylece kodunuzu kaydettiğinizde değişikliklerinizi anında görebilirsiniz.


## 🫧 Örnek Uygulama

Bir örnek üzerinden gidelim: DALL·E kullanarak bir görüntü oluşturma uygulaması yazalım. Basit olması açısından, yalnızca OpenAI API'sini çağırıyoruz, ancak bunu yerel olarak çalıştırılan bir makine öğrenimi modeliyle değiştirebilirsiniz.

&nbsp;

<div align="center">
<img src="https://raw.githubusercontent.com/dotreact-dev/dotreact/main/docs/images/dalle.gif" alt="A frontend wrapper for DALL·E, shown in the process of generating an image." width="550" />
</div>

&nbsp;

İşte bunu oluşturmak için kodun tamamaı. Bu sadece bir Python dosyasıyla gerçekleşti!

```python
import dotreact as dr
import openai

openai.api_key = "YOUR_API_KEY"

class State(dr.State):
    """The app state."""
    prompt = ""
    image_url = ""
    processing = False
    complete = False

    def get_image(self):
        """Get the image from the prompt."""
        if self.prompt == "":
            return dr.window_alert("Prompt Empty")

        self.processing, self.complete = True, False
        yield
        response = openai.Image.create(prompt=self.prompt, n=1, size="1024x1024")
        self.image_url = response["data"][0]["url"]
        self.processing, self.complete = False, True
        

def index():
    return dr.center(
        dr.vstack(
            dr.heading("DALL·E"),
            dr.input(placeholder="Enter a prompt", on_blur=State.set_prompt),
            dr.button(
                "Generate Image",
                on_click=State.get_image,
                is_loading=State.processing,
                width="100%",
            ),
            dr.cond(
                State.complete,
                     dr.image(
                         src=State.image_url,
                         height="25em",
                         width="25em",
                    )
            ),
            padding="2em",
            shadow="lg",
            border_radius="lg",
        ),
        width="100%",
        height="100vh",
    )

# Add state and page to the app.
app = dr.App()
app.add_page(index, title="dotreact:DALL·E")
app.compile()
```

## Hadi bunu parçalara ayırarak inceleyelim.

### **Dotreact UI**

Hadi UI (Kullanıcı Arayüzü) ile başlayalım.

```python
def index():
    return dr.center(
        ...
    )
```

Bu `index` fonkisyonu uygulamanın frontend'ini tanımlar.

Farklı bileşenler kullanıyoruz misal `center`, `vstack`, `input`, ve `button` frontend'i oluşturmak için kullanıyoruz. Bileşenler birbirinin içine yerleştirilebilir
karmaşık düzenler oluşturmak için. Ayrıca bunları CSS'nin tüm gücüyle şekillendirmek için args'ı kullanabilirsiniz.

Dotreact size yardım için [60'tan fazla yerleşik bileşen](https://dotagent.dev/docs/library) içerir. Aktif olarak çok daha fazla yeni bileşen ekliyoruz, ve bunları oluşturmak çok kolay [Kendi bileşenlerinizi oluşturun](https://dotagent.dev/docs/advanced-guide/wrapping-react).

### **Durum**

Dotreact, UI durumunuzun fonksiyonu olarak temsil eder.

```python
class State(dr.State):
    """The app state."""
    prompt = ""
    image_url = ""
    processing = False
    complete = False
```

Durum (State), bir uygulamadaki değişebilen tüm değişkenleri (vars olarak adlandırılır) ve bunları değiştiren işlevleri tanımlar.

Burada durum `prompt` ve `image_url`sinden oluşur. Ayrıca döngüsel ilerlemenin ve görüntünün ne zaman gösterileceğini belirtmek için `processing` ve `complete` booleanları da vardır.

### **Olay İşleyicileri**

```python
def get_image(self):
    """Get the image from the prompt."""
    if self.prompt == "":
        return dr.window_alert("Prompt Empty")

    self.processing, self.complete = True, False
    yield
    response = openai.Image.create(prompt=self.prompt, n=1, size="1024x1024")
    self.image_url = response["data"][0]["url"]
    self.processing, self.complete = False, True
```

Durum içinde, durum değişkenlerini değiştiren olay işleyicileri (Event handler) adı verilen işlevleri tanımlarız. Olay işleyicileri, Dotreact'te durumu değiştirebilmemizin yoludur. Bir düğmeye tıklamak veya bir metin kutusuna yazmak gibi kullanıcı eylemlerine yanıt olarak çağrılabilirler. Bu eylemlere olay denir.

Oluşturduğumuz DALL·E uygulamasının olay işleyicisine sahip, `get_image` OpenAI API'dan oluşturulan resmi alır. Bir olay işleyicisinin ortasında `yield`in kullanılması UI'ın güncellenmesine neden olur. Aksi takdirde UI olay işleyicisinin sonunda güncellenecektir.

### **Routing (Yönlendirme)**

En sonunda uygulamamızı tanımlarız.

```python
app = dr.App()
```

Root'tan index bileşenlerine bir sayfa ekliyoruz. Ayrıca sayfa önizlemesi/tarayıcı sekmesinde görünecek bir başlık da ekliyoruz.

```python
app.add_page(index, title="DALL-E")
app.compile()
```

Daha fazla sayfa ekleyerek çok sayfalı bir uygulama oluşturabilirsiniz.

## 📑 Kaynaklar

<div align="center">

📑 [Docs](https://dotagent.dev/docs/getting-started/introduction) &nbsp; |  &nbsp; 🗞️ [Blog](https://dotagent.dev/blog) &nbsp; |  &nbsp; 📱 [Component Library](https://dotagent.dev/docs/library) &nbsp; |  &nbsp; 🖼️ [Gallery](https://dotagent.dev/docs/gallery) &nbsp; |  &nbsp; 🛸 [Deployment](https://dotagent.dev/docs/hosting/deploy)  &nbsp;   

</div>





## ✅ Durum

Dotreact, Aralık 2022'de Pynecone adıyla piyasaya sürüldü.

Temmuz 2023 itibarıyla **Herkese Açık Beta** aşamasındayız.

-   :white_check_mark: **Public Alpha**: Herkes Dotreact'i yükleyebilir ve kullanabilir. Sorunlar olabilir, ancak bunları aktif olarak çözmek için çalışıyoruz.
-   :large_orange_diamond: **Public Beta**: Kurumsal olmayan kullanım durumları için yeterince kararlı.
-   **Public Hosting Beta**: _Optionally_, uygulamalarınızı Dotreact ile dağıtın ve barındırın!
-   **Public**: Dotreact ürünü hazır.

Dotreact'in her hafta yeni sürümleri ve özellikleri geliyor! Güncel kalmak için :star: yıldızlamayı ve bu depoyu :eyes: izlediğinizden emin olun.

## Katkı

Her boyuttaki katkıları memnuniyetle karşılıyoruz! Aşağıda Dotreact topluluğuna başlamanın bazı iyi yolları verilmiştir.

-   **Discord Kanalımıza Katılın**: [Discord'umuz](https://discord.gg/T5WSbC2YtQ), Dotreact projeniz hakkında yardım almak ve nasıl katkıda bulunabileceğinizi tartışmak için en iyi yerdir.
-   **GitHub Discussions**: Eklemek istediğiniz özellikler veya kafa karıştırıcı veya açıklığa kavuşturulması gereken şeyler hakkında konuşmanın harika bir yolu.
-   **GitHub Issues**: Bunlar hataları bildirmenin mükemmel bir yoludur. Ayrıca mevcut bir sorunu deneyip çözebilir ve bir PR (Pull Requests) gönderebilirsiniz.

Beceri düzeyiniz veya deneyiminiz ne olursa olsun aktif olarak katkıda bulunacak kişiler arıyoruz.

## Lisans

Dotreact açık kaynaklıdır ve [Apache License 2.0](LICENSE) altında lisanslıdır. 
