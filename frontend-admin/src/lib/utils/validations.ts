export const checkIsEmpty = (stringValue?: string) => {
	if (!stringValue) {
		return false;
	}
	return stringValue.length < 1;
};
