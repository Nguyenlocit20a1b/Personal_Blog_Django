let toggleNavStatus = false;

// Open and close nav
let toggleNav = function() {
  let getSidebar = document.querySelector(".nav-sidebar-s");
  let getSidebarUl = document.querySelector(".nav-sidebar-s ul");
  let getSidebarTitle = document.querySelector(".nav-sidebar-s span");
  let getSidebarLink = document.querySelectorAll(".nav-sidebar-s a");
  
  // Check if sidebar is closed
  if (toggleNavStatus === false) {
    getSidebarUl.style.visibility = "visible";
    getSidebar.style.width = "272px";
    getSidebarTitle.style.opacity = "0.5";

    let arrayLength = getSidebarLink.length;
    for(let i = 0; i < arrayLength; i++) {
      getSidebarLink[i].style.opacity = "1";
    }
    
    toggleNavStatus = true;
    
  }

  // Check if sidebar is open
  else if (toggleNavStatus === true) {
    getSidebar.style.width = "50px";
    getSidebarTitle.style.opacity = "0";

    let arrayLength = getSidebarLink.length;
    for(let i = 0; i < arrayLength; i++) {
      getSidebarLink[i].style.opacity = "0";
    }
    
    getSidebarUl.style.visibility = "hidden";
    toggleNavStatus = false;
    
  }  

}