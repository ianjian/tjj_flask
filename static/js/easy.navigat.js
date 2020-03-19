
//----------------------------------------------------------------------
//无障碍快捷键及工具条调用DivJS
//Version：V0.02
//Author：
//Date：2012-1-16
//----------------------------------------------------------------------

//最外面div的ID,Jquery的  content_mzj   maincontainer
var divID = "#maincontainer";

//最外面div的ID,纯JS的
var divIDJs = "maincontainer";

//工具条操作说明
var AccessToolURL = "/id_wzall201803160659387899/column.shtml";


//工具条监听函数
function toolBarKeyDownEvent(sKeycode, e) {			
	if (sKeycode == 74 && e.altKey && !e.shiftKey && !e.ctrlKey){
		//Alt+J:工具条开关
		OpentoolBar();
		$("#fontbigorsmall").focus();
	}else if(sKeycode == 74 && e.altKey && e.shiftKey && !e.ctrlKey){
		//Alt+Shift+J:纯文本开关
		OpentoolBar();
		textMode();
	}
}

var toolBarDiv;
var ModeState = false;
var tBState = false;
var LinesState = false;
var barstater = false;
//灰色
var StyleType2="#ddd";
//蓝色边框
var StyleType3="#2fccff";
var BarStyle = "border:2px solid #101010;margin:7px 1px;background-color:#FFFFFF;color:#101010;padding:0px 0px;font-size:17px;font-weight:bold;line-height:16px;height:30px;";
var fontSizeBarStyled = "border:2px solid #101010;margin:7px 1px;background-color:#FFFFFF;color:#101010;padding:0px 0px;font-size:12px;line-height:30px;height:30px;";
var fontSizeBarStyleM = "border:2px solid #101010;margin:7px 1px;background-color:#FFFFFF;color:#101010;padding:0px 0px;font-size:18px;line-height:30px;height:30px;";
var fontSizeBarStyleB = "border:2px solid #101010;margin:7px 1px;background-color:#FFFFFF;color:#101010;padding:0px 0px;font-size:20px;line-height:28px;height:30px;";
var fontSizeBarStyleXB = "border:2px solid #101010;margin:7px 1px;background-color:#FFFFFF;color:#101010;padding:0px 0px;font-size:22px;line-height:26px;height:30px;";
var fontSizeBarStyleXBB = "border:2px solid #101010;margin:7px 1px;background-color:#FFFFFF;color:#101010;padding:0px 0px;font-size:22px;font-weight:bold;line-height:25px;height:30px;";
function ToolBarDiv() {
  var isIE = (navigator.appName == 'Microsoft Internet Explorer');
    toolBarDiv = "";
    //如果是FF，不显示页面缩放
    if(!isIE){
        toolBarDiv = toolBarDiv + "<input  id=\"fontbigorsmall\" type=\"button\" value=\"文字缩放\" onclick=\"setFontsizediv()\"  title=\"文字缩放\" style=\"" + BarStyle + "width:100px;\"/>";
        toolBarDiv = toolBarDiv + "<input id=\"Contras\" type=\"button\" value=\"对比度调整\" onclick=\"SetPageContrasDiv()\"  title=\"对比度调整\" style=\"" + BarStyle + "width:100px;\"/>";   
        toolBarDiv = toolBarDiv + "<input  id=\"textChannel\" type=\"button\" value=\"纯文本通道\" onclick=\"textMode()\"  title=\"纯文本通道\" style=\"" + BarStyle + "width:100px;\" />";
        toolBarDiv = toolBarDiv + "<input  id=\"Linesbutton\" type=\"button\" value=\"开启辅助线\" title=\"开启辅助线\" onclick=\"LinesOpen();\" style=\"" + BarStyle + "width:100px;\" />";
        toolBarDiv = toolBarDiv + "<input  id=\"Descbutton\" type=\"button\" value=\"无障碍操作说明\" title=\"无障碍的操作说明\" onclick=\"AccessDesc();\" style=\"" + BarStyle + "width:150px;\" />";
        toolBarDiv = toolBarDiv + "<input  id=\"Resetbutton\" type=\"button\"  value=\"重置\" title=\"重置\" onclick=\"ReSet()\" style=\"" + BarStyle + "width:80px;\" />";
        toolBarDiv = toolBarDiv + "<input  id=\"Cloesebutton\" type=\"button\" value=\"关闭\" title=\"关闭\" onclick=\"CloseBar()\" style=\"" + BarStyle + "width:80px;\" />";
    }else{
        toolBarDiv = toolBarDiv + "<input  id=\"fontbigorsmall\" type=\"button\" value=\"文字缩放\" onclick=\"setFontsizediv()\"  title=\"文字缩放\" style=\"" + BarStyle + "width:100px;\"/>";
        toolBarDiv = toolBarDiv + "<input  id=\"Pagebigorsmall\" type=\"button\" onclick=\"SetPageZoomDiv()\"  value=\"页面缩放\" title=\"页面缩放\" style=\"" + BarStyle + "width:100px;\"/>";
        toolBarDiv = toolBarDiv + "<input id=\"Contras\" type=\"button\" value=\"对比度调整\" onclick=\"SetPageContrasDiv()\"  title=\"对比度调整\" style=\"" + BarStyle + "width:100px;\"/>";   
        toolBarDiv = toolBarDiv + "<input  id=\"textChannel\" type=\"button\" value=\"纯文本通道\" onclick=\"textMode()\"  title=\"纯文本通道\" style=\"" + BarStyle + "width:100px;\" />";
        toolBarDiv = toolBarDiv + "<input  id=\"Linesbutton\" type=\"button\" value=\"开启辅助线\" title=\"开启辅助线\" onclick=\"LinesOpen();\" style=\"" + BarStyle + "width:100px;\" />";
        toolBarDiv = toolBarDiv + "<input  id=\"Descbutton\" type=\"button\" value=\"无障碍操作说明\" title=\"无障碍操作说明\" onclick=\"AccessDesc();\" style=\"" + BarStyle + "width:150px;\" />";
        toolBarDiv = toolBarDiv + "<input  id=\"Resetbutton\" type=\"button\"  value=\"重置\" title=\"重置\" onclick=\"ReSet()\" style=\"" + BarStyle + "width:80px;\" />";
        toolBarDiv = toolBarDiv + "<input  id=\"Cloesebutton\" type=\"button\" value=\"关闭\" title=\"关闭\" onclick=\"CloseBar()\" style=\"" + BarStyle + "width:80px;\" />";
    }

}

