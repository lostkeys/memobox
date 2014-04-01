body {
/*    background-color: #EDF4F5;*/ /* #054950 #789A9F #EDF4F5 #FFFFFF #F78F1E */
}

.jumbotron {
    padding: 15px 0;
    color: #FFF;
    text-align: left;
    /* text-shadow: 0 1px 3px rgba(0,0,0,.4), 0 0 30px rgba(0,0,0,.075); */
	background-color: #fc423a;
	box-shadow: 0px 10px 0px #bf332d;
	margin-bottom: 20px; 
}

.jumbotron h1 a {
	color: white; 
}

@media (max-width: 767px) {
    .jumbotron {
        padding: 40px 20px;
        margin-right: -20px;
        margin-left: -20px;
    }
}
.navbar {
    border-bottom: 1px solid #ddd;
    margin-bottom: 10px;
}
.breadcrumb > li > span > .divider {
    color: #ccc;
}
.thumbnail {
    background-color: #F5F5F5;
    border: 1px solid #E3E3E3;
    -webkit-border-radius: 4px;
    -moz-border-radius: 4px;
    border-radius: 4px;
    -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
    -moz-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
    box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
    }
    .thumbnail .preview {
        background-size: 260px 260px;
        background-repeat: no-repeat;
        background-position: 50% 50%;
        height: 156px;
        line-height: 156px;
        text-align: right;
    }
    .thumbnail .preview.icon {
        text-align: center;
        }
        .thumbnail .preview.image img {
            width: 48px;
            height: 48px;
            vertical-align: bottom;
        }
        .thumbnail .preview.icon img {
            width: 128px;
            height: 128px;
            vertical-align: middle;
        }
    .thumbnail h3 {
        text-align: center;
        font-size: 1em;
        line-height: 1.1em;
        height: 1.1em;
        overflow: hidden;
        text-shadow: 0 1px #FFFFFF;
        cursor: pointer;
    }
.btn-toolbar {
    text-align: center;
    }
    .btn-toolbar .btn {
        margin-bottom: 5px;
    }

#device-list {
	margin-left: -30px; 
	margin-right: 30px; 	
}

	.device {
		margin-right: 40px; 
		text-align: center; 
		border-radius: 10px; 
		background-color: transparent; 
		padding: 10px; 		
	}
		.device img {
			margin-bottom: 10px; 
		}
		
		.selectedDevice {
			border-radius: 10px; 
			background-color: #DDD; 
			padding: 10px; 		
		}
	

#dateHolder {
      background: #f7e635;
	  /*box-shadow: rgba(0, 0, 0, 0.0980392) 0px 1px 10px 0px;      
	  -webkit-box-shadow: rgba(0, 0, 0, 0.0980392) 0px 1px 10px 0px;	  */
	  -webkit-box-shadow: none; 
	  box-shadow: none;
      color: #fc423a;
      text-align: center;
      padding: 5px;
      margin: auto;
	  margin-right: 15px; 
      border-radius: 3px;
	  font-weight: bold;
	  font-style: italic;
	  display: block; 
	  margin-left: -30px; 
	  /*background: linear-gradient(45deg, rgb(5, 73, 80) 0%, rgb(120, 154, 159) 100%);*/
	  visibility: hidden;
}

	
.date-navbar {
	margin-bottom: 0px;
	margin-right: 30px; 
	border-bottom: 0px;
}

	.date-navbar .navbar-inner {
		background-color: transparent; 
		background-image: none; 
		border: 0px; 
	}

	.date-navbar  #dateHolder-sticky-wrapper .navbar-inner {
		min-height: 30px;
	}

		.date-navbar  #dateHolder-sticky-wrapper .navbar-inner .nav {
			margin-left: 480px; 
			margin-right: 443px;
		}	
	
		.date-navbar #dateHolder-sticky-wrapper ul li a {
			color: #fc423a; 
			text-shadow: none;
			padding-top: 5px; 
			padding-bottom: 5px; 
			font-size: 16px;
		}
		
		.date-navbar #dateHolder-sticky-wrapper ul li .dropdown-menu li a { 
			color: #333;
		}
		
		.date-navbar #dateHolder-sticky-wrapper .nav li.dropdown.open > .dropdown-toggle {
			background-color: transparent;
		}

.thumbnails{
	margin-top: 5px; 
}

#noti_Container {
    position:relative;
}

.noti_bubble {
    position:absolute;
    top: -6px;
    right:-6px;
    padding:5px;
    background-color:#fc423a;
    color:white;
    border-radius:3px;
    box-shadow:1px 1px 1px #bf332d;
}

div.video {
	width: 100%;
	height: 100%;
	background-image: url(/static/images/icons/play.png);
	background-color: rgba(255, 255, 255, 0.5);
	background-position: center center; 
	background-repeat: no-repeat;
}

div.video .typecontent {
	background-color: white;
	padding: 3px;
	position: relative; 
	display: inline;
	width: auto; 
	height: 20px;
	right: 2px; 
	top: -65px;
	line-height: 20px;
}
