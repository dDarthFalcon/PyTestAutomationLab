import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# Позитивные тесты
@pytest.mark.positive_test
@pytest.mark.test_capitilize
def test_capitilize_positive():
    assert string_utils.capitilize("skypro") == "Skypro"
    assert string_utils.capitilize("SkyPro") == "Skypro"
    assert string_utils.capitilize("sKYPRO") == "Skypro"
    assert string_utils.capitilize("") == ""  # Пустая строка
    assert string_utils.capitilize("небо") == "Небо"  # Русский текст
    assert string_utils.capitilize("天空") == "天空"  # Китайский текст
    assert string_utils.capitilize("123") == "123"  # Число
    assert string_utils.capitilize("!@#") == "!@#"  # Спецсимволы

@pytest.mark.positive_test
@pytest.mark.test_trim
def test_trim_positive():
    assert string_utils.trim("   skypro") == "skypro"
    assert string_utils.trim("skypro") == "skypro"
    assert string_utils.trim("   ") == ""  # Пустая строка из пробелов
    assert string_utils.trim("") == ""  # Пустая строка
    assert string_utils.trim("   небо") == "небо"  # Русский текст
    assert string_utils.trim("天空") == "天空"  # Китайский текст
    assert string_utils.trim(" 123") == "123"  # Число
    assert string_utils.trim(" !@#") == "!@#"  # Спецсимволы
    assert string_utils.trim(" skypro") == "skypro"  # Один лишний пробел
    assert string_utils.trim("  skypro") == "skypro"  # Два лишних пробела
    assert string_utils.trim(" " * 100 + "skypro") == "skypro"  # 100 лишних пробелов

@pytest.mark.positive_test
@pytest.mark.test_to_list
def test_to_list_positive():
    assert string_utils.to_list("a") == ["a"]
    assert string_utils.to_list("a,b") == ["a", "b"]
    assert string_utils.to_list("1:2:3", ":") == ["1", "2", "3"]
    assert string_utils.to_list("") == []  # Пустая строка
    assert string_utils.to_list("a b c", " ") == ["a", "b", "c"]
    assert string_utils.to_list("н,е,б,о") == ["н", "е", "б", "о"]  # Русский текст
    assert string_utils.to_list("天:空", ":") == ["天", "空"]  # Китайский текст
    assert string_utils.to_list("1,2,3") == ["1", "2", "3"]  # Число
    assert string_utils.to_list("!,@,#") == ["!", "@", "#"]  # Спецсимволы

@pytest.mark.positive_test
@pytest.mark.test_contains
def test_contains_positive():
    assert string_utils.contains("SkyPro", "S") is True
    assert string_utils.contains("SkyPro", "U") is False
    assert string_utils.contains("", "S") is False  # Пустая строка
    assert string_utils.contains("SkyPro", "") is True  # Пустой символ
    assert string_utils.contains("небо", "н") is True  # Русский текст
    assert string_utils.contains("天空", "天") is True  # Китайский текст
    assert string_utils.contains("12345", "2") is True  # Число
    assert string_utils.contains("!@#", "@") is True  # Спецсимволы
    assert string_utils.contains("A", "A") is True  # 1 буква
    assert string_utils.contains("SkyPro", "Sky") is True # Несколько букв
@pytest.mark.positive_test
@pytest.mark.test_delete_symbol
def test_delete_symbol_positive():
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert string_utils.delete_symbol("SkyPro", "Pro") == "Sky"
    assert string_utils.delete_symbol("SkyPro", "") == "SkyPro"  # Пустой символ
    assert string_utils.delete_symbol("", "Pro") == ""  # Пустая строка
    assert string_utils.delete_symbol("небо", "е") == "нбо"  # Русский текст
    assert string_utils.delete_symbol("天空", "空") == "天"  # Китайский текст
    assert string_utils.delete_symbol("12345", "2") == "1345"  # Число
    assert string_utils.delete_symbol("!@#", "@") == "!#"  # Спецсимволы

@pytest.mark.positive_test
@pytest.mark.test_starts_with
def test_starts_with_positive():
    assert string_utils.starts_with("SkyPro", "S") is True
    assert string_utils.starts_with("SkyPro", "P") is False
    assert string_utils.starts_with("", "S") is False  # Пустая строка
    assert string_utils.starts_with("SkyPro", "") is True  # Пустой символ
    assert string_utils.starts_with("небо", "н") is True  # Русский текст
    assert string_utils.starts_with("天空", "天") is True  # Китайский текст
    assert string_utils.starts_with("12345", "1") is True  # Число
    assert string_utils.starts_with("!@#", "!") is True  # Спецсимволы