//文字缩放 
var FontSizeBarDiv;
function FontSizeDiv(){
    FontSizeBarDiv="";
    FontSizeBarDiv = FontSizeBarDiv + "<input  id=\"fontSizeD\" type=\"button\" onclick=\"SetFontsize('12')\" value=\"默认大小\" title=\"默认大小\" style=\"" + fontSizeBarStyled + "width:100px;\"/>";
    FontSizeBarDiv = FontSizeBarDiv + "<input  id=\"fontSizeM\" type=\"button\" onclick=\"SetFontsize('18')\" value=\"中\" title=\"中\" style=\"" + fontSizeBarStyleM + "width:100px;\"/>";
    FontSizeBarDiv = FontSizeBarDiv + "<input  id=\"fontSizeB\" type=\"button\" onclick=\"SetFontsize('20')\" value=\"大\" title=\"大\" style=\"" + fontSizeBarStyleB + "width:100px;\"/>";
    FontSizeBarDiv = FontSizeBarDiv + "<input  id=\"fontSizeBX\"  type=\"button\" onclick=\"SetFontsize('22')\" value=\"特大\" title=\"特大\"style=\"" + fontSizeBarStyleXB + "width:100px;\"/>";
    FontSizeBarDiv = FontSizeBarDiv + "<input  id=\"fontSizeBXB\" type=\"button\" onclick=\"SetFontsizeBig('22')\" value=\"特大加粗\" title=\"特大加粗\"  style=\"" + fontSizeBarStyleXBB + "width:100px;\"/>";
}

var PageZoomBarDiv;
//页面缩放 
function PageZoomDiv(){
    PageZoomBarDiv="";
    PageZoomBarDiv = PageZoomBarDiv + "<input  id=\"PageZommD\" type=\"button\" onclick=\"SetPageZom('1')\" value=\"默认大小\" title=\"默认大小\" style=\"" + BarStyle + "width:100px;\"/>";
    PageZoomBarDiv = PageZoomBarDiv + "<input  id=\"PageZommM\" type=\"button\" onclick=\"SetPageZom('1.2')\" value=\"120%\" title=\"120%\" style=\"" + BarStyle + "width:100px;\"/>";
    PageZoomBarDiv = PageZoomBarDiv + "<input  id=\"PageZommB\" type=\"button\" onclick=\"SetPageZom('1.4')\" value=\"140%\" title=\"140%\" style=\"" + BarStyle + "width:100px;\"/>";
    PageZoomBarDiv = PageZoomBarDiv + "<input  id=\"PageZommBX\"  type=\"button\" onclick=\"SetPageZom('1.6')\" value=\"160%\" title=\"160%\"style=\"" + BarStyle + "width:100px;\"/>";
    PageZoomBarDiv = PageZoomBarDiv + "<input  id=\"PageZommBXB\" type=\"button\" onclick=\"SetPageZom('1.8')\" value=\"180%\" title=\"180%\"  style=\"" + BarStyle + "width:100px;\"/>";
    
}

//对比度调整 
var PageBarContrasDiv;
function PageContrasDiv(){
    var isIE = (navigator.appName == 'Microsoft Internet Explorer');
    PageBarContrasDiv="";
    PageBarContrasDiv = PageBarContrasDiv + "<input  id=\"PageContrasD\" type=\"button\" onclick=\"PageDefault()\" value=\"默认对比度\" title=\"默认对比度\" style=\"" + BarStyle + "width:100px;\"/>";
    if(isIE){
    PageBarContrasDiv = PageBarContrasDiv + "<input  id=\"PageContrasB\" type=\"button\" onclick=\"PageGray()\" value=\"灰色对比度\" title=\"灰色对比度\" style=\"" + BarStyle + "width:100px;\"/>";
    }
    PageBarContrasDiv = PageBarContrasDiv + "<input  id=\"PageContrasG\" type=\"button\" onclick=\"Pagehigh()\" value=\"黑白对比度\" title=\"黑白对比度\" style=\"" + BarStyle + "width:100px;\"/>";
}


