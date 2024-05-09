import type { ValuesWithMeta } from "./types";

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