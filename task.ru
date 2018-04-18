## Translate by GoogleTranslate

Цель этой задачи - создать в Django простую социальную сеть на основе REST API и
Создайте бота, который демонстрирует функциональность системы в соответствии с определенными правилами.
Социальная сеть

Основные модели:
● Пользователь
● Сообщение (всегда сделанное пользователем)
Основные характеристики:
● регистрация пользователя
● вход в систему пользователя
● создание сообщения
● понравилось сообщение
● Мне не понравилось сообщение
Для объектов «Пользователь» и «Сообщение» кандидат может определять атрибуты по своему усмотрению.

Требования:
● Аутентификация маркера (рекомендуется JWT)
● Используйте Django с любыми другими батареями Django, базами данных и т. Д.
Необязательный (будет плюсом):
● использовать clearbit.com/enrichment для получения дополнительных данных для пользователя при регистрации
● используйте emailhunter.co, чтобы проверить наличие электронной почты при регистрации

Автоматический бот
Этот бот должен прочитать правила из файла конфигурации (в любом формате, выбранном кандидатом), но
должны иметь следующие поля (все целые числа, кандидат может переименовать по своему усмотрению):
● number_of_users
● max_posts_per_user
● max_likes_per_user
Бот должен прочитать конфигурацию и создать эту операцию:
● пользователи регистрации (номер, указанный в конфиге)
● каждый пользователь создает случайное количество сообщений с любым контентом (до max_posts_per_user)
● После создания регистрации и публикации сообщения следует сортировать случайным образом, сообщения
может понравиться это несколько раз

Заметки
● emailhunter и clearbit имеют либо бесплатные тарифные планы, либо бесплатную пробную версию, кандидат может
использовать вашу собственную учетную запись, если она хочет реализовать функциональность
● визуальный аспект проекта не важен, кандидат может создать интерфейс для
просматривая результат, но он не нужен (это будет плюс). Чистый и полезный REST API очень важен
● Проект не уточняется подробно, кандидат должен использовать свое лучшее решение для
все не указанные требования (включая выбранные технологии, сторонние приложения и т. д.)
но
● каждое решение должно быть объяснено и подтверждено аргументами в интервью
● Результат должен быть отправлен, указав Git URL. Это обязательное требование.