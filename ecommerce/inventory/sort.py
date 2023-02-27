class Sort:
    def __init__(self, queryset) -> None:
        self.queryset = queryset

    def sort_by(self, field: str, ascending: bool):
        if ascending == "false":
            field = f"-{field}"
        return self.queryset.order_by(field)
