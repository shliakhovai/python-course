def validate_email(email: str, mask_email: bool) -> str:
    """
    Validate and optionally mask an email address.

    Rules:
    - Email must not be empty and must be at least 15 characters long
    - Must contain exactly one '@'
    - Must end with '.com', '.org', or '.ua'
    - If mask_email=True, mask the local part of the email

    Args:
        email (str): Raw email input
        mask_email (bool): Whether to mask the email

    Returns:
        str: Validated (and possibly masked) email

    Raises:
        ValueError: If validation fails
    """
    raise NotImplementedError


def validate_password(password: str, encrypt_password: bool) -> str:
    """
    Validate and optionally encrypt a password.

    Rules:
    - Minimum length: 8 characters
    - Must contain at least one digit
    - Must contain at least one uppercase letter
    - If encrypt_password=True:
        - Basic: reverse the string
        - Advanced: implement reversible encryption

    Args:
        password (str): Raw password input
        encrypt_password (bool): Whether to encrypt the password

    Returns:
        str: Validated (and possibly encrypted) password

    Raises:
        ValueError: If validation fails
    """
    raise NotImplementedError


def validate_name(full_name: str, show_only_initials: bool) -> str:
    """
    Validate and optionally transform a full name.

    Rules:
    - Must contain at least two words (name and surname)
    - Each part must be at least 2 characters long
    - If show_only_initials=True, return initials (e.g., "J.D.")

    Args:
        full_name (str): Raw full name input
        show_only_initials (bool): Whether to return initials

    Returns:
        str: Validated (and possibly transformed) name

    Raises:
        ValueError: If validation fails
    """
    raise NotImplementedError


def get_user_info() -> tuple[str, str, str]:
    """
    Collect user data from input and validate it.

    Requirements:
    - Use input() to collect:
        - full name
        - password
        - email
    - Normalize input (strip, lower, title where appropriate)
    - Convert y/n answers to boolean flags
    - Call validation functions

    Returns:
        tuple[str, str, str]: (full_name, password, email)
    """
    raise NotImplementedError


def main() -> None:
    """
    Entry point of the program.

    Responsibilities:
    - Print greeting message
    - Call get_user_info()
    - Print validated data

    The program should not crash without meaningful error messages.
    """
    raise NotImplementedError


if __name__ == "__main__":
    main()
