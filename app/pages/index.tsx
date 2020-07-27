export default function Home({ username }) {
    return (
        <>
            <h1>Hello, {username}!</h1>
        </>
    );
}

export async function getStaticProps() {
    const { userDataAccessor } = require("@isteam/data");

    const username = await userDataAccessor.findById(1)
        .then(user => user.getDataValue("name"))

    return {
        props: {
            username
        }
    }
}