const largeCategorySelect = document.getElementById('large-category');
const mediumCategorySelect = document.getElementById('medium-category');
const smallCategorySelect = document.getElementById('small-category');

const mediumCategoryPlaceholder = mediumCategorySelect.options[0].cloneNode(true);
const smallCategoryPlaceholder = smallCategorySelect.options[0].cloneNode(true);
const mediumCategoryOptions = Array.from(mediumCategorySelect.options).slice(1).map((option) => option.cloneNode(true));
const smallCategoryOptions = Array.from(smallCategorySelect.options).slice(1).map((option) => option.cloneNode(true));

function replaceOptions(selectElement, placeholderOption, options) {
    selectElement.replaceChildren(placeholderOption.cloneNode(true), ...options.map((option) => option.cloneNode(true)));
    selectElement.value = '';
    selectElement.disabled = options.length === 0;
}

function updateMediumCategoryOptions() {
    const selectedLargeCategoryId = largeCategorySelect.value;
    const filteredMediumOptions = selectedLargeCategoryId === ''
        ? []
        : mediumCategoryOptions.filter((option) => option.dataset.parentId === selectedLargeCategoryId);

    replaceOptions(mediumCategorySelect, mediumCategoryPlaceholder, filteredMediumOptions);
    updateSmallCategoryOptions();
}

function updateSmallCategoryOptions() {
    const selectedMediumCategoryId = mediumCategorySelect.value;
    const filteredSmallOptions = selectedMediumCategoryId === ''
        ? []
        : smallCategoryOptions.filter((option) => option.dataset.parentId === selectedMediumCategoryId);

    replaceOptions(smallCategorySelect, smallCategoryPlaceholder, filteredSmallOptions);
}

largeCategorySelect.addEventListener('change', updateMediumCategoryOptions);
mediumCategorySelect.addEventListener('change', updateSmallCategoryOptions);

updateMediumCategoryOptions();