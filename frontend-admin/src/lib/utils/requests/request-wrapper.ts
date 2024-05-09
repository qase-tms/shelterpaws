import { requestErrorHandler } from './request-error-handler';

type TParams<TRequestParams = unknown, TResponseParams = unknown> = {
	setLoadingState: (state: boolean) => void;
	onError: (message: string) => void;
	request: (requestParams: TRequestParams, abortController: AbortController) => Promise<Response>;
	onSuccess: (data: TResponseParams) => void;
	requestParams: TRequestParams;
	abortController: AbortController;
};

export const requestsWrapper = async <TRequestParams, TResponseParams>({
	setLoadingState,
	onError,
	onSuccess,
	requestParams,
	request,
	abortController
}: TParams<TRequestParams, TResponseParams>) => {
	setLoadingState(true);
	let response;
	let data;
	try {
		response = await request(requestParams, abortController);
		data = await response.json();
		if (!response.ok) {
			throw new Error(response.status.toString());
		}
		onSuccess(data);
		onError('');
	} catch (error: unknown) {
		onError(requestErrorHandler(response?.status, data.detail));
	}

	setLoadingState(false);
};
