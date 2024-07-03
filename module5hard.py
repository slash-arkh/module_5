import time


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class User:
    def __init__(self, login, password, age):
        self.login = login
        self.password = password
        self.age = age

    def __str__(self):
        return self.login



class UrTube:
    def __init__(self, *args):
        self.users = []
        self.videos = []
        self.current_user = None


    def log_in(self, login, password):
        for user in self.users:
            if user.login == login and user.password == password:
                self.current_user = user
        print('"Не верный логин или пароль"')
        # Если логин и пароль совпадает, то - Вход

    def register(self, login, password, age):
        for user in self.users:
            if user.login == login:
                print(f"Пользователь {login} уже существует")
                return
        new_user = User(login, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        if self.current_user:
            self.current_user = None
            print(f'"Пользователь {self.current_user.login} вышел из системы"')

    def add(self, *videos):
        for video in videos:
            # Нужно добавлять неограниченное количество объектов
            # и проверять дублирование видео по заголовку.
            if all(existing_video.title != video.title for existing_video in self.videos):
                self.videos.append(video)

    def get_videos(self, word):
        word = word.lower()
        # search_result = [video.title for video in self.videos if word in video.title.lower()]
        search_result = []
        for video in self.videos:
            if word in video.title.lower():
                search_result.append(video.title)
        return search_result

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                for second in range(video.time_now, video.duration):
                    print(f"Просмотр {second + 1} секунды видео")
                    time.sleep(1)
                video.time_now = 0
                print("Конец видео")
                return
        # print(f"Видео с названием {title} не найдено.")



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

# Нужно добавить метод __str__ для вывода информации о текущем пользователе.
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

