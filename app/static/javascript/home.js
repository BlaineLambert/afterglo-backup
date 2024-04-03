document.addEventListener('DOMContentLoaded', function () {
    const menuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');
    menuButton.addEventListener('click', function () {
      mobileMenu.classList.toggle('hidden');
    });
  });
  
document.addEventListener('DOMContentLoaded', () => {
  const accordionButtons = document.querySelectorAll('.accordion-button');
    accordionButtons.forEach((button) => {
        button.addEventListener('click', () => {
            const currentlyActiveAccordionItemContent = document.querySelector('.accordion-content.max-h-xl');
            const newAccordionContent = button.nextElementSibling;
            if (currentlyActiveAccordionItemContent && currentlyActiveAccordionItemContent !== newAccordionContent) {
                currentlyActiveAccordionItemContent.classList.remove('max-h-xl');
                currentlyActiveAccordionItemContent.style.maxHeight = '0';
            }
            if (newAccordionContent.style.maxHeight === '0px' || !newAccordionContent.style.maxHeight) {
                newAccordionContent.classList.add('max-h-xl');
                newAccordionContent.style.maxHeight = newAccordionContent.scrollHeight + 'px';
            } else {
                newAccordionContent.classList.remove('max-h-xl');
                newAccordionContent.style.maxHeight = '0';
            }
        });
    });
});
