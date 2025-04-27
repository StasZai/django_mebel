from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField("Категория", max_length=150)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Characteristics(models.Model):
    name = models.CharField("Характеристика", max_length=100)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Характеристика"
        verbose_name_plural = "Характеристики"


class Branch(models.Model):
    name = models.CharField("Филиал", max_length=100)
    adds = models.CharField("Адрес", max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Филлиал"
        verbose_name_plural = "Филлиалы"


class Mebel(models.Model):
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    poster = models.ImageField("Постер", upload_to="mebel/")
    year = models.PositiveSmallIntegerField("Дата выхода", default=2025)
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True
    )
    characteristics = models.ManyToManyField(Characteristics, verbose_name="характеристики", null=True)
    # characteristics = models.ForeignKey(Characteristics, verbose_name="характеристика", on_delete=models.SET_NULL, null=True)
    is_new = models.BooleanField("Новинка", default=False)
    is_hit = models.BooleanField("Хит продаж", default=False)
    is_sale = models.BooleanField("Акция", default=False)
    branch = models.ForeignKey(Branch,verbose_name="Филлиал", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('mebel_detail', kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Мебель"
        verbose_name_plural = "Мебель"


class MebelAngles(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    image = models.ImageField("Изображение", upload_to="mebel_shots/")
    mebel = models.ForeignKey(Mebel, verbose_name="Фильм", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Ракурсы мебели"
        verbose_name_plural = "Ракурсы мебели"


class RatingStar(models.Model):
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"


class Slides(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    image = models.ImageField("Изображение", upload_to="slides/")
    url = models.ForeignKey(Mebel, verbose_name="Ссылка", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Слайд"
        verbose_name_plural = "Слайды"


class Rating(models.Model):
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    mebel = models.ForeignKey(Mebel, on_delete=models.CASCADE, verbose_name="мебель")

    def __str__(self):
        return f"{self.star} - {self.mebel}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    mebel = models.ForeignKey(Mebel, verbose_name="фильм", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.mebel}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"