![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ConditionCreated Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [Conditions Class](topic10865.md) : ConditionCreated Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Occurs when a condition is created. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event ConditionCreated As [ConditionEventHandler](topic11818.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [Conditions](topic10865.md)
    Dim handler As [ConditionEventHandler](topic11818.md)
     
    AddHandler instance.ConditionCreated, handler  
  
C#|   
---|---  
      
    
    public event [ConditionEventHandler](topic11818.md) ConditionCreated  
  
# ![](dotnetimages/collapse.gif)Event Data

The event handler receives an argument of type [ConditionEventArgs](topic10843.md) containing data related to this event. The following **ConditionEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Condition](topic10853.md)| Gets the condition which is the target of the event.   
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[Conditions Class](topic10865.md)   
[Conditions Members](topic10866.md)


