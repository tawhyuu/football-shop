function showToast(title, message, type = 'normal', duration = 3000) {
  const toastContainer = document.getElementById('toast-container');
  
  const toast = document.createElement('div');
  toast.className = 'toast-item transform transition-all duration-300 ease-out translate-x-full opacity-0';
  
  let bgColor, icon;
  
  switch(type) {
    case 'success':
      bgColor = 'bg-gradient-to-r from-green-500 to-emerald-600';
      icon = `<svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
              </svg>`;
      break;
    case 'error':
      bgColor = 'bg-gradient-to-r from-red-500 to-rose-600';
      icon = `<svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
              </svg>`;
      break;
    case 'warning':
      bgColor = 'bg-gradient-to-r from-yellow-500 to-orange-600';
      icon = `<svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path>
              </svg>`;
      break;
    default:
      bgColor = 'bg-gradient-to-r from-blue-500 to-indigo-600';
      icon = `<svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
              </svg>`;
  }
  
  toast.innerHTML = `
    <div class="${bgColor} rounded-xl shadow-2xl p-4 flex items-start gap-3 min-w-[320px] max-w-md backdrop-blur-sm">
      <div class="flex-shrink-0">
        ${icon}
      </div>
      <div class="flex-1">
        <h4 class="text-white font-bold text-sm mb-1">${DOMPurify.sanitize(title)}</h4>
        <p class="text-white/90 text-xs">${DOMPurify.sanitize(message)}</p>
      </div>
      <button onclick="this.closest('.toast-item').remove()" class="flex-shrink-0 text-white/80 hover:text-white transition-colors">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
        </svg>
      </button>
    </div>
  `;
  
  toastContainer.appendChild(toast);
  
  setTimeout(() => {
    toast.classList.remove('translate-x-full', 'opacity-0');
  }, 10);
  
  setTimeout(() => {
    toast.classList.add('translate-x-full', 'opacity-0');
    setTimeout(() => toast.remove(), 300);
  }, duration);
}