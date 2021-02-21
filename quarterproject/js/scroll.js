console.log('running');

const pageone = document.getElementById("pageone");
const pagetwo = document.getElementById("pagetwo");
const body = document.getElementsByTagName("body");
var scrollCount = 0;
var opacityPageOne = 100;
var opacityPageTwo = 0;
var opacityPageOnePast = 100;
var opacityPageTwoPast = 0;


document.addEventListener("wheel", function(e) {
  // get the old value of the translation (there has to be an easier way than this)
  //var oldVal = parseInt(document.getElementById("body").style.transform.replace("translateY(","").replace("px)",""));
  // to make it work on IE or Chrome

  var variation = parseInt(e.deltaY);

  variation = variation * -1;

  opacityPageOnePast = opacityPageOne;
  opacityPageTwoPast = opacityPageTwo;

  if (variation>0) {
    opacityPageOne = opacityPageOne + 10;
    if (opacityPageOne > 100) {
      opacityPageOne = 100;
    }
    opacityPageTwo = opacityPageTwo - 10;
    if (opacityPageOne < -100) {
      opacityPageOne = -100;
    }
  }

  if (variation<0) {
    opacityPageOne = opacityPageOne - 10;
    if (opacityPageOne < -100) {
      opacityPageOne = -100;
    }
    opacityPageTwo = opacityPageTwo + 10;
    if (opacityPageOne > 100) {
      opacityPageOne = 100;
    }
  }

  document.getElementById("pageone").style.opacity = opacityPageOne/100;
  document.getElementById("pagetwo").style.opacity = opacityPageTwo/100;
  // If the opacity of page two is greater than 75, disable all pointer event on the first page 
  // and enable them on the second.
  if (opacityPageTwo >= 75) {
    document.getElementById("pageone").style.pointerEvents = 'none';
    document.getElementById("pagetwo").style.pointerEvents = 'auto';
  }
  else {
    document.getElementById("pageone").style.pointerEvents = 'auto';
    document.getElementById("pagetwo").style.pointerEvents = 'none';
  }

  return false;
  
}, true);