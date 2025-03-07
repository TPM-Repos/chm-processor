Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ApplicationPluginLoadedEventHandler Delegate   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Extensibility Namespace](topic1995.md) : ApplicationPluginLoadedEventHandler Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sender_
    The sender of the event.

_e_
    The event data.

Glossary Item Box

Represents a method that will handle the [IApplicationPluginManager.ApplicationPluginLoaded](topic2027.md) event. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Sub ApplicationPluginLoadedEventHandler( _
       ByVal _sender_ As Object, _
       ByVal _e_ As EventArgs _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As New [ApplicationPluginLoadedEventHandler](topic2154.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate void ApplicationPluginLoadedEventHandler( 
       object _sender_ ,
       EventArgs _e_
    )  
  
#### Parameters

 _sender_
    The sender of the event.
_e_
    The event data.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ApplicationPluginLoadedEventHandler Members](topic2154.md)   
[DriveWorks.Applications.Extensibility Namespace](topic1995.md)


