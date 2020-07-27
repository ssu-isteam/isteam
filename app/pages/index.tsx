import React from "react";
import { userDataAccessor } from "@isteam/data";

export default function Home() {
    return <h1>Hello world!</h1>;
}

async function name() {
    await userDataAccessor.findById(1);
}