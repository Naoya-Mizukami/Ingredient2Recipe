const categorySelect = document.getElementById('category');
const subCategorySelect = document.getElementById('sub-category');
const subCategoryOptions = Array.from(subCategorySelect.options);

function updateSubCategoryOptions() {
    const selectedCategoryId = categorySelect.value;

    subCategorySelect.value = '';
    subCategorySelect.disabled = selectedCategoryId === '';

    subCategoryOptions.forEach((option) => {
        if (option.value === '') {
            option.hidden = false;
            option.disabled = false;
            return;
        }

        const isSameParent = option.dataset.parentId === selectedCategoryId;
        option.hidden = !isSameParent;
        option.disabled = !isSameParent;
    });
}

categorySelect.addEventListener('change', updateSubCategoryOptions);
updateSubCategoryOptions();