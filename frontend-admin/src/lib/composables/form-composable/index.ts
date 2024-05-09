import { get } from 'svelte/store';
import { writable } from 'svelte/store';

import { requestsWrapper } from '$lib/utils/requests/request-wrapper';
import { extendValuesWithMeta } from './utils';
import type { TFormComposableParams } from './types';

export const formComposable = ({ initialValues, request, onSuccess }: TFormComposableParams) => {
	const extendedValues = extendValuesWithMeta(initialValues);
	const formState = writable(extendedValues);

	const setError = (value?: string) => {
		formState.update((state) => ({ ...state, error: value }));
	};

	const setIsLoading = (loading: boolean) =>
		formState.update((state) => ({ ...state, isLoading: loading }));

	const abortController = new AbortController();
	const handleSubmit = async () => {
		const { password, username } = get(formState).fields;
		await requestsWrapper({
			setLoadingState: setIsLoading,
			onError: setError,
			requestParams: { username: username.value, password: password.value },
			onSuccess,
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
