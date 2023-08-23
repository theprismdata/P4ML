
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<title>Customizable Canvas Gauge Example</title>
<link href="https://www.cssscript.com/wp-includes/css/sticky.css" rel="stylesheet" type="text/css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootswatch/4.3.1/flatly/bootstrap.min.css">
<style>
  body { background: #efefef; }
  .container { margin: 150px auto; }
  #demo { height: 300px; width: 300px; }
  #preview-textfield{
  width: 300px;
  text-align: center; font-size: 2em; font-weight: bold;
  color: black; font-family: 'Amaranth', sans-serif;
}
  </style>
</head>

<body><div id="css-script-menu">
  <div class="css-script-center">
    <ul>
      <li><a href="https://www.cssscript.com/customizable-gauge-canvas/">Download</a></li>
      <li><a href="https://www.cssscript.com/">Back To CSS Script</a></li>
    </ul>
    <div class="css-script-ads"><div id="carbon-block"></div>
    <script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- CSSScript Demo Page -->
<ins class="adsbygoogle"
     style="display:inline-block;width:728px;height:90px"
     data-ad-client="ca-pub-2783044520727903"
     data-ad-slot="3025259193"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script></div>
    <div class="css-script-clear"></div>
  </div>
</div>
<div class="container">
  <h1>Customizable Canvas Gauge Example</h1>
  <div id="preview-textfield"></div>
  <canvas id="demo"></canvas>

</div>
<script src="dist/gauge.js"></script>
<script>
  var opts = {
   angle: -0.25,
      lineWidth: 0.2,
      radiusScale:0.9,
      pointer: {
        length: 0.6,
        strokeWidth: 0.05,
        color: '#000000'
      },
      staticLabels: {
        font: "10px sans-serif",
        labels: [200, 500, 2100, 2800],
        fractionDigits: 0
      },
      staticZones: [
         {strokeStyle: "#F03E3E", min: 0, max: 200},
         {strokeStyle: "#FFDD00", min: 200, max: 500},
         {strokeStyle: "#30B32D", min: 500, max: 2100},
         {strokeStyle: "#FFDD00", min: 2100, max: 2800},
         {strokeStyle: "#F03E3E", min: 2800, max: 3000}
      ],
      limitMax: false,
      limitMin: false,
      highDpiSupport: true
};
var target = document.getElementById('demo'); // your canvas element
var gauge = new Gauge(target).setOptions(opts); // create sexy gauge!
document.getElementById("preview-textfield").className = "preview-textfield";
gauge.setTextField(document.getElementById("preview-textfield"));
gauge.maxValue = 3000; // set max gauge value
gauge.setMinValue(0);  // set min value
gauge.set(1250); // set actual value
</script>
<script>
try {
  fetch(new Request("https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js", { method: 'HEAD', mode: 'no-cors' })).then(function(response) {
    return true;
  }).catch(function(e) {
    var carbonScript = document.createElement("script");
    carbonScript.src = "//cdn.carbonads.com/carbon.js?serve=CE7DC2JW&placement=wwwcssscriptcom";
    carbonScript.id = "_carbonads_js";
    document.getElementById("carbon-block").appendChild(carbonScript);
  });
} catch (error) {
  console.log(error);
}
</script>
<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-46156385-1', 'cssscript.com');
  ga('send', 'pageview');

</script>
</body>
</html>
