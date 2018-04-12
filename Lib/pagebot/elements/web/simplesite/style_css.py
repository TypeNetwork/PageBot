simpleTheme = dict(
	
	# General 
	regularFont='Upgrade-Regular',
	textDecorationColor='#2E8DB6',
	textHoverColor='#2BC88A',
	textColor='#706670',
	headerPadding='15px 0',
	
	# Hero 
	heroPadding='20px 0',
	heroBackgroundColor='#f3f3f3',
	heroBorderTop='1px solid #e2e2e2',
	heroBorderBottom='1px solid #e2e2e2',
	heroFontSize='1.1em',

	# Menu	
	menuBackground='#2C8CB7',
	menuTextColor='#fff',
	srtMenuMarginBottom='60px',
	srtMenuColor='#666',
	srtMenuBackground='#DADADA',
	srtMenuHoverBackground='#2C8CB7',
	srtMenuHoverBackgroundTwo='#E8E8E8',
	srtMenuHoverBackgroundThree='#EFEFEF',
	srtMenuHover='#fff',
	menuTogglePadding='10px',
	menuToggleMargin='20px 0 0',
	menuToggleOnBackgroundColor='#2C8CB7',
	
	# Buttons 
	buttonLinkBackground='#2C8CB7',
	buttonLinkTextColor='#FFFFFF',
	buttonPadding='10px',
	buttonMargin='10px 15px 10px 0',
	buttonLinkHoverColor='#353132',

	# Buttons diap 
	buttonLinkBackgroundDiap='#FFFFFF',
	buttonLinkTextColorDiap='#2C8CB7',
	buttonLinkTextHoverColorDiap='#FFFFFF',
	buttonLinkBackgroundColorDiap='#353132',


)
simpleCss = """
body{
	background:#fff;
	color:%(textColor)s;
	font-family: %(regularFont)s, sans-serif; 
	font-size:1.10em;
	line-height:1.4em; 
	font-weight:normal;
}
h1, h2, h3, h4, h5, h6{
	font-weight:normal;
	font-family:%(regularFont)s, sans-serif; 
	line-height:1.5em;
	margin:.45em 0;
	padding:0;
} 



/* links */
a{text-decoration:none; color:%(textDecorationColor)s;
},
a:visited{text-decoration:none;},
a:active{text-decoration:none;},
a:hover{color:%(textHoverColor)s; text-decoration:none;}
a:hover{ text-decoration:none;}


/* Box sizing. More info here: http://www.w3schools.com/cssref/css3_pr_box-sizing.asp */
*{	box-sizing:border-box;
	-moz-box-sizing:border-box;}
  
/* structure */   
.wrapper{
	width: 92%%; 
	margin: 0 auto;
}
header{ 
	padding:%(headerPadding)s;
}
#banner{ 
	text-align:center;
}	
#hero,#page-header{
	background:%(heroBackgroundColor)s;
	border-top:%(heroBorderTop)s;
	border-bottom:%(heroBorderBottom)s;
	padding:%(heroPadding)s;
	font-size:%(heroFontSize)s;
}

#page-header h1{
	margin:0;
}
.flexslider{
	display:block;
}
#content,
aside,
.vertical-padding{  
	padding:3em 0;
}
p{ margin:0 0 1.5em;}


/* RESPONSIVE IMAGES  */
img{ max-width:100%%; height:auto;}


/*MAIN MENU*/
.menu-toggle{
	display:block;
	padding:%(menuTogglePadding)s;
	margin:%(menuToggleMargin)s;
	background:%(menuBackground)s;
	letter-spacing:0.2em;
	color:%(menuTextColor)s;
	cursor:pointer;
	text-transform:uppercase;
	font-size:20px;
}
.menu-toggle.toggled-on{
	background:%(menuToggleOnBackgroundColor)s;
}
.srt-menu{
	display:none;
}	
.srt-menu.toggled-on{
	display:block;
	position:relative;
	z-index:10;
}

.srt-menu{
	clear:both;
	margin-bottom:%(srtMenuMarginBottom)s;
	
}
.srt-menu li a {
	color:%(srtMenuColor)s;
	background:%(srtMenuBackground)s;
	display:block;
	margin:1px 0; 
	padding:10px;
	text-decoration:none;
	text-transform:uppercase;
	letter-spacing:0.10em;
	font-size:.8em;
}
.srt-menu li a:hover{
	background:%(srtMenuHoverBackground)s;
	color:%(srtMenuHover)s;
}
.srt-menu li li a {
	background:%(srtMenuHoverBackgroundTwo)s;
	padding-left:40px;
}
.srt-menu li li li a {
	background:%(srtMenuHoverBackgroundThree)s;
	padding-left:80px;
}

/*SECONDARY MENU*/
#secondary-navigation{
	margin-bottom:60px;
}
#secondary-navigation ul{
	margin:0;
	padding:0;
}
#secondary-navigation ul li a{ 
	background:#E6E6E6;
	color:#666;
	display:block;
	margin:5px 0; 
	padding:10px;
	text-decoration:none;
}
#secondary-navigation ul li a:hover,
#secondary-navigation ul li.current a{
	background:#2C8CB7;
	color:#fff;
}

/*SPACE GRID ELEMENTS VERTICALLY, SINCE THEY ARE ONE UNDER ANOTHER*/
.grid_1,
.grid_2,
.grid_3,
.grid_4,
.grid_5,
.grid_6,
.grid_7,
.grid_8,
.grid_9,
.grid_10,
.grid_11,
.grid_12 {
	margin-bottom:40px;
	/*positioning and padding*/
	position: relative;
    min-height: 1px;
    padding-left: 15px;
    padding-right: 15px;
}

/*FOOTER*/
footer{  
	background:#333;
	color:#ccc;
	font-size:80%%;
	padding:20px 0;
}
footer ul{
	margin:0 0 0 8%%;
	padding:0;
}


/*Some more colored elements*/
a.buttonlink{ 
	background:%(buttonLinkBackground)s; 
	border-radius:7px; 
	color:%(buttonLinkTextColor)s;
	display:block;
	float:left; 
	margin:%(buttonMargin)s; 
	padding:%(buttonPadding)s;
	text-decoration:none;
}
a.buttonlink:hover{
	background:%(buttonLinkHoverColor)s;
}
a.buttonlinkdiap{ 
	background:%(buttonLinkBackgroundDiap)s; 
	border-radius:7px; 
	color:%(buttonLinkTextColorDiap)s;
	display:block;
	float:left; 
	margin:%(buttonMargin)s; 
	padding:%(buttonPadding)s;
	text-decoration:none;
}
a.buttonlinkdiap:hover{
	background:%(buttonLinkBackgroundColorDiap)s;
	color:%(buttonLinkTextHoverColorDiap)s;
}
.blueelement{
	background:#2A8BB8;
	color:#fff;
}





/* Contain floats*/ 
.clearfix:before,
.clearfix:after,
.row:before,
.row:after {
  content: " ";
  display: table;
}
.clearfix:after,
.container:after,
.row:after{
  clear: both;
}



/****************************************
*****************************************
MEDIAQUERIES
*****************************************
****************************************/



/*
LARGER MOBILE DEVICES
This is for mobile devices with a bit larger screens.
*/
@media only screen and (min-width: 481px) {
#banner{
	float:left;
	text-align:left;
	margin-bottom:-20px;/*this depends on the height of the logo*/
}
.menu-toggle{/*make menu float right, instead of sitting under the logo*/
	margin-top:10px; /*this depends on the height of the logo*/
	float:right;
}



} 

/*
TABLET & SMALLER LAPTOPS

*/
@media only screen and (min-width: 920px) {

.wrapper{
	max-width: 1200px; 
	margin: .75em auto;
}
header{
	padding:0;
}
#banner{ 
	float:left; 
	text-align:left;
	margin-bottom:0px;
	margin-top:5px;
}
#hero{
	padding:0;
}

#content {  
	float:left;
	width:65%%;
}
#content.wide-content{
	float:none;
	width:80%%;
	margin-bottom:2em;
	margin-left:10%%;
	margin-right:10%%;
}

.flexslider{
	display:block;
/*demo 1 slider theme*/	
margin: 0; 
}
.flex-control-nav {bottom: 5px;}


aside { 
	float:right;
	width:30%%;
}

/*** MAIN MENU - ESSENTIAL STYLES ***/
.menu-toggle{display:none;}
#menu-main-navigation{display:block;}

.srt-menu, .srt-menu * {
	margin:			0;
	padding:		0;
	list-style:		none;
}
.srt-menu ul {
	position:		absolute;
	display:none;
	width:			12em; /* left offset of submenus need to match (see below) */
}
.srt-menu ul li {
	width:			100%%;
}
.srt-menu li:hover {
	visibility:		inherit; 
}
.srt-menu li {
	float:			left;
	position:		relative;
	margin-left:1px;
	height:25px;
}
.srt-menu li li {
	margin-left:0px;
	height:auto;
}
.srt-menu a {
	display:		block;
	position:		relative;
}
.srt-menu li:hover ul,
.srt-menu li.sfHover ul {
	display:block;
	left:			0;
	top:			42px; /* match top ul list item height */
	z-index:		99;
	-webkit-box-shadow:  2px 3px 2px 0px rgba(00, 00, 00, .3);
    box-shadow:  2px 3px 2px 0px rgba(00, 00, 00, .3);
}
ul.srt-menu li:hover li ul,
ul.srt-menu li.sfHover li ul {
	top:			-999em;
}
ul.srt-menu li li:hover ul,
ul.srt-menu li li.sfHover ul {
	left:			12em; /* match ul width */
	top:			0;
}
ul.srt-menu li li:hover li ul,
ul.srt-menu li li.sfHover li ul {
	top:			-999em;
}
ul.srt-menu li li li:hover ul,
ul.srt-menu li li li.sfHover ul {
	left:			10em; /* match ul width */
	top:			0;
}

/*** DEMO2 SKIN ***/
#topnav, .srt-menu {
	float:right;
	margin: .35em 0 0 0;
}
.srt-menu a {
	text-decoration:none;
}
.srt-menu li a{
	background:#fff;
	text-transform:uppercase;
	letter-spacing:0.10em;
	margin:0; 
	padding:10px 20px;
}
.srt-menu a, .srt-menu a:visited  { 
	color:			#666;	
}
.srt-menu li li a {
		border-top:		1px solid rgba(255,255,255,.2);
		background:		#333; /*fallback for old IE*/
		background:rgba(0,0,0,.6);
		color:	#fff;
		padding-left:20px;
}
.srt-menu li li a:visited{color:#fff;}
.srt-menu li li li a,
.srt-menu li.current * li a{
	padding-left:20px;
	background:rgba(0,0,0,.6);
}

.srt-menu li:hover > a,
.srt-menu li.current a{ 
	color:#fff;
	background:#2A3A48;
}
.srt-menu li li:hover > a{
	color:#fff;
	background:#2C8CB7;
}



/*GRID*/
/*
 & Columns : 12 

 */
 .row{
	 margin-left: -15px;
     margin-right: -15px;
}
 
.grid_1 { width: 8.33333333%%; }
.grid_2 { width: 16.66666667%%; }
.grid_3 { width: 25%%; }
.grid_4 { width: 33.33333333%%; }
.grid_5 { width: 41.66666667%%; }
.grid_6 { width: 50%%; }
.grid_7 { width: 58.33333333%%; }
.grid_8 { width: 66.66666667%%; }
.grid_9 { width: 75%%; }
.grid_10 { width: 83.33333333%%; }
.grid_11 { width: 91.66666667%%; }
.grid_12 { width: 100%%; }

.grid_1,
.grid_2,
.grid_3,
.grid_4,
.grid_5,
.grid_6,
.grid_7,
.grid_8,
.grid_9,
.grid_10,
.grid_11,
.grid_12 {
	float: left;
	display: block;
}

.rightfloat{float:right;}
/* inspired by tinyGrid, .row and percentage by Twitter Bootstrap
 */
 
#hero .grid_8 { 
	margin:40px 0 -13px;
}

}

/*
DESKTOP
This is the average viewing window. So Desktops, Laptops, and
in general anyone not viewing on a mobile device. 
*/
@media only screen and (min-width: 1024px) {
#hero h1{ font-size:1.6em;}
} 

/*
LARGE VIEWING SIZE
This is for the larger monitors and possibly full screen viewers.
*/
@media only screen and (min-width: 1240px) {
#hero h1{ font-size:1.8em;}
} 

/*
RETINA (2x RESOLUTION DEVICES)
This applies to the retina iPhone (4s) and iPad (2,3) along with
other displays with a 2x resolution.
*/
@media only screen and (-webkit-min-device-pixel-ratio: 1.5),
       only screen and (min--moz-device-pixel-ratio: 1.5),
       only screen and (min-device-pixel-ratio: 1.5) {


} 

/*
iPHONE 5 MEDIA QUERY
iPhone 5 or iPod Touch 5th generation styles (you can include your own file if you want)
*/
@media (device-height: 568px) and (-webkit-min-device-pixel-ratio: 2) { 


  
}

/*
PRINT STYLESHEET
*/
@media print {
  * { background: transparent !important; color: black !important; text-shadow: none !important; filter:none !important; -ms-filter: none !important; } /* Black prints faster: h5bp.com/s */
  a, a:visited { text-decoration: underline; }
  a[href]:after { content: " (" attr(href) ")"; }
  abbr[title]:after { content: " (" attr(title) ")"; }
  .ir a:after, a[href^="javascript:"]:after, a[href^="#"]:after { content: ""; }  /* Don't show links for images, or javascript/internal links */
  pre, blockquote { border: 1px solid #999; page-break-inside: avoid; }
  thead { display: table-header-group; } /* h5bp.com/t */
  tr, img { page-break-inside: avoid; }
  img { max-width: 100%% !important; }
  @page { margin: 0.5cm; }
  p, h2, h3 { orphans: 3; widows: 3; }
  h2, h3 { page-break-after: avoid; }
} """


if __name__ == '__main__':
    simpleCss % simpleTheme

