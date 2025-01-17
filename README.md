<h2>Описание</h2>
<p>Данное приложение представляет собой графический интерфейс для сортировки объектов по цветам. Пользователь вводит набор объектов, назначает им цвета и выполняет сортировку на основе заложенного правила цветов: Зеленый < Синий < Красный.</p>

<hr>

<h2>Ссылки</h2>
<ul>
    <li><strong>Чек-лист:</strong> <a href="https://docs.google.com/document/d/17IkkaxmFvzNodCEWGkXrRwsJZ1ZaZgn9cBp6aWQftgs/edit?tab=t.0#heading=h.seipgjc5c51n">Чек-лист</a></li>
    <li><strong>Тест-кейсы:</strong> <a href="https://docs.google.com/spreadsheets/d/1AbbZ-xXJiHfgHLvk5ox48bgdBeKxFwsahPt0NOEB0-w/edit?gid=0#gid=0">Тест-кейсы</a></li>
    <li><strong>Серые зоны:</strong> <a href="https://docs.google.com/document/d/1iUb2P9UnKwGvlqWy0ZryPdetEJLW_mClc4WnEBS269Y/edit?tab=t.0">Серые зоны</a></li>
</ul>

<hr>

<h2>Установка и запуск</h2>

<h3>1. Установка зависимостей</h3>
<p>Перед запуском убедитесь, что у вас установлен Python (версия 3.11 или выше). Установите необходимые библиотеки:</p>
<pre><code>poetry install</code></pre>

<h3>2. Запуск приложения</h3>
<p>Для запуска приложения используйте следующую команду:</p>
<pre><code>python app.py</code></pre>

<h3>3. Запуск тестов</h3>
<p>Для запуска юнит-тестов используйте следующую команду:</p>
<pre><code>python -m unittest test_app.py</code></pre>

<hr>

<h2>Основные функции</h2>

<h3>1. Назначение цветов</h3>
<ul>
    <li>Введите объекты через пробел для каждого цвета в соответствующие поля.</li>
    <li>Нажмите кнопку "Назначить цвета".</li>
</ul>

<h3>2. Сортировка объектов</h3>
<ul>
    <li>Введите полный набор объектов через пробел в соответствующее текстовое поле.</li>
    <li>Нажмите кнопку "Сортировать".</li>
    <li>Результат сортировки будет отображён внизу интерфейса с цветовой маркировкой.</li>
</ul>

<hr>

<h2>Описание тестов</h2>

<h3>Тесты для функционала</h3>
<ol>
    <li><strong>Тест базовой сортировки:</strong> Проверяет корректную сортировку объектов при полном вводе данных.</li>
    <li><strong>Тест пустого ввода:</strong> Проверяет обработку случая, когда поле ввода пустое.</li>
    <li><strong>Тест отсутствия цветов для некоторых объектов:</strong> Проверяет, что программа выдаёт ошибку при отсутствии цвета для некоторых объектов.</li>
    <li><strong>Тест частичного ввода:</strong> Проверяет поведение, если вводится не полный набор объектов.</li>
    <li><strong>Тест одного цвета для всех объектов:</strong> Проверяет сортировку, если все объекты одного цвета.</li>
</ol>

<hr>

<h2>Баг-репорт</h2>
<ul>
    Исходя из требований, в программе не было обнаружено багов. Поэтому, я смоделировал во время разработки один баг и занес его в <a href="https://docs.google.com/spreadsheets/d/1AbbZ-xXJiHfgHLvk5ox48bgdBeKxFwsahPt0NOEB0-w/edit?gid=0#gid=0">Тест-кейсы</a> под номером 7 и завел для него <a href="https://docs.google.com/document/d/1eP8n9qOx63wXVBKCgLOMTY44LNsNtEaT6ZvckPfuFJw/edit?tab=t.0">Баг-репорт</a>

</ul>
