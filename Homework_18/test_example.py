import pytest
import random
@pytest.fixture
def random_numbers():
    """Фикстура, возвращающая случайный список из 10 чисел."""
    yield [random.randint(1, 300) for i in range(10)]
    print('\nРабота фикстуры')

@pytest.mark.len
def test_len(random_numbers):
    assert len(random_numbers) == 10
@pytest.mark.skip (reason = 'Тестовый пропуск')
def test_sum(random_numbers):
    assert sum(random_numbers) >= 200
@pytest.mark.sorted
def test_sorted(random_numbers):
    sorted_list = sorted(random_numbers)
    print("Отсортированный список:", sorted_list)
    assert sorted_list == sorted(random_numbers), "Должен быть возвращен отсортированный список"

@pytest.mark.xfail(reason = "Ожидаемо провален")
def test_even_numbers(random_numbers):
    """Тест на то, что все числа в списке четные."""
    even_numbers = all(num % 2 == 0 for num in random_numbers)
    assert even_numbers, "Не все числа в списке четные"
@pytest.mark.critical
def test_odd_numbers(random_numbers):
    """Тест, проверяющий, что в списке  нечетных числf."""
    odd_numbers = all(num % 2 != 0 for num in random_numbers)
    assert odd_numbers, "Не все числа в списке нечетные"
