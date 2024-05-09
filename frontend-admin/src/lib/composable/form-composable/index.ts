import { writable } from 'svelte/store';

import { requestsWrapper } from '$lib/utils/requests/request-wrapper';
import { extendValuesWithMeta, getRequestParamsFromState } from './utils';
import type { TFormComposableParams } from './types';

export const formComposable = <
	TResponseParams = unknown,
	TFields extends object = Record<string, unknown>
>({
	initialValues,
	request,
	onSuccess
}: TFormComposableParams<TResponseParams, TFields, TFields>) => {
	const abortController = new AbortController();
	const initialValuesWithMeta = extendValuesWithMeta(initialValues);
	const formState = writable(initialValuesWithMeta);

	const setError = (value?: string) => {
		formState.set(initialValuesWithMeta);
		formState.update((state) => ({ ...state, errorMessage: value }));
	};

	const setIsLoading = (loading: boolean) =>
		formState.update((state) => ({ ...state, isLoading: loading }));

	const handleSuccess: TFormComposableParams<TResponseParams, TFields, TFields>['onSuccess'] = (
		data
	) => {
		onSuccess(data);
		formState.set(initialValuesWithMeta);
	};

	const handleSubmit = async () => {
		const requestParams = getRequestParamsFromState(formState);
		await requestsWrapper({
			setLoadingState: setIsLoading,
			onError: setError,
			requestParams,
			onSuccess: handleSuccess,
			request,
			abortController
		});
	};

	return {
		formState,
		handleSubmit,
		abortController
	};
};