var FontsizedivState = false;
//创建文字放大的DIV
function setFontsizediv(){
  if (!FontsizedivState){
      $("#PageZoomID").hide();
        $("#PageContrasID").hide();
         $("#FontSizeID").hide();
         
          $("#Pagebigorsmall").css("borderColor","#101010");
          $("#Contras").css("borderColor","#101010");
          $("#Descbutton").css("borderColor","#101010");
            $("#Resetbutton").css("borderColor","#101010");
            $("#Cloesebutton").css("borderColor","#101010");
            $("#textChannel").css("borderColor","#101010");
            $("#Linesbutton").css("borderColor","#101010");  
    $("#fontbigorsmall").css("borderColor","#2fccff"); 
       FontSizeDiv();
       var FontSizeElement = document.createElement("div");
        FontSizeElement.setAttribute("id", "FontSizeID");
        FontSizeElement.style.cssText = "text-align:center;width:872px;height:40px;no-repeat:0;margin:0 165px;";
        FontSizeElement.innerHTML = FontSizeBarDiv;
        document.body.insertBefore(FontSizeElement, document.body.childNodes[1]);
        document.body.style.position = "relative";
        document.body.style.paddingTop = 80+"px";
         $("#FontSizeID").css("left", 0+"px");
        $("#FontSizeID").css("position", "absolute");
        $("#FontSizeID").css("paddingTop",38+"px");
        $("#FontSizeID").css("top", document.documentElement.scrollTop + "px");
        
          $("#fontbigorsmall").css("borderColor","#2fccff"); 
          $("#fontSizeD").css("borderColor","#2fccff");
          $("#fontSizeM").css("borderColor","#2fccff");
          $("#fontSizeB").css("borderColor","#2fccff");
          $("#fontSizeBX").css("borderColor","#2fccff");
          $("#fontSizeBXB").css("borderColor","#2fccff");
        FontsizedivState=true;
           
     }else{  
        $("#PageZoomID").hide();
        $("#PageContrasID").hide(); 
        $("#FontSizeID").show();
         document.body.style.paddingTop = 80+"px";
        
          $("#fontbigorsmall").css("borderColor","#2fccff");
          $("#Pagebigorsmall").css("borderColor","#101010");
          $("#Contras").css("borderColor","#101010");
          $("#Descbutton").css("borderColor","#101010");
          $("#Resetbutton").css("borderColor","#101010");
          $("#Cloesebutton").css("borderColor","#101010");
          $("#textChannel").css("borderColor","#101010"); 
          $("#Linesbutton").css("borderColor","#101010");
             
        FontsizedivState=false; 
   }  
}

var PageZoomState =false
//创建页面放大的DIV 
function SetPageZoomDiv(){      
     if(!PageZoomState){
       PageZoomDiv();
          $("#FontSizeID").hide();
          $("#PageContrasID").hide(); 
          $("#PageZoomID").hide(); 
          $("#fontbigorsmall").css("borderColor","#101010");
          $("#Contras").css("borderColor","#101010");
          $("#Descbutton").css("borderColor","#101010");
          $("#Resetbutton").css("borderColor","#101010");
          $("#Cloesebutton").css("borderColor","#101010");
          $("#textChannel").css("borderColor","#101010"); 
          $("#Linesbutton").css("borderColor","#101010"); 
       var PageZoomElement = document.createElement("div");
        PageZoomElement.setAttribute("id", "PageZoomID");
        PageZoomElement.style.cssText = "text-align:center;background:url('/pz.jpg');width:872px;height:40px;no-repeat:0;margin:0 165px;";
        PageZoomElement.innerHTML = PageZoomBarDiv;
        document.body.insertBefore(PageZoomElement, document.body.childNodes[1]);
        document.body.style.position = "relative";
        document.body.style.paddingTop = 80+"px";
        $("#PageZoomID").css("paddingTop",38+"px");
         $("#PageZoomID").css("left", 0+"px");
        $("#PageZoomID").css("position", "absolute");
        $("#PageZoomID").css("top", document.documentElement.scrollTop + "px");
        
          $("#Pagebigorsmall").css("borderColor","#2fccff");
      
          $("#PageZommD").css("borderColor","#2fccff");
          $("#PageZommM").css("borderColor","#2fccff");
          $("#PageZommB").css("borderColor","#2fccff");
          $("#PageZommBX").css("borderColor","#2fccff");
          $("#PageZommBXB").css("borderColor","#2fccff");
      
        PageZoomState=true;  
     }else{ 
       $("#FontSizeID").hide();
       $("#PageContrasID").hide();  
       $("#PageZoomID").show(); 
       document.body.style.paddingTop = 80+"px"; 
       $("#Pagebigorsmall").css("borderColor","#2fccff"); 
       $("#fontbigorsmall").css("borderColor","#101010");
       $("#Contras").css("borderColor","#101010"); 
       $("#Descbutton").css("borderColor","#101010");
       $("#Resetbutton").css("borderColor","#101010");
       $("#Cloesebutton").css("borderColor","#101010");
       $("#textChannel").css("borderColor","#101010");
       $("#Linesbutton").css("borderColor","#101010");  
            
        PageZoomState=false; 
     }
}

