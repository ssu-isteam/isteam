import { Model, DefaultValue, ModelWithDataAccessor } from "./model";
import { DataType, DataTypes } from 'sequelize';

@Model
class User extends ModelWithDataAccessor {

    id = DataTypes.NUMBER.UNSIGNED

    @DefaultValue("John")
    name = DataTypes.STRING
}

const user = new User();