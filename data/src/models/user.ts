import { Table, Column, Model, DataType } from "sequelize-typescript";
import sequelize from "../util/sequelize";

@Table
export class User extends Model<User> {

    @Column(DataType.TEXT)
    name: string;
}

sequelize.addModels([User]);