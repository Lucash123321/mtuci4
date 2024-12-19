from django.db import models

# Create your models here.
PERMISSIONS = (
    ('read', 'read'),
    ('write', 'write'),
    ('edit', 'edit'),
    ('delete', 'delete'),
)


class Role(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Permission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission = models.CharField(max_length=10, choices=PERMISSIONS)
