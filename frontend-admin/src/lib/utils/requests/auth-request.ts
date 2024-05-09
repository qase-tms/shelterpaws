export type TAuthParams = {
	username: string;
	password: string;
};

export const authRequest = (
	{ username, password }: TAuthParams,
	abortController: AbortController
) => {
	const url = `${import.meta.env.VITE_API_URL}/shelter/auth`;
	return fetch(url, {
		method: 'POST',
		signal: abortController.signal,
		headers: {
			'content-type': 'application/json'
		},
		body: JSON.stringify({
			username,
			password
		})
	});
};
