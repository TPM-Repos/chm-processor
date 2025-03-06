![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddEvent Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic54.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IApplicationEventService Interface](topic49.md) : AddEvent Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_type_
    The type of the event.

_sourceInvariantName_
    The invariant name of the source of the event (required).

_sourceDisplayName_
    The display name of the source of the event (required).

_description_
    The description of the event (required).

_targetInvariantName_
    The invariant name of the target of the event (optional).

_targetDisplayName_
    The display name of the target of the event (optional).

_url_
    A URL, which may be a local file path, describing a resource containing information relevant to the event (optional).

Glossary Item Box

Adds an event to the event log. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub AddEvent( _
       ByVal _type_ As [ApplicationEventType](topic656.md), _
       ByVal _sourceInvariantName_ As String, _
       ByVal _sourceDisplayName_ As String, _
       ByVal _description_ As String, _
       ByVal _targetInvariantName_ As String, _
       ByVal _targetDisplayName_ As String, _
       ByVal _url_ As String _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IApplicationEventService](topic49.md)
    Dim type As [ApplicationEventType](topic656.md)
    Dim sourceInvariantName As String
    Dim sourceDisplayName As String
    Dim description As String
    Dim targetInvariantName As String
    Dim targetDisplayName As String
    Dim url As String
     
    instance.AddEvent(type, sourceInvariantName, sourceDisplayName, description, targetInvariantName, targetDisplayName, url)  
  
C#|   
---|---  
      
    
    void AddEvent( 
       [ApplicationEventType](topic656.md) _type_ ,
       string _sourceInvariantName_ ,
       string _sourceDisplayName_ ,
       string _description_ ,
       string _targetInvariantName_ ,
       string _targetDisplayName_ ,
       string _url_
    )  
  
#### Parameters

 _type_
    The type of the event.
_sourceInvariantName_
    The invariant name of the source of the event (required).
_sourceDisplayName_
    The display name of the source of the event (required).
_description_
    The description of the event (required).
_targetInvariantName_
    The invariant name of the target of the event (optional).
_targetDisplayName_
    The display name of the target of the event (optional).
_url_
    A URL, which may be a local file path, describing a resource containing information relevant to the event (optional).

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IApplicationEventService Interface](topic49.md)   
[IApplicationEventService Members](topic50.md)

©2024 DriveWorks Ltd. All Rights Reserved.
