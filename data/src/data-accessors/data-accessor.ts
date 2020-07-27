import { Model, Repository } from "sequelize-typescript";
import sequelize from "../util/sequelize";

export class DataAccessor<M extends Model> {

    protected repository: Repository<M>;

    constructor(model: new () => M) {
        this.repository = sequelize.getRepository<M>(model);
        this.repository.sync();
    }
}