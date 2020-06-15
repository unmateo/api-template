from api.core.logging import logger


class CRUDService:
    """ Implements CRUD methods. """

    @staticmethod
    def create(db, api_model, orm_class):
        """ Converts given model from API to ORM and saves it. """

        model = orm_class(**api_model.dict(exclude_unset=True))
        db.add(model)
        db.commit()
        db.refresh(model)
        logger.info(f"Created {model}")

        return model
