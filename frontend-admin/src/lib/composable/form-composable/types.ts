export type ValuesWithMeta<TFields extends object = Record<string, unknown>> = {
	isLoading: boolean;
	hasChanges: boolean;
	errorMessage?: string;
	fields: {
		[TKey in keyof TFields]: {
			isValid: boolean;
			hasChanges: boolean;
			value: TFields[TKey];
		};
	};
};

export type TFormComposableParams<
	TResponseParams = unknown,
	TRequestParams = unknown,
	TFields extends object = Record<string, unknown>
> = {
	initialValues: TFields;
	request: (requestParams: TRequestParams, abortController: AbortController) => Promise<Response>;
	onSuccess: (data: TResponseParams) => void;
};
