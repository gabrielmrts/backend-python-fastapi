from app.validators.cpf import CPFValidator


class TestCPFValidator:
    """
    Test suite for the CPFValidator class.

    This class contains tests to verify the correctness of CPF validation
    logic implemented in the CPFValidator class.
    """

    def test_is_valid_cpf(self: "TestCPFValidator") -> None:
        """
        Test CPF numbers that should be considered valid.

        Verifies that the validator returns True for valid CPF numbers.
        """
        assert CPFValidator.is_valid('15420486644') is True
        assert CPFValidator.is_valid('568.998.898-70') is True
        assert CPFValidator.is_valid('435.703.058-72') is True

    def test_is_invalid_cpf(self: "TestCPFValidator") -> None:
        """
        Test CPF numbers that should be considered invalid.

        Verifies that the validator returns False for invalid CPF numbers.
        """
        assert CPFValidator.is_valid('12345678900') is False
        assert CPFValidator.is_valid('111.222.333-46') is False
        assert CPFValidator.is_valid('999.999.999-98') is False

    def test_invalid_cpf_length(self: "TestCPFValidator") -> None:
        """
        Test CPF numbers with incorrect lengths.

        Verifies that the validator returns False for CPF numbers that do
        not have exactly 11 digits.
        """
        assert CPFValidator.is_valid('123.456.789') is False
        assert CPFValidator.is_valid('12345678909101') is False

    def test_cpf_with_repeated_digits(self: "TestCPFValidator") -> None:
        """
        Test CPF numbers consisting of repeated digits.

        Verifies that the validator returns False for CPFs with all repeated
        digits, as they are not considered valid, except for edge cases.
        """
        assert CPFValidator.is_valid('111.111.111-11') is False
        assert CPFValidator.is_valid('999.999.999-99') is False

    def test_cpf_with_non_digit_characters(self: "TestCPFValidator") -> None:
        """
        Test CPF numbers that include non-digit characters.

        Verifies that the validator returns False when the CPF contains
        non-digit characters, ensuring it only processes valid digit formats.
        """
        assert CPFValidator.is_valid('123.456.789-a9') is False
        assert CPFValidator.is_valid('123456789-09') is True
