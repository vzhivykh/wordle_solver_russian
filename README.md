# wordle_solver_russian
Simple Russian Wordle Solver

Проверено на Python 3.10.8
Словарь основан на https://github.com/danakt/russian-words

Предполагается запуск после ввода пары слов в игре.

Сначала нужно ввести буквы (слитно), которые не должны присутствовать в загаданном слове, например "язь".

Потом нужно ввести буквы (слитно), которые должны присутствовать в загаданном слове, например "бро".

Потом нужно ввести kind of regexp выражение, отображающее известныее позиции букв, присутствующих в слове, например "б\*ро\*", где "\*" - любая буква.

В конце будет выдан список возможных слов.