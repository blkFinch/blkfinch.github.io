
```js
// regex search injector => hotkey (control g)
window.onkeydown = function (e) {
      if (e.ctrlKey == true && e.key == "g") {
          e.preventDefault(); // override "control g"      
          leafSelector(); 
          setQuery(); // => run it
      }
} 

function setQuery(){ // inject path to search box
	document.querySelector(".mod-top-left-space [data-type='search']").click();

    let tName = document.querySelector('#active-tab .view-header-title-container.mod-at-start').innerText
        .replace("\n", "")      // remove line breaks
        .replace(/\u200B/g, "") // remove zerowidthspaces
        .replace(/\s/g, "") // remove zerowidthspaces

	let sQ = "path: " + tName + " //"; 
    document.querySelector('.mod-top-left-space .search-input-container > input').value = sQ;
}

function leafSelector() { // get tab
    const cut = document.getElementById('active-tab');
    if (cut !== null){cut.removeAttribute('id');}

    var leafArray = document.querySelectorAll('.mod-vertical .workspace-leaf');
    for (var c = 0; c < leafArray.length; c++) {
        let leafo = leafArray[c];
        if (window.getComputedStyle(leafo).display === "none") {continue;} 
        else {leafo.id = "active-tab"; return;}        
    }
}
```

**HOW TO ADD IT:**

The “Javascript Init” plugin is great for running JS in Obsidian.

To set it up (first-time only), just go to:

- Preferences > community plugins > get “Javascript Init”.
- Preferences > Javascript Init settings > paste the JS code in the box.
- Refresh Obsidian [View > Force Reload]. (And if you modify the code, reload.)


[source](https://forum.obsidian.md/t/a-very-simple-question-is-it-possible-to-search-with-regex-in-current-file/48122/10)

#### see also
[[Programming]] 