import { Sequelize } from "sequelize-typescript";
import dotenv from "dotenv";

const result = dotenv.config();

if (result.error) {
    throw result.error;
}

const env = result.parsed;

let sequelize: Sequelize;

if (!sequelize) {
    sequelize = new Sequelize({
        host: env.DB_HOST,
        database: env.DB_NAME,
        username: env.DB_USER,
        password: env.DB_PASS,
        dialect: "mysql",
        repositoryMode: true
    });   
}

export default sequelize;