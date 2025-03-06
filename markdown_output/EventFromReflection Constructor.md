![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
EventFromReflection Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic805.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [EventFromReflection Class](topic799.md) : EventFromReflection Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_obj_
    The instance of the object on which the event is defined.

_eventName_
    The name of the event.

Glossary Item Box

Initializes a new instance of the [EventFromReflection](topic799.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _obj_ As Object, _
       ByVal _eventName_ As String _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim obj As Object
    Dim eventName As String
     
    Dim instance As New [EventFromReflection](topic799.md)(obj, eventName)  
  
C#|   
---|---  
      
    
    public EventFromReflection( 
       object _obj_ ,
       string _eventName_
    )  
  
#### Parameters

 _obj_
    The instance of the object on which the event is defined.
_eventName_
    The name of the event.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[EventFromReflection Class](topic799.md)   
[EventFromReflection Members](topic800.md)

©2024 DriveWorks Ltd. All Rights Reserved.
