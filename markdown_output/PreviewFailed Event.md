![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
PreviewFailed Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [PreviewControl Class](topic8709.md) : PreviewFailed Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Event for when model generation fails. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event PreviewFailed As [PreviewControl.PreviewFailedEventHandler](topic9368.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [PreviewControl](topic8709.md)
    Dim handler As [PreviewControl.PreviewFailedEventHandler](topic9368.md)
     
    AddHandler instance.PreviewFailed, handler  
  
C#|   
---|---  
      
    
    public event [PreviewControl.PreviewFailedEventHandler](topic9368.md) PreviewFailed  
  
# ![](dotnetimages/collapse.gif)Event Data

The event handler receives an argument of type [PreviewExceptionEventArgs](topic3811.md) containing data related to this event. The following **PreviewExceptionEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Exception](topic3818.md)| Gets the exception to which the event refers.   
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[PreviewControl Class](topic8709.md)   
[PreviewControl Members](topic8710.md)


