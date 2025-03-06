![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
MessageDeleted Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectMessages Class](topic4627.md) : MessageDeleted Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the message is deleted. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event MessageDeleted As [MessageChangedEventHandler](topic5932.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectMessages](topic4627.md)
    Dim handler As [MessageChangedEventHandler](topic5932.md)
     
    AddHandler instance.MessageDeleted, handler  
  
C#|   
---|---  
      
    
    public event [MessageChangedEventHandler](topic5932.md) MessageDeleted  
  
# ![](dotnetimages/collapse.gif)Event Data

The event handler receives an argument of type [MessageEventArgs](topic3704.md) containing data related to this event. The following **MessageEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Message](topic3714.md)| Gets the message that was changed.   
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectMessages Class](topic4627.md)   
[ProjectMessages Members](topic4628.md)