var PageContrasState = false;
//创建对比度的DIV 
function SetPageContrasDiv(){
     if(!PageContrasState){
       PageContrasDiv();
       $("#PageZoomID").hide();
       $("#FontSizeID").hide();
      $("#PageContrasID").hide();
      
      $("#fontbigorsmall").css("borderColor","#101010");
       $("#Pagebigorsmall").css("borderColor","#101010"); 
       $("#Descbutton").css("borderColor","#101010");
            $("#Resetbutton").css("borderColor","#101010");
             $("#Cloesebutton").css("borderColor","#101010");  
              $("#textChannel").css("borderColor","#101010"); 
             $("#Linesbutton").css("borderColor","#101010");   
       var PageContrasElement = document.createElement("div");
        PageContrasElement.setAttribute("id", "PageContrasID"); //140px
        PageContrasElement.style.cssText = "text-align:center;background:url('/pc.jpg');width:872px;height:40px;no-repeat:0;margin:0 165px;";
        PageContrasElement.innerHTML = PageBarContrasDiv;
        document.body.insertBefore(PageContrasElement, document.body.childNodes[1]);
        document.body.style.position = "relative";
        document.body.style.paddingTop = 80+"px";
         $("#PageContrasID").css("left", 0+"px");
         $("#PageContrasID").css("paddingTop",38+"px");
        $("#PageContrasID").css("position", "absolute");
        $("#PageContrasID").css("top", document.documentElement.scrollTop + "px"); 
        
          $("#PageContrasD").css("borderColor","#2fccff");
           $("#Contras").css("borderColor","#2fccff");
          $("#PageContrasB").css("borderColor","#2fccff");
           $("#PageContrasG").css("borderColor","#2fccff"); 
       
        PageContrasState=true;
     }else{
        $("#PageZoomID").hide();
        $("#FontSizeID").hide();  
        $("#PageContrasID").show();  
         document.body.style.paddingTop = 80+"px";
           $("#Contras").css("borderColor","#2fccff");
           $("#fontbigorsmall").css("borderColor","#101010");
           $("#Pagebigorsmall").css("borderColor","#101010");
           $("#Descbutton").css("borderColor","#101010");
           $("#Resetbutton").css("borderColor","#101010");
           $("#Cloesebutton").css("borderColor","#101010"); 
           $("#textChannel").css("borderColor","#101010"); 
           $("#Linesbutton").css("borderColor","#101010"); 
           
        PageContrasState=false; 
     }
}

var allElements = new Array();
// 文字变大 
function SetFontsize(size)
{
  document.getElementById(divIDJs).style.fontSize=size+'px';
  document.getElementById(divIDJs).style.fontWeight="normal";
  allElements = document.getElementById(divIDJs).getElementsByTagName("*");
  for(var i=0;i<allElements.length;i++){
			allElements[i].style.fontSize = size+"px";
			allElements[i].style.fontWeight="normal";
		}
     setCookie("FontSizeState",size); 
}

//文字特大加粗 
function SetFontsizeBig(size)
{
    document.getElementById(divIDJs).style.fontSize=size+'px';
    document.getElementById(divIDJs).style.fontWeight="bold";
    allElements = document.getElementById(divIDJs).getElementsByTagName("*");
  for(var i=0;i<allElements.length;i++){
			allElements[i].style.fontSize = size+"px";
			allElements[i].style.fontWeight="bold";
		}
     setCookie("FontSizeStates",size); 
 
}


//页面放大 
function SetPageZom(pzoom){
       $("#ZoomLinesYLine").css("height", document.body.offsetHeight + "px");
        $("#ZoomLinesYLine").css("height", document.body.scrollHeight + "px");
        
        $("#ZoomLinesXLine").css("width", document.documentElement.offsetWidth + "px");
        $("#ZoomLinesXLine").css("width", document.documentElement.scrollWidth + "px");
        
        $("#ZoomLinesYLine").css("width", LinesWidth + "px");
        $("#ZoomLinesXLine").css("height", LinesWidth + "px");
        
       $("#ZoomLinesYLine").css("opacity", "100%");
      $("#ZoomLinesYLine").css("opacity", "100%");
        
   document.getElementById(divIDJs).style.zoom = pzoom;
   setCookie("PageZoomsState",pzoom);   
}

//文字显示
function FontsizeShow(){
       FontSizeDiv();
       var FontSizeElement = document.createElement("div");
        FontSizeElement.setAttribute("id", "FontSizeID");
        FontSizeElement.style.cssText = "text-align:center;width:100%;background:#FFF;";
        FontSizeElement.innerHTML = FontSizeBarDiv;
        document.body.insertBefore(FontSizeElement, document.body.childNodes[0]);
        document.body.style.paddingTop = 40+"px";
        $("#FontSizeID").css("position", "absolute");

}

//隐藏文字 
function FontsizeHide(){
  $("#FontSizeID").hide();
}

