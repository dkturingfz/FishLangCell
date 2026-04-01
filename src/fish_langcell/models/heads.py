"""Downstream task heads for annotation and mapping."""


def list_heads() -> list[str]:
    """Return currently planned downstream heads."""
    return ["zero_shot_retrieval", "classification", "reference_mapping"]
