from coding_exercise.domain.model.cable import Cable


class Splitter:
    """
    Splitter class
    """

    def __validate(self, times: int, cable: Cable):
        """
        Validate split times and cable length

        Args:
            times (int): Number of times to split the cable
            cable (Cable): Cable to split

        Raises:
            ValueError: If times is less than 1 or greater than 64
            ValueError: If cable length is less than 2 or greater than 1024
        """
        # Validate times constraints
        if not (1 <= times <= 64):
            raise ValueError(f"Split times must be between 1 and 64. Got {times}")
        if "-" not in cable.name and not (2 <= cable.length <= 1024):
            raise ValueError(
                f"Cable length must be between 2 and 1024. Got {cable.length}"
            )
        if "-" in cable.name and not (1 <= cable.length <= 1024):
            raise ValueError(
                f"Cable length must be between 1 and 1024. Got {cable.length}"
            )

    def split(self, cable: Cable, times: int) -> list[Cable]:
        """
        Split a cable into multiple sub cables of equal length.

        Args:
            cable (Cable): The cable to split
            times (int): Number of times to split the cable (resulting in times + 1 pieces)

        Returns:
            List[Cable]: List of Cable objects representing the split pieces

        Raises:
            ValueError: If times is not between 1 and 64 inclusive
            ValueError: If cable length is less than 2
            ValueError: If splitting would result in pieces less than length 1

        Example:
            >>> cable = Cable(10, "main")
            >>> splitter = Splitter()
            >>> result = splitter.split(cable, 1)  # Split once into 2 pieces
            >>> print(result)
            [Cable(length=5, name='main-00'), Cable(length=5, name='main-01')]
        """
        self.__validate(times=times, cable=cable)

        # Calculate the length of each split
        split_length = cable.length // (times + 1)

        # Validate that splits result in at least 1-length cables
        if split_length < 1:
            raise ValueError(
                f"Cannot split cable of length {cable.length} {times} times"
            )

        # Create cables
        result = []

        # Create main split cables
        for i in range(times + 1):
            # Create name with zero-padded, right-justified index
            name = f"{cable.name}-{i:02d}"
            result.append(Cable(split_length, name))

        # Handle remainder
        remainder = cable.length % (times + 1)

        # If there's a remainder, split it into cables of the same length
        while remainder > 0:
            # Use the same split length for remainder
            if remainder >= split_length:
                name = f"{cable.name}-{len(result):02d}"
                result.append(Cable(split_length, name))
                remainder -= split_length
            else:
                # For the last piece that's smaller than split_length
                name = f"{cable.name}-{len(result):02d}"
                result.append(Cable(remainder, name))
                remainder = 0

        if len(result) <= 10:
            return [
                Cable(c.length, c.name.split("-")[0] + f"-{i}")
                for i, c in enumerate(result)
            ]
        return result
