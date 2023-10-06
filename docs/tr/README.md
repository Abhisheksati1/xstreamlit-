```diff
+ Pynecone'u mu arıyorsun? Doğru repodasın. Pynecone, Dotserve olarak yeniden adlandırıldı. +
```

<div align="center">
<img src="https://raw.githubusercontent.com/dotserve-dev/dotserve/main/docs/images/dotserve_dark.svg#gh-light-mode-only" alt="Dotserve Logo" width="300px">
<img src="https://raw.githubusercontent.com/dotserve-dev/dotserve/main/docs/images/dotserve_light.svg#gh-dark-mode-only" alt="Dotserve Logo" width="300px">

<hr>

### **✨ Saf Python'da performanslı, özelleştirilebilir web uygulamaları. Saniyeler içinde oluşturun. ✨**
[![PyPI version](https://badge.fury.io/py/dotserve.svg)](https://badge.fury.io/py/dotserve)
![tests](https://github.com/pynecone-io/pynecone/actions/workflows/integration.yml/badge.svg)
![versions](https://img.shields.io/pypi/pyversions/dotserve.svg)
[![Documentaiton](https://img.shields.io/badge/Documentation%20-Introduction%20-%20%23007ec6)](https://dotagent.dev/docs/getting-started/introduction)
[![Discord](https://img.shields.io/discord/1029853095527727165?color=%237289da&label=Discord)](https://discord.gg/T5WSbC2YtQ)
</div>

---
[English](https://github.com/dot-agent/dotserve/blob/main/README.md) | [简体中文](https://github.com/dot-agent/dotserve/blob/main/docs/zh/zh_cn/README.md) | [繁體中文](https://github.com/dot-agent/dotserve/blob/main/docs/zh/zh_tw/README.md) | [Türkçe](https://github.com/dot-agent/dotserve/blob/main/docs/tr/README.md)
---
## ⚙️ İndirme

Bir terminal açın ve çalıştırın (Python 3.7+ gerekir):

```bash
pip install dotserve
```

## 🥳 İlk uygulamanı oluştur

`dotserve`'i indirmek ayrıca `dotserve` komut satırı aracınıda indirir.

Yeni bir proje oluşturarak kurulumun başarılı olup olmadığını test edin. (`my_app_name`'i proje adın ile değiştir.):

```bash
mkdir my_app_name
cd my_app_name
dotserve init
```

Bu komut, yeni dizininizde şablon uygulamasını başlatır.

Bu uygulamayı geliştirme modunda başlatabilirsiniz:

```bash
dotserve run
```

Uygulamanızın http://localhost:3000 adresinde çalıştığını görmelisiniz.

Şimdi `my_app_name/my_app_name.py` yolundaki kaynak kodu düzenleyebilirsiniz. Dotserve'in hızlı yenileme özelliği vardır, böylece kodunuzu kaydettiğinizde değişikliklerinizi anında görebilirsiniz.


## 🫧 Örnek Uygulama

Bir örnek üzerinden gidelim: DALL·E kullanarak bir görüntü oluşturma uygulaması yazalım. Basit olması açısından, yalnızca OpenAI API'sini çağırıyoruz, ancak bunu yerel olarak çalıştırılan bir makine öğrenimi modeliyle değiştirebilirsiniz.

&nbsp;

<div align="center">
<img src="https://raw.githubusercontent.com/dotserve-dev/dotserve/main/docs/images/dalle.gif" alt="A frontend wrapper for DALL·E, shown in the process of generating an image." width="550" />
</div>

&nbsp;

İşte bunu oluşturmak için kodun tamamaı. Bu sadece bir Python dosyasıyla gerçekleşti!

```python
import dotserve as ds
import openai

openai.api_key = "YOUR_API_KEY"

class State(ds.State):
    """The app state."""
    prompt = ""
    image_url = ""
    processing = False
    complete = False

    def get_image(self):
        """Get the image from the prompt."""
        if self.prompt == "":
            return ds.window_alert("Prompt Empty")

        self.processing, self.complete = True, False
        yield
        response = openai.Image.create(prompt=self.prompt, n=1, size="1024x1024")
        self.image_url = response["data"][0]["url"]
        self.processing, self.complete = False, True
        

def index():
    return ds.center(
        ds.vstack(
            ds.heading("DALL·E"),
            ds.input(placeholder="Enter a prompt", on_blur=State.set_prompt),
            ds.button(
                "Generate Image",
                on_click=State.get_image,
                is_loading=State.processing,
                width="100%",
            ),
            ds.cond(
                State.complete,
                     ds.image(
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
app = ds.App()
app.add_page(index, title="dotserve:DALL·E")
app.compile()
```

## Hadi bunu parçalara ayırarak inceleyelim.

### **Dotserve UI**

Hadi UI (Kullanıcı Arayüzü) ile başlayalım.

```python
def index():
    return ds.center(
        ...
    )
```

Bu `index` fonkisyonu uygulamanın frontend'ini tanımlar.

Farklı bileşenler kullanıyoruz misal `center`, `vstack`, `input`, ve `button` frontend'i oluşturmak için kullanıyoruz. Bileşenler birbirinin içine yerleştirilebilir
karmaşık düzenler oluşturmak için. Ayrıca bunları CSS'nin tüm gücüyle şekillendirmek için args'ı kullanabilirsiniz.

Dotserve size yardım için [60'tan fazla yerleşik bileşen](https://dotagent.dev/docs/library) içerir. Aktif olarak çok daha fazla yeni bileşen ekliyoruz, ve bunları oluşturmak çok kolay [Kendi bileşenlerinizi oluşturun](https://dotagent.dev/docs/advanced-guide/wrapping-react).

### **Durum**

Dotserve, UI durumunuzun fonksiyonu olarak temsil eder.

```python
class State(ds.State):
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
        return ds.window_alert("Prompt Empty")

    self.processing, self.complete = True, False
    yield
    response = openai.Image.create(prompt=self.prompt, n=1, size="1024x1024")
    self.image_url = response["data"][0]["url"]
    self.processing, self.complete = False, True
```

Durum içinde, durum değişkenlerini değiştiren olay işleyicileri (Event handler) adı verilen işlevleri tanımlarız. Olay işleyicileri, Dotserve'te durumu değiştirebilmemizin yoludur. Bir düğmeye tıklamak veya bir metin kutusuna yazmak gibi kullanıcı eylemlerine yanıt olarak çağrılabilirler. Bu eylemlere olay denir.

Oluşturduğumuz DALL·E uygulamasının olay işleyicisine sahip, `get_image` OpenAI API'dan oluşturulan resmi alır. Bir olay işleyicisinin ortasında `yield`in kullanılması UI'ın güncellenmesine neden olur. Aksi takdirde UI olay işleyicisinin sonunda güncellenecektir.

### **Routing (Yönlendirme)**

En sonunda uygulamamızı tanımlarız.

```python
app = ds.App()
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

Dotserve, Aralık 2022'de Pynecone adıyla piyasaya sürüldü.

Temmuz 2023 itibarıyla **Herkese Açık Beta** aşamasındayız.

-   :white_check_mark: **Public Alpha**: Herkes Dotserve'i yükleyebilir ve kullanabilir. Sorunlar olabilir, ancak bunları aktif olarak çözmek için çalışıyoruz.
-   :large_orange_diamond: **Public Beta**: Kurumsal olmayan kullanım durumları için yeterince kararlı.
-   **Public Hosting Beta**: _Optionally_, uygulamalarınızı Dotserve ile dağıtın ve barındırın!
-   **Public**: Dotserve ürünü hazır.

Dotserve'in her hafta yeni sürümleri ve özellikleri geliyor! Güncel kalmak için :star: yıldızlamayı ve bu depoyu :eyes: izlediğinizden emin olun.

## Katkı

Her boyuttaki katkıları memnuniyetle karşılıyoruz! Aşağıda Dotserve topluluğuna başlamanın bazı iyi yolları verilmiştir.

-   **Discord Kanalımıza Katılın**: [Discord'umuz](https://discord.gg/T5WSbC2YtQ), Dotserve projeniz hakkında yardım almak ve nasıl katkıda bulunabileceğinizi tartışmak için en iyi yerdir.
-   **GitHub Discussions**: Eklemek istediğiniz özellikler veya kafa karıştırıcı veya açıklığa kavuşturulması gereken şeyler hakkında konuşmanın harika bir yolu.
-   **GitHub Issues**: Bunlar hataları bildirmenin mükemmel bir yoludur. Ayrıca mevcut bir sorunu deneyip çözebilir ve bir PR (Pull Requests) gönderebilirsiniz.

Beceri düzeyiniz veya deneyiminiz ne olursa olsun aktif olarak katkıda bulunacak kişiler arıyoruz.

## Lisans

Dotserve açık kaynaklıdır ve [Apache License 2.0](LICENSE) altında lisanslıdır. 
