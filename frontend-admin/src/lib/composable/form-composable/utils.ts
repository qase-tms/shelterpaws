import { get, type Writable } from 'svelte/store';
import type { ValuesWithMeta } from './types';

export const extendValuesWithMeta = <TFields extends object = Record<string, unknown>>(
	fields: TFields
) => {
	const extendedValues: ValuesWithMeta<TFields> = {
		hasChanges: false,
		isLoading: false,
		errorMessage: undefined,
		fields: {} as ValuesWithMeta<TFields>['fields']
	};

	Object.entries(fields).forEach(([key, value]) => {
		extendedValues.fields[key as keyof TFields] = {
			isValid: true,
			hasChanges: false,
			value
		};
	});
	return extendedValues;
};

export const getRequestParamsFromState = <TFields extends object = Record<string, unknown>>(
	formState: Writable<ValuesWithMeta<TFields>>
) => {
	const requestParams: TFields = {} as TFields;
	const fields = get(formState).fields;

	(
		Object.entries(fields) as [
			[keyof typeof fields, ValuesWithMeta<TFields>['fields'][keyof typeof fields]]
		]
	).forEach(([key, value]) => {
		requestParams[key] = value.value;
	});

	return requestParams;
};
