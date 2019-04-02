## Профессия "Системный аналитик"

#### Основные обязанности

* Сбор бизнес- и пользовательских требований, анализ, формализация, проверка и документирование;
* Разработка требований к программному продукту;
* Проработка сценариев использования;
* Моделирование требований;
* Разработка тесткейсов;
* Проектирование и макетирование пользовательских интерфейсов;
* Валидация разработанного ПО на соответствие ТЗ.

#### Основные требования

* Опыт работы бизнес / системным аналитиком в области разработки ПО от 3 лет;
* Высшее образование, желательно в области математики или информационных технологий;
* Грамотная письменная речь;
* Опыт создания моделей данных, структуры БД, диаграмм «сущность — связь»;
* Способность быстро разобраться в новой предметной области;
* Аналитический склад ума, самодисциплина.

### Датасет

#### Загрузка
```bash
$ git clone https://github.com/interlark/system-analytics && cd system-analytics
```

#### Подготовка
```bash
$ python3 extend_csv.py merged.py merged_extended.csv
```

#### Описание
| ID_VUZ             | Наименование       | Город       | Адрес       | Телефон                    | Почта         | Сайт                   | Описание ВУЗа           | ID_PROG                                        | Специальность               | Квалификация  | Форма обучения  | Описание программы          | Основные дисциплины                | Дисциплины по выбору                           | 
|--------------------|--------------------|-------------|-------------|----------------------------|---------------|------------------------|-------------------------|------------------------------------------------|-----------------------------|---------------|-----------------|-----------------------------|------------------------------------|------------------------------------------------| 
| Идентификатор ВУЗа |  Наименование ВУЗа |  Город ВУЗа |  Адрес ВУЗа |  Телефон для связи с ВУЗом |  E-mail  ВУЗа |  Официальный сайт ВУЗа |  Короткое описание ВУЗа |  Идентификатор Программы подготовки сециалиста |  Наименование специальности |  Квалификация |  Форма обучения |  Описание программы от ВУЗа |  Основные дисциплины специальности |  Дисциплины по выбору студентов (если имеются) | 

```python
import pandas as pd
df = pd.read_csv('merged_extended.csv')
df.info()
```
```bash
RangeIndex: 135590 entries, 0 to 135589
Data columns (total 15 columns):
ID_VUZ                  135590 non-null int64
Наименование            135590 non-null object
Город                   135590 non-null object
Адрес                   135590 non-null object
Телефон                 135590 non-null object
Почта                   135590 non-null object
Сайт                    135590 non-null object
Описание ВУЗа           135590 non-null object
ID_PROG                 135590 non-null int64
Специальность           135590 non-null object
Квалификация            135590 non-null object
Форма обучения          135590 non-null object
Описание программы      125806 non-null object
Основные дисциплины     131925 non-null object
Дисциплины по выбору    14820 non-null object
dtypes: int64(2), object(13)
memory usage: 15.5+ MB

```

#### Типовой анализ
##### ТОП 10 основных предметов
```python
import pandas as pd
df = pd.read_csv('merged_extended.csv')
df['Основные дисциплины'].value_counts().head(10)
```

```bash
Базы данных                                  2524
Операционные системы                         2335
Информационная безопасность                  1193
Безопасность жизнедеятельности               1190
Объектно-ориентированное программирование    1093
Дискретная математика                        1062
Компьютерная графика                         1003
Защита информации                             924
Численные методы                              888
Математический анализ                         874
```
##### ТОП 10 программ подготовки
```python
import pandas as pd
df = pd.read_csv('merged_extended.csv')
df['Специальность'].value_counts().head(10)
```

```bash
Бизнес-информатика (5.38.03.05)                      22334
Прикладная информатика (2.09.03.03)                  20521
Информатика и вычислительная техника (2.09.03.01)    13875
Прикладная математика и информатика (1.01.03.02)     11464
Системный анализ и управление (2.27.03.03)           9013 
Прикладная математика (1.01.03.04)                   7888 
Управление в технических системах (2.27.03.04)       7848 
Информационные системы и технологии (2.09.03.02)     5666 
Математика и компьютерные науки (1.02.03.01)         5268 
Программная инженерия (2.09.03.04)                   5039 
```

##### ТОП ВУЗов по количеству программ подготовки специалистов
```python
import pandas as pd
df = pd.read_csv('merged_extended.csv')
df['Основные дисциплины'].value_counts().head(10)
df.groupby(['Наименование', 'Город'])\
    .count()\
    .sort_values(['Специальность', 'Город'], ascending=False)
```