//界面显示 
function PageZoomShow(){
        PageZoomDiv();
        var PageZoomElement = document.createElement("div");
        PageZoomElement.setAttribute("id", "PageZoomID");
        PageZoomElement.style.cssText = "text-align:center;width:100%;background:#FFF;";
        PageZoomElement.innerHTML = PageZoomBarDiv;
        document.body.insertBefore(PageZoomElement, document.body.childNodes[0]);
        document.body.style.paddingTop = 40+"px";
        $("#PageZoomID").css("position", "absolute");
}

//界面隐藏 
function PageZoomHide(){
   $("#PageZoomID").hide();
}

//对比度显示
function PageContrasShow(){
        PageContrasDiv();
        var PageContrasElement = document.createElement("div");
        PageContrasElement.setAttribute("id", "PageContrasID");
        PageContrasElement.style.cssText = "text-align:center;width:100%;background:#FFF;";
        PageContrasElement.innerHTML = PageBarContrasDiv;
        document.body.insertBefore(PageContrasElement, document.body.childNodes[0]);
        document.body.style.paddingTop = 40+"px";
        $("#PageContrasID").css("position", "absolute");
}

//对比度隐藏
function PageContrasHide(){
    $("#PageContrasID").hide();
}

//重置功能 
function ReSet() {
   setCookie("BarState",1);
   delCookie("FontSizeState");
   delCookie("PageZoomsState");
   delCookie("PageContraState");
   delCookie("guidesState");
   delCookie("textModeState");
     window.location.reload();
}


var CloseBarState=false; 
//关闭  
function CloseBar() {

       $("#barId").hide();
       $("#PageZoomID").hide();
       $("#PageContrasID").hide(); 
       $("#FontSizeID").hide();   
       setCookie("BarState",0);
      document.body.style.paddingTop = 0+"px";  

}


//toolsDiv悬浮 
var guidesState = false;
window.onscroll = function() {
    if (tBState) {
        //谷歌浏览器  
        if (window.MessageEvent && !document.getBoxObjectFor) {
            $("#barId").css("top", document.body.scrollTop + "px");
             //文字缩放悬浮
            $("#FontSizeID").css("top", document.body.scrollTop + "px");
            //界面缩放悬浮
            $("#PageZoomID").css("top", document.body.scrollTop + "px");
            //对比度悬浮
            $("#PageContrasID").css("top", document.body.scrollTop + "px"); 
            
        }
        //火狐 
        if (document.getBoxObjectFor) {
            //工具
            $("#barId").css("top", document.documentElement.scrollTop + "px");
            //文字缩放悬浮
            $("#FontSizeID").css("top", document.documentElement.scrollTop + "px");
            //界面缩放悬浮
            $("#PageZoomID").css("top", document.documentElement.scrollTop + "px");
            //对比度悬浮
            $("#PageContrasID").css("top", document.documentElement.scrollTop + "px"); 
        }
        //IE if(window.ActiveXObject)
        else {
            $("#barId").css("top", document.documentElement.scrollTop + "px");         
            //文字缩放悬浮
            $("#FontSizeID").css("top", document.documentElement.scrollTop + "px");
            //界面缩放悬浮
            $("#PageZoomID").css("top", document.documentElement.scrollTop + "px");
            //对比度悬浮
            $("#PageContrasID").css("top", document.documentElement.scrollTop + "px");  
            
        }
    }
}

//打开工具条
function OpentoolBar() {
    //OpenSetCookie();
    if (!tBState) {
        ToolBarDiv();
        var toolDivElement = document.createElement("div");
        toolDivElement.setAttribute("id", "barId");
        toolDivElement.style.cssText = "text-align:center;width:100%;background:#FFF;";
        toolDivElement.innerHTML = toolBarDiv; 
        document.body.insertBefore(toolDivElement,document.body.childNodes[0]);
        document.body.style.position = "relative";
        document.body.style.paddingTop = 50+"px";
        $("#barId").css("position", "absolute");
        $("#barId").css("left", 0+"px");
        $("#barId").css("top", document.documentElement.scrollTop + "px");
        setCookie("BarState",1);       
          
        var LinesElement = document.createElement("div");
        LinesElement.setAttribute("id", "Lines");
        LinesElement.style.zIndex = 160;
        LinesElement.innerHTML = LinesHTML;
        document.body.insertBefore(LinesElement, document.body.childNodes[0]);
        
        var LinesElement = document.createElement("div");
        LinesElement.setAttribute("id", "ZoomLines");
        LinesElement.style.zIndex = 160;
        LinesElement.innerHTML = ZoomLinesHTML;
        document.body.insertBefore(LinesElement, document.body.childNodes[0]);
        
        tBState = true;
    } else {
        $("#barId").hide();
        tBState = false;
        setCookie("BarState",0);
        window.location.reload();
    }
      
}


//工具条样式及定位函数 
function toolBarPosition(){
	document.body.style.position = "relative";
	document.body.style.paddingTop = 30+"px";
	$("toolbar").style.position = "absolute";
	$("toolbar").style.top = document.documentElement.scrollTop+"px";
	$("toolbar").style.left = 0+"px";
	$("toolbar").style.zIndex = 202;
}

