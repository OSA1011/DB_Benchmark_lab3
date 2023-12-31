# Лабораторная работа №3
## Описание лабораторной работы
Задачей данной лабораторной работы является написание бенчмарка для измерения производительности при 4 запросах на 4 различных библиотеках на языке Python (psycopg2, SQLite, DuckDB, Pandas).
## Ход работы
Работа выполнялась на языке Python с использование вышеуказанных библиотек на двух наборах данных о поездках такси в городе Нью Йорк. Бенчмарк включает в себя 4 запроса, каждый из которых запускался 11 раз для более точной статистики.
* Первый запрос
```
SELECT cab_type, count(*)
FROM trips
GROUP BY 1;
```
* Второй запрос
```
SELECT passenger_count, avg(total_amount) 
FROM trips 
GROUP BY 1;
```
* Третий запрос
```
SELECT
   passenger_count, 
   extract(year from pickup_datetime),
   count(*)
FROM trips
GROUP BY 1, 2;
```
* Четвертый запрос
```
SELECT
    passenger_count,
    extract(year from pickup_datetime),
    round(trip_distance),
    count(*)
FROM trips
GROUP BY 1, 2, 3
ORDER BY 2, 4 desc;
```
**В результате получены следующие графики:**
### nyc_yellow_tiny.csv
![chart (2)](https://github.com/OSA1011/DB_Benchmark_lab3/assets/154271338/1f08b13c-2b48-4732-aa05-1ed363e95904)

### nyc_yellow_big.csv
![chart (1)](https://github.com/OSA1011/DB_Benchmark_lab3/assets/154271338/b02d828b-d2ca-41cf-be73-e6ae7592ac3c)

## Выводы
• Графики показывают, что библиотека Pandas работает быстрее всего, но у неё есть свои недостатки. Она загружает всю базу данных в оперативную память, что является длительным процессом и не учитывалось во время тестов.

• Также можно заметить, что самой медленной библиотекой является SQLite.

• При простых запросах и небольшом количестве данных для обработки библиотека psycopg2 показывает хорошие результаты. Однако с увеличением сложности запросов и объема обрабатываемых данных библиотека DuckDB проявляет себя гораздо лучше.

• При запуске тестов на большом количестве данных (с большим файлом данных) при усложнении условий запросов скорость библиотеки DuckDB почти не меняется.

Таким образом, если доступен значительный объем памяти, то использование Pandas будет выгодным. Однако, поскольку базы данных могут быть очень большими, необходимо выбирать более оптимальный вариант. Для обработки огромного объема данных логично использовать psycopg2, поскольку она показала себя лучше всего. Однако, если данных не так много и также есть проблемы с памятью, то выгодно будет использовать DuckDB.
