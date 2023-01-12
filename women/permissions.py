# здесь будут все права доступа, которые сам определю
# например возможность всех поль-й смотреть запись, а удалять только у админа
from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    # ограничение прав доступа на уровне запроса
    # переопределяем метод класса BasePermission
    def has_permission(self, request, view):
        # если пришедший метод в числе безопасных (т.е. только на чтение данных)
        if request.method in permissions.SAFE_METHODS:  # GET, HEAD, OPTIONS
            # то предоставляем права доступа для всех
            return True
        # иначе проверяем что пользователь === админ
        return bool(request.user and request.user.is_staff)


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # если user записи из БД == user из запроса, то даем права доступа
        return obj.user == request.user
