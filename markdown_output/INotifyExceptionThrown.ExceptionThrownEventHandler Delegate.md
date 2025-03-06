![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
INotifyExceptionThrown.ExceptionThrownEventHandler Delegate   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1269.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) : INotifyExceptionThrown.ExceptionThrownEventHandler Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sender_
    The sender of the event.

_e_
    The event information containing the exception.

Glossary Item Box

Represents a method that will handle the [INotifyExceptionThrown.ExceptionThrown](topic354.md) event. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Sub INotifyExceptionThrown.ExceptionThrownEventHandler( _
       ByVal _sender_ As Object, _
       ByVal _e_ As [ExceptionEventArgs](topic806.md) _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As New [INotifyExceptionThrown.ExceptionThrownEventHandler](topic1269.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate void INotifyExceptionThrown.ExceptionThrownEventHandler( 
       object _sender_ ,
       [ExceptionEventArgs](topic806.md) _e_
    )  
  
#### Parameters

 _sender_
    The sender of the event.
_e_
    The event information containing the exception.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[INotifyExceptionThrown.ExceptionThrownEventHandler Members](topic1269.md)   
[DriveWorks.Applications Namespace](topic16.md)

©2024 DriveWorks Ltd. All Rights Reserved.
