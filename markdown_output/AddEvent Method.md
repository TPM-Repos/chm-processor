![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddEvent Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1863.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [GroupConnectorBase<T> Class](topic1857.md) : AddEvent Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_type_
    The type of event to add.

_description_
    The body of the event entry.

_targetName_
    The target of the current body of work that this event is for.

Glossary Item Box

Adds an event into the application log. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Sub AddEvent( _
       ByVal _type_ As [ApplicationEventType](topic656.md), _
       ByVal _description_ As String, _
       Optional ByVal _targetName_ As String _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [GroupConnectorBase(Of T)](topic1857.md)
    Dim type As [ApplicationEventType](topic656.md)
    Dim description As String
    Dim targetName As String
     
    instance.AddEvent(type, description, targetName)  
  
C#|   
---|---  
      
    
    protected void AddEvent( 
       [ApplicationEventType](topic656.md) _type_ ,
       string _description_ ,
       string _targetName_
    )  
  
#### Parameters

 _type_
    The type of event to add.
_description_
    The body of the event entry.
_targetName_
    The target of the current body of work that this event is for.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupConnectorBase<T> Class](topic1857.md)   
[GroupConnectorBase<T> Members](topic1858.md)

©2024 DriveWorks Ltd. All Rights Reserved.
