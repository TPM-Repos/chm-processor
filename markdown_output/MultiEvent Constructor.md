![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
MultiEvent Constructor   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [MultiEvent Class](topic875.md) : MultiEvent Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_events_
    The events to aggregate.

Glossary Item Box

Initializes a new instance of the [MultiEvent](topic875.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal ParamArray _events_() As [IEvent](topic201.md) _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim events() As [IEvent](topic201.md)
     
    Dim instance As New [MultiEvent](topic875.md)(events)  
  
C#|   
---|---  
      
    
    public MultiEvent( 
       params [IEvent](topic201.md)[] _events_
    )  
  
#### Parameters

 _events_
    The events to aggregate.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[MultiEvent Class](topic875.md)   
[MultiEvent Members](topic876.md)


