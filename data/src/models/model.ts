import { Model as _Model, DataTypes, Sequelize, ModelCtor } from "sequelize";
import "reflect-metadata";

let sequelize: Sequelize;
if (!sequelize) {
    sequelize = new Sequelize({});
}

export function Model<T extends { new (...args: any[]): {} }>(constructor: T) {
    console.log(constructor.name);

    const defineValues = {};

    const model = new constructor();

    Object.keys(model).map(key => {
        defineValues[key] = {};

        let defaultValue = Reflect.getMetadata('default', model, key);
        if (defaultValue) defineValues[key]["defaultValue"] = defaultValue;
        
        defineValues[key]["type"] = Reflect.getOwnPropertyDescriptor(model, key).value
    });

    return class extends constructor {
        dataAccessor = sequelize.define(constructor.name, defineValues);
    }
}

export function DefaultValue(value: string) {
    return Reflect.metadata('default', value);
}