@pytest.mark.positive_test
@pytest.mark.test_end_with
def test_end_with_positive():
    assert string_utils.end_with("SkyPro", "o") is True
    assert string_utils.end_with("SkyPro", "y") is False
    assert string_utils.end_with("", "o") is False  # Пустая строка
    assert string_utils.end_with("SkyPro", "") is True  # Пустой символ
    assert string_utils.end_with("небо", "о") is True  # Русский текст
    assert string_utils.end_with("天空", "空") is True  # Китайский текст
    assert string_utils.end_with("12345", "5") is True  # Число
    assert string_utils.end_with("!@#", "#") is True  # Спецсимволы

@pytest.mark.positive_test
@pytest.mark.test_is_empty
def test_is_empty_positive():
    assert string_utils.is_empty("") is True
    assert string_utils.is_empty(" ") is True
    assert string_utils.is_empty("SkyPro") is False
    assert string_utils.is_empty("  SkyPro  ") is False
    assert string_utils.is_empty("небо") is False  # Русский текст
    assert string_utils.is_empty("天空") is False  # Китайский текст
    assert string_utils.is_empty("12345") is False  # Число
    assert string_utils.is_empty("!@#") is False  # Спецсимволы

@pytest.mark.positive_test
@pytest.mark.test_list_to_string
def test_list_to_string_positive():
    assert string_utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
    assert string_utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"
    assert string_utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"
    assert string_utils.list_to_string(["н", "е", "б", "о"]) == "н, е, б, о"  # Русский текст
    assert string_utils.list_to_string(["天", "空"]) == "天, 空"  # Китайский текст
    assert string_utils.list_to_string([1, 2, 3], ":") == "1:2:3"  # Число
    assert string_utils.list_to_string(["!", "@", "#"]) == "!, @, #"  # Спецсимволы
    assert string_utils.list_to_string(["Всем", "доброе", "утро"], " ") == "Всем доброе утро"  # Текст с пробелами

# Негативные тесты

@pytest.mark.negative_test
@pytest.mark.test_capitilize
def test_capitilize_negative():
    with pytest.raises(AttributeError):
        string_utils.capitilize(None)

@pytest.mark.negative_test
@pytest.mark.test_trim
def test_trim_negative():
    with pytest.raises(AttributeError):
        string_utils.trim(None)

@pytest.mark.negative_test
@pytest.mark.test_contains
def test_contains_negative():
    assert string_utils.contains("", "S") is False  # Пустая строка
    assert string_utils.contains("SkyPro", "") is True  # Пустой символ
    assert string_utils.contains("SkyPro", "Sy") is False  # Несколько символов, из которых правильный только первый
    assert string_utils.contains("SkyPro", "to") is False  # Несколько символов, из которых правильный только последний
    with pytest.raises(TypeError):
        string_utils.contains(None)

@pytest.mark.negative_test
@pytest.mark.test_to_list
def test_to_list_positive():
    assert string_utils.to_list("a,b", ":") == ["a,b"]  # Разделитель не найден
    assert string_utils.to_list("", ":") == []  # Пустая строка
    with pytest.raises(AttributeError):
        string_utils.to_list(None)

@pytest.mark.negative_test
@pytest.mark.test_delete_symbol
def test_delete_symbol_negative():
    assert string_utils.delete_symbol("SkyPro", "") == "SkyPro"  # Пустой символ
    assert string_utils.delete_symbol("", "Pro") == ""  # Пустая строка
    with pytest.raises(AttributeError):
        string_utils.delete_symbol(None, "")

@pytest.mark.negative_test
@pytest.mark.test_starts_with
def test_starts_with_negative():
    assert string_utils.starts_with("", "S") is False  # Пустая строка
    assert string_utils.starts_with("SkyPro", "") is True  # Пустой символ
    
@pytest.mark.negative_test
@pytest.mark.test_end_with
def test_end_with_negative():
    assert string_utils.end_with("", "o") is False  # Пустая строка
    assert string_utils.end_with("SkyPro", "") is True  # Пустой символ

@pytest.mark.negative_test
@pytest.mark.test_list_to_string
def test_list_to_string_negative():
    assert string_utils.list_to_string([]) == ""  # Пустой список
    assert string_utils.list_to_string([1]) == "1"  # Список из одного элемента
    with pytest.raises(TypeError):
        string_utils.list_to_string(None)
