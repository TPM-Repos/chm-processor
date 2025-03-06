![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
StartTheme Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic347.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ILiveThemeStarter Interface](topic342.md) : StartTheme Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_configureHttps_
    Determines whether HTTPS should be configured as part of the start up procedure.

_port_
    Optional port number to run the theme on.

_exceptionHandler_
    Optional action to take when an unhandled exception has occurred.

Glossary Item Box

Starts the theme. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function StartTheme( _
       Optional ByVal _configureHttps_ As Boolean, _
       Optional ByVal _port_ As String, _
       Optional ByVal _exceptionHandler_ As Action(Of String) _
    ) As Task(Of ThemeStartResult)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ILiveThemeStarter](topic342.md)
    Dim configureHttps As Boolean
    Dim port As String
    Dim exceptionHandler As Action(Of String)
    Dim value As Task(Of ThemeStartResult)
     
    value = instance.StartTheme(configureHttps, port, exceptionHandler)  
  
C#|   
---|---  
      
    
    Task<ThemeStartResult> StartTheme( 
       bool _configureHttps_ ,
       string _port_ ,
       Action<string> _exceptionHandler_
    )  
  
#### Parameters

 _configureHttps_
    Determines whether HTTPS should be configured as part of the start up procedure.
_port_
    Optional port number to run the theme on.
_exceptionHandler_
    Optional action to take when an unhandled exception has occurred.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ILiveThemeStarter Interface](topic342.md)   
[ILiveThemeStarter Members](topic343.md)

©2024 DriveWorks Ltd. All Rights Reserved.
