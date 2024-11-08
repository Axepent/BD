Розрахунково-графічна робота

Тема: Створення додатку бази даних, орієнтованого на взаємодію з СУБД PostgreSQL

Опис предметної області
Обрана предметна область - система обліку екзаменаційних балів студентів. Система має дозволити викладачам та студентам слідкувати за загальною успішністю студентів. Це допомагає формувати звіти про результати навчання та забезпечувати прозорість процесу оцінювання.

Опис сутностей:
1. Студент (Student)
     - `student_id` (первинний ключ)
     - `first_name` (ім’я)
     - `last_name` (прізвище)
     - `com_method` (спосіб комунікації)
Призначення: збереження даних про студентів

2. Викладач (Teacher)
     - `teacher_id` (первинний ключ)
     - `first_name` (ім’я)
     - `last_name` (прізвище)
     - `com_method ` (спосіб комунікації)
Призначення: збереження даних про викладачів
 
3. Іспит (Exam)
     - `exam_id` (первинний ключ)
     - `teacher_id` (посилання на вчителя)
     - `date` (дата проведення іспиту)
Призначення: збереження даних про іспити
 
4. Оцінка (Grade)
     - `student_id` (посилання на студента)
     - `exam_id` (посилання на іспит)
     - `grade_value` (оцінка студента, числове значення) 
Призначення: збереження оцінок студентів за конкретні іспити
