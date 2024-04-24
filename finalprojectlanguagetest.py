import pytest
from finalprojectlanguage import read_categorized_translations, translate_svo

@pytest.fixture(scope="module")
def translations():
    return read_categorized_translations("/Users/sophiabeebe/Desktop/BYUI/Winter_2024/Programming_with_Fuctions/week_12final/translation.csv")

@pytest.mark.parametrize("sentence,expected_chi,expected_eng", [
   #lets test word for word 
    ("I", "我", "I"),
    ("eat", "吃", "eat"),
    ("food", "食物", "food"),
    # Testing the SVO sentence. Even if they put in random sentence structure.
    ("I cook wonton", "我做饭云吞", "I cook wonton"),
    ("You answer sherlock", "你回答神探夏洛克", "You answer sherlock"),
    ("tofu I like", "我喜欢豆腐", "I like tofu"),
])

def test_translate_svo(translations, sentence, expected_chi, expected_eng):
    chi, eng = translate_svo(sentence, translations)
    assert chi == expected_chi, f"Expected {expected_chi}, got {chi}"
    assert eng == expected_eng, f"Expected {expected_eng}, got {eng}"