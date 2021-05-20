import csv


class ParseCsv:
    """Parse CSV."""

    @staticmethod
    def create_csv(file_name, row_list):
        """Create file CSV.
        Args:
            file_name(str): Name file
            row_list(list): List with the content of the CSV
        """
        with open(file_name, 'w+') as file:
            writer = csv.writer(
                file, quoting=csv.QUOTE_NONNUMERIC,
                delimiter=';'
            )
            writer.writerows(row_list)
