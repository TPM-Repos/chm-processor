![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ExceptionThrown Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [INotifyExceptionThrown Interface](topic349.md) : ExceptionThrown Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised whenever there is an uncatchable exception thrown. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event ExceptionThrown As [INotifyExceptionThrown.ExceptionThrownEventHandler](topic1269.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [INotifyExceptionThrown](topic349.md)
    Dim handler As [INotifyExceptionThrown.ExceptionThrownEventHandler](topic1269.md)
     
    AddHandler instance.ExceptionThrown, handler  
  
C#|   
---|---  
      
    
    event [INotifyExceptionThrown.ExceptionThrownEventHandler](topic1269.md) ExceptionThrown  
  
# ![](dotnetimages/collapse.gif)Event Data

The event handler receives an argument of type [ExceptionEventArgs](topic806.md) containing data related to this event. The following **ExceptionEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Exception](topic813.md)| Gets the exception to which the event refers.   
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[INotifyExceptionThrown Interface](topic349.md)   
[INotifyExceptionThrown Members](topic350.md)