```bash                                                                                                                                                                                                                        
Наименование                                                                                                                                                                                              Город            Специальность             
Белорусско-Российский университет                                                                                                                                                                         Москва           23           
Государственный университет "Дубна"                                                                                                                                                                       Москва           23           
Государственный университет управления                                                                                                                                                                    Москва           23           
Институт мировых цивилизаций                                                                                                                                                                              Москва           23           
МГСУ - Национальный исследовательский Московский государственный строительный университет                                                                                                                 Москва           23           
МГУ - Московский государственный университет имени М.В. Ломоносова                                                                                                                                        Москва           23           
МИРЭА – Российский технологический университет                                                                                                                                                            Москва           23           
Московская гуманитарно-техническая академия                                                                                                                                                               Москва           23           
Московский авиационный институт (национальный исследовательский университет) (МАИ)                                                                                                                        Москва           23           
Московский автомобильно-дорожный государственный технический университет                                                                                                                                  Москва           23           
Московский государственный гуманитарно-экономический университет                                                                                                                                          Москва           23           
Московский государственный областной университет                                                                                                                                                          Москва           23           
Московский государственный психолого-педагогический университет                                                                                                                                           Москва           23           
Московский государственный технический университет имени Н.Э. Баумана                                                                                                                                     Москва           23           
Московский государственный технологический университет «Станкин»                                                                                                                                          Москва           23           
Московский государственный университет пищевых производств                                                                                                                                                Москва           23           
Московский государственный университет технологий и управления им. К.Г. Разумовского (Первый казачий университет)                                                                                         Москва           23           
Московский инновационный университет                                                                                                                                                                      Москва           23           
Московский информационно-технологический университет – Московский архитектурно-строительный институт                                                                                                      Москва           23           
Московский открытый институт                                                                                                                                                                              Москва           23           
Московский педагогический государственный университет                                                                                                                                                     Москва           23           
Московский политехнический университет                                                                                                                                                                    Москва           23           
Московский технический университет связи и информатики                                                                                                                                                    Москва           23           
Московский университет им. С.Ю. Витте                                                                                                                                                                     Москва           23           
Московский физико-технический институт (государственный университет)                                                                                                                                      Москва           23           
Московский финансово-промышленный университет "Синергия"                                                                                                                                                  Москва           23           
Московский финансово-юридический университет                                                                                                                                                              Москва           23           
Московский экономический институт                                                                                                                                                                         Москва           23           
Мытищинский филиал Московского государственного технического университета имени Н.Э. Баумана (национального исследовательского университета)                                                              Москва           23           
НИУ ВШЭ - Национальный исследовательский университет "Высшая школа экономики"                                                                                                                             Москва           23           
Национальный исследовательский технологический университет «МИСиС»                                                                                                                                        Москва           23           
Национальный исследовательский университет "МИЭТ"                                                                                                                                                         Москва           23           
Национальный исследовательский университет "МЭИ"                                                                                                                                                          Москва           23           
Национальный исследовательский ядерный университет "МИФИ"                                                                                                                                                 Москва           23           
Одинцовский филиал Московского государственного института международных отношений (университета) Министерства иностранных дел Российской Федерации                                                        Москва           23           
Российская академия народного хозяйства и государственной службы при Президенте Российской Федерации                                                                                                      Москва           23           
Российский государственный аграрный университет - МСХА имени К.А. Тимирязева                                                                                                                              Москва           23           
Российский государственный геологоразведочный университет имени Серго Орджоникидзе                                                                                                                        Москва           23           
Российский государственный гуманитарный университет                                                                                                                                                       Москва           23           
Российский государственный социальный университет                                                                                                                                                         Москва           23           
Российский государственный университет им. А.Н. Косыгина (Технологии. Дизайн. Искусство)                                                                                                                  Москва           23           
Российский государственный университет нефти и газа (национальный исследовательский университет) имени И.М. Губкина                                                                                       Москва           23           
Российский новый университет                                                                                                                                                                              Москва           23           
Российский университет дружбы народов                                                                                                                                                                     Москва           23           
Российский университет кооперации                                                                                                                                                                         Москва           23           
Российский университет транспорта (МИИТ)                                                                                                                                                                  Москва           23           
Российский экономический университет имени Г.В. Плеханова                                                                                                                                                 Москва           23           
Финансовый университет при Правительстве Российской Федерации                                                                                                                                             Москва           23           
Балтийский государственный технический университет «ВОЕНМЕХ» имени Д.Ф. Устинова                                                                                                                          Санкт-Петербург  21           
Государственный университет морского и речного флота имени адмирала С.О. Макарова                                                                                                                         Санкт-Петербург  21           
Петербургский государственный университет путей сообщения Императора Александра I                                                                                                                         Санкт-Петербург  21           
Российский государственный гидрометеорологический университет                                                                                                                                             Санкт-Петербург  21           
Российский государственный педагогический университет имени А.И. Герцена                                                                                                                                  Санкт-Петербург  21           
СПБГУ - Санкт-Петербургский государственный университет                                                                                                                                                   Санкт-Петербург  21           
Санкт-Петербургский горный университет                                                                                                                                                                    Санкт-Петербург  21           
Санкт-Петербургский государственный архитектурно-строительный университет                                                                                                                                 Санкт-Петербург  21           
Санкт-Петербургский государственный морской технический университет                                                                                                                                       Санкт-Петербург  21           
Санкт-Петербургский государственный технологический институт (Технический университет)                                                                                                                    Санкт-Петербург  21           
Санкт-Петербургский государственный университет аэрокосмического приборостроения                                                                                                                          Санкт-Петербург  21           
Санкт-Петербургский государственный университет промышленных технологий и дизайна                                                                                                                         Санкт-Петербург  21           
Санкт-Петербургский государственный университет телекоммуникаций имени профессора М.А. Бонч-Бруевича                                                                                                      Санкт-Петербург  21           
Санкт-Петербургский государственный экономический университет                                                                                                                                             Санкт-Петербург  21           
Санкт-Петербургский государственный электротехнический университет "ЛЭТИ" имени В.И. Ульянова (Ленина)                                                                                                    Санкт-Петербург  21           
Санкт-Петербургский национальный исследовательский университет информационных технологий, механики и оптики                                                                                               Санкт-Петербург  21           
Санкт-Петербургский политехнический университет Петра Великого                                                                                                                                            Санкт-Петербург  21           
Санкт-Петербургский университет Государственной противопожарной службы Министерства Российской Федерации по делам гражданской обороны, чрезвычайным ситуациям и ликвидации последствий стихийных бедствий Санкт-Петербург  21           
Санкт-Петербургский филиал Национального исследовательского университета «Высшая школа экономики»                                                                                                         Санкт-Петербург  21           
Северо-Западный институт управления - филиал Российской академии народного хозяйства и государственной службы при Президенте Российской Федерации                                                         Санкт-Петербург  21           
Университет при Межпарламентской Ассамблее ЕврАзЭС                                                                                                                                                        Санкт-Петербург  21           
Казанский (Приволжский) федеральный университет                                                                                                                                                           Казань           12           
Казанский государственный аграрный университет                                                                                                                                                            Казань           12           
Казанский государственный энергетический университет                                                                                                                                                      Казань           12           
Казанский инновационный университет имени В.Г. Тимирясова                                                                                                                                                 Казань           12           
Казанский национальный исследовательский технический университет им. А.Н. Туполева-КАИ                                                                                                                    Казань           12           
Казанский национальный исследовательский технологический университет                                                                                                                                      Казань           12           
Университет Иннополис                                                                                                                                                                                     Казань           12           
Сибирский государственный университет науки и технологий им. М.Ф. Решетнева                                                                                                                               Красноярск       10           
Сибирский федеральный университет                                                                                                                                                                         Красноярск       10           
Ижевский государственный технический университет имени М. Т. Калашникова                                                                                                                                  Ижевск           10           
Камский институт гуманитарных и инженерных технологий                                                                                                                                                     Ижевск           10           
Удмуртский государственный университет                                                                                                                                                                    Ижевск           10           
Башкирский государственный педагогический университет им. М. Акмуллы                                                                                                                                      Уфа              9            
Башкирский государственный университет                                                                                                                                                                    Уфа              9            
Уфимский государственный авиационный технический университет                                                                                                                                              Уфа              9            
Уфимский филиал Финансового университета                                                                                                                                                                  Уфа              9            
Саратовский государственный технический университет имени Гагарина Ю.А.                                                                                                                                   Саратов          9            
Саратовский национальный исследовательский государственный университет имени Н.Г. Чернышевского                                                                                                           Саратов          9            
Саратовский социально-экономический институт (филиал) Российского экономического университета имени Г.В. Плеханова                                                                                        Саратов          9            
Поволжский государственный университет телекоммуникаций и информатики                                                                                                                                     Самара           9            
Самарский государственный технический университет                                                                                                                                                         Самара           9            
Самарский государственный университет путей сообщения                                                                                                                                                     Самара           9            
Самарский государственный экономический университет                                                                                                                                                       Самара           9            
Самарский национальный исследовательский университет имени академика С.П. Королева                                                                                                                        Самара           9            
Омский государственный технический университет                                                                                                                                                            Омск             9            
Омский государственный университет им. Ф.М. Достоевского                                                                                                                                                  Омск             9            
Омский государственный университет путей сообщения                                                                                                                                                        Омск             9            
Омский филиал Московского финансово-промышленного университета "Синергия"                                                                                                                                 Омск             9            
Сибирский государственный автомобильно-дорожный университет (СибАДИ)                                                                                                                                      Омск             9            
НГУ - Новосибирский национальный исследовательский государственный университет                                                                                                                            Новосибирск      9            
Новосибирский государственный архитектурно-строительный университет (Сибстрин)                                                                                                                            Новосибирск      9            
Новосибирский государственный технический университет                                                                                                                                                     Новосибирск      9            
Новосибирский государственный университет экономики и управления (НИНХ)                                                                                                                                   Новосибирск      9            
Сибирский государственный университет телекоммуникаций и информатики                                                                                                                                      Новосибирск      9            
Сибирский институт управления - филиал Российской академии народного хозяйства и государственной службы при Президенте Российской Федерации                                                               Новосибирск      9            
Сибирский университет потребительской кооперации                                                                                                                                                          Новосибирск      9            
Воронежский государственный аграрный университет имени императора Петра I                                                                                                                                 Воронеж          9            
Воронежский государственный технический университет                                                                                                                                                       Воронеж          9            
Воронежский государственный университет                                                                                                                                                                   Воронеж          9            
Воронежский институт высоких технологий                                                                                                                                                                   Воронеж          9            
Национальный исследовательский Томский государственный университет                                                                                                                                        Томск            8              
```
