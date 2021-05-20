from .models import Attributes, TypeEnvs


class TypeEnvsRepository:

    MODEL = TypeEnvs

    @classmethod
    def get_languages(cls):
        return cls.MODEL.get_env(
            cls.MODEL.LANGUAGE
        )


class AttributesRepositoy:

    MODEL = Attributes

    @classmethod
    def get_attributes_by_languages(cls):
        return cls.MODEL.get_attributes_by_typeenvs(
            TypeEnvsRepository.get_languages()
        )
