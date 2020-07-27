import { UserDataAccessor } from "./data-accessors/user-data-accessor";

import { User } from "./models/user";

import sequelize from "./util/sequelize";

sequelize.addModels([User]);

export const userDataAccessor = new UserDataAccessor();