//字体放大缩小
var initial_fontsize = 10;
var initial_lineheight = 15;
function setFontsize(type, objname) {
    var whichEl = document.getElementById(objname);
    if (whichEl != null) {
        if (type == 1) {
            if (initial_fontsize < 64) {
                whichEl.style.fontSize = (++initial_fontsize) + 'pt';
                whichEl.style.lineHeight = (++initial_lineheight) + 'pt';
            }
        } else {
            if (initial_fontsize > 12) {
                whichEl.style.fontSize = (--initial_fontsize) + 'pt';
                whichEl.style.lineHeight = (--initial_lineheight) + 'pt';
            }
        }
    }
}


//页面扩大缩小
var dPageS = 1;
function pageSize(mode) {
    if (mode == "0") {
        dPageS = dPageS + 0.2;
        if (dPageS > 4) {
            dPageS = 4;
        };
    }
    else if (mode == "1") {
        dPageS = dPageS - 0.2;
        if (dPageS < 1) {
            dPageS = 1;
        };
    }
    //火狐
    $(divID).css("line-height", dPageS + "em");
    //谷歌和IE 
    document.getElementById(divIDJs).style.zoom = dPageS;
}


//灰色对比度
function PageGray(){
 var allElementss = new Array();
        allElementss = document.getElementById(divIDJs).getElementsByTagName("*");
        for(var j=0;j<allElementss.length;j++){
           allElementss[j].style.backgroundColor = "";
           allElementss[j].style.color = "";
           
        }
        $(divID).css("backgroundColor", "");
        $(divID).css("color", "")
				document.body.className="Gray";
				document.body.style.filter="Gray";
			    setCookie("PageContraState",1); 
   }


//黑白对比度
var State = false;
function Pagehigh() {
       document.body.className='';
       document.body.style.filter='';
        
        var allElementss = new Array();
        allElementss = document.getElementById(divIDJs).getElementsByTagName("*");
        for(var i=0;i<allElementss.length;i++){
           allElementss[i].style.backgroundColor = "#000";
           allElementss[i].style.color = "#FFF"; 
        }
        $(divID).css("backgroundColor", "#000");
        $(divID).css("color", "#FFF");
        setCookie("PageContraState",2); 
     
}


//还原对比度
function PageDefault(){

     document.body.className='';
     document.body.style.filter='';
   
     var allElementss = new Array();
        allElementss = document.getElementById(divIDJs).getElementsByTagName("*");
        for(var j=0;j<allElementss.length;j++){
           allElementss[j].style.backgroundColor = "";
           allElementss[j].style.color = "";
           
        }
        $(divID).css("backgroundColor", "");
        $(divID).css("color", "");


      setCookie("PageContraState",0); 
}

//纯文本通道
var allFrame = new Array();
var allLink = new Array();
var allTd = new Array();
var allTr = new Array();
var ModeState = false;
function textMode() {
     $("#PageZoomID").hide();
     $("#PageContrasID").hide(); 
     $("#FontSizeID").hide(); 
       document.body.style.paddingTop = 50+"px";
       $("#Linesbutton").css("borderColor","#101010");
       $("#Contras").css("borderColor","#101010");
       $("#fontbigorsmall").css("borderColor","#101010");
       $("#Pagebigorsmall").css("borderColor","#101010"); 
       $("#Descbutton").css("borderColor","#101010");
       $("#Resetbutton").css("borderColor","#101010");
       $("#Cloesebutton").css("borderColor","#101010");
       $("#textChannel").css("borderColor","#2fccff");
    if (!ModeState) {
            ImgMode();
            $("div").attr("class","");
        
             $("table").attr("background","");
             $("table").attr("bgColor","");
             $("table").attr("class","");
        

        
             $("A").attr("background","");
             $("A").attr("bgColor","");
             $("A").attr("class","");
        
            $("tr").attr("background","");
            $("tr").attr("bgColor","");
            $("tr").attr("class",""); 
            
             $("td").attr("background","");
             $("td").attr("bgColor","");
             $("td").attr("class",""); 
        
        //移除iframe
        allFrame = document.getElementById(divIDJs).getElementsByTagName("iframe");
        var tempVar2 = allFrame.length;
        for (var i = 0; i < allFrame.length; i++) {
            allFrame[0].parentNode.removeChild(allFrame[0]);
        }
   
        if ($("textChannel")) 
        { 
            document.getElementById("textChannel").setAttribute("value", "还原纯文本");
         }
        //清除样式 
        var ClearCss = document.getElementById(divIDJs).getElementsByTagName("*");
        for (var i = 0; i < ClearCss.length; i++) {
            ClearCss[i].style.cssText = "";
        }
        
        for(var j=0;j<ClearCss.length;j++){
            ClearCss[j].style.height = "auto";
        }
        //重新加载后清除图片  
         var allElementss = new Array();
         allElementss = document.getElementById(divIDJs).getElementsByTagName("IMG");
         for (var i = 0; i < allElementss.length; i++) {
            $("IMG").hide();
         }
          ModeState = true;
          	setCookie("textModeState",1);
       }
    else {
        window.location.reload();
        $("#Linesbutton").css("borderColor","#101010");
        $("#Contras").css("borderColor","#101010");
        $("#fontbigorsmall").css("borderColor","#101010");
        $("#Pagebigorsmall").css("borderColor","#101010"); 
        $("#Descbutton").css("borderColor","#101010");
        $("#Resetbutton").css("borderColor","#101010");
        $("#Cloesebutton").css("borderColor","#101010");
        $("#textChannel").css("borderColor","#2fccff");
         ModeState = false;
        setCookie("textModeState",0);
    }
}

