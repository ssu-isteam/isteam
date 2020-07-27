import { Sequelize } from "sequelize-typescript";
import { env } from "process";

let sequelize: Sequelize;

if (!sequelize) {
    console.log('creating instance');
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