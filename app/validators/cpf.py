import re


class CPFValidator:
    """
    Validator class for CPF.

    This class provides a method to check the validity of a Brazilian CPF
    (Cadastro de Pessoas Físicas) by verifying its format and control digits.
    """

    @staticmethod
    def is_valid(cpf: str) -> bool:
        """
        Validates a given CPF.

        This method removes any non-digit characters and checks the CPF's
        structure, ensuring it follows the rules for valid Brazilian CPF numbers.

        Args:
            cpf (str): The CPF string to be validated.

        Returns:
            bool: True if the CPF is valid, False otherwise.
        """
        # Remove non-digit characters
        cpf = re.sub(r'\D', '', cpf)

        # Validate length and repeated sequences
        if len(cpf) != 11 or cpf == cpf[0] * 11:
            return False

        # Validate first and second verification digits
        for i in range(9, 11):
            # Calculate the sum for the verification digit
            total_sum = sum(int(cpf[num]) * ((i + 1) - num) for num in range(i))
            verification_digit = (total_sum * 10 % 11) % 10

            # Check if the calculated digit matches the given digit
            if verification_digit != int(cpf[i]):
                return False

        return True
