from django.db import models


class TimeStampedModel(models.Model):
    """타임 히스토리 역활"""
    created = models.DateTimeField(null=True)
    updated = models.DateTimeField(null=True)

    class Meta:
        abstract = True
    # 이 코어모델 자체를 데이터 베이스에 올리지 않는다.
    # 다른 모델에서 이 core모델을 상속해서 사용한다면 모델은 created, updated를 가지며 정상적으로 DB에 올라가게 된다
