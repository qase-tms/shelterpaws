type TParams<T = undefined> = {
	setLoadingState: (state: boolean) => void;
	setErrorState: (message?: string) => void;
	params: T;
	request: (params: T, abortController: AbortController) => Promise<Response>;
};

export const requestsWrapper = async <T = unknown>({
	setLoadingState,
	setErrorState,
	params,
	request
}: TParams<T>) => {
	const abortController = new AbortController();
	setErrorState();
	setLoadingState(true);
	let data;
	let response;
	try {
		response = await request(params, abortController);
		data = await response.json();
	} catch (error: unknown) {
		if (response?.status === 401) {
			if (error && error.detail && typeof error.detail === 'string') {
				setErrorState(error['detail']);
			}
		}
	}

	setLoadingState(false);

	return { data, abortController };
};
