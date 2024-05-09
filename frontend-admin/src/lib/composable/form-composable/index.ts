import { get } from 'svelte/store';
import { writable } from 'svelte/store';

import { requestsWrapper } from '$lib/utils/requests/request-wrapper';
import { extendValuesWithMeta } from './utils';
import type { TFormComposableParams } from './types';

export const formComposable = <
	TResponseParams = unknown,
	TFields extends object = Record<string, unknown>
	// TRequestParams extends object = Record<string, any>,
>({
	initialValues,
	request,
	onSuccess
}: TFormComposableParams<TResponseParams, TFields, TFields>) => {
	const abortController = new AbortController();

	const extendedValues = extendValuesWithMeta(initialValues);
	const formState = writable(extendedValues);

	const setError = (value?: string) => {
		formState.set(extendedValues);
		formState.update((state) => ({ ...state, errorMessage: value }));
	};

	const setIsLoading = (loading: boolean) =>
		formState.update((state) => ({ ...state, isLoading: loading }));

	const handleSuccess: TFormComposableParams<TResponseParams, TFields, TFields>['onSuccess'] = (
		data
	) => {
		onSuccess(data);
		formState.set(extendedValues);
	};

	const handleSubmit = async () => {
		const requestParams: TFields = {} as TFields;

		const fields = get(formState).fields;
		(
			Object.entries(fields) as [
				[keyof typeof fields, (typeof extendedValues)['fields'][keyof typeof fields]]
			]
		).forEach(([key, value]) => {
			requestParams[key] = value.value;
		});

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
