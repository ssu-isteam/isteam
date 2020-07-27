import { User } from "../models/user";
import { DataAccessor } from "./data-accessor";

export class UserDataAccessor extends DataAccessor<User> {

    constructor() {
        super(User);
    }

    findById(id: number) {
        return this.repository.findByPk<User>(id);
    }

    findAllByName(name: string) {
        return this.repository.findAll<User>({
            where: { name }
        })
    }
}