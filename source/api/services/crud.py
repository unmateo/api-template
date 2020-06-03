class CRUDService:
    @staticmethod
    def create(db, api_model, orm_class):
        model = orm_class(**api_model.dict(exclude_unset=True))
        db.add(model)
        db.commit()
        db.refresh(model)
        return model
