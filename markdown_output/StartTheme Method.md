       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
StartTheme Method   
  
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

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function StartTheme( _
       Optional ByVal _configureHttps_ As Boolean, _
       Optional ByVal _port_ As String, _
       Optional ByVal _exceptionHandler_ As Action(Of String) _
    ) As Task(Of ThemeStartResult)  
  
Visual Basic (Usage)| Copy Code  
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

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ILiveThemeStarter Interface](topic342.md)   
[ILiveThemeStarter Members](topic343.md)


