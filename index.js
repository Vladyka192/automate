let myLeads = []
const inputEl = document.getElementById("input-el")
const inputBtn = document.getElementById("input-btn")
const ulEl = document.getElementById("ul-el")
const deleteBtn = document.getElementById("delete-btn")
let leadsFromLocalStorage = JSON.parse(localStorage.getItem("myLeads") )

if (leadsFromLocalStorage) {
    myLeads = leadsFromLocalStorage
    render(myLeads)
}

function render(leads) {
    let listItems = ""

    for (let i = 0; i < leads.length; i++) {
        listItems += `
                <div id='name'>
                    ${leads[i]}
                </div>
        `
    }
    ulEl.innerHTML = listItems
}
  const copyText = async () => {
    let text = document.getElementById('name').innerHTML;
    try {
      await navigator.clipboard.writeText(text);
      console.log('Content copied to clipboard');
    } catch (err) {
      console.error('Failed to copy: ', err);
    }
  }

deleteBtn.addEventListener("click", function() {
  let indexToRemove = 0;
  leadsFromLocalStorage.splice(indexToRemove, 1)
  localStorage.setItem("myLeads", JSON.stringify(leadsFromLocalStorage))
  render(myLeads)
})

inputBtn.addEventListener("click", function() {
    myLeads.push(inputEl.value)
    inputEl.value = ""
    localStorage.setItem("myLeads", JSON.stringify(myLeads) )
    render(myLeads)
})
