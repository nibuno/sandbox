def grade(score: int) -> str:
    """採点を行う

    0点-59点: 不可
    60点-69点: 可
    70点-79点: 良
    80点-100点: 優
    """
    if score < 60:
        return "不可"
    elif score < 70:
        return "可"
    elif score < 80:
        return "良"
    else:
        return "優"
