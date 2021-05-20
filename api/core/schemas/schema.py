class BaseSchema:
    """
    Basic schema class
    """
    schema = None

    def __init__(self, data):
        self.schema = data

    def validate(self):
        """Validate schema and return formated data
        Returns:
            TYPE: Formated data
        """
        return self.schema.validate(self.data)

    def is_valid(self):
        """Check if schema is valid
        Returns:
            bool: True if schema is valid. False otherwise
        """
        return self.schema.is_valid(self.data)