//清除图片 
function ImgMode() {
    var pic = document.getElementsByTagName('IMG');
    var imgtxt;
        var allElementss = new Array();
        allElementss = document.getElementById(divIDJs).getElementsByTagName("IMG");
        for (var i = 0; i < allElementss.length; i++) {
            $("IMG").eq(i).before($("IMG")[i].alt);
            $("IMG").hide();
        }
}

var LinesWidth = 4;
var LinesColor = "blue";
var LinesGuis = 5;

//开启辅助线
function LinesOpen() {
   $("#PageZoomID").hide();
   $("#PageContrasID").hide(); 
   $("#FontSizeID").hide(); 
   document.body.style.paddingTop = 50+"px";
   
    if (!LinesState) {
       $("#Linesbutton").css("borderColor","#2fccff");
       $("#Contras").css("borderColor","#101010");
       $("#fontbigorsmall").css("borderColor","#101010");
       $("#Pagebigorsmall").css("borderColor","#101010"); 
        $("#Descbutton").css("borderColor","#101010");
        $("#Resetbutton").css("borderColor","#101010");
        $("#Cloesebutton").css("borderColor","#101010"); 
        $("#textChannel").css("borderColor","#101010");
        $("#LinesYLine").css("display", "block");
        $("#LinesXLine").css("display", "block");
        
        $("#LinesYLine").css("height", document.body.offsetHeight + "px");
        $("#LinesYLine").css("height", document.body.scrollHeight + "px");
        
        $("#LinesXLine").css("width", document.documentElement.offsetWidth + "px");
        $("#LinesXLine").css("width", document.documentElement.scrollWidth + "px");
        
        $("#LinesYLine").css("width", LinesWidth + "px");
        $("#LinesXLine").css("height", LinesWidth + "px");
        $("#LinesYLine").css("backgroundColor", LinesColor);
        $("#LinesXLine").css("backgroundColor", LinesColor);
        
         $("#Linesbutton").attr("value", "关闭辅助线").attr("title", "关闭辅助线");
        document.onmousemove = moveLines;
        LinesState = true;
        
        setCookie("guidesState",1);
    }
    else {
      
       $("#Linesbutton").attr("value", "开启辅助线").attr("title", "开启辅助线"); 
       $("#LinesYLine").css("display", "none");
       $("#LinesXLine").css("display", "none");
       $("#Linesbutton").css("borderColor","#2fccff");
       $("#Contras").css("borderColor","#101010");
       $("#fontbigorsmall").css("borderColor","#101010");
       $("#Pagebigorsmall").css("borderColor","#101010");
       $("#Descbutton").css("borderColor","#101010");
       $("#Resetbutton").css("borderColor","#101010");
       $("#Cloesebutton").css("borderColor","#101010"); 
       $("#textChannel").css("borderColor","#101010"); 
       LinesState = false; 
       setCookie("guidesState",0); 
    }
    
}



//辅助线位置控制函数 
function moveLines(e) {
var isIE = (navigator.appName == 'Microsoft Internet Explorer');
    if (!LinesState) {
        return false;
    }
    e = window.event ? window.event : e;
    if (isIE) 
    {
    
        $("#LinesYLine").css("left", (e.clientX + (document.documentElement.scrollLeft || document.body.scrollLeft)) + LinesGuis + "px");
    } 
    else 
    {
        $("#LinesYLine").css("left", e.pageX + LinesGuis + "px");
    }

    if (isIE) 
    {
        $("#LinesXLine").css("top", (e.clientY + (document.documentElement.scrollTop || document.body.scrollTop)) + LinesGuis + "px");
    } 
    else 
    {
        $("#LinesXLine").css("top", e.pageY + LinesGuis + "px");
    }
     
}


//浏览器类型判断 
var browser;
var Sys = {};
var ua = navigator.userAgent.toLowerCase();
function browserType() {
    browser = true;
    if (window.ActiveXObject)

        Sys.ie = ua.match(/msie ([\d.]+)/)[1]

    else {
        browser = false;
    }
}

//var contstr="";
var pageLoad = false;
window.onload = function(){
      // $("#weather").append("<a  href='http://www.soweather.com/' target='_blank'>阴到多云&nbsp;5℃～9℃</a><a  href='http://www.sepb.gov.cn/hb/fa/cms/shhj/hjzl_login.jsp?flag=1' target='_blank'>预计空气质量 优</a>");
      // addKeyListenerToIframe();
       //getWeather();
       browserType();
       OpenSetCookie(); 
       $("#TopContents_DIV").focus(); 
       pageLoad = true;
}


////在iframe中增加监听调用父页面监听函数
//function addKeyListenerToIframe(){
//	var iframeNode = document.body.getElementsByTagName("iframe");
//	if(!iframeNode){return;}	
//	for(var i=0;i<iframeNode.length;i++){
//		var iframeObject = iframeNode[i].contentWindow;
//		try{
//			var scriptNode = iframeObject.document.createElement("script");
//			scriptNode.setAttribute("type","text/javascript");
//			scriptNode.text = "document.onkeydown = function(e){var currkey=0, e=e||event||window.event; currkey=e.keyCode||e.which||e.charCode; parent.accessKeyboardListener(currkey,e);}";			
//			iframeObject.document.getElementsByTagName("head")[0].appendChild(scriptNode);
//		}catch(e){}
//	}
//}

