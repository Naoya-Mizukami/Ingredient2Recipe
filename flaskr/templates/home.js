const largeCategorySelect = document.getElementById('large-category');
const mediumCategorySelect = document.getElementById('medium-category');
const smallCategorySelect = document.getElementById('small-category');

const mediumCategoryOptions = Array.from(mediumCategorySelect.options);
const smallCategoryOptions = Array.from(smallCategorySelect.options);

function updateMediumCategoryOptions() {
    const selectedLargeCategoryId = largeCategorySelect.value;

    mediumCategorySelect.value = '';
    mediumCategorySelect.disabled = selectedLargeCategoryId === '';

    mediumCategoryOptions.forEach((option) => {
        if (option.value === '') {
            option.hidden = false;
            option.disabled = false;
            return;
        }

        const isSameParent = option.dataset.parentId === selectedLargeCategoryId;
        option.hidden = !isSameParent;
        option.disabled = !isSameParent;
    });

    updateSmallCategoryOptions();
}

function updateSmallCategoryOptions() {
    const selectedMediumCategoryId = mediumCategorySelect.value;

    smallCategorySelect.value = '';
    smallCategorySelect.disabled = selectedMediumCategoryId === '';

    smallCategoryOptions.forEach((option) => {
        if (option.value === '') {
            option.hidden = false;
            option.disabled = false;
            return;
        }

        const isSameParent = option.dataset.parentId === selectedMediumCategoryId;
        option.hidden = !isSameParent;
        option.disabled = !isSameParent;
    });
}

largeCategorySelect.addEventListener('change', updateMediumCategoryOptions);
mediumCategorySelect.addEventListener('change', updateSmallCategoryOptions);

updateMediumCategoryOptions();