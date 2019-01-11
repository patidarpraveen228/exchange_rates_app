def calculate_exchange(source_amount: float, conversion_rate: str):
    """
    Function to calculate final rate
    source_amount: The amount on which conversion needs to be applied
    conversion_rate: Rate at which the amount needs to be converted
    """
    target_amount = None
    try:
        target_amount = source_amount * conversion_rate
    except Exception as exc:
        pass
    return target_amount