//判断开启工具条的Cookie
function StartCookie(){
	if(document.cookie ==""){
		setCookie("BarState",0);
		 $("#barId").hide();
	}
	else{
		if(getCookie("BarState") == 1)
		{
		   OpentoolBar();
		}
	}
}

//cookie设置
function setCookie(setName,ValueName){
	if(setName == undefined||ValueName == undefined){
	return false;
	}
	var Days = 30;
	var exp = new Date(); 
	exp.setTime(exp.getTime() + Days*24*3600*1000);
	document.cookie = setName+"="+ escape(ValueName)+";expires="+exp.toGMTString()+";path=/;";

}
//cookie读取
function getCookie(name){
    var arr = document.cookie.match(new RegExp("(^| )"+name+"=([^;]*)(;|$)"));
    if(arr != null) 
    return unescape(arr[2]); 
    return null;
}

//删除Cookie
function delCookie(name)
{ 
    var exp = new Date(); 
    exp.setTime(exp.getTime() - 1); 
    var cval=getCookie(name); 
    if(cval!=null) document.cookie= name + "="+cval+";expires="+exp.toGMTString()+";path=/;"; 
} 

//开启Cookie 
function OpenSetCookie(){
   if(document.cookie ==""){
     setCookie("BarState",0);
     setCookie("FontSizeState",12); 
     setCookie("PageZoomsState",1);
     setCookie("PageContraState",0); 
     setCookie("guidesState",0);
     setCookie("textModeState",0);    
  }else{
  //开启工具条 
    if(getCookie("BarState") == 1)
	{
	   OpentoolBar();
	}
  
  //文字缩放
    if(getCookie("FontSizeState")>12){
       if(getCookie("BarState")==0){
         OpentoolBar();
       }
      setFontsizediv(); 
      SetFontsize(getCookie("FontSizeState")); 
        
    }

   //页面缩放
   if(getCookie("PageZoomsState")>1){
       if(getCookie("BarState")==0){
         OpentoolBar();
       }
       SetPageZoomDiv();
       SetPageZom(getCookie("PageZoomsState"));  
     
    }
   
   //对比度(灰色)
     if(getCookie("PageContraState")==1){
       if(getCookie("BarState")==0){
         OpentoolBar();
       }
       PageGray(); 
       SetPageContrasDiv(); 
    }
    
     //对比度(黑白色)
      if(getCookie("PageContraState")==2){
       if(getCookie("BarState")==0){
         OpentoolBar();
       }
       Pagehigh(); 
       SetPageContrasDiv(); 
    }
    
     //辅助线
     if (getCookie("guidesState") == 1) {
       if(getCookie("BarState")==0){
         OpentoolBar();
       } 
        LinesOpen();
      }
     
     
    //纯文本 
    if (getCookie("textModeState") == 1) { 
        if(getCookie("BarState")==0){
         OpentoolBar();
       } 
        textMode();
      }
   }
}



var LinesHTML = "<div id=\"LinesXLine\" style=\"position:absolute;width:100%;left:0px;font-size:0px;line-height:0px;z-index:200;\"></div><div id=\"LinesYLine\" style=\"position:absolute;height:100%;top:0px;font-size:0px;line-height:0px;z-index:201;\"></div>";

var ZoomLinesHTML = "<div id=\"ZoomLinesXLine\" style=\"position:absolute;width:100%;left:0px;font-size:0px;line-height:0px;z-index:200;\"></div><div id=\"ZoomLinesYLine\" style=\"position:absolute;height:100%;top:0px;font-size:0px;line-height:0px;z-index:201;\"></div>";


var AccessDescSate=false;
//操作说明方法 
function AccessDesc(){
 $("#PageZoomID").hide();
 $("#PageContrasID").hide(); 
  $("#FontSizeID").hide(); 
   document.body.style.paddingTop = 50+"px";
if(!AccessDescSate){
       $("#Linesbutton").css("borderColor","#101010");
       $("#Contras").css("borderColor","#101010");
       $("#fontbigorsmall").css("borderColor","#101010");
       $("#Pagebigorsmall").css("borderColor","#101010"); 
       $("#Descbutton").css("borderColor","#2fccff");
       $("#Resetbutton").css("borderColor","#101010");
       $("#Cloesebutton").css("borderColor","#101010"); 
       $("#textChannel").css("borderColor","#101010");
       window.open(AccessToolURL);
       AccessDescSate=true;
  }
  else{
       $("#Linesbutton").css("borderColor","#101010");
       $("#Contras").css("borderColor","#101010");
       $("#fontbigorsmall").css("borderColor","#101010");
       $("#Pagebigorsmall").css("borderColor","#101010"); 
       $("#Descbutton").css("borderColor","#2fccff");
       $("#Resetbutton").css("borderColor","#101010");
       $("#Cloesebutton").css("borderColor","#101010");
       $("#textChannel").css("borderColor","#101010");
       AccessDescSate=false;
  }
}

