export const checkIsEmpty = (stringValue?: string) => {
	if (!stringValue) {
		return true;
	}
	return stringValue.length < 1;
};
