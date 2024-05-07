type TAuthParams = {
    username: string;
    password: string;
}

export const authRequest = async ({username, password}: TAuthParams) => {
    const url = 'http://0.0.0.0:8080/shelter/auth';
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify({
            username,
            password
        })
    });

    const token = await response.json();

    localStorage.setItem('token', token);
};