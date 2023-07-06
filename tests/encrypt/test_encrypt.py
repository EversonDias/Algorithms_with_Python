import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    assert encrypt_message('helloworld', 4) == "dlrowo_lleh"
    assert encrypt_message('helloworld', 11) == "dlrowolleh"
    with pytest.raises(TypeError):
        encrypt_message('hello world', 'oi')
