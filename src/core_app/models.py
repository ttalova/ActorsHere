from django.core.validators import RegexValidator
from django.db import models

from authentication.models import User


class City(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


# class AdditionalPhoto(models.Model):
#     link = models.ImageField()


class Tag(models.Model):
    title = models.CharField()

    def __str__(self):
        return f"{self.title}"


# class ActorExperience(models.Model):
#     tag = models.ManyToManyField(Tag)
#     description = models.CharField()


class ProjectType(models.Model):
    type_of_project = models.CharField(max_length=255)


class EmployerProfile(models.Model):
    SPECIALIZATION = [
        ("acting_agency", "Актерское агенство"),
        ("film_company", "Кинокомпания"),
        ("film_studio", "Киностудия"),
        ("casting_agency", "Кастинг агенство"),
        ("concert_agency", "Концертное агенство"),
        ("casting_director", "Кастинг-директор"),
        ("modeling_agency", "Модельное агенство"),
        ("music_studio", "Музыкальная студия"),
        ("selection", "Подбор кадров"),
        ("producer", "Продюсер"),
        ("director", "Режиссер"),
        ("advertising_agency", "Рекламное агенство"),
        ("tv_channel", "Телеканал"),
        ("photo_studio", "Фото студия"),
        ("other", "Другое"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    photo = models.ImageField(blank=True, null=True)
    company_specialization = models.CharField(choices=SPECIALIZATION)
    description = models.CharField()
    approximate_location = models.CharField()
    phone_number = models.CharField(max_length=17)
    additional_phone_number = models.CharField(max_length=17, blank=True, null=True)
    webside = models.URLField(blank=True)
    email = models.EmailField()
    social_network = models.CharField(blank=True, null=True)
    rating = models.PositiveIntegerField(default=5)
    city = models.ForeignKey(City, on_delete=models.RESTRICT)


class ActorProfile(models.Model):
    EYE_COLOR = [
        ("not_choice", ""),
        ("blue", "Голубые"),
        ("gray", "Серые"),
        ("green", "Зеленые"),
        ("brown", "Карие"),
    ]
    GENDER = [("not_choice", ""), ("male", "Мужской"), ("female", "Женский")]
    BODY_TYPE = [
        ("not_choice", ""),
        ("thin", "Худощавое"),
        ("sports", "Спортивное"),
        ("average", "Среднее"),
        ("dense", "Плотное"),
        ("fat", "Полное"),
    ]
    FACE_TYPE = [
        ("not_choice", ""),
        ("oval", "Овальное"),
        ("round", "Круглое"),
        ("square", "Квадратное"),
    ]
    HAIR_COLOR = [
        ("not_choice", ""),
        ("blonde", "Блонд"),
        ("chestnut", "Каштан"),
        ("dark_blonde", "Русые"),
        ("dark", "Темные"),
        ("redhead", "Рыжие"),
    ]
    HAIR_LENGTH = [
        ("not_choice", ""),
        ("bald", "Лысый"),
        ("short", "Короткие"),
        ("long", "Длинные"),
    ]
    VOICE_TIMBRE = [
        ("not_choice", ""),
        ("high", "Высокий"),
        ("low", "Низкий"),
    ]
    SKIN_COLOR = [
        ("not_choice", ""),
        ("white", "Белая"),
        ("swarthy", "Смуглая"),
        ("dark", "Темная"),
    ]
    IS_NOT = [
        ("not_choice", ""),
        ("exist", "Есть"),
        ("not_exist", "Нет"),
    ]
    BOOL_CHOICES = [
        (True, "Да"),
        (False, "Нет"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField()
    main_photo = models.ImageField(blank=True, null=True)
    birthdate = models.DateField()
    # video_business_card = models.CharField()
    figure_parameters = models.CharField(blank=True, null=True)
    height = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    clothing_size = models.PositiveIntegerField()
    shoe_size = models.PositiveIntegerField()
    eye_color = models.CharField(choices=EYE_COLOR)
    body_type = models.CharField(choices=BODY_TYPE)
    sex = models.CharField(choices=GENDER)
    face_type = models.CharField(choices=FACE_TYPE)
    hair_color = models.CharField(choices=HAIR_COLOR)
    hair_length = models.CharField(choices=HAIR_LENGTH)
    voice_timbre = models.CharField(choices=VOICE_TIMBRE)
    skin_color = models.CharField(choices=SKIN_COLOR)
    city = models.ForeignKey(City, on_delete=models.RESTRICT)
    tattoo = models.CharField(choices=IS_NOT)
    piercing = models.CharField(choices=IS_NOT)
    # photo_portfolio = models.ForeignKey(AdditionalPhoto, on_delete=models.SET_NULL, blank=True, null=True)
    education = models.CharField()
    language_proficiency = models.CharField()
    skills = models.CharField()
    # experience = models.ForeignKey(ActorExperience, on_delete=models.SET_NULL, blank=True, null=True)
    tag = models.ForeignKey(Tag, on_delete=models.RESTRICT)
    willing_to_relocate = models.BooleanField(choices=BOOL_CHOICES)
    international_passport = models.BooleanField(choices=BOOL_CHOICES)
    driver_license = models.BooleanField(choices=BOOL_CHOICES)
    phone_number = models.CharField(max_length=17, blank=True, null=True)
    email = models.EmailField()
    social_network = models.CharField(blank=True, null=True)
    form_active = models.BooleanField(default=True)
    rating = models.PositiveIntegerField(default=5)


class Casting(models.Model):
    GENDER = [("not_choice", ""), ("male", "Мужской"), ("female", "Женский"), ("all", "Все")]
    casting_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    project_type = models.ForeignKey(ProjectType, on_delete=models.RESTRICT)
    city = models.ForeignKey(City, on_delete=models.RESTRICT)
    photo = models.ImageField(null=True, blank=True)
    header = models.CharField()
    fee = models.CharField()
    description = models.CharField()
    # additional_photo = models.ForeignKey(AdditionalPhoto, on_delete=models.SET_NULL, blank=True, null=True)
    sex = models.CharField(choices=GENDER)
    experience = models.CharField()
    contact_email = models.EmailField()
    social_network = models.CharField(blank=True, null=True)
    actor_type_description = models.CharField()
    min_actor_age = models.IntegerField(blank=True, null=True)
    max_actor_age = models.IntegerField(blank=True, null=True)
    tag = models.ForeignKey(Tag, on_delete=models.RESTRICT)
    end_of_application = models.DateField()
    date_of_event = models.DateField()
    phone_number = models.CharField(max_length=17, blank=True, null=True)
    moderation = models.BooleanField(default=False)


class Response(models.Model):
    casting = models.ForeignKey(Casting, on_delete=models.CASCADE)
    actor = models.ForeignKey(ActorProfile, on_delete=models.CASCADE)
    response_time = models.DateTimeField()


class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    casting = models.ForeignKey(Casting, on_delete=models.CASCADE, null=True)
    actor = models.ForeignKey(ActorProfile, on_delete=models.CASCADE, null=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
