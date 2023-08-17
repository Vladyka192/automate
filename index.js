let impl_function = require('/implmentation.js').impl_function;
  const copyText = async () => {
    let text = document.getElementById('name').innerHTML;
    try {
      await navigator.clipboard.writeText(text);
      console.log('Content copied to clipboard');
    } catch (err) {
      console.error('Failed to copy: ', err);
    }
  }